from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.OMB_O27_ORDER_GROUP_OBSERVATION_GROUP import (
    OMB_O27_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segments.ORC import ORC
from ..segment_groups.OMB_O27_ORDER_GROUP_TIMING_GROUP import (
    OMB_O27_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.BLG import BLG
from ..segments.BPO import BPO
from ..segments.SPM import SPM
from ..segments.FT1 import FT1


"""
ORDER - OMB_O27_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMB_O27_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMB_O27_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    DG1, NTE, ORC, BLG, SPM, FT1, BPO
)
from utils.hl7.v2_5_1.segment_groups import (
    OMB_O27_ORDER_GROUP_TIMING_GROUP, OMB_O27_ORDER_GROUP_OBSERVATION_GROUP
)

omb_o27_order_group = OMB_O27_ORDER_GROUP(  # ORDER - Segment group for OMB_O27 - Blood Product Order consisting of ORC, TIMING|None, BPO, SPM|None, NTE|None, DG1|None, OBSERVATION|None, FT1|None, BLG|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # OMB_O27_ORDER_GROUP_TIMING_GROUP(...) 
    blood_product_order=bpo,  # BPO(...)  # Required.
    specimen=None,  # SPM(...) 
    notes_and_comments=None,  # NTE(...) 
    diagnosis=None,  # DG1(...) 
    observation=None,  # OMB_O27_ORDER_GROUP_OBSERVATION_GROUP(...) 
    financial_transaction=None,  # FT1(...) 
    billing=None,  # BLG(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMB_O27_ORDER_GROUP TEMPLATE-----
"""


class OMB_O27_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMB_O27_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for OMB_O27 - Blood Product Order consisting of ORC, TIMING|None, BPO, SPM|None, NTE|None, DG1|None, OBSERVATION|None, FT1|None, BLG|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMB_O27_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535, 65535, 65535, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("14", "None", "17", "18", "19", "20", "None", "23", "24")
    _c_components = (ORC, OMB_O27_ORDER_GROUP_TIMING_GROUP, BPO, SPM, NTE, DG1, OMB_O27_ORDER_GROUP_OBSERVATION_GROUP, FT1, BLG)
    _c_name = ("ORC", "TIMING", "BPO", "SPM", "NTE", "DG1", "OBSERVATION", "FT1", "BLG")
    _c_is_group = (False, True, False, False, False, False, True, False, False)
    _c_attrs = ("common_order", "timing", "blood_product_order", "specimen", "notes_and_comments", "diagnosis", "observation", "financial_transaction", "billing",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.14
        blood_product_order: BPO,  #  Required. BPO.17
        timing: OMB_O27_ORDER_GROUP_TIMING_GROUP
        | tuple[OMB_O27_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.15, TQ2.16, ...)
        specimen: SPM | None = None,  #  SPM.18
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.19
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.20
        observation: OMB_O27_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[OMB_O27_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.21, NTE.22, ...)
        financial_transaction: FT1 | tuple[FT1, ...] | None = None,  #  FT1.23
        billing: BLG | None = None,  #  BLG.24
    ):
        """
        None - `OMB_O27_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMB_O27_ORDER_GROUP>`_
        Segment group for OMB_O27 - Blood Product Order consisting of ORC, TIMING|None, BPO, SPM|None, NTE|None, DG1|None, OBSERVATION|None, FT1|None, BLG|None

        :param common_order: Common Order (id: ORC | seq: 14 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 15, 16 | use: O | rpt: *)
        :param blood_product_order: Blood product order (id: BPO | seq: 17 | use: R | rpt: 1)
        :param specimen: Specimen (id: SPM | seq: 18 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 19 | use: O | rpt: *)
        :param diagnosis: Diagnosis (id: DG1 | seq: 20 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 21, 22 | use: O | rpt: *)
        :param financial_transaction: Financial Transaction (id: FT1 | seq: 23 | use: O | rpt: *)
        :param billing: Billing (id: BLG | seq: 24 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.common_order = common_order
        self.timing = timing
        self.blood_product_order = blood_product_order
        self.specimen = specimen
        self.notes_and_comments = notes_and_comments
        self.diagnosis = diagnosis
        self.observation = observation
        self.financial_transaction = financial_transaction
        self.billing = billing

    @property  # get ORC.14
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 14
        ---
        return_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.14
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 14
        ---
        param_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(self) -> tuple[OMB_O27_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: OMB_O27_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMB_O27_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMB_O27_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: OMB_O27_ORDER_GROUP_TIMING_GROUP
        | tuple[OMB_O27_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMB_O27_ORDER_GROUP_TIMING_GROUP.None | tuple[OMB_O27_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMB_O27_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get BPO.17
    def blood_product_order(self) -> BPO:
        """
        id: BPO | use: R | rpt: 1 | seq: 17
        ---
        return_type: BPO.17: Blood product order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPO
        """
        return self._c_data[2][0]

    @blood_product_order.setter  # set BPO.17
    def blood_product_order(self, bpo: BPO):
        """
        id: BPO | use: R | rpt: 1 | seq: 17
        ---
        param_type: BPO.17: Blood product order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPO
        """
        self._c_data[2] = (bpo,)

    @property  # get SPM.18
    def specimen(self) -> SPM | None:
        """
        id: SPM | use: O | rpt: 1 | seq: 18
        ---
        return_type: SPM.18: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[3][0]

    @specimen.setter  # set SPM.18
    def specimen(self, spm: SPM | None):
        """
        id: SPM | use: O | rpt: 1 | seq: 18
        ---
        param_type: SPM.18: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[3] = (spm,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[4]

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
            self._c_data[4] = nte
        else:
            self._c_data[4] = (nte,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[5]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        param_type: DG1.20 | tuple[DG1, ...]: (Diagnosis, ...)
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
    ) -> tuple[OMB_O27_ORDER_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: OMB_O27_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMB_O27_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMB_O27_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[6]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: OMB_O27_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[OMB_O27_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMB_O27_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[OMB_O27_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMB_O27_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[6] = observation
        else:
            self._c_data[6] = (observation,)

    @property  # get FT1
    def financial_transaction(self) -> tuple[FT1, ...] | tuple[None]:
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        return_type: tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        return self._c_data[7]

    @financial_transaction.setter  # set FT1
    def financial_transaction(self, ft1: FT1 | tuple[FT1, ...] | None):
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        param_type: FT1.23 | tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        if isinstance(ft1, tuple):
            self._c_data[7] = ft1
        else:
            self._c_data[7] = (ft1,)

    @property  # get BLG.24
    def billing(self) -> BLG | None:
        """
        id: BLG | use: O | rpt: 1 | seq: 24
        ---
        return_type: BLG.24: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        return self._c_data[8][0]

    @billing.setter  # set BLG.24
    def billing(self, blg: BLG | None):
        """
        id: BLG | use: O | rpt: 1 | seq: 24
        ---
        param_type: BLG.24: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        self._c_data[8] = (blg,)
