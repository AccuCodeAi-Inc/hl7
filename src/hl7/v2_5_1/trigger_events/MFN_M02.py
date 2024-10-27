from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.MFI import MFI
from ..segment_groups.MFN_M02_MF_STAFF_GROUP import MFN_M02_MF_STAFF_GROUP


"""
Master files notification - Staff/practitioner master file - MFN_M02
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::MFN_M02 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M02
from utils.hl7.v2_5_1.segments import (
    SFT, MFI, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    MFN_M02_MF_STAFF_GROUP
)

mfn_m02 = MFN_M02(  #  - The staff identification (STF), practitioner detail (PRA), practitioner organization unit segment (ORG), professional affiliation (AFF), language detail (LAN), educational detail (EDU), and certificate detail (CER) segments can be used to transmit master files information between systems
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    master_file_identification=mfi,  # MFI(...)  # Required.
    mf_staff=mfn_m02_mf_staff_group,  # MFN_M02_MF_STAFF_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::MFN_M02 TEMPLATE-----
"""


class MFN_M02(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """MFN_M02"""
    _hl7_name = """Master files notification - Staff/practitioner master file"""
    _hl7_description = """The staff identification (STF), practitioner detail (PRA), practitioner organization unit segment (ORG), professional affiliation (AFF), language detail (LAN), educational detail (EDU), and certificate detail (CER) segments can be used to transmit master files information between systems"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M02"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "None")
    _c_components = (MSH, SFT, MFI, MFN_M02_MF_STAFF_GROUP)
    _c_name = ("MSH", "SFT", "MFI", "MF STAFF")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "master_file_identification", "mf_staff",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        master_file_identification: MFI,  #  Required. MFI.3
        mf_staff: MFN_M02_MF_STAFF_GROUP
        | tuple[
            MFN_M02_MF_STAFF_GROUP, ...
        ],  #  Required. (MFE.4, STF.5, PRA.6, ORG.7, AFF.8, LAN.9, EDU.10, CER.11, NTE.12, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `MFN_M02 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M02>`_
        The staff identification (STF), practitioner detail (PRA), practitioner organization unit segment (ORG), professional affiliation (AFF), language detail (LAN), educational detail (EDU), and certificate detail (CER) segments can be used to transmit master files information between systems. The STF segment provides general information about personnel; the PRA, ORG, AFF, LAN, EDU, CER and NTE segments provide detailed information for a staff member.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param master_file_identification: Master File Identification (id: MFI | seq: 3 | use: R | rpt: 1)
        :param mf_staff: Mf Staff segment group: [MFE, STF, PRA|None, ORG|None, AFF|None, LAN|None, EDU|None, CER|None, NTE|None] (id: MF STAFF | seq: 4, 5, 6, 7, 8, 9, 10, 11, 12 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.master_file_identification = master_file_identification
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

    @property  # get MF STAFF
    def mf_staff(self) -> tuple[MFN_M02_MF_STAFF_GROUP, ...]:
        """
        id: MFN_M02_MF_STAFF_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[MFN_M02_MF_STAFF_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M02_MF_STAFF_GROUP
        """
        return self._c_data[3]

    @mf_staff.setter  # set MF STAFF
    def mf_staff(
        self, mf_staff: MFN_M02_MF_STAFF_GROUP | tuple[MFN_M02_MF_STAFF_GROUP, ...]
    ):
        """
        id: MF STAFF SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: MFN_M02_MF_STAFF_GROUP.None | tuple[MFN_M02_MF_STAFF_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M02_MF_STAFF_GROUP
        """
        if isinstance(mf_staff, tuple):
            self._c_data[3] = mf_staff
        else:
            self._c_data[3] = (mf_staff,)
