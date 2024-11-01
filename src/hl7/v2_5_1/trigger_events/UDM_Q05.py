from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.DSC import DSC
from ..segments.URS import URS
from ..segments.DSP import DSP
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.URD import URD


"""
Unsolicited Display Update - UDM_Q05
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::UDM_Q05 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import UDM_Q05
from utils.hl7.v2_5_1.segments import (
    MSH, URD, SFT, DSP, DSC, URS
)

udm_q05 = UDM_Q05(  #  - This section is retained for backward compatibility and the framework for the existing functional queries
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    results_or_update_definition=urd,  # URD(...)  # Required.
    unsolicited_selection=None,  # URS(...) 
    display_data=dsp,  # DSP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::UDM_Q05 TEMPLATE-----
"""


class UDM_Q05(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """UDM_Q05"""
    _hl7_name = """Unsolicited Display Update"""
    _hl7_description = """This section is retained for backward compatibility and the framework for the existing functional queries"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/UDM_Q05"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6")
    _c_components = (MSH, SFT, URD, URS, DSP, DSC)
    _c_name = ("MSH", "SFT", "URD", "URS", "DSP", "DSC")
    _c_is_group = (False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "results_or_update_definition", "unsolicited_selection", "display_data", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        results_or_update_definition: URD,  #  Required. URD.3
        display_data: DSP | tuple[DSP, ...],  #  Required. DSP.5
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        unsolicited_selection: URS | None = None,  #  URS.4
        continuation_pointer: DSC | None = None,  #  DSC.6
    ):
        """
                 - `UDM_Q05 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/UDM_Q05>`_
                This section is retained for backward compatibility and the framework for the existing functional queries.

        The UDM message does not have a direct replacement in the new methodology. It is not clear how extensively this message is used.

        There is a simple HL7 message that allows for unsolicited display update messages to be sent in HL7 format from one system to another.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param results_or_update_definition: Results/update Definition (id: URD | seq: 3 | use: R | rpt: 1)
                :param unsolicited_selection: Unsolicited Selection (id: URS | seq: 4 | use: O | rpt: 1)
                :param display_data: Display Data (id: DSP | seq: 5 | use: R | rpt: *)
                :param continuation_pointer: Continuation Pointer (id: DSC | seq: 6 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.software_segment = software_segment
        self.results_or_update_definition = results_or_update_definition
        self.unsolicited_selection = unsolicited_selection
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

    @property  # get URD.3
    def results_or_update_definition(self) -> URD:
        """
        id: URD | use: R | rpt: 1 | seq: 3
        ---
        return_type: URD.3: Results/update Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/URD
        """
        return self._c_data[2][0]

    @results_or_update_definition.setter  # set URD.3
    def results_or_update_definition(self, urd: URD):
        """
        id: URD | use: R | rpt: 1 | seq: 3
        ---
        param_type: URD.3: Results/update Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/URD
        """
        self._c_data[2] = (urd,)

    @property  # get URS.4
    def unsolicited_selection(self) -> URS | None:
        """
        id: URS | use: O | rpt: 1 | seq: 4
        ---
        return_type: URS.4: Unsolicited Selection
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/URS
        """
        return self._c_data[3][0]

    @unsolicited_selection.setter  # set URS.4
    def unsolicited_selection(self, urs: URS | None):
        """
        id: URS | use: O | rpt: 1 | seq: 4
        ---
        param_type: URS.4: Unsolicited Selection
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/URS
        """
        self._c_data[3] = (urs,)

    @property  # get DSP
    def display_data(self) -> tuple[DSP, ...]:
        """
        id: DSP SEGMENT GROUP | use: R | rpt: * | seq: 5
        ---
        return_type: tuple[DSP, ...]: (Display Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSP
        """
        return self._c_data[4]

    @display_data.setter  # set DSP
    def display_data(self, dsp: DSP | tuple[DSP, ...]):
        """
        id: DSP SEGMENT GROUP | use: R | rpt: * | seq: 5
        ---
        param_type: DSP.5 | tuple[DSP, ...]: (Display Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSP
        """
        if isinstance(dsp, tuple):
            self._c_data[4] = dsp
        else:
            self._c_data[4] = (dsp,)

    @property  # get DSC.6
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 6
        ---
        return_type: DSC.6: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[5][0]

    @continuation_pointer.setter  # set DSC.6
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 6
        ---
        param_type: DSC.6: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[5] = (dsc,)
