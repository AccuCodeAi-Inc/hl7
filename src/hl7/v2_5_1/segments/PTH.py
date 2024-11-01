from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.EI import EI
from ..data_types.CE import CE
from ..data_types.TS import TS
from ..tables.ProblemOrGoalActionCode import ProblemOrGoalActionCode


"""
Pathway - PTH
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PTH TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PTH,
    ID, EI, CE, TS
)

pth = PTH(  #  - The pathway segment contains the data necessary to add, update, correct, and delete from the record pathways that are utilized to address an individuals health care
    action_code=id,  # ID(...)  # Required.
    pathway_id=ce,  # CE(...)  # Required.
    pathway_instance_id=ei,  # EI(...)  # Required.
    pathway_established_date_or_time=ts,  # TS(...)  # Required.
    pathway_life_cycle_status=None,  # CE(...) 
    change_pathway_life_cycle_status_date_or_time=None,  # TS(...) 
)

-----END SEGMENT::PTH TEMPLATE-----
"""


class PTH(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PTH"""
    _hl7_name = """Pathway"""
    _hl7_description = """The pathway segment contains the data necessary to add, update, correct, and delete from the record pathways that are utilized to address an individuals health care"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTH"
    _c_length = (2, 250, 60, 26, 250, 26,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "R", "R", "O", "C",)
    _c_components = (ID, CE, EI, TS, CE, TS,)
    _c_aliases = ("PTH.1", "PTH.2", "PTH.3", "PTH.4", "PTH.5", "PTH.6",)
    _c_names = ("Action Code", "Pathway ID", "Pathway Instance ID", "Pathway Established Date/Time", "Pathway Life Cycle Status", "Change Pathway Life Cycle Status Date/Time",)
    _c_attrs = ("action_code", "pathway_id", "pathway_instance_id", "pathway_established_date_or_time", "pathway_life_cycle_status", "change_pathway_life_cycle_status_date_or_time",)
    # fmt: on

    def __init__(
        self,
        action_code: ProblemOrGoalActionCode
        | ID
        | tuple[ProblemOrGoalActionCode | ID],  # PTH.1
        pathway_id: CE | tuple[CE],  # PTH.2
        pathway_instance_id: EI | tuple[EI],  # PTH.3
        pathway_established_date_or_time: TS | tuple[TS],  # PTH.4
        pathway_life_cycle_status: CE | tuple[CE] | None = None,  # PTH.5
        change_pathway_life_cycle_status_date_or_time: TS
        | tuple[TS]
        | None = None,  # PTH.6
    ):
        """
        Pathway - `PTH <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTH>`_
        The pathway segment contains the data necessary to add, update, correct, and delete from the record pathways that are utilized to address an individuals health care.

        :param action_code: Coded values for HL7 tables (id: PTH.1 | len: 2 | use: R | rpt: 1)
        :param pathway_id: Coded Element (id: PTH.2 | len: 250 | use: R | rpt: 1)
        :param pathway_instance_id: Entity Identifier (id: PTH.3 | len: 60 | use: R | rpt: 1)
        :param pathway_established_date_or_time: Time Stamp (id: PTH.4 | len: 26 | use: R | rpt: 1)
        :param pathway_life_cycle_status: Coded Element (id: PTH.5 | len: 250 | use: O | rpt: 1)
        :param change_pathway_life_cycle_status_date_or_time: Time Stamp (id: PTH.6 | len: 26 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.action_code = action_code
        self.pathway_id = pathway_id
        self.pathway_instance_id = pathway_instance_id
        self.pathway_established_date_or_time = pathway_established_date_or_time
        self.pathway_life_cycle_status = pathway_life_cycle_status
        self.change_pathway_life_cycle_status_date_or_time = (
            change_pathway_life_cycle_status_date_or_time
        )

    @property  # get PTH.1
    def action_code(self) -> ProblemOrGoalActionCode:
        """
        id: PTH.1 | len: 2 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.1
        """
        return self._c_data[0][0]

    @action_code.setter  # set PTH.1
    def action_code(self, problem_or_goal_action_code: ProblemOrGoalActionCode):
        """
        id: PTH.1 | len: 2 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.1
        """
        self._c_data[0] = (problem_or_goal_action_code,)

    @property  # get PTH.2
    def pathway_id(self) -> CE:
        """
        id: PTH.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.2
        """
        return self._c_data[1][0]

    @pathway_id.setter  # set PTH.2
    def pathway_id(self, ce: CE):
        """
        id: PTH.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.2
        """
        self._c_data[1] = (ce,)

    @property  # get PTH.3
    def pathway_instance_id(self) -> EI:
        """
        id: PTH.3 | len: 60 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.3
        """
        return self._c_data[2][0]

    @pathway_instance_id.setter  # set PTH.3
    def pathway_instance_id(self, ei: EI):
        """
        id: PTH.3 | len: 60 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.3
        """
        self._c_data[2] = (ei,)

    @property  # get PTH.4
    def pathway_established_date_or_time(self) -> TS:
        """
        id: PTH.4 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.4
        """
        return self._c_data[3][0]

    @pathway_established_date_or_time.setter  # set PTH.4
    def pathway_established_date_or_time(self, ts: TS):
        """
        id: PTH.4 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.4
        """
        self._c_data[3] = (ts,)

    @property  # get PTH.5
    def pathway_life_cycle_status(self) -> CE | None:
        """
        id: PTH.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.5
        """
        return self._c_data[4][0]

    @pathway_life_cycle_status.setter  # set PTH.5
    def pathway_life_cycle_status(self, ce: CE | None):
        """
        id: PTH.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.5
        """
        self._c_data[4] = (ce,)

    @property  # get PTH.6
    def change_pathway_life_cycle_status_date_or_time(self) -> TS | None:
        """
        id: PTH.6 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.6
        """
        return self._c_data[5][0]

    @change_pathway_life_cycle_status_date_or_time.setter  # set PTH.6
    def change_pathway_life_cycle_status_date_or_time(self, ts: TS | None):
        """
        id: PTH.6 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTH.6
        """
        self._c_data[5] = (ts,)
