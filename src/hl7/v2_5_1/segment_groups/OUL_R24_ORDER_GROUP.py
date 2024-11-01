from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.OUL_R24_ORDER_GROUP_RESULT_GROUP import (
    OUL_R24_ORDER_GROUP_RESULT_GROUP,
)
from ..segment_groups.OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP import (
    OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP,
)
from ..segments.NTE import NTE
from ..segment_groups.OUL_R24_ORDER_GROUP_SPECIMEN_GROUP import (
    OUL_R24_ORDER_GROUP_SPECIMEN_GROUP,
)
from ..segments.OBR import OBR
from ..segments.CTI import CTI
from ..segments.ORC import ORC


"""
ORDER - OUL_R24_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OUL_R24_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OUL_R24_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, ORC, CTI, OBR
)
from utils.hl7.v2_5_1.segment_groups import (
    OUL_R24_ORDER_GROUP_RESULT_GROUP, OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP, OUL_R24_ORDER_GROUP_SPECIMEN_GROUP
)

oul_r24_order_group = OUL_R24_ORDER_GROUP(  # ORDER - Segment group for OUL_R24 - Unsolicited Order Oriented Observation Message consisting of OBR, ORC|None, NTE|None, TIMING QTY|None, SPECIMEN|None, RESULT|None, CTI|None
    observation_request=obr,  # OBR(...)  # Required.
    common_order=None,  # ORC(...) 
    notes_and_comments=None,  # NTE(...) 
    timing_qty=None,  # OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP(...) 
    specimen=None,  # OUL_R24_ORDER_GROUP_SPECIMEN_GROUP(...) 
    result=None,  # OUL_R24_ORDER_GROUP_RESULT_GROUP(...) 
    clinical_trial_identification=None,  # CTI(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OUL_R24_ORDER_GROUP TEMPLATE-----
"""


class OUL_R24_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OUL_R24_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for OUL_R24 - Unsolicited Order Oriented Observation Message consisting of OBR, ORC|None, NTE|None, TIMING QTY|None, SPECIMEN|None, RESULT|None, CTI|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R24_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("9", "10", "11", "None", "None", "None", "22")
    _c_components = (OBR, ORC, NTE, OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP, OUL_R24_ORDER_GROUP_SPECIMEN_GROUP, OUL_R24_ORDER_GROUP_RESULT_GROUP, CTI)
    _c_name = ("OBR", "ORC", "NTE", "TIMING QTY", "SPECIMEN", "RESULT", "CTI")
    _c_is_group = (False, False, False, True, True, True, False)
    _c_attrs = ("observation_request", "common_order", "notes_and_comments", "timing_qty", "specimen", "result", "clinical_trial_identification",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.9
        common_order: ORC | None = None,  #  ORC.10
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.11
        timing_qty: OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP
        | tuple[OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP, ...]
        | None = None,  #  (TQ1.12, TQ2.13, ...)
        specimen: OUL_R24_ORDER_GROUP_SPECIMEN_GROUP
        | tuple[OUL_R24_ORDER_GROUP_SPECIMEN_GROUP, ...]
        | None = None,  #  (SPM.14, OBX.15, ...)
        result: OUL_R24_ORDER_GROUP_RESULT_GROUP
        | tuple[OUL_R24_ORDER_GROUP_RESULT_GROUP, ...]
        | None = None,  #  (OBX.18, TCD.19, SID.20, NTE.21, ...)
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.22
    ):
        """
        None - `OUL_R24_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R24_ORDER_GROUP>`_
        Segment group for OUL_R24 - Unsolicited Order Oriented Observation Message consisting of OBR, ORC|None, NTE|None, TIMING QTY|None, SPECIMEN|None, RESULT|None, CTI|None

        :param observation_request: Observation Request (id: OBR | seq: 9 | use: R | rpt: 1)
        :param common_order: Common Order (id: ORC | seq: 10 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 11 | use: O | rpt: *)
        :param timing_qty: Timing Qty segment group: [TQ1, TQ2|None] (id: TIMING QTY | seq: 12, 13 | use: O | rpt: *)
        :param specimen: Specimen segment group: [SPM, OBX|None, CONTAINER|None] (id: SPECIMEN | seq: 14, 15, None | use: O | rpt: *)
        :param result: Result segment group: [OBX, TCD|None, SID|None, NTE|None] (id: RESULT | seq: 18, 19, 20, 21 | use: O | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 22 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.observation_request = observation_request
        self.common_order = common_order
        self.notes_and_comments = notes_and_comments
        self.timing_qty = timing_qty
        self.specimen = specimen
        self.result = result
        self.clinical_trial_identification = clinical_trial_identification

    @property  # get OBR.9
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 9
        ---
        return_type: OBR.9: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[0][0]

    @observation_request.setter  # set OBR.9
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 9
        ---
        param_type: OBR.9: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[0] = (obr,)

    @property  # get ORC.10
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 10
        ---
        return_type: ORC.10: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[1][0]

    @common_order.setter  # set ORC.10
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 10
        ---
        param_type: ORC.10: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[1] = (orc,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: NTE.11 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get TIMING QTY
    def timing_qty(
        self,
    ) -> tuple[OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP, ...] | tuple[None]:
        """
        id: OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP
        """
        return self._c_data[3]

    @timing_qty.setter  # set TIMING QTY
    def timing_qty(
        self,
        timing_qty: OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP
        | tuple[OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP, ...]
        | None,
    ):
        """
        id: TIMING QTY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP.None | tuple[OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R24_ORDER_GROUP_TIMING_QTY_GROUP
        """
        if isinstance(timing_qty, tuple):
            self._c_data[3] = timing_qty
        else:
            self._c_data[3] = (timing_qty,)

    @property  # get SPECIMEN
    def specimen(self) -> tuple[OUL_R24_ORDER_GROUP_SPECIMEN_GROUP, ...] | tuple[None]:
        """
        id: OUL_R24_ORDER_GROUP_SPECIMEN_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R24_ORDER_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R24_ORDER_GROUP_SPECIMEN_GROUP
        """
        return self._c_data[4]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self,
        specimen: OUL_R24_ORDER_GROUP_SPECIMEN_GROUP
        | tuple[OUL_R24_ORDER_GROUP_SPECIMEN_GROUP, ...]
        | None,
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OUL_R24_ORDER_GROUP_SPECIMEN_GROUP.None | tuple[OUL_R24_ORDER_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R24_ORDER_GROUP_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[4] = specimen
        else:
            self._c_data[4] = (specimen,)

    @property  # get RESULT
    def result(self) -> tuple[OUL_R24_ORDER_GROUP_RESULT_GROUP, ...] | tuple[None]:
        """
        id: OUL_R24_ORDER_GROUP_RESULT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R24_ORDER_GROUP_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R24_ORDER_GROUP_RESULT_GROUP
        """
        return self._c_data[5]

    @result.setter  # set RESULT
    def result(
        self,
        result: OUL_R24_ORDER_GROUP_RESULT_GROUP
        | tuple[OUL_R24_ORDER_GROUP_RESULT_GROUP, ...]
        | None,
    ):
        """
        id: RESULT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OUL_R24_ORDER_GROUP_RESULT_GROUP.None | tuple[OUL_R24_ORDER_GROUP_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R24_ORDER_GROUP_RESULT_GROUP
        """
        if isinstance(result, tuple):
            self._c_data[5] = result
        else:
            self._c_data[5] = (result,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[6]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        param_type: CTI.22 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[6] = cti
        else:
            self._c_data[6] = (cti,)
