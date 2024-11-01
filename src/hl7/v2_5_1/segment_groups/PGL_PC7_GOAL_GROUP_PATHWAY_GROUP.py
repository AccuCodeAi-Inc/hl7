from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.VAR import VAR
from ..segments.PTH import PTH


"""
PATHWAY - PGL_PC7_GOAL_GROUP_PATHWAY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PGL_PC7_GOAL_GROUP_PATHWAY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PGL_PC7_GOAL_GROUP_PATHWAY_GROUP
from utils.hl7.v2_5_1.segments import (
    PTH, VAR
)

pgl_pc7_goal_group_pathway_group = PGL_PC7_GOAL_GROUP_PATHWAY_GROUP(  # PATHWAY - Segment group for PGL_PC7_GOAL_GROUP - GOAL consisting of PTH, VAR|None
    pathway=pth,  # PTH(...)  # Required.
    variance=None,  # VAR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PGL_PC7_GOAL_GROUP_PATHWAY_GROUP TEMPLATE-----
"""


class PGL_PC7_GOAL_GROUP_PATHWAY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PGL_PC7_GOAL_GROUP_PATHWAY_GROUP"""
    _hl7_name = """PATHWAY"""
    _hl7_description = """Segment group for PGL_PC7_GOAL_GROUP - GOAL consisting of PTH, VAR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PGL_PC7_GOAL_GROUP_PATHWAY_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("11", "12")
    _c_components = (PTH, VAR)
    _c_name = ("PTH", "VAR")
    _c_is_group = (False, False)
    _c_attrs = ("pathway", "variance",)
    # fmt: on

    def __init__(
        self,
        pathway: PTH,  #  Required. PTH.11
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.12
    ):
        """
        None - `PGL_PC7_GOAL_GROUP_PATHWAY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PGL_PC7_GOAL_GROUP_PATHWAY_GROUP>`_
        Segment group for PGL_PC7_GOAL_GROUP - GOAL consisting of PTH, VAR|None

        :param pathway: Pathway (id: PTH | seq: 11 | use: R | rpt: 1)
        :param variance: Variance (id: VAR | seq: 12 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.pathway = pathway
        self.variance = variance

    @property  # get PTH.11
    def pathway(self) -> PTH:
        """
        id: PTH | use: R | rpt: 1 | seq: 11
        ---
        return_type: PTH.11: Pathway
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTH
        """
        return self._c_data[0][0]

    @pathway.setter  # set PTH.11
    def pathway(self, pth: PTH):
        """
        id: PTH | use: R | rpt: 1 | seq: 11
        ---
        param_type: PTH.11: Pathway
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTH
        """
        self._c_data[0] = (pth,)

    @property  # get VAR
    def variance(self) -> tuple[VAR, ...] | tuple[None]:
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[1]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: VAR.12 | tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        if isinstance(var, tuple):
            self._c_data[1] = var
        else:
            self._c_data[1] = (var,)
