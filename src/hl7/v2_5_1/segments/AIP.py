from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.IS import IS
from ..data_types.XCN import XCN
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..tables.StaffType import StaffType
from ..tables.AllowSubstitutionCodes import AllowSubstitutionCodes
from ..tables.FillerStatusCodes import FillerStatusCodes
from ..tables.SegmentActionCode import SegmentActionCode


"""
Appointment Information - Personnel Resource - AIP
HL7 Version: 2.5.1

-----BEGIN SEGMENT::AIP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    AIP,
    TS, ID, NM, IS, XCN, SI, CE
)

aip = AIP(  #  - The AIP segment contains information about the personnel types that can be scheduled
    set_id_aip=si,  # SI(...)  # Required.
    segment_action_code=None,  # ID(...) 
    personnel_resource_id=None,  # XCN(...) 
    resource_type=None,  # CE(...) 
    resource_group=None,  # CE(...) 
    start_date_or_time=None,  # TS(...) 
    start_date_or_time_offset=None,  # NM(...) 
    start_date_or_time_offset_units=None,  # CE(...) 
    duration=None,  # NM(...) 
    duration_units=None,  # CE(...) 
    allow_substitution_code=None,  # IS(...) 
    filler_status_code=None,  # CE(...) 
)

-----END SEGMENT::AIP TEMPLATE-----
"""


class AIP(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """AIP"""
    _hl7_name = """Appointment Information - Personnel Resource"""
    _hl7_description = """The AIP segment contains information about the personnel types that can be scheduled"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIP"
    _c_length = (4, 3, 250, 250, 250, 26, 20, 250, 20, 250, 10, 250,)
    _c_rpt = (1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "C", "C", "C", "O", "C", "C", "C", "O", "O", "C", "C",)
    _c_components = (SI, ID, XCN, CE, CE, TS, NM, CE, NM, CE, IS, CE,)
    _c_aliases = ("AIP.1", "AIP.2", "AIP.3", "AIP.4", "AIP.5", "AIP.6", "AIP.7", "AIP.8", "AIP.9", "AIP.10", "AIP.11", "AIP.12",)
    _c_names = ("Set ID - AIP", "Segment Action Code", "Personnel Resource ID", "Resource Type", "Resource Group", "Start Date/Time", "Start Date/Time Offset", "Start Date/Time Offset Units", "Duration", "Duration Units", "Allow Substitution Code", "Filler Status Code",)
    _c_attrs = ("set_id_aip", "segment_action_code", "personnel_resource_id", "resource_type", "resource_group", "start_date_or_time", "start_date_or_time_offset", "start_date_or_time_offset_units", "duration", "duration_units", "allow_substitution_code", "filler_status_code",)
    # fmt: on

    def __init__(
        self,
        set_id_aip: SI | tuple[SI],  # AIP.1
        segment_action_code: SegmentActionCode
        | ID
        | tuple[SegmentActionCode | ID]
        | None = None,  # AIP.2
        personnel_resource_id: XCN | tuple[XCN] | None = None,  # AIP.3
        resource_type: StaffType | CE | tuple[StaffType | CE] | None = None,  # AIP.4
        resource_group: CE | tuple[CE] | None = None,  # AIP.5
        start_date_or_time: TS | tuple[TS] | None = None,  # AIP.6
        start_date_or_time_offset: NM | tuple[NM] | None = None,  # AIP.7
        start_date_or_time_offset_units: CE | tuple[CE] | None = None,  # AIP.8
        duration: NM | tuple[NM] | None = None,  # AIP.9
        duration_units: CE | tuple[CE] | None = None,  # AIP.10
        allow_substitution_code: AllowSubstitutionCodes
        | IS
        | tuple[AllowSubstitutionCodes | IS]
        | None = None,  # AIP.11
        filler_status_code: FillerStatusCodes
        | CE
        | tuple[FillerStatusCodes | CE]
        | None = None,  # AIP.12
    ):
        """
        Appointment Information - Personnel Resource - `AIP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIP>`_
        The AIP segment contains information about the personnel types that can be scheduled. Personnel included in a transaction using this segment are assumed to be controlled by a schedule on a schedule filler application. Personnel not controlled by a schedule are not identified on a schedule request using this segment. The kinds of personnel described on this segment include any healthcare provider in the institution controlled by a schedule (for example: technicians, physicians, nurses, surgeons, anesthesiologists, or CRNAs).

        :param set_id_aip: Sequence ID (id: AIP.1 | len: 4 | use: R | rpt: 1)
        :param segment_action_code: Coded values for HL7 tables (id: AIP.2 | len: 3 | use: C | rpt: 1)
        :param personnel_resource_id: Extended Composite ID Number and Name for Persons (id: AIP.3 | len: 250 | use: C | rpt: *)
        :param resource_type: Coded Element (id: AIP.4 | len: 250 | use: C | rpt: 1)
        :param resource_group: Coded Element (id: AIP.5 | len: 250 | use: O | rpt: 1)
        :param start_date_or_time: Time Stamp (id: AIP.6 | len: 26 | use: C | rpt: 1)
        :param start_date_or_time_offset: Numeric (id: AIP.7 | len: 20 | use: C | rpt: 1)
        :param start_date_or_time_offset_units: Coded Element (id: AIP.8 | len: 250 | use: C | rpt: 1)
        :param duration: Numeric (id: AIP.9 | len: 20 | use: O | rpt: 1)
        :param duration_units: Coded Element (id: AIP.10 | len: 250 | use: O | rpt: 1)
        :param allow_substitution_code: Coded value for user-defined tables (id: AIP.11 | len: 10 | use: C | rpt: 1)
        :param filler_status_code: Coded Element (id: AIP.12 | len: 250 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.set_id_aip = set_id_aip
        self.segment_action_code = segment_action_code
        self.personnel_resource_id = personnel_resource_id
        self.resource_type = resource_type
        self.resource_group = resource_group
        self.start_date_or_time = start_date_or_time
        self.start_date_or_time_offset = start_date_or_time_offset
        self.start_date_or_time_offset_units = start_date_or_time_offset_units
        self.duration = duration
        self.duration_units = duration_units
        self.allow_substitution_code = allow_substitution_code
        self.filler_status_code = filler_status_code

    @property  # get AIP.1
    def set_id_aip(self) -> SI:
        """
        id: AIP.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.1
        """
        return self._c_data[0][0]

    @set_id_aip.setter  # set AIP.1
    def set_id_aip(self, si: SI):
        """
        id: AIP.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.1
        """
        self._c_data[0] = (si,)

    @property  # get AIP.2
    def segment_action_code(self) -> SegmentActionCode | None:
        """
        id: AIP.2 | len: 3 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.2
        """
        return self._c_data[1][0]

    @segment_action_code.setter  # set AIP.2
    def segment_action_code(self, segment_action_code: SegmentActionCode | None):
        """
        id: AIP.2 | len: 3 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.2
        """
        self._c_data[1] = (segment_action_code,)

    @property
    def personnel_resource_id(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: AIP.3 | len: 250 | use: C | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.3
        """
        return self._c_data[2]

    @personnel_resource_id.setter  # set AIP.3
    def personnel_resource_id(self, xcn: XCN | tuple[XCN] | None):
        """
        id: AIP.3 | len: 250 | use: C | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.3
        """
        if isinstance(xcn, tuple):
            self._c_data[2] = xcn
        else:
            self._c_data[2] = (xcn,)

    @property  # get AIP.4
    def resource_type(self) -> StaffType | None:
        """
        id: AIP.4 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.4
        """
        return self._c_data[3][0]

    @resource_type.setter  # set AIP.4
    def resource_type(self, staff_type: StaffType | None):
        """
        id: AIP.4 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.4
        """
        self._c_data[3] = (staff_type,)

    @property  # get AIP.5
    def resource_group(self) -> CE | None:
        """
        id: AIP.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.5
        """
        return self._c_data[4][0]

    @resource_group.setter  # set AIP.5
    def resource_group(self, ce: CE | None):
        """
        id: AIP.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.5
        """
        self._c_data[4] = (ce,)

    @property  # get AIP.6
    def start_date_or_time(self) -> TS | None:
        """
        id: AIP.6 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.6
        """
        return self._c_data[5][0]

    @start_date_or_time.setter  # set AIP.6
    def start_date_or_time(self, ts: TS | None):
        """
        id: AIP.6 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.6
        """
        self._c_data[5] = (ts,)

    @property  # get AIP.7
    def start_date_or_time_offset(self) -> NM | None:
        """
        id: AIP.7 | len: 20 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.7
        """
        return self._c_data[6][0]

    @start_date_or_time_offset.setter  # set AIP.7
    def start_date_or_time_offset(self, nm: NM | None):
        """
        id: AIP.7 | len: 20 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.7
        """
        self._c_data[6] = (nm,)

    @property  # get AIP.8
    def start_date_or_time_offset_units(self) -> CE | None:
        """
        id: AIP.8 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.8
        """
        return self._c_data[7][0]

    @start_date_or_time_offset_units.setter  # set AIP.8
    def start_date_or_time_offset_units(self, ce: CE | None):
        """
        id: AIP.8 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.8
        """
        self._c_data[7] = (ce,)

    @property  # get AIP.9
    def duration(self) -> NM | None:
        """
        id: AIP.9 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.9
        """
        return self._c_data[8][0]

    @duration.setter  # set AIP.9
    def duration(self, nm: NM | None):
        """
        id: AIP.9 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.9
        """
        self._c_data[8] = (nm,)

    @property  # get AIP.10
    def duration_units(self) -> CE | None:
        """
        id: AIP.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.10
        """
        return self._c_data[9][0]

    @duration_units.setter  # set AIP.10
    def duration_units(self, ce: CE | None):
        """
        id: AIP.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.10
        """
        self._c_data[9] = (ce,)

    @property  # get AIP.11
    def allow_substitution_code(self) -> AllowSubstitutionCodes | None:
        """
        id: AIP.11 | len: 10 | use: C | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.11
        """
        return self._c_data[10][0]

    @allow_substitution_code.setter  # set AIP.11
    def allow_substitution_code(
        self, allow_substitution_codes: AllowSubstitutionCodes | None
    ):
        """
        id: AIP.11 | len: 10 | use: C | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.11
        """
        self._c_data[10] = (allow_substitution_codes,)

    @property  # get AIP.12
    def filler_status_code(self) -> FillerStatusCodes | None:
        """
        id: AIP.12 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.12
        """
        return self._c_data[11][0]

    @filler_status_code.setter  # set AIP.12
    def filler_status_code(self, filler_status_codes: FillerStatusCodes | None):
        """
        id: AIP.12 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIP.12
        """
        self._c_data[11] = (filler_status_codes,)
