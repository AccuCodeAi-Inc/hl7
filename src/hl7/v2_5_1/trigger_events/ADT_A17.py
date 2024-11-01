from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.PD1 import PD1
from ..segments.MSH import MSH
from ..segments.PV2 import PV2
from ..segments.EVN import EVN
from ..segments.DB1 import DB1
from ..segments.PV1 import PV1
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.SFT import SFT


"""
Swap Patients - ADT_A17
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADT_A17 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A17
from utils.hl7.v2_5_1.segments import (
    DB1, PID, SFT, EVN, MSH, PD1, PV1, PV2, OBX
)

adt_a17 = ADT_A17(  #  - The A17 is used when it is decided that two patients will exchange beds
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    patient_visit=pv1,  # PV1(...)  # Required.
    patient_visit_additional_information=None,  # PV2(...) 
    disability=None,  # DB1(...) 
    observation_or_result=None,  # OBX(...) 
    patient_identification_10=pid,  # PID(...)  # Required.
    patient_additional_demographic_11=None,  # PD1(...) 
    patient_visit_12=pv1,  # PV1(...)  # Required.
    patient_visit_additional_information_13=None,  # PV2(...) 
    disability_14=None,  # DB1(...) 
    observation_or_result_15=None,  # OBX(...) 
)

-----END TRIGGER_EVENT::ADT_A17 TEMPLATE-----
"""


class ADT_A17(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADT_A17"""
    _hl7_name = """Swap Patients"""
    _hl7_description = """The A17 is used when it is decided that two patients will exchange beds"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A17"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 1, 65535, 65535, 1, 1, 1, 1, 65535, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "R", "O", "O", "O", "R", "O", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15")
    _c_components = (MSH, SFT, EVN, PID, PD1, PV1, PV2, DB1, OBX, PID, PD1, PV1, PV2, DB1, OBX)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PD1", "PV1", "PV2", "DB1", "OBX", "PID", "PD1", "PV1", "PV2", "DB1", "OBX")
    _c_is_group = (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_additional_demographic", "patient_visit", "patient_visit_additional_information", "disability", "observation_or_result", "patient_identification_10", "patient_additional_demographic_11", "patient_visit_12", "patient_visit_additional_information_13", "disability_14", "observation_or_result_15",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        patient_visit: PV1,  #  Required. PV1.6
        patient_identification_10: PID,  #  Required. PID.10
        patient_visit_12: PV1,  #  Required. PV1.12
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        patient_visit_additional_information: PV2 | None = None,  #  PV2.7
        disability: DB1 | tuple[DB1, ...] | None = None,  #  DB1.8
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.9
        patient_additional_demographic_11: PD1 | None = None,  #  PD1.11
        patient_visit_additional_information_13: PV2 | None = None,  #  PV2.13
        disability_14: DB1 | tuple[DB1, ...] | None = None,  #  DB1.14
        observation_or_result_15: OBX | tuple[OBX, ...] | None = None,  #  OBX.15
    ):
        """
         - `ADT_A17 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A17>`_
        The A17 is used when it is decided that two patients will exchange beds.  The patient ID and visit data are repeated for the two patients changing places.  See Section 3.6.1, “Swapping a patient,” for a discussion of issues related to implementing this trigger event. When other important fields change, it is recommended that the A08 (update patient information) event be used in addition.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 6 | use: R | rpt: 1)
        :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 7 | use: O | rpt: 1)
        :param disability: Disability (id: DB1 | seq: 8 | use: O | rpt: *)
        :param observation_or_result: Observation/Result (id: OBX | seq: 9 | use: O | rpt: *)
        :param patient_identification_10: Patient Identification (id: PID | seq: 10 | use: R | rpt: 1)
        :param patient_additional_demographic_11: Patient Additional Demographic (id: PD1 | seq: 11 | use: O | rpt: 1)
        :param patient_visit_12: Patient Visit (id: PV1 | seq: 12 | use: R | rpt: 1)
        :param patient_visit_additional_information_13: Patient Visit - Additional Information (id: PV2 | seq: 13 | use: O | rpt: 1)
        :param disability_14: Disability (id: DB1 | seq: 14 | use: O | rpt: *)
        :param observation_or_result_15: Observation/Result (id: OBX | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 15
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information
        self.disability = disability
        self.observation_or_result = observation_or_result
        self.patient_identification_10 = patient_identification_10
        self.patient_additional_demographic_11 = patient_additional_demographic_11
        self.patient_visit_12 = patient_visit_12
        self.patient_visit_additional_information_13 = (
            patient_visit_additional_information_13
        )
        self.disability_14 = disability_14
        self.observation_or_result_15 = observation_or_result_15

    @property  # get MSH.1
    def message_header(self) -> MSH:
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        return_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        return self._c_data[0][0]

    @message_header.setter  # set MSH.1
    def message_header(self, msh: MSH):
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        param_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        self._c_data[0] = (msh,)

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[1]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        param_type: SFT.2 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[1] = sft
        else:
            self._c_data[1] = (sft,)

    @property  # get EVN.3
    def event_type(self) -> EVN:
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        return_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        return self._c_data[2][0]

    @event_type.setter  # set EVN.3
    def event_type(self, evn: EVN):
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        param_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        self._c_data[2] = (evn,)

    @property  # get PID.4
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        return_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[3][0]

    @patient_identification.setter  # set PID.4
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        param_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[3] = (pid,)

    @property  # get PD1.5
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[4][0]

    @patient_additional_demographic.setter  # set PD1.5
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[4] = (pd1,)

    @property  # get PV1.6
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 6
        ---
        return_type: PV1.6: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[5][0]

    @patient_visit.setter  # set PV1.6
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 6
        ---
        param_type: PV1.6: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[5] = (pv1,)

    @property  # get PV2.7
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 7
        ---
        return_type: PV2.7: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[6][0]

    @patient_visit_additional_information.setter  # set PV2.7
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 7
        ---
        param_type: PV2.7: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[6] = (pv2,)

    @property  # get DB1
    def disability(self) -> tuple[DB1, ...] | tuple[None]:
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        return self._c_data[7]

    @disability.setter  # set DB1
    def disability(self, db1: DB1 | tuple[DB1, ...] | None):
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: DB1.8 | tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        if isinstance(db1, tuple):
            self._c_data[7] = db1
        else:
            self._c_data[7] = (db1,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[8]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: OBX.9 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[8] = obx
        else:
            self._c_data[8] = (obx,)

    @property  # get PID.10
    def patient_identification_10(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 10
        ---
        return_type: PID.10: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[9][0]

    @patient_identification_10.setter  # set PID.10
    def patient_identification_10(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 10
        ---
        param_type: PID.10: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[9] = (pid,)

    @property  # get PD1.11
    def patient_additional_demographic_11(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 11
        ---
        return_type: PD1.11: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[10][0]

    @patient_additional_demographic_11.setter  # set PD1.11
    def patient_additional_demographic_11(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 11
        ---
        param_type: PD1.11: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[10] = (pd1,)

    @property  # get PV1.12
    def patient_visit_12(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 12
        ---
        return_type: PV1.12: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[11][0]

    @patient_visit_12.setter  # set PV1.12
    def patient_visit_12(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 12
        ---
        param_type: PV1.12: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[11] = (pv1,)

    @property  # get PV2.13
    def patient_visit_additional_information_13(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 13
        ---
        return_type: PV2.13: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[12][0]

    @patient_visit_additional_information_13.setter  # set PV2.13
    def patient_visit_additional_information_13(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 13
        ---
        param_type: PV2.13: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[12] = (pv2,)

    @property  # get DB1
    def disability_14(self) -> tuple[DB1, ...] | tuple[None]:
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        return_type: tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        return self._c_data[13]

    @disability_14.setter  # set DB1
    def disability_14(self, db1: DB1 | tuple[DB1, ...] | None):
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        param_type: DB1.14 | tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        if isinstance(db1, tuple):
            self._c_data[13] = db1
        else:
            self._c_data[13] = (db1,)

    @property  # get OBX
    def observation_or_result_15(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[14]

    @observation_or_result_15.setter  # set OBX
    def observation_or_result_15(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: OBX.15 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[14] = obx
        else:
            self._c_data[14] = (obx,)
