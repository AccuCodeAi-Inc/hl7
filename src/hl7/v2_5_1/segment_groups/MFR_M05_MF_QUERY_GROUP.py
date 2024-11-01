from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.MFE import MFE
from ..segments.LCH import LCH
from ..segments.LRL import LRL
from ..segments.LCC import LCC
from ..segments.LDP import LDP
from ..segments.LOC import LOC


"""
MF QUERY - MFR_M05_MF_QUERY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFR_M05_MF_QUERY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFR_M05_MF_QUERY_GROUP
from utils.hl7.v2_5_1.segments import (
    LRL, LCH, LDP, LCC, LOC, MFE
)

mfr_m05_mf_query_group = MFR_M05_MF_QUERY_GROUP(  # MF QUERY - Segment group for MFR_M05 - Master Files Response - Patient Location master file consisting of MFE, LOC, LCH|None, LRL|None, LDP, LCH|None, LCC|None
    master_file_entry=mfe,  # MFE(...)  # Required.
    location_identification=loc,  # LOC(...)  # Required.
    location_characteristic=None,  # LCH(...) 
    location_relationship=None,  # LRL(...) 
    location_department=ldp,  # LDP(...)  # Required.
    location_characteristic_14=None,  # LCH(...) 
    location_charge_code=None,  # LCC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFR_M05_MF_QUERY_GROUP TEMPLATE-----
"""


class MFR_M05_MF_QUERY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFR_M05_MF_QUERY_GROUP"""
    _hl7_name = """MF QUERY"""
    _hl7_description = """Segment group for MFR_M05 - Master Files Response - Patient Location master file consisting of MFE, LOC, LCH|None, LRL|None, LDP, LCH|None, LCC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFR_M05_MF_QUERY_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "R", "O", "O", "R", "O", "O")
    _c_aliases = ("9", "10", "11", "12", "13", "14", "15")
    _c_components = (MFE, LOC, LCH, LRL, LDP, LCH, LCC)
    _c_name = ("MFE", "LOC", "LCH", "LRL", "LDP", "LCH", "LCC")
    _c_is_group = (False, False, False, False, False, False, False)
    _c_attrs = ("master_file_entry", "location_identification", "location_characteristic", "location_relationship", "location_department", "location_characteristic_14", "location_charge_code",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.9
        location_identification: LOC,  #  Required. LOC.10
        location_department: LDP | tuple[LDP, ...],  #  Required. LDP.13
        location_characteristic: LCH | tuple[LCH, ...] | None = None,  #  LCH.11
        location_relationship: LRL | tuple[LRL, ...] | None = None,  #  LRL.12
        location_characteristic_14: LCH | tuple[LCH, ...] | None = None,  #  LCH.14
        location_charge_code: LCC | tuple[LCC, ...] | None = None,  #  LCC.15
    ):
        """
        None - `MFR_M05_MF_QUERY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFR_M05_MF_QUERY_GROUP>`_
        Segment group for MFR_M05 - Master Files Response - Patient Location master file consisting of MFE, LOC, LCH|None, LRL|None, LDP, LCH|None, LCC|None

        :param master_file_entry: Master File Entry (id: MFE | seq: 9 | use: R | rpt: 1)
        :param location_identification: Location Identification (id: LOC | seq: 10 | use: R | rpt: 1)
        :param location_characteristic: Location Characteristic (id: LCH | seq: 11 | use: O | rpt: *)
        :param location_relationship: Location Relationship (id: LRL | seq: 12 | use: O | rpt: *)
        :param location_department: Location Department (id: LDP | seq: 13 | use: R | rpt: *)
        :param location_characteristic_14: Location Characteristic (id: LCH | seq: 14 | use: O | rpt: *)
        :param location_charge_code: Location Charge Code (id: LCC | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.master_file_entry = master_file_entry
        self.location_identification = location_identification
        self.location_characteristic = location_characteristic
        self.location_relationship = location_relationship
        self.location_department = location_department
        self.location_characteristic_14 = location_characteristic_14
        self.location_charge_code = location_charge_code

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

    @property  # get LOC.10
    def location_identification(self) -> LOC:
        """
        id: LOC | use: R | rpt: 1 | seq: 10
        ---
        return_type: LOC.10: Location Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LOC
        """
        return self._c_data[1][0]

    @location_identification.setter  # set LOC.10
    def location_identification(self, loc: LOC):
        """
        id: LOC | use: R | rpt: 1 | seq: 10
        ---
        param_type: LOC.10: Location Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LOC
        """
        self._c_data[1] = (loc,)

    @property  # get LCH
    def location_characteristic(self) -> tuple[LCH, ...] | tuple[None]:
        """
        id: LCH SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[LCH, ...]: (Location Characteristic, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCH
        """
        return self._c_data[2]

    @location_characteristic.setter  # set LCH
    def location_characteristic(self, lch: LCH | tuple[LCH, ...] | None):
        """
        id: LCH SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: LCH.11 | tuple[LCH, ...]: (Location Characteristic, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCH
        """
        if isinstance(lch, tuple):
            self._c_data[2] = lch
        else:
            self._c_data[2] = (lch,)

    @property  # get LRL
    def location_relationship(self) -> tuple[LRL, ...] | tuple[None]:
        """
        id: LRL SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[LRL, ...]: (Location Relationship, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LRL
        """
        return self._c_data[3]

    @location_relationship.setter  # set LRL
    def location_relationship(self, lrl: LRL | tuple[LRL, ...] | None):
        """
        id: LRL SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: LRL.12 | tuple[LRL, ...]: (Location Relationship, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LRL
        """
        if isinstance(lrl, tuple):
            self._c_data[3] = lrl
        else:
            self._c_data[3] = (lrl,)

    @property  # get LDP
    def location_department(self) -> tuple[LDP, ...]:
        """
        id: LDP SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        return_type: tuple[LDP, ...]: (Location Department, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LDP
        """
        return self._c_data[4]

    @location_department.setter  # set LDP
    def location_department(self, ldp: LDP | tuple[LDP, ...]):
        """
        id: LDP SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        param_type: LDP.13 | tuple[LDP, ...]: (Location Department, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LDP
        """
        if isinstance(ldp, tuple):
            self._c_data[4] = ldp
        else:
            self._c_data[4] = (ldp,)

    @property  # get LCH
    def location_characteristic_14(self) -> tuple[LCH, ...] | tuple[None]:
        """
        id: LCH SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        return_type: tuple[LCH, ...]: (Location Characteristic, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCH
        """
        return self._c_data[5]

    @location_characteristic_14.setter  # set LCH
    def location_characteristic_14(self, lch: LCH | tuple[LCH, ...] | None):
        """
        id: LCH SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        param_type: LCH.14 | tuple[LCH, ...]: (Location Characteristic, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCH
        """
        if isinstance(lch, tuple):
            self._c_data[5] = lch
        else:
            self._c_data[5] = (lch,)

    @property  # get LCC
    def location_charge_code(self) -> tuple[LCC, ...] | tuple[None]:
        """
        id: LCC SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[LCC, ...]: (Location Charge Code, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCC
        """
        return self._c_data[6]

    @location_charge_code.setter  # set LCC
    def location_charge_code(self, lcc: LCC | tuple[LCC, ...] | None):
        """
        id: LCC SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: LCC.15 | tuple[LCC, ...]: (Location Charge Code, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCC
        """
        if isinstance(lcc, tuple):
            self._c_data[6] = lcc
        else:
            self._c_data[6] = (lcc,)
