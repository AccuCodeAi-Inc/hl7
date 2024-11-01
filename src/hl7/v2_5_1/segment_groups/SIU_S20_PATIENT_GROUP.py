from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PV2 import PV2
from ..segments.OBX import OBX
from ..segments.PV1 import PV1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.DG1 import DG1


"""
PATIENT - SIU_S20_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SIU_S20_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SIU_S20_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    OBX, PID, PD1, PV1, PV2, DG1
)

siu_s20_patient_group = SIU_S20_PATIENT_GROUP(  # PATIENT - Segment group for SIU_S20 - Notification of Cancellation of Service/Resource on Appointment consisting of PID, PD1|None, PV1|None, PV2|None, OBX|None, DG1|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    patient_visit=None,  # PV1(...) 
    patient_visit_additional_information=None,  # PV2(...) 
    observation_or_result=None,  # OBX(...) 
    diagnosis=None,  # DG1(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SIU_S20_PATIENT_GROUP TEMPLATE-----
"""


class SIU_S20_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SIU_S20_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for SIU_S20 - Notification of Cancellation of Service/Resource on Appointment consisting of PID, PD1|None, PV1|None, PV2|None, OBX|None, DG1|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SIU_S20_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 1, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O")
    _c_aliases = ("5", "6", "7", "8", "9", "10")
    _c_components = (PID, PD1, PV1, PV2, OBX, DG1)
    _c_name = ("PID", "PD1", "PV1", "PV2", "OBX", "DG1")
    _c_is_group = (False, False, False, False, False, False)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "patient_visit", "patient_visit_additional_information", "observation_or_result", "diagnosis",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.5
        patient_additional_demographic: PD1 | None = None,  #  PD1.6
        patient_visit: PV1 | None = None,  #  PV1.7
        patient_visit_additional_information: PV2 | None = None,  #  PV2.8
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.9
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.10
    ):
        """
        None - `SIU_S20_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SIU_S20_PATIENT_GROUP>`_
        Segment group for SIU_S20 - Notification of Cancellation of Service/Resource on Appointment consisting of PID, PD1|None, PV1|None, PV2|None, OBX|None, DG1|None

        :param patient_identification: Patient Identification (id: PID | seq: 5 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 6 | use: O | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 7 | use: O | rpt: 1)
        :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 8 | use: O | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 9 | use: O | rpt: *)
        :param diagnosis: Diagnosis (id: DG1 | seq: 10 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information
        self.observation_or_result = observation_or_result
        self.diagnosis = diagnosis

    @property  # get PID.5
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 5
        ---
        return_type: PID.5: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.5
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 5
        ---
        param_type: PID.5: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get PD1.6
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 6
        ---
        return_type: PD1.6: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[1][0]

    @patient_additional_demographic.setter  # set PD1.6
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 6
        ---
        param_type: PD1.6: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[1] = (pd1,)

    @property  # get PV1.7
    def patient_visit(self) -> PV1 | None:
        """
        id: PV1 | use: O | rpt: 1 | seq: 7
        ---
        return_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[2][0]

    @patient_visit.setter  # set PV1.7
    def patient_visit(self, pv1: PV1 | None):
        """
        id: PV1 | use: O | rpt: 1 | seq: 7
        ---
        param_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[2] = (pv1,)

    @property  # get PV2.8
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 8
        ---
        return_type: PV2.8: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[3][0]

    @patient_visit_additional_information.setter  # set PV2.8
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 8
        ---
        param_type: PV2.8: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[3] = (pv2,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[4]

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
            self._c_data[4] = obx
        else:
            self._c_data[4] = (obx,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[5]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: DG1.10 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[5] = dg1
        else:
            self._c_data[5] = (dg1,)
