from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBR import OBR
from ..segment_groups.ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP import (
    ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.ORC import ORC
from ..segments.NTE import NTE
from ..segments.CTI import CTI
from ..segment_groups.ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP import (
    ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP,
)


"""
ORDER - ORG_O20_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORG_O20_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORG_O20_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR, NTE, ORC, CTI
)
from utils.hl7.v2_5_1.segment_groups import (
    ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP, ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
)

org_o20_response_group_order_group = ORG_O20_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for ORG_O20_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, OBR|None, NTE|None, CTI|None, SPECIMEN|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    observation_request=None,  # OBR(...) 
    notes_and_comments=None,  # NTE(...) 
    clinical_trial_identification=None,  # CTI(...) 
    specimen=None,  # ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORG_O20_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class ORG_O20_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORG_O20_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for ORG_O20_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, OBR|None, NTE|None, CTI|None, SPECIMEN|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORG_O20_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O")
    _c_aliases = ("8", "None", "11", "12", "13", "None")
    _c_components = (ORC, ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, OBR, NTE, CTI, ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP)
    _c_name = ("ORC", "TIMING", "OBR", "NTE", "CTI", "SPECIMEN")
    _c_is_group = (False, True, False, False, False, True)
    _c_attrs = ("common_order", "timing", "observation_request", "notes_and_comments", "clinical_trial_identification", "specimen",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.8
        timing: ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.9, TQ2.10, ...)
        observation_request: OBR | None = None,  #  OBR.11
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.12
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.13
        specimen: ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP
        | tuple[ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP, ...]
        | None = None,  #  (SPM.14, SAC.15, ...)
    ):
        """
        None - `ORG_O20_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORG_O20_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for ORG_O20_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, OBR|None, NTE|None, CTI|None, SPECIMEN|None

        :param common_order: Common Order (id: ORC | seq: 8 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 9, 10 | use: O | rpt: *)
        :param observation_request: Observation Request (id: OBR | seq: 11 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 12 | use: O | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 13 | use: O | rpt: *)
        :param specimen: Specimen segment group: [SPM, SAC|None] (id: SPECIMEN | seq: 14, 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.common_order = common_order
        self.timing = timing
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.clinical_trial_identification = clinical_trial_identification
        self.specimen = specimen

    @property  # get ORC.8
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 8
        ---
        return_type: ORC.8: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.8
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 8
        ---
        param_type: ORC.8: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(
        self,
    ) -> tuple[ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG_O20_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get OBR.11
    def observation_request(self) -> OBR | None:
        """
        id: OBR | use: O | rpt: 1 | seq: 11
        ---
        return_type: OBR.11: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[2][0]

    @observation_request.setter  # set OBR.11
    def observation_request(self, obr: OBR | None):
        """
        id: OBR | use: O | rpt: 1 | seq: 11
        ---
        param_type: OBR.11: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[2] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: NTE.12 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[4]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        param_type: CTI.13 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[4] = cti
        else:
            self._c_data[4] = (cti,)

    @property  # get SPECIMEN
    def specimen(
        self,
    ) -> tuple[ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP, ...] | tuple[None]:
        """
        id: ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP
        """
        return self._c_data[5]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self,
        specimen: ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP
        | tuple[ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP, ...]
        | None,
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP.None | tuple[ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG_O20_RESPONSE_GROUP_ORDER_GROUP_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[5] = specimen
        else:
            self._c_data[5] = (specimen,)
