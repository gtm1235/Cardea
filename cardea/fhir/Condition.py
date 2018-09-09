from .fhirbase import fhirbase


class Condition(fhirbase):
    """
    A clinical condition, problem, diagnosis, or other event, situation,
    issue, or clinical concept that has risen to a level of concern.
    """

    __name__ = 'Condition'

    def __init__(self, dict_values=None):
        self.resourceType = 'Condition'
        """
        This is a Condition resource

        type: string
        possible values: Condition
        """

        self.clinicalStatus = None
        """
        The clinical status of the condition.

        type: string
        """

        self.verificationStatus = None
        """
        The verification status to support the clinical status of the
        condition.

        type: string
        possible values: provisional, differential, confirmed,
        refuted, entered-in-error, unknown
        """

        self.category = None
        """
        A category assigned to the condition.

        type: array
        reference to CodeableConcept
        """

        self.severity = None
        """
        A subjective assessment of the severity of the condition as evaluated
        by the clinician.

        reference to CodeableConcept
        """

        self.code = None
        """
        Identification of the condition, problem or diagnosis.

        reference to CodeableConcept
        """

        self.bodySite = None
        """
        The anatomical location where this condition manifests itself.

        type: array
        reference to CodeableConcept
        """

        self.subject = None
        """
        Indicates the patient or group who the condition record is associated
        with.

        reference to Reference: identifier
        """

        self.context = None
        """
        Encounter during which the condition was first asserted.

        reference to Reference: identifier
        """

        self.onsetDateTime = None
        """
        Estimated or actual date or date-time  the condition began, in the
        opinion of the clinician.

        type: string
        """

        self.onsetAge = None
        """
        Estimated or actual date or date-time  the condition began, in the
        opinion of the clinician.

        reference to Age
        """

        self.onsetPeriod = None
        """
        Estimated or actual date or date-time  the condition began, in the
        opinion of the clinician.

        reference to Period
        """

        self.onsetRange = None
        """
        Estimated or actual date or date-time  the condition began, in the
        opinion of the clinician.

        reference to Range
        """

        self.onsetString = None
        """
        Estimated or actual date or date-time  the condition began, in the
        opinion of the clinician.

        type: string
        """

        self.abatementDateTime = None
        """
        The date or estimated date that the condition resolved or went into
        remission. This is called "abatement" because of the many overloaded
        connotations associated with "remission" or "resolution" - Conditions
        are never really resolved, but they can abate.

        type: string
        """

        self.abatementAge = None
        """
        The date or estimated date that the condition resolved or went into
        remission. This is called "abatement" because of the many overloaded
        connotations associated with "remission" or "resolution" - Conditions
        are never really resolved, but they can abate.

        reference to Age
        """

        self.abatementBoolean = None
        """
        The date or estimated date that the condition resolved or went into
        remission. This is called "abatement" because of the many overloaded
        connotations associated with "remission" or "resolution" - Conditions
        are never really resolved, but they can abate.

        type: boolean
        """

        self.abatementPeriod = None
        """
        The date or estimated date that the condition resolved or went into
        remission. This is called "abatement" because of the many overloaded
        connotations associated with "remission" or "resolution" - Conditions
        are never really resolved, but they can abate.

        reference to Period
        """

        self.abatementRange = None
        """
        The date or estimated date that the condition resolved or went into
        remission. This is called "abatement" because of the many overloaded
        connotations associated with "remission" or "resolution" - Conditions
        are never really resolved, but they can abate.

        reference to Range
        """

        self.abatementString = None
        """
        The date or estimated date that the condition resolved or went into
        remission. This is called "abatement" because of the many overloaded
        connotations associated with "remission" or "resolution" - Conditions
        are never really resolved, but they can abate.

        type: string
        """

        self.assertedDate = None
        """
        The date on which the existance of the Condition was first asserted or
        acknowledged.

        type: string
        """

        self.asserter = None
        """
        Individual who is making the condition statement.

        reference to Reference: identifier
        """

        self.stage = None
        """
        Clinical stage or grade of a condition. May include formal severity
        assessments.

        reference to Condition_Stage
        """

        self.evidence = None
        """
        Supporting Evidence / manifestations that are the basis on which this
        condition is suspected or confirmed.

        type: array
        reference to Condition_Evidence
        """

        self.note = None
        """
        Additional information about the Condition. This is a general
        notes/comments entry  for description of the Condition, its diagnosis
        and prognosis.

        type: array
        reference to Annotation
        """

        self.identifier = None
        """
        This records identifiers associated with this condition that are
        defined by business processes and/or used to refer to it when a direct
        URL reference to the resource itself is not appropriate (e.g. in CDA
        documents, or in written / printed documentation).

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.verificationStatus is not None:
            for value in self.verificationStatus:
                if value is not None and value.lower() not in [
                    'provisional', 'differential', 'confirmed', 'refuted',
                        'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'provisional, differential, confirmed, refuted, entered-in-error,'
                        'unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'severity'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'onsetAge'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition',
             'child_variable': 'asserter'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'abatementPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'category'},

            {'parent_entity': 'Condition_Stage',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'stage'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition',
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'onsetPeriod'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'onsetRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'code'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'abatementAge'},

            {'parent_entity': 'Condition_Evidence',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'evidence'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'identifier'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'abatementRange'},
        ]


class Condition_Stage(fhirbase):
    """
    A clinical condition, problem, diagnosis, or other event, situation,
    issue, or clinical concept that has risen to a level of concern.
    """

    __name__ = 'Condition_Stage'

    def __init__(self, dict_values=None):
        self.summary = None
        """
        A simple summary of the stage such as "Stage 3". The determination of
        the stage is disease-specific.

        reference to CodeableConcept
        """

        self.assessment = None
        """
        Reference to a formal record of the evidence on which the staging
        assessment is based.

        type: array
        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition_Stage',
             'child_variable': 'assessment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition_Stage',
             'child_variable': 'summary'},
        ]


class Condition_Evidence(fhirbase):
    """
    A clinical condition, problem, diagnosis, or other event, situation,
    issue, or clinical concept that has risen to a level of concern.
    """

    __name__ = 'Condition_Evidence'

    def __init__(self, dict_values=None):
        self.code = None
        """
        A manifestation or symptom that led to the recording of this
        condition.

        type: array
        reference to CodeableConcept
        """

        self.detail = None
        """
        Links to other relevant information, including pathology reports.

        type: array
        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition_Evidence',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition_Evidence',
             'child_variable': 'detail'},
        ]
