from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segment_groups.ADT_A45_MERGE_INFO_GROUP import ADT_A45_MERGE_INFO_GROUP
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.EVN import EVN


"""
Move Visit Information - Visit Number - ADT_A45
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADT_A45 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A45
from utils.hl7.v2_5_1.segments import (
    PID, MSH, PD1, SFT, EVN
)
from utils.hl7.v2_5_1.segment_groups import (
    ADT_A45_MERGE_INFO_GROUP
)

adt_a45 = ADT_A45(  #  - A move has been done at the visit identifier level
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    merge_info=adt_a45_merge_info_group,  # ADT_A45_MERGE_INFO_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::ADT_A45 TEMPLATE-----
"""


class ADT_A45(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADT_A45"""
    _hl7_name = """Move Visit Information - Visit Number"""
    _hl7_description = """A move has been done at the visit identifier level"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A45"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "5", "None")
    _c_components = (MSH, SFT, EVN, PID, PD1, ADT_A45_MERGE_INFO_GROUP)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PD1", "MERGE INFO")
    _c_is_group = (False, False, False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_additional_demographic", "merge_info",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        merge_info: ADT_A45_MERGE_INFO_GROUP
        | tuple[ADT_A45_MERGE_INFO_GROUP, ...],  #  Required. (MRG.6, PV1.7, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
    ):
        """
                 - `ADT_A45 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A45>`_
                A move has been done at the visit identifier level.  That is, a PV1-19 - Visit Number or PV1-50 - Alternate Visit ID associated with one account identifier (PID-18 - Patient Account Number) has been moved to another account identifier.

        An A45 event is used to signal a move of records identified by the MRG-5 - Prior Visit Number or the MRG-6 - Prior Alternate Visit ID from the “incorrect source account identifier” identified in the MRG segment (MRG-3 - Prior Patient Account Number) to the “correct target account identifier” identified in the PID segment (PID-18 - Patient Account Number).

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
                :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
                :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
                :param merge_info: Merge Info segment group: [MRG, PV1] (id: MERGE INFO | seq: 6, 7 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.merge_info = merge_info

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

    @property  # get MERGE INFO
    def merge_info(self) -> tuple[ADT_A45_MERGE_INFO_GROUP, ...]:
        """
        id: ADT_A45_MERGE_INFO_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ADT_A45_MERGE_INFO_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADT_A45_MERGE_INFO_GROUP
        """
        return self._c_data[5]

    @merge_info.setter  # set MERGE INFO
    def merge_info(
        self,
        merge_info: ADT_A45_MERGE_INFO_GROUP | tuple[ADT_A45_MERGE_INFO_GROUP, ...],
    ):
        """
        id: MERGE INFO SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ADT_A45_MERGE_INFO_GROUP.None | tuple[ADT_A45_MERGE_INFO_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADT_A45_MERGE_INFO_GROUP
        """
        if isinstance(merge_info, tuple):
            self._c_data[5] = merge_info
        else:
            self._c_data[5] = (merge_info,)
