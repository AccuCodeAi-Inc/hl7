from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.RPL_I02_PROVIDER_GROUP import RPL_I02_PROVIDER_GROUP
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.MSH import MSH
from ..segments.MSA import MSA


"""
Request/receipt of patient selection display list acknowledgement - RPL_I02
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RPL_I02 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RPL_I02
from utils.hl7.v2_5_1.segments import (
    DSP, DSC, NTE, MSA, SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    RPL_I02_PROVIDER_GROUP
)

rpl_i02 = RPL_I02(  #  - This trigger event occurs when the inquirer specifies a request for a name lookup listing
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    provider=rpl_i02_provider_group,  # RPL_I02_PROVIDER_GROUP(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    display_data=None,  # DSP(...) 
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::RPL_I02 TEMPLATE-----
"""


class RPL_I02(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RPL_I02"""
    _hl7_name = """Request/receipt of patient selection display list acknowledgement"""
    _hl7_description = """This trigger event occurs when the inquirer specifies a request for a name lookup listing"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPL_I02"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 65535, 65535, 1)
    _c_usage = ("R", "O", "R", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "None", "6", "7", "8")
    _c_components = (MSH, SFT, MSA, RPL_I02_PROVIDER_GROUP, NTE, DSP, DSC)
    _c_name = ("MSH", "SFT", "MSA", "PROVIDER", "NTE", "DSP", "DSC")
    _c_is_group = (False, False, False, True, False, False, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "provider", "notes_and_comments", "display_data", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        provider: RPL_I02_PROVIDER_GROUP
        | tuple[RPL_I02_PROVIDER_GROUP, ...],  #  Required. (PRD.4, CTD.5, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.6
        display_data: DSP | tuple[DSP, ...] | None = None,  #  DSP.7
        continuation_pointer: DSC | None = None,  #  DSC.8
    ):
        """
         - `RPL_I02 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPL_I02>`_
        This trigger event occurs when the inquirer specifies a request for a name lookup listing.  Generally, this request is used by the responder when insufficient data is on hand for a positive match.  In this case, the requester may ask for a list of possible candidates from which to make a selection.  This event code is also used by the responder to signify that the return information contains a list of information rather than information specific to a single patient.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param provider: Provider segment group: [PRD, CTD|None] (id: PROVIDER | seq: 4, 5 | use: R | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 6 | use: O | rpt: *)
        :param display_data: Display Data (id: DSP | seq: 7 | use: O | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.provider = provider
        self.notes_and_comments = notes_and_comments
        self.display_data = display_data
        self.continuation_pointer = continuation_pointer

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
    def provider(self) -> tuple[RPL_I02_PROVIDER_GROUP, ...]:
        """
        id: RPL_I02_PROVIDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RPL_I02_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPL_I02_PROVIDER_GROUP
        """
        return self._c_data[3]

    @provider.setter  # set PROVIDER
    def provider(
        self, provider: RPL_I02_PROVIDER_GROUP | tuple[RPL_I02_PROVIDER_GROUP, ...]
    ):
        """
        id: PROVIDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RPL_I02_PROVIDER_GROUP.None | tuple[RPL_I02_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPL_I02_PROVIDER_GROUP
        """
        if isinstance(provider, tuple):
            self._c_data[3] = provider
        else:
            self._c_data[3] = (provider,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[4]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: NTE.6 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[4] = nte
        else:
            self._c_data[4] = (nte,)

    @property  # get DSP
    def display_data(self) -> tuple[DSP, ...] | tuple[None]:
        """
        id: DSP SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[DSP, ...]: (Display Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSP
        """
        return self._c_data[5]

    @display_data.setter  # set DSP
    def display_data(self, dsp: DSP | tuple[DSP, ...] | None):
        """
        id: DSP SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: DSP.7 | tuple[DSP, ...]: (Display Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSP
        """
        if isinstance(dsp, tuple):
            self._c_data[5] = dsp
        else:
            self._c_data[5] = (dsp,)

    @property  # get DSC.8
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 8
        ---
        return_type: DSC.8: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[6][0]

    @continuation_pointer.setter  # set DSC.8
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 8
        ---
        param_type: DSC.8: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[6] = (dsc,)
