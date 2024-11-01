from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segments.MFE import MFE
from ..segments.MFI import MFI
from ..segments.SFT import SFT


"""
Master File Notification - General - MFN_M13
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::MFN_M13 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M13
from utils.hl7.v2_5_1.segments import (
    SFT, MFI, MFE, MSH
)

mfn_m13 = MFN_M13(  #  - The MFN General master file notification transaction is used where the master file is a simple one that contains only a key and the text value of that key
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    master_file_identification=mfi,  # MFI(...)  # Required.
    master_file_entry=mfe,  # MFE(...)  # Required.
)

-----END TRIGGER_EVENT::MFN_M13 TEMPLATE-----
"""


class MFN_M13(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """MFN_M13"""
    _hl7_name = """Master File Notification - General"""
    _hl7_description = """The MFN General master file notification transaction is used where the master file is a simple one that contains only a key and the text value of that key"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M13"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "4")
    _c_components = (MSH, SFT, MFI, MFE)
    _c_name = ("MSH", "SFT", "MFI", "MFE")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "master_file_identification", "master_file_entry",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        master_file_identification: MFI,  #  Required. MFI.3
        master_file_entry: MFE | tuple[MFE, ...],  #  Required. MFE.4
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `MFN_M13 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M13>`_
        The MFN General master file notification transaction is used where the master file is a simple one that contains only a key and the text value of that key.  Both values are carried in MFE-4 - Primary Key Value - MFE.  The specific master file being updated is identified by MFI-1 - Master File Identifier and MFI-2 - Master Files Application Identifier.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param master_file_identification: Master File Identification (id: MFI | seq: 3 | use: R | rpt: 1)
        :param master_file_entry: Master File Entry (id: MFE | seq: 4 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.master_file_identification = master_file_identification
        self.master_file_entry = master_file_entry

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

    @property  # get MFI.3
    def master_file_identification(self) -> MFI:
        """
        id: MFI | use: R | rpt: 1 | seq: 3
        ---
        return_type: MFI.3: Master File Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI
        """
        return self._c_data[2][0]

    @master_file_identification.setter  # set MFI.3
    def master_file_identification(self, mfi: MFI):
        """
        id: MFI | use: R | rpt: 1 | seq: 3
        ---
        param_type: MFI.3: Master File Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI
        """
        self._c_data[2] = (mfi,)

    @property  # get MFE
    def master_file_entry(self) -> tuple[MFE, ...]:
        """
        id: MFE SEGMENT GROUP | use: R | rpt: * | seq: 4
        ---
        return_type: tuple[MFE, ...]: (Master File Entry, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        return self._c_data[3]

    @master_file_entry.setter  # set MFE
    def master_file_entry(self, mfe: MFE | tuple[MFE, ...]):
        """
        id: MFE SEGMENT GROUP | use: R | rpt: * | seq: 4
        ---
        param_type: MFE.4 | tuple[MFE, ...]: (Master File Entry, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        if isinstance(mfe, tuple):
            self._c_data[3] = mfe
        else:
            self._c_data[3] = (mfe,)
