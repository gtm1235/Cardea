from __future__ import absolute_import

import pandas as pd


class fhirbase(object):

    def set_attributes(self, dict_values):
        """Set values to class attributes."""

        for attr, _ in self.__dict__.items():
            if attr in dict_values.keys():
                self.__dict__[str(attr)] = dict_values[str(attr)]

    def get_dataframe(self):
        """Return dataframe from class attribute values."""
        dataframe = {}
        for attr, value in self.__dict__.items():
            if value is not None and attr != 'resourceType':
                dataframe[attr] = value

        return pd.DataFrame(dataframe)

    def get_id(self):
        """Return class identifier."""
        if hasattr(self, 'identifier') and getattr(self, 'identifier') is not None:
            return 'identifier'
        elif hasattr(self, 'id') and getattr(self, 'id') is not None:
            return 'id'
        elif hasattr(self, 'object_id') and getattr(self, 'object_id') is not None:
            return 'object_id'
        else:
            raise LookupError('{} is missing an identifier column'.format(self.__name__))

    def assert_type(self):
        """Return class values follow set possible enumerations."""

    def get_relationships(self):
        """Return class relationships."""
        return []

    def get_eligible_relationships(self):
        """Return class relationships for attributes that are used."""

        all_relationships = self.get_relationships()
        eligible = [
            relation for relation in all_relationships if getattr(
                self, relation['child_variable']) is not None]
        return eligible
