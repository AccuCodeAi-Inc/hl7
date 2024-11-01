from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segment_groups.MFN_M15_MF_INV_ITEM_GROUP import MFN_M15_MF_INV_ITEM_GROUP
from ..segments.MFI import MFI
from ..segments.SFT import SFT


"""
Master File Notification - Inventory Item Master File Message - MFN_M15
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::MFN_M15 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M15
from utils.hl7.v2_5_1.segments import (
    SFT, MFI, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    MFN_M15_MF_INV_ITEM_GROUP
)

mfn_m15 = MFN_M15(  #  - This section is concerned with describing a master file message that should be used to communicate information that relates to the inventory of items that can be used to perform an ordered service
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    master_file_identification=mfi,  # MFI(...)  # Required.
    mf_inv_item=mfn_m15_mf_inv_item_group,  # MFN_M15_MF_INV_ITEM_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::MFN_M15 TEMPLATE-----
"""


class MFN_M15(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """MFN_M15"""
    _hl7_name = """Master File Notification - Inventory Item Master File Message"""
    _hl7_description = """This section is concerned with describing a master file message that should be used to communicate information that relates to the inventory of items that can be used to perform an ordered service"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M15"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "None")
    _c_components = (MSH, SFT, MFI, MFN_M15_MF_INV_ITEM_GROUP)
    _c_name = ("MSH", "SFT", "MFI", "MF INV ITEM")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "master_file_identification", "mf_inv_item",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        master_file_identification: MFI,  #  Required. MFI.3
        mf_inv_item: MFN_M15_MF_INV_ITEM_GROUP
        | tuple[MFN_M15_MF_INV_ITEM_GROUP, ...],  #  Required. (MFE.4, IIM.5, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `MFN_M15 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M15>`_
        This section is concerned with describing a master file message that should be used to communicate information that relates to the inventory of items that can be used to perform an ordered service.  While an order specifies a service that is represented in an Other Observation/Service Item master file, this message is concerned with communicating attributes of those orderable items (for example lot number and expiration date) that are represented in the Other Observation/Service Item master file.  These attributes are more granular than can be represented in the Other Observation/Service Item master file as there may be multiple items in inventory that meet the characteristics of the Service Item but have different specific characteristics, e.g., multiple lots of a vaccine

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param master_file_identification: Master File Identification (id: MFI | seq: 3 | use: R | rpt: 1)
        :param mf_inv_item: Mf Inv Item segment group: [MFE, IIM] (id: MF INV ITEM | seq: 4, 5 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.master_file_identification = master_file_identification
        self.mf_inv_item = mf_inv_item

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

    @property  # get MF INV ITEM
    def mf_inv_item(self) -> tuple[MFN_M15_MF_INV_ITEM_GROUP, ...]:
        """
        id: MFN_M15_MF_INV_ITEM_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[MFN_M15_MF_INV_ITEM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M15_MF_INV_ITEM_GROUP
        """
        return self._c_data[3]

    @mf_inv_item.setter  # set MF INV ITEM
    def mf_inv_item(
        self,
        mf_inv_item: MFN_M15_MF_INV_ITEM_GROUP | tuple[MFN_M15_MF_INV_ITEM_GROUP, ...],
    ):
        """
        id: MF INV ITEM SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: MFN_M15_MF_INV_ITEM_GROUP.None | tuple[MFN_M15_MF_INV_ITEM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M15_MF_INV_ITEM_GROUP
        """
        if isinstance(mf_inv_item, tuple):
            self._c_data[3] = mf_inv_item
        else:
            self._c_data[3] = (mf_inv_item,)
