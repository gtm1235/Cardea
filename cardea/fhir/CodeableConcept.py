from .fhirbase import fhirbase


class CodeableConcept(fhirbase):
    """
    A concept that may be defined by a formal reference to a terminology
    or ontology or may be provided by text.
    """

    __name__ = 'CodeableConcept'

    def __init__(self, dict_values=None):
        self.coding = None
        """
        A reference to a code defined by a terminology system.

        type: array
        reference to Coding
        """

        self.text = None
        """
        A human language representation of the concept as
        seen/selected/uttered by the user who entered the data and/or which
        represents the intended meaning of the user.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'CodeableConcept',
             'child_variable': 'coding'},
        ]
