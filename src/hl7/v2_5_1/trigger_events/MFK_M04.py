from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.ERR import ERR
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.MFA import MFA
from ..segments.MSA import MSA
from ..segments.MFI import MFI


"""
Master file acknowledgment - Charge description master file - MFK_M04
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::MFK_M04 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFK_M04
from utils.hl7.v2_5_1.segments import (
    MSH, MFI, SFT, ERR, MFA, MSA
)

mfk_m04 = MFK_M04(  #  - The charge description (CDM) master file segment should be used in conjunction with the general master file segments in Section 8
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    master_file_identification=mfi,  # MFI(...)  # Required.
    master_file_acknowledgment=None,  # MFA(...) 
)

-----END TRIGGER_EVENT::MFK_M04 TEMPLATE-----
"""


class MFK_M04(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """MFK_M04"""
    _hl7_name = """Master file acknowledgment - Charge description master file"""
    _hl7_description = """The charge description (CDM) master file segment should be used in conjunction with the general master file segments in Section 8"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFK_M04"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6")
    _c_components = (MSH, SFT, MSA, ERR, MFI, MFA)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "MFI", "MFA")
    _c_is_group = (False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "master_file_identification", "master_file_acknowledgment",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        master_file_identification: MFI,  #  Required. MFI.5
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.4
        master_file_acknowledgment: MFA | tuple[MFA, ...] | None = None,  #  MFA.6
    ):
        """
         - `MFK_M04 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFK_M04>`_
        The charge description (CDM) master file segment should be used in conjunction with the general master file segments in Section 8.5, GENERAL MASTER FILE SEGMENTS.  Interfacing systems often need not only to communicate data about a patient’s detailed charges, but also to communicate the charge identification entries by which an application knows how to handle a particular charge code.  The charge description master is a master file.  The CDM segment below is a specially designed master file segment for interfacing charge description masters.  In the following message, the MFI-master file identifier should equal "CDM."

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: *)
        :param master_file_identification: Master File Identification (id: MFI | seq: 5 | use: R | rpt: 1)
        :param master_file_acknowledgment: Master File Acknowledgment (id: MFA | seq: 6 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.master_file_identification = master_file_identification
        self.master_file_acknowledgment = master_file_acknowledgment

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

    @property  # get ERR
    def error(self) -> tuple[ERR, ...] | tuple[None]:
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        return_type: tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        return self._c_data[3]

    @error.setter  # set ERR
    def error(self, err: ERR | tuple[ERR, ...] | None):
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        param_type: ERR.4 | tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        if isinstance(err, tuple):
            self._c_data[3] = err
        else:
            self._c_data[3] = (err,)

    @property  # get MFI.5
    def master_file_identification(self) -> MFI:
        """
        id: MFI | use: R | rpt: 1 | seq: 5
        ---
        return_type: MFI.5: Master File Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI
        """
        return self._c_data[4][0]

    @master_file_identification.setter  # set MFI.5
    def master_file_identification(self, mfi: MFI):
        """
        id: MFI | use: R | rpt: 1 | seq: 5
        ---
        param_type: MFI.5: Master File Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI
        """
        self._c_data[4] = (mfi,)

    @property  # get MFA
    def master_file_acknowledgment(self) -> tuple[MFA, ...] | tuple[None]:
        """
        id: MFA SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[MFA, ...]: (Master File Acknowledgment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFA
        """
        return self._c_data[5]

    @master_file_acknowledgment.setter  # set MFA
    def master_file_acknowledgment(self, mfa: MFA | tuple[MFA, ...] | None):
        """
        id: MFA SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: MFA.6 | tuple[MFA, ...]: (Master File Acknowledgment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFA
        """
        if isinstance(mfa, tuple):
            self._c_data[5] = mfa
        else:
            self._c_data[5] = (mfa,)
