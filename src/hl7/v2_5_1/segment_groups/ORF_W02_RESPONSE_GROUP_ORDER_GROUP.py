from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CTI import CTI
from ..segments.CTD import CTD
from ..segments.ORC import ORC
from ..segment_groups.ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP import (
    ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segments.NTE import NTE
from ..segments.OBR import OBR


"""
ORDER - ORF_W02_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORF_W02_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORF_W02_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    CTD, NTE, ORC, OBR, CTI
)
from utils.hl7.v2_5_1.segment_groups import (
    ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
)

orf_w02_response_group_order_group = ORF_W02_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for ORF_W02_RESPONSE_GROUP - RESPONSE consisting of ORC|None, OBR, NTE|None, CTD|None, OBSERVATION, CTI|None
    common_order=None,  # ORC(...) 
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    contact_data=None,  # CTD(...) 
    observation=orf_w02_response_group_order_group_observation_group,  # ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP(...)  # Required.
    clinical_trial_identification=None,  # CTI(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORF_W02_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class ORF_W02_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORF_W02_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for ORF_W02_RESPONSE_GROUP - RESPONSE consisting of ORC|None, OBR, NTE|None, CTD|None, OBSERVATION, CTI|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORF_W02_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1, 65535, 65535)
    _c_usage = ("O", "R", "O", "O", "R", "O")
    _c_aliases = ("8", "9", "10", "11", "None", "14")
    _c_components = (ORC, OBR, NTE, CTD, ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, CTI)
    _c_name = ("ORC", "OBR", "NTE", "CTD", "OBSERVATION", "CTI")
    _c_is_group = (False, False, False, False, True, False)
    _c_attrs = ("common_order", "observation_request", "notes_and_comments", "contact_data", "observation", "clinical_trial_identification",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.9
        observation: ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[
            ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, ...
        ],  #  Required. (OBX.12, NTE.13, ...)
        common_order: ORC | None = None,  #  ORC.8
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.10
        contact_data: CTD | None = None,  #  CTD.11
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.14
    ):
        """
        None - `ORF_W02_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORF_W02_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for ORF_W02_RESPONSE_GROUP - RESPONSE consisting of ORC|None, OBR, NTE|None, CTD|None, OBSERVATION, CTI|None

        :param common_order: Common Order (id: ORC | seq: 8 | use: O | rpt: 1)
        :param observation_request: Observation Request (id: OBR | seq: 9 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 10 | use: O | rpt: *)
        :param contact_data: Contact Data (id: CTD | seq: 11 | use: O | rpt: 1)
        :param observation: Observation segment group: [OBX|None, NTE|None] (id: OBSERVATION | seq: 12, 13 | use: R | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 14 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.common_order = common_order
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.contact_data = contact_data
        self.observation = observation
        self.clinical_trial_identification = clinical_trial_identification

    @property  # get ORC.8
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 8
        ---
        return_type: ORC.8: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.8
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 8
        ---
        param_type: ORC.8: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get OBR.9
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 9
        ---
        return_type: OBR.9: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[1][0]

    @observation_request.setter  # set OBR.9
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 9
        ---
        param_type: OBR.9: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[1] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: NTE.10 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get CTD.11
    def contact_data(self) -> CTD | None:
        """
        id: CTD | use: O | rpt: 1 | seq: 11
        ---
        return_type: CTD.11: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[3][0]

    @contact_data.setter  # set CTD.11
    def contact_data(self, ctd: CTD | None):
        """
        id: CTD | use: O | rpt: 1 | seq: 11
        ---
        param_type: CTD.11: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        self._c_data[3] = (ctd,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, ...]:
        """
        id: ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[4]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, ...],
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[4] = observation
        else:
            self._c_data[4] = (observation,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[5]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        param_type: CTI.14 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[5] = cti
        else:
            self._c_data[5] = (cti,)
