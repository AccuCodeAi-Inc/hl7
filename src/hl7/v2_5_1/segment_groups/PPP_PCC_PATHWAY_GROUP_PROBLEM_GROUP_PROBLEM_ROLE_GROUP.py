from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ROL import ROL
from ..segments.VAR import VAR


"""
PROBLEM ROLE - PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
from utils.hl7.v2_5_1.segments import (
    ROL, VAR
)

ppp_pcc_pathway_group_problem_group_problem_role_group = PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP(  # PROBLEM ROLE - Segment group for PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP - PROBLEM consisting of ROL, VAR|None
    role=rol,  # ROL(...)  # Required.
    variance=None,  # VAR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP TEMPLATE-----
"""


class PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP"""
    _hl7_name = """PROBLEM ROLE"""
    _hl7_description = """Segment group for PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP - PROBLEM consisting of ROL, VAR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("14", "15")
    _c_components = (ROL, VAR)
    _c_name = ("ROL", "VAR")
    _c_is_group = (False, False)
    _c_attrs = ("role", "variance",)
    # fmt: on

    def __init__(
        self,
        role: ROL,  #  Required. ROL.14
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.15
    ):
        """
        None - `PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP>`_
        Segment group for PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP - PROBLEM consisting of ROL, VAR|None

        :param role: Role (id: ROL | seq: 14 | use: R | rpt: 1)
        :param variance: Variance (id: VAR | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.role = role
        self.variance = variance

    @property  # get ROL.14
    def role(self) -> ROL:
        """
        id: ROL | use: R | rpt: 1 | seq: 14
        ---
        return_type: ROL.14: Role
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[0][0]

    @role.setter  # set ROL.14
    def role(self, rol: ROL):
        """
        id: ROL | use: R | rpt: 1 | seq: 14
        ---
        param_type: ROL.14: Role
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        self._c_data[0] = (rol,)

    @property  # get VAR
    def variance(self) -> tuple[VAR, ...] | tuple[None]:
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[1]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: VAR.15 | tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        if isinstance(var, tuple):
            self._c_data[1] = var
        else:
            self._c_data[1] = (var,)
