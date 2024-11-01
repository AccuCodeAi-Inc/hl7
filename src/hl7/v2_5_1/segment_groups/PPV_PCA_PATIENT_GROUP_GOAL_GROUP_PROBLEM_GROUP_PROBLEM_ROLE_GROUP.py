from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ROL import ROL
from ..segments.VAR import VAR


"""
PROBLEM ROLE - PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
from utils.hl7.v2_5_1.segments import (
    ROL, VAR
)

ppv_pca_patient_group_goal_group_problem_group_problem_role_group = PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP(  # PROBLEM ROLE - Segment group for PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP - PROBLEM consisting of ROL, VAR|None
    role=rol,  # ROL(...)  # Required.
    variance=None,  # VAR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP TEMPLATE-----
"""


class PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP"""
    _hl7_name = """PROBLEM ROLE"""
    _hl7_description = """Segment group for PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP - PROBLEM consisting of ROL, VAR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("22", "23")
    _c_components = (ROL, VAR)
    _c_name = ("ROL", "VAR")
    _c_is_group = (False, False)
    _c_attrs = ("role", "variance",)
    # fmt: on

    def __init__(
        self,
        role: ROL,  #  Required. ROL.22
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.23
    ):
        """
        None - `PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP>`_
        Segment group for PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP - PROBLEM consisting of ROL, VAR|None

        :param role: Role (id: ROL | seq: 22 | use: R | rpt: 1)
        :param variance: Variance (id: VAR | seq: 23 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.role = role
        self.variance = variance

    @property  # get ROL.22
    def role(self) -> ROL:
        """
        id: ROL | use: R | rpt: 1 | seq: 22
        ---
        return_type: ROL.22: Role
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[0][0]

    @role.setter  # set ROL.22
    def role(self, rol: ROL):
        """
        id: ROL | use: R | rpt: 1 | seq: 22
        ---
        param_type: ROL.22: Role
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        self._c_data[0] = (rol,)

    @property  # get VAR
    def variance(self) -> tuple[VAR, ...] | tuple[None]:
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[1]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        param_type: VAR.23 | tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        if isinstance(var, tuple):
            self._c_data[1] = var
        else:
            self._c_data[1] = (var,)
