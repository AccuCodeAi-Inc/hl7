from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CDM import CDM
from ..segments.PRC import PRC
from ..segments.MFE import MFE


"""
MF QUERY - MFR_M04_MF_QUERY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFR_M04_MF_QUERY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFR_M04_MF_QUERY_GROUP
from utils.hl7.v2_5_1.segments import (
    PRC, MFE, CDM
)

mfr_m04_mf_query_group = MFR_M04_MF_QUERY_GROUP(  # MF QUERY - Segment group for MFR_M04 - Master Files Response - Charge description master file consisting of MFE, CDM, PRC|None
    master_file_entry=mfe,  # MFE(...)  # Required.
    charge_description_master=cdm,  # CDM(...)  # Required.
    pricing=None,  # PRC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFR_M04_MF_QUERY_GROUP TEMPLATE-----
"""


class MFR_M04_MF_QUERY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFR_M04_MF_QUERY_GROUP"""
    _hl7_name = """MF QUERY"""
    _hl7_description = """Segment group for MFR_M04 - Master Files Response - Charge description master file consisting of MFE, CDM, PRC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFR_M04_MF_QUERY_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("9", "10", "11")
    _c_components = (MFE, CDM, PRC)
    _c_name = ("MFE", "CDM", "PRC")
    _c_is_group = (False, False, False)
    _c_attrs = ("master_file_entry", "charge_description_master", "pricing",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.9
        charge_description_master: CDM,  #  Required. CDM.10
        pricing: PRC | tuple[PRC, ...] | None = None,  #  PRC.11
    ):
        """
        None - `MFR_M04_MF_QUERY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFR_M04_MF_QUERY_GROUP>`_
        Segment group for MFR_M04 - Master Files Response - Charge description master file consisting of MFE, CDM, PRC|None

        :param master_file_entry: Master File Entry (id: MFE | seq: 9 | use: R | rpt: 1)
        :param charge_description_master: Charge Description Master (id: CDM | seq: 10 | use: R | rpt: 1)
        :param pricing: Pricing (id: PRC | seq: 11 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.master_file_entry = master_file_entry
        self.charge_description_master = charge_description_master
        self.pricing = pricing

    @property  # get MFE.9
    def master_file_entry(self) -> MFE:
        """
        id: MFE | use: R | rpt: 1 | seq: 9
        ---
        return_type: MFE.9: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        return self._c_data[0][0]

    @master_file_entry.setter  # set MFE.9
    def master_file_entry(self, mfe: MFE):
        """
        id: MFE | use: R | rpt: 1 | seq: 9
        ---
        param_type: MFE.9: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        self._c_data[0] = (mfe,)

    @property  # get CDM.10
    def charge_description_master(self) -> CDM:
        """
        id: CDM | use: R | rpt: 1 | seq: 10
        ---
        return_type: CDM.10: Charge Description Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CDM
        """
        return self._c_data[1][0]

    @charge_description_master.setter  # set CDM.10
    def charge_description_master(self, cdm: CDM):
        """
        id: CDM | use: R | rpt: 1 | seq: 10
        ---
        param_type: CDM.10: Charge Description Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CDM
        """
        self._c_data[1] = (cdm,)

    @property  # get PRC
    def pricing(self) -> tuple[PRC, ...] | tuple[None]:
        """
        id: PRC SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[PRC, ...]: (Pricing, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRC
        """
        return self._c_data[2]

    @pricing.setter  # set PRC
    def pricing(self, prc: PRC | tuple[PRC, ...] | None):
        """
        id: PRC SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: PRC.11 | tuple[PRC, ...]: (Pricing, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRC
        """
        if isinstance(prc, tuple):
            self._c_data[2] = prc
        else:
            self._c_data[2] = (prc,)
