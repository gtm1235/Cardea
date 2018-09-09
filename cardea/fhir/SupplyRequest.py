from .fhirbase import fhirbase


class SupplyRequest(fhirbase):
    """
    A record of a request for a medication, substance or device used in
    the healthcare setting.
    """

    __name__ = 'SupplyRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'SupplyRequest'
        """
        This is a SupplyRequest resource

        type: string
        possible values: SupplyRequest
        """

        self.status = None
        """
        Status of the supply request.

        type: string
        possible values: draft, active, suspended, cancelled,
        completed, entered-in-error, unknown
        """

        self.category = None
        """
        Category of supply, e.g.  central, non-stock, etc. This is used to
        support work flows associated with the supply process.

        reference to CodeableConcept
        """

        self.priority = None
        """
        Indicates how quickly this SupplyRequest should be addressed with
        respect to other requests.

        type: string
        """

        self.orderedItem = None
        """
        The item being requested.

        reference to SupplyRequest_OrderedItem
        """

        self.occurrenceDateTime = None
        """
        When the request should be fulfilled.

        type: string
        """

        self.occurrencePeriod = None
        """
        When the request should be fulfilled.

        reference to Period
        """

        self.occurrenceTiming = None
        """
        When the request should be fulfilled.

        reference to Timing
        """

        self.authoredOn = None
        """
        When the request was made.

        type: string
        """

        self.requester = None
        """
        The individual who initiated the request and has responsibility for
        its activation.

        reference to SupplyRequest_Requester
        """

        self.supplier = None
        """
        Who is intended to fulfill the request.

        type: array
        reference to Reference: identifier
        """

        self.reasonCodeableConcept = None
        """
        Why the supply item was requested.

        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Why the supply item was requested.

        reference to Reference: identifier
        """

        self.deliverFrom = None
        """
        Where the supply is expected to come from.

        reference to Reference: identifier
        """

        self.deliverTo = None
        """
        Where the supply is destined to go.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        Unique identifier for this supply request.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'draft', 'active', 'suspended', 'cancelled', 'completed',
                        'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, suspended, cancelled, completed, entered-in-error,'
                        'unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest',
             'child_variable': 'deliverFrom'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest',
             'child_variable': 'supplier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest',
             'child_variable': 'deliverTo'},

            {'parent_entity': 'SupplyRequest_OrderedItem',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'orderedItem'},

            {'parent_entity': 'SupplyRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'category'},
        ]


class SupplyRequest_OrderedItem(fhirbase):
    """
    A record of a request for a medication, substance or device used in
    the healthcare setting.
    """

    __name__ = 'SupplyRequest_OrderedItem'

    def __init__(self, dict_values=None):
        self.quantity = None
        """
        The amount that is being ordered of the indicated item.

        reference to Quantity
        """

        self.itemCodeableConcept = None
        """
        The item that is requested to be supplied. This is either a link to a
        resource representing the details of the item or a code that
        identifies the item from a known list.

        reference to CodeableConcept
        """

        self.itemReference = None
        """
        The item that is requested to be supplied. This is either a link to a
        resource representing the details of the item or a code that
        identifies the item from a known list.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest_OrderedItem',
             'child_variable': 'quantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest_OrderedItem',
             'child_variable': 'itemReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest_OrderedItem',
             'child_variable': 'itemCodeableConcept'},
        ]


class SupplyRequest_Requester(fhirbase):
    """
    A record of a request for a medication, substance or device used in
    the healthcare setting.
    """

    __name__ = 'SupplyRequest_Requester'

    def __init__(self, dict_values=None):
        self.agent = None
        """
        The device, practitioner, etc. who initiated the request.

        reference to Reference: identifier
        """

        self.onBehalfOf = None
        """
        The organization the device or practitioner was acting on behalf of.

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
             'child_entity': 'SupplyRequest_Requester',
             'child_variable': 'agent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest_Requester',
             'child_variable': 'onBehalfOf'},
        ]
