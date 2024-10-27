from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..data_types.IS import IS
from ..tables.FillerStatusCodes import FillerStatusCodes
from ..tables.SupplementalServiceInformationValues import (
    SupplementalServiceInformationValues,
)
from ..tables.SegmentActionCode import SegmentActionCode
from ..tables.AllowSubstitutionCodes import AllowSubstitutionCodes


"""
Appointment Information - AIS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::AIS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    AIS,
    ID, TS, SI, CE, NM, IS
)

ais = AIS(  #  - The AIS segment contains information about various kinds of services that can be scheduled
    set_id_ais=si,  # SI(...)  # Required.
    segment_action_code=None,  # ID(...) 
    universal_service_identifier=ce,  # CE(...)  # Required.
    start_date_or_time=None,  # TS(...) 
    start_date_or_time_offset=None,  # NM(...) 
    start_date_or_time_offset_units=None,  # CE(...) 
    duration=None,  # NM(...) 
    duration_units=None,  # CE(...) 
    allow_substitution_code=None,  # IS(...) 
    filler_status_code=None,  # CE(...) 
    placer_supplemental_service_information=None,  # CE(...) 
    filler_supplemental_service_information=None,  # CE(...) 
)

-----END SEGMENT::AIS TEMPLATE-----
"""


class AIS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """AIS"""
    _hl7_name = """Appointment Information"""
    _hl7_description = """The AIS segment contains information about various kinds of services that can be scheduled"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIS"
    _c_length = (4, 3, 250, 26, 20, 250, 20, 250, 10, 250, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 65535,)
    _c_usage = ("R", "C", "R", "C", "C", "C", "O", "O", "C", "C", "O", "O",)
    _c_components = (SI, ID, CE, TS, NM, CE, NM, CE, IS, CE, CE, CE,)
    _c_aliases = ("AIS.1", "AIS.2", "AIS.3", "AIS.4", "AIS.5", "AIS.6", "AIS.7", "AIS.8", "AIS.9", "AIS.10", "AIS.11", "AIS.12",)
    _c_names = ("Set ID - AIS", "Segment Action Code", "Universal Service Identifier", "Start Date/Time", "Start Date/Time Offset", "Start Date/Time Offset Units", "Duration", "Duration Units", "Allow Substitution Code", "Filler Status Code", "Placer Supplemental Service Information", "Filler Supplemental Service Information",)
    _c_attrs = ("set_id_ais", "segment_action_code", "universal_service_identifier", "start_date_or_time", "start_date_or_time_offset", "start_date_or_time_offset_units", "duration", "duration_units", "allow_substitution_code", "filler_status_code", "placer_supplemental_service_information", "filler_supplemental_service_information",)
    # fmt: on

    def __init__(
        self,
        set_id_ais: SI,  # AIS.1
        universal_service_identifier: CE,  # AIS.3
        segment_action_code: SegmentActionCode | ID | None = None,  # AIS.2
        start_date_or_time: TS | None = None,  # AIS.4
        start_date_or_time_offset: NM | None = None,  # AIS.5
        start_date_or_time_offset_units: CE | None = None,  # AIS.6
        duration: NM | None = None,  # AIS.7
        duration_units: CE | None = None,  # AIS.8
        allow_substitution_code: AllowSubstitutionCodes | IS | None = None,  # AIS.9
        filler_status_code: FillerStatusCodes | CE | None = None,  # AIS.10
        placer_supplemental_service_information: SupplementalServiceInformationValues
        | CE
        | None = None,  # AIS.11
        filler_supplemental_service_information: SupplementalServiceInformationValues
        | CE
        | None = None,  # AIS.12
    ):
        """
        Appointment Information - `AIS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIS>`_
        The AIS segment contains information about various kinds of services that can be scheduled. Services included in a transaction using this segment are assumed to be controlled by a schedule on a schedule filler application. Services not controlled by a schedule are not identified on a schedule request using this segment.

        :param set_id_ais: Sequence ID (id: AIS.1 | len: 4 | use: R | rpt: 1)
        :param segment_action_code: Coded values for HL7 tables (id: AIS.2 | len: 3 | use: C | rpt: 1)
        :param universal_service_identifier: Coded Element (id: AIS.3 | len: 250 | use: R | rpt: 1)
        :param start_date_or_time: Time Stamp (id: AIS.4 | len: 26 | use: C | rpt: 1)
        :param start_date_or_time_offset: Numeric (id: AIS.5 | len: 20 | use: C | rpt: 1)
        :param start_date_or_time_offset_units: Coded Element (id: AIS.6 | len: 250 | use: C | rpt: 1)
        :param duration: Numeric (id: AIS.7 | len: 20 | use: O | rpt: 1)
        :param duration_units: Coded Element (id: AIS.8 | len: 250 | use: O | rpt: 1)
        :param allow_substitution_code: Coded value for user-defined tables (id: AIS.9 | len: 10 | use: C | rpt: 1)
        :param filler_status_code: Coded Element (id: AIS.10 | len: 250 | use: C | rpt: 1)
        :param placer_supplemental_service_information: Coded Element (id: AIS.11 | len: 250 | use: O | rpt: *)
        :param filler_supplemental_service_information: Coded Element (id: AIS.12 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.set_id_ais = set_id_ais
        self.segment_action_code = segment_action_code
        self.universal_service_identifier = universal_service_identifier
        self.start_date_or_time = start_date_or_time
        self.start_date_or_time_offset = start_date_or_time_offset
        self.start_date_or_time_offset_units = start_date_or_time_offset_units
        self.duration = duration
        self.duration_units = duration_units
        self.allow_substitution_code = allow_substitution_code
        self.filler_status_code = filler_status_code
        self.placer_supplemental_service_information = (
            placer_supplemental_service_information
        )
        self.filler_supplemental_service_information = (
            filler_supplemental_service_information
        )

    @property  # get AIS.1
    def set_id_ais(self) -> SI:
        """
        id: AIS.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.1
        """
        return self._c_data[0][0]

    @set_id_ais.setter  # set AIS.1
    def set_id_ais(self, si: SI):
        """
        id: AIS.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.1
        """
        self._c_data[0] = (si,)

    @property  # get AIS.2
    def segment_action_code(self) -> SegmentActionCode | None:
        """
        id: AIS.2 | len: 3 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.2
        """
        return self._c_data[1][0]

    @segment_action_code.setter  # set AIS.2
    def segment_action_code(self, segment_action_code: SegmentActionCode | None):
        """
        id: AIS.2 | len: 3 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.2
        """
        self._c_data[1] = (segment_action_code,)

    @property  # get AIS.3
    def universal_service_identifier(self) -> CE:
        """
        id: AIS.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.3
        """
        return self._c_data[2][0]

    @universal_service_identifier.setter  # set AIS.3
    def universal_service_identifier(self, ce: CE):
        """
        id: AIS.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.3
        """
        self._c_data[2] = (ce,)

    @property  # get AIS.4
    def start_date_or_time(self) -> TS | None:
        """
        id: AIS.4 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.4
        """
        return self._c_data[3][0]

    @start_date_or_time.setter  # set AIS.4
    def start_date_or_time(self, ts: TS | None):
        """
        id: AIS.4 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.4
        """
        self._c_data[3] = (ts,)

    @property  # get AIS.5
    def start_date_or_time_offset(self) -> NM | None:
        """
        id: AIS.5 | len: 20 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.5
        """
        return self._c_data[4][0]

    @start_date_or_time_offset.setter  # set AIS.5
    def start_date_or_time_offset(self, nm: NM | None):
        """
        id: AIS.5 | len: 20 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.5
        """
        self._c_data[4] = (nm,)

    @property  # get AIS.6
    def start_date_or_time_offset_units(self) -> CE | None:
        """
        id: AIS.6 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.6
        """
        return self._c_data[5][0]

    @start_date_or_time_offset_units.setter  # set AIS.6
    def start_date_or_time_offset_units(self, ce: CE | None):
        """
        id: AIS.6 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.6
        """
        self._c_data[5] = (ce,)

    @property  # get AIS.7
    def duration(self) -> NM | None:
        """
        id: AIS.7 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.7
        """
        return self._c_data[6][0]

    @duration.setter  # set AIS.7
    def duration(self, nm: NM | None):
        """
        id: AIS.7 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.7
        """
        self._c_data[6] = (nm,)

    @property  # get AIS.8
    def duration_units(self) -> CE | None:
        """
        id: AIS.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.8
        """
        return self._c_data[7][0]

    @duration_units.setter  # set AIS.8
    def duration_units(self, ce: CE | None):
        """
        id: AIS.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.8
        """
        self._c_data[7] = (ce,)

    @property  # get AIS.9
    def allow_substitution_code(self) -> AllowSubstitutionCodes | None:
        """
        id: AIS.9 | len: 10 | use: C | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.9
        """
        return self._c_data[8][0]

    @allow_substitution_code.setter  # set AIS.9
    def allow_substitution_code(
        self, allow_substitution_codes: AllowSubstitutionCodes | None
    ):
        """
        id: AIS.9 | len: 10 | use: C | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.9
        """
        self._c_data[8] = (allow_substitution_codes,)

    @property  # get AIS.10
    def filler_status_code(self) -> FillerStatusCodes | None:
        """
        id: AIS.10 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.10
        """
        return self._c_data[9][0]

    @filler_status_code.setter  # set AIS.10
    def filler_status_code(self, filler_status_codes: FillerStatusCodes | None):
        """
        id: AIS.10 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.10
        """
        self._c_data[9] = (filler_status_codes,)

    @property
    def placer_supplemental_service_information(
        self,
    ) -> tuple[SupplementalServiceInformationValues, ...] | tuple[None]:
        """
        id: AIS.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.11
        """
        return self._c_data[10]

    @placer_supplemental_service_information.setter  # set AIS.11
    def placer_supplemental_service_information(
        self,
        supplemental_service_information_values: SupplementalServiceInformationValues
        | tuple[SupplementalServiceInformationValues]
        | None,
    ):
        """
        id: AIS.11 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.11
        """
        if isinstance(supplemental_service_information_values, tuple):
            self._c_data[10] = supplemental_service_information_values
        else:
            self._c_data[10] = (supplemental_service_information_values,)

    @property
    def filler_supplemental_service_information(
        self,
    ) -> tuple[SupplementalServiceInformationValues, ...] | tuple[None]:
        """
        id: AIS.12 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.12
        """
        return self._c_data[11]

    @filler_supplemental_service_information.setter  # set AIS.12
    def filler_supplemental_service_information(
        self,
        supplemental_service_information_values: SupplementalServiceInformationValues
        | tuple[SupplementalServiceInformationValues]
        | None,
    ):
        """
        id: AIS.12 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AIS.12
        """
        if isinstance(supplemental_service_information_values, tuple):
            self._c_data[11] = supplemental_service_information_values
        else:
            self._c_data[11] = (supplemental_service_information_values,)
