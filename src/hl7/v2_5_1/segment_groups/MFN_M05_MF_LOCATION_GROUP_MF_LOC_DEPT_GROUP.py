from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.LDP import LDP
from ..segments.LCC import LCC
from ..segments.LCH import LCH


"""
MF LOC DEPT - MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP
from utils.hl7.v2_5_1.segments import (
    LDP, LCC, LCH
)

mfn_m05_mf_location_group_mf_loc_dept_group = MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP(  # MF LOC DEPT - Segment group for MFN_M05_MF_LOCATION_GROUP - MF LOCATION consisting of LDP, LCH|None, LCC|None
    location_department=ldp,  # LDP(...)  # Required.
    location_characteristic=None,  # LCH(...) 
    location_charge_code=None,  # LCC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP TEMPLATE-----
"""


class MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP"""
    _hl7_name = """MF LOC DEPT"""
    _hl7_description = """Segment group for MFN_M05_MF_LOCATION_GROUP - MF LOCATION consisting of LDP, LCH|None, LCC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("8", "9", "10")
    _c_components = (LDP, LCH, LCC)
    _c_name = ("LDP", "LCH", "LCC")
    _c_is_group = (False, False, False)
    _c_attrs = ("location_department", "location_characteristic", "location_charge_code",)
    # fmt: on

    def __init__(
        self,
        location_department: LDP,  #  Required. LDP.8
        location_characteristic: LCH | tuple[LCH, ...] | None = None,  #  LCH.9
        location_charge_code: LCC | tuple[LCC, ...] | None = None,  #  LCC.10
    ):
        """
        None - `MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP>`_
        Segment group for MFN_M05_MF_LOCATION_GROUP - MF LOCATION consisting of LDP, LCH|None, LCC|None

        :param location_department: Location Department (id: LDP | seq: 8 | use: R | rpt: 1)
        :param location_characteristic: Location Characteristic (id: LCH | seq: 9 | use: O | rpt: *)
        :param location_charge_code: Location Charge Code (id: LCC | seq: 10 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.location_department = location_department
        self.location_characteristic = location_characteristic
        self.location_charge_code = location_charge_code

    @property  # get LDP.8
    def location_department(self) -> LDP:
        """
        id: LDP | use: R | rpt: 1 | seq: 8
        ---
        return_type: LDP.8: Location Department
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LDP
        """
        return self._c_data[0][0]

    @location_department.setter  # set LDP.8
    def location_department(self, ldp: LDP):
        """
        id: LDP | use: R | rpt: 1 | seq: 8
        ---
        param_type: LDP.8: Location Department
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LDP
        """
        self._c_data[0] = (ldp,)

    @property  # get LCH
    def location_characteristic(self) -> tuple[LCH, ...] | tuple[None]:
        """
        id: LCH SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[LCH, ...]: (Location Characteristic, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCH
        """
        return self._c_data[1]

    @location_characteristic.setter  # set LCH
    def location_characteristic(self, lch: LCH | tuple[LCH, ...] | None):
        """
        id: LCH SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: LCH.9 | tuple[LCH, ...]: (Location Characteristic, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCH
        """
        if isinstance(lch, tuple):
            self._c_data[1] = lch
        else:
            self._c_data[1] = (lch,)

    @property  # get LCC
    def location_charge_code(self) -> tuple[LCC, ...] | tuple[None]:
        """
        id: LCC SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[LCC, ...]: (Location Charge Code, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCC
        """
        return self._c_data[2]

    @location_charge_code.setter  # set LCC
    def location_charge_code(self, lcc: LCC | tuple[LCC, ...] | None):
        """
        id: LCC SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: LCC.10 | tuple[LCC, ...]: (Location Charge Code, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCC
        """
        if isinstance(lcc, tuple):
            self._c_data[2] = lcc
        else:
            self._c_data[2] = (lcc,)
