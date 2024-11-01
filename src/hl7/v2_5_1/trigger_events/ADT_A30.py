from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MRG import MRG
from ..segments.PD1 import PD1
from ..segments.EVN import EVN
from ..segments.SFT import SFT
from ..segments.PID import PID
from ..segments.MSH import MSH


"""
Merge Person Information - ADT_A30
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADT_A30 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A30
from utils.hl7.v2_5_1.segments import (
    MRG, EVN, SFT, PID, MSH, PD1
)

adt_a30 = ADT_A30(  #  - Event A30 has been retained for backward compatibility only
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    merge_patient_information=mrg,  # MRG(...)  # Required.
)

-----END TRIGGER_EVENT::ADT_A30 TEMPLATE-----
"""


class ADT_A30(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADT_A30"""
    _hl7_name = """Merge Person Information"""
    _hl7_description = """Event A30 has been retained for backward compatibility only"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A30"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1)
    _c_usage = ("R", "O", "R", "R", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "5", "6")
    _c_components = (MSH, SFT, EVN, PID, PD1, MRG)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PD1", "MRG")
    _c_is_group = (False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_additional_demographic", "merge_patient_information",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        merge_patient_information: MRG,  #  Required. MRG.6
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
    ):
        """
                 - `ADT_A30 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A30>`_
                Event A30 has been retained for backward compatibility only.  An A30 event was used to merge person information on an MPI.  From V 2.3.1 onwards, the A40 (merge patient-patient identifier list) events should be used to merge patient information for a current episode.  The “incorrect MRN” identified on the MRG segment (MRG-1 - Prior Patient Identifier List) is to be merged with the “correct MRN” identified on the PID segment (PID-3 - Patient Identifier List).  The “incorrect MRN” then no longer exists.  All PID data associated with the “correct MRN” are treated as updated information.

        The MRNs involved may or may not have active or inactive cases associated with them.  Any episode of care that was previously associated with the “incorrect MRN” is now associated with the “correct MRN.”  A list of these cases is not provided.

        The fields included when this message is sent should be the fields pertinent to communicate this event.  When other important fields change, it is recommended that the A08 (update patient information) event be used in addition.

        An A30 (merge person information) is intended for merging person records without merging patient identifiers.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
                :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
                :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
                :param merge_patient_information: Merge Patient Information (id: MRG | seq: 6 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.merge_patient_information = merge_patient_information

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

    @property  # get MRG.6
    def merge_patient_information(self) -> MRG:
        """
        id: MRG | use: R | rpt: 1 | seq: 6
        ---
        return_type: MRG.6: Merge Patient Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MRG
        """
        return self._c_data[5][0]

    @merge_patient_information.setter  # set MRG.6
    def merge_patient_information(self, mrg: MRG):
        """
        id: MRG | use: R | rpt: 1 | seq: 6
        ---
        param_type: MRG.6: Merge Patient Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MRG
        """
        self._c_data[5] = (mrg,)
