from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.SAC import SAC
from ..segments.SID import SID


"""
CONTAINER - OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP
from utils.hl7.v2_5_1.segments import (
    SAC, SID
)

oul_r21_order_observation_group_container_group = OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP(  # CONTAINER - Segment group for OUL_R21_ORDER_OBSERVATION_GROUP - ORDER OBSERVATION consisting of SAC, SID|None
    specimen_container_detail=sac,  # SAC(...)  # Required.
    substance_identifier=None,  # SID(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP TEMPLATE-----
"""


class OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP"""
    _hl7_name = """CONTAINER"""
    _hl7_description = """Segment group for OUL_R21_ORDER_OBSERVATION_GROUP - ORDER OBSERVATION consisting of SAC, SID|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("9", "10")
    _c_components = (SAC, SID)
    _c_name = ("SAC", "SID")
    _c_is_group = (False, False)
    _c_attrs = ("specimen_container_detail", "substance_identifier",)
    # fmt: on

    def __init__(
        self,
        specimen_container_detail: SAC,  #  Required. SAC.9
        substance_identifier: SID | None = None,  #  SID.10
    ):
        """
        None - `OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP>`_
        Segment group for OUL_R21_ORDER_OBSERVATION_GROUP - ORDER OBSERVATION consisting of SAC, SID|None

        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 9 | use: R | rpt: 1)
        :param substance_identifier: Substance Identifier (id: SID | seq: 10 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.specimen_container_detail = specimen_container_detail
        self.substance_identifier = substance_identifier

    @property  # get SAC.9
    def specimen_container_detail(self) -> SAC:
        """
        id: SAC | use: R | rpt: 1 | seq: 9
        ---
        return_type: SAC.9: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[0][0]

    @specimen_container_detail.setter  # set SAC.9
    def specimen_container_detail(self, sac: SAC):
        """
        id: SAC | use: R | rpt: 1 | seq: 9
        ---
        param_type: SAC.9: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        self._c_data[0] = (sac,)

    @property  # get SID.10
    def substance_identifier(self) -> SID | None:
        """
        id: SID | use: O | rpt: 1 | seq: 10
        ---
        return_type: SID.10: Substance Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SID
        """
        return self._c_data[1][0]

    @substance_identifier.setter  # set SID.10
    def substance_identifier(self, sid: SID | None):
        """
        id: SID | use: O | rpt: 1 | seq: 10
        ---
        param_type: SID.10: Substance Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SID
        """
        self._c_data[1] = (sid,)
