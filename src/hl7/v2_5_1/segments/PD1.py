from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.XON import XON
from ..data_types.IS import IS
from ..data_types.CX import CX
from ..data_types.DT import DT
from ..data_types.ID import ID
from ..data_types.XCN import XCN
from ..tables.StudentStatus import StudentStatus
from ..tables.AdvanceDirectiveCode import AdvanceDirectiveCode
from ..tables.LivingWillCode import LivingWillCode
from ..tables.LivingDependency import LivingDependency
from ..tables.ImmunizationRegistryStatus import ImmunizationRegistryStatus
from ..tables.LivingArrangement import LivingArrangement
from ..tables.MilitaryRankOrGrade import MilitaryRankOrGrade
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.PublicityCode import PublicityCode
from ..tables.OrganDonorCode import OrganDonorCode
from ..tables.MilitaryService import MilitaryService
from ..tables.Handicap import Handicap
from ..tables.MilitaryStatus import MilitaryStatus


"""
Patient Additional Demographic - PD1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PD1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PD1,
    CE, XON, IS, CX, DT, ID, XCN
)

pd1 = PD1(  #  - The patient additional demographic segment contains demographic information that is likely to change about the patient
    living_dependency=None,  # IS(...) 
    living_arrangement=None,  # IS(...) 
    patient_primary_facility=None,  # XON(...) 
    patient_primary_care_provider_name_and_id_no=None,  # XCN(...) 
    student_indicator=None,  # IS(...) 
    handicap=None,  # IS(...) 
    living_will_code=None,  # IS(...) 
    organ_donor_code=None,  # IS(...) 
    separate_bill=None,  # ID(...) 
    duplicate_patient=None,  # CX(...) 
    publicity_code=None,  # CE(...) 
    protection_indicator=None,  # ID(...) 
    protection_indicator_effective_date=None,  # DT(...) 
    place_of_worship=None,  # XON(...) 
    advance_directive_code=None,  # CE(...) 
    immunization_registry_status=None,  # IS(...) 
    immunization_registry_status_effective_date=None,  # DT(...) 
    publicity_code_effective_date=None,  # DT(...) 
    military_branch=None,  # IS(...) 
    military_rank_or_grade=None,  # IS(...) 
    military_status=None,  # IS(...) 
)

-----END SEGMENT::PD1 TEMPLATE-----
"""


class PD1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PD1"""
    _hl7_name = """Patient Additional Demographic"""
    _hl7_description = """The patient additional demographic segment contains demographic information that is likely to change about the patient"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1"
    _c_length = (2, 2, 250, 250, 2, 2, 2, 2, 1, 250, 250, 1, 8, 250, 250, 1, 8, 8, 5, 2, 3,)
    _c_rpt = (65535, 1, 65535, 65535, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 65535, 65535, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (IS, IS, XON, XCN, IS, IS, IS, IS, ID, CX, CE, ID, DT, XON, CE, IS, DT, DT, IS, IS, IS,)
    _c_aliases = ("PD1.1", "PD1.2", "PD1.3", "PD1.4", "PD1.5", "PD1.6", "PD1.7", "PD1.8", "PD1.9", "PD1.10", "PD1.11", "PD1.12", "PD1.13", "PD1.14", "PD1.15", "PD1.16", "PD1.17", "PD1.18", "PD1.19", "PD1.20", "PD1.21",)
    _c_names = ("Living Dependency", "Living Arrangement", "Patient Primary Facility", "Patient Primary Care Provider Name and ID No.", "Student Indicator", "Handicap", "Living Will Code", "Organ Donor Code", "Separate Bill", "Duplicate Patient", "Publicity Code", "Protection Indicator", "Protection Indicator Effective Date", "Place of Worship", "Advance Directive Code", "Immunization Registry Status", "Immunization Registry Status Effective Date", "Publicity Code Effective Date", "Military Branch", "Military Rank/Grade", "Military Status",)
    _c_attrs = ("living_dependency", "living_arrangement", "patient_primary_facility", "patient_primary_care_provider_name_and_id_no", "student_indicator", "handicap", "living_will_code", "organ_donor_code", "separate_bill", "duplicate_patient", "publicity_code", "protection_indicator", "protection_indicator_effective_date", "place_of_worship", "advance_directive_code", "immunization_registry_status", "immunization_registry_status_effective_date", "publicity_code_effective_date", "military_branch", "military_rank_or_grade", "military_status",)
    # fmt: on

    def __init__(
        self,
        living_dependency: LivingDependency | IS | None = None,  # PD1.1
        living_arrangement: LivingArrangement | IS | None = None,  # PD1.2
        patient_primary_facility: XON | None = None,  # PD1.3
        patient_primary_care_provider_name_and_id_no: XCN | None = None,  # PD1.4
        student_indicator: StudentStatus | IS | None = None,  # PD1.5
        handicap: Handicap | IS | None = None,  # PD1.6
        living_will_code: LivingWillCode | IS | None = None,  # PD1.7
        organ_donor_code: OrganDonorCode | IS | None = None,  # PD1.8
        separate_bill: YesOrNoIndicator | ID | None = None,  # PD1.9
        duplicate_patient: CX | None = None,  # PD1.10
        publicity_code: PublicityCode | CE | None = None,  # PD1.11
        protection_indicator: YesOrNoIndicator | ID | None = None,  # PD1.12
        protection_indicator_effective_date: DT | None = None,  # PD1.13
        place_of_worship: XON | None = None,  # PD1.14
        advance_directive_code: AdvanceDirectiveCode | CE | None = None,  # PD1.15
        immunization_registry_status: ImmunizationRegistryStatus
        | IS
        | None = None,  # PD1.16
        immunization_registry_status_effective_date: DT | None = None,  # PD1.17
        publicity_code_effective_date: DT | None = None,  # PD1.18
        military_branch: MilitaryService | IS | None = None,  # PD1.19
        military_rank_or_grade: MilitaryRankOrGrade | IS | None = None,  # PD1.20
        military_status: MilitaryStatus | IS | None = None,  # PD1.21
    ):
        """
        Patient Additional Demographic - `PD1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1>`_
        The patient additional demographic segment contains demographic information that is likely to change about the patient.

        :param living_dependency: Coded value for user-defined tables (id: PD1.1 | len: 2 | use: O | rpt: *)
        :param living_arrangement: Coded value for user-defined tables (id: PD1.2 | len: 2 | use: O | rpt: 1)
        :param patient_primary_facility: Extended Composite Name and Identification Number for Organizations (id: PD1.3 | len: 250 | use: O | rpt: *)
        :param patient_primary_care_provider_name_and_id_no: Extended Composite ID Number and Name for Persons (id: PD1.4 | len: 250 | use: B | rpt: *)
        :param student_indicator: Coded value for user-defined tables (id: PD1.5 | len: 2 | use: O | rpt: 1)
        :param handicap: Coded value for user-defined tables (id: PD1.6 | len: 2 | use: O | rpt: 1)
        :param living_will_code: Coded value for user-defined tables (id: PD1.7 | len: 2 | use: O | rpt: 1)
        :param organ_donor_code: Coded value for user-defined tables (id: PD1.8 | len: 2 | use: O | rpt: 1)
        :param separate_bill: Coded values for HL7 tables (id: PD1.9 | len: 1 | use: O | rpt: 1)
        :param duplicate_patient: Extended Composite ID with Check Digit (id: PD1.10 | len: 250 | use: O | rpt: *)
        :param publicity_code: Coded Element (id: PD1.11 | len: 250 | use: O | rpt: 1)
        :param protection_indicator: Coded values for HL7 tables (id: PD1.12 | len: 1 | use: O | rpt: 1)
        :param protection_indicator_effective_date: Date (id: PD1.13 | len: 8 | use: O | rpt: 1)
        :param place_of_worship: Extended Composite Name and Identification Number for Organizations (id: PD1.14 | len: 250 | use: O | rpt: *)
        :param advance_directive_code: Coded Element (id: PD1.15 | len: 250 | use: O | rpt: *)
        :param immunization_registry_status: Coded value for user-defined tables (id: PD1.16 | len: 1 | use: O | rpt: 1)
        :param immunization_registry_status_effective_date: Date (id: PD1.17 | len: 8 | use: O | rpt: 1)
        :param publicity_code_effective_date: Date (id: PD1.18 | len: 8 | use: O | rpt: 1)
        :param military_branch: Coded value for user-defined tables (id: PD1.19 | len: 5 | use: O | rpt: 1)
        :param military_rank_or_grade: Coded value for user-defined tables (id: PD1.20 | len: 2 | use: O | rpt: 1)
        :param military_status: Coded value for user-defined tables (id: PD1.21 | len: 3 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 21
        self.living_dependency = living_dependency
        self.living_arrangement = living_arrangement
        self.patient_primary_facility = patient_primary_facility
        self.patient_primary_care_provider_name_and_id_no = (
            patient_primary_care_provider_name_and_id_no
        )
        self.student_indicator = student_indicator
        self.handicap = handicap
        self.living_will_code = living_will_code
        self.organ_donor_code = organ_donor_code
        self.separate_bill = separate_bill
        self.duplicate_patient = duplicate_patient
        self.publicity_code = publicity_code
        self.protection_indicator = protection_indicator
        self.protection_indicator_effective_date = protection_indicator_effective_date
        self.place_of_worship = place_of_worship
        self.advance_directive_code = advance_directive_code
        self.immunization_registry_status = immunization_registry_status
        self.immunization_registry_status_effective_date = (
            immunization_registry_status_effective_date
        )
        self.publicity_code_effective_date = publicity_code_effective_date
        self.military_branch = military_branch
        self.military_rank_or_grade = military_rank_or_grade
        self.military_status = military_status

    @property
    def living_dependency(self) -> tuple[LivingDependency, ...] | tuple[None]:
        """
        id: PD1.1 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.1
        """
        return self._c_data[0]

    @living_dependency.setter  # set PD1.1
    def living_dependency(
        self, living_dependency: LivingDependency | tuple[LivingDependency] | None
    ):
        """
        id: PD1.1 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.1
        """
        if isinstance(living_dependency, tuple):
            self._c_data[0] = living_dependency
        else:
            self._c_data[0] = (living_dependency,)

    @property  # get PD1.2
    def living_arrangement(self) -> LivingArrangement | None:
        """
        id: PD1.2 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.2
        """
        return self._c_data[1][0]

    @living_arrangement.setter  # set PD1.2
    def living_arrangement(self, living_arrangement: LivingArrangement | None):
        """
        id: PD1.2 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.2
        """
        self._c_data[1] = (living_arrangement,)

    @property
    def patient_primary_facility(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: PD1.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.3
        """
        return self._c_data[2]

    @patient_primary_facility.setter  # set PD1.3
    def patient_primary_facility(self, xon: XON | tuple[XON] | None):
        """
        id: PD1.3 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.3
        """
        if isinstance(xon, tuple):
            self._c_data[2] = xon
        else:
            self._c_data[2] = (xon,)

    @property
    def patient_primary_care_provider_name_and_id_no(
        self,
    ) -> tuple[XCN, ...] | tuple[None]:
        """
        id: PD1.4 | len: 250 | use: B | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.4
        """
        return self._c_data[3]

    @patient_primary_care_provider_name_and_id_no.setter  # set PD1.4
    def patient_primary_care_provider_name_and_id_no(
        self, xcn: XCN | tuple[XCN] | None
    ):
        """
        id: PD1.4 | len: 250 | use: B | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.4
        """
        if isinstance(xcn, tuple):
            self._c_data[3] = xcn
        else:
            self._c_data[3] = (xcn,)

    @property  # get PD1.5
    def student_indicator(self) -> StudentStatus | None:
        """
        id: PD1.5 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.5
        """
        return self._c_data[4][0]

    @student_indicator.setter  # set PD1.5
    def student_indicator(self, student_status: StudentStatus | None):
        """
        id: PD1.5 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.5
        """
        self._c_data[4] = (student_status,)

    @property  # get PD1.6
    def handicap(self) -> Handicap | None:
        """
        id: PD1.6 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.6
        """
        return self._c_data[5][0]

    @handicap.setter  # set PD1.6
    def handicap(self, handicap: Handicap | None):
        """
        id: PD1.6 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.6
        """
        self._c_data[5] = (handicap,)

    @property  # get PD1.7
    def living_will_code(self) -> LivingWillCode | None:
        """
        id: PD1.7 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.7
        """
        return self._c_data[6][0]

    @living_will_code.setter  # set PD1.7
    def living_will_code(self, living_will_code: LivingWillCode | None):
        """
        id: PD1.7 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.7
        """
        self._c_data[6] = (living_will_code,)

    @property  # get PD1.8
    def organ_donor_code(self) -> OrganDonorCode | None:
        """
        id: PD1.8 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.8
        """
        return self._c_data[7][0]

    @organ_donor_code.setter  # set PD1.8
    def organ_donor_code(self, organ_donor_code: OrganDonorCode | None):
        """
        id: PD1.8 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.8
        """
        self._c_data[7] = (organ_donor_code,)

    @property  # get PD1.9
    def separate_bill(self) -> YesOrNoIndicator | None:
        """
        id: PD1.9 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.9
        """
        return self._c_data[8][0]

    @separate_bill.setter  # set PD1.9
    def separate_bill(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PD1.9 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.9
        """
        self._c_data[8] = (yes_or_no_indicator,)

    @property
    def duplicate_patient(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: PD1.10 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.10
        """
        return self._c_data[9]

    @duplicate_patient.setter  # set PD1.10
    def duplicate_patient(self, cx: CX | tuple[CX] | None):
        """
        id: PD1.10 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.10
        """
        if isinstance(cx, tuple):
            self._c_data[9] = cx
        else:
            self._c_data[9] = (cx,)

    @property  # get PD1.11
    def publicity_code(self) -> PublicityCode | None:
        """
        id: PD1.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.11
        """
        return self._c_data[10][0]

    @publicity_code.setter  # set PD1.11
    def publicity_code(self, publicity_code: PublicityCode | None):
        """
        id: PD1.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.11
        """
        self._c_data[10] = (publicity_code,)

    @property  # get PD1.12
    def protection_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PD1.12 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.12
        """
        return self._c_data[11][0]

    @protection_indicator.setter  # set PD1.12
    def protection_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PD1.12 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.12
        """
        self._c_data[11] = (yes_or_no_indicator,)

    @property  # get PD1.13
    def protection_indicator_effective_date(self) -> DT | None:
        """
        id: PD1.13 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.13
        """
        return self._c_data[12][0]

    @protection_indicator_effective_date.setter  # set PD1.13
    def protection_indicator_effective_date(self, dt: DT | None):
        """
        id: PD1.13 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.13
        """
        self._c_data[12] = (dt,)

    @property
    def place_of_worship(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: PD1.14 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.14
        """
        return self._c_data[13]

    @place_of_worship.setter  # set PD1.14
    def place_of_worship(self, xon: XON | tuple[XON] | None):
        """
        id: PD1.14 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.14
        """
        if isinstance(xon, tuple):
            self._c_data[13] = xon
        else:
            self._c_data[13] = (xon,)

    @property
    def advance_directive_code(self) -> tuple[AdvanceDirectiveCode, ...] | tuple[None]:
        """
        id: PD1.15 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.15
        """
        return self._c_data[14]

    @advance_directive_code.setter  # set PD1.15
    def advance_directive_code(
        self,
        advance_directive_code: AdvanceDirectiveCode
        | tuple[AdvanceDirectiveCode]
        | None,
    ):
        """
        id: PD1.15 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.15
        """
        if isinstance(advance_directive_code, tuple):
            self._c_data[14] = advance_directive_code
        else:
            self._c_data[14] = (advance_directive_code,)

    @property  # get PD1.16
    def immunization_registry_status(self) -> ImmunizationRegistryStatus | None:
        """
        id: PD1.16 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.16
        """
        return self._c_data[15][0]

    @immunization_registry_status.setter  # set PD1.16
    def immunization_registry_status(
        self, immunization_registry_status: ImmunizationRegistryStatus | None
    ):
        """
        id: PD1.16 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.16
        """
        self._c_data[15] = (immunization_registry_status,)

    @property  # get PD1.17
    def immunization_registry_status_effective_date(self) -> DT | None:
        """
        id: PD1.17 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.17
        """
        return self._c_data[16][0]

    @immunization_registry_status_effective_date.setter  # set PD1.17
    def immunization_registry_status_effective_date(self, dt: DT | None):
        """
        id: PD1.17 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.17
        """
        self._c_data[16] = (dt,)

    @property  # get PD1.18
    def publicity_code_effective_date(self) -> DT | None:
        """
        id: PD1.18 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.18
        """
        return self._c_data[17][0]

    @publicity_code_effective_date.setter  # set PD1.18
    def publicity_code_effective_date(self, dt: DT | None):
        """
        id: PD1.18 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.18
        """
        self._c_data[17] = (dt,)

    @property  # get PD1.19
    def military_branch(self) -> MilitaryService | None:
        """
        id: PD1.19 | len: 5 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.19
        """
        return self._c_data[18][0]

    @military_branch.setter  # set PD1.19
    def military_branch(self, military_service: MilitaryService | None):
        """
        id: PD1.19 | len: 5 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.19
        """
        self._c_data[18] = (military_service,)

    @property  # get PD1.20
    def military_rank_or_grade(self) -> MilitaryRankOrGrade | None:
        """
        id: PD1.20 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.20
        """
        return self._c_data[19][0]

    @military_rank_or_grade.setter  # set PD1.20
    def military_rank_or_grade(
        self, military_rank_or_grade: MilitaryRankOrGrade | None
    ):
        """
        id: PD1.20 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.20
        """
        self._c_data[19] = (military_rank_or_grade,)

    @property  # get PD1.21
    def military_status(self) -> MilitaryStatus | None:
        """
        id: PD1.21 | len: 3 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.21
        """
        return self._c_data[20][0]

    @military_status.setter  # set PD1.21
    def military_status(self, military_status: MilitaryStatus | None):
        """
        id: PD1.21 | len: 3 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PD1.21
        """
        self._c_data[20] = (military_status,)
