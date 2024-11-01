from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CTD import CTD
from ..segments.BLG import BLG
from ..segment_groups.OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP import (
    OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP,
)
from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segment_groups.OMG_O19_ORDER_GROUP_OBSERVATION_GROUP import (
    OMG_O19_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segments.FT1 import FT1
from ..segments.CTI import CTI
from ..segment_groups.OMG_O19_ORDER_GROUP_TIMING_GROUP import (
    OMG_O19_ORDER_GROUP_TIMING_GROUP,
)
from ..segment_groups.OMG_O19_ORDER_GROUP_SPECIMEN_GROUP import (
    OMG_O19_ORDER_GROUP_SPECIMEN_GROUP,
)
from ..segments.ORC import ORC


"""
ORDER - OMG_O19_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMG_O19_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMG_O19_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, OBR, DG1, CTD, BLG, ORC, CTI, FT1
)
from utils.hl7.v2_5_1.segment_groups import (
    OMG_O19_ORDER_GROUP_OBSERVATION_GROUP, OMG_O19_ORDER_GROUP_SPECIMEN_GROUP, OMG_O19_ORDER_GROUP_TIMING_GROUP, OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP
)

omg_o19_order_group = OMG_O19_ORDER_GROUP(  # ORDER - Segment group for OMG_O19 - General Clinical Order consisting of ORC, TIMING|None, OBR, NTE|None, CTD|None, DG1|None, OBSERVATION|None, SPECIMEN|None, PRIOR RESULT|None, FT1|None, CTI|None, BLG|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # OMG_O19_ORDER_GROUP_TIMING_GROUP(...) 
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    contact_data=None,  # CTD(...) 
    diagnosis=None,  # DG1(...) 
    observation=None,  # OMG_O19_ORDER_GROUP_OBSERVATION_GROUP(...) 
    specimen=None,  # OMG_O19_ORDER_GROUP_SPECIMEN_GROUP(...) 
    prior_result=None,  # OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP(...) 
    financial_transaction=None,  # FT1(...) 
    clinical_trial_identification=None,  # CTI(...) 
    billing=None,  # BLG(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMG_O19_ORDER_GROUP TEMPLATE-----
"""


class OMG_O19_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMG_O19_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for OMG_O19 - General Clinical Order consisting of ORC, TIMING|None, OBR, NTE|None, CTD|None, DG1|None, OBSERVATION|None, SPECIMEN|None, PRIOR RESULT|None, FT1|None, CTI|None, BLG|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMG_O19_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 65535, 65535, 65535, 65535, 65535, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("15", "None", "18", "19", "20", "21", "None", "None", "None", "41", "42", "43")
    _c_components = (ORC, OMG_O19_ORDER_GROUP_TIMING_GROUP, OBR, NTE, CTD, DG1, OMG_O19_ORDER_GROUP_OBSERVATION_GROUP, OMG_O19_ORDER_GROUP_SPECIMEN_GROUP, OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP, FT1, CTI, BLG)
    _c_name = ("ORC", "TIMING", "OBR", "NTE", "CTD", "DG1", "OBSERVATION", "SPECIMEN", "PRIOR RESULT", "FT1", "CTI", "BLG")
    _c_is_group = (False, True, False, False, False, False, True, True, True, False, False, False)
    _c_attrs = ("common_order", "timing", "observation_request", "notes_and_comments", "contact_data", "diagnosis", "observation", "specimen", "prior_result", "financial_transaction", "clinical_trial_identification", "billing",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.15
        observation_request: OBR,  #  Required. OBR.18
        timing: OMG_O19_ORDER_GROUP_TIMING_GROUP
        | tuple[OMG_O19_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.16, TQ2.17, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.19
        contact_data: CTD | None = None,  #  CTD.20
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.21
        observation: OMG_O19_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[OMG_O19_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.22, NTE.23, ...)
        specimen: OMG_O19_ORDER_GROUP_SPECIMEN_GROUP
        | tuple[OMG_O19_ORDER_GROUP_SPECIMEN_GROUP, ...]
        | None = None,  #  (SPM.24, OBX.25, ...)
        prior_result: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP
        | tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP, ...]
        | None = None,  #  (AL1.32, ...)
        financial_transaction: FT1 | tuple[FT1, ...] | None = None,  #  FT1.41
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.42
        billing: BLG | None = None,  #  BLG.43
    ):
        """
        None - `OMG_O19_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMG_O19_ORDER_GROUP>`_
        Segment group for OMG_O19 - General Clinical Order consisting of ORC, TIMING|None, OBR, NTE|None, CTD|None, DG1|None, OBSERVATION|None, SPECIMEN|None, PRIOR RESULT|None, FT1|None, CTI|None, BLG|None

        :param common_order: Common Order (id: ORC | seq: 15 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 16, 17 | use: O | rpt: *)
        :param observation_request: Observation Request (id: OBR | seq: 18 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 19 | use: O | rpt: *)
        :param contact_data: Contact Data (id: CTD | seq: 20 | use: O | rpt: 1)
        :param diagnosis: Diagnosis (id: DG1 | seq: 21 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 22, 23 | use: O | rpt: *)
        :param specimen: Specimen segment group: [SPM, OBX|None, CONTAINER|None] (id: SPECIMEN | seq: 24, 25, None | use: O | rpt: *)
        :param prior_result: Prior Result segment group: [PATIENT PRIOR|None, PATIENT VISIT PRIOR|None, AL1|None, ORDER PRIOR] (id: PRIOR RESULT | seq: None, None, 32, None | use: O | rpt: *)
        :param financial_transaction: Financial Transaction (id: FT1 | seq: 41 | use: O | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 42 | use: O | rpt: *)
        :param billing: Billing (id: BLG | seq: 43 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.common_order = common_order
        self.timing = timing
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.contact_data = contact_data
        self.diagnosis = diagnosis
        self.observation = observation
        self.specimen = specimen
        self.prior_result = prior_result
        self.financial_transaction = financial_transaction
        self.clinical_trial_identification = clinical_trial_identification
        self.billing = billing

    @property  # get ORC.15
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 15
        ---
        return_type: ORC.15: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.15
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 15
        ---
        param_type: ORC.15: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(self) -> tuple[OMG_O19_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: OMG_O19_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMG_O19_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: OMG_O19_ORDER_GROUP_TIMING_GROUP
        | tuple[OMG_O19_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMG_O19_ORDER_GROUP_TIMING_GROUP.None | tuple[OMG_O19_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get OBR.18
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 18
        ---
        return_type: OBR.18: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[2][0]

    @observation_request.setter  # set OBR.18
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 18
        ---
        param_type: OBR.18: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[2] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        param_type: NTE.19 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get CTD.20
    def contact_data(self) -> CTD | None:
        """
        id: CTD | use: O | rpt: 1 | seq: 20
        ---
        return_type: CTD.20: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[4][0]

    @contact_data.setter  # set CTD.20
    def contact_data(self, ctd: CTD | None):
        """
        id: CTD | use: O | rpt: 1 | seq: 20
        ---
        param_type: CTD.20: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        self._c_data[4] = (ctd,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[5]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        param_type: DG1.21 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[5] = dg1
        else:
            self._c_data[5] = (dg1,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[OMG_O19_ORDER_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: OMG_O19_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMG_O19_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[6]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: OMG_O19_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[OMG_O19_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMG_O19_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[OMG_O19_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[6] = observation
        else:
            self._c_data[6] = (observation,)

    @property  # get SPECIMEN
    def specimen(self) -> tuple[OMG_O19_ORDER_GROUP_SPECIMEN_GROUP, ...] | tuple[None]:
        """
        id: OMG_O19_ORDER_GROUP_SPECIMEN_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMG_O19_ORDER_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_SPECIMEN_GROUP
        """
        return self._c_data[7]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self,
        specimen: OMG_O19_ORDER_GROUP_SPECIMEN_GROUP
        | tuple[OMG_O19_ORDER_GROUP_SPECIMEN_GROUP, ...]
        | None,
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMG_O19_ORDER_GROUP_SPECIMEN_GROUP.None | tuple[OMG_O19_ORDER_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[7] = specimen
        else:
            self._c_data[7] = (specimen,)

    @property  # get PRIOR RESULT
    def prior_result(
        self,
    ) -> tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP, ...] | tuple[None]:
        """
        id: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP
        """
        return self._c_data[8]

    @prior_result.setter  # set PRIOR RESULT
    def prior_result(
        self,
        prior_result: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP
        | tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP, ...]
        | None,
    ):
        """
        id: PRIOR RESULT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP.None | tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP
        """
        if isinstance(prior_result, tuple):
            self._c_data[8] = prior_result
        else:
            self._c_data[8] = (prior_result,)

    @property  # get FT1
    def financial_transaction(self) -> tuple[FT1, ...] | tuple[None]:
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 41
        ---
        return_type: tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        return self._c_data[9]

    @financial_transaction.setter  # set FT1
    def financial_transaction(self, ft1: FT1 | tuple[FT1, ...] | None):
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 41
        ---
        param_type: FT1.41 | tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        if isinstance(ft1, tuple):
            self._c_data[9] = ft1
        else:
            self._c_data[9] = (ft1,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 42
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[10]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 42
        ---
        param_type: CTI.42 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[10] = cti
        else:
            self._c_data[10] = (cti,)

    @property  # get BLG.43
    def billing(self) -> BLG | None:
        """
        id: BLG | use: O | rpt: 1 | seq: 43
        ---
        return_type: BLG.43: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        return self._c_data[11][0]

    @billing.setter  # set BLG.43
    def billing(self, blg: BLG | None):
        """
        id: BLG | use: O | rpt: 1 | seq: 43
        ---
        param_type: BLG.43: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        self._c_data[11] = (blg,)
