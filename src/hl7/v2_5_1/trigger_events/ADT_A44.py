from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segments.EVN import EVN
from ..segments.SFT import SFT
from ..segment_groups.ADT_A44_PATIENT_ID_GROUP import ADT_A44_PATIENT_ID_GROUP


"""
Move Account Information - Patient Account Number - ADT_A44
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADT_A44 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A44
from utils.hl7.v2_5_1.segments import (
    EVN, SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    ADT_A44_PATIENT_ID_GROUP
)

adt_a44 = ADT_A44(  #  - A move has been done at the account identifier level
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_id=adt_a44_patient_id_group,  # ADT_A44_PATIENT_ID_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::ADT_A44 TEMPLATE-----
"""


class ADT_A44(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADT_A44"""
    _hl7_name = """Move Account Information - Patient Account Number"""
    _hl7_description = """A move has been done at the account identifier level"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A44"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "None")
    _c_components = (MSH, SFT, EVN, ADT_A44_PATIENT_ID_GROUP)
    _c_name = ("MSH", "SFT", "EVN", "PATIENT ID")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_id",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_id: ADT_A44_PATIENT_ID_GROUP
        | tuple[ADT_A44_PATIENT_ID_GROUP, ...],  #  Required. (PID.4, PD1.5, MRG.6, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
                 - `ADT_A44 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A44>`_
                A move has been done at the account identifier level.  That is, a PID-18 - Patient Account Number associated with one PID-3 - Patient Identifier List has been moved to another patient identifier list.

        An A44 event is used to signal a move of records identified by the MRG-3 - Prior Patient Account Nu
        mber from the “incorrect source patient identifier list” identified in the MRG segment (MRG-1 - Prior Patient Identifier List) to the “correct target patient identifier list” identified in the PID segment (PID-3 - Patient Identifier List).

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
                :param patient_id: Patient Id segment group: [PID, PD1|None, MRG] (id: PATIENT ID | seq: 4, 5, 6 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_id = patient_id

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

    @property  # get PATIENT ID
    def patient_id(self) -> tuple[ADT_A44_PATIENT_ID_GROUP, ...]:
        """
        id: ADT_A44_PATIENT_ID_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ADT_A44_PATIENT_ID_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADT_A44_PATIENT_ID_GROUP
        """
        return self._c_data[3]

    @patient_id.setter  # set PATIENT ID
    def patient_id(
        self,
        patient_id: ADT_A44_PATIENT_ID_GROUP | tuple[ADT_A44_PATIENT_ID_GROUP, ...],
    ):
        """
        id: PATIENT ID SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ADT_A44_PATIENT_ID_GROUP.None | tuple[ADT_A44_PATIENT_ID_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADT_A44_PATIENT_ID_GROUP
        """
        if isinstance(patient_id, tuple):
            self._c_data[3] = patient_id
        else:
            self._c_data[3] = (patient_id,)
