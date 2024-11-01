from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.IAM import IAM
from ..segments.PV2 import PV2
from ..segments.EVN import EVN
from ..segments.SFT import SFT
from ..segments.PID import PID
from ..segments.MSH import MSH
from ..segments.PV1 import PV1


"""
Update Adverse Reaction Information - ADT_A60
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADT_A60 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A60
from utils.hl7.v2_5_1.segments import (
    PV2, PV1, IAM, EVN, SFT, PID, MSH
)

adt_a60 = ADT_A60(  #  - This trigger event is used when person/patient allergy information has changed
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PV1(...) 
    patient_visit_additional_information=None,  # PV2(...) 
    patient_adverse_reaction_information=None,  # IAM(...) 
)

-----END TRIGGER_EVENT::ADT_A60 TEMPLATE-----
"""


class ADT_A60(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADT_A60"""
    _hl7_name = """Update Adverse Reaction Information"""
    _hl7_description = """This trigger event is used when person/patient allergy information has changed"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A60"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7")
    _c_components = (MSH, SFT, EVN, PID, PV1, PV2, IAM)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PV1", "PV2", "IAM")
    _c_is_group = (False, False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_visit", "patient_visit_additional_information", "patient_adverse_reaction_information",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_visit: PV1 | None = None,  #  PV1.5
        patient_visit_additional_information: PV2 | None = None,  #  PV2.6
        patient_adverse_reaction_information: IAM
        | tuple[IAM, ...]
        | None = None,  #  IAM.7
    ):
        """
         - `ADT_A60 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A60>`_
        This trigger event is used when person/patient allergy information has changed.  It is used in conjunction with a new allergy segment, the IAM - Patient Allergy Information Segment-Unique Identifier, which supports Action code/unique identifier mode update for repeating segments as defined in 2.14.4 Modes for updating via repeating segments.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 5 | use: O | rpt: 1)
        :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 6 | use: O | rpt: 1)
        :param patient_adverse_reaction_information: Patient Adverse Reaction Information (id: IAM | seq: 7 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information
        self.patient_adverse_reaction_information = patient_adverse_reaction_information

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

    @property  # get PV1.5
    def patient_visit(self) -> PV1 | None:
        """
        id: PV1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: PV1.5: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[4][0]

    @patient_visit.setter  # set PV1.5
    def patient_visit(self, pv1: PV1 | None):
        """
        id: PV1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: PV1.5: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[4] = (pv1,)

    @property  # get PV2.6
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 6
        ---
        return_type: PV2.6: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[5][0]

    @patient_visit_additional_information.setter  # set PV2.6
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 6
        ---
        param_type: PV2.6: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[5] = (pv2,)

    @property  # get IAM
    def patient_adverse_reaction_information(self) -> tuple[IAM, ...] | tuple[None]:
        """
        id: IAM SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[IAM, ...]: (Patient Adverse Reaction Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IAM
        """
        return self._c_data[6]

    @patient_adverse_reaction_information.setter  # set IAM
    def patient_adverse_reaction_information(self, iam: IAM | tuple[IAM, ...] | None):
        """
        id: IAM SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: IAM.7 | tuple[IAM, ...]: (Patient Adverse Reaction Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IAM
        """
        if isinstance(iam, tuple):
            self._c_data[6] = iam
        else:
            self._c_data[6] = (iam,)
