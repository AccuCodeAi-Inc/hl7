from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.LRL import LRL
from ..segment_groups.MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP import (
    MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP,
)
from ..segments.MFE import MFE
from ..segments.LOC import LOC
from ..segments.LCH import LCH


"""
MF LOCATION - MFN_M05_MF_LOCATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M05_MF_LOCATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M05_MF_LOCATION_GROUP
from utils.hl7.v2_5_1.segments import (
    LRL, LCH, MFE, LOC
)
from utils.hl7.v2_5_1.segment_groups import (
    MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP
)

mfn_m05_mf_location_group = MFN_M05_MF_LOCATION_GROUP(  # MF LOCATION - Segment group for MFN_M05 - Master files notification - Patient location master file consisting of MFE, LOC, LCH|None, LRL|None, MF LOC DEPT
    master_file_entry=mfe,  # MFE(...)  # Required.
    location_identification=loc,  # LOC(...)  # Required.
    location_characteristic=None,  # LCH(...) 
    location_relationship=None,  # LRL(...) 
    mf_loc_dept=mfn_m05_mf_location_group_mf_loc_dept_group,  # MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M05_MF_LOCATION_GROUP TEMPLATE-----
"""


class MFN_M05_MF_LOCATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M05_MF_LOCATION_GROUP"""
    _hl7_name = """MF LOCATION"""
    _hl7_description = """Segment group for MFN_M05 - Master files notification - Patient location master file consisting of MFE, LOC, LCH|None, LRL|None, MF LOC DEPT"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M05_MF_LOCATION_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535)
    _c_usage = ("R", "R", "O", "O", "R")
    _c_aliases = ("4", "5", "6", "7", "None")
    _c_components = (MFE, LOC, LCH, LRL, MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP)
    _c_name = ("MFE", "LOC", "LCH", "LRL", "MF LOC DEPT")
    _c_is_group = (False, False, False, False, True)
    _c_attrs = ("master_file_entry", "location_identification", "location_characteristic", "location_relationship", "mf_loc_dept",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.4
        location_identification: LOC,  #  Required. LOC.5
        mf_loc_dept: MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP
        | tuple[
            MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP, ...
        ],  #  Required. (LDP.8, LCH.9, LCC.10, ...)
        location_characteristic: LCH | tuple[LCH, ...] | None = None,  #  LCH.6
        location_relationship: LRL | tuple[LRL, ...] | None = None,  #  LRL.7
    ):
        """
        None - `MFN_M05_MF_LOCATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M05_MF_LOCATION_GROUP>`_
        Segment group for MFN_M05 - Master files notification - Patient location master file consisting of MFE, LOC, LCH|None, LRL|None, MF LOC DEPT

        :param master_file_entry: Master File Entry (id: MFE | seq: 4 | use: R | rpt: 1)
        :param location_identification: Location Identification (id: LOC | seq: 5 | use: R | rpt: 1)
        :param location_characteristic: Location Characteristic (id: LCH | seq: 6 | use: O | rpt: *)
        :param location_relationship: Location Relationship (id: LRL | seq: 7 | use: O | rpt: *)
        :param mf_loc_dept: Mf Loc Dept segment group: [LDP, LCH|None, LCC|None] (id: MF LOC DEPT | seq: 8, 9, 10 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.master_file_entry = master_file_entry
        self.location_identification = location_identification
        self.location_characteristic = location_characteristic
        self.location_relationship = location_relationship
        self.mf_loc_dept = mf_loc_dept

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

    @property  # get LOC.5
    def location_identification(self) -> LOC:
        """
        id: LOC | use: R | rpt: 1 | seq: 5
        ---
        return_type: LOC.5: Location Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LOC
        """
        return self._c_data[1][0]

    @location_identification.setter  # set LOC.5
    def location_identification(self, loc: LOC):
        """
        id: LOC | use: R | rpt: 1 | seq: 5
        ---
        param_type: LOC.5: Location Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LOC
        """
        self._c_data[1] = (loc,)

    @property  # get LCH
    def location_characteristic(self) -> tuple[LCH, ...] | tuple[None]:
        """
        id: LCH SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[LCH, ...]: (Location Characteristic, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCH
        """
        return self._c_data[2]

    @location_characteristic.setter  # set LCH
    def location_characteristic(self, lch: LCH | tuple[LCH, ...] | None):
        """
        id: LCH SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: LCH.6 | tuple[LCH, ...]: (Location Characteristic, ...)
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
        id: LRL SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[LRL, ...]: (Location Relationship, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LRL
        """
        return self._c_data[3]

    @location_relationship.setter  # set LRL
    def location_relationship(self, lrl: LRL | tuple[LRL, ...] | None):
        """
        id: LRL SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: LRL.7 | tuple[LRL, ...]: (Location Relationship, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LRL
        """
        if isinstance(lrl, tuple):
            self._c_data[3] = lrl
        else:
            self._c_data[3] = (lrl,)

    @property  # get MF LOC DEPT
    def mf_loc_dept(self) -> tuple[MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP, ...]:
        """
        id: MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP
        """
        return self._c_data[4]

    @mf_loc_dept.setter  # set MF LOC DEPT
    def mf_loc_dept(
        self,
        mf_loc_dept: MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP
        | tuple[MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP, ...],
    ):
        """
        id: MF LOC DEPT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP.None | tuple[MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M05_MF_LOCATION_GROUP_MF_LOC_DEPT_GROUP
        """
        if isinstance(mf_loc_dept, tuple):
            self._c_data[4] = mf_loc_dept
        else:
            self._c_data[4] = (mf_loc_dept,)
