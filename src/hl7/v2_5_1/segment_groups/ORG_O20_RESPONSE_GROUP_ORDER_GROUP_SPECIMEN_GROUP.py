from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.SAC import SAC
from ..segments.SPM import SPM


"""
SPECIMEN - ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    SPM, SAC
)

org_o20_response_group_order_group_specimen_group = ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP(  # SPECIMEN - Segment group for ORG_O20_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of SPM, SAC|None
    specimen=spm,  # SPM(...)  # Required.
    specimen_container_detail=None,  # SAC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP TEMPLATE-----
"""


class ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for ORG_O20_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of SPM, SAC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("14", "15")
    _c_components = (SPM, SAC)
    _c_name = ("SPM", "SAC")
    _c_is_group = (False, False)
    _c_attrs = ("specimen", "specimen_container_detail",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.14
        specimen_container_detail: SAC | tuple[SAC, ...] | None = None,  #  SAC.15
    ):
        """
        None - `ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP>`_
        Segment group for ORG_O20_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of SPM, SAC|None

        :param specimen: Specimen (id: SPM | seq: 14 | use: R | rpt: 1)
        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.specimen = specimen
        self.specimen_container_detail = specimen_container_detail

    @property  # get SPM.14
    def specimen(self) -> SPM:
        """
        id: SPM | use: R | rpt: 1 | seq: 14
        ---
        return_type: SPM.14: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.14
    def specimen(self, spm: SPM):
        """
        id: SPM | use: R | rpt: 1 | seq: 14
        ---
        param_type: SPM.14: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get SAC
    def specimen_container_detail(self) -> tuple[SAC, ...] | tuple[None]:
        """
        id: SAC SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[SAC, ...]: (Specimen Container detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[1]

    @specimen_container_detail.setter  # set SAC
    def specimen_container_detail(self, sac: SAC | tuple[SAC, ...] | None):
        """
        id: SAC SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: SAC.15 | tuple[SAC, ...]: (Specimen Container detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        if isinstance(sac, tuple):
            self._c_data[1] = sac
        else:
            self._c_data[1] = (sac,)
