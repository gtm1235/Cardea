from .fhirbase import fhirbase


class Annotation(fhirbase):
    """
    A  text note which also  contains information about who made the
    statement and when.
    """

    __name__ = 'Annotation'

    def __init__(self, dict_values=None):
        self.authorReference = None
        """
        The individual responsible for making the annotation.

        reference to Reference: identifier
        """

        self.authorString = None
        """
        The individual responsible for making the annotation.

        type: string
        """

        self.time = None
        """
        Indicates when this particular annotation was made.

        type: string
        """

        self.text = None
        """
        The text of the annotation.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Annotation',
             'child_variable': 'authorReference'},
        ]
