from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CTI import CTI
from ..segments.ORC import ORC
from ..segment_groups.OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP import (
    OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP,
)
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segment_groups.OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP import (
    OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP,
)


"""
ORDER - OUL_R22_SPECIMEN_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OUL_R22_SPECIMEN_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OUL_R22_SPECIMEN_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR, CTI, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP, OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP
)

oul_r22_specimen_group_order_group = OUL_R22_SPECIMEN_GROUP_ORDER_GROUP(  # ORDER - Segment group for OUL_R22_SPECIMEN_GROUP - SPECIMEN consisting of OBR, ORC|None, NTE|None, TIMING QTY|None, RESULT|None, CTI|None
    observation_request=obr,  # OBR(...)  # Required.
    common_order=None,  # ORC(...) 
    notes_and_comments=None,  # NTE(...) 
    timing_qty=None,  # OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP(...) 
    result=None,  # OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP(...) 
    clinical_trial_identification=None,  # CTI(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OUL_R22_SPECIMEN_GROUP_ORDER_GROUP TEMPLATE-----
"""


class OUL_R22_SPECIMEN_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OUL_R22_SPECIMEN_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for OUL_R22_SPECIMEN_GROUP - SPECIMEN consisting of OBR, ORC|None, NTE|None, TIMING QTY|None, RESULT|None, CTI|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R22_SPECIMEN_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O")
    _c_aliases = ("13", "14", "15", "None", "None", "22")
    _c_components = (OBR, ORC, NTE, OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP, OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP, CTI)
    _c_name = ("OBR", "ORC", "NTE", "TIMING QTY", "RESULT", "CTI")
    _c_is_group = (False, False, False, True, True, False)
    _c_attrs = ("observation_request", "common_order", "notes_and_comments", "timing_qty", "result", "clinical_trial_identification",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.13
        common_order: ORC | None = None,  #  ORC.14
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.15
        timing_qty: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP
        | tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP, ...]
        | None = None,  #  (TQ1.16, TQ2.17, ...)
        result: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP
        | tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP, ...]
        | None = None,  #  (OBX.18, TCD.19, SID.20, NTE.21, ...)
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.22
    ):
        """
        None - `OUL_R22_SPECIMEN_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R22_SPECIMEN_GROUP_ORDER_GROUP>`_
        Segment group for OUL_R22_SPECIMEN_GROUP - SPECIMEN consisting of OBR, ORC|None, NTE|None, TIMING QTY|None, RESULT|None, CTI|None

        :param observation_request: Observation Request (id: OBR | seq: 13 | use: R | rpt: 1)
        :param common_order: Common Order (id: ORC | seq: 14 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 15 | use: O | rpt: *)
        :param timing_qty: Timing Qty segment group: [TQ1, TQ2|None] (id: TIMING QTY | seq: 16, 17 | use: O | rpt: *)
        :param result: Result segment group: [OBX, TCD|None, SID|None, NTE|None] (id: RESULT | seq: 18, 19, 20, 21 | use: O | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 22 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.observation_request = observation_request
        self.common_order = common_order
        self.notes_and_comments = notes_and_comments
        self.timing_qty = timing_qty
        self.result = result
        self.clinical_trial_identification = clinical_trial_identification

    @property  # get OBR.13
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 13
        ---
        return_type: OBR.13: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[0][0]

    @observation_request.setter  # set OBR.13
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 13
        ---
        param_type: OBR.13: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[0] = (obr,)

    @property  # get ORC.14
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 14
        ---
        return_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[1][0]

    @common_order.setter  # set ORC.14
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 14
        ---
        param_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[1] = (orc,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: NTE.15 | tuple[NTE, ...]: (Notes and Comments, ...)
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
    ) -> tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP, ...] | tuple[None]:
        """
        id: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP
        """
        return self._c_data[3]

    @timing_qty.setter  # set TIMING QTY
    def timing_qty(
        self,
        timing_qty: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP
        | tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP, ...]
        | None,
    ):
        """
        id: TIMING QTY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP.None | tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_TIMING_QTY_GROUP
        """
        if isinstance(timing_qty, tuple):
            self._c_data[3] = timing_qty
        else:
            self._c_data[3] = (timing_qty,)

    @property  # get RESULT
    def result(
        self,
    ) -> tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP, ...] | tuple[None]:
        """
        id: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP
        """
        return self._c_data[4]

    @result.setter  # set RESULT
    def result(
        self,
        result: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP
        | tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP, ...]
        | None,
    ):
        """
        id: RESULT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP.None | tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R22_SPECIMEN_GROUP_ORDER_GROUP_RESULT_GROUP
        """
        if isinstance(result, tuple):
            self._c_data[4] = result
        else:
            self._c_data[4] = (result,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[5]

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
            self._c_data[5] = cti
        else:
            self._c_data[5] = (cti,)
