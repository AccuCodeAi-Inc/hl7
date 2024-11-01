from __future__ import annotations
from ...base import HL7Segment
from ..data_types.XAD import XAD
from ..data_types.IS import IS
from ..data_types.DT import DT
from ..data_types.CWE import CWE
from ..data_types.SI import SI
from ..data_types.DR import DR
from ..data_types.CE import CE
from ..data_types.XON import XON
from ..tables.DegreeOrLicenseOrCertificate import DegreeOrLicenseOrCertificate
from ..tables.SchoolType import SchoolType


"""
Educational Detail - EDU
HL7 Version: 2.5.1

-----BEGIN SEGMENT::EDU TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    EDU,
    XAD, IS, DT, CWE, SI, DR, CE, XON
)

edu = EDU(  #  - The EDU segment adds detailed educational information to the staff member identified by the STF segment
    set_id_edu=si,  # SI(...)  # Required.
    academic_degree=None,  # IS(...) 
    academic_degree_program_date_range=None,  # DR(...) 
    academic_degree_program_participation_date_range=None,  # DR(...) 
    academic_degree_granted_date=None,  # DT(...) 
    school=None,  # XON(...) 
    school_type_code=None,  # CE(...) 
    school_address=None,  # XAD(...) 
    major_field_of_study=None,  # CWE(...) 
)

-----END SEGMENT::EDU TEMPLATE-----
"""


class EDU(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """EDU"""
    _hl7_name = """Educational Detail"""
    _hl7_description = """The EDU segment adds detailed educational information to the staff member identified by the STF segment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EDU"
    _c_length = (60, 10, 52, 52, 8, 250, 250, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 65535,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, IS, DR, DR, DT, XON, CE, XAD, CWE,)
    _c_aliases = ("EDU.1", "EDU.2", "EDU.3", "EDU.4", "EDU.5", "EDU.6", "EDU.7", "EDU.8", "EDU.9",)
    _c_names = ("Set ID - EDU", "Academic Degree", "Academic Degree Program Date Range", "Academic Degree Program Participation Date Range", "Academic Degree Granted Date", "School", "School Type Code", "School Address", "Major Field of Study",)
    _c_attrs = ("set_id_edu", "academic_degree", "academic_degree_program_date_range", "academic_degree_program_participation_date_range", "academic_degree_granted_date", "school", "school_type_code", "school_address", "major_field_of_study",)
    # fmt: on

    def __init__(
        self,
        set_id_edu: SI | tuple[SI],  # EDU.1
        academic_degree: DegreeOrLicenseOrCertificate
        | IS
        | tuple[DegreeOrLicenseOrCertificate | IS]
        | None = None,  # EDU.2
        academic_degree_program_date_range: DR | tuple[DR] | None = None,  # EDU.3
        academic_degree_program_participation_date_range: DR
        | tuple[DR]
        | None = None,  # EDU.4
        academic_degree_granted_date: DT | tuple[DT] | None = None,  # EDU.5
        school: XON | tuple[XON] | None = None,  # EDU.6
        school_type_code: SchoolType
        | CE
        | tuple[SchoolType | CE]
        | None = None,  # EDU.7
        school_address: XAD | tuple[XAD] | None = None,  # EDU.8
        major_field_of_study: CWE | tuple[CWE] | None = None,  # EDU.9
    ):
        """
        Educational Detail - `EDU <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EDU>`_
        The EDU segment adds detailed educational information to the staff member identified by the STF segment. An EDU segment may optionally follow an STF segment. An EDU segment must always have been preceded by a corresponding STF segment.

        :param set_id_edu: Sequence ID (id: EDU.1 | len: 60 | use: R | rpt: 1)
        :param academic_degree: Coded value for user-defined tables (id: EDU.2 | len: 10 | use: O | rpt: 1)
        :param academic_degree_program_date_range: Date/Time Range (id: EDU.3 | len: 52 | use: O | rpt: 1)
        :param academic_degree_program_participation_date_range: Date/Time Range (id: EDU.4 | len: 52 | use: O | rpt: 1)
        :param academic_degree_granted_date: Date (id: EDU.5 | len: 8 | use: O | rpt: 1)
        :param school: Extended Composite Name and Identification Number for Organizations (id: EDU.6 | len: 250 | use: O | rpt: 1)
        :param school_type_code: Coded Element (id: EDU.7 | len: 250 | use: O | rpt: 1)
        :param school_address: Extended Address (id: EDU.8 | len: 250 | use: O | rpt: 1)
        :param major_field_of_study: Coded with Exceptions (id: EDU.9 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.set_id_edu = set_id_edu
        self.academic_degree = academic_degree
        self.academic_degree_program_date_range = academic_degree_program_date_range
        self.academic_degree_program_participation_date_range = (
            academic_degree_program_participation_date_range
        )
        self.academic_degree_granted_date = academic_degree_granted_date
        self.school = school
        self.school_type_code = school_type_code
        self.school_address = school_address
        self.major_field_of_study = major_field_of_study

    @property  # get EDU.1
    def set_id_edu(self) -> SI:
        """
        id: EDU.1 | len: 60 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.1
        """
        return self._c_data[0][0]

    @set_id_edu.setter  # set EDU.1
    def set_id_edu(self, si: SI):
        """
        id: EDU.1 | len: 60 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.1
        """
        self._c_data[0] = (si,)

    @property  # get EDU.2
    def academic_degree(self) -> DegreeOrLicenseOrCertificate | None:
        """
        id: EDU.2 | len: 10 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.2
        """
        return self._c_data[1][0]

    @academic_degree.setter  # set EDU.2
    def academic_degree(
        self, degree_or_license_or_certificate: DegreeOrLicenseOrCertificate | None
    ):
        """
        id: EDU.2 | len: 10 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.2
        """
        self._c_data[1] = (degree_or_license_or_certificate,)

    @property  # get EDU.3
    def academic_degree_program_date_range(self) -> DR | None:
        """
        id: EDU.3 | len: 52 | use: O | rpt: 1
        ---
        return_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.3
        """
        return self._c_data[2][0]

    @academic_degree_program_date_range.setter  # set EDU.3
    def academic_degree_program_date_range(self, dr: DR | None):
        """
        id: EDU.3 | len: 52 | use: O | rpt: 1
        ---
        param_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.3
        """
        self._c_data[2] = (dr,)

    @property  # get EDU.4
    def academic_degree_program_participation_date_range(self) -> DR | None:
        """
        id: EDU.4 | len: 52 | use: O | rpt: 1
        ---
        return_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.4
        """
        return self._c_data[3][0]

    @academic_degree_program_participation_date_range.setter  # set EDU.4
    def academic_degree_program_participation_date_range(self, dr: DR | None):
        """
        id: EDU.4 | len: 52 | use: O | rpt: 1
        ---
        param_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.4
        """
        self._c_data[3] = (dr,)

    @property  # get EDU.5
    def academic_degree_granted_date(self) -> DT | None:
        """
        id: EDU.5 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.5
        """
        return self._c_data[4][0]

    @academic_degree_granted_date.setter  # set EDU.5
    def academic_degree_granted_date(self, dt: DT | None):
        """
        id: EDU.5 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.5
        """
        self._c_data[4] = (dt,)

    @property  # get EDU.6
    def school(self) -> XON | None:
        """
        id: EDU.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.6
        """
        return self._c_data[5][0]

    @school.setter  # set EDU.6
    def school(self, xon: XON | None):
        """
        id: EDU.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.6
        """
        self._c_data[5] = (xon,)

    @property  # get EDU.7
    def school_type_code(self) -> SchoolType | None:
        """
        id: EDU.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.7
        """
        return self._c_data[6][0]

    @school_type_code.setter  # set EDU.7
    def school_type_code(self, school_type: SchoolType | None):
        """
        id: EDU.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.7
        """
        self._c_data[6] = (school_type,)

    @property  # get EDU.8
    def school_address(self) -> XAD | None:
        """
        id: EDU.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.8
        """
        return self._c_data[7][0]

    @school_address.setter  # set EDU.8
    def school_address(self, xad: XAD | None):
        """
        id: EDU.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.8
        """
        self._c_data[7] = (xad,)

    @property
    def major_field_of_study(self) -> tuple[CWE, ...] | tuple[None]:
        """
        id: EDU.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.9
        """
        return self._c_data[8]

    @major_field_of_study.setter  # set EDU.9
    def major_field_of_study(self, cwe: CWE | tuple[CWE] | None):
        """
        id: EDU.9 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EDU.9
        """
        if isinstance(cwe, tuple):
            self._c_data[8] = cwe
        else:
            self._c_data[8] = (cwe,)
