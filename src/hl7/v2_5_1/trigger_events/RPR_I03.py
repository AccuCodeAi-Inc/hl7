from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segment_groups.RPR_I03_PROVIDER_GROUP import RPR_I03_PROVIDER_GROUP
from ..segments.NTE import NTE
from ..segments.MSA import MSA
from ..segments.PID import PID


"""
Request/receipt of patient selection list acknowledgement - RPR_I03
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RPR_I03 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RPR_I03
from utils.hl7.v2_5_1.segments import (
    PID, MSH, SFT, NTE, MSA
)
from utils.hl7.v2_5_1.segment_groups import (
    RPR_I03_PROVIDER_GROUP
)

rpr_i03 = RPR_I03(  #  - This trigger event occurs when the inquirer specifies a request for a listing of patient names
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    provider=rpr_i03_provider_group,  # RPR_I03_PROVIDER_GROUP(...)  # Required.
    patient_identification=None,  # PID(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT::RPR_I03 TEMPLATE-----
"""


class RPR_I03(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RPR_I03"""
    _hl7_name = """Request/receipt of patient selection list acknowledgement"""
    _hl7_description = """This trigger event occurs when the inquirer specifies a request for a listing of patient names"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPR_I03"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "O")
    _c_aliases = ("1", "2", "3", "None", "6", "7")
    _c_components = (MSH, SFT, MSA, RPR_I03_PROVIDER_GROUP, PID, NTE)
    _c_name = ("MSH", "SFT", "MSA", "PROVIDER", "PID", "NTE")
    _c_is_group = (False, False, False, True, False, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "provider", "patient_identification", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        provider: RPR_I03_PROVIDER_GROUP
        | tuple[RPR_I03_PROVIDER_GROUP, ...],  #  Required. (PRD.4, CTD.5, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_identification: PID | tuple[PID, ...] | None = None,  #  PID.6
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.7
    ):
        """
         - `RPR_I03 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPR_I03>`_
        This trigger event occurs when the inquirer specifies a request for a listing of patient names.  This event differs from event I02 (request/receipts of patient selection display list) in that it returns the patient list in repeating PID segments instead of repeating DSP segments.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param provider: Provider segment group: [PRD, CTD|None] (id: PROVIDER | seq: 4, 5 | use: R | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 6 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 7 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.provider = provider
        self.patient_identification = patient_identification
        self.notes_and_comments = notes_and_comments

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

    @property  # get MSA.3
    def message_acknowledgment(self) -> MSA:
        """
        id: MSA | use: R | rpt: 1 | seq: 3
        ---
        return_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        return self._c_data[2][0]

    @message_acknowledgment.setter  # set MSA.3
    def message_acknowledgment(self, msa: MSA):
        """
        id: MSA | use: R | rpt: 1 | seq: 3
        ---
        param_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        self._c_data[2] = (msa,)

    @property  # get PROVIDER
    def provider(self) -> tuple[RPR_I03_PROVIDER_GROUP, ...]:
        """
        id: RPR_I03_PROVIDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RPR_I03_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPR_I03_PROVIDER_GROUP
        """
        return self._c_data[3]

    @provider.setter  # set PROVIDER
    def provider(
        self, provider: RPR_I03_PROVIDER_GROUP | tuple[RPR_I03_PROVIDER_GROUP, ...]
    ):
        """
        id: PROVIDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RPR_I03_PROVIDER_GROUP.None | tuple[RPR_I03_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPR_I03_PROVIDER_GROUP
        """
        if isinstance(provider, tuple):
            self._c_data[3] = provider
        else:
            self._c_data[3] = (provider,)

    @property  # get PID
    def patient_identification(self) -> tuple[PID, ...] | tuple[None]:
        """
        id: PID SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[PID, ...]: (Patient Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[4]

    @patient_identification.setter  # set PID
    def patient_identification(self, pid: PID | tuple[PID, ...] | None):
        """
        id: PID SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: PID.6 | tuple[PID, ...]: (Patient Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        if isinstance(pid, tuple):
            self._c_data[4] = pid
        else:
            self._c_data[4] = (pid,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[5]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: NTE.7 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[5] = nte
        else:
            self._c_data[5] = (nte,)
