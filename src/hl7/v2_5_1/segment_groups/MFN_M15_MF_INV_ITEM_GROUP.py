from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.IIM import IIM
from ..segments.MFE import MFE


"""
MF INV ITEM - MFN_M15_MF_INV_ITEM_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M15_MF_INV_ITEM_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M15_MF_INV_ITEM_GROUP
from utils.hl7.v2_5_1.segments import (
    IIM, MFE
)

mfn_m15_mf_inv_item_group = MFN_M15_MF_INV_ITEM_GROUP(  # MF INV ITEM - Segment group for MFN_M15 - Master File Notification - Inventory Item Master File Message consisting of MFE, IIM
    master_file_entry=mfe,  # MFE(...)  # Required.
    inventory_item_master=iim,  # IIM(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M15_MF_INV_ITEM_GROUP TEMPLATE-----
"""


class MFN_M15_MF_INV_ITEM_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M15_MF_INV_ITEM_GROUP"""
    _hl7_name = """MF INV ITEM"""
    _hl7_description = """Segment group for MFN_M15 - Master File Notification - Inventory Item Master File Message consisting of MFE, IIM"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M15_MF_INV_ITEM_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "R")
    _c_aliases = ("4", "5")
    _c_components = (MFE, IIM)
    _c_name = ("MFE", "IIM")
    _c_is_group = (False, False)
    _c_attrs = ("master_file_entry", "inventory_item_master",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.4
        inventory_item_master: IIM,  #  Required. IIM.5
    ):
        """
        None - `MFN_M15_MF_INV_ITEM_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M15_MF_INV_ITEM_GROUP>`_
        Segment group for MFN_M15 - Master File Notification - Inventory Item Master File Message consisting of MFE, IIM

        :param master_file_entry: Master File Entry (id: MFE | seq: 4 | use: R | rpt: 1)
        :param inventory_item_master: Inventory Item Master (id: IIM | seq: 5 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.master_file_entry = master_file_entry
        self.inventory_item_master = inventory_item_master

    @property  # get MFE.4
    def master_file_entry(self) -> MFE:
        """
        id: MFE | use: R | rpt: 1 | seq: 4
        ---
        return_type: MFE.4: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        return self._c_data[0][0]

    @master_file_entry.setter  # set MFE.4
    def master_file_entry(self, mfe: MFE):
        """
        id: MFE | use: R | rpt: 1 | seq: 4
        ---
        param_type: MFE.4: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        self._c_data[0] = (mfe,)

    @property  # get IIM.5
    def inventory_item_master(self) -> IIM:
        """
        id: IIM | use: R | rpt: 1 | seq: 5
        ---
        return_type: IIM.5: Inventory Item Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IIM
        """
        return self._c_data[1][0]

    @inventory_item_master.setter  # set IIM.5
    def inventory_item_master(self, iim: IIM):
        """
        id: IIM | use: R | rpt: 1 | seq: 5
        ---
        param_type: IIM.5: Inventory Item Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IIM
        """
        self._c_data[1] = (iim,)
