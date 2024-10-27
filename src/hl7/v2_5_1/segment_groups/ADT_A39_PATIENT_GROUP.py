from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PV1 import PV1
from ..segments.PID import PID
from ..segments.PD1 import PD1
from ..segments.MRG import MRG


"""
PATIENT - ADT_A39_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ADT_A39_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A39_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    MRG, PID, PV1, PD1
)

adt_a39_patient_group = ADT_A39_PATIENT_GROUP(  # PATIENT - Segment group for ADT_A39 - Merge Person - Patient ID consisting of PID, PD1|None, MRG, PV1|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    merge_patient_information=mrg,  # MRG(...)  # Required.
    patient_visit=None,  # PV1(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ADT_A39_PATIENT_GROUP TEMPLATE-----
"""


class ADT_A39_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ADT_A39_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for ADT_A39 - Merge Person - Patient ID consisting of PID, PD1|None, MRG, PV1|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A39_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 1)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("4", "5", "6", "7")
    _c_components = (PID, PD1, MRG, PV1)
    _c_name = ("PID", "PD1", "MRG", "PV1")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "merge_patient_information", "patient_visit",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.4
        merge_patient_information: MRG,  #  Required. MRG.6
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        patient_visit: PV1 | None = None,  #  PV1.7
    ):
        """
        None - `ADT_A39_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A39_PATIENT_GROUP>`_
        Segment group for ADT_A39 - Merge Person - Patient ID consisting of PID, PD1|None, MRG, PV1|None

        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
        :param merge_patient_information: Merge Patient Information (id: MRG | seq: 6 | use: R | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 7 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.merge_patient_information = merge_patient_information
        self.patient_visit = patient_visit

    @property  # get PID.4
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        return_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.4
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        param_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get PD1.5
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[1][0]

    @patient_additional_demographic.setter  # set PD1.5
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[1] = (pd1,)

    @property  # get MRG.6
    def merge_patient_information(self) -> MRG:
        """
        id: MRG | use: R | rpt: 1 | seq: 6
        ---
        return_type: MRG.6: Merge Patient Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MRG
        """
        return self._c_data[2][0]

    @merge_patient_information.setter  # set MRG.6
    def merge_patient_information(self, mrg: MRG):
        """
        id: MRG | use: R | rpt: 1 | seq: 6
        ---
        param_type: MRG.6: Merge Patient Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MRG
        """
        self._c_data[2] = (mrg,)

    @property  # get PV1.7
    def patient_visit(self) -> PV1 | None:
        """
        id: PV1 | use: O | rpt: 1 | seq: 7
        ---
        return_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[3][0]

    @patient_visit.setter  # set PV1.7
    def patient_visit(self, pv1: PV1 | None):
        """
        id: PV1 | use: O | rpt: 1 | seq: 7
        ---
        param_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[3] = (pv1,)