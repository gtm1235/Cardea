from .fhirbase import fhirbase


class Contributor(fhirbase):
    """
    A contributor to the content of a knowledge asset, including authors,
    editors, reviewers, and endorsers.
    """

    __name__ = 'Contributor'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The type of contributor.

        type: string
        possible values: author, editor, reviewer, endorser
        """

        self.name = None
        """
        The name of the individual or organization responsible for the
        contribution.

        type: string
        """

        self.contact = None
        """
        Contact details to assist a user in finding and communicating with the
        contributor.

        type: array
        reference to ContactDetail
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'author', 'editor', 'reviewer', 'endorser']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'author, editor, reviewer, endorser'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Contributor',
             'child_variable': 'contact'},
        ]
