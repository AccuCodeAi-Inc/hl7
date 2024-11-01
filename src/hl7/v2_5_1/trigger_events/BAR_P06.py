from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segments.EVN import EVN
from ..segment_groups.BAR_P06_PATIENT_GROUP import BAR_P06_PATIENT_GROUP
from ..segments.SFT import SFT


"""
End account - BAR_P06
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::BAR_P06 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BAR_P06
from utils.hl7.v2_5_1.segments import (
    EVN, SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    BAR_P06_PATIENT_GROUP
)

bar_p06 = BAR_P06(  #  - The P06 event is a notification that the account is no longer open, that is, no new charges can accrue to this account
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient=bar_p06_patient_group,  # BAR_P06_PATIENT_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::BAR_P06 TEMPLATE-----
"""


class BAR_P06(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """BAR_P06"""
    _hl7_name = """End account"""
    _hl7_description = """The P06 event is a notification that the account is no longer open, that is, no new charges can accrue to this account"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P06"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "None")
    _c_components = (MSH, SFT, EVN, BAR_P06_PATIENT_GROUP)
    _c_name = ("MSH", "SFT", "EVN", "PATIENT")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient: BAR_P06_PATIENT_GROUP
        | tuple[BAR_P06_PATIENT_GROUP, ...],  #  Required. (PID.4, PV1.5, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `BAR_P06 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P06>`_
        The P06 event is a notification that the account is no longer open, that is, no new charges can accrue to this account.  This notification is not related to whether or not the account is paid in full.  EVN-2 - Recorded Date/Time must contain the account end date.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param patient: Patient segment group: [PID, PV1|None] (id: PATIENT | seq: 4, 5 | use: R | rpt: *)
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
    def patient(self) -> tuple[BAR_P06_PATIENT_GROUP, ...]:
        """
        id: BAR_P06_PATIENT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[BAR_P06_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P06_PATIENT_GROUP
        """
        return self._c_data[3]

    @patient.setter  # set PATIENT
    def patient(
        self, patient: BAR_P06_PATIENT_GROUP | tuple[BAR_P06_PATIENT_GROUP, ...]
    ):
        """
        id: PATIENT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: BAR_P06_PATIENT_GROUP.None | tuple[BAR_P06_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P06_PATIENT_GROUP
        """
        if isinstance(patient, tuple):
            self._c_data[3] = patient
        else:
            self._c_data[3] = (patient,)
