from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CTI import CTI
from ..segments.CTD import CTD
from ..segments.FT1 import FT1
from ..segment_groups.ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP import (
    ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP,
)
from ..segments.ORC import ORC
from ..segment_groups.ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP import (
    ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP,
)
from ..segments.NTE import NTE
from ..segments.OBR import OBR


"""
ORDER OBSERVATION - ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    CTD, NTE, ORC, OBR, CTI, FT1
)
from utils.hl7.v2_5_1.segment_groups import (
    ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP
)

oru_w01_patient_result_group_order_observation_group = ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP(  # ORDER OBSERVATION - Segment group for ORU_W01_PATIENT_RESULT_GROUP - PATIENT RESULT consisting of ORC|None, OBR, NTE|None, CTD|None, OBSERVATION, FT1|None, CTI|None, SPECIMEN|None
    common_order=None,  # ORC(...) 
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    contact_data=None,  # CTD(...) 
    observation=oru_w01_patient_result_group_order_observation_group_observation_group,  # ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP(...)  # Required.
    financial_transaction=None,  # FT1(...) 
    clinical_trial_identification=None,  # CTI(...) 
    specimen=None,  # ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP TEMPLATE-----
"""


class ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP"""
    _hl7_name = """ORDER OBSERVATION"""
    _hl7_description = """Segment group for ORU_W01_PATIENT_RESULT_GROUP - PATIENT RESULT consisting of ORC|None, OBR, NTE|None, CTD|None, OBSERVATION, FT1|None, CTI|None, SPECIMEN|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1, 65535, 65535, 65535, 65535)
    _c_usage = ("O", "R", "O", "O", "R", "O", "O", "O")
    _c_aliases = ("9", "10", "11", "12", "None", "15", "16", "None")
    _c_components = (ORC, OBR, NTE, CTD, ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, FT1, CTI, ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP)
    _c_name = ("ORC", "OBR", "NTE", "CTD", "OBSERVATION", "FT1", "CTI", "SPECIMEN")
    _c_is_group = (False, False, False, False, True, False, False, True)
    _c_attrs = ("common_order", "observation_request", "notes_and_comments", "contact_data", "observation", "financial_transaction", "clinical_trial_identification", "specimen",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.10
        observation: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        | tuple[
            ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...
        ],  #  Required. (OBX.13, NTE.14, ...)
        common_order: ORC | None = None,  #  ORC.9
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.11
        contact_data: CTD | None = None,  #  CTD.12
        financial_transaction: FT1 | tuple[FT1, ...] | None = None,  #  FT1.15
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.16
        specimen: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP
        | tuple[
            ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP, ...
        ]
        | None = None,  #  (SPM.17, OBX.18, ...)
    ):
        """
        None - `ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP>`_
        Segment group for ORU_W01_PATIENT_RESULT_GROUP - PATIENT RESULT consisting of ORC|None, OBR, NTE|None, CTD|None, OBSERVATION, FT1|None, CTI|None, SPECIMEN|None

        :param common_order: Common Order (id: ORC | seq: 9 | use: O | rpt: 1)
        :param observation_request: Observation Request (id: OBR | seq: 10 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 11 | use: O | rpt: *)
        :param contact_data: Contact Data (id: CTD | seq: 12 | use: O | rpt: 1)
        :param observation: Observation segment group: [OBX|None, NTE|None] (id: OBSERVATION | seq: 13, 14 | use: R | rpt: *)
        :param financial_transaction: Financial Transaction (id: FT1 | seq: 15 | use: O | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 16 | use: O | rpt: *)
        :param specimen: Specimen segment group: [SPM, OBX|None] (id: SPECIMEN | seq: 17, 18 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.common_order = common_order
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
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

    @property  # get CTD.12
    def contact_data(self) -> CTD | None:
        """
        id: CTD | use: O | rpt: 1 | seq: 12
        ---
        return_type: CTD.12: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[3][0]

    @contact_data.setter  # set CTD.12
    def contact_data(self, ctd: CTD | None):
        """
        id: CTD | use: O | rpt: 1 | seq: 12
        ---
        param_type: CTD.12: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        self._c_data[3] = (ctd,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[
        ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...
    ]:
        """
        id: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[4]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        | tuple[
            ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...
        ],
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP.None | tuple[ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[4] = observation
        else:
            self._c_data[4] = (observation,)

    @property  # get FT1
    def financial_transaction(self) -> tuple[FT1, ...] | tuple[None]:
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        return self._c_data[5]

    @financial_transaction.setter  # set FT1
    def financial_transaction(self, ft1: FT1 | tuple[FT1, ...] | None):
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: FT1.15 | tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        if isinstance(ft1, tuple):
            self._c_data[5] = ft1
        else:
            self._c_data[5] = (ft1,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[6]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: CTI.16 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[6] = cti
        else:
            self._c_data[6] = (cti,)

    @property  # get SPECIMEN
    def specimen(
        self,
    ) -> (
        tuple[ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP, ...]
        | tuple[None]
    ):
        """
        id: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP
        """
        return self._c_data[7]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self,
        specimen: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP
        | tuple[
            ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP, ...
        ]
        | None,
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP.None | tuple[ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[7] = specimen
        else:
            self._c_data[7] = (specimen,)
