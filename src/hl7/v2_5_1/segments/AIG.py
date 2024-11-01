from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.TS import TS
from ..data_types.IS import IS
from ..data_types.NM import NM
from ..data_types.ID import ID
from ..tables.AllowSubstitutionCodes import AllowSubstitutionCodes
from ..tables.SegmentActionCode import SegmentActionCode
from ..tables.FillerStatusCodes import FillerStatusCodes


"""
Appointment Information - General Resource - AIG
HL7 Version: 2.5.1

-----BEGIN SEGMENT::AIG TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    AIG,
    SI, CE, TS, IS, NM, ID
)

aig = AIG(  #  - The AIG segment contains information about various kinds of resources (other than those with specifically defined segments in this chapter) that can be scheduled
    set_id_aig=si,  # SI(...)  # Required.
    segment_action_code=None,  # ID(...) 
    resource_id=None,  # CE(...) 
    resource_type=ce,  # CE(...)  # Required.
    resource_group=None,  # CE(...) 
    resource_quantity=None,  # NM(...) 
    resource_quantity_units=None,  # CE(...) 
    start_date_or_time=None,  # TS(...) 
    start_date_or_time_offset=None,  # NM(...) 
    start_date_or_time_offset_units=None,  # CE(...) 
    duration=None,  # NM(...) 
    duration_units=None,  # CE(...) 
    allow_substitution_code=None,  # IS(...) 
    filler_status_code=None,  # CE(...) 
)

-----END SEGMENT::AIG TEMPLATE-----
"""


class AIG(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """AIG"""
    _hl7_name = """Appointment Information - General Resource"""
    _hl7_description = """The AIG segment contains information about various kinds of resources (other than those with specifically defined segments in this chapter) that can be scheduled"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIG"
    _c_length = (4, 3, 250, 250, 250, 5, 250, 26, 20, 250, 20, 250, 10, 250,)
    _c_rpt = (1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "C", "C", "R", "O", "O", "O", "C", "C", "C", "O", "O", "C", "C",)
    _c_components = (SI, ID, CE, CE, CE, NM, CE, TS, NM, CE, NM, CE, IS, CE,)
    _c_aliases = ("AIG.1", "AIG.2", "AIG.3", "AIG.4", "AIG.5", "AIG.6", "AIG.7", "AIG.8", "AIG.9", "AIG.10", "AIG.11", "AIG.12", "AIG.13", "AIG.14",)
    _c_names = ("Set ID - AIG", "Segment Action Code", "Resource ID", "Resource Type", "Resource Group", "Resource Quantity", "Resource Quantity Units", "Start Date/Time", "Start Date/Time Offset", "Start Date/Time Offset Units", "Duration", "Duration Units", "Allow Substitution Code", "Filler Status Code",)
    _c_attrs = ("set_id_aig", "segment_action_code", "resource_id", "resource_type", "resource_group", "resource_quantity", "resource_quantity_units", "start_date_or_time", "start_date_or_time_offset", "start_date_or_time_offset_units", "duration", "duration_units", "allow_substitution_code", "filler_status_code",)
    # fmt: on

    def __init__(
        self,
        set_id_aig: SI | tuple[SI, ...],  # AIG.1
        resource_type: CE | tuple[CE, ...],  # AIG.4
        segment_action_code: SegmentActionCode
        | ID
        | tuple[SegmentActionCode | ID, ...]
        | None = None,  # AIG.2
        resource_id: CE | tuple[CE, ...] | None = None,  # AIG.3
        resource_group: CE | tuple[CE, ...] | None = None,  # AIG.5
        resource_quantity: NM | tuple[NM, ...] | None = None,  # AIG.6
        resource_quantity_units: CE | tuple[CE, ...] | None = None,  # AIG.7
        start_date_or_time: TS | tuple[TS, ...] | None = None,  # AIG.8
        start_date_or_time_offset: NM | tuple[NM, ...] | None = None,  # AIG.9
        start_date_or_time_offset_units: CE | tuple[CE, ...] | None = None,  # AIG.10
        duration: NM | tuple[NM, ...] | None = None,  # AIG.11
        duration_units: CE | tuple[CE, ...] | None = None,  # AIG.12
        allow_substitution_code: AllowSubstitutionCodes
        | IS
        | tuple[AllowSubstitutionCodes | IS, ...]
        | None = None,  # AIG.13
        filler_status_code: FillerStatusCodes
        | CE
        | tuple[FillerStatusCodes | CE, ...]
        | None = None,  # AIG.14
    ):
        """
        Appointment Information - General Resource - `AIG <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIG>`_
        The AIG segment contains information about various kinds of resources (other than those with specifically defined segments in this chapter) that can be scheduled. Resources included in a transaction using this segment are assumed to be controlled by a schedule on a schedule filler application. Resources not controlled by a schedule are not identified on a schedule request using this segment. Resources described by this segment are general kinds of resources, such as equipment, that are identified with a simple identification code.

        :param set_id_aig: Sequence ID (id: AIG.1 | len: 4 | use: R | rpt: 1)
        :param segment_action_code: Coded values for HL7 tables (id: AIG.2 | len: 3 | use: C | rpt: 1)
        :param resource_id: Coded Element (id: AIG.3 | len: 250 | use: C | rpt: 1)
        :param resource_type: Coded Element (id: AIG.4 | len: 250 | use: R | rpt: 1)
        :param resource_group: Coded Element (id: AIG.5 | len: 250 | use: O | rpt: *)
        :param resource_quantity: Numeric (id: AIG.6 | len: 5 | use: O | rpt: 1)
        :param resource_quantity_units: Coded Element (id: AIG.7 | len: 250 | use: O | rpt: 1)
        :param start_date_or_time: Time Stamp (id: AIG.8 | len: 26 | use: C | rpt: 1)
        :param start_date_or_time_offset: Numeric (id: AIG.9 | len: 20 | use: C | rpt: 1)
        :param start_date_or_time_offset_units: Coded Element (id: AIG.10 | len: 250 | use: C | rpt: 1)
        :param duration: Numeric (id: AIG.11 | len: 20 | use: O | rpt: 1)
        :param duration_units: Coded Element (id: AIG.12 | len: 250 | use: O | rpt: 1)
        :param allow_substitution_code: Coded value for user-defined tables (id: AIG.13 | len: 10 | use: C | rpt: 1)
        :param filler_status_code: Coded Element (id: AIG.14 | len: 250 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 14
        self.set_id_aig = set_id_aig
        self.segment_action_code = segment_action_code
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.resource_group = resource_group
        self.resource_quantity = resource_quantity
        self.resource_quantity_units = resource_quantity_units
        self.start_date_or_time = start_date_or_time
        self.start_date_or_time_offset = start_date_or_time_offset
        self.start_date_or_time_offset_units = start_date_or_time_offset_units
        self.duration = duration
        self.duration_units = duration_units
        self.allow_substitution_code = allow_substitution_code
        self.filler_status_code = filler_status_code

    @property  # get AIG.1
    def set_id_aig(self) -> SI:
        """
        id: AIG.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.1
        """
        return self._c_data[0][0]

    @set_id_aig.setter  # set AIG.1
    def set_id_aig(self, si: SI):
        """
        id: AIG.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.1
        """
        self._c_data[0] = (si,)

    @property  # get AIG.2
    def segment_action_code(self) -> SegmentActionCode | None:
        """
        id: AIG.2 | len: 3 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.2
        """
        return self._c_data[1][0]

    @segment_action_code.setter  # set AIG.2
    def segment_action_code(self, segment_action_code: SegmentActionCode | None):
        """
        id: AIG.2 | len: 3 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.2
        """
        self._c_data[1] = (segment_action_code,)

    @property  # get AIG.3
    def resource_id(self) -> CE | None:
        """
        id: AIG.3 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.3
        """
        return self._c_data[2][0]

    @resource_id.setter  # set AIG.3
    def resource_id(self, ce: CE | None):
        """
        id: AIG.3 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.3
        """
        self._c_data[2] = (ce,)

    @property  # get AIG.4
    def resource_type(self) -> CE:
        """
        id: AIG.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.4
        """
        return self._c_data[3][0]

    @resource_type.setter  # set AIG.4
    def resource_type(self, ce: CE):
        """
        id: AIG.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.4
        """
        self._c_data[3] = (ce,)

    @property
    def resource_group(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: AIG.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.5
        """
        return self._c_data[4]

    @resource_group.setter  # set AIG.5
    def resource_group(self, ce: CE | tuple[CE] | None):
        """
        id: AIG.5 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.5
        """
        if isinstance(ce, tuple):
            self._c_data[4] = ce
        else:
            self._c_data[4] = (ce,)

    @property  # get AIG.6
    def resource_quantity(self) -> NM | None:
        """
        id: AIG.6 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.6
        """
        return self._c_data[5][0]

    @resource_quantity.setter  # set AIG.6
    def resource_quantity(self, nm: NM | None):
        """
        id: AIG.6 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.6
        """
        self._c_data[5] = (nm,)

    @property  # get AIG.7
    def resource_quantity_units(self) -> CE | None:
        """
        id: AIG.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.7
        """
        return self._c_data[6][0]

    @resource_quantity_units.setter  # set AIG.7
    def resource_quantity_units(self, ce: CE | None):
        """
        id: AIG.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.7
        """
        self._c_data[6] = (ce,)

    @property  # get AIG.8
    def start_date_or_time(self) -> TS | None:
        """
        id: AIG.8 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.8
        """
        return self._c_data[7][0]

    @start_date_or_time.setter  # set AIG.8
    def start_date_or_time(self, ts: TS | None):
        """
        id: AIG.8 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.8
        """
        self._c_data[7] = (ts,)

    @property  # get AIG.9
    def start_date_or_time_offset(self) -> NM | None:
        """
        id: AIG.9 | len: 20 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.9
        """
        return self._c_data[8][0]

    @start_date_or_time_offset.setter  # set AIG.9
    def start_date_or_time_offset(self, nm: NM | None):
        """
        id: AIG.9 | len: 20 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.9
        """
        self._c_data[8] = (nm,)

    @property  # get AIG.10
    def start_date_or_time_offset_units(self) -> CE | None:
        """
        id: AIG.10 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.10
        """
        return self._c_data[9][0]

    @start_date_or_time_offset_units.setter  # set AIG.10
    def start_date_or_time_offset_units(self, ce: CE | None):
        """
        id: AIG.10 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.10
        """
        self._c_data[9] = (ce,)

    @property  # get AIG.11
    def duration(self) -> NM | None:
        """
        id: AIG.11 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.11
        """
        return self._c_data[10][0]

    @duration.setter  # set AIG.11
    def duration(self, nm: NM | None):
        """
        id: AIG.11 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.11
        """
        self._c_data[10] = (nm,)

    @property  # get AIG.12
    def duration_units(self) -> CE | None:
        """
        id: AIG.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.12
        """
        return self._c_data[11][0]

    @duration_units.setter  # set AIG.12
    def duration_units(self, ce: CE | None):
        """
        id: AIG.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.12
        """
        self._c_data[11] = (ce,)

    @property  # get AIG.13
    def allow_substitution_code(self) -> AllowSubstitutionCodes | None:
        """
        id: AIG.13 | len: 10 | use: C | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.13
        """
        return self._c_data[12][0]

    @allow_substitution_code.setter  # set AIG.13
    def allow_substitution_code(
        self, allow_substitution_codes: AllowSubstitutionCodes | None
    ):
        """
        id: AIG.13 | len: 10 | use: C | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.13
        """
        self._c_data[12] = (allow_substitution_codes,)

    @property  # get AIG.14
    def filler_status_code(self) -> FillerStatusCodes | None:
        """
        id: AIG.14 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.14
        """
        return self._c_data[13][0]

    @filler_status_code.setter  # set AIG.14
    def filler_status_code(self, filler_status_codes: FillerStatusCodes | None):
        """
        id: AIG.14 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIG.14
        """
        self._c_data[13] = (filler_status_codes,)
