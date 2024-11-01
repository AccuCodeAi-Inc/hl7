from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.ST import ST
from ..data_types.EI import EI
from ..data_types.TS import TS
from ..tables.ProblemOrGoalActionCode import ProblemOrGoalActionCode


"""
Problem Details - PRB
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PRB TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PRB,
    CE, ID, NM, ST, EI, TS
)

prb = PRB(  #  - The problem detail segment contains the data necessary to add, update, correct, and delete the problems of a given individual
    action_code=id,  # ID(...)  # Required.
    action_date_or_time=ts,  # TS(...)  # Required.
    problem_id=ce,  # CE(...)  # Required.
    problem_instance_id=ei,  # EI(...)  # Required.
    episode_of_care_id=None,  # EI(...) 
    problem_list_priority=None,  # NM(...) 
    problem_established_date_or_time=None,  # TS(...) 
    anticipated_problem_resolution_date_or_time=None,  # TS(...) 
    actual_problem_resolution_date_or_time=None,  # TS(...) 
    problem_classification=None,  # CE(...) 
    problem_management_discipline=None,  # CE(...) 
    problem_persistence=None,  # CE(...) 
    problem_confirmation_status=None,  # CE(...) 
    problem_life_cycle_status=None,  # CE(...) 
    problem_life_cycle_status_date_or_time=None,  # TS(...) 
    problem_date_of_onset=None,  # TS(...) 
    problem_onset_text=None,  # ST(...) 
    problem_ranking=None,  # CE(...) 
    certainty_of_problem=None,  # CE(...) 
    probability_of_problem=None,  # NM(...) 
    individual_awareness_of_problem=None,  # CE(...) 
    problem_prognosis=None,  # CE(...) 
    individual_awareness_of_prognosis=None,  # CE(...) 
    family_or_significant_other_awareness_of_problem_or_prognosis=None,  # ST(...) 
    security_or_sensitivity=None,  # CE(...) 
)

-----END SEGMENT::PRB TEMPLATE-----
"""


class PRB(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PRB"""
    _hl7_name = """Problem Details"""
    _hl7_description = """The problem detail segment contains the data necessary to add, update, correct, and delete the problems of a given individual"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB"
    _c_length = (2, 26, 250, 60, 60, 60, 26, 26, 26, 250, 250, 250, 250, 250, 26, 26, 80, 250, 250, 5, 250, 250, 250, 200, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (ID, TS, CE, EI, EI, NM, TS, TS, TS, CE, CE, CE, CE, CE, TS, TS, ST, CE, CE, NM, CE, CE, CE, ST, CE,)
    _c_aliases = ("PRB.1", "PRB.2", "PRB.3", "PRB.4", "PRB.5", "PRB.6", "PRB.7", "PRB.8", "PRB.9", "PRB.10", "PRB.11", "PRB.12", "PRB.13", "PRB.14", "PRB.15", "PRB.16", "PRB.17", "PRB.18", "PRB.19", "PRB.20", "PRB.21", "PRB.22", "PRB.23", "PRB.24", "PRB.25",)
    _c_names = ("Action Code", "Action Date/Time", "Problem ID", "Problem Instance ID", "Episode of Care ID", "Problem List Priority", "Problem Established Date/Time", "Anticipated Problem Resolution Date/Time", "Actual Problem Resolution Date/Time", "Problem Classification", "Problem Management Discipline", "Problem Persistence", "Problem Confirmation Status", "Problem Life Cycle Status", "Problem Life Cycle Status Date/Time", "Problem Date of Onset", "Problem Onset Text", "Problem Ranking", "Certainty of Problem (0-1)", "Probability of Problem", "Individual Awareness of Problem", "Problem Prognosis", "Individual Awareness of Prognosis", "Family/Significant Other Awareness of Problem/Prognosis", "Security/Sensitivity",)
    _c_attrs = ("action_code", "action_date_or_time", "problem_id", "problem_instance_id", "episode_of_care_id", "problem_list_priority", "problem_established_date_or_time", "anticipated_problem_resolution_date_or_time", "actual_problem_resolution_date_or_time", "problem_classification", "problem_management_discipline", "problem_persistence", "problem_confirmation_status", "problem_life_cycle_status", "problem_life_cycle_status_date_or_time", "problem_date_of_onset", "problem_onset_text", "problem_ranking", "certainty_of_problem", "probability_of_problem", "individual_awareness_of_problem", "problem_prognosis", "individual_awareness_of_prognosis", "family_or_significant_other_awareness_of_problem_or_prognosis", "security_or_sensitivity",)
    # fmt: on

    def __init__(
        self,
        action_code: ProblemOrGoalActionCode | ID,  # PRB.1
        action_date_or_time: TS,  # PRB.2
        problem_id: CE,  # PRB.3
        problem_instance_id: EI,  # PRB.4
        episode_of_care_id: EI | None = None,  # PRB.5
        problem_list_priority: NM | None = None,  # PRB.6
        problem_established_date_or_time: TS | None = None,  # PRB.7
        anticipated_problem_resolution_date_or_time: TS | None = None,  # PRB.8
        actual_problem_resolution_date_or_time: TS | None = None,  # PRB.9
        problem_classification: CE | None = None,  # PRB.10
        problem_management_discipline: CE | None = None,  # PRB.11
        problem_persistence: CE | None = None,  # PRB.12
        problem_confirmation_status: CE | None = None,  # PRB.13
        problem_life_cycle_status: CE | None = None,  # PRB.14
        problem_life_cycle_status_date_or_time: TS | None = None,  # PRB.15
        problem_date_of_onset: TS | None = None,  # PRB.16
        problem_onset_text: ST | None = None,  # PRB.17
        problem_ranking: CE | None = None,  # PRB.18
        certainty_of_problem: CE | None = None,  # PRB.19
        probability_of_problem: NM | None = None,  # PRB.20
        individual_awareness_of_problem: CE | None = None,  # PRB.21
        problem_prognosis: CE | None = None,  # PRB.22
        individual_awareness_of_prognosis: CE | None = None,  # PRB.23
        family_or_significant_other_awareness_of_problem_or_prognosis: ST
        | None = None,  # PRB.24
        security_or_sensitivity: CE | None = None,  # PRB.25
    ):
        """
        Problem Details - `PRB <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB>`_
        The problem detail segment contains the data necessary to add, update, correct, and delete the problems of a given individual.

        :param action_code: Coded values for HL7 tables (id: PRB.1 | len: 2 | use: R | rpt: 1)
        :param action_date_or_time: Time Stamp (id: PRB.2 | len: 26 | use: R | rpt: 1)
        :param problem_id: Coded Element (id: PRB.3 | len: 250 | use: R | rpt: 1)
        :param problem_instance_id: Entity Identifier (id: PRB.4 | len: 60 | use: R | rpt: 1)
        :param episode_of_care_id: Entity Identifier (id: PRB.5 | len: 60 | use: O | rpt: 1)
        :param problem_list_priority: Numeric (id: PRB.6 | len: 60 | use: O | rpt: 1)
        :param problem_established_date_or_time: Time Stamp (id: PRB.7 | len: 26 | use: O | rpt: 1)
        :param anticipated_problem_resolution_date_or_time: Time Stamp (id: PRB.8 | len: 26 | use: O | rpt: 1)
        :param actual_problem_resolution_date_or_time: Time Stamp (id: PRB.9 | len: 26 | use: O | rpt: 1)
        :param problem_classification: Coded Element (id: PRB.10 | len: 250 | use: O | rpt: 1)
        :param problem_management_discipline: Coded Element (id: PRB.11 | len: 250 | use: O | rpt: *)
        :param problem_persistence: Coded Element (id: PRB.12 | len: 250 | use: O | rpt: 1)
        :param problem_confirmation_status: Coded Element (id: PRB.13 | len: 250 | use: O | rpt: 1)
        :param problem_life_cycle_status: Coded Element (id: PRB.14 | len: 250 | use: O | rpt: 1)
        :param problem_life_cycle_status_date_or_time: Time Stamp (id: PRB.15 | len: 26 | use: O | rpt: 1)
        :param problem_date_of_onset: Time Stamp (id: PRB.16 | len: 26 | use: O | rpt: 1)
        :param problem_onset_text: String Data (id: PRB.17 | len: 80 | use: O | rpt: 1)
        :param problem_ranking: Coded Element (id: PRB.18 | len: 250 | use: O | rpt: 1)
        :param certainty_of_problem: Coded Element (id: PRB.19 | len: 250 | use: O | rpt: 1)
        :param probability_of_problem: Numeric (id: PRB.20 | len: 5 | use: O | rpt: 1)
        :param individual_awareness_of_problem: Coded Element (id: PRB.21 | len: 250 | use: O | rpt: 1)
        :param problem_prognosis: Coded Element (id: PRB.22 | len: 250 | use: O | rpt: 1)
        :param individual_awareness_of_prognosis: Coded Element (id: PRB.23 | len: 250 | use: O | rpt: 1)
        :param family_or_significant_other_awareness_of_problem_or_prognosis: String Data (id: PRB.24 | len: 200 | use: O | rpt: 1)
        :param security_or_sensitivity: Coded Element (id: PRB.25 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 25
        self.action_code = action_code
        self.action_date_or_time = action_date_or_time
        self.problem_id = problem_id
        self.problem_instance_id = problem_instance_id
        self.episode_of_care_id = episode_of_care_id
        self.problem_list_priority = problem_list_priority
        self.problem_established_date_or_time = problem_established_date_or_time
        self.anticipated_problem_resolution_date_or_time = (
            anticipated_problem_resolution_date_or_time
        )
        self.actual_problem_resolution_date_or_time = (
            actual_problem_resolution_date_or_time
        )
        self.problem_classification = problem_classification
        self.problem_management_discipline = problem_management_discipline
        self.problem_persistence = problem_persistence
        self.problem_confirmation_status = problem_confirmation_status
        self.problem_life_cycle_status = problem_life_cycle_status
        self.problem_life_cycle_status_date_or_time = (
            problem_life_cycle_status_date_or_time
        )
        self.problem_date_of_onset = problem_date_of_onset
        self.problem_onset_text = problem_onset_text
        self.problem_ranking = problem_ranking
        self.certainty_of_problem = certainty_of_problem
        self.probability_of_problem = probability_of_problem
        self.individual_awareness_of_problem = individual_awareness_of_problem
        self.problem_prognosis = problem_prognosis
        self.individual_awareness_of_prognosis = individual_awareness_of_prognosis
        self.family_or_significant_other_awareness_of_problem_or_prognosis = (
            family_or_significant_other_awareness_of_problem_or_prognosis
        )
        self.security_or_sensitivity = security_or_sensitivity

    @property  # get PRB.1
    def action_code(self) -> ProblemOrGoalActionCode:
        """
        id: PRB.1 | len: 2 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.1
        """
        return self._c_data[0][0]

    @action_code.setter  # set PRB.1
    def action_code(self, problem_or_goal_action_code: ProblemOrGoalActionCode):
        """
        id: PRB.1 | len: 2 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.1
        """
        self._c_data[0] = (problem_or_goal_action_code,)

    @property  # get PRB.2
    def action_date_or_time(self) -> TS:
        """
        id: PRB.2 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.2
        """
        return self._c_data[1][0]

    @action_date_or_time.setter  # set PRB.2
    def action_date_or_time(self, ts: TS):
        """
        id: PRB.2 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.2
        """
        self._c_data[1] = (ts,)

    @property  # get PRB.3
    def problem_id(self) -> CE:
        """
        id: PRB.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.3
        """
        return self._c_data[2][0]

    @problem_id.setter  # set PRB.3
    def problem_id(self, ce: CE):
        """
        id: PRB.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.3
        """
        self._c_data[2] = (ce,)

    @property  # get PRB.4
    def problem_instance_id(self) -> EI:
        """
        id: PRB.4 | len: 60 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.4
        """
        return self._c_data[3][0]

    @problem_instance_id.setter  # set PRB.4
    def problem_instance_id(self, ei: EI):
        """
        id: PRB.4 | len: 60 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.4
        """
        self._c_data[3] = (ei,)

    @property  # get PRB.5
    def episode_of_care_id(self) -> EI | None:
        """
        id: PRB.5 | len: 60 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.5
        """
        return self._c_data[4][0]

    @episode_of_care_id.setter  # set PRB.5
    def episode_of_care_id(self, ei: EI | None):
        """
        id: PRB.5 | len: 60 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.5
        """
        self._c_data[4] = (ei,)

    @property  # get PRB.6
    def problem_list_priority(self) -> NM | None:
        """
        id: PRB.6 | len: 60 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.6
        """
        return self._c_data[5][0]

    @problem_list_priority.setter  # set PRB.6
    def problem_list_priority(self, nm: NM | None):
        """
        id: PRB.6 | len: 60 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.6
        """
        self._c_data[5] = (nm,)

    @property  # get PRB.7
    def problem_established_date_or_time(self) -> TS | None:
        """
        id: PRB.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.7
        """
        return self._c_data[6][0]

    @problem_established_date_or_time.setter  # set PRB.7
    def problem_established_date_or_time(self, ts: TS | None):
        """
        id: PRB.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.7
        """
        self._c_data[6] = (ts,)

    @property  # get PRB.8
    def anticipated_problem_resolution_date_or_time(self) -> TS | None:
        """
        id: PRB.8 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.8
        """
        return self._c_data[7][0]

    @anticipated_problem_resolution_date_or_time.setter  # set PRB.8
    def anticipated_problem_resolution_date_or_time(self, ts: TS | None):
        """
        id: PRB.8 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.8
        """
        self._c_data[7] = (ts,)

    @property  # get PRB.9
    def actual_problem_resolution_date_or_time(self) -> TS | None:
        """
        id: PRB.9 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.9
        """
        return self._c_data[8][0]

    @actual_problem_resolution_date_or_time.setter  # set PRB.9
    def actual_problem_resolution_date_or_time(self, ts: TS | None):
        """
        id: PRB.9 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.9
        """
        self._c_data[8] = (ts,)

    @property  # get PRB.10
    def problem_classification(self) -> CE | None:
        """
        id: PRB.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.10
        """
        return self._c_data[9][0]

    @problem_classification.setter  # set PRB.10
    def problem_classification(self, ce: CE | None):
        """
        id: PRB.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.10
        """
        self._c_data[9] = (ce,)

    @property
    def problem_management_discipline(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: PRB.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.11
        """
        return self._c_data[10]

    @problem_management_discipline.setter  # set PRB.11
    def problem_management_discipline(self, ce: CE | tuple[CE] | None):
        """
        id: PRB.11 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.11
        """
        if isinstance(ce, tuple):
            self._c_data[10] = ce
        else:
            self._c_data[10] = (ce,)

    @property  # get PRB.12
    def problem_persistence(self) -> CE | None:
        """
        id: PRB.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.12
        """
        return self._c_data[11][0]

    @problem_persistence.setter  # set PRB.12
    def problem_persistence(self, ce: CE | None):
        """
        id: PRB.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.12
        """
        self._c_data[11] = (ce,)

    @property  # get PRB.13
    def problem_confirmation_status(self) -> CE | None:
        """
        id: PRB.13 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.13
        """
        return self._c_data[12][0]

    @problem_confirmation_status.setter  # set PRB.13
    def problem_confirmation_status(self, ce: CE | None):
        """
        id: PRB.13 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.13
        """
        self._c_data[12] = (ce,)

    @property  # get PRB.14
    def problem_life_cycle_status(self) -> CE | None:
        """
        id: PRB.14 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.14
        """
        return self._c_data[13][0]

    @problem_life_cycle_status.setter  # set PRB.14
    def problem_life_cycle_status(self, ce: CE | None):
        """
        id: PRB.14 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.14
        """
        self._c_data[13] = (ce,)

    @property  # get PRB.15
    def problem_life_cycle_status_date_or_time(self) -> TS | None:
        """
        id: PRB.15 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.15
        """
        return self._c_data[14][0]

    @problem_life_cycle_status_date_or_time.setter  # set PRB.15
    def problem_life_cycle_status_date_or_time(self, ts: TS | None):
        """
        id: PRB.15 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.15
        """
        self._c_data[14] = (ts,)

    @property  # get PRB.16
    def problem_date_of_onset(self) -> TS | None:
        """
        id: PRB.16 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.16
        """
        return self._c_data[15][0]

    @problem_date_of_onset.setter  # set PRB.16
    def problem_date_of_onset(self, ts: TS | None):
        """
        id: PRB.16 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.16
        """
        self._c_data[15] = (ts,)

    @property  # get PRB.17
    def problem_onset_text(self) -> ST | None:
        """
        id: PRB.17 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.17
        """
        return self._c_data[16][0]

    @problem_onset_text.setter  # set PRB.17
    def problem_onset_text(self, st: ST | None):
        """
        id: PRB.17 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.17
        """
        self._c_data[16] = (st,)

    @property  # get PRB.18
    def problem_ranking(self) -> CE | None:
        """
        id: PRB.18 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.18
        """
        return self._c_data[17][0]

    @problem_ranking.setter  # set PRB.18
    def problem_ranking(self, ce: CE | None):
        """
        id: PRB.18 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.18
        """
        self._c_data[17] = (ce,)

    @property  # get PRB.19
    def certainty_of_problem(self) -> CE | None:
        """
        id: PRB.19 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.19
        """
        return self._c_data[18][0]

    @certainty_of_problem.setter  # set PRB.19
    def certainty_of_problem(self, ce: CE | None):
        """
        id: PRB.19 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.19
        """
        self._c_data[18] = (ce,)

    @property  # get PRB.20
    def probability_of_problem(self) -> NM | None:
        """
        id: PRB.20 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.20
        """
        return self._c_data[19][0]

    @probability_of_problem.setter  # set PRB.20
    def probability_of_problem(self, nm: NM | None):
        """
        id: PRB.20 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.20
        """
        self._c_data[19] = (nm,)

    @property  # get PRB.21
    def individual_awareness_of_problem(self) -> CE | None:
        """
        id: PRB.21 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.21
        """
        return self._c_data[20][0]

    @individual_awareness_of_problem.setter  # set PRB.21
    def individual_awareness_of_problem(self, ce: CE | None):
        """
        id: PRB.21 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.21
        """
        self._c_data[20] = (ce,)

    @property  # get PRB.22
    def problem_prognosis(self) -> CE | None:
        """
        id: PRB.22 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.22
        """
        return self._c_data[21][0]

    @problem_prognosis.setter  # set PRB.22
    def problem_prognosis(self, ce: CE | None):
        """
        id: PRB.22 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.22
        """
        self._c_data[21] = (ce,)

    @property  # get PRB.23
    def individual_awareness_of_prognosis(self) -> CE | None:
        """
        id: PRB.23 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.23
        """
        return self._c_data[22][0]

    @individual_awareness_of_prognosis.setter  # set PRB.23
    def individual_awareness_of_prognosis(self, ce: CE | None):
        """
        id: PRB.23 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.23
        """
        self._c_data[22] = (ce,)

    @property  # get PRB.24
    def family_or_significant_other_awareness_of_problem_or_prognosis(
        self,
    ) -> ST | None:
        """
        id: PRB.24 | len: 200 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.24
        """
        return self._c_data[23][0]

    @family_or_significant_other_awareness_of_problem_or_prognosis.setter  # set PRB.24
    def family_or_significant_other_awareness_of_problem_or_prognosis(
        self, st: ST | None
    ):
        """
        id: PRB.24 | len: 200 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.24
        """
        self._c_data[23] = (st,)

    @property  # get PRB.25
    def security_or_sensitivity(self) -> CE | None:
        """
        id: PRB.25 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.25
        """
        return self._c_data[24][0]

    @security_or_sensitivity.setter  # set PRB.25
    def security_or_sensitivity(self, ce: CE | None):
        """
        id: PRB.25 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRB.25
        """
        self._c_data[24] = (ce,)
