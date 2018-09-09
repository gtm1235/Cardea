from .fhirbase import fhirbase


class Provenance(fhirbase):
    """
    Provenance of a resource is a record that describes entities and
    processes involved in producing and delivering or otherwise
    influencing that resource. Provenance provides a critical foundation
    for assessing authenticity, enabling trust, and allowing
    reproducibility. Provenance assertions are a form of contextual
    metadata and can themselves become important records with their own
    provenance. Provenance statement indicates clinical significance in
    terms of confidence in authenticity, reliability, and trustworthiness,
    integrity, and stage in lifecycle (e.g. Document Completion - has the
    artifact been legally authenticated), all of which may impact
    security, privacy, and trust policies.
    """

    __name__ = 'Provenance'

    def __init__(self, dict_values=None):
        self.resourceType = 'Provenance'
        """
        This is a Provenance resource

        type: string
        possible values: Provenance
        """

        self.target = None
        """
        The Reference(s) that were generated or updated by  the activity
        described in this resource. A provenance can point to more than one
        target if multiple resources were created/updated by the same
        activity.

        type: array
        reference to Reference: identifier
        """

        self.period = None
        """
        The period during which the activity occurred.

        reference to Period
        """

        self.recorded = None
        """
        The instant of time at which the activity was recorded.

        type: string
        """

        self.policy = None
        """
        Policy or plan the activity was defined by. Typically, a single
        activity may have multiple applicable policy documents, such as
        patient consent, guarantor funding, etc.

        type: array
        """

        self.location = None
        """
        Where the activity occurred, if relevant.

        reference to Reference: identifier
        """

        self.reason = None
        """
        The reason that the activity was taking place.

        type: array
        reference to Coding
        """

        self.activity = None
        """
        An activity is something that occurs over a period of time and acts
        upon or with entities; it may include consuming, processing,
        transforming, modifying, relocating, using, or generating entities.

        reference to Coding
        """

        self.agent = None
        """
        An actor taking a role in an activity  for which it can be assigned
        some degree of responsibility for the activity taking place.

        type: array
        reference to Provenance_Agent
        """

        self.entity = None
        """
        An entity used in this activity.

        type: array
        reference to Provenance_Entity
        """

        self.signature = None
        """
        A digital signature on the target Reference(s). The signer should
        match a Provenance.agent. The purpose of the signature is indicated.

        type: array
        reference to Signature
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Provenance',
             'child_variable': 'signature'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Provenance',
             'child_variable': 'period'},

            {'parent_entity': 'Provenance_Entity',
             'parent_variable': 'object_id',
             'child_entity': 'Provenance',
             'child_variable': 'entity'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Provenance',
             'child_variable': 'activity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Provenance',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Provenance',
             'child_variable': 'target'},

            {'parent_entity': 'Provenance_Agent',
             'parent_variable': 'object_id',
             'child_entity': 'Provenance',
             'child_variable': 'agent'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Provenance',
             'child_variable': 'reason'},
        ]


class Provenance_Agent(fhirbase):
    """
    Provenance of a resource is a record that describes entities and
    processes involved in producing and delivering or otherwise
    influencing that resource. Provenance provides a critical foundation
    for assessing authenticity, enabling trust, and allowing
    reproducibility. Provenance assertions are a form of contextual
    metadata and can themselves become important records with their own
    provenance. Provenance statement indicates clinical significance in
    terms of confidence in authenticity, reliability, and trustworthiness,
    integrity, and stage in lifecycle (e.g. Document Completion - has the
    artifact been legally authenticated), all of which may impact
    security, privacy, and trust policies.
    """

    __name__ = 'Provenance_Agent'

    def __init__(self, dict_values=None):
        self.role = None
        """
        The function of the agent with respect to the activity. The security
        role enabling the agent with respect to the activity.

        type: array
        reference to CodeableConcept
        """

        self.whoUri = None
        """
        The individual, device or organization that participated in the event.

        type: string
        """

        self.whoReference = None
        """
        The individual, device or organization that participated in the event.

        reference to Reference: identifier
        """

        self.onBehalfOfUri = None
        """
        The individual, device, or organization for whom the change was made.

        type: string
        """

        self.onBehalfOfReference = None
        """
        The individual, device, or organization for whom the change was made.

        reference to Reference: identifier
        """

        self.relatedAgentType = None
        """
        The type of relationship between agents.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Provenance_Agent',
             'child_variable': 'whoReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Provenance_Agent',
             'child_variable': 'onBehalfOfReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Provenance_Agent',
             'child_variable': 'relatedAgentType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Provenance_Agent',
             'child_variable': 'role'},
        ]


class Provenance_Entity(fhirbase):
    """
    Provenance of a resource is a record that describes entities and
    processes involved in producing and delivering or otherwise
    influencing that resource. Provenance provides a critical foundation
    for assessing authenticity, enabling trust, and allowing
    reproducibility. Provenance assertions are a form of contextual
    metadata and can themselves become important records with their own
    provenance. Provenance statement indicates clinical significance in
    terms of confidence in authenticity, reliability, and trustworthiness,
    integrity, and stage in lifecycle (e.g. Document Completion - has the
    artifact been legally authenticated), all of which may impact
    security, privacy, and trust policies.
    """

    __name__ = 'Provenance_Entity'

    def __init__(self, dict_values=None):
        self.role = None
        """
        How the entity was used during the activity.

        type: string
        possible values: derivation, revision, quotation, source,
        removal
        """

        self.whatUri = None
        """
        Identity of the  Entity used. May be a logical or physical uri and
        maybe absolute or relative.

        type: string
        """

        self.whatReference = None
        """
        Identity of the  Entity used. May be a logical or physical uri and
        maybe absolute or relative.

        reference to Reference: identifier
        """

        self.whatIdentifier = None
        """
        Identity of the  Entity used. May be a logical or physical uri and
        maybe absolute or relative.

        reference to Identifier
        """

        self.agent = None
        """
        The entity is attributed to an agent to express the agent's
        responsibility for that entity, possibly along with other agents. This
        description can be understood as shorthand for saying that the agent
        was responsible for the activity which generated the entity.

        type: array
        reference to Provenance_Agent
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.role is not None:
            for value in self.role:
                if value is not None and value.lower() not in [
                        'derivation', 'revision', 'quotation', 'source', 'removal']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'derivation, revision, quotation, source, removal'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Provenance_Agent',
             'parent_variable': 'object_id',
             'child_entity': 'Provenance_Entity',
             'child_variable': 'agent'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Provenance_Entity',
             'child_variable': 'whatIdentifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Provenance_Entity',
             'child_variable': 'whatReference'},
        ]
