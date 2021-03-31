"""Cardea Core module.

This module defines the Cardea Class, which is responsible for the
tying all components together, as well as the interact with them.
"""
import logging
import os
import pickle
from functools import partial
from inspect import ismethod
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

import featuretools as ft
import pandas as pd

import cardea
from cardea.data_assembling import EntitySetLoader, load_mimic_data
from cardea.data_labeling import DataLabeler
from cardea.featurizing import Featurization
from cardea.modeling import Modeler

LOGGER = logging.getLogger(__name__)

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'data'
)
BUCKET = 'dai-cardea'
S3_URL = 'https://{}.s3.amazonaws.com/{}'


class Cardea():
    """An interface class that ties the end-to-end system together.

    Args:
        es_loader (EntitySetLoader):
            An entityset loader.
        featurization (Featurization):
            A featurization class.
        modeler (Modeler):
            A modeling class.
        problems (list):
            A list of currently available prediction problems.
        chosen_problem (str):
            The selected prediction problem or regression.
        es (featuretools.EntitySet):
            The loaded entityset.
        target_entity (str):
            The target entity for featurization.
    """

    def __init__(self):

        self.es_loader = EntitySetLoader()
        self.featurization = Featurization()

        self.es = None
        self.chosen_problem = None
        self.target_entity = None
        self.modeler = None

    def load_entityset(self, data, fhir=True):
        """Returns an entityset loaded with .csv files in data.

        Load the given dataset into an entityset. The dataset
        must be in FHIR or MIMIC structure format.

        Args:
            data (str):
                A directory of all .csv files that should be loaded. To load demo dataset,
                pass the name of the dataset "kaggle" or "mimic".

        Returns:
            featuretools.EntitySet:
                An entityset with loaded data.
        """
        demo = ['kaggle', 'mimic']
        if not os.path.exists(data) and data in demo:
            path = self.download_demo(data)

        if data == "kaggle":
            self.es = self.es_loader.load_data_entityset(path)
        elif data == "mimic":
            self.es = load_mimic_data(path)

    @staticmethod
    def download_demo(name, data_path=DATA_PATH):
        data_path = os.path.join(data_path, name)
        os.makedirs(data_path, exist_ok=True)

        url = S3_URL.format(BUCKET, '{}.zip'.format(name))
        compressed = ZipFile(BytesIO(urlopen(url).read()))

        LOGGER.info('Downloading dataset %s from %s', name, url)
        for file in compressed.namelist():
            filename = os.path.join(data_path, file)
            csv_file = compressed.open(file, 'r')

            data = pd.read_csv(csv_file, dtype=str, encoding="utf-8")
            data.to_csv(filename, index=False)

        return data_path

    def list_problems(self):
        """Returns a list of the currently available problems.

        Returns:
            list:
                A list of the available problems.
        """

        problems = set([])
        for attribute_string in dir(cardea.data_labeling):
            attribute = getattr(cardea.data_labeling, attribute_string)
            if ismethod(attribute):
                problems.add(attribute.__name__)

        return problems

    def select_problem(self, function, parameter=None, **kwargs):
        """Select a prediction problem and extract information.

        Update the select_problem attribute and generate the cutoff times,
        the target entity and update the entityset.

        Args:
            function (method):
                function that defines the prediction task, it should return a
                tuple of labeling function, the dataframe, and the name of the
                target entity.
            parameter (dict):
                Variables to change the default parameters, if any.

        Returns:
            featuretools.EntitySet, str, pandas.DataFrame:
                * An updated EntitySet if a new column is generated.
                * A string indicating the selected target entity.
                * A dataframe of cutoff times and their target labels.
        """
        LOGGER.info("Selecting %s prediction problem", str(function))

        if parameter:
            function = partial(function, parameter)

        data_labeler = DataLabeler(function)

        # target label calculation
        label_times, self.target_entity, self.prediction_type = data_labeler.generate_label_times(
            self.es)

        # set default pipeline
        if self.prediction_type == "classification":
            pipeline = "Random Forest"
        else:
            pipeline = "Random Forest Regressor"

        self.modeler = Modeler(pipeline, self.prediction_type)

        return label_times

    def list_feature_primitives(self):
        """Returns built-in primitive in Featuretools.

        Returns:
            pandas.DataFrame:
                A dataframe that lists and describes each built-in primitives.
        """
        return ft.list_primitives()

    def generate_features(self, label_times, verbose=False):
        """Returns a the calculated feature matrix.

        Args:
            es (featuretools.EntitySet):
                An entityset that holds data.
            label_times (pandas.DataFrame):
                A dataframe that indicates cutoff time for each instance.

        Returns:
            pandas.DataFrame, list:
              * The generated feature matrix.
              * List of feature definitions in the feature matrix.
        """

        fm_encoded, _ = self.featurization.generate_feature_matrix(
            self.es, self.target_entity, label_times, verbose=verbose)
        fm_encoded = fm_encoded.reset_index(drop=True)
        return fm_encoded

    def select_pipeline(self, pipeline):
        """Select a pipeline.

        Args:
            pipeline (MLPipeline or str):
                A pipeline instance or the name/path of a pipeline.
        """
        LOGGER.info("Selecting %s pipeline", pipeline)
        self.modeler = Modeler(pipeline, self.prediction_type)

    def train_test_split(self, X, y, test_size, shuffle):
        """Split the training dataset and the testing dataset.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series or ndarray):
                Target values.
            test_size (float):
                The proportion of the dataset to include in the test dataset.
            shuffle (bool):
                Whether or not to shuffle the data before splitting.

        Returns:
            list:
                List containing the train-test split of the inputs and targets.
        """
        return self.modeler.train_test_split(X, y, test_size, shuffle)

    def fit(self, X, y, tune=False, max_evals=10, scoring=None, verbose=False):
        """Train the cardea pipeline.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series ndarray):
                Target values.
            tune (bool):
                Whether to optimize hyper-parameters of the pipelines.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function used in the hyper-parameter optimization.
            verbose (bool):
                Whether to log information during processing.
        """
        self.modeler.fit(X, y, tune, max_evals, scoring, verbose)

    def predict(self, X):
        """Get predictions from the cardea pipeline.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.

        Returns:
            ndarray:
                Predictions to the input data.
        """
        return self.modeler.predict(X)

    def fit_predict(self, X, y, tune=False, max_evals=10, scoring=None, verbose=False):
        """Train a cardea pipeline then make predictions.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series or ndarray):
                Target values.
            tune (bool):
                Whether to optimize hyper-parameters of the pipelines.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function used in the hyper-parameter optimization.
            verbose (bool):
                Whether to log information during processing.

        Returns:
            ndarray:
                Predictions to the input data.
        """
        return self.modeler.fit_predict(X, y, tune, max_evals, scoring, verbose)

    def evaluate(self, X, y, test_size=0.2, shuffle=True, tune=False, max_evals=10, scoring=None,
                 metrics=None, verbose=False):
        """Evaluate the cardea pipeline.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series or ndarray):
                Target values.
            test_size (float):
                The proportion of the dataset to include in the test dataset.
            shuffle (bool):
                Whether or not to shuffle the data before splitting.
            tune (bool):
                Whether to optimize hyper-parameters of the pipelines.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function used in the hyper-parameter optimization.
            metrics (list):
                A list of scoring function names. The scoring functions should be consistent
                with the problem type.
            verbose (bool):
                Whether to log information during processing.
        """
        return self.modeler.evaluate(
            X, y, test_size, shuffle, tune, max_evals, scoring, metrics, verbose)

    def save(self, path):
        """Save this object using pickle.

        Args:
            path (str):
                Path to the file where the serialization of
                this object will be stored.
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as pickle_file:
            pickle.dump(self, pickle_file)

    @classmethod
    def load(cls, path: str):
        """Load an Orion instance from a pickle file.

        Args:
            path (str):
                Path to the file where the instance has been
                previously serialized.

        Returns:
            Cardea:
                A Cardea instance

        Raises:
            ValueError:
                If the serialized object is not an Cardea instance.
        """
        with open(path, 'rb') as pickle_file:
            cardea = pickle.load(pickle_file)
            if not isinstance(cardea, cls):
                raise ValueError('Serialized object is not a Cardea instance')

            return cardea
