from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PRB import PRB
from ..segments.OBX import OBX
from ..segments.NK1 import NK1
from ..segment_groups.PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP import (
    PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP,
)
from ..segment_groups.PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP import (
    PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP,
)


"""
ASSOCIATED PERSON - PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP
from utils.hl7.v2_5_1.segments import (
    NK1, OBX, PRB
)
from utils.hl7.v2_5_1.segment_groups import (
    PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP, PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP
)

pex_p07_experience_group_pex_observation_group_pex_cause_group_associated_person_group = PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP(  # ASSOCIATED PERSON - Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP - PEX CAUSE consisting of NK1, ASSOCIATED RX ORDER|None, ASSOCIATED RX ADMIN|None, PRB|None, OBX|None
    next_of_kin_or_associated_parties=nk1,  # NK1(...)  # Required.
    associated_rx_order=None,  # PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP(...) 
    associated_rx_admin=None,  # PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP(...) 
    problem_details=None,  # PRB(...) 
    observation_or_result=None,  # OBX(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP TEMPLATE-----
"""


class PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP"""
    _hl7_name = """ASSOCIATED PERSON"""
    _hl7_description = """Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP - PEX CAUSE consisting of NK1, ASSOCIATED RX ORDER|None, ASSOCIATED RX ADMIN|None, PRB|None, OBX|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("21", "None", "None", "28", "29")
    _c_components = (NK1, PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP, PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP, PRB, OBX)
    _c_name = ("NK1", "ASSOCIATED RX ORDER", "ASSOCIATED RX ADMIN", "PRB", "OBX")
    _c_is_group = (False, True, True, False, False)
    _c_attrs = ("next_of_kin_or_associated_parties", "associated_rx_order", "associated_rx_admin", "problem_details", "observation_or_result",)
    # fmt: on

    def __init__(
        self,
        next_of_kin_or_associated_parties: NK1,  #  Required. NK1.21
        associated_rx_order: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP
        | None = None,  #  RXE.22, RXR.25
        associated_rx_admin: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP
        | tuple[
            PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP,
            ...,
        ]
        | None = None,  #  (RXA.26, RXR.27, ...)
        problem_details: PRB | tuple[PRB, ...] | None = None,  #  PRB.28
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.29
    ):
        """
        None - `PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP>`_
        Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP - PEX CAUSE consisting of NK1, ASSOCIATED RX ORDER|None, ASSOCIATED RX ADMIN|None, PRB|None, OBX|None

        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 21 | use: R | rpt: 1)
        :param associated_rx_order: Associated Rx Order segment group: [RXE, NK1 TIMING QTY, RXR|None] (id: ASSOCIATED RX ORDER | seq: 22, None, 25 | use: O | rpt: 1)
        :param associated_rx_admin: Associated Rx Admin segment group: [RXA, RXR|None] (id: ASSOCIATED RX ADMIN | seq: 26, 27 | use: O | rpt: *)
        :param problem_details: Problem Details (id: PRB | seq: 28 | use: O | rpt: *)
        :param observation_or_result: Observation/Result (id: OBX | seq: 29 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.associated_rx_order = associated_rx_order
        self.associated_rx_admin = associated_rx_admin
        self.problem_details = problem_details
        self.observation_or_result = observation_or_result

    @property  # get NK1.21
    def next_of_kin_or_associated_parties(self) -> NK1:
        """
        id: NK1 | use: R | rpt: 1 | seq: 21
        ---
        return_type: NK1.21: Next of Kin / Associated Parties
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[0][0]

    @next_of_kin_or_associated_parties.setter  # set NK1.21
    def next_of_kin_or_associated_parties(self, nk1: NK1):
        """
        id: NK1 | use: R | rpt: 1 | seq: 21
        ---
        param_type: NK1.21: Next of Kin / Associated Parties
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        self._c_data[0] = (nk1,)

    @property  # get PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP.None
    def associated_rx_order(
        self,
    ) -> (
        PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP
        | None
    ):
        """
        id: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP
        """
        return self._c_data[1][0]

    @associated_rx_order.setter  # set PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP.None
    def associated_rx_order(
        self,
        associated_rx_order: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP
        | None,
    ):
        """
        id: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP
        """
        self._c_data[1] = (associated_rx_order,)

    @property  # get ASSOCIATED RX ADMIN
    def associated_rx_admin(
        self,
    ) -> (
        tuple[
            PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP
        """
        return self._c_data[2]

    @associated_rx_admin.setter  # set ASSOCIATED RX ADMIN
    def associated_rx_admin(
        self,
        associated_rx_admin: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP
        | tuple[
            PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: ASSOCIATED RX ADMIN SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP.None | tuple[PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP
        """
        if isinstance(associated_rx_admin, tuple):
            self._c_data[2] = associated_rx_admin
        else:
            self._c_data[2] = (associated_rx_admin,)

    @property  # get PRB
    def problem_details(self) -> tuple[PRB, ...] | tuple[None]:
        """
        id: PRB SEGMENT GROUP | use: O | rpt: * | seq: 28
        ---
        return_type: tuple[PRB, ...]: (Problem Details, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB
        """
        return self._c_data[3]

    @problem_details.setter  # set PRB
    def problem_details(self, prb: PRB | tuple[PRB, ...] | None):
        """
        id: PRB SEGMENT GROUP | use: O | rpt: * | seq: 28
        ---
        param_type: PRB.28 | tuple[PRB, ...]: (Problem Details, ...)
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
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 29
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[4]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 29
        ---
        param_type: OBX.29 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[4] = obx
        else:
            self._c_data[4] = (obx,)
