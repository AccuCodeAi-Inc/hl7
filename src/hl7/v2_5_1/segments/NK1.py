from __future__ import annotations
from ...base import HL7Segment
from ..data_types.JCC import JCC
from ..data_types.XPN import XPN
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.DT import DT
from ..data_types.CX import CX
from ..data_types.IS import IS
from ..data_types.SI import SI
from ..data_types.XTN import XTN
from ..data_types.XAD import XAD
from ..data_types.CE import CE
from ..data_types.ST import ST
from ..data_types.XON import XON
from ..tables.JobStatus import JobStatus
from ..tables.StudentStatus import StudentStatus
from ..tables.LivingArrangement import LivingArrangement
from ..tables.Race import Race
from ..tables.VipIndicator import VipIndicator
from ..tables.LivingDependency import LivingDependency
from ..tables.ContactReason import ContactReason
from ..tables.Handicap import Handicap
from ..tables.PrimaryLanguage import PrimaryLanguage
from ..tables.AmbulatoryStatus import AmbulatoryStatus
from ..tables.ContactRole import ContactRole
from ..tables.Religion import Religion
from ..tables.Relationship import Relationship
from ..tables.Citizenship import Citizenship
from ..tables.AdministrativeSex import AdministrativeSex
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.PublicityCode import PublicityCode
from ..tables.Nationality import Nationality
from ..tables.EthnicGroup import EthnicGroup
from ..tables.MaritalStatus import MaritalStatus


"""
Next of Kin / Associated Parties - NK1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::NK1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    NK1,
    JCC, XPN, TS, ID, DT, CX, IS, SI, XTN, XAD, CE, ST, XON
)

nk1 = NK1(  #  - The NK1 segment contains information about the patients other related parties
    set_id_nk1=si,  # SI(...)  # Required.
    nk_name=None,  # XPN(...) 
    relationship=None,  # CE(...) 
    address=None,  # XAD(...) 
    phone_number=None,  # XTN(...) 
    business_phone_number=None,  # XTN(...) 
    contact_role=None,  # CE(...) 
    start_date=None,  # DT(...) 
    end_date=None,  # DT(...) 
    next_of_kin_or_associated_parties_job_title=None,  # ST(...) 
    next_of_kin_or_associated_parties_job_code_or_class=None,  # JCC(...) 
    next_of_kin_or_associated_parties_employee_number=None,  # CX(...) 
    organization_name_nk1=None,  # XON(...) 
    marital_status=None,  # CE(...) 
    administrative_sex=None,  # IS(...) 
    date_or_time_of_birth=None,  # TS(...) 
    living_dependency=None,  # IS(...) 
    ambulatory_status=None,  # IS(...) 
    citizenship=None,  # CE(...) 
    primary_language=None,  # CE(...) 
    living_arrangement=None,  # IS(...) 
    publicity_code=None,  # CE(...) 
    protection_indicator=None,  # ID(...) 
    student_indicator=None,  # IS(...) 
    religion=None,  # CE(...) 
    mothers_maiden_name=None,  # XPN(...) 
    nationality=None,  # CE(...) 
    ethnic_group=None,  # CE(...) 
    contact_reason=None,  # CE(...) 
    contact_persons_name=None,  # XPN(...) 
    contact_persons_telephone_number=None,  # XTN(...) 
    contact_persons_address=None,  # XAD(...) 
    next_of_kin_or_associated_partys_identifiers=None,  # CX(...) 
    job_status=None,  # IS(...) 
    race=None,  # CE(...) 
    handicap=None,  # IS(...) 
    contact_person_social_security_number=None,  # ST(...) 
    next_of_kin_birth_place=None,  # ST(...) 
    vip_indicator=None,  # IS(...) 
)

-----END SEGMENT::NK1 TEMPLATE-----
"""


class NK1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """NK1"""
    _hl7_name = """Next of Kin / Associated Parties"""
    _hl7_description = """The NK1 segment contains information about the patients other related parties"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1"
    _c_length = (4, 250, 250, 250, 250, 250, 250, 8, 8, 60, 20, 250, 250, 250, 1, 26, 2, 2, 250, 250, 2, 250, 1, 2, 250, 250, 250, 250, 250, 250, 250, 250, 250, 2, 250, 2, 16, 250, 2,)
    _c_rpt = (1, 65535, 1, 65535, 65535, 65535, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 65535, 65535, 65535, 1, 1, 1, 1, 1, 1, 65535, 1, 65535, 65535, 65535, 65535, 65535, 65535, 1, 65535, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, XPN, CE, XAD, XTN, XTN, CE, DT, DT, ST, JCC, CX, XON, CE, IS, TS, IS, IS, CE, CE, IS, CE, ID, IS, CE, XPN, CE, CE, CE, XPN, XTN, XAD, CX, IS, CE, IS, ST, ST, IS,)
    _c_aliases = ("NK1.1", "NK1.2", "NK1.3", "NK1.4", "NK1.5", "NK1.6", "NK1.7", "NK1.8", "NK1.9", "NK1.10", "NK1.11", "NK1.12", "NK1.13", "NK1.14", "NK1.15", "NK1.16", "NK1.17", "NK1.18", "NK1.19", "NK1.20", "NK1.21", "NK1.22", "NK1.23", "NK1.24", "NK1.25", "NK1.26", "NK1.27", "NK1.28", "NK1.29", "NK1.30", "NK1.31", "NK1.32", "NK1.33", "NK1.34", "NK1.35", "NK1.36", "NK1.37", "NK1.38", "NK1.39",)
    _c_names = ("Set ID - NK1", "NK Name", "Relationship", "Address", "Phone Number", "Business Phone Number", "Contact Role", "Start Date", "End Date", "Next of Kin / Associated Parties Job Title", "Next of Kin / Associated Parties Job Code/Class", "Next of Kin / Associated Parties Employee Number", "Organization Name - NK1", "Marital Status", "Administrative Sex", "Date/Time of Birth", "Living Dependency", "Ambulatory Status", "Citizenship", "Primary Language", "Living Arrangement", "Publicity Code", "Protection Indicator", "Student Indicator", "Religion", "Mother's Maiden Name", "Nationality", "Ethnic Group", "Contact Reason", "Contact Person's Name", "Contact Person's Telephone Number", "Contact Person's Address", "Next of Kin/Associated Party's Identifiers", "Job Status", "Race", "Handicap", "Contact Person Social Security Number", "Next of Kin Birth Place", "VIP Indicator",)
    _c_attrs = ("set_id_nk1", "nk_name", "relationship", "address", "phone_number", "business_phone_number", "contact_role", "start_date", "end_date", "next_of_kin_or_associated_parties_job_title", "next_of_kin_or_associated_parties_job_code_or_class", "next_of_kin_or_associated_parties_employee_number", "organization_name_nk1", "marital_status", "administrative_sex", "date_or_time_of_birth", "living_dependency", "ambulatory_status", "citizenship", "primary_language", "living_arrangement", "publicity_code", "protection_indicator", "student_indicator", "religion", "mothers_maiden_name", "nationality", "ethnic_group", "contact_reason", "contact_persons_name", "contact_persons_telephone_number", "contact_persons_address", "next_of_kin_or_associated_partys_identifiers", "job_status", "race", "handicap", "contact_person_social_security_number", "next_of_kin_birth_place", "vip_indicator",)
    # fmt: on

    def __init__(
        self,
        set_id_nk1: SI | tuple[SI],  # NK1.1
        nk_name: XPN | tuple[XPN] | None = None,  # NK1.2
        relationship: Relationship
        | CE
        | tuple[Relationship | CE]
        | None = None,  # NK1.3
        address: XAD | tuple[XAD] | None = None,  # NK1.4
        phone_number: XTN | tuple[XTN] | None = None,  # NK1.5
        business_phone_number: XTN | tuple[XTN] | None = None,  # NK1.6
        contact_role: ContactRole | CE | tuple[ContactRole | CE] | None = None,  # NK1.7
        start_date: DT | tuple[DT] | None = None,  # NK1.8
        end_date: DT | tuple[DT] | None = None,  # NK1.9
        next_of_kin_or_associated_parties_job_title: ST
        | tuple[ST]
        | None = None,  # NK1.10
        next_of_kin_or_associated_parties_job_code_or_class: JCC
        | tuple[JCC]
        | None = None,  # NK1.11
        next_of_kin_or_associated_parties_employee_number: CX
        | tuple[CX]
        | None = None,  # NK1.12
        organization_name_nk1: XON | tuple[XON] | None = None,  # NK1.13
        marital_status: MaritalStatus
        | CE
        | tuple[MaritalStatus | CE]
        | None = None,  # NK1.14
        administrative_sex: AdministrativeSex
        | IS
        | tuple[AdministrativeSex | IS]
        | None = None,  # NK1.15
        date_or_time_of_birth: TS | tuple[TS] | None = None,  # NK1.16
        living_dependency: LivingDependency
        | IS
        | tuple[LivingDependency | IS]
        | None = None,  # NK1.17
        ambulatory_status: AmbulatoryStatus
        | IS
        | tuple[AmbulatoryStatus | IS]
        | None = None,  # NK1.18
        citizenship: Citizenship | CE | tuple[Citizenship | CE] | None = None,  # NK1.19
        primary_language: PrimaryLanguage
        | CE
        | tuple[PrimaryLanguage | CE]
        | None = None,  # NK1.20
        living_arrangement: LivingArrangement
        | IS
        | tuple[LivingArrangement | IS]
        | None = None,  # NK1.21
        publicity_code: PublicityCode
        | CE
        | tuple[PublicityCode | CE]
        | None = None,  # NK1.22
        protection_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # NK1.23
        student_indicator: StudentStatus
        | IS
        | tuple[StudentStatus | IS]
        | None = None,  # NK1.24
        religion: Religion | CE | tuple[Religion | CE] | None = None,  # NK1.25
        mothers_maiden_name: XPN | tuple[XPN] | None = None,  # NK1.26
        nationality: Nationality | CE | tuple[Nationality | CE] | None = None,  # NK1.27
        ethnic_group: EthnicGroup
        | CE
        | tuple[EthnicGroup | CE]
        | None = None,  # NK1.28
        contact_reason: ContactReason
        | CE
        | tuple[ContactReason | CE]
        | None = None,  # NK1.29
        contact_persons_name: XPN | tuple[XPN] | None = None,  # NK1.30
        contact_persons_telephone_number: XTN | tuple[XTN] | None = None,  # NK1.31
        contact_persons_address: XAD | tuple[XAD] | None = None,  # NK1.32
        next_of_kin_or_associated_partys_identifiers: CX
        | tuple[CX]
        | None = None,  # NK1.33
        job_status: JobStatus | IS | tuple[JobStatus | IS] | None = None,  # NK1.34
        race: Race | CE | tuple[Race | CE] | None = None,  # NK1.35
        handicap: Handicap | IS | tuple[Handicap | IS] | None = None,  # NK1.36
        contact_person_social_security_number: ST | tuple[ST] | None = None,  # NK1.37
        next_of_kin_birth_place: ST | tuple[ST] | None = None,  # NK1.38
        vip_indicator: VipIndicator
        | IS
        | tuple[VipIndicator | IS]
        | None = None,  # NK1.39
    ):
        """
        Next of Kin / Associated Parties - `NK1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1>`_
        The NK1 segment contains information about the patients other related parties. Any associated parties may be identified. Utilizing NK1-1 - set ID, multiple NK1 segments can be sent to patient accounts.

        :param set_id_nk1: Sequence ID (id: NK1.1 | len: 4 | use: R | rpt: 1)
        :param nk_name: Extended Person Name (id: NK1.2 | len: 250 | use: O | rpt: *)
        :param relationship: Coded Element (id: NK1.3 | len: 250 | use: O | rpt: 1)
        :param address: Extended Address (id: NK1.4 | len: 250 | use: O | rpt: *)
        :param phone_number: Extended Telecommunication Number (id: NK1.5 | len: 250 | use: O | rpt: *)
        :param business_phone_number: Extended Telecommunication Number (id: NK1.6 | len: 250 | use: O | rpt: *)
        :param contact_role: Coded Element (id: NK1.7 | len: 250 | use: O | rpt: 1)
        :param start_date: Date (id: NK1.8 | len: 8 | use: O | rpt: 1)
        :param end_date: Date (id: NK1.9 | len: 8 | use: O | rpt: 1)
        :param next_of_kin_or_associated_parties_job_title: String Data (id: NK1.10 | len: 60 | use: O | rpt: 1)
        :param next_of_kin_or_associated_parties_job_code_or_class: Job Code/Class (id: NK1.11 | len: 20 | use: O | rpt: 1)
        :param next_of_kin_or_associated_parties_employee_number: Extended Composite ID with Check Digit (id: NK1.12 | len: 250 | use: O | rpt: 1)
        :param organization_name_nk1: Extended Composite Name and Identification Number for Organizations (id: NK1.13 | len: 250 | use: O | rpt: *)
        :param marital_status: Coded Element (id: NK1.14 | len: 250 | use: O | rpt: 1)
        :param administrative_sex: Coded value for user-defined tables (id: NK1.15 | len: 1 | use: O | rpt: 1)
        :param date_or_time_of_birth: Time Stamp (id: NK1.16 | len: 26 | use: O | rpt: 1)
        :param living_dependency: Coded value for user-defined tables (id: NK1.17 | len: 2 | use: O | rpt: *)
        :param ambulatory_status: Coded value for user-defined tables (id: NK1.18 | len: 2 | use: O | rpt: *)
        :param citizenship: Coded Element (id: NK1.19 | len: 250 | use: O | rpt: *)
        :param primary_language: Coded Element (id: NK1.20 | len: 250 | use: O | rpt: 1)
        :param living_arrangement: Coded value for user-defined tables (id: NK1.21 | len: 2 | use: O | rpt: 1)
        :param publicity_code: Coded Element (id: NK1.22 | len: 250 | use: O | rpt: 1)
        :param protection_indicator: Coded values for HL7 tables (id: NK1.23 | len: 1 | use: O | rpt: 1)
        :param student_indicator: Coded value for user-defined tables (id: NK1.24 | len: 2 | use: O | rpt: 1)
        :param religion: Coded Element (id: NK1.25 | len: 250 | use: O | rpt: 1)
        :param mothers_maiden_name: Extended Person Name (id: NK1.26 | len: 250 | use: O | rpt: *)
        :param nationality: Coded Element (id: NK1.27 | len: 250 | use: O | rpt: 1)
        :param ethnic_group: Coded Element (id: NK1.28 | len: 250 | use: O | rpt: *)
        :param contact_reason: Coded Element (id: NK1.29 | len: 250 | use: O | rpt: *)
        :param contact_persons_name: Extended Person Name (id: NK1.30 | len: 250 | use: O | rpt: *)
        :param contact_persons_telephone_number: Extended Telecommunication Number (id: NK1.31 | len: 250 | use: O | rpt: *)
        :param contact_persons_address: Extended Address (id: NK1.32 | len: 250 | use: O | rpt: *)
        :param next_of_kin_or_associated_partys_identifiers: Extended Composite ID with Check Digit (id: NK1.33 | len: 250 | use: O | rpt: *)
        :param job_status: Coded value for user-defined tables (id: NK1.34 | len: 2 | use: O | rpt: 1)
        :param race: Coded Element (id: NK1.35 | len: 250 | use: O | rpt: *)
        :param handicap: Coded value for user-defined tables (id: NK1.36 | len: 2 | use: O | rpt: 1)
        :param contact_person_social_security_number: String Data (id: NK1.37 | len: 16 | use: O | rpt: 1)
        :param next_of_kin_birth_place: String Data (id: NK1.38 | len: 250 | use: O | rpt: 1)
        :param vip_indicator: Coded value for user-defined tables (id: NK1.39 | len: 2 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 39
        self.set_id_nk1 = set_id_nk1
        self.nk_name = nk_name
        self.relationship = relationship
        self.address = address
        self.phone_number = phone_number
        self.business_phone_number = business_phone_number
        self.contact_role = contact_role
        self.start_date = start_date
        self.end_date = end_date
        self.next_of_kin_or_associated_parties_job_title = (
            next_of_kin_or_associated_parties_job_title
        )
        self.next_of_kin_or_associated_parties_job_code_or_class = (
            next_of_kin_or_associated_parties_job_code_or_class
        )
        self.next_of_kin_or_associated_parties_employee_number = (
            next_of_kin_or_associated_parties_employee_number
        )
        self.organization_name_nk1 = organization_name_nk1
        self.marital_status = marital_status
        self.administrative_sex = administrative_sex
        self.date_or_time_of_birth = date_or_time_of_birth
        self.living_dependency = living_dependency
        self.ambulatory_status = ambulatory_status
        self.citizenship = citizenship
        self.primary_language = primary_language
        self.living_arrangement = living_arrangement
        self.publicity_code = publicity_code
        self.protection_indicator = protection_indicator
        self.student_indicator = student_indicator
        self.religion = religion
        self.mothers_maiden_name = mothers_maiden_name
        self.nationality = nationality
        self.ethnic_group = ethnic_group
        self.contact_reason = contact_reason
        self.contact_persons_name = contact_persons_name
        self.contact_persons_telephone_number = contact_persons_telephone_number
        self.contact_persons_address = contact_persons_address
        self.next_of_kin_or_associated_partys_identifiers = (
            next_of_kin_or_associated_partys_identifiers
        )
        self.job_status = job_status
        self.race = race
        self.handicap = handicap
        self.contact_person_social_security_number = (
            contact_person_social_security_number
        )
        self.next_of_kin_birth_place = next_of_kin_birth_place
        self.vip_indicator = vip_indicator

    @property  # get NK1.1
    def set_id_nk1(self) -> SI:
        """
        id: NK1.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.1
        """
        return self._c_data[0][0]

    @set_id_nk1.setter  # set NK1.1
    def set_id_nk1(self, si: SI):
        """
        id: NK1.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.1
        """
        self._c_data[0] = (si,)

    @property
    def nk_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: NK1.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.2
        """
        return self._c_data[1]

    @nk_name.setter  # set NK1.2
    def nk_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: NK1.2 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.2
        """
        if isinstance(xpn, tuple):
            self._c_data[1] = xpn
        else:
            self._c_data[1] = (xpn,)

    @property  # get NK1.3
    def relationship(self) -> Relationship | None:
        """
        id: NK1.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.3
        """
        return self._c_data[2][0]

    @relationship.setter  # set NK1.3
    def relationship(self, relationship: Relationship | None):
        """
        id: NK1.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.3
        """
        self._c_data[2] = (relationship,)

    @property
    def address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: NK1.4 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.4
        """
        return self._c_data[3]

    @address.setter  # set NK1.4
    def address(self, xad: XAD | tuple[XAD] | None):
        """
        id: NK1.4 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.4
        """
        if isinstance(xad, tuple):
            self._c_data[3] = xad
        else:
            self._c_data[3] = (xad,)

    @property
    def phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: NK1.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.5
        """
        return self._c_data[4]

    @phone_number.setter  # set NK1.5
    def phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: NK1.5 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.5
        """
        if isinstance(xtn, tuple):
            self._c_data[4] = xtn
        else:
            self._c_data[4] = (xtn,)

    @property
    def business_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: NK1.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.6
        """
        return self._c_data[5]

    @business_phone_number.setter  # set NK1.6
    def business_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: NK1.6 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.6
        """
        if isinstance(xtn, tuple):
            self._c_data[5] = xtn
        else:
            self._c_data[5] = (xtn,)

    @property  # get NK1.7
    def contact_role(self) -> ContactRole | None:
        """
        id: NK1.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.7
        """
        return self._c_data[6][0]

    @contact_role.setter  # set NK1.7
    def contact_role(self, contact_role: ContactRole | None):
        """
        id: NK1.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.7
        """
        self._c_data[6] = (contact_role,)

    @property  # get NK1.8
    def start_date(self) -> DT | None:
        """
        id: NK1.8 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.8
        """
        return self._c_data[7][0]

    @start_date.setter  # set NK1.8
    def start_date(self, dt: DT | None):
        """
        id: NK1.8 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.8
        """
        self._c_data[7] = (dt,)

    @property  # get NK1.9
    def end_date(self) -> DT | None:
        """
        id: NK1.9 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.9
        """
        return self._c_data[8][0]

    @end_date.setter  # set NK1.9
    def end_date(self, dt: DT | None):
        """
        id: NK1.9 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.9
        """
        self._c_data[8] = (dt,)

    @property  # get NK1.10
    def next_of_kin_or_associated_parties_job_title(self) -> ST | None:
        """
        id: NK1.10 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.10
        """
        return self._c_data[9][0]

    @next_of_kin_or_associated_parties_job_title.setter  # set NK1.10
    def next_of_kin_or_associated_parties_job_title(self, st: ST | None):
        """
        id: NK1.10 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.10
        """
        self._c_data[9] = (st,)

    @property  # get NK1.11
    def next_of_kin_or_associated_parties_job_code_or_class(self) -> JCC | None:
        """
        id: NK1.11 | len: 20 | use: O | rpt: 1
        ---
        return_type: JCC: Job Code/Class
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.11
        """
        return self._c_data[10][0]

    @next_of_kin_or_associated_parties_job_code_or_class.setter  # set NK1.11
    def next_of_kin_or_associated_parties_job_code_or_class(self, jcc: JCC | None):
        """
        id: NK1.11 | len: 20 | use: O | rpt: 1
        ---
        param_type: JCC: Job Code/Class
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.11
        """
        self._c_data[10] = (jcc,)

    @property  # get NK1.12
    def next_of_kin_or_associated_parties_employee_number(self) -> CX | None:
        """
        id: NK1.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.12
        """
        return self._c_data[11][0]

    @next_of_kin_or_associated_parties_employee_number.setter  # set NK1.12
    def next_of_kin_or_associated_parties_employee_number(self, cx: CX | None):
        """
        id: NK1.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.12
        """
        self._c_data[11] = (cx,)

    @property
    def organization_name_nk1(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: NK1.13 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.13
        """
        return self._c_data[12]

    @organization_name_nk1.setter  # set NK1.13
    def organization_name_nk1(self, xon: XON | tuple[XON] | None):
        """
        id: NK1.13 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.13
        """
        if isinstance(xon, tuple):
            self._c_data[12] = xon
        else:
            self._c_data[12] = (xon,)

    @property  # get NK1.14
    def marital_status(self) -> MaritalStatus | None:
        """
        id: NK1.14 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.14
        """
        return self._c_data[13][0]

    @marital_status.setter  # set NK1.14
    def marital_status(self, marital_status: MaritalStatus | None):
        """
        id: NK1.14 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.14
        """
        self._c_data[13] = (marital_status,)

    @property  # get NK1.15
    def administrative_sex(self) -> AdministrativeSex | None:
        """
        id: NK1.15 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.15
        """
        return self._c_data[14][0]

    @administrative_sex.setter  # set NK1.15
    def administrative_sex(self, administrative_sex: AdministrativeSex | None):
        """
        id: NK1.15 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.15
        """
        self._c_data[14] = (administrative_sex,)

    @property  # get NK1.16
    def date_or_time_of_birth(self) -> TS | None:
        """
        id: NK1.16 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.16
        """
        return self._c_data[15][0]

    @date_or_time_of_birth.setter  # set NK1.16
    def date_or_time_of_birth(self, ts: TS | None):
        """
        id: NK1.16 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.16
        """
        self._c_data[15] = (ts,)

    @property
    def living_dependency(self) -> tuple[LivingDependency, ...] | tuple[None]:
        """
        id: NK1.17 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.17
        """
        return self._c_data[16]

    @living_dependency.setter  # set NK1.17
    def living_dependency(
        self, living_dependency: LivingDependency | tuple[LivingDependency] | None
    ):
        """
        id: NK1.17 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.17
        """
        if isinstance(living_dependency, tuple):
            self._c_data[16] = living_dependency
        else:
            self._c_data[16] = (living_dependency,)

    @property
    def ambulatory_status(self) -> tuple[AmbulatoryStatus, ...] | tuple[None]:
        """
        id: NK1.18 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.18
        """
        return self._c_data[17]

    @ambulatory_status.setter  # set NK1.18
    def ambulatory_status(
        self, ambulatory_status: AmbulatoryStatus | tuple[AmbulatoryStatus] | None
    ):
        """
        id: NK1.18 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.18
        """
        if isinstance(ambulatory_status, tuple):
            self._c_data[17] = ambulatory_status
        else:
            self._c_data[17] = (ambulatory_status,)

    @property
    def citizenship(self) -> tuple[Citizenship, ...] | tuple[None]:
        """
        id: NK1.19 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.19
        """
        return self._c_data[18]

    @citizenship.setter  # set NK1.19
    def citizenship(self, citizenship: Citizenship | tuple[Citizenship] | None):
        """
        id: NK1.19 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.19
        """
        if isinstance(citizenship, tuple):
            self._c_data[18] = citizenship
        else:
            self._c_data[18] = (citizenship,)

    @property  # get NK1.20
    def primary_language(self) -> PrimaryLanguage | None:
        """
        id: NK1.20 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.20
        """
        return self._c_data[19][0]

    @primary_language.setter  # set NK1.20
    def primary_language(self, primary_language: PrimaryLanguage | None):
        """
        id: NK1.20 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.20
        """
        self._c_data[19] = (primary_language,)

    @property  # get NK1.21
    def living_arrangement(self) -> LivingArrangement | None:
        """
        id: NK1.21 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.21
        """
        return self._c_data[20][0]

    @living_arrangement.setter  # set NK1.21
    def living_arrangement(self, living_arrangement: LivingArrangement | None):
        """
        id: NK1.21 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.21
        """
        self._c_data[20] = (living_arrangement,)

    @property  # get NK1.22
    def publicity_code(self) -> PublicityCode | None:
        """
        id: NK1.22 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.22
        """
        return self._c_data[21][0]

    @publicity_code.setter  # set NK1.22
    def publicity_code(self, publicity_code: PublicityCode | None):
        """
        id: NK1.22 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.22
        """
        self._c_data[21] = (publicity_code,)

    @property  # get NK1.23
    def protection_indicator(self) -> YesOrNoIndicator | None:
        """
        id: NK1.23 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.23
        """
        return self._c_data[22][0]

    @protection_indicator.setter  # set NK1.23
    def protection_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: NK1.23 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.23
        """
        self._c_data[22] = (yes_or_no_indicator,)

    @property  # get NK1.24
    def student_indicator(self) -> StudentStatus | None:
        """
        id: NK1.24 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.24
        """
        return self._c_data[23][0]

    @student_indicator.setter  # set NK1.24
    def student_indicator(self, student_status: StudentStatus | None):
        """
        id: NK1.24 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.24
        """
        self._c_data[23] = (student_status,)

    @property  # get NK1.25
    def religion(self) -> Religion | None:
        """
        id: NK1.25 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.25
        """
        return self._c_data[24][0]

    @religion.setter  # set NK1.25
    def religion(self, religion: Religion | None):
        """
        id: NK1.25 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.25
        """
        self._c_data[24] = (religion,)

    @property
    def mothers_maiden_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: NK1.26 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.26
        """
        return self._c_data[25]

    @mothers_maiden_name.setter  # set NK1.26
    def mothers_maiden_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: NK1.26 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.26
        """
        if isinstance(xpn, tuple):
            self._c_data[25] = xpn
        else:
            self._c_data[25] = (xpn,)

    @property  # get NK1.27
    def nationality(self) -> Nationality | None:
        """
        id: NK1.27 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.27
        """
        return self._c_data[26][0]

    @nationality.setter  # set NK1.27
    def nationality(self, nationality: Nationality | None):
        """
        id: NK1.27 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.27
        """
        self._c_data[26] = (nationality,)

    @property
    def ethnic_group(self) -> tuple[EthnicGroup, ...] | tuple[None]:
        """
        id: NK1.28 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.28
        """
        return self._c_data[27]

    @ethnic_group.setter  # set NK1.28
    def ethnic_group(self, ethnic_group: EthnicGroup | tuple[EthnicGroup] | None):
        """
        id: NK1.28 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.28
        """
        if isinstance(ethnic_group, tuple):
            self._c_data[27] = ethnic_group
        else:
            self._c_data[27] = (ethnic_group,)

    @property
    def contact_reason(self) -> tuple[ContactReason, ...] | tuple[None]:
        """
        id: NK1.29 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.29
        """
        return self._c_data[28]

    @contact_reason.setter  # set NK1.29
    def contact_reason(
        self, contact_reason: ContactReason | tuple[ContactReason] | None
    ):
        """
        id: NK1.29 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.29
        """
        if isinstance(contact_reason, tuple):
            self._c_data[28] = contact_reason
        else:
            self._c_data[28] = (contact_reason,)

    @property
    def contact_persons_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: NK1.30 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.30
        """
        return self._c_data[29]

    @contact_persons_name.setter  # set NK1.30
    def contact_persons_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: NK1.30 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.30
        """
        if isinstance(xpn, tuple):
            self._c_data[29] = xpn
        else:
            self._c_data[29] = (xpn,)

    @property
    def contact_persons_telephone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: NK1.31 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.31
        """
        return self._c_data[30]

    @contact_persons_telephone_number.setter  # set NK1.31
    def contact_persons_telephone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: NK1.31 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.31
        """
        if isinstance(xtn, tuple):
            self._c_data[30] = xtn
        else:
            self._c_data[30] = (xtn,)

    @property
    def contact_persons_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: NK1.32 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.32
        """
        return self._c_data[31]

    @contact_persons_address.setter  # set NK1.32
    def contact_persons_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: NK1.32 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.32
        """
        if isinstance(xad, tuple):
            self._c_data[31] = xad
        else:
            self._c_data[31] = (xad,)

    @property
    def next_of_kin_or_associated_partys_identifiers(
        self,
    ) -> tuple[CX, ...] | tuple[None]:
        """
        id: NK1.33 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.33
        """
        return self._c_data[32]

    @next_of_kin_or_associated_partys_identifiers.setter  # set NK1.33
    def next_of_kin_or_associated_partys_identifiers(self, cx: CX | tuple[CX] | None):
        """
        id: NK1.33 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.33
        """
        if isinstance(cx, tuple):
            self._c_data[32] = cx
        else:
            self._c_data[32] = (cx,)

    @property  # get NK1.34
    def job_status(self) -> JobStatus | None:
        """
        id: NK1.34 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.34
        """
        return self._c_data[33][0]

    @job_status.setter  # set NK1.34
    def job_status(self, job_status: JobStatus | None):
        """
        id: NK1.34 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.34
        """
        self._c_data[33] = (job_status,)

    @property
    def race(self) -> tuple[Race, ...] | tuple[None]:
        """
        id: NK1.35 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.35
        """
        return self._c_data[34]

    @race.setter  # set NK1.35
    def race(self, race: Race | tuple[Race] | None):
        """
        id: NK1.35 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.35
        """
        if isinstance(race, tuple):
            self._c_data[34] = race
        else:
            self._c_data[34] = (race,)

    @property  # get NK1.36
    def handicap(self) -> Handicap | None:
        """
        id: NK1.36 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.36
        """
        return self._c_data[35][0]

    @handicap.setter  # set NK1.36
    def handicap(self, handicap: Handicap | None):
        """
        id: NK1.36 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.36
        """
        self._c_data[35] = (handicap,)

    @property  # get NK1.37
    def contact_person_social_security_number(self) -> ST | None:
        """
        id: NK1.37 | len: 16 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.37
        """
        return self._c_data[36][0]

    @contact_person_social_security_number.setter  # set NK1.37
    def contact_person_social_security_number(self, st: ST | None):
        """
        id: NK1.37 | len: 16 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.37
        """
        self._c_data[36] = (st,)

    @property  # get NK1.38
    def next_of_kin_birth_place(self) -> ST | None:
        """
        id: NK1.38 | len: 250 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.38
        """
        return self._c_data[37][0]

    @next_of_kin_birth_place.setter  # set NK1.38
    def next_of_kin_birth_place(self, st: ST | None):
        """
        id: NK1.38 | len: 250 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.38
        """
        self._c_data[37] = (st,)

    @property  # get NK1.39
    def vip_indicator(self) -> VipIndicator | None:
        """
        id: NK1.39 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.39
        """
        return self._c_data[38][0]

    @vip_indicator.setter  # set NK1.39
    def vip_indicator(self, vip_indicator: VipIndicator | None):
        """
        id: NK1.39 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NK1.39
        """
        self._c_data[38] = (vip_indicator,)
