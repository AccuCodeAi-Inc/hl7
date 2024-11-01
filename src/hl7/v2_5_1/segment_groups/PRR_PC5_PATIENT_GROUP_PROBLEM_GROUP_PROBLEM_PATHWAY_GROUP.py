from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.VAR import VAR
from ..segments.PTH import PTH


"""
PROBLEM PATHWAY - PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP
from utils.hl7.v2_5_1.segments import (
    PTH, VAR
)

prr_pc5_patient_group_problem_group_problem_pathway_group = PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP(  # PROBLEM PATHWAY - Segment group for PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP - PROBLEM consisting of PTH, VAR|None
    pathway=pth,  # PTH(...)  # Required.
    variance=None,  # VAR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP TEMPLATE-----
"""


class PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP"""
    _hl7_name = """PROBLEM PATHWAY"""
    _hl7_description = """Segment group for PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP - PROBLEM consisting of PTH, VAR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("15", "16")
    _c_components = (PTH, VAR)
    _c_name = ("PTH", "VAR")
    _c_is_group = (False, False)
    _c_attrs = ("pathway", "variance",)
    # fmt: on

    def __init__(
        self,
        pathway: PTH,  #  Required. PTH.15
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.16
    ):
        """
        None - `PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP>`_
        Segment group for PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP - PROBLEM consisting of PTH, VAR|None

        :param pathway: Pathway (id: PTH | seq: 15 | use: R | rpt: 1)
        :param variance: Variance (id: VAR | seq: 16 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.pathway = pathway
        self.variance = variance

    @property  # get PTH.15
    def pathway(self) -> PTH:
        """
        id: PTH | use: R | rpt: 1 | seq: 15
        ---
        return_type: PTH.15: Pathway
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTH
        """
        return self._c_data[0][0]

    @pathway.setter  # set PTH.15
    def pathway(self, pth: PTH):
        """
        id: PTH | use: R | rpt: 1 | seq: 15
        ---
        param_type: PTH.15: Pathway
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTH
        """
        self._c_data[0] = (pth,)

    @property  # get VAR
    def variance(self) -> tuple[VAR, ...] | tuple[None]:
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[1]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: VAR.16 | tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        if isinstance(var, tuple):
            self._c_data[1] = var
        else:
            self._c_data[1] = (var,)
