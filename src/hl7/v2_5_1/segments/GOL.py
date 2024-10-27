from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.TQ import TQ
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..data_types.XPN import XPN
from ..data_types.EI import EI
from ..tables.ProblemOrGoalActionCode import ProblemOrGoalActionCode


"""
Goal Detail - GOL
HL7 Version: 2.5.1

-----BEGIN SEGMENT::GOL TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    GOL,
    ID, TS, TQ, ST, CE, NM, XPN, EI
)

gol = GOL(  #  - The goal detail segment contains the data necessary to add, update, correct, and delete the goals for an individual
    action_code=id,  # ID(...)  # Required.
    action_date_or_time=ts,  # TS(...)  # Required.
    goal_id=ce,  # CE(...)  # Required.
    goal_instance_id=ei,  # EI(...)  # Required.
    episode_of_care_id=None,  # EI(...) 
    goal_list_priority=None,  # NM(...) 
    goal_established_date_or_time=None,  # TS(...) 
    expected_goal_achieve_date_or_time=None,  # TS(...) 
    goal_classification=None,  # CE(...) 
    goal_management_discipline=None,  # CE(...) 
    current_goal_review_status=None,  # CE(...) 
    current_goal_review_date_or_time=None,  # TS(...) 
    next_goal_review_date_or_time=None,  # TS(...) 
    previous_goal_review_date_or_time=None,  # TS(...) 
    goal_review_interval=None,  # TQ(...) 
    goal_evaluation=None,  # CE(...) 
    goal_evaluation_comment=None,  # ST(...) 
    goal_life_cycle_status=None,  # CE(...) 
    goal_life_cycle_status_date_or_time=None,  # TS(...) 
    goal_target_type=None,  # CE(...) 
    goal_target_name=None,  # XPN(...) 
)

-----END SEGMENT::GOL TEMPLATE-----
"""


class GOL(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """GOL"""
    _hl7_name = """Goal Detail"""
    _hl7_description = """The goal detail segment contains the data necessary to add, update, correct, and delete the goals for an individual"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GOL"
    _c_length = (2, 26, 250, 60, 60, 60, 26, 26, 250, 250, 250, 26, 26, 26, 200, 250, 300, 250, 26, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 65535, 65535,)
    _c_usage = ("R", "R", "R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (ID, TS, CE, EI, EI, NM, TS, TS, CE, CE, CE, TS, TS, TS, TQ, CE, ST, CE, TS, CE, XPN,)
    _c_aliases = ("GOL.1", "GOL.2", "GOL.3", "GOL.4", "GOL.5", "GOL.6", "GOL.7", "GOL.8", "GOL.9", "GOL.10", "GOL.11", "GOL.12", "GOL.13", "GOL.14", "GOL.15", "GOL.16", "GOL.17", "GOL.18", "GOL.19", "GOL.20", "GOL.21",)
    _c_names = ("Action Code", "Action Date/Time", "Goal ID", "Goal Instance ID", "Episode of Care ID", "Goal List Priority", "Goal Established Date/Time", "Expected Goal Achieve Date/Time", "Goal Classification", "Goal Management Discipline", "Current Goal Review Status", "Current Goal Review Date/Time", "Next Goal Review Date/Time", "Previous Goal Review Date/Time", "Goal Review Interval", "Goal Evaluation", "Goal Evaluation Comment", "Goal Life Cycle Status", "Goal Life Cycle Status Date/Time", "Goal Target Type", "Goal Target Name",)
    _c_attrs = ("action_code", "action_date_or_time", "goal_id", "goal_instance_id", "episode_of_care_id", "goal_list_priority", "goal_established_date_or_time", "expected_goal_achieve_date_or_time", "goal_classification", "goal_management_discipline", "current_goal_review_status", "current_goal_review_date_or_time", "next_goal_review_date_or_time", "previous_goal_review_date_or_time", "goal_review_interval", "goal_evaluation", "goal_evaluation_comment", "goal_life_cycle_status", "goal_life_cycle_status_date_or_time", "goal_target_type", "goal_target_name",)
    # fmt: on

    def __init__(
        self,
        action_code: ProblemOrGoalActionCode | ID,  # GOL.1
        action_date_or_time: TS,  # GOL.2
        goal_id: CE,  # GOL.3
        goal_instance_id: EI,  # GOL.4
        episode_of_care_id: EI | None = None,  # GOL.5
        goal_list_priority: NM | None = None,  # GOL.6
        goal_established_date_or_time: TS | None = None,  # GOL.7
        expected_goal_achieve_date_or_time: TS | None = None,  # GOL.8
        goal_classification: CE | None = None,  # GOL.9
        goal_management_discipline: CE | None = None,  # GOL.10
        current_goal_review_status: CE | None = None,  # GOL.11
        current_goal_review_date_or_time: TS | None = None,  # GOL.12
        next_goal_review_date_or_time: TS | None = None,  # GOL.13
        previous_goal_review_date_or_time: TS | None = None,  # GOL.14
        goal_review_interval: TQ | None = None,  # GOL.15
        goal_evaluation: CE | None = None,  # GOL.16
        goal_evaluation_comment: ST | None = None,  # GOL.17
        goal_life_cycle_status: CE | None = None,  # GOL.18
        goal_life_cycle_status_date_or_time: TS | None = None,  # GOL.19
        goal_target_type: CE | None = None,  # GOL.20
        goal_target_name: XPN | None = None,  # GOL.21
    ):
        """
        Goal Detail - `GOL <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GOL>`_
        The goal detail segment contains the data necessary to add, update, correct, and delete the goals for an individual.

        :param action_code: Coded values for HL7 tables (id: GOL.1 | len: 2 | use: R | rpt: 1)
        :param action_date_or_time: Time Stamp (id: GOL.2 | len: 26 | use: R | rpt: 1)
        :param goal_id: Coded Element (id: GOL.3 | len: 250 | use: R | rpt: 1)
        :param goal_instance_id: Entity Identifier (id: GOL.4 | len: 60 | use: R | rpt: 1)
        :param episode_of_care_id: Entity Identifier (id: GOL.5 | len: 60 | use: O | rpt: 1)
        :param goal_list_priority: Numeric (id: GOL.6 | len: 60 | use: O | rpt: 1)
        :param goal_established_date_or_time: Time Stamp (id: GOL.7 | len: 26 | use: O | rpt: 1)
        :param expected_goal_achieve_date_or_time: Time Stamp (id: GOL.8 | len: 26 | use: O | rpt: 1)
        :param goal_classification: Coded Element (id: GOL.9 | len: 250 | use: O | rpt: 1)
        :param goal_management_discipline: Coded Element (id: GOL.10 | len: 250 | use: O | rpt: 1)
        :param current_goal_review_status: Coded Element (id: GOL.11 | len: 250 | use: O | rpt: 1)
        :param current_goal_review_date_or_time: Time Stamp (id: GOL.12 | len: 26 | use: O | rpt: 1)
        :param next_goal_review_date_or_time: Time Stamp (id: GOL.13 | len: 26 | use: O | rpt: 1)
        :param previous_goal_review_date_or_time: Time Stamp (id: GOL.14 | len: 26 | use: O | rpt: 1)
        :param goal_review_interval: Timing Quantity (id: GOL.15 | len: 200 | use: O | rpt: 1)
        :param goal_evaluation: Coded Element (id: GOL.16 | len: 250 | use: O | rpt: 1)
        :param goal_evaluation_comment: String Data (id: GOL.17 | len: 300 | use: O | rpt: *)
        :param goal_life_cycle_status: Coded Element (id: GOL.18 | len: 250 | use: O | rpt: 1)
        :param goal_life_cycle_status_date_or_time: Time Stamp (id: GOL.19 | len: 26 | use: O | rpt: 1)
        :param goal_target_type: Coded Element (id: GOL.20 | len: 250 | use: O | rpt: *)
        :param goal_target_name: Extended Person Name (id: GOL.21 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 21
        self.action_code = action_code
        self.action_date_or_time = action_date_or_time
        self.goal_id = goal_id
        self.goal_instance_id = goal_instance_id
        self.episode_of_care_id = episode_of_care_id
        self.goal_list_priority = goal_list_priority
        self.goal_established_date_or_time = goal_established_date_or_time
        self.expected_goal_achieve_date_or_time = expected_goal_achieve_date_or_time
        self.goal_classification = goal_classification
        self.goal_management_discipline = goal_management_discipline
        self.current_goal_review_status = current_goal_review_status
        self.current_goal_review_date_or_time = current_goal_review_date_or_time
        self.next_goal_review_date_or_time = next_goal_review_date_or_time
        self.previous_goal_review_date_or_time = previous_goal_review_date_or_time
        self.goal_review_interval = goal_review_interval
        self.goal_evaluation = goal_evaluation
        self.goal_evaluation_comment = goal_evaluation_comment
        self.goal_life_cycle_status = goal_life_cycle_status
        self.goal_life_cycle_status_date_or_time = goal_life_cycle_status_date_or_time
        self.goal_target_type = goal_target_type
        self.goal_target_name = goal_target_name

    @property  # get GOL.1
    def action_code(self) -> ProblemOrGoalActionCode:
        """
        id: GOL.1 | len: 2 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.1
        """
        return self._c_data[0][0]

    @action_code.setter  # set GOL.1
    def action_code(self, problem_or_goal_action_code: ProblemOrGoalActionCode):
        """
        id: GOL.1 | len: 2 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.1
        """
        self._c_data[0] = (problem_or_goal_action_code,)

    @property  # get GOL.2
    def action_date_or_time(self) -> TS:
        """
        id: GOL.2 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.2
        """
        return self._c_data[1][0]

    @action_date_or_time.setter  # set GOL.2
    def action_date_or_time(self, ts: TS):
        """
        id: GOL.2 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.2
        """
        self._c_data[1] = (ts,)

    @property  # get GOL.3
    def goal_id(self) -> CE:
        """
        id: GOL.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.3
        """
        return self._c_data[2][0]

    @goal_id.setter  # set GOL.3
    def goal_id(self, ce: CE):
        """
        id: GOL.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.3
        """
        self._c_data[2] = (ce,)

    @property  # get GOL.4
    def goal_instance_id(self) -> EI:
        """
        id: GOL.4 | len: 60 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.4
        """
        return self._c_data[3][0]

    @goal_instance_id.setter  # set GOL.4
    def goal_instance_id(self, ei: EI):
        """
        id: GOL.4 | len: 60 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.4
        """
        self._c_data[3] = (ei,)

    @property  # get GOL.5
    def episode_of_care_id(self) -> EI | None:
        """
        id: GOL.5 | len: 60 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.5
        """
        return self._c_data[4][0]

    @episode_of_care_id.setter  # set GOL.5
    def episode_of_care_id(self, ei: EI | None):
        """
        id: GOL.5 | len: 60 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.5
        """
        self._c_data[4] = (ei,)

    @property  # get GOL.6
    def goal_list_priority(self) -> NM | None:
        """
        id: GOL.6 | len: 60 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.6
        """
        return self._c_data[5][0]

    @goal_list_priority.setter  # set GOL.6
    def goal_list_priority(self, nm: NM | None):
        """
        id: GOL.6 | len: 60 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.6
        """
        self._c_data[5] = (nm,)

    @property  # get GOL.7
    def goal_established_date_or_time(self) -> TS | None:
        """
        id: GOL.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.7
        """
        return self._c_data[6][0]

    @goal_established_date_or_time.setter  # set GOL.7
    def goal_established_date_or_time(self, ts: TS | None):
        """
        id: GOL.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.7
        """
        self._c_data[6] = (ts,)

    @property  # get GOL.8
    def expected_goal_achieve_date_or_time(self) -> TS | None:
        """
        id: GOL.8 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.8
        """
        return self._c_data[7][0]

    @expected_goal_achieve_date_or_time.setter  # set GOL.8
    def expected_goal_achieve_date_or_time(self, ts: TS | None):
        """
        id: GOL.8 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.8
        """
        self._c_data[7] = (ts,)

    @property  # get GOL.9
    def goal_classification(self) -> CE | None:
        """
        id: GOL.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.9
        """
        return self._c_data[8][0]

    @goal_classification.setter  # set GOL.9
    def goal_classification(self, ce: CE | None):
        """
        id: GOL.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.9
        """
        self._c_data[8] = (ce,)

    @property  # get GOL.10
    def goal_management_discipline(self) -> CE | None:
        """
        id: GOL.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.10
        """
        return self._c_data[9][0]

    @goal_management_discipline.setter  # set GOL.10
    def goal_management_discipline(self, ce: CE | None):
        """
        id: GOL.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.10
        """
        self._c_data[9] = (ce,)

    @property  # get GOL.11
    def current_goal_review_status(self) -> CE | None:
        """
        id: GOL.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.11
        """
        return self._c_data[10][0]

    @current_goal_review_status.setter  # set GOL.11
    def current_goal_review_status(self, ce: CE | None):
        """
        id: GOL.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.11
        """
        self._c_data[10] = (ce,)

    @property  # get GOL.12
    def current_goal_review_date_or_time(self) -> TS | None:
        """
        id: GOL.12 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.12
        """
        return self._c_data[11][0]

    @current_goal_review_date_or_time.setter  # set GOL.12
    def current_goal_review_date_or_time(self, ts: TS | None):
        """
        id: GOL.12 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.12
        """
        self._c_data[11] = (ts,)

    @property  # get GOL.13
    def next_goal_review_date_or_time(self) -> TS | None:
        """
        id: GOL.13 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.13
        """
        return self._c_data[12][0]

    @next_goal_review_date_or_time.setter  # set GOL.13
    def next_goal_review_date_or_time(self, ts: TS | None):
        """
        id: GOL.13 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.13
        """
        self._c_data[12] = (ts,)

    @property  # get GOL.14
    def previous_goal_review_date_or_time(self) -> TS | None:
        """
        id: GOL.14 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.14
        """
        return self._c_data[13][0]

    @previous_goal_review_date_or_time.setter  # set GOL.14
    def previous_goal_review_date_or_time(self, ts: TS | None):
        """
        id: GOL.14 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.14
        """
        self._c_data[13] = (ts,)

    @property  # get GOL.15
    def goal_review_interval(self) -> TQ | None:
        """
        id: GOL.15 | len: 200 | use: O | rpt: 1
        ---
        return_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.15
        """
        return self._c_data[14][0]

    @goal_review_interval.setter  # set GOL.15
    def goal_review_interval(self, tq: TQ | None):
        """
        id: GOL.15 | len: 200 | use: O | rpt: 1
        ---
        param_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.15
        """
        self._c_data[14] = (tq,)

    @property  # get GOL.16
    def goal_evaluation(self) -> CE | None:
        """
        id: GOL.16 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.16
        """
        return self._c_data[15][0]

    @goal_evaluation.setter  # set GOL.16
    def goal_evaluation(self, ce: CE | None):
        """
        id: GOL.16 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.16
        """
        self._c_data[15] = (ce,)

    @property
    def goal_evaluation_comment(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: GOL.17 | len: 300 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.17
        """
        return self._c_data[16]

    @goal_evaluation_comment.setter  # set GOL.17
    def goal_evaluation_comment(self, st: ST | tuple[ST] | None):
        """
        id: GOL.17 | len: 300 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.17
        """
        if isinstance(st, tuple):
            self._c_data[16] = st
        else:
            self._c_data[16] = (st,)

    @property  # get GOL.18
    def goal_life_cycle_status(self) -> CE | None:
        """
        id: GOL.18 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.18
        """
        return self._c_data[17][0]

    @goal_life_cycle_status.setter  # set GOL.18
    def goal_life_cycle_status(self, ce: CE | None):
        """
        id: GOL.18 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.18
        """
        self._c_data[17] = (ce,)

    @property  # get GOL.19
    def goal_life_cycle_status_date_or_time(self) -> TS | None:
        """
        id: GOL.19 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.19
        """
        return self._c_data[18][0]

    @goal_life_cycle_status_date_or_time.setter  # set GOL.19
    def goal_life_cycle_status_date_or_time(self, ts: TS | None):
        """
        id: GOL.19 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.19
        """
        self._c_data[18] = (ts,)

    @property
    def goal_target_type(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: GOL.20 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.20
        """
        return self._c_data[19]

    @goal_target_type.setter  # set GOL.20
    def goal_target_type(self, ce: CE | tuple[CE] | None):
        """
        id: GOL.20 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.20
        """
        if isinstance(ce, tuple):
            self._c_data[19] = ce
        else:
            self._c_data[19] = (ce,)

    @property
    def goal_target_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: GOL.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.21
        """
        return self._c_data[20]

    @goal_target_name.setter  # set GOL.21
    def goal_target_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: GOL.21 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GOL.21
        """
        if isinstance(xpn, tuple):
            self._c_data[20] = xpn
        else:
            self._c_data[20] = (xpn,)
