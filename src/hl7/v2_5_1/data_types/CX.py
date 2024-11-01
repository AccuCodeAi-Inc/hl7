from __future__ import annotations
from ...base import DataType
from .DT import DT
from .HD import HD
from .CWE import CWE
from .ST import ST
from .ID import ID
from ..tables.CheckDigitScheme import CheckDigitScheme
from ..tables.AssigningAuthority import AssigningAuthority
from ..tables.IdentifierType import IdentifierType


"""
DataType - CX
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CX TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CX,
    DT, HD, CWE, ST, ID
)

cx = CX(  # Extended Composite ID with Check Digit - This data type is used for specifying an identifier with its associated administrative detail
    id_number=st,  # ST(...)  # Required.
    check_digit=None,  # ST(...) 
    check_digit_scheme=None,  # ID(...) 
    assigning_authority=None,  # HD(...) 
    identifier_type_code=None,  # ID(...) 
    assigning_facility=None,  # HD(...) 
    effective_date=None,  # DT(...) 
    expiration_date=None,  # DT(...) 
    assigning_jurisdiction=None,  # CWE(...) 
    assigning_agency_or_department=None,  # CWE(...) 
)

-----END COMPOSITE_DATA_TYPE::CX TEMPLATE-----
"""


class CX(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 1913
    _hl7_id = """CX"""
    _hl7_name = """Extended Composite ID with Check Digit"""
    _hl7_description = """This data type is used for specifying an identifier with its associated administrative detail"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX"
    _c_length = (15, 1, 3, 227, 5, 227, 8, 8, 705, 705,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("CX.1", "CX.2", "CX.3", "CX.4", "CX.5", "CX.6", "CX.7", "CX.8", "CX.9", "CX.10",)
    _c_components = (ST, ST, ID, HD, ID, HD, DT, DT, CWE, CWE,)
    _c_names = ("Id Number", "Check Digit", "Check Digit Scheme", "Assigning Authority", "Identifier Type Code", "Assigning Facility", "Effective Date", "Expiration Date", "Assigning Jurisdiction", "Assigning Agency Or Department",)
    _c_attrs = ("id_number", "check_digit", "check_digit_scheme", "assigning_authority", "identifier_type_code", "assigning_facility", "effective_date", "expiration_date", "assigning_jurisdiction", "assigning_agency_or_department",)
    # fmt: on

    def __init__(
        self,
        id_number: ST | tuple[ST, ...],  # CX.1
        check_digit: ST | tuple[ST, ...] | None = None,  # CX.2
        check_digit_scheme: CheckDigitScheme
        | ID
        | tuple[CheckDigitScheme | ID, ...]
        | None = None,  # CX.3
        assigning_authority: AssigningAuthority
        | HD
        | tuple[AssigningAuthority | HD, ...]
        | None = None,  # CX.4
        identifier_type_code: IdentifierType
        | ID
        | tuple[IdentifierType | ID, ...]
        | None = None,  # CX.5
        assigning_facility: HD | tuple[HD, ...] | None = None,  # CX.6
        effective_date: DT | tuple[DT, ...] | None = None,  # CX.7
        expiration_date: DT | tuple[DT, ...] | None = None,  # CX.8
        assigning_jurisdiction: CWE | tuple[CWE, ...] | None = None,  # CX.9
        assigning_agency_or_department: CWE | tuple[CWE, ...] | None = None,  # CX.10
    ):
        """
                Extended Composite ID with Check Digit - `CX <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CX>`_
                This data type is used for specifying an identifier with its associated administrative detail.

        Example: |1234567^4^M11^ADT01^MR^Good Health Hospital|

                :param id_number: The value of the identifier itself (id: CX.1 | len: 15 | use: R | rpt: 1)
                :param check_digit: The check digit in this data type is not an add-on produced by the message processor (id: CX.2 | len: 1 | use: O | rpt: 1)
                :param check_digit_scheme: Contains the code identifying the check digit scheme employed (id: CX.3 | len: 3 | use: O | rpt: 1)
                :param assigning_authority: The assigning authority is a unique name of the system (or organization or agency or department) that creates the data (id: CX.4 | len: 227 | use: O | rpt: 1)
                :param identifier_type_code: A code corresponding to the type of identifier (id: CX.5 | len: 5 | use: O | rpt: 1)
                :param assigning_facility: The place or location identifier where the identifier was first assigned to the patient (id: CX.6 | len: 227 | use: O | rpt: 1)
                :param effective_date: The first date, if known, on which the identifier is valid and active (id: CX.7 | len: 8 | use: O | rpt: 1)
                :param expiration_date: The last date, if known, on which the identifier is valid and active (id: CX.8 | len: 8 | use: O | rpt: 1)
                :param assigning_jurisdiction: The geo-political body that assigned the identifier in component 1 (id: CX.9 | len: 705 | use: O | rpt: 1)
                :param assigning_agency_or_department: The agency or department that assigned the identifier in component 1 (id: CX.10 | len: 705 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.id_number = id_number
        self.check_digit = check_digit
        self.check_digit_scheme = check_digit_scheme
        self.assigning_authority = assigning_authority
        self.identifier_type_code = identifier_type_code
        self.assigning_facility = assigning_facility
        self.effective_date = effective_date
        self.expiration_date = expiration_date
        self.assigning_jurisdiction = assigning_jurisdiction
        self.assigning_agency_or_department = assigning_agency_or_department

    @property  # get CX.1
    def id_number(self) -> ST:
        """
        id: CX.1 | len: 15 | use: R | rpt: 1
        ---
        The value of the identifier itself.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.1
        """
        return self._c_data[0][0]

    @id_number.setter  # set CX.1
    def id_number(self, st: ST):
        """
        id: CX.1 | len: 15 | use: R | rpt: 1
        ---
        The value of the identifier itself.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.1
        """
        self._c_data[0] = (st,)

    @property  # get CX.2
    def check_digit(self) -> ST | None:
        """
        id: CX.2 | len: 1 | use: O | rpt: 1
        ---
        The check digit in this data type is not an add-on produced by the message processor. It is the check digit that is part of the identifying number used in the sending application. If the sending application does not include a self-generated check digit in the identifying number, this component should be valued null.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.2
        """
        return self._c_data[1][0]

    @check_digit.setter  # set CX.2
    def check_digit(self, st: ST | None):
        """
        id: CX.2 | len: 1 | use: O | rpt: 1
        ---
        The check digit in this data type is not an add-on produced by the message processor. It is the check digit that is part of the identifying number used in the sending application. If the sending application does not include a self-generated check digit in the identifying number, this component should be valued null.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.2
        """
        self._c_data[1] = (st,)

    @property  # get CX.3
    def check_digit_scheme(self) -> CheckDigitScheme | None:
        """
        id: CX.3 | len: 3 | use: O | rpt: 1
        ---
        Contains the code identifying the check digit scheme employed.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.3
        """
        return self._c_data[2][0]

    @check_digit_scheme.setter  # set CX.3
    def check_digit_scheme(self, check_digit_scheme: CheckDigitScheme | None):
        """
        id: CX.3 | len: 3 | use: O | rpt: 1
        ---
        Contains the code identifying the check digit scheme employed.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.3
        """
        self._c_data[2] = (check_digit_scheme,)

    @property  # get CX.4
    def assigning_authority(self) -> HD | None:
        """
        id: CX.4 | len: 227 | use: O | rpt: 1
        ---
        The assigning authority is a unique name of the system (or organization or agency or department) that creates the data. . Refer to User-defined Table 0363 - Assigning authority for suggested values.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.4
        """
        return self._c_data[3][0]

    @assigning_authority.setter  # set CX.4
    def assigning_authority(self, hd: HD | None):
        """
        id: CX.4 | len: 227 | use: O | rpt: 1
        ---
        The assigning authority is a unique name of the system (or organization or agency or department) that creates the data. . Refer to User-defined Table 0363 - Assigning authority for suggested values.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.4
        """
        self._c_data[3] = (hd,)

    @property  # get CX.5
    def identifier_type_code(self) -> IdentifierType | None:
        """
        id: CX.5 | len: 5 | use: O | rpt: 1
        ---
        A code corresponding to the type of identifier. In some cases, this code may be used as a qualifier to the Assigning authority component. Refer to HL7 Table 0203 - Identifier type for suggested values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.5
        """
        return self._c_data[4][0]

    @identifier_type_code.setter  # set CX.5
    def identifier_type_code(self, identifier_type: IdentifierType | None):
        """
        id: CX.5 | len: 5 | use: O | rpt: 1
        ---
        A code corresponding to the type of identifier. In some cases, this code may be used as a qualifier to the Assigning authority component. Refer to HL7 Table 0203 - Identifier type for suggested values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.5
        """
        self._c_data[4] = (identifier_type,)

    @property  # get CX.6
    def assigning_facility(self) -> HD | None:
        """
        id: CX.6 | len: 227 | use: O | rpt: 1
        ---
        The place or location identifier where the identifier was first assigned to the patient. This component is not an inherent part of the identifier but rather part of the history of the identifier: as part of this data type, its existence is a convenience for certain intercommunicating systems.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.6
        """
        return self._c_data[5][0]

    @assigning_facility.setter  # set CX.6
    def assigning_facility(self, hd: HD | None):
        """
        id: CX.6 | len: 227 | use: O | rpt: 1
        ---
        The place or location identifier where the identifier was first assigned to the patient. This component is not an inherent part of the identifier but rather part of the history of the identifier: as part of this data type, its existence is a convenience for certain intercommunicating systems.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.6
        """
        self._c_data[5] = (hd,)

    @property  # get CX.7
    def effective_date(self) -> DT | None:
        """
        id: CX.7 | len: 8 | use: O | rpt: 1
        ---
        The first date, if known, on which the identifier is valid and active.
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.7
        """
        return self._c_data[6][0]

    @effective_date.setter  # set CX.7
    def effective_date(self, dt: DT | None):
        """
        id: CX.7 | len: 8 | use: O | rpt: 1
        ---
        The first date, if known, on which the identifier is valid and active.
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.7
        """
        self._c_data[6] = (dt,)

    @property  # get CX.8
    def expiration_date(self) -> DT | None:
        """
        id: CX.8 | len: 8 | use: O | rpt: 1
        ---
        The last date, if known, on which the identifier is valid and active.
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.8
        """
        return self._c_data[7][0]

    @expiration_date.setter  # set CX.8
    def expiration_date(self, dt: DT | None):
        """
        id: CX.8 | len: 8 | use: O | rpt: 1
        ---
        The last date, if known, on which the identifier is valid and active.
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.8
        """
        self._c_data[7] = (dt,)

    @property  # get CX.9
    def assigning_jurisdiction(self) -> CWE | None:
        """
        id: CX.9 | len: 705 | use: O | rpt: 1
        ---
        The geo-political body that assigned the identifier in component 1.
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.9
        """
        return self._c_data[8][0]

    @assigning_jurisdiction.setter  # set CX.9
    def assigning_jurisdiction(self, cwe: CWE | None):
        """
        id: CX.9 | len: 705 | use: O | rpt: 1
        ---
        The geo-political body that assigned the identifier in component 1.
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.9
        """
        self._c_data[8] = (cwe,)

    @property  # get CX.10
    def assigning_agency_or_department(self) -> CWE | None:
        """
        id: CX.10 | len: 705 | use: O | rpt: 1
        ---
        The agency or department that assigned the identifier in component 1.
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.10
        """
        return self._c_data[9][0]

    @assigning_agency_or_department.setter  # set CX.10
    def assigning_agency_or_department(self, cwe: CWE | None):
        """
        id: CX.10 | len: 705 | use: O | rpt: 1
        ---
        The agency or department that assigned the identifier in component 1.
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CX.10
        """
        self._c_data[9] = (cwe,)
