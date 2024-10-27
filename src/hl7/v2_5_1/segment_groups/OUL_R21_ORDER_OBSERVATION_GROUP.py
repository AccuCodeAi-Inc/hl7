from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP import (
    OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP,
)
from ..segments.OBR import OBR
from ..segment_groups.OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP import (
    OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP,
)
from ..segments.ORC import ORC
from ..segment_groups.OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP import (
    OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP,
)
from ..segments.NTE import NTE
from ..segments.CTI import CTI


"""
ORDER OBSERVATION - OUL_R21_ORDER_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OUL_R21_ORDER_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OUL_R21_ORDER_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR, NTE, ORC, CTI
)
from utils.hl7.v2_5_1.segment_groups import (
    OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP, OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP
)

oul_r21_order_observation_group = OUL_R21_ORDER_OBSERVATION_GROUP(  # ORDER OBSERVATION - Segment group for OUL_R21 - Unsolicited laboratory observation consisting of CONTAINER|None, ORC|None, OBR, NTE|None, TIMING QTY|None, OBSERVATION, CTI|None
    container=None,  # OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP(...) 
    common_order=None,  # ORC(...) 
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    timing_qty=None,  # OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP(...) 
    observation=oul_r21_order_observation_group_observation_group,  # OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP(...)  # Required.
    clinical_trial_identification=None,  # CTI(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OUL_R21_ORDER_OBSERVATION_GROUP TEMPLATE-----
"""


class OUL_R21_ORDER_OBSERVATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OUL_R21_ORDER_OBSERVATION_GROUP"""
    _hl7_name = """ORDER OBSERVATION"""
    _hl7_description = """Segment group for OUL_R21 - Unsolicited laboratory observation consisting of CONTAINER|None, ORC|None, OBR, NTE|None, TIMING QTY|None, OBSERVATION, CTI|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R21_ORDER_OBSERVATION_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 65535, 65535, 65535, 65535)
    _c_usage = ("O", "O", "R", "O", "O", "R", "O")
    _c_aliases = ("None", "11", "12", "13", "None", "None", "20")
    _c_components = (OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP, ORC, OBR, NTE, OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, CTI)
    _c_name = ("CONTAINER", "ORC", "OBR", "NTE", "TIMING QTY", "OBSERVATION", "CTI")
    _c_is_group = (True, False, False, False, True, True, False)
    _c_attrs = ("container", "common_order", "observation_request", "notes_and_comments", "timing_qty", "observation", "clinical_trial_identification",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.12
        observation: OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        | tuple[
            OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...
        ],  #  Required. (OBX.16, TCD.17, SID.18, NTE.19, ...)
        container: OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP
        | None = None,  #  SAC.9, SID.10
        common_order: ORC | None = None,  #  ORC.11
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.13
        timing_qty: OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP
        | tuple[OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...]
        | None = None,  #  (TQ1.14, TQ2.15, ...)
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.20
    ):
        """
        None - `OUL_R21_ORDER_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R21_ORDER_OBSERVATION_GROUP>`_
        Segment group for OUL_R21 - Unsolicited laboratory observation consisting of CONTAINER|None, ORC|None, OBR, NTE|None, TIMING QTY|None, OBSERVATION, CTI|None

        :param container: Container segment group: [SAC, SID|None] (id: CONTAINER | seq: 9, 10 | use: O | rpt: 1)
        :param common_order: Common Order (id: ORC | seq: 11 | use: O | rpt: 1)
        :param observation_request: Observation Request (id: OBR | seq: 12 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 13 | use: O | rpt: *)
        :param timing_qty: Timing Qty segment group: [TQ1, TQ2|None] (id: TIMING QTY | seq: 14, 15 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX|None, TCD|None, SID|None, NTE|None] (id: OBSERVATION | seq: 16, 17, 18, 19 | use: R | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 20 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.container = container
        self.common_order = common_order
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.timing_qty = timing_qty
        self.observation = observation
        self.clinical_trial_identification = clinical_trial_identification

    @property  # get OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP.None
    def container(self) -> OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP | None:
        """
        id: OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP
        """
        return self._c_data[0][0]

    @container.setter  # set OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP.None
    def container(
        self, container: OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP | None
    ):
        """
        id: OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R21_ORDER_OBSERVATION_GROUP_CONTAINER_GROUP
        """
        self._c_data[0] = (container,)

    @property  # get ORC.11
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 11
        ---
        return_type: ORC.11: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[1][0]

    @common_order.setter  # set ORC.11
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 11
        ---
        param_type: ORC.11: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[1] = (orc,)

    @property  # get OBR.12
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 12
        ---
        return_type: OBR.12: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[2][0]

    @observation_request.setter  # set OBR.12
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 12
        ---
        param_type: OBR.12: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[2] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        param_type: NTE.13 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get TIMING QTY
    def timing_qty(
        self,
    ) -> tuple[OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...] | tuple[None]:
        """
        id: OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP
        """
        return self._c_data[4]

    @timing_qty.setter  # set TIMING QTY
    def timing_qty(
        self,
        timing_qty: OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP
        | tuple[OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...]
        | None,
    ):
        """
        id: TIMING QTY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP.None | tuple[OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R21_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP
        """
        if isinstance(timing_qty, tuple):
            self._c_data[4] = timing_qty
        else:
            self._c_data[4] = (timing_qty,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...]:
        """
        id: OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[5]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        | tuple[OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...],
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP.None | tuple[OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R21_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[5] = observation
        else:
            self._c_data[5] = (observation,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[6]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        param_type: CTI.20 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[6] = cti
        else:
            self._c_data[6] = (cti,)
