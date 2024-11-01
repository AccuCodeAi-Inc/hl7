from __future__ import annotations
from ...base import HL7Segment
from ..data_types.DIN import DIN
from ..data_types.JCC import JCC
from ..data_types.XPN import XPN
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.IS import IS
from ..data_types.CX import CX
from ..data_types.DT import DT
from ..data_types.DR import DR
from ..data_types.CWE import CWE
from ..data_types.CE import CE
from ..data_types.XTN import XTN
from ..data_types.XAD import XAD
from ..data_types.ST import ST
from ..data_types.DLN import DLN
from ..tables.StaffType import StaffType
from ..tables.HospitalService import HospitalService
from ..tables.PreferredMethodOfContact import PreferredMethodOfContact
from ..tables.Race import Race
from ..tables.EmploymentStatus import EmploymentStatus
from ..tables.Citizenship import Citizenship
from ..tables.Department import Department
from ..tables.ActiveOrInactive import ActiveOrInactive
from ..tables.AdministrativeSex import AdministrativeSex
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.CostCenterCode import CostCenterCode
from ..tables.InstitutionRelationshipType import InstitutionRelationshipType
from ..tables.InactiveReasonCode import InactiveReasonCode
from ..tables.EthnicGroup import EthnicGroup
from ..tables.MaritalStatus import MaritalStatus


"""
Staff Identification - STF
HL7 Version: 2.5.1

-----BEGIN SEGMENT::STF TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    STF,
    DIN, JCC, XPN, TS, ID, IS, CX, DT, DR, CWE, CE, XTN, XAD, ST, DLN
)

stf = STF(  #  - The STF segment can identify any personnel referenced by information systems
    primary_key_value_stf=None,  # CE(...) 
    staff_identifier_list=None,  # CX(...) 
    staff_name=None,  # XPN(...) 
    staff_type=None,  # IS(...) 
    administrative_sex=None,  # IS(...) 
    date_or_time_of_birth=None,  # TS(...) 
    active_or_inactive_flag=None,  # ID(...) 
    department=None,  # CE(...) 
    hospital_service_stf=None,  # CE(...) 
    phone=None,  # XTN(...) 
    office_or_home_address_or_birthplace=None,  # XAD(...) 
    institution_activation_date=None,  # DIN(...) 
    institution_inactivation_date=None,  # DIN(...) 
    backup_person_id=None,  # CE(...) 
    e_mail_address=None,  # ST(...) 
    preferred_method_of_contact=None,  # CE(...) 
    marital_status=None,  # CE(...) 
    job_title=None,  # ST(...) 
    job_code_or_class=None,  # JCC(...) 
    employment_status_code=None,  # CE(...) 
    additional_insured_on_auto=None,  # ID(...) 
    drivers_license_number_staff=None,  # DLN(...) 
    copy_auto_ins=None,  # ID(...) 
    auto_ins_expires=None,  # DT(...) 
    date_last_dmv_review=None,  # DT(...) 
    date_next_dmv_review=None,  # DT(...) 
    race=None,  # CE(...) 
    ethnic_group=None,  # CE(...) 
    re_activation_approval_indicator=None,  # ID(...) 
    citizenship=None,  # CWE(...) 
    death_date_and_time=None,  # TS(...) 
    death_indicator=None,  # ID(...) 
    institution_relationship_type_code=None,  # CWE(...) 
    institution_relationship_period=None,  # DR(...) 
    expected_return_date=None,  # DT(...) 
    cost_center_code=None,  # CWE(...) 
    generic_classification_indicator=None,  # ID(...) 
    inactive_reason_code=None,  # CWE(...) 
)

-----END SEGMENT::STF TEMPLATE-----
"""


class STF(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """STF"""
    _hl7_name = """Staff Identification"""
    _hl7_description = """The STF segment can identify any personnel referenced by information systems"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/STF"
    _c_length = (250, 250, 250, 2, 1, 26, 1, 250, 250, 250, 250, 276, 276, 250, 40, 250, 250, 20, 20, 250, 1, 25, 1, 8, 8, 8, 250, 250, 1, 250, 8, 1, 250, 52, 8, 250, 1, 250,)
    _c_rpt = (1, 65535, 65535, 65535, 1, 1, 1, 65535, 65535, 65535, 65535, 65535, 65535, 65535, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 65535, 1, 1,)
    _c_usage = ("C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, CX, XPN, IS, IS, TS, ID, CE, CE, XTN, XAD, DIN, DIN, CE, ST, CE, CE, ST, JCC, CE, ID, DLN, ID, DT, DT, DT, CE, CE, ID, CWE, TS, ID, CWE, DR, DT, CWE, ID, CWE,)
    _c_aliases = ("STF.1", "STF.2", "STF.3", "STF.4", "STF.5", "STF.6", "STF.7", "STF.8", "STF.9", "STF.10", "STF.11", "STF.12", "STF.13", "STF.14", "STF.15", "STF.16", "STF.17", "STF.18", "STF.19", "STF.20", "STF.21", "STF.22", "STF.23", "STF.24", "STF.25", "STF.26", "STF.27", "STF.28", "STF.29", "STF.30", "STF.31", "STF.32", "STF.33", "STF.34", "STF.35", "STF.36", "STF.37", "STF.38",)
    _c_names = ("Primary Key Value - STF", "Staff Identifier List", "Staff Name", "Staff Type", "Administrative Sex", "Date/Time of Birth", "Active/Inactive Flag", "Department", "Hospital Service - STF", "Phone", "Office/Home Address/Birthplace", "Institution Activation Date", "Institution Inactivation Date", "Backup Person ID", "E-Mail Address", "Preferred Method of Contact", "Marital Status", "Job Title", "Job Code/Class", "Employment Status Code", "Additional Insured on Auto", "Driver's License Number - Staff", "Copy Auto Ins", "Auto Ins. Expires", "Date Last DMV Review", "Date Next DMV Review", "Race", "Ethnic Group", "Re-activation Approval Indicator", "Citizenship", "Death Date and Time", "Death Indicator", "Institution Relationship Type Code", "Institution Relationship Period", "Expected Return Date", "Cost Center Code", "Generic Classification Indicator", "Inactive Reason Code",)
    _c_attrs = ("primary_key_value_stf", "staff_identifier_list", "staff_name", "staff_type", "administrative_sex", "date_or_time_of_birth", "active_or_inactive_flag", "department", "hospital_service_stf", "phone", "office_or_home_address_or_birthplace", "institution_activation_date", "institution_inactivation_date", "backup_person_id", "e_mail_address", "preferred_method_of_contact", "marital_status", "job_title", "job_code_or_class", "employment_status_code", "additional_insured_on_auto", "drivers_license_number_staff", "copy_auto_ins", "auto_ins_expires", "date_last_dmv_review", "date_next_dmv_review", "race", "ethnic_group", "re_activation_approval_indicator", "citizenship", "death_date_and_time", "death_indicator", "institution_relationship_type_code", "institution_relationship_period", "expected_return_date", "cost_center_code", "generic_classification_indicator", "inactive_reason_code",)
    # fmt: on

    def __init__(
        self,
        primary_key_value_stf: CE | tuple[CE] | None = None,  # STF.1
        staff_identifier_list: CX | tuple[CX] | None = None,  # STF.2
        staff_name: XPN | tuple[XPN] | None = None,  # STF.3
        staff_type: StaffType | IS | tuple[StaffType | IS] | None = None,  # STF.4
        administrative_sex: AdministrativeSex
        | IS
        | tuple[AdministrativeSex | IS]
        | None = None,  # STF.5
        date_or_time_of_birth: TS | tuple[TS] | None = None,  # STF.6
        active_or_inactive_flag: ActiveOrInactive
        | ID
        | tuple[ActiveOrInactive | ID]
        | None = None,  # STF.7
        department: Department | CE | tuple[Department | CE] | None = None,  # STF.8
        hospital_service_stf: HospitalService
        | CE
        | tuple[HospitalService | CE]
        | None = None,  # STF.9
        phone: XTN | tuple[XTN] | None = None,  # STF.10
        office_or_home_address_or_birthplace: XAD | tuple[XAD] | None = None,  # STF.11
        institution_activation_date: DIN | tuple[DIN] | None = None,  # STF.12
        institution_inactivation_date: DIN | tuple[DIN] | None = None,  # STF.13
        backup_person_id: CE | tuple[CE] | None = None,  # STF.14
        e_mail_address: ST | tuple[ST] | None = None,  # STF.15
        preferred_method_of_contact: PreferredMethodOfContact
        | CE
        | tuple[PreferredMethodOfContact | CE]
        | None = None,  # STF.16
        marital_status: MaritalStatus
        | CE
        | tuple[MaritalStatus | CE]
        | None = None,  # STF.17
        job_title: ST | tuple[ST] | None = None,  # STF.18
        job_code_or_class: JCC | tuple[JCC] | None = None,  # STF.19
        employment_status_code: EmploymentStatus
        | CE
        | tuple[EmploymentStatus | CE]
        | None = None,  # STF.20
        additional_insured_on_auto: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # STF.21
        drivers_license_number_staff: DLN | tuple[DLN] | None = None,  # STF.22
        copy_auto_ins: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # STF.23
        auto_ins_expires: DT | tuple[DT] | None = None,  # STF.24
        date_last_dmv_review: DT | tuple[DT] | None = None,  # STF.25
        date_next_dmv_review: DT | tuple[DT] | None = None,  # STF.26
        race: Race | CE | tuple[Race | CE] | None = None,  # STF.27
        ethnic_group: EthnicGroup
        | CE
        | tuple[EthnicGroup | CE]
        | None = None,  # STF.28
        re_activation_approval_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # STF.29
        citizenship: Citizenship
        | CWE
        | tuple[Citizenship | CWE]
        | None = None,  # STF.30
        death_date_and_time: TS | tuple[TS] | None = None,  # STF.31
        death_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # STF.32
        institution_relationship_type_code: InstitutionRelationshipType
        | CWE
        | tuple[InstitutionRelationshipType | CWE]
        | None = None,  # STF.33
        institution_relationship_period: DR | tuple[DR] | None = None,  # STF.34
        expected_return_date: DT | tuple[DT] | None = None,  # STF.35
        cost_center_code: CostCenterCode
        | CWE
        | tuple[CostCenterCode | CWE]
        | None = None,  # STF.36
        generic_classification_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # STF.37
        inactive_reason_code: InactiveReasonCode
        | CWE
        | tuple[InactiveReasonCode | CWE]
        | None = None,  # STF.38
    ):
        """
        Staff Identification - `STF <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/STF>`_
        The STF segment can identify any personnel referenced by information systems.  These can be providers, staff, system users, and referring agents.  In a network environment, this segment can be used to define personnel to other applications; for example, order entry clerks, insurance verification clerks, admission clerks, as well as provider demographics. When using the STF and PRA segments in the Staff/Practitioner Master File message, MFE-4-primary key value is used to link all the segments pertaining to the same master file entry.  Therefore, in the MFE segment, MFE-4-primary key value must be filled in.  Other segments may follow the STF segment to provide data for a particular type of staff member. The PRA segment (practitioner) is one such.  It may optionally follow the STF segment in order to add practitionerspecific data. Other segments may be defined as needed. When using the segments included in this chapter for other then Staff/Practitioner Master File messages, disregard references to MFE-4 - primary key value.

        :param primary_key_value_stf: Coded Element (id: STF.1 | len: 250 | use: C | rpt: 1)
        :param staff_identifier_list: Extended Composite ID with Check Digit (id: STF.2 | len: 250 | use: O | rpt: *)
        :param staff_name: Extended Person Name (id: STF.3 | len: 250 | use: O | rpt: *)
        :param staff_type: Coded value for user-defined tables (id: STF.4 | len: 2 | use: O | rpt: *)
        :param administrative_sex: Coded value for user-defined tables (id: STF.5 | len: 1 | use: O | rpt: 1)
        :param date_or_time_of_birth: Time Stamp (id: STF.6 | len: 26 | use: O | rpt: 1)
        :param active_or_inactive_flag: Coded values for HL7 tables (id: STF.7 | len: 1 | use: O | rpt: 1)
        :param department: Coded Element (id: STF.8 | len: 250 | use: O | rpt: *)
        :param hospital_service_stf: Coded Element (id: STF.9 | len: 250 | use: O | rpt: *)
        :param phone: Extended Telecommunication Number (id: STF.10 | len: 250 | use: O | rpt: *)
        :param office_or_home_address_or_birthplace: Extended Address (id: STF.11 | len: 250 | use: O | rpt: *)
        :param institution_activation_date: Date and Institution Name (id: STF.12 | len: 276 | use: O | rpt: *)
        :param institution_inactivation_date: Date and Institution Name (id: STF.13 | len: 276 | use: O | rpt: *)
        :param backup_person_id: Coded Element (id: STF.14 | len: 250 | use: O | rpt: *)
        :param e_mail_address: String Data (id: STF.15 | len: 40 | use: O | rpt: *)
        :param preferred_method_of_contact: Coded Element (id: STF.16 | len: 250 | use: O | rpt: 1)
        :param marital_status: Coded Element (id: STF.17 | len: 250 | use: O | rpt: 1)
        :param job_title: String Data (id: STF.18 | len: 20 | use: O | rpt: 1)
        :param job_code_or_class: Job Code/Class (id: STF.19 | len: 20 | use: O | rpt: 1)
        :param employment_status_code: Coded Element (id: STF.20 | len: 250 | use: O | rpt: 1)
        :param additional_insured_on_auto: Coded values for HL7 tables (id: STF.21 | len: 1 | use: O | rpt: 1)
        :param drivers_license_number_staff: Driver License Number (id: STF.22 | len: 25 | use: O | rpt: 1)
        :param copy_auto_ins: Coded values for HL7 tables (id: STF.23 | len: 1 | use: O | rpt: 1)
        :param auto_ins_expires: Date (id: STF.24 | len: 8 | use: O | rpt: 1)
        :param date_last_dmv_review: Date (id: STF.25 | len: 8 | use: O | rpt: 1)
        :param date_next_dmv_review: Date (id: STF.26 | len: 8 | use: O | rpt: 1)
        :param race: Coded Element (id: STF.27 | len: 250 | use: O | rpt: 1)
        :param ethnic_group: Coded Element (id: STF.28 | len: 250 | use: O | rpt: 1)
        :param re_activation_approval_indicator: Coded values for HL7 tables (id: STF.29 | len: 1 | use: O | rpt: 1)
        :param citizenship: Coded with Exceptions (id: STF.30 | len: 250 | use: O | rpt: *)
        :param death_date_and_time: Time Stamp (id: STF.31 | len: 8 | use: O | rpt: 1)
        :param death_indicator: Coded values for HL7 tables (id: STF.32 | len: 1 | use: O | rpt: 1)
        :param institution_relationship_type_code: Coded with Exceptions (id: STF.33 | len: 250 | use: O | rpt: 1)
        :param institution_relationship_period: Date/Time Range (id: STF.34 | len: 52 | use: O | rpt: 1)
        :param expected_return_date: Date (id: STF.35 | len: 8 | use: O | rpt: 1)
        :param cost_center_code: Coded with Exceptions (id: STF.36 | len: 250 | use: O | rpt: *)
        :param generic_classification_indicator: Coded values for HL7 tables (id: STF.37 | len: 1 | use: O | rpt: 1)
        :param inactive_reason_code: Coded with Exceptions (id: STF.38 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 38
        self.primary_key_value_stf = primary_key_value_stf
        self.staff_identifier_list = staff_identifier_list
        self.staff_name = staff_name
        self.staff_type = staff_type
        self.administrative_sex = administrative_sex
        self.date_or_time_of_birth = date_or_time_of_birth
        self.active_or_inactive_flag = active_or_inactive_flag
        self.department = department
        self.hospital_service_stf = hospital_service_stf
        self.phone = phone
        self.office_or_home_address_or_birthplace = office_or_home_address_or_birthplace
        self.institution_activation_date = institution_activation_date
        self.institution_inactivation_date = institution_inactivation_date
        self.backup_person_id = backup_person_id
        self.e_mail_address = e_mail_address
        self.preferred_method_of_contact = preferred_method_of_contact
        self.marital_status = marital_status
        self.job_title = job_title
        self.job_code_or_class = job_code_or_class
        self.employment_status_code = employment_status_code
        self.additional_insured_on_auto = additional_insured_on_auto
        self.drivers_license_number_staff = drivers_license_number_staff
        self.copy_auto_ins = copy_auto_ins
        self.auto_ins_expires = auto_ins_expires
        self.date_last_dmv_review = date_last_dmv_review
        self.date_next_dmv_review = date_next_dmv_review
        self.race = race
        self.ethnic_group = ethnic_group
        self.re_activation_approval_indicator = re_activation_approval_indicator
        self.citizenship = citizenship
        self.death_date_and_time = death_date_and_time
        self.death_indicator = death_indicator
        self.institution_relationship_type_code = institution_relationship_type_code
        self.institution_relationship_period = institution_relationship_period
        self.expected_return_date = expected_return_date
        self.cost_center_code = cost_center_code
        self.generic_classification_indicator = generic_classification_indicator
        self.inactive_reason_code = inactive_reason_code

    @property  # get STF.1
    def primary_key_value_stf(self) -> CE | None:
        """
        id: STF.1 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.1
        """
        return self._c_data[0][0]

    @primary_key_value_stf.setter  # set STF.1
    def primary_key_value_stf(self, ce: CE | None):
        """
        id: STF.1 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.1
        """
        self._c_data[0] = (ce,)

    @property
    def staff_identifier_list(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: STF.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.2
        """
        return self._c_data[1]

    @staff_identifier_list.setter  # set STF.2
    def staff_identifier_list(self, cx: CX | tuple[CX] | None):
        """
        id: STF.2 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.2
        """
        if isinstance(cx, tuple):
            self._c_data[1] = cx
        else:
            self._c_data[1] = (cx,)

    @property
    def staff_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: STF.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.3
        """
        return self._c_data[2]

    @staff_name.setter  # set STF.3
    def staff_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: STF.3 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.3
        """
        if isinstance(xpn, tuple):
            self._c_data[2] = xpn
        else:
            self._c_data[2] = (xpn,)

    @property
    def staff_type(self) -> tuple[StaffType, ...] | tuple[None]:
        """
        id: STF.4 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.4
        """
        return self._c_data[3]

    @staff_type.setter  # set STF.4
    def staff_type(self, staff_type: StaffType | tuple[StaffType] | None):
        """
        id: STF.4 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.4
        """
        if isinstance(staff_type, tuple):
            self._c_data[3] = staff_type
        else:
            self._c_data[3] = (staff_type,)

    @property  # get STF.5
    def administrative_sex(self) -> AdministrativeSex | None:
        """
        id: STF.5 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.5
        """
        return self._c_data[4][0]

    @administrative_sex.setter  # set STF.5
    def administrative_sex(self, administrative_sex: AdministrativeSex | None):
        """
        id: STF.5 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.5
        """
        self._c_data[4] = (administrative_sex,)

    @property  # get STF.6
    def date_or_time_of_birth(self) -> TS | None:
        """
        id: STF.6 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.6
        """
        return self._c_data[5][0]

    @date_or_time_of_birth.setter  # set STF.6
    def date_or_time_of_birth(self, ts: TS | None):
        """
        id: STF.6 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.6
        """
        self._c_data[5] = (ts,)

    @property  # get STF.7
    def active_or_inactive_flag(self) -> ActiveOrInactive | None:
        """
        id: STF.7 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.7
        """
        return self._c_data[6][0]

    @active_or_inactive_flag.setter  # set STF.7
    def active_or_inactive_flag(self, active_or_inactive: ActiveOrInactive | None):
        """
        id: STF.7 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.7
        """
        self._c_data[6] = (active_or_inactive,)

    @property
    def department(self) -> tuple[Department, ...] | tuple[None]:
        """
        id: STF.8 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.8
        """
        return self._c_data[7]

    @department.setter  # set STF.8
    def department(self, department: Department | tuple[Department] | None):
        """
        id: STF.8 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.8
        """
        if isinstance(department, tuple):
            self._c_data[7] = department
        else:
            self._c_data[7] = (department,)

    @property
    def hospital_service_stf(self) -> tuple[HospitalService, ...] | tuple[None]:
        """
        id: STF.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.9
        """
        return self._c_data[8]

    @hospital_service_stf.setter  # set STF.9
    def hospital_service_stf(
        self, hospital_service: HospitalService | tuple[HospitalService] | None
    ):
        """
        id: STF.9 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.9
        """
        if isinstance(hospital_service, tuple):
            self._c_data[8] = hospital_service
        else:
            self._c_data[8] = (hospital_service,)

    @property
    def phone(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: STF.10 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.10
        """
        return self._c_data[9]

    @phone.setter  # set STF.10
    def phone(self, xtn: XTN | tuple[XTN] | None):
        """
        id: STF.10 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.10
        """
        if isinstance(xtn, tuple):
            self._c_data[9] = xtn
        else:
            self._c_data[9] = (xtn,)

    @property
    def office_or_home_address_or_birthplace(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: STF.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.11
        """
        return self._c_data[10]

    @office_or_home_address_or_birthplace.setter  # set STF.11
    def office_or_home_address_or_birthplace(self, xad: XAD | tuple[XAD] | None):
        """
        id: STF.11 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.11
        """
        if isinstance(xad, tuple):
            self._c_data[10] = xad
        else:
            self._c_data[10] = (xad,)

    @property
    def institution_activation_date(self) -> tuple[DIN, ...] | tuple[None]:
        """
        id: STF.12 | len: 276 | use: O | rpt: *
        ---
        return_type: tuple[DIN, ...]: (Date and Institution Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.12
        """
        return self._c_data[11]

    @institution_activation_date.setter  # set STF.12
    def institution_activation_date(self, din: DIN | tuple[DIN] | None):
        """
        id: STF.12 | len: 276 | use: O | rpt: *
        ---
        param_type: DIN | tuple[DIN, ...]: (Date and Institution Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.12
        """
        if isinstance(din, tuple):
            self._c_data[11] = din
        else:
            self._c_data[11] = (din,)

    @property
    def institution_inactivation_date(self) -> tuple[DIN, ...] | tuple[None]:
        """
        id: STF.13 | len: 276 | use: O | rpt: *
        ---
        return_type: tuple[DIN, ...]: (Date and Institution Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.13
        """
        return self._c_data[12]

    @institution_inactivation_date.setter  # set STF.13
    def institution_inactivation_date(self, din: DIN | tuple[DIN] | None):
        """
        id: STF.13 | len: 276 | use: O | rpt: *
        ---
        param_type: DIN | tuple[DIN, ...]: (Date and Institution Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.13
        """
        if isinstance(din, tuple):
            self._c_data[12] = din
        else:
            self._c_data[12] = (din,)

    @property
    def backup_person_id(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: STF.14 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.14
        """
        return self._c_data[13]

    @backup_person_id.setter  # set STF.14
    def backup_person_id(self, ce: CE | tuple[CE] | None):
        """
        id: STF.14 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.14
        """
        if isinstance(ce, tuple):
            self._c_data[13] = ce
        else:
            self._c_data[13] = (ce,)

    @property
    def e_mail_address(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: STF.15 | len: 40 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.15
        """
        return self._c_data[14]

    @e_mail_address.setter  # set STF.15
    def e_mail_address(self, st: ST | tuple[ST] | None):
        """
        id: STF.15 | len: 40 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.15
        """
        if isinstance(st, tuple):
            self._c_data[14] = st
        else:
            self._c_data[14] = (st,)

    @property  # get STF.16
    def preferred_method_of_contact(self) -> PreferredMethodOfContact | None:
        """
        id: STF.16 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.16
        """
        return self._c_data[15][0]

    @preferred_method_of_contact.setter  # set STF.16
    def preferred_method_of_contact(
        self, preferred_method_of_contact: PreferredMethodOfContact | None
    ):
        """
        id: STF.16 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.16
        """
        self._c_data[15] = (preferred_method_of_contact,)

    @property  # get STF.17
    def marital_status(self) -> MaritalStatus | None:
        """
        id: STF.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.17
        """
        return self._c_data[16][0]

    @marital_status.setter  # set STF.17
    def marital_status(self, marital_status: MaritalStatus | None):
        """
        id: STF.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.17
        """
        self._c_data[16] = (marital_status,)

    @property  # get STF.18
    def job_title(self) -> ST | None:
        """
        id: STF.18 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.18
        """
        return self._c_data[17][0]

    @job_title.setter  # set STF.18
    def job_title(self, st: ST | None):
        """
        id: STF.18 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.18
        """
        self._c_data[17] = (st,)

    @property  # get STF.19
    def job_code_or_class(self) -> JCC | None:
        """
        id: STF.19 | len: 20 | use: O | rpt: 1
        ---
        return_type: JCC: Job Code/Class
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.19
        """
        return self._c_data[18][0]

    @job_code_or_class.setter  # set STF.19
    def job_code_or_class(self, jcc: JCC | None):
        """
        id: STF.19 | len: 20 | use: O | rpt: 1
        ---
        param_type: JCC: Job Code/Class
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.19
        """
        self._c_data[18] = (jcc,)

    @property  # get STF.20
    def employment_status_code(self) -> EmploymentStatus | None:
        """
        id: STF.20 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.20
        """
        return self._c_data[19][0]

    @employment_status_code.setter  # set STF.20
    def employment_status_code(self, employment_status: EmploymentStatus | None):
        """
        id: STF.20 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.20
        """
        self._c_data[19] = (employment_status,)

    @property  # get STF.21
    def additional_insured_on_auto(self) -> YesOrNoIndicator | None:
        """
        id: STF.21 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.21
        """
        return self._c_data[20][0]

    @additional_insured_on_auto.setter  # set STF.21
    def additional_insured_on_auto(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: STF.21 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.21
        """
        self._c_data[20] = (yes_or_no_indicator,)

    @property  # get STF.22
    def drivers_license_number_staff(self) -> DLN | None:
        """
        id: STF.22 | len: 25 | use: O | rpt: 1
        ---
        return_type: DLN: Driver License Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.22
        """
        return self._c_data[21][0]

    @drivers_license_number_staff.setter  # set STF.22
    def drivers_license_number_staff(self, dln: DLN | None):
        """
        id: STF.22 | len: 25 | use: O | rpt: 1
        ---
        param_type: DLN: Driver License Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.22
        """
        self._c_data[21] = (dln,)

    @property  # get STF.23
    def copy_auto_ins(self) -> YesOrNoIndicator | None:
        """
        id: STF.23 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.23
        """
        return self._c_data[22][0]

    @copy_auto_ins.setter  # set STF.23
    def copy_auto_ins(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: STF.23 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.23
        """
        self._c_data[22] = (yes_or_no_indicator,)

    @property  # get STF.24
    def auto_ins_expires(self) -> DT | None:
        """
        id: STF.24 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.24
        """
        return self._c_data[23][0]

    @auto_ins_expires.setter  # set STF.24
    def auto_ins_expires(self, dt: DT | None):
        """
        id: STF.24 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.24
        """
        self._c_data[23] = (dt,)

    @property  # get STF.25
    def date_last_dmv_review(self) -> DT | None:
        """
        id: STF.25 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.25
        """
        return self._c_data[24][0]

    @date_last_dmv_review.setter  # set STF.25
    def date_last_dmv_review(self, dt: DT | None):
        """
        id: STF.25 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.25
        """
        self._c_data[24] = (dt,)

    @property  # get STF.26
    def date_next_dmv_review(self) -> DT | None:
        """
        id: STF.26 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.26
        """
        return self._c_data[25][0]

    @date_next_dmv_review.setter  # set STF.26
    def date_next_dmv_review(self, dt: DT | None):
        """
        id: STF.26 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.26
        """
        self._c_data[25] = (dt,)

    @property  # get STF.27
    def race(self) -> Race | None:
        """
        id: STF.27 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.27
        """
        return self._c_data[26][0]

    @race.setter  # set STF.27
    def race(self, race: Race | None):
        """
        id: STF.27 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.27
        """
        self._c_data[26] = (race,)

    @property  # get STF.28
    def ethnic_group(self) -> EthnicGroup | None:
        """
        id: STF.28 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.28
        """
        return self._c_data[27][0]

    @ethnic_group.setter  # set STF.28
    def ethnic_group(self, ethnic_group: EthnicGroup | None):
        """
        id: STF.28 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.28
        """
        self._c_data[27] = (ethnic_group,)

    @property  # get STF.29
    def re_activation_approval_indicator(self) -> YesOrNoIndicator | None:
        """
        id: STF.29 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.29
        """
        return self._c_data[28][0]

    @re_activation_approval_indicator.setter  # set STF.29
    def re_activation_approval_indicator(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: STF.29 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.29
        """
        self._c_data[28] = (yes_or_no_indicator,)

    @property
    def citizenship(self) -> tuple[Citizenship, ...] | tuple[None]:
        """
        id: STF.30 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.30
        """
        return self._c_data[29]

    @citizenship.setter  # set STF.30
    def citizenship(self, citizenship: Citizenship | tuple[Citizenship] | None):
        """
        id: STF.30 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.30
        """
        if isinstance(citizenship, tuple):
            self._c_data[29] = citizenship
        else:
            self._c_data[29] = (citizenship,)

    @property  # get STF.31
    def death_date_and_time(self) -> TS | None:
        """
        id: STF.31 | len: 8 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.31
        """
        return self._c_data[30][0]

    @death_date_and_time.setter  # set STF.31
    def death_date_and_time(self, ts: TS | None):
        """
        id: STF.31 | len: 8 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.31
        """
        self._c_data[30] = (ts,)

    @property  # get STF.32
    def death_indicator(self) -> YesOrNoIndicator | None:
        """
        id: STF.32 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.32
        """
        return self._c_data[31][0]

    @death_indicator.setter  # set STF.32
    def death_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: STF.32 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.32
        """
        self._c_data[31] = (yes_or_no_indicator,)

    @property  # get STF.33
    def institution_relationship_type_code(self) -> InstitutionRelationshipType | None:
        """
        id: STF.33 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.33
        """
        return self._c_data[32][0]

    @institution_relationship_type_code.setter  # set STF.33
    def institution_relationship_type_code(
        self, institution_relationship_type: InstitutionRelationshipType | None
    ):
        """
        id: STF.33 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.33
        """
        self._c_data[32] = (institution_relationship_type,)

    @property  # get STF.34
    def institution_relationship_period(self) -> DR | None:
        """
        id: STF.34 | len: 52 | use: O | rpt: 1
        ---
        return_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.34
        """
        return self._c_data[33][0]

    @institution_relationship_period.setter  # set STF.34
    def institution_relationship_period(self, dr: DR | None):
        """
        id: STF.34 | len: 52 | use: O | rpt: 1
        ---
        param_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.34
        """
        self._c_data[33] = (dr,)

    @property  # get STF.35
    def expected_return_date(self) -> DT | None:
        """
        id: STF.35 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.35
        """
        return self._c_data[34][0]

    @expected_return_date.setter  # set STF.35
    def expected_return_date(self, dt: DT | None):
        """
        id: STF.35 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.35
        """
        self._c_data[34] = (dt,)

    @property
    def cost_center_code(self) -> tuple[CostCenterCode, ...] | tuple[None]:
        """
        id: STF.36 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.36
        """
        return self._c_data[35]

    @cost_center_code.setter  # set STF.36
    def cost_center_code(
        self, cost_center_code: CostCenterCode | tuple[CostCenterCode] | None
    ):
        """
        id: STF.36 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.36
        """
        if isinstance(cost_center_code, tuple):
            self._c_data[35] = cost_center_code
        else:
            self._c_data[35] = (cost_center_code,)

    @property  # get STF.37
    def generic_classification_indicator(self) -> YesOrNoIndicator | None:
        """
        id: STF.37 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.37
        """
        return self._c_data[36][0]

    @generic_classification_indicator.setter  # set STF.37
    def generic_classification_indicator(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: STF.37 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.37
        """
        self._c_data[36] = (yes_or_no_indicator,)

    @property  # get STF.38
    def inactive_reason_code(self) -> InactiveReasonCode | None:
        """
        id: STF.38 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.38
        """
        return self._c_data[37][0]

    @inactive_reason_code.setter  # set STF.38
    def inactive_reason_code(self, inactive_reason_code: InactiveReasonCode | None):
        """
        id: STF.38 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/STF.38
        """
        self._c_data[37] = (inactive_reason_code,)
