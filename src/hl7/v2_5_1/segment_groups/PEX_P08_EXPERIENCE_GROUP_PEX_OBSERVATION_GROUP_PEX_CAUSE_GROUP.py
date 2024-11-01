from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP,
)
from ..segment_groups.PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP,
)
from ..segments.PCR import PCR
from ..segments.PRB import PRB
from ..segment_groups.PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP,
)
from ..segments.OBX import OBX
from ..segment_groups.PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP,
)
from ..segments.NTE import NTE


"""
PEX CAUSE - PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, PCR, PRB, OBX
)
from utils.hl7.v2_5_1.segment_groups import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP, PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP, PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP, PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP
)

pex_p08_experience_group_pex_observation_group_pex_cause_group = PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP(  # PEX CAUSE - Segment group for PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP - PEX OBSERVATION consisting of PCR, RX ORDER|None, RX ADMINISTRATION|None, PRB|None, OBX|None, NTE|None, ASSOCIATED PERSON|None, STUDY|None
    possible_causal_relationship=pcr,  # PCR(...)  # Required.
    rx_order=None,  # PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP(...) 
    rx_administration=None,  # PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP(...) 
    problem_details=None,  # PRB(...) 
    observation_or_result=None,  # OBX(...) 
    notes_and_comments=None,  # NTE(...) 
    associated_person=None,  # PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP(...) 
    study=None,  # PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP TEMPLATE-----
"""


class PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP"""
    _hl7_name = """PEX CAUSE"""
    _hl7_description = """Segment group for PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP - PEX OBSERVATION consisting of PCR, RX ORDER|None, RX ADMINISTRATION|None, PRB|None, OBX|None, NTE|None, ASSOCIATED PERSON|None, STUDY|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("11", "None", "None", "18", "19", "20", "None", "None")
    _c_components = (PCR, PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP, PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP, PRB, OBX, NTE, PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP, PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP)
    _c_name = ("PCR", "RX ORDER", "RX ADMINISTRATION", "PRB", "OBX", "NTE", "ASSOCIATED PERSON", "STUDY")
    _c_is_group = (False, True, True, False, False, False, True, True)
    _c_attrs = ("possible_causal_relationship", "rx_order", "rx_administration", "problem_details", "observation_or_result", "notes_and_comments", "associated_person", "study",)
    # fmt: on

    def __init__(
        self,
        possible_causal_relationship: PCR,  #  Required. PCR.11
        rx_order: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP
        | None = None,  #  RXE.12, RXR.15
        rx_administration: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP
        | tuple[
            PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP,
            ...,
        ]
        | None = None,  #  (RXA.16, RXR.17, ...)
        problem_details: PRB | tuple[PRB, ...] | None = None,  #  PRB.18
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.19
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.20
        associated_person: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP
        | None = None,  #  NK1.21, PRB.28, OBX.29
        study: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP
        | tuple[
            PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP,
            ...,
        ]
        | None = None,  #  (CSR.30, CSP.31, ...)
    ):
        """
        None - `PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP>`_
        Segment group for PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP - PEX OBSERVATION consisting of PCR, RX ORDER|None, RX ADMINISTRATION|None, PRB|None, OBX|None, NTE|None, ASSOCIATED PERSON|None, STUDY|None

        :param possible_causal_relationship: Possible Causal Relationship (id: PCR | seq: 11 | use: R | rpt: 1)
        :param rx_order: Rx Order segment group: [RXE, TIMING QTY, RXR|None] (id: RX ORDER | seq: 12, None, 15 | use: O | rpt: 1)
        :param rx_administration: Rx Administration segment group: [RXA, RXR|None] (id: RX ADMINISTRATION | seq: 16, 17 | use: O | rpt: *)
        :param problem_details: Problem Details (id: PRB | seq: 18 | use: O | rpt: *)
        :param observation_or_result: Observation/Result (id: OBX | seq: 19 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 20 | use: O | rpt: *)
        :param associated_person: Associated Person segment group: [NK1, ASSOCIATED RX ORDER|None, ASSOCIATED RX ADMIN|None, PRB|None, OBX|None] (id: ASSOCIATED PERSON | seq: 21, None, None, 28, 29 | use: O | rpt: 1)
        :param study: Study segment group: [CSR, CSP|None] (id: STUDY | seq: 30, 31 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.possible_causal_relationship = possible_causal_relationship
        self.rx_order = rx_order
        self.rx_administration = rx_administration
        self.problem_details = problem_details
        self.observation_or_result = observation_or_result
        self.notes_and_comments = notes_and_comments
        self.associated_person = associated_person
        self.study = study

    @property  # get PCR.11
    def possible_causal_relationship(self) -> PCR:
        """
        id: PCR | use: R | rpt: 1 | seq: 11
        ---
        return_type: PCR.11: Possible Causal Relationship
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PCR
        """
        return self._c_data[0][0]

    @possible_causal_relationship.setter  # set PCR.11
    def possible_causal_relationship(self, pcr: PCR):
        """
        id: PCR | use: R | rpt: 1 | seq: 11
        ---
        param_type: PCR.11: Possible Causal Relationship
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PCR
        """
        self._c_data[0] = (pcr,)

    @property  # get PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP.None
    def rx_order(
        self,
    ) -> (
        PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP
        | None
    ):
        """
        id: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP
        """
        return self._c_data[1][0]

    @rx_order.setter  # set PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP.None
    def rx_order(
        self,
        rx_order: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP
        | None,
    ):
        """
        id: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP
        """
        self._c_data[1] = (rx_order,)

    @property  # get RX ADMINISTRATION
    def rx_administration(
        self,
    ) -> (
        tuple[
            PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP
        """
        return self._c_data[2]

    @rx_administration.setter  # set RX ADMINISTRATION
    def rx_administration(
        self,
        rx_admin_istration: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP
        | tuple[
            PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: RX ADMINISTRATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP.None | tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ADMINISTRATION_GROUP
        """
        if isinstance(rx_admin_istration, tuple):
            self._c_data[2] = rx_admin_istration
        else:
            self._c_data[2] = (rx_admin_istration,)

    @property  # get PRB
    def problem_details(self) -> tuple[PRB, ...] | tuple[None]:
        """
        id: PRB SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[PRB, ...]: (Problem Details, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB
        """
        return self._c_data[3]

    @problem_details.setter  # set PRB
    def problem_details(self, prb: PRB | tuple[PRB, ...] | None):
        """
        id: PRB SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        param_type: PRB.18 | tuple[PRB, ...]: (Problem Details, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB
        """
        if isinstance(prb, tuple):
            self._c_data[3] = prb
        else:
            self._c_data[3] = (prb,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[4]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        param_type: OBX.19 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[4] = obx
        else:
            self._c_data[4] = (obx,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[5]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        param_type: NTE.20 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[5] = nte
        else:
            self._c_data[5] = (nte,)

    @property  # get PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP.None
    def associated_person(
        self,
    ) -> (
        PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP
        | None
    ):
        """
        id: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP
        """
        return self._c_data[6][0]

    @associated_person.setter  # set PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP.None
    def associated_person(
        self,
        associated_person: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP
        | None,
    ):
        """
        id: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP
        """
        self._c_data[6] = (associated_person,)

    @property  # get STUDY
    def study(
        self,
    ) -> (
        tuple[
            PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP
        """
        return self._c_data[7]

    @study.setter  # set STUDY
    def study(
        self,
        study: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP
        | tuple[
            PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: STUDY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP.None | tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP
        """
        if isinstance(study, tuple):
            self._c_data[7] = study
        else:
            self._c_data[7] = (study,)
