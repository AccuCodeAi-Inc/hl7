from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.BLG import BLG
from ..segments.FT1 import FT1
from ..segments.CTI import CTI
from ..segment_groups.OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP import (
    OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP,
)
from ..segment_groups.OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP import (
    OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP,
)
from ..segments.ORC import ORC


"""
ORDER - OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    BLG, ORC, CTI, FT1
)
from utils.hl7.v2_5_1.segment_groups import (
    OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP, OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
)

oml_o35_specimen_group_specimen_container_group_order_group = OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP(  # ORDER - Segment group for OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP - SPECIMEN CONTAINER consisting of ORC, TIIMING|None, OBSERVATION REQUEST|None, FT1|None, CTI|None, BLG|None
    common_order=orc,  # ORC(...)  # Required.
    tiiming=None,  # OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP(...) 
    observation_request=None,  # OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP(...) 
    financial_transaction=None,  # FT1(...) 
    clinical_trial_identification=None,  # CTI(...) 
    billing=None,  # BLG(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP TEMPLATE-----
"""


class OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP - SPECIMEN CONTAINER consisting of ORC, TIIMING|None, OBSERVATION REQUEST|None, FT1|None, CTI|None, BLG|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 65535, 1)
    _c_usage = ("R", "O", "O", "O", "O", "O")
    _c_aliases = ("18", "None", "None", "40", "41", "42")
    _c_components = (ORC, OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP, OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP, FT1, CTI, BLG)
    _c_name = ("ORC", "TIIMING", "OBSERVATION REQUEST", "FT1", "CTI", "BLG")
    _c_is_group = (False, True, True, False, False, False)
    _c_attrs = ("common_order", "tiiming", "observation_request", "financial_transaction", "clinical_trial_identification", "billing",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.18
        tiiming: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP
        | tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP,
            ...,
        ]
        | None = None,  #  (TQ1.19, TQ2.20, ...)
        observation_request: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
        | None = None,  #  OBR.21, TCD.22, NTE.23, DG1.24
        financial_transaction: FT1 | tuple[FT1, ...] | None = None,  #  FT1.40
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.41
        billing: BLG | None = None,  #  BLG.42
    ):
        """
        None - `OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP>`_
        Segment group for OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP - SPECIMEN CONTAINER consisting of ORC, TIIMING|None, OBSERVATION REQUEST|None, FT1|None, CTI|None, BLG|None

        :param common_order: Common Order (id: ORC | seq: 18 | use: R | rpt: 1)
        :param tiiming: Tiiming segment group: [TQ1, TQ2|None] (id: TIIMING | seq: 19, 20 | use: O | rpt: *)
        :param observation_request: Observation Request segment group: [OBR, TCD|None, NTE|None, DG1|None, OBSERVATION|None, PRIOR RESULT|None] (id: OBSERVATION REQUEST | seq: 21, 22, 23, 24, None, None | use: O | rpt: 1)
        :param financial_transaction: Financial Transaction (id: FT1 | seq: 40 | use: O | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 41 | use: O | rpt: *)
        :param billing: Billing (id: BLG | seq: 42 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.common_order = common_order
        self.tiiming = tiiming
        self.observation_request = observation_request
        self.financial_transaction = financial_transaction
        self.clinical_trial_identification = clinical_trial_identification
        self.billing = billing

    @property  # get ORC.18
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 18
        ---
        return_type: ORC.18: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.18
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 18
        ---
        param_type: ORC.18: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIIMING
    def tiiming(
        self,
    ) -> (
        tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP
        """
        return self._c_data[1]

    @tiiming.setter  # set TIIMING
    def tiiming(
        self,
        tiiming: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP
        | tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: TIIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP.None | tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIIMING_GROUP
        """
        if isinstance(tiiming, tuple):
            self._c_data[1] = tiiming
        else:
            self._c_data[1] = (tiiming,)

    @property  # get OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP.None
    def observation_request(
        self,
    ) -> (
        OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
        | None
    ):
        """
        id: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
        """
        return self._c_data[2][0]

    @observation_request.setter  # set OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP.None
    def observation_request(
        self,
        observation_request: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
        | None,
    ):
        """
        id: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
        """
        self._c_data[2] = (observation_request,)

    @property  # get FT1
    def financial_transaction(self) -> tuple[FT1, ...] | tuple[None]:
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 40
        ---
        return_type: tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        return self._c_data[3]

    @financial_transaction.setter  # set FT1
    def financial_transaction(self, ft1: FT1 | tuple[FT1, ...] | None):
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 40
        ---
        param_type: FT1.40 | tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        if isinstance(ft1, tuple):
            self._c_data[3] = ft1
        else:
            self._c_data[3] = (ft1,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 41
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[4]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 41
        ---
        param_type: CTI.41 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[4] = cti
        else:
            self._c_data[4] = (cti,)

    @property  # get BLG.42
    def billing(self) -> BLG | None:
        """
        id: BLG | use: O | rpt: 1 | seq: 42
        ---
        return_type: BLG.42: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        return self._c_data[5][0]

    @billing.setter  # set BLG.42
    def billing(self, blg: BLG | None):
        """
        id: BLG | use: O | rpt: 1 | seq: 42
        ---
        param_type: BLG.42: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        self._c_data[5] = (blg,)
