from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.IS import IS
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.SI import SI
from ..data_types.PL import PL
from ..data_types.TS import TS
from ..tables.AllowSubstitutionCodes import AllowSubstitutionCodes
from ..tables.SegmentActionCode import SegmentActionCode
from ..tables.PersonLocationType import PersonLocationType
from ..tables.FillerStatusCodes import FillerStatusCodes


"""
Appointment Information - Location Resource - AIL
HL7 Version: 2.5.1

-----BEGIN SEGMENT::AIL TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    AIL,
    CE, IS, ID, NM, SI, PL, TS
)

ail = AIL(  #  - The AIL segment contains information about location resources (meeting rooms, operating rooms, examination rooms, or other locations) that can be scheduled
    set_id_ail=si,  # SI(...)  # Required.
    segment_action_code=None,  # ID(...) 
    location_resource_id=None,  # PL(...) 
    location_type_ail=None,  # CE(...) 
    location_group=None,  # CE(...) 
    start_date_or_time=None,  # TS(...) 
    start_date_or_time_offset=None,  # NM(...) 
    start_date_or_time_offset_units=None,  # CE(...) 
    duration=None,  # NM(...) 
    duration_units=None,  # CE(...) 
    allow_substitution_code=None,  # IS(...) 
    filler_status_code=None,  # CE(...) 
)

-----END SEGMENT::AIL TEMPLATE-----
"""


class AIL(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """AIL"""
    _hl7_name = """Appointment Information - Location Resource"""
    _hl7_description = """The AIL segment contains information about location resources (meeting rooms, operating rooms, examination rooms, or other locations) that can be scheduled"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIL"
    _c_length = (4, 3, 80, 250, 250, 26, 20, 250, 20, 250, 10, 250,)
    _c_rpt = (1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "C", "C", "C", "O", "C", "C", "C", "O", "O", "C", "C",)
    _c_components = (SI, ID, PL, CE, CE, TS, NM, CE, NM, CE, IS, CE,)
    _c_aliases = ("AIL.1", "AIL.2", "AIL.3", "AIL.4", "AIL.5", "AIL.6", "AIL.7", "AIL.8", "AIL.9", "AIL.10", "AIL.11", "AIL.12",)
    _c_names = ("Set ID - AIL", "Segment Action Code", "Location Resource ID", "Location Type-AIL", "Location Group", "Start Date/Time", "Start Date/Time Offset", "Start Date/Time Offset Units", "Duration", "Duration Units", "Allow Substitution Code", "Filler Status Code",)
    _c_attrs = ("set_id_ail", "segment_action_code", "location_resource_id", "location_type_ail", "location_group", "start_date_or_time", "start_date_or_time_offset", "start_date_or_time_offset_units", "duration", "duration_units", "allow_substitution_code", "filler_status_code",)
    # fmt: on

    def __init__(
        self,
        set_id_ail: SI,  # AIL.1
        segment_action_code: SegmentActionCode | ID | None = None,  # AIL.2
        location_resource_id: PL | None = None,  # AIL.3
        location_type_ail: PersonLocationType | CE | None = None,  # AIL.4
        location_group: CE | None = None,  # AIL.5
        start_date_or_time: TS | None = None,  # AIL.6
        start_date_or_time_offset: NM | None = None,  # AIL.7
        start_date_or_time_offset_units: CE | None = None,  # AIL.8
        duration: NM | None = None,  # AIL.9
        duration_units: CE | None = None,  # AIL.10
        allow_substitution_code: AllowSubstitutionCodes | IS | None = None,  # AIL.11
        filler_status_code: FillerStatusCodes | CE | None = None,  # AIL.12
    ):
        """
        Appointment Information - Location Resource - `AIL <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIL>`_
        The AIL segment contains information about location resources (meeting rooms, operating rooms, examination rooms, or other locations) that can be scheduled. Resources included in a transaction using this segment are assumed to be controlled by a schedule on a schedule filler application. Resources not controlled by a schedule are not identified on a schedule request using this segment. Location resources are identified with this specific segment because of the specific encoding of locations used by the HL7 specification.

        :param set_id_ail: Sequence ID (id: AIL.1 | len: 4 | use: R | rpt: 1)
        :param segment_action_code: Coded values for HL7 tables (id: AIL.2 | len: 3 | use: C | rpt: 1)
        :param location_resource_id: Person Location (id: AIL.3 | len: 80 | use: C | rpt: *)
        :param location_type_ail: Coded Element (id: AIL.4 | len: 250 | use: C | rpt: 1)
        :param location_group: Coded Element (id: AIL.5 | len: 250 | use: O | rpt: 1)
        :param start_date_or_time: Time Stamp (id: AIL.6 | len: 26 | use: C | rpt: 1)
        :param start_date_or_time_offset: Numeric (id: AIL.7 | len: 20 | use: C | rpt: 1)
        :param start_date_or_time_offset_units: Coded Element (id: AIL.8 | len: 250 | use: C | rpt: 1)
        :param duration: Numeric (id: AIL.9 | len: 20 | use: O | rpt: 1)
        :param duration_units: Coded Element (id: AIL.10 | len: 250 | use: O | rpt: 1)
        :param allow_substitution_code: Coded value for user-defined tables (id: AIL.11 | len: 10 | use: C | rpt: 1)
        :param filler_status_code: Coded Element (id: AIL.12 | len: 250 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.set_id_ail = set_id_ail
        self.segment_action_code = segment_action_code
        self.location_resource_id = location_resource_id
        self.location_type_ail = location_type_ail
        self.location_group = location_group
        self.start_date_or_time = start_date_or_time
        self.start_date_or_time_offset = start_date_or_time_offset
        self.start_date_or_time_offset_units = start_date_or_time_offset_units
        self.duration = duration
        self.duration_units = duration_units
        self.allow_substitution_code = allow_substitution_code
        self.filler_status_code = filler_status_code

    @property  # get AIL.1
    def set_id_ail(self) -> SI:
        """
        id: AIL.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.1
        """
        return self._c_data[0][0]

    @set_id_ail.setter  # set AIL.1
    def set_id_ail(self, si: SI):
        """
        id: AIL.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.1
        """
        self._c_data[0] = (si,)

    @property  # get AIL.2
    def segment_action_code(self) -> SegmentActionCode | None:
        """
        id: AIL.2 | len: 3 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.2
        """
        return self._c_data[1][0]

    @segment_action_code.setter  # set AIL.2
    def segment_action_code(self, segment_action_code: SegmentActionCode | None):
        """
        id: AIL.2 | len: 3 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.2
        """
        self._c_data[1] = (segment_action_code,)

    @property
    def location_resource_id(self) -> tuple[PL, ...] | tuple[None]:
        """
        id: AIL.3 | len: 80 | use: C | rpt: *
        ---
        return_type: tuple[PL, ...]: (Person Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.3
        """
        return self._c_data[2]

    @location_resource_id.setter  # set AIL.3
    def location_resource_id(self, pl: PL | tuple[PL] | None):
        """
        id: AIL.3 | len: 80 | use: C | rpt: *
        ---
        param_type: PL | tuple[PL, ...]: (Person Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.3
        """
        if isinstance(pl, tuple):
            self._c_data[2] = pl
        else:
            self._c_data[2] = (pl,)

    @property  # get AIL.4
    def location_type_ail(self) -> PersonLocationType | None:
        """
        id: AIL.4 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.4
        """
        return self._c_data[3][0]

    @location_type_ail.setter  # set AIL.4
    def location_type_ail(self, person_location_type: PersonLocationType | None):
        """
        id: AIL.4 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.4
        """
        self._c_data[3] = (person_location_type,)

    @property  # get AIL.5
    def location_group(self) -> CE | None:
        """
        id: AIL.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.5
        """
        return self._c_data[4][0]

    @location_group.setter  # set AIL.5
    def location_group(self, ce: CE | None):
        """
        id: AIL.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.5
        """
        self._c_data[4] = (ce,)

    @property  # get AIL.6
    def start_date_or_time(self) -> TS | None:
        """
        id: AIL.6 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.6
        """
        return self._c_data[5][0]

    @start_date_or_time.setter  # set AIL.6
    def start_date_or_time(self, ts: TS | None):
        """
        id: AIL.6 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.6
        """
        self._c_data[5] = (ts,)

    @property  # get AIL.7
    def start_date_or_time_offset(self) -> NM | None:
        """
        id: AIL.7 | len: 20 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.7
        """
        return self._c_data[6][0]

    @start_date_or_time_offset.setter  # set AIL.7
    def start_date_or_time_offset(self, nm: NM | None):
        """
        id: AIL.7 | len: 20 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.7
        """
        self._c_data[6] = (nm,)

    @property  # get AIL.8
    def start_date_or_time_offset_units(self) -> CE | None:
        """
        id: AIL.8 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.8
        """
        return self._c_data[7][0]

    @start_date_or_time_offset_units.setter  # set AIL.8
    def start_date_or_time_offset_units(self, ce: CE | None):
        """
        id: AIL.8 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.8
        """
        self._c_data[7] = (ce,)

    @property  # get AIL.9
    def duration(self) -> NM | None:
        """
        id: AIL.9 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.9
        """
        return self._c_data[8][0]

    @duration.setter  # set AIL.9
    def duration(self, nm: NM | None):
        """
        id: AIL.9 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.9
        """
        self._c_data[8] = (nm,)

    @property  # get AIL.10
    def duration_units(self) -> CE | None:
        """
        id: AIL.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.10
        """
        return self._c_data[9][0]

    @duration_units.setter  # set AIL.10
    def duration_units(self, ce: CE | None):
        """
        id: AIL.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.10
        """
        self._c_data[9] = (ce,)

    @property  # get AIL.11
    def allow_substitution_code(self) -> AllowSubstitutionCodes | None:
        """
        id: AIL.11 | len: 10 | use: C | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.11
        """
        return self._c_data[10][0]

    @allow_substitution_code.setter  # set AIL.11
    def allow_substitution_code(
        self, allow_substitution_codes: AllowSubstitutionCodes | None
    ):
        """
        id: AIL.11 | len: 10 | use: C | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.11
        """
        self._c_data[10] = (allow_substitution_codes,)

    @property  # get AIL.12
    def filler_status_code(self) -> FillerStatusCodes | None:
        """
        id: AIL.12 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.12
        """
        return self._c_data[11][0]

    @filler_status_code.setter  # set AIL.12
    def filler_status_code(self, filler_status_codes: FillerStatusCodes | None):
        """
        id: AIL.12 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIL.12
        """
        self._c_data[11] = (filler_status_codes,)
