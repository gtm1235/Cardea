from .fhirbase import fhirbase


class RelatedArtifact(fhirbase):
    """
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """

    __name__ = 'RelatedArtifact'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The type of relationship to the related artifact.

        type: string
        possible values: documentation, justification, citation,
        predecessor, successor, derived-from, depends-on, composed-of
        """

        self.display = None
        """
        A brief description of the document or knowledge resource being
        referenced, suitable for display to a consumer.

        type: string
        """

        self.citation = None
        """
        A bibliographic citation for the related artifact. This text SHOULD be
        formatted according to an accepted citation format.

        type: string
        """

        self.url = None
        """
        A url for the artifact that can be followed to access the actual
        content.

        type: string
        """

        self.document = None
        """
        The document being referenced, represented as an attachment. This is
        exclusive with the resource element.

        reference to Attachment
        """

        self.resource = None
        """
        The related resource, such as a library, value set, profile, or other
        knowledge resource.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'documentation', 'justification', 'citation', 'predecessor',
                        'successor', 'derived-from', 'depends-on', 'composed-of']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'documentation, justification, citation, predecessor, successor,'
                        'derived-from, depends-on, composed-of'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RelatedArtifact',
             'child_variable': 'resource'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedArtifact',
             'child_variable': 'document'},
        ]
