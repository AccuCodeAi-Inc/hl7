from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXO import RXO
from ..segments.NTE import NTE
from ..segments.RXR import RXR
from ..segment_groups.RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP import (
    RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP,
)


"""
ORDER DETAIL - RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    RXO, RXR, NTE
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP
)

rsp_z82_query_response_group_common_order_group_order_detail_group = RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP(  # ORDER DETAIL - Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXO, NTE|None, RXR, TREATMENT|None
    pharmacy_or_treatment_order=rxo,  # RXO(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    treatment=None,  # RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----
"""


class RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _hl7_name = """ORDER DETAIL"""
    _hl7_description = """Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXO, NTE|None, RXR, TREATMENT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("17", "18", "19", "None")
    _c_components = (RXO, NTE, RXR, RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP)
    _c_name = ("RXO", "NTE", "RXR", "TREATMENT")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("pharmacy_or_treatment_order", "notes_and_comments", "pharmacy_or_treatment_route", "treatment",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_order: RXO,  #  Required. RXO.17
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.19
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.18
        treatment: RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP
        | None = None,  #  RXC.20, NTE.21
    ):
        """
        None - `RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP>`_
        Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXO, NTE|None, RXR, TREATMENT|None

        :param pharmacy_or_treatment_order: Pharmacy/Treatment Order (id: RXO | seq: 17 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 18 | use: O | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 19 | use: R | rpt: *)
        :param treatment: Treatment segment group: [RXC, NTE|None] (id: TREATMENT | seq: 20, 21 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.pharmacy_or_treatment_order = pharmacy_or_treatment_order
        self.notes_and_comments = notes_and_comments
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.treatment = treatment

    @property  # get RXO.17
    def pharmacy_or_treatment_order(self) -> RXO:
        """
        id: RXO | use: R | rpt: 1 | seq: 17
        ---
        return_type: RXO.17: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_order.setter  # set RXO.17
    def pharmacy_or_treatment_order(self, rxo: RXO):
        """
        id: RXO | use: R | rpt: 1 | seq: 17
        ---
        param_type: RXO.17: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        self._c_data[0] = (rxo,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        param_type: NTE.18 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 19
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[2]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 19
        ---
        param_type: RXR.19 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[2] = rxr
        else:
            self._c_data[2] = (rxr,)

    @property  # get RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP.None
    def treatment(
        self,
    ) -> (
        RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP
        | None
    ):
        """
        id: RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP
        """
        return self._c_data[3][0]

    @treatment.setter  # set RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP.None
    def treatment(
        self,
        treatment: RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP
        | None,
    ):
        """
        id: RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP
        """
        self._c_data[3] = (treatment,)
