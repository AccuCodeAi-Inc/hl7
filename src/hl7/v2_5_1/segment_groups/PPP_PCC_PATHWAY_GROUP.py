from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP import (
    PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP,
)
from ..segments.PTH import PTH
from ..segments.VAR import VAR
from ..segment_groups.PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP import (
    PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP,
)
from ..segments.NTE import NTE


"""
PATHWAY - PPP_PCC_PATHWAY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPP_PCC_PATHWAY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPP_PCC_PATHWAY_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, VAR, PTH
)
from utils.hl7.v2_5_1.segment_groups import (
    PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP, PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP
)

ppp_pcc_pathway_group = PPP_PCC_PATHWAY_GROUP(  # PATHWAY - Segment group for PPP_PCC - Pathway (problem-oriented) update consisting of PTH, NTE|None, VAR|None, PATHWAY ROLE|None, PROBLEM|None
    pathway=pth,  # PTH(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
    pathway_role=None,  # PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP(...) 
    problem=None,  # PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPP_PCC_PATHWAY_GROUP TEMPLATE-----
"""


class PPP_PCC_PATHWAY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPP_PCC_PATHWAY_GROUP"""
    _hl7_name = """PATHWAY"""
    _hl7_description = """Segment group for PPP_PCC - Pathway (problem-oriented) update consisting of PTH, NTE|None, VAR|None, PATHWAY ROLE|None, PROBLEM|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPP_PCC_PATHWAY_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("6", "7", "8", "None", "None")
    _c_components = (PTH, NTE, VAR, PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP, PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP)
    _c_name = ("PTH", "NTE", "VAR", "PATHWAY ROLE", "PROBLEM")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("pathway", "notes_and_comments", "variance", "pathway_role", "problem",)
    # fmt: on

    def __init__(
        self,
        pathway: PTH,  #  Required. PTH.6
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.7
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.8
        pathway_role: PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP
        | tuple[PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP, ...]
        | None = None,  #  (ROL.9, VAR.10, ...)
        problem: PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP
        | tuple[PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP, ...]
        | None = None,  #  (PRB.11, NTE.12, VAR.13, ...)
    ):
        """
        None - `PPP_PCC_PATHWAY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPP_PCC_PATHWAY_GROUP>`_
        Segment group for PPP_PCC - Pathway (problem-oriented) update consisting of PTH, NTE|None, VAR|None, PATHWAY ROLE|None, PROBLEM|None

        :param pathway: Pathway (id: PTH | seq: 6 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 7 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 8 | use: O | rpt: *)
        :param pathway_role: Pathway Role segment group: [ROL, VAR|None] (id: PATHWAY ROLE | seq: 9, 10 | use: O | rpt: *)
        :param problem: Problem segment group: [PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM OBSERVATION|None, GOAL|None, ORDER|None] (id: PROBLEM | seq: 11, 12, 13, None, None, None, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.pathway = pathway
        self.notes_and_comments = notes_and_comments
        self.variance = variance
        self.pathway_role = pathway_role
        self.problem = problem

    @property  # get PTH.6
    def pathway(self) -> PTH:
        """
        id: PTH | use: R | rpt: 1 | seq: 6
        ---
        return_type: PTH.6: Pathway
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTH
        """
        return self._c_data[0][0]

    @pathway.setter  # set PTH.6
    def pathway(self, pth: PTH):
        """
        id: PTH | use: R | rpt: 1 | seq: 6
        ---
        param_type: PTH.6: Pathway
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTH
        """
        self._c_data[0] = (pth,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: NTE.7 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get VAR
    def variance(self) -> tuple[VAR, ...] | tuple[None]:
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[2]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: VAR.8 | tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        if isinstance(var, tuple):
            self._c_data[2] = var
        else:
            self._c_data[2] = (var,)

    @property  # get PATHWAY ROLE
    def pathway_role(
        self,
    ) -> tuple[PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP, ...] | tuple[None]:
        """
        id: PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP
        """
        return self._c_data[3]

    @pathway_role.setter  # set PATHWAY ROLE
    def pathway_role(
        self,
        pathway_role: PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP
        | tuple[PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP, ...]
        | None,
    ):
        """
        id: PATHWAY ROLE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP.None | tuple[PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPP_PCC_PATHWAY_GROUP_PATHWAY_ROLE_GROUP
        """
        if isinstance(pathway_role, tuple):
            self._c_data[3] = pathway_role
        else:
            self._c_data[3] = (pathway_role,)

    @property  # get PROBLEM
    def problem(self) -> tuple[PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP, ...] | tuple[None]:
        """
        id: PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP
        """
        return self._c_data[4]

    @problem.setter  # set PROBLEM
    def problem(
        self,
        problem: PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP
        | tuple[PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP, ...]
        | None,
    ):
        """
        id: PROBLEM SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP.None | tuple[PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPP_PCC_PATHWAY_GROUP_PROBLEM_GROUP
        """
        if isinstance(problem, tuple):
            self._c_data[4] = problem
        else:
            self._c_data[4] = (problem,)
