from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CTD import CTD
from ..segment_groups.ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP import (
    ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP,
)
from ..segment_groups.ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP import (
    ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP,
)
from ..segments.ORC import ORC
from ..segments.FT1 import FT1
from ..segment_groups.ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP import (
    ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP,
)
from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR


"""
ORDER OBSERVATION - ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    CTD, OBR, FT1, CTI, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP
)

oru_r01_patient_result_group_order_observation_group = ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP(  # ORDER OBSERVATION - Segment group for ORU_R01_PATIENT_RESULT_GROUP - PATIENT RESULT consisting of ORC|None, OBR, NTE|None, TIMING QTY|None, CTD|None, OBSERVATION|None, FT1|None, CTI|None, SPECIMEN|None
    common_order=None,  # ORC(...) 
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    timing_qty=None,  # ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP(...) 
    contact_data=None,  # CTD(...) 
    observation=None,  # ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP(...) 
    financial_transaction=None,  # FT1(...) 
    clinical_trial_identification=None,  # CTI(...) 
    specimen=None,  # ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP TEMPLATE-----
"""


class ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP"""
    _hl7_name = """ORDER OBSERVATION"""
    _hl7_description = """Segment group for ORU_R01_PATIENT_RESULT_GROUP - PATIENT RESULT consisting of ORC|None, OBR, NTE|None, TIMING QTY|None, CTD|None, OBSERVATION|None, FT1|None, CTI|None, SPECIMEN|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 1, 65535, 65535, 65535, 65535)
    _c_usage = ("O", "R", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("9", "10", "11", "None", "14", "None", "17", "18", "None")
    _c_components = (ORC, OBR, NTE, ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, CTD, ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, FT1, CTI, ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP)
    _c_name = ("ORC", "OBR", "NTE", "TIMING QTY", "CTD", "OBSERVATION", "FT1", "CTI", "SPECIMEN")
    _c_is_group = (False, False, False, True, False, True, False, False, True)
    _c_attrs = ("common_order", "observation_request", "notes_and_comments", "timing_qty", "contact_data", "observation", "financial_transaction", "clinical_trial_identification", "specimen",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.10
        common_order: ORC | None = None,  #  ORC.9
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.11
        timing_qty: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP
        | tuple[
            ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...
        ]
        | None = None,  #  (TQ1.12, TQ2.13, ...)
        contact_data: CTD | None = None,  #  CTD.14
        observation: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        | tuple[
            ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...
        ]
        | None = None,  #  (OBX.15, NTE.16, ...)
        financial_transaction: FT1 | tuple[FT1, ...] | None = None,  #  FT1.17
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.18
        specimen: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP
        | tuple[
            ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP, ...
        ]
        | None = None,  #  (SPM.19, OBX.20, ...)
    ):
        """
        None - `ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP>`_
        Segment group for ORU_R01_PATIENT_RESULT_GROUP - PATIENT RESULT consisting of ORC|None, OBR, NTE|None, TIMING QTY|None, CTD|None, OBSERVATION|None, FT1|None, CTI|None, SPECIMEN|None

        :param common_order: Common Order (id: ORC | seq: 9 | use: O | rpt: 1)
        :param observation_request: Observation Request (id: OBR | seq: 10 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 11 | use: O | rpt: *)
        :param timing_qty: Timing Qty segment group: [TQ1, TQ2|None] (id: TIMING QTY | seq: 12, 13 | use: O | rpt: *)
        :param contact_data: Contact Data (id: CTD | seq: 14 | use: O | rpt: 1)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 15, 16 | use: O | rpt: *)
        :param financial_transaction: Financial Transaction (id: FT1 | seq: 17 | use: O | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 18 | use: O | rpt: *)
        :param specimen: Specimen segment group: [SPM, OBX|None] (id: SPECIMEN | seq: 19, 20 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.common_order = common_order
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.timing_qty = timing_qty
        self.contact_data = contact_data
        self.observation = observation
        self.financial_transaction = financial_transaction
        self.clinical_trial_identification = clinical_trial_identification
        self.specimen = specimen

    @property  # get ORC.9
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 9
        ---
        return_type: ORC.9: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.9
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 9
        ---
        param_type: ORC.9: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get OBR.10
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 10
        ---
        return_type: OBR.10: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[1][0]

    @observation_request.setter  # set OBR.10
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 10
        ---
        param_type: OBR.10: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[1] = (obr,)

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
    ) -> (
        tuple[
            ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...
        ]
        | tuple[None]
    ):
        """
        id: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP
        """
        return self._c_data[3]

    @timing_qty.setter  # set TIMING QTY
    def timing_qty(
        self,
        timing_qty: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP
        | tuple[
            ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...
        ]
        | None,
    ):
        """
        id: TIMING QTY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP.None | tuple[ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_TIMING_QTY_GROUP
        """
        if isinstance(timing_qty, tuple):
            self._c_data[3] = timing_qty
        else:
            self._c_data[3] = (timing_qty,)

    @property  # get CTD.14
    def contact_data(self) -> CTD | None:
        """
        id: CTD | use: O | rpt: 1 | seq: 14
        ---
        return_type: CTD.14: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[4][0]

    @contact_data.setter  # set CTD.14
    def contact_data(self, ctd: CTD | None):
        """
        id: CTD | use: O | rpt: 1 | seq: 14
        ---
        param_type: CTD.14: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        self._c_data[4] = (ctd,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> (
        tuple[
            ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...
        ]
        | tuple[None]
    ):
        """
        id: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[5]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        | tuple[
            ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...
        ]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP.None | tuple[ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[5] = observation
        else:
            self._c_data[5] = (observation,)

    @property  # get FT1
    def financial_transaction(self) -> tuple[FT1, ...] | tuple[None]:
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        return_type: tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        return self._c_data[6]

    @financial_transaction.setter  # set FT1
    def financial_transaction(self, ft1: FT1 | tuple[FT1, ...] | None):
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        param_type: FT1.17 | tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        if isinstance(ft1, tuple):
            self._c_data[6] = ft1
        else:
            self._c_data[6] = (ft1,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[7]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        param_type: CTI.18 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[7] = cti
        else:
            self._c_data[7] = (cti,)

    @property  # get SPECIMEN
    def specimen(
        self,
    ) -> (
        tuple[ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP, ...]
        | tuple[None]
    ):
        """
        id: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP
        """
        return self._c_data[8]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self,
        specimen: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP
        | tuple[
            ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP, ...
        ]
        | None,
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP.None | tuple[ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[8] = specimen
        else:
            self._c_data[8] = (specimen,)
