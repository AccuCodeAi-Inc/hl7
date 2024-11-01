from __future__ import annotations
from ...base import HL7Segment
from ..data_types.XPN import XPN
from ..data_types.XTN import XTN
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.IS import IS
from ..data_types.CX import CX
from ..data_types.CWE import CWE
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.XAD import XAD
from ..data_types.ST import ST
from ..data_types.HD import HD
from ..data_types.DLN import DLN
from ..tables.SpeciesCode import SpeciesCode
from ..tables.PrimaryLanguage import PrimaryLanguage
from ..tables.BreedCode import BreedCode
from ..tables.IdentityReliabilityCode import IdentityReliabilityCode
from ..tables.Race import Race
from ..tables.Citizenship import Citizenship
from ..tables.AdministrativeSex import AdministrativeSex
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.ProductionClassCode import ProductionClassCode
from ..tables.CountyOrParish import CountyOrParish
from ..tables.Nationality import Nationality
from ..tables.Religion import Religion
from ..tables.VeteransMilitaryStatus import VeteransMilitaryStatus
from ..tables.EthnicGroup import EthnicGroup
from ..tables.MaritalStatus import MaritalStatus


"""
Patient Identification - PID
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PID TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PID,
    XPN, XTN, TS, ID, NM, IS, CX, CWE, SI, CE, XAD, ST, HD, DLN
)

pid = PID(  #  - The PID segment is used by all applications as the primary means of communicating patient identification information
    set_id_pid=None,  # SI(...) 
    patient_id=None,  # CX(...) 
    patient_identifier_list=cx,  # CX(...)  # Required.
    alternate_patient_id_pid=None,  # CX(...) 
    patient_name=xpn,  # XPN(...)  # Required.
    mothers_maiden_name=None,  # XPN(...) 
    date_or_time_of_birth=None,  # TS(...) 
    administrative_sex=None,  # IS(...) 
    patient_alias=None,  # XPN(...) 
    race=None,  # CE(...) 
    patient_address=None,  # XAD(...) 
    county_code=None,  # IS(...) 
    phone_number_home=None,  # XTN(...) 
    phone_number_business=None,  # XTN(...) 
    primary_language=None,  # CE(...) 
    marital_status=None,  # CE(...) 
    religion=None,  # CE(...) 
    patient_account_number=None,  # CX(...) 
    ssn_number_patient=None,  # ST(...) 
    drivers_license_number_patient=None,  # DLN(...) 
    mothers_identifier=None,  # CX(...) 
    ethnic_group=None,  # CE(...) 
    birth_place=None,  # ST(...) 
    multiple_birth_indicator=None,  # ID(...) 
    birth_order=None,  # NM(...) 
    citizenship=None,  # CE(...) 
    veterans_military_status=None,  # CE(...) 
    nationality=None,  # CE(...) 
    patient_death_date_and_time=None,  # TS(...) 
    patient_death_indicator=None,  # ID(...) 
    identity_unknown_indicator=None,  # ID(...) 
    identity_reliability_code=None,  # IS(...) 
    last_update_date_or_time=None,  # TS(...) 
    last_update_facility=None,  # HD(...) 
    species_code=None,  # CE(...) 
    breed_code=None,  # CE(...) 
    strain=None,  # ST(...) 
    production_class_code=None,  # CE(...) 
    tribal_citizenship=None,  # CWE(...) 
)

-----END SEGMENT::PID TEMPLATE-----
"""


class PID(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PID"""
    _hl7_name = """Patient Identification"""
    _hl7_description = """The PID segment is used by all applications as the primary means of communicating patient identification information"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID"
    _c_length = (4, 20, 250, 20, 250, 250, 26, 1, 250, 250, 250, 4, 250, 250, 250, 250, 250, 250, 16, 25, 250, 250, 250, 1, 2, 250, 250, 250, 26, 1, 1, 20, 26, 241, 250, 250, 80, 250, 250,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535, 1, 1, 65535, 65535, 65535, 1, 65535, 65535, 1, 1, 1, 1, 1, 1, 65535, 65535, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 2, 65535,)
    _c_usage = ("O", "B", "R", "B", "R", "O", "O", "O", "B", "O", "O", "B", "O", "O", "O", "O", "O", "O", "B", "B", "O", "O", "O", "O", "O", "O", "O", "B", "O", "O", "O", "O", "O", "O", "C", "C", "O", "O", "O",)
    _c_components = (SI, CX, CX, CX, XPN, XPN, TS, IS, XPN, CE, XAD, IS, XTN, XTN, CE, CE, CE, CX, ST, DLN, CX, CE, ST, ID, NM, CE, CE, CE, TS, ID, ID, IS, TS, HD, CE, CE, ST, CE, CWE,)
    _c_aliases = ("PID.1", "PID.2", "PID.3", "PID.4", "PID.5", "PID.6", "PID.7", "PID.8", "PID.9", "PID.10", "PID.11", "PID.12", "PID.13", "PID.14", "PID.15", "PID.16", "PID.17", "PID.18", "PID.19", "PID.20", "PID.21", "PID.22", "PID.23", "PID.24", "PID.25", "PID.26", "PID.27", "PID.28", "PID.29", "PID.30", "PID.31", "PID.32", "PID.33", "PID.34", "PID.35", "PID.36", "PID.37", "PID.38", "PID.39",)
    _c_names = ("Set ID - PID", "Patient ID", "Patient Identifier List", "Alternate Patient ID - PID", "Patient Name", "Mother's Maiden Name", "Date/Time of Birth", "Administrative Sex", "Patient Alias", "Race", "Patient Address", "County Code", "Phone Number - Home", "Phone Number - Business", "Primary Language", "Marital Status", "Religion", "Patient Account Number", "SSN Number - Patient", "Driver's License Number - Patient", "Mother's Identifier", "Ethnic Group", "Birth Place", "Multiple Birth Indicator", "Birth Order", "Citizenship", "Veterans Military Status", "Nationality", "Patient Death Date and Time", "Patient Death Indicator", "Identity Unknown Indicator", "Identity Reliability Code", "Last Update Date/Time", "Last Update Facility", "Species Code", "Breed Code", "Strain", "Production Class Code", "Tribal Citizenship",)
    _c_attrs = ("set_id_pid", "patient_id", "patient_identifier_list", "alternate_patient_id_pid", "patient_name", "mothers_maiden_name", "date_or_time_of_birth", "administrative_sex", "patient_alias", "race", "patient_address", "county_code", "phone_number_home", "phone_number_business", "primary_language", "marital_status", "religion", "patient_account_number", "ssn_number_patient", "drivers_license_number_patient", "mothers_identifier", "ethnic_group", "birth_place", "multiple_birth_indicator", "birth_order", "citizenship", "veterans_military_status", "nationality", "patient_death_date_and_time", "patient_death_indicator", "identity_unknown_indicator", "identity_reliability_code", "last_update_date_or_time", "last_update_facility", "species_code", "breed_code", "strain", "production_class_code", "tribal_citizenship",)
    # fmt: on

    def __init__(
        self,
        patient_identifier_list: CX | tuple[CX],  # PID.3
        patient_name: XPN | tuple[XPN],  # PID.5
        set_id_pid: SI | tuple[SI] | None = None,  # PID.1
        patient_id: CX | tuple[CX] | None = None,  # PID.2
        alternate_patient_id_pid: CX | tuple[CX] | None = None,  # PID.4
        mothers_maiden_name: XPN | tuple[XPN] | None = None,  # PID.6
        date_or_time_of_birth: TS | tuple[TS] | None = None,  # PID.7
        administrative_sex: AdministrativeSex
        | IS
        | tuple[AdministrativeSex | IS]
        | None = None,  # PID.8
        patient_alias: XPN | tuple[XPN] | None = None,  # PID.9
        race: Race | CE | tuple[Race | CE] | None = None,  # PID.10
        patient_address: XAD | tuple[XAD] | None = None,  # PID.11
        county_code: CountyOrParish
        | IS
        | tuple[CountyOrParish | IS]
        | None = None,  # PID.12
        phone_number_home: XTN | tuple[XTN] | None = None,  # PID.13
        phone_number_business: XTN | tuple[XTN] | None = None,  # PID.14
        primary_language: PrimaryLanguage
        | CE
        | tuple[PrimaryLanguage | CE]
        | None = None,  # PID.15
        marital_status: MaritalStatus
        | CE
        | tuple[MaritalStatus | CE]
        | None = None,  # PID.16
        religion: Religion | CE | tuple[Religion | CE] | None = None,  # PID.17
        patient_account_number: CX | tuple[CX] | None = None,  # PID.18
        ssn_number_patient: ST | tuple[ST] | None = None,  # PID.19
        drivers_license_number_patient: DLN | tuple[DLN] | None = None,  # PID.20
        mothers_identifier: CX | tuple[CX] | None = None,  # PID.21
        ethnic_group: EthnicGroup
        | CE
        | tuple[EthnicGroup | CE]
        | None = None,  # PID.22
        birth_place: ST | tuple[ST] | None = None,  # PID.23
        multiple_birth_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # PID.24
        birth_order: NM | tuple[NM] | None = None,  # PID.25
        citizenship: Citizenship | CE | tuple[Citizenship | CE] | None = None,  # PID.26
        veterans_military_status: VeteransMilitaryStatus
        | CE
        | tuple[VeteransMilitaryStatus | CE]
        | None = None,  # PID.27
        nationality: Nationality | CE | tuple[Nationality | CE] | None = None,  # PID.28
        patient_death_date_and_time: TS | tuple[TS] | None = None,  # PID.29
        patient_death_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # PID.30
        identity_unknown_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # PID.31
        identity_reliability_code: IdentityReliabilityCode
        | IS
        | tuple[IdentityReliabilityCode | IS]
        | None = None,  # PID.32
        last_update_date_or_time: TS | tuple[TS] | None = None,  # PID.33
        last_update_facility: HD | tuple[HD] | None = None,  # PID.34
        species_code: SpeciesCode
        | CE
        | tuple[SpeciesCode | CE]
        | None = None,  # PID.35
        breed_code: BreedCode | CE | tuple[BreedCode | CE] | None = None,  # PID.36
        strain: ST | tuple[ST] | None = None,  # PID.37
        production_class_code: ProductionClassCode
        | CE
        | tuple[ProductionClassCode | CE]
        | None = None,  # PID.38
        tribal_citizenship: Citizenship
        | CWE
        | tuple[Citizenship | CWE]
        | None = None,  # PID.39
    ):
        """
        Patient Identification - `PID <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID>`_
        The PID segment is used by all applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying and demographic information that, for the most part, is not likely to change frequently.

        :param set_id_pid: Sequence ID (id: PID.1 | len: 4 | use: O | rpt: 1)
        :param patient_id: Extended Composite ID with Check Digit (id: PID.2 | len: 20 | use: B | rpt: 1)
        :param patient_identifier_list: Extended Composite ID with Check Digit (id: PID.3 | len: 250 | use: R | rpt: *)
        :param alternate_patient_id_pid: Extended Composite ID with Check Digit (id: PID.4 | len: 20 | use: B | rpt: *)
        :param patient_name: Extended Person Name (id: PID.5 | len: 250 | use: R | rpt: *)
        :param mothers_maiden_name: Extended Person Name (id: PID.6 | len: 250 | use: O | rpt: *)
        :param date_or_time_of_birth: Time Stamp (id: PID.7 | len: 26 | use: O | rpt: 1)
        :param administrative_sex: Coded value for user-defined tables (id: PID.8 | len: 1 | use: O | rpt: 1)
        :param patient_alias: Extended Person Name (id: PID.9 | len: 250 | use: B | rpt: *)
        :param race: Coded Element (id: PID.10 | len: 250 | use: O | rpt: *)
        :param patient_address: Extended Address (id: PID.11 | len: 250 | use: O | rpt: *)
        :param county_code: Coded value for user-defined tables (id: PID.12 | len: 4 | use: B | rpt: 1)
        :param phone_number_home: Extended Telecommunication Number (id: PID.13 | len: 250 | use: O | rpt: *)
        :param phone_number_business: Extended Telecommunication Number (id: PID.14 | len: 250 | use: O | rpt: *)
        :param primary_language: Coded Element (id: PID.15 | len: 250 | use: O | rpt: 1)
        :param marital_status: Coded Element (id: PID.16 | len: 250 | use: O | rpt: 1)
        :param religion: Coded Element (id: PID.17 | len: 250 | use: O | rpt: 1)
        :param patient_account_number: Extended Composite ID with Check Digit (id: PID.18 | len: 250 | use: O | rpt: 1)
        :param ssn_number_patient: String Data (id: PID.19 | len: 16 | use: B | rpt: 1)
        :param drivers_license_number_patient: Driver License Number (id: PID.20 | len: 25 | use: B | rpt: 1)
        :param mothers_identifier: Extended Composite ID with Check Digit (id: PID.21 | len: 250 | use: O | rpt: *)
        :param ethnic_group: Coded Element (id: PID.22 | len: 250 | use: O | rpt: *)
        :param birth_place: String Data (id: PID.23 | len: 250 | use: O | rpt: 1)
        :param multiple_birth_indicator: Coded values for HL7 tables (id: PID.24 | len: 1 | use: O | rpt: 1)
        :param birth_order: Numeric (id: PID.25 | len: 2 | use: O | rpt: 1)
        :param citizenship: Coded Element (id: PID.26 | len: 250 | use: O | rpt: *)
        :param veterans_military_status: Coded Element (id: PID.27 | len: 250 | use: O | rpt: 1)
        :param nationality: Coded Element (id: PID.28 | len: 250 | use: B | rpt: 1)
        :param patient_death_date_and_time: Time Stamp (id: PID.29 | len: 26 | use: O | rpt: 1)
        :param patient_death_indicator: Coded values for HL7 tables (id: PID.30 | len: 1 | use: O | rpt: 1)
        :param identity_unknown_indicator: Coded values for HL7 tables (id: PID.31 | len: 1 | use: O | rpt: 1)
        :param identity_reliability_code: Coded value for user-defined tables (id: PID.32 | len: 20 | use: O | rpt: *)
        :param last_update_date_or_time: Time Stamp (id: PID.33 | len: 26 | use: O | rpt: 1)
        :param last_update_facility: Hierarchic Designator (id: PID.34 | len: 241 | use: O | rpt: 1)
        :param species_code: Coded Element (id: PID.35 | len: 250 | use: C | rpt: 1)
        :param breed_code: Coded Element (id: PID.36 | len: 250 | use: C | rpt: 1)
        :param strain: String Data (id: PID.37 | len: 80 | use: O | rpt: 1)
        :param production_class_code: Coded Element (id: PID.38 | len: 250 | use: O | rpt: 2)
        :param tribal_citizenship: Coded with Exceptions (id: PID.39 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 39
        self.set_id_pid = set_id_pid
        self.patient_id = patient_id
        self.patient_identifier_list = patient_identifier_list
        self.alternate_patient_id_pid = alternate_patient_id_pid
        self.patient_name = patient_name
        self.mothers_maiden_name = mothers_maiden_name
        self.date_or_time_of_birth = date_or_time_of_birth
        self.administrative_sex = administrative_sex
        self.patient_alias = patient_alias
        self.race = race
        self.patient_address = patient_address
        self.county_code = county_code
        self.phone_number_home = phone_number_home
        self.phone_number_business = phone_number_business
        self.primary_language = primary_language
        self.marital_status = marital_status
        self.religion = religion
        self.patient_account_number = patient_account_number
        self.ssn_number_patient = ssn_number_patient
        self.drivers_license_number_patient = drivers_license_number_patient
        self.mothers_identifier = mothers_identifier
        self.ethnic_group = ethnic_group
        self.birth_place = birth_place
        self.multiple_birth_indicator = multiple_birth_indicator
        self.birth_order = birth_order
        self.citizenship = citizenship
        self.veterans_military_status = veterans_military_status
        self.nationality = nationality
        self.patient_death_date_and_time = patient_death_date_and_time
        self.patient_death_indicator = patient_death_indicator
        self.identity_unknown_indicator = identity_unknown_indicator
        self.identity_reliability_code = identity_reliability_code
        self.last_update_date_or_time = last_update_date_or_time
        self.last_update_facility = last_update_facility
        self.species_code = species_code
        self.breed_code = breed_code
        self.strain = strain
        self.production_class_code = production_class_code
        self.tribal_citizenship = tribal_citizenship

    @property  # get PID.1
    def set_id_pid(self) -> SI | None:
        """
        id: PID.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.1
        """
        return self._c_data[0][0]

    @set_id_pid.setter  # set PID.1
    def set_id_pid(self, si: SI | None):
        """
        id: PID.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.1
        """
        self._c_data[0] = (si,)

    @property  # get PID.2
    def patient_id(self) -> CX | None:
        """
        id: PID.2 | len: 20 | use: B | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.2
        """
        return self._c_data[1][0]

    @patient_id.setter  # set PID.2
    def patient_id(self, cx: CX | None):
        """
        id: PID.2 | len: 20 | use: B | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.2
        """
        self._c_data[1] = (cx,)

    @property
    def patient_identifier_list(self) -> tuple[CX, ...]:
        """
        id: PID.3 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.3
        """
        return self._c_data[2]

    @patient_identifier_list.setter  # set PID.3
    def patient_identifier_list(self, cx: CX | tuple[CX]):
        """
        id: PID.3 | len: 250 | use: R | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.3
        """
        if isinstance(cx, tuple):
            self._c_data[2] = cx
        else:
            self._c_data[2] = (cx,)

    @property
    def alternate_patient_id_pid(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: PID.4 | len: 20 | use: B | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.4
        """
        return self._c_data[3]

    @alternate_patient_id_pid.setter  # set PID.4
    def alternate_patient_id_pid(self, cx: CX | tuple[CX] | None):
        """
        id: PID.4 | len: 20 | use: B | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.4
        """
        if isinstance(cx, tuple):
            self._c_data[3] = cx
        else:
            self._c_data[3] = (cx,)

    @property
    def patient_name(self) -> tuple[XPN, ...]:
        """
        id: PID.5 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.5
        """
        return self._c_data[4]

    @patient_name.setter  # set PID.5
    def patient_name(self, xpn: XPN | tuple[XPN]):
        """
        id: PID.5 | len: 250 | use: R | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.5
        """
        if isinstance(xpn, tuple):
            self._c_data[4] = xpn
        else:
            self._c_data[4] = (xpn,)

    @property
    def mothers_maiden_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: PID.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.6
        """
        return self._c_data[5]

    @mothers_maiden_name.setter  # set PID.6
    def mothers_maiden_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: PID.6 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.6
        """
        if isinstance(xpn, tuple):
            self._c_data[5] = xpn
        else:
            self._c_data[5] = (xpn,)

    @property  # get PID.7
    def date_or_time_of_birth(self) -> TS | None:
        """
        id: PID.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.7
        """
        return self._c_data[6][0]

    @date_or_time_of_birth.setter  # set PID.7
    def date_or_time_of_birth(self, ts: TS | None):
        """
        id: PID.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.7
        """
        self._c_data[6] = (ts,)

    @property  # get PID.8
    def administrative_sex(self) -> AdministrativeSex | None:
        """
        id: PID.8 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.8
        """
        return self._c_data[7][0]

    @administrative_sex.setter  # set PID.8
    def administrative_sex(self, administrative_sex: AdministrativeSex | None):
        """
        id: PID.8 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.8
        """
        self._c_data[7] = (administrative_sex,)

    @property
    def patient_alias(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: PID.9 | len: 250 | use: B | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.9
        """
        return self._c_data[8]

    @patient_alias.setter  # set PID.9
    def patient_alias(self, xpn: XPN | tuple[XPN] | None):
        """
        id: PID.9 | len: 250 | use: B | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.9
        """
        if isinstance(xpn, tuple):
            self._c_data[8] = xpn
        else:
            self._c_data[8] = (xpn,)

    @property
    def race(self) -> tuple[Race, ...] | tuple[None]:
        """
        id: PID.10 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.10
        """
        return self._c_data[9]

    @race.setter  # set PID.10
    def race(self, race: Race | tuple[Race] | None):
        """
        id: PID.10 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.10
        """
        if isinstance(race, tuple):
            self._c_data[9] = race
        else:
            self._c_data[9] = (race,)

    @property
    def patient_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: PID.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.11
        """
        return self._c_data[10]

    @patient_address.setter  # set PID.11
    def patient_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: PID.11 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.11
        """
        if isinstance(xad, tuple):
            self._c_data[10] = xad
        else:
            self._c_data[10] = (xad,)

    @property  # get PID.12
    def county_code(self) -> CountyOrParish | None:
        """
        id: PID.12 | len: 4 | use: B | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.12
        """
        return self._c_data[11][0]

    @county_code.setter  # set PID.12
    def county_code(self, county_or_parish: CountyOrParish | None):
        """
        id: PID.12 | len: 4 | use: B | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.12
        """
        self._c_data[11] = (county_or_parish,)

    @property
    def phone_number_home(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: PID.13 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.13
        """
        return self._c_data[12]

    @phone_number_home.setter  # set PID.13
    def phone_number_home(self, xtn: XTN | tuple[XTN] | None):
        """
        id: PID.13 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.13
        """
        if isinstance(xtn, tuple):
            self._c_data[12] = xtn
        else:
            self._c_data[12] = (xtn,)

    @property
    def phone_number_business(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: PID.14 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.14
        """
        return self._c_data[13]

    @phone_number_business.setter  # set PID.14
    def phone_number_business(self, xtn: XTN | tuple[XTN] | None):
        """
        id: PID.14 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.14
        """
        if isinstance(xtn, tuple):
            self._c_data[13] = xtn
        else:
            self._c_data[13] = (xtn,)

    @property  # get PID.15
    def primary_language(self) -> PrimaryLanguage | None:
        """
        id: PID.15 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.15
        """
        return self._c_data[14][0]

    @primary_language.setter  # set PID.15
    def primary_language(self, primary_language: PrimaryLanguage | None):
        """
        id: PID.15 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.15
        """
        self._c_data[14] = (primary_language,)

    @property  # get PID.16
    def marital_status(self) -> MaritalStatus | None:
        """
        id: PID.16 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.16
        """
        return self._c_data[15][0]

    @marital_status.setter  # set PID.16
    def marital_status(self, marital_status: MaritalStatus | None):
        """
        id: PID.16 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.16
        """
        self._c_data[15] = (marital_status,)

    @property  # get PID.17
    def religion(self) -> Religion | None:
        """
        id: PID.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.17
        """
        return self._c_data[16][0]

    @religion.setter  # set PID.17
    def religion(self, religion: Religion | None):
        """
        id: PID.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.17
        """
        self._c_data[16] = (religion,)

    @property  # get PID.18
    def patient_account_number(self) -> CX | None:
        """
        id: PID.18 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.18
        """
        return self._c_data[17][0]

    @patient_account_number.setter  # set PID.18
    def patient_account_number(self, cx: CX | None):
        """
        id: PID.18 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.18
        """
        self._c_data[17] = (cx,)

    @property  # get PID.19
    def ssn_number_patient(self) -> ST | None:
        """
        id: PID.19 | len: 16 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.19
        """
        return self._c_data[18][0]

    @ssn_number_patient.setter  # set PID.19
    def ssn_number_patient(self, st: ST | None):
        """
        id: PID.19 | len: 16 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.19
        """
        self._c_data[18] = (st,)

    @property  # get PID.20
    def drivers_license_number_patient(self) -> DLN | None:
        """
        id: PID.20 | len: 25 | use: B | rpt: 1
        ---
        return_type: DLN: Driver License Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.20
        """
        return self._c_data[19][0]

    @drivers_license_number_patient.setter  # set PID.20
    def drivers_license_number_patient(self, dln: DLN | None):
        """
        id: PID.20 | len: 25 | use: B | rpt: 1
        ---
        param_type: DLN: Driver License Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.20
        """
        self._c_data[19] = (dln,)

    @property
    def mothers_identifier(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: PID.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.21
        """
        return self._c_data[20]

    @mothers_identifier.setter  # set PID.21
    def mothers_identifier(self, cx: CX | tuple[CX] | None):
        """
        id: PID.21 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.21
        """
        if isinstance(cx, tuple):
            self._c_data[20] = cx
        else:
            self._c_data[20] = (cx,)

    @property
    def ethnic_group(self) -> tuple[EthnicGroup, ...] | tuple[None]:
        """
        id: PID.22 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.22
        """
        return self._c_data[21]

    @ethnic_group.setter  # set PID.22
    def ethnic_group(self, ethnic_group: EthnicGroup | tuple[EthnicGroup] | None):
        """
        id: PID.22 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.22
        """
        if isinstance(ethnic_group, tuple):
            self._c_data[21] = ethnic_group
        else:
            self._c_data[21] = (ethnic_group,)

    @property  # get PID.23
    def birth_place(self) -> ST | None:
        """
        id: PID.23 | len: 250 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.23
        """
        return self._c_data[22][0]

    @birth_place.setter  # set PID.23
    def birth_place(self, st: ST | None):
        """
        id: PID.23 | len: 250 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.23
        """
        self._c_data[22] = (st,)

    @property  # get PID.24
    def multiple_birth_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PID.24 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.24
        """
        return self._c_data[23][0]

    @multiple_birth_indicator.setter  # set PID.24
    def multiple_birth_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PID.24 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.24
        """
        self._c_data[23] = (yes_or_no_indicator,)

    @property  # get PID.25
    def birth_order(self) -> NM | None:
        """
        id: PID.25 | len: 2 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.25
        """
        return self._c_data[24][0]

    @birth_order.setter  # set PID.25
    def birth_order(self, nm: NM | None):
        """
        id: PID.25 | len: 2 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.25
        """
        self._c_data[24] = (nm,)

    @property
    def citizenship(self) -> tuple[Citizenship, ...] | tuple[None]:
        """
        id: PID.26 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.26
        """
        return self._c_data[25]

    @citizenship.setter  # set PID.26
    def citizenship(self, citizenship: Citizenship | tuple[Citizenship] | None):
        """
        id: PID.26 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.26
        """
        if isinstance(citizenship, tuple):
            self._c_data[25] = citizenship
        else:
            self._c_data[25] = (citizenship,)

    @property  # get PID.27
    def veterans_military_status(self) -> VeteransMilitaryStatus | None:
        """
        id: PID.27 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.27
        """
        return self._c_data[26][0]

    @veterans_military_status.setter  # set PID.27
    def veterans_military_status(
        self, veterans_military_status: VeteransMilitaryStatus | None
    ):
        """
        id: PID.27 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.27
        """
        self._c_data[26] = (veterans_military_status,)

    @property  # get PID.28
    def nationality(self) -> Nationality | None:
        """
        id: PID.28 | len: 250 | use: B | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.28
        """
        return self._c_data[27][0]

    @nationality.setter  # set PID.28
    def nationality(self, nationality: Nationality | None):
        """
        id: PID.28 | len: 250 | use: B | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.28
        """
        self._c_data[27] = (nationality,)

    @property  # get PID.29
    def patient_death_date_and_time(self) -> TS | None:
        """
        id: PID.29 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.29
        """
        return self._c_data[28][0]

    @patient_death_date_and_time.setter  # set PID.29
    def patient_death_date_and_time(self, ts: TS | None):
        """
        id: PID.29 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.29
        """
        self._c_data[28] = (ts,)

    @property  # get PID.30
    def patient_death_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PID.30 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.30
        """
        return self._c_data[29][0]

    @patient_death_indicator.setter  # set PID.30
    def patient_death_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PID.30 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.30
        """
        self._c_data[29] = (yes_or_no_indicator,)

    @property  # get PID.31
    def identity_unknown_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PID.31 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.31
        """
        return self._c_data[30][0]

    @identity_unknown_indicator.setter  # set PID.31
    def identity_unknown_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PID.31 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.31
        """
        self._c_data[30] = (yes_or_no_indicator,)

    @property
    def identity_reliability_code(
        self,
    ) -> tuple[IdentityReliabilityCode, ...] | tuple[None]:
        """
        id: PID.32 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.32
        """
        return self._c_data[31]

    @identity_reliability_code.setter  # set PID.32
    def identity_reliability_code(
        self,
        identity_reliability_code: IdentityReliabilityCode
        | tuple[IdentityReliabilityCode]
        | None,
    ):
        """
        id: PID.32 | len: 20 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.32
        """
        if isinstance(identity_reliability_code, tuple):
            self._c_data[31] = identity_reliability_code
        else:
            self._c_data[31] = (identity_reliability_code,)

    @property  # get PID.33
    def last_update_date_or_time(self) -> TS | None:
        """
        id: PID.33 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.33
        """
        return self._c_data[32][0]

    @last_update_date_or_time.setter  # set PID.33
    def last_update_date_or_time(self, ts: TS | None):
        """
        id: PID.33 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.33
        """
        self._c_data[32] = (ts,)

    @property  # get PID.34
    def last_update_facility(self) -> HD | None:
        """
        id: PID.34 | len: 241 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.34
        """
        return self._c_data[33][0]

    @last_update_facility.setter  # set PID.34
    def last_update_facility(self, hd: HD | None):
        """
        id: PID.34 | len: 241 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.34
        """
        self._c_data[33] = (hd,)

    @property  # get PID.35
    def species_code(self) -> SpeciesCode | None:
        """
        id: PID.35 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.35
        """
        return self._c_data[34][0]

    @species_code.setter  # set PID.35
    def species_code(self, species_code: SpeciesCode | None):
        """
        id: PID.35 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.35
        """
        self._c_data[34] = (species_code,)

    @property  # get PID.36
    def breed_code(self) -> BreedCode | None:
        """
        id: PID.36 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.36
        """
        return self._c_data[35][0]

    @breed_code.setter  # set PID.36
    def breed_code(self, breed_code: BreedCode | None):
        """
        id: PID.36 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.36
        """
        self._c_data[35] = (breed_code,)

    @property  # get PID.37
    def strain(self) -> ST | None:
        """
        id: PID.37 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.37
        """
        return self._c_data[36][0]

    @strain.setter  # set PID.37
    def strain(self, st: ST | None):
        """
        id: PID.37 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.37
        """
        self._c_data[36] = (st,)

    @property
    def production_class_code(self) -> tuple[ProductionClassCode, ...] | tuple[None]:
        """
        id: PID.38 | len: 250 | use: O | rpt: 2
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.38
        """
        return self._c_data[37]

    @production_class_code.setter  # set PID.38
    def production_class_code(
        self,
        production_class_code: ProductionClassCode | tuple[ProductionClassCode] | None,
    ):
        """
        id: PID.38 | len: 250 | use: O | rpt: 2
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.38
        """
        if isinstance(production_class_code, tuple):
            self._c_data[37] = production_class_code
        else:
            self._c_data[37] = (production_class_code,)

    @property
    def tribal_citizenship(self) -> tuple[Citizenship, ...] | tuple[None]:
        """
        id: PID.39 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.39
        """
        return self._c_data[38]

    @tribal_citizenship.setter  # set PID.39
    def tribal_citizenship(self, citizenship: Citizenship | tuple[Citizenship] | None):
        """
        id: PID.39 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PID.39
        """
        if isinstance(citizenship, tuple):
            self._c_data[38] = citizenship
        else:
            self._c_data[38] = (citizenship,)
