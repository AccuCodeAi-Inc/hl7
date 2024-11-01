from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.MFK_M02_MF_STAFF_GROUP import MFK_M02_MF_STAFF_GROUP
from ..segments.ERR import ERR
from ..segments.MSH import MSH
from ..segments.MSA import MSA
from ..segments.MFI import MFI
from ..segments.MFA import MFA
from ..segments.SFT import SFT


"""
Master file acknowledgment - Staff/practitioner master file - MFK_M02
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::MFK_M02 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFK_M02
from utils.hl7.v2_5_1.segments import (
    MFI, MFA, SFT, ERR, MSA, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    MFK_M02_MF_STAFF_GROUP
)

mfk_m02 = MFK_M02(  #  - The staff identification (STF), practitioner detail (PRA), and practitioner organization unit segment (ORG) segments can be used to transmit master files information between systems
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    master_file_identification=mfi,  # MFI(...)  # Required.
    master_file_acknowledgment=None,  # MFA(...) 
    mf_staff=mfk_m02_mf_staff_group,  # MFK_M02_MF_STAFF_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::MFK_M02 TEMPLATE-----
"""


class MFK_M02(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """MFK_M02"""
    _hl7_name = """Master file acknowledgment - Staff/practitioner master file"""
    _hl7_description = """The staff identification (STF), practitioner detail (PRA), and practitioner organization unit segment (ORG) segments can be used to transmit master files information between systems"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFK_M02"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 65535, 65535)
    _c_usage = ("R", "O", "R", "O", "R", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "None")
    _c_components = (MSH, SFT, MSA, ERR, MFI, MFA, MFK_M02_MF_STAFF_GROUP)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "MFI", "MFA", "MF STAFF")
    _c_is_group = (False, False, False, False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "master_file_identification", "master_file_acknowledgment", "mf_staff",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        master_file_identification: MFI,  #  Required. MFI.5
        mf_staff: MFK_M02_MF_STAFF_GROUP
        | tuple[
            MFK_M02_MF_STAFF_GROUP, ...
        ],  #  Required. (MFE.7, STF.8, PRA.9, ORG.10, AFF.11, LAN.12, EDU.13, CER.14, NTE.15, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.4
        master_file_acknowledgment: MFA | tuple[MFA, ...] | None = None,  #  MFA.6
    ):
        """
         - `MFK_M02 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFK_M02>`_
        The staff identification (STF), practitioner detail (PRA), and practitioner organization unit segment (ORG) segments can be used to transmit master files information between systems. The STF segment provides general information about personnel; the PRA and ORG segments provides detailed information for a staff member who is also a health practitioner. Other segments may be defined to follow the STF segment to provide additional detail information for a particular type of staff member: the PRA and ORG segments are the first such segments

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: *)
        :param master_file_identification: Master File Identification (id: MFI | seq: 5 | use: R | rpt: 1)
        :param master_file_acknowledgment: Master File Acknowledgment (id: MFA | seq: 6 | use: O | rpt: *)
        :param mf_staff: Mf Staff segment group: [MFE, STF, PRA|None, ORG|None, AFF|None, LAN|None, EDU|None, CER|None, NTE|None] (id: MF STAFF | seq: 7, 8, 9, 10, 11, 12, 13, 14, 15 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.master_file_identification = master_file_identification
        self.master_file_acknowledgment = master_file_acknowledgment
        self.mf_staff = mf_staff

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

    @property  # get MF STAFF
    def mf_staff(self) -> tuple[MFK_M02_MF_STAFF_GROUP, ...]:
        """
        id: MFK_M02_MF_STAFF_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[MFK_M02_MF_STAFF_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFK_M02_MF_STAFF_GROUP
        """
        return self._c_data[6]

    @mf_staff.setter  # set MF STAFF
    def mf_staff(
        self, mf_staff: MFK_M02_MF_STAFF_GROUP | tuple[MFK_M02_MF_STAFF_GROUP, ...]
    ):
        """
        id: MF STAFF SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: MFK_M02_MF_STAFF_GROUP.None | tuple[MFK_M02_MF_STAFF_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFK_M02_MF_STAFF_GROUP
        """
        if isinstance(mf_staff, tuple):
            self._c_data[6] = mf_staff
        else:
            self._c_data[6] = (mf_staff,)
