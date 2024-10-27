from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.ADT_A39_PATIENT_GROUP import ADT_A39_PATIENT_GROUP
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.EVN import EVN


"""
Merge Person - Patient ID - ADT_A39
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADT_A39 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A39
from utils.hl7.v2_5_1.segments import (
    SFT, EVN, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    ADT_A39_PATIENT_GROUP
)

adt_a39 = ADT_A39(  #  - Event A39 has been retained for backward compatibility only
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient=adt_a39_patient_group,  # ADT_A39_PATIENT_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::ADT_A39 TEMPLATE-----
"""


class ADT_A39(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADT_A39"""
    _hl7_name = """Merge Person - Patient ID"""
    _hl7_description = """Event A39 has been retained for backward compatibility only"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A39"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "None")
    _c_components = (MSH, SFT, EVN, ADT_A39_PATIENT_GROUP)
    _c_name = ("MSH", "SFT", "EVN", "PATIENT")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient: ADT_A39_PATIENT_GROUP
        | tuple[
            ADT_A39_PATIENT_GROUP, ...
        ],  #  Required. (PID.4, PD1.5, MRG.6, PV1.7, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
                 - `ADT_A39 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A39>`_
                Event A39 has been retained for backward compatibility only. From V2.3.1 onwards, event A40 (merge patient - patient identifier list) should be used instead. A merge has been done at the patient identifier level.  That is, two PID-2 - Patient ID identifiers have been merged into one.

        An A39 event is used to signal a merge of records for a person that was incorrectly filed under two different PID-2 - Patient IDs.  The “incorrect source patient ID” identified in the MRG segment (MRG-4 - Prior Patient ID) is to be merged with the required “correct target patient ID” identified in the PID segment (PID-2 - Patient ID).  The “incorrect source patient ID” would then logically never be referenced in future transactions.  It is noted that some systems may still physically keep this “incorrect identifier” for audit trail purposes or other reasons associated with database index implementation requirements.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
                :param patient: Patient segment group: [PID, PD1|None, MRG, PV1|None] (id: PATIENT | seq: 4, 5, 6, 7 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient = patient

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

    @property  # get PATIENT
    def patient(self) -> tuple[ADT_A39_PATIENT_GROUP, ...]:
        """
        id: ADT_A39_PATIENT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ADT_A39_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADT_A39_PATIENT_GROUP
        """
        return self._c_data[3]

    @patient.setter  # set PATIENT
    def patient(
        self, patient: ADT_A39_PATIENT_GROUP | tuple[ADT_A39_PATIENT_GROUP, ...]
    ):
        """
        id: PATIENT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ADT_A39_PATIENT_GROUP.None | tuple[ADT_A39_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADT_A39_PATIENT_GROUP
        """
        if isinstance(patient, tuple):
            self._c_data[3] = patient
        else:
            self._c_data[3] = (patient,)
