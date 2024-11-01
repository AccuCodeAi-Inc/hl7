from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PRC import PRC
from ..segments.CDM import CDM
from ..segments.MFE import MFE


"""
MF CDM - MFN_M04_MF_CDM_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M04_MF_CDM_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M04_MF_CDM_GROUP
from utils.hl7.v2_5_1.segments import (
    MFE, CDM, PRC
)

mfn_m04_mf_cdm_group = MFN_M04_MF_CDM_GROUP(  # MF CDM - Segment group for MFN_M04 - Master files notification - Charge description master file consisting of MFE, CDM, PRC|None
    master_file_entry=mfe,  # MFE(...)  # Required.
    charge_description_master=cdm,  # CDM(...)  # Required.
    pricing=None,  # PRC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M04_MF_CDM_GROUP TEMPLATE-----
"""


class MFN_M04_MF_CDM_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M04_MF_CDM_GROUP"""
    _hl7_name = """MF CDM"""
    _hl7_description = """Segment group for MFN_M04 - Master files notification - Charge description master file consisting of MFE, CDM, PRC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M04_MF_CDM_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("4", "5", "6")
    _c_components = (MFE, CDM, PRC)
    _c_name = ("MFE", "CDM", "PRC")
    _c_is_group = (False, False, False)
    _c_attrs = ("master_file_entry", "charge_description_master", "pricing",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.4
        charge_description_master: CDM,  #  Required. CDM.5
        pricing: PRC | tuple[PRC, ...] | None = None,  #  PRC.6
    ):
        """
        None - `MFN_M04_MF_CDM_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M04_MF_CDM_GROUP>`_
        Segment group for MFN_M04 - Master files notification - Charge description master file consisting of MFE, CDM, PRC|None

        :param master_file_entry: Master File Entry (id: MFE | seq: 4 | use: R | rpt: 1)
        :param charge_description_master: Charge Description Master (id: CDM | seq: 5 | use: R | rpt: 1)
        :param pricing: Pricing (id: PRC | seq: 6 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.master_file_entry = master_file_entry
        self.charge_description_master = charge_description_master
        self.pricing = pricing

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

    @property  # get CDM.5
    def charge_description_master(self) -> CDM:
        """
        id: CDM | use: R | rpt: 1 | seq: 5
        ---
        return_type: CDM.5: Charge Description Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CDM
        """
        return self._c_data[1][0]

    @charge_description_master.setter  # set CDM.5
    def charge_description_master(self, cdm: CDM):
        """
        id: CDM | use: R | rpt: 1 | seq: 5
        ---
        param_type: CDM.5: Charge Description Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CDM
        """
        self._c_data[1] = (cdm,)

    @property  # get PRC
    def pricing(self) -> tuple[PRC, ...] | tuple[None]:
        """
        id: PRC SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[PRC, ...]: (Pricing, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRC
        """
        return self._c_data[2]

    @pricing.setter  # set PRC
    def pricing(self, prc: PRC | tuple[PRC, ...] | None):
        """
        id: PRC SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: PRC.6 | tuple[PRC, ...]: (Pricing, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRC
        """
        if isinstance(prc, tuple):
            self._c_data[2] = prc
        else:
            self._c_data[2] = (prc,)
