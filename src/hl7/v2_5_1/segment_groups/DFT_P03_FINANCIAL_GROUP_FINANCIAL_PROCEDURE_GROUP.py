from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PR1 import PR1
from ..segments.ROL import ROL


"""
FINANCIAL PROCEDURE - DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
from utils.hl7.v2_5_1.segments import (
    ROL, PR1
)

dft_p03_financial_group_financial_procedure_group = DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP(  # FINANCIAL PROCEDURE - Segment group for DFT_P03_FINANCIAL_GROUP - FINANCIAL consisting of PR1, ROL|None
    procedures=pr1,  # PR1(...)  # Required.
    role=None,  # ROL(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP TEMPLATE-----
"""


class DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP"""
    _hl7_name = """FINANCIAL PROCEDURE"""
    _hl7_description = """Segment group for DFT_P03_FINANCIAL_GROUP - FINANCIAL consisting of PR1, ROL|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("20", "21")
    _c_components = (PR1, ROL)
    _c_name = ("PR1", "ROL")
    _c_is_group = (False, False)
    _c_attrs = ("procedures", "role",)
    # fmt: on

    def __init__(
        self,
        procedures: PR1,  #  Required. PR1.20
        role: ROL | tuple[ROL, ...] | None = None,  #  ROL.21
    ):
        """
        None - `DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP>`_
        Segment group for DFT_P03_FINANCIAL_GROUP - FINANCIAL consisting of PR1, ROL|None

        :param procedures: Procedures (id: PR1 | seq: 20 | use: R | rpt: 1)
        :param role: Role (id: ROL | seq: 21 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.procedures = procedures
        self.role = role

    @property  # get PR1.20
    def procedures(self) -> PR1:
        """
        id: PR1 | use: R | rpt: 1 | seq: 20
        ---
        return_type: PR1.20: Procedures
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1
        """
        return self._c_data[0][0]

    @procedures.setter  # set PR1.20
    def procedures(self, pr1: PR1):
        """
        id: PR1 | use: R | rpt: 1 | seq: 20
        ---
        param_type: PR1.20: Procedures
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1
        """
        self._c_data[0] = (pr1,)

    @property  # get ROL
    def role(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[1]

    @role.setter  # set ROL
    def role(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        param_type: ROL.21 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[1] = rol
        else:
            self._c_data[1] = (rol,)
