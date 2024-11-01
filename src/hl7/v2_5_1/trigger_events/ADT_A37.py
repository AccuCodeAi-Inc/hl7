from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.PV1 import PV1
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.DB1 import DB1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.EVN import EVN


"""
Unlink Patient Information - ADT_A37
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADT_A37 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A37
from utils.hl7.v2_5_1.segments import (
    PID, MSH, PD1, PV1, DB1, SFT, EVN
)

adt_a37 = ADT_A37(  #  - The A37 event unlinks two patient identifiers
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    patient_visit=None,  # PV1(...) 
    disability=None,  # DB1(...) 
    patient_identification_8=pid,  # PID(...)  # Required.
    patient_additional_demographic_9=None,  # PD1(...) 
    patient_visit_10=None,  # PV1(...) 
    disability_11=None,  # DB1(...) 
)

-----END TRIGGER_EVENT::ADT_A37 TEMPLATE-----
"""


class ADT_A37(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADT_A37"""
    _hl7_name = """Unlink Patient Information"""
    _hl7_description = """The A37 event unlinks two patient identifiers"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A37"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 65535, 1, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "O", "O", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    _c_components = (MSH, SFT, EVN, PID, PD1, PV1, DB1, PID, PD1, PV1, DB1)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PD1", "PV1", "DB1", "PID", "PD1", "PV1", "DB1")
    _c_is_group = (False, False, False, False, False, False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_additional_demographic", "patient_visit", "disability", "patient_identification_8", "patient_additional_demographic_9", "patient_visit_10", "disability_11",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        patient_identification_8: PID,  #  Required. PID.8
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        patient_visit: PV1 | None = None,  #  PV1.6
        disability: DB1 | tuple[DB1, ...] | None = None,  #  DB1.7
        patient_additional_demographic_9: PD1 | None = None,  #  PD1.9
        patient_visit_10: PV1 | None = None,  #  PV1.10
        disability_11: DB1 | tuple[DB1, ...] | None = None,  #  DB1.11
    ):
        """
         - `ADT_A37 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A37>`_
        The A37 event unlinks two patient identifiers.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 6 | use: O | rpt: 1)
        :param disability: Disability (id: DB1 | seq: 7 | use: O | rpt: *)
        :param patient_identification_8: Patient Identification (id: PID | seq: 8 | use: R | rpt: 1)
        :param patient_additional_demographic_9: Patient Additional Demographic (id: PD1 | seq: 9 | use: O | rpt: 1)
        :param patient_visit_10: Patient Visit (id: PV1 | seq: 10 | use: O | rpt: 1)
        :param disability_11: Disability (id: DB1 | seq: 11 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 11
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.patient_visit = patient_visit
        self.disability = disability
        self.patient_identification_8 = patient_identification_8
        self.patient_additional_demographic_9 = patient_additional_demographic_9
        self.patient_visit_10 = patient_visit_10
        self.disability_11 = disability_11

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
    def patient_visit(self) -> PV1 | None:
        """
        id: PV1 | use: O | rpt: 1 | seq: 6
        ---
        return_type: PV1.6: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[5][0]

    @patient_visit.setter  # set PV1.6
    def patient_visit(self, pv1: PV1 | None):
        """
        id: PV1 | use: O | rpt: 1 | seq: 6
        ---
        param_type: PV1.6: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[5] = (pv1,)

    @property  # get DB1
    def disability(self) -> tuple[DB1, ...] | tuple[None]:
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        return self._c_data[6]

    @disability.setter  # set DB1
    def disability(self, db1: DB1 | tuple[DB1, ...] | None):
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: DB1.7 | tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        if isinstance(db1, tuple):
            self._c_data[6] = db1
        else:
            self._c_data[6] = (db1,)

    @property  # get PID.8
    def patient_identification_8(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 8
        ---
        return_type: PID.8: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[7][0]

    @patient_identification_8.setter  # set PID.8
    def patient_identification_8(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 8
        ---
        param_type: PID.8: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[7] = (pid,)

    @property  # get PD1.9
    def patient_additional_demographic_9(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 9
        ---
        return_type: PD1.9: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[8][0]

    @patient_additional_demographic_9.setter  # set PD1.9
    def patient_additional_demographic_9(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 9
        ---
        param_type: PD1.9: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[8] = (pd1,)

    @property  # get PV1.10
    def patient_visit_10(self) -> PV1 | None:
        """
        id: PV1 | use: O | rpt: 1 | seq: 10
        ---
        return_type: PV1.10: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[9][0]

    @patient_visit_10.setter  # set PV1.10
    def patient_visit_10(self, pv1: PV1 | None):
        """
        id: PV1 | use: O | rpt: 1 | seq: 10
        ---
        param_type: PV1.10: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[9] = (pv1,)

    @property  # get DB1
    def disability_11(self) -> tuple[DB1, ...] | tuple[None]:
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        return self._c_data[10]

    @disability_11.setter  # set DB1
    def disability_11(self, db1: DB1 | tuple[DB1, ...] | None):
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: DB1.11 | tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        if isinstance(db1, tuple):
            self._c_data[10] = db1
        else:
            self._c_data[10] = (db1,)
