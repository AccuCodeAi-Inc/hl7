from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segment_groups.MFN_M05_MF_LOCATION_GROUP import MFN_M05_MF_LOCATION_GROUP
from ..segments.MFI import MFI
from ..segments.SFT import SFT


"""
Master files notification - Patient location master file - MFN_M05
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::MFN_M05 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M05
from utils.hl7.v2_5_1.segments import (
    SFT, MFI, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    MFN_M05_MF_LOCATION_GROUP
)

mfn_m05 = MFN_M05(  #  - This section is specifically concerned with describing a master file message that should be used to transmit information which identifies the inventory of healthcare patient locations, such as nursing units, rooms, beds, clinics, exam rooms, etc
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    master_file_identification=mfi,  # MFI(...)  # Required.
    mf_location=mfn_m05_mf_location_group,  # MFN_M05_MF_LOCATION_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::MFN_M05 TEMPLATE-----
"""


class MFN_M05(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """MFN_M05"""
    _hl7_name = """Master files notification - Patient location master file"""
    _hl7_description = """This section is specifically concerned with describing a master file message that should be used to transmit information which identifies the inventory of healthcare patient locations, such as nursing units, rooms, beds, clinics, exam rooms, etc"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M05"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "None")
    _c_components = (MSH, SFT, MFI, MFN_M05_MF_LOCATION_GROUP)
    _c_name = ("MSH", "SFT", "MFI", "MF LOCATION")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "master_file_identification", "mf_location",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        master_file_identification: MFI,  #  Required. MFI.3
        mf_location: MFN_M05_MF_LOCATION_GROUP
        | tuple[
            MFN_M05_MF_LOCATION_GROUP, ...
        ],  #  Required. (MFE.4, LOC.5, LCH.6, LRL.7, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `MFN_M05 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M05>`_
        This section is specifically concerned with describing a master file message that should be used to transmit information which identifies the inventory of healthcare patient locations, such as nursing units, rooms, beds, clinics, exam rooms, etc.  In a network environment, this segment can be used to define patient locations to other applications.  The segment also includes the readiness states and support locations for the patient locations.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param master_file_identification: Master File Identification (id: MFI | seq: 3 | use: R | rpt: 1)
        :param mf_location: Mf Location segment group: [MFE, LOC, LCH|None, LRL|None, MF LOC DEPT] (id: MF LOCATION | seq: 4, 5, 6, 7, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.master_file_identification = master_file_identification
        self.mf_location = mf_location

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

    @property  # get MF LOCATION
    def mf_location(self) -> tuple[MFN_M05_MF_LOCATION_GROUP, ...]:
        """
        id: MFN_M05_MF_LOCATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[MFN_M05_MF_LOCATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M05_MF_LOCATION_GROUP
        """
        return self._c_data[3]

    @mf_location.setter  # set MF LOCATION
    def mf_location(
        self,
        mf_location: MFN_M05_MF_LOCATION_GROUP | tuple[MFN_M05_MF_LOCATION_GROUP, ...],
    ):
        """
        id: MF LOCATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: MFN_M05_MF_LOCATION_GROUP.None | tuple[MFN_M05_MF_LOCATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M05_MF_LOCATION_GROUP
        """
        if isinstance(mf_location, tuple):
            self._c_data[3] = mf_location
        else:
            self._c_data[3] = (mf_location,)
