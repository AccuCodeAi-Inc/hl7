from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ROL import ROL
from ..segments.CER import CER


"""
CERTIFICATE - PMU_B07_CERTIFICATE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PMU_B07_CERTIFICATE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PMU_B07_CERTIFICATE_GROUP
from utils.hl7.v2_5_1.segments import (
    CER, ROL
)

pmu_b07_certificate_group = PMU_B07_CERTIFICATE_GROUP(  # CERTIFICATE - Segment group for PMU_B07 - Add personnel record consisting of CER, ROL|None
    certificate_detail=cer,  # CER(...)  # Required.
    role=None,  # ROL(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PMU_B07_CERTIFICATE_GROUP TEMPLATE-----
"""


class PMU_B07_CERTIFICATE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PMU_B07_CERTIFICATE_GROUP"""
    _hl7_name = """CERTIFICATE"""
    _hl7_description = """Segment group for PMU_B07 - Add personnel record consisting of CER, ROL|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PMU_B07_CERTIFICATE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("6", "7")
    _c_components = (CER, ROL)
    _c_name = ("CER", "ROL")
    _c_is_group = (False, False)
    _c_attrs = ("certificate_detail", "role",)
    # fmt: on

    def __init__(
        self,
        certificate_detail: CER,  #  Required. CER.6
        role: ROL | tuple[ROL, ...] | None = None,  #  ROL.7
    ):
        """
        None - `PMU_B07_CERTIFICATE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PMU_B07_CERTIFICATE_GROUP>`_
        Segment group for PMU_B07 - Add personnel record consisting of CER, ROL|None

        :param certificate_detail: Certificate Detail (id: CER | seq: 6 | use: R | rpt: 1)
        :param role: Role (id: ROL | seq: 7 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.certificate_detail = certificate_detail
        self.role = role

    @property  # get CER.6
    def certificate_detail(self) -> CER:
        """
        id: CER | use: R | rpt: 1 | seq: 6
        ---
        return_type: CER.6: Certificate Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CER
        """
        return self._c_data[0][0]

    @certificate_detail.setter  # set CER.6
    def certificate_detail(self, cer: CER):
        """
        id: CER | use: R | rpt: 1 | seq: 6
        ---
        param_type: CER.6: Certificate Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CER
        """
        self._c_data[0] = (cer,)

    @property  # get ROL
    def role(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[1]

    @role.setter  # set ROL
    def role(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: ROL.7 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[1] = rol
        else:
            self._c_data[1] = (rol,)
