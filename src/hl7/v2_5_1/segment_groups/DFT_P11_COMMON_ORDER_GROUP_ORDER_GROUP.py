from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.OBR import OBR


"""
ORDER - DFT_P11_COMMON_ORDER_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::DFT_P11_COMMON_ORDER_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import DFT_P11_COMMON_ORDER_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR, NTE
)

dft_p11_common_order_group_order_group = DFT_P11_COMMON_ORDER_GROUP_ORDER_GROUP(  # ORDER - Segment group for DFT_P11_COMMON_ORDER_GROUP - COMMON ORDER consisting of OBR, NTE|None
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::DFT_P11_COMMON_ORDER_GROUP_ORDER_GROUP TEMPLATE-----
"""


class DFT_P11_COMMON_ORDER_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """DFT_P11_COMMON_ORDER_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for DFT_P11_COMMON_ORDER_GROUP - COMMON ORDER consisting of OBR, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P11_COMMON_ORDER_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("14", "15")
    _c_components = (OBR, NTE)
    _c_name = ("OBR", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("observation_request", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.14
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.15
    ):
        """
        None - `DFT_P11_COMMON_ORDER_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P11_COMMON_ORDER_GROUP_ORDER_GROUP>`_
        Segment group for DFT_P11_COMMON_ORDER_GROUP - COMMON ORDER consisting of OBR, NTE|None

        :param observation_request: Observation Request (id: OBR | seq: 14 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments

    @property  # get OBR.14
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 14
        ---
        return_type: OBR.14: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[0][0]

    @observation_request.setter  # set OBR.14
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 14
        ---
        param_type: OBR.14: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[0] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: NTE.15 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
