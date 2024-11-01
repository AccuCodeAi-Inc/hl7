from __future__ import annotations
from ...base import DataType
from .CE import CE
from .IS import IS
from .ID import ID
from .FN import FN
from .ST import ST
from .CWE import CWE
from .DR import DR
from .HD import HD
from .TS import TS
from ..tables.DegreeOrLicenseOrCertificate import DegreeOrLicenseOrCertificate
from ..tables.CheckDigitScheme import CheckDigitScheme
from ..tables.CnIdSource import CnIdSource
from ..tables.NameType import NameType
from ..tables.NameAssemblyOrder import NameAssemblyOrder
from ..tables.NameContext import NameContext
from ..tables.FirstName import FirstName
from ..tables.NameOrAddressRepresentation import NameOrAddressRepresentation
from ..tables.AssigningAuthority import AssigningAuthority
from ..tables.IdentifierType import IdentifierType


"""
DataType - XCN
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::XCN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    XCN,
    CE, IS, ID, FN, ST, CWE, DR, HD, TS
)

xcn = XCN(  # Extended Composite ID Number and Name for Persons - Example without assigning authority and assigning facility: |1234567^Everyman^Adam^A^III^DR^PHD^ADT01^^L^4^M11^MR| 
Examples with assigning authority and assigning facility: |12188^Hippocrates^Harold^H^IV^Dr^MD^^&Provider Master
    id_number=None,  # ST(...) 
    family_name=None,  # FN(...) 
    given_name=None,  # ST(...) 
    second_and_further_given_names_or_initials_thereof=None,  # ST(...) 
    suffix=None,  # ST(...) 
    prefix=None,  # ST(...) 
    degree=None,  # IS(...) 
    source_table=None,  # IS(...) 
    assigning_authority=None,  # HD(...) 
    name_type_code=None,  # ID(...) 
    identifier_check_digit=None,  # ST(...) 
    check_digit_scheme=None,  # ID(...) 
    identifier_type_code=None,  # ID(...) 
    assigning_facility=None,  # HD(...) 
    name_representation_code=None,  # ID(...) 
    name_context=None,  # CE(...) 
    name_validity_range=None,  # DR(...) 
    name_assembly_order=None,  # ID(...) 
    effective_date=None,  # TS(...) 
    expiration_date=None,  # TS(...) 
    professional_suffix=None,  # ST(...) 
    assigning_jurisdiction=None,  # CWE(...) 
    assigning_agency_or_department=None,  # CWE(...) 
)

-----END COMPOSITE_DATA_TYPE::XCN TEMPLATE-----
"""


class XCN(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 3002
    _hl7_id = """XCN"""
    _hl7_name = """Extended Composite ID Number and Name for Persons"""
    _hl7_description = """Example without assigning authority and assigning facility: |1234567^Everyman^Adam^A^III^DR^PHD^ADT01^^L^4^M11^MR| 
Examples with assigning authority and assigning facility: |12188^Hippocrates^Harold^H^IV^Dr^MD^^&Provider Master"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN"
    _c_length = (15, 194, 30, 30, 20, 20, 5, 4, 227, 1, 1, 3, 5, 227, 1, 483, 53, 1, 26, 26, 199, 705, 705,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "B", "C", "O", "O", "O", "C", "O", "O", "O", "O", "B", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("XCN.1", "XCN.2", "XCN.3", "XCN.4", "XCN.5", "XCN.6", "XCN.7", "XCN.8", "XCN.9", "XCN.10", "XCN.11", "XCN.12", "XCN.13", "XCN.14", "XCN.15", "XCN.16", "XCN.17", "XCN.18", "XCN.19", "XCN.20", "XCN.21", "XCN.22", "XCN.23",)
    _c_components = (ST, FN, ST, ST, ST, ST, IS, IS, HD, ID, ST, ID, ID, HD, ID, CE, DR, ID, TS, TS, ST, CWE, CWE,)
    _c_names = ("Id Number", "Family Name", "Given Name", "Second And Further Given Names Or Initials Thereof", "Suffix (e.g., Jr Or Iii)", "Prefix (e.g., Dr)", "Degree (e.g., Md)", "Source Table", "Assigning Authority", "Name Type Code", "Identifier Check Digit", "Check Digit Scheme", "Identifier Type Code", "Assigning Facility", "Name Representation Code", "Name Context", "Name Validity Range", "Name Assembly Order", "Effective Date", "Expiration Date", "Professional Suffix", "Assigning Jurisdiction", "Assigning Agency Or Department",)
    _c_attrs = ("id_number", "family_name", "given_name", "second_and_further_given_names_or_initials_thereof", "suffix", "prefix", "degree", "source_table", "assigning_authority", "name_type_code", "identifier_check_digit", "check_digit_scheme", "identifier_type_code", "assigning_facility", "name_representation_code", "name_context", "name_validity_range", "name_assembly_order", "effective_date", "expiration_date", "professional_suffix", "assigning_jurisdiction", "assigning_agency_or_department",)
    # fmt: on

    def __init__(
        self,
        id_number: ST | None = None,  # XCN.1
        family_name: FN | None = None,  # XCN.2
        given_name: FirstName | ST | None = None,  # XCN.3
        second_and_further_given_names_or_initials_thereof: ST | None = None,  # XCN.4
        suffix: ST | None = None,  # XCN.5
        prefix: ST | None = None,  # XCN.6
        degree: DegreeOrLicenseOrCertificate | IS | None = None,  # XCN.7
        source_table: CnIdSource | IS | None = None,  # XCN.8
        assigning_authority: AssigningAuthority | HD | None = None,  # XCN.9
        name_type_code: NameType | ID | None = None,  # XCN.10
        identifier_check_digit: ST | None = None,  # XCN.11
        check_digit_scheme: CheckDigitScheme | ID | None = None,  # XCN.12
        identifier_type_code: IdentifierType | ID | None = None,  # XCN.13
        assigning_facility: HD | None = None,  # XCN.14
        name_representation_code: NameOrAddressRepresentation
        | ID
        | None = None,  # XCN.15
        name_context: NameContext | CE | None = None,  # XCN.16
        name_validity_range: DR | None = None,  # XCN.17
        name_assembly_order: NameAssemblyOrder | ID | None = None,  # XCN.18
        effective_date: TS | None = None,  # XCN.19
        expiration_date: TS | None = None,  # XCN.20
        professional_suffix: ST | None = None,  # XCN.21
        assigning_jurisdiction: CWE | None = None,  # XCN.22
        assigning_agency_or_department: CWE | None = None,  # XCN.23
    ):
        """
                Extended Composite ID Number and Name for Persons - `XCN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/XCN>`_
                Example without assigning authority and assigning facility: |1234567^Everyman^Adam^A^III^DR^PHD^ADT01^^L^4^M11^MR|
        Examples with assigning authority and assigning facility: |12188^Hippocrates^Harold^H^IV^Dr^MD^^&Provider Master.Community Health and Hospitals&L^L^9^M10^DN^&Good Health Hospital.Community Health and Hospitals&L^A|

                :param id_number: This string refers to the coded ID according to a user-defined table, defined by the 9th component (id: XCN.1 | len: 15 | use: O | rpt: 1)
                :param family_name: This component allows full specification of the surname of a person (id: XCN.2 | len: 194 | use: O | rpt: 1)
                :param given_name: First name (id: XCN.3 | len: 30 | use: O | rpt: 1)
                :param second_and_further_given_names_or_initials_thereof: Multiple middle names may be included by separating them with spaces (id: XCN.4 | len: 30 | use: O | rpt: 1)
                :param suffix: Used to specify a name suffix (e (id: XCN.5 | len: 20 | use: O | rpt: 1)
                :param prefix: Used to specify a name prefix (e (id: XCN.6 | len: 20 | use: O | rpt: 1)
                :param degree: Retained for backward compatibility only as of v 2 (id: XCN.7 | len: 5 | use: B | rpt: 1)
                :param source_table: CN ID source is used as the HL7 identifier for the user-defined table of values for this component (id: XCN.8 | len: 4 | use: C | rpt: 1)
                :param assigning_authority: The assigning authority is a unique identifier of the system (or organization or agency of department) that creates the data (id: XCN.9 | len: 227 | use: O | rpt: 1)
                :param name_type_code: A code that represents the type of name (id: XCN.10 | len: 1 | use: O | rpt: 1)
                :param identifier_check_digit: The check digit in this data type is not an add-on produced by the message processor (id: XCN.11 | len: 1 | use: O | rpt: 1)
                :param check_digit_scheme: Contains the code identifying the check digit scheme employed (id: XCN.12 | len: 3 | use: C | rpt: 1)
                :param identifier_type_code: A code corresponding to the type of identifier (id: XCN.13 | len: 5 | use: O | rpt: 1)
                :param assigning_facility: The place or location identifier where the identifier was first assigned to the person (id: XCN.14 | len: 227 | use: O | rpt: 1)
                :param name_representation_code: Different <name/address types> and representations of the same <name/address> should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component (id: XCN.15 | len: 1 | use: O | rpt: 1)
                :param name_context: This component is used to designate the context in which a name is used (id: XCN.16 | len: 483 | use: O | rpt: 1)
                :param name_validity_range: Retained for backward compatibility only as of v 2 (id: XCN.17 | len: 53 | use: B | rpt: 1)
                :param name_assembly_order: A code that represents the preferred display order of the components of this person name (id: XCN.18 | len: 1 | use: O | rpt: 1)
                :param effective_date: The first date, if known, on which the address is valid and active (id: XCN.19 | len: 26 | use: O | rpt: 1)
                :param expiration_date: The last date, if known, on which the address is valid and active (id: XCN.20 | len: 26 | use: O | rpt: 1)
                :param professional_suffix: Used to specify an abbreviation, or a string of abbreviations denoting qualifications that support the persons profession, (e (id: XCN.21 | len: 199 | use: O | rpt: 1)
                :param assigning_jurisdiction: The geo-political body that assigned the identifier in component 1 (id: XCN.22 | len: 705 | use: O | rpt: 1)
                :param assigning_agency_or_department: The agency or department that assigned the identifier in component 1 (id: XCN.23 | len: 705 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 23
        self.id_number = id_number
        self.family_name = family_name
        self.given_name = given_name
        self.second_and_further_given_names_or_initials_thereof = (
            second_and_further_given_names_or_initials_thereof
        )
        self.suffix = suffix
        self.prefix = prefix
        self.degree = degree
        self.source_table = source_table
        self.assigning_authority = assigning_authority
        self.name_type_code = name_type_code
        self.identifier_check_digit = identifier_check_digit
        self.check_digit_scheme = check_digit_scheme
        self.identifier_type_code = identifier_type_code
        self.assigning_facility = assigning_facility
        self.name_representation_code = name_representation_code
        self.name_context = name_context
        self.name_validity_range = name_validity_range
        self.name_assembly_order = name_assembly_order
        self.effective_date = effective_date
        self.expiration_date = expiration_date
        self.professional_suffix = professional_suffix
        self.assigning_jurisdiction = assigning_jurisdiction
        self.assigning_agency_or_department = assigning_agency_or_department

    @property  # get XCN.1
    def id_number(self) -> ST | None:
        """
        id: XCN.1 | len: 15 | use: O | rpt: 1
        ---
        This string refers to the coded ID according to a user-defined table, defined by the 9th component. If the first component is present, either the source table or the assigning authority must be valued.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.1
        """
        return self._c_data[0][0]

    @id_number.setter  # set XCN.1
    def id_number(self, st: ST | None):
        """
        id: XCN.1 | len: 15 | use: O | rpt: 1
        ---
        This string refers to the coded ID according to a user-defined table, defined by the 9th component. If the first component is present, either the source table or the assigning authority must be valued.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.1
        """
        self._c_data[0] = (st,)

    @property  # get XCN.2
    def family_name(self) -> FN | None:
        """
        id: XCN.2 | len: 194 | use: O | rpt: 1
        ---
        This component allows full specification of the surname of a person. Where appropriate, it differentiates the person's own surname from that of the person's partner or spouse, in cases where the person's name may contain elements from either name. It also permits messages to distinguish the surname prefix (such as "van" or "de") from the surname root. See section 2.A.30, " FN - family name".
        ---
        return_type: FN: Family Name
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.2
        """
        return self._c_data[1][0]

    @family_name.setter  # set XCN.2
    def family_name(self, fn: FN | None):
        """
        id: XCN.2 | len: 194 | use: O | rpt: 1
        ---
        This component allows full specification of the surname of a person. Where appropriate, it differentiates the person's own surname from that of the person's partner or spouse, in cases where the person's name may contain elements from either name. It also permits messages to distinguish the surname prefix (such as "van" or "de") from the surname root. See section 2.A.30, " FN - family name".
        ---
        param_type: FN: Family Name
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.2
        """
        self._c_data[1] = (fn,)

    @property  # get XCN.3
    def given_name(self) -> FirstName | None:
        """
        id: XCN.3 | len: 30 | use: O | rpt: 1
        ---
        First name.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.3
        """
        return self._c_data[2][0]

    @given_name.setter  # set XCN.3
    def given_name(self, first_name: FirstName | None):
        """
        id: XCN.3 | len: 30 | use: O | rpt: 1
        ---
        First name.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.3
        """
        self._c_data[2] = (first_name,)

    @property  # get XCN.4
    def second_and_further_given_names_or_initials_thereof(self) -> ST | None:
        """
        id: XCN.4 | len: 30 | use: O | rpt: 1
        ---
        Multiple middle names may be included by separating them with spaces.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.4
        """
        return self._c_data[3][0]

    @second_and_further_given_names_or_initials_thereof.setter  # set XCN.4
    def second_and_further_given_names_or_initials_thereof(self, st: ST | None):
        """
        id: XCN.4 | len: 30 | use: O | rpt: 1
        ---
        Multiple middle names may be included by separating them with spaces.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.4
        """
        self._c_data[3] = (st,)

    @property  # get XCN.5
    def suffix(self) -> ST | None:
        """
        id: XCN.5 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name suffix (e.g., Jr. or III).
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.5
        """
        return self._c_data[4][0]

    @suffix.setter  # set XCN.5
    def suffix(self, st: ST | None):
        """
        id: XCN.5 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name suffix (e.g., Jr. or III).
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.5
        """
        self._c_data[4] = (st,)

    @property  # get XCN.6
    def prefix(self) -> ST | None:
        """
        id: XCN.6 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name prefix (e.g., Dr.).
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.6
        """
        return self._c_data[5][0]

    @prefix.setter  # set XCN.6
    def prefix(self, st: ST | None):
        """
        id: XCN.6 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name prefix (e.g., Dr.).
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.6
        """
        self._c_data[5] = (st,)

    @property  # get XCN.7
    def degree(self) -> DegreeOrLicenseOrCertificate | None:
        """
                id: XCN.7 | len: 5 | use: B | rpt: 1
                ---
                Retained for backward compatibility only as of v 2.5. See Professional Suffix component.

        Used to specify an educational degree (e.g., MD). Refer to User-defined Table 0360 – Degree for suggested values.
                ---
                return_type: IS: Coded value for user-defined tables
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.7
        """
        return self._c_data[6][0]

    @degree.setter  # set XCN.7
    def degree(
        self, degree_or_license_or_certificate: DegreeOrLicenseOrCertificate | None
    ):
        """
                id: XCN.7 | len: 5 | use: B | rpt: 1
                ---
                Retained for backward compatibility only as of v 2.5. See Professional Suffix component.

        Used to specify an educational degree (e.g., MD). Refer to User-defined Table 0360 – Degree for suggested values.
                ---
                param_type: IS: Coded value for user-defined tables
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.7
        """
        self._c_data[6] = (degree_or_license_or_certificate,)

    @property  # get XCN.8
    def source_table(self) -> CnIdSource | None:
        """
        id: XCN.8 | len: 4 | use: C | rpt: 1
        ---
        CN ID source is used as the HL7 identifier for the user-defined table of values for this component. Used to delineate the first component.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.8
        """
        return self._c_data[7][0]

    @source_table.setter  # set XCN.8
    def source_table(self, cn_id_source: CnIdSource | None):
        """
        id: XCN.8 | len: 4 | use: C | rpt: 1
        ---
        CN ID source is used as the HL7 identifier for the user-defined table of values for this component. Used to delineate the first component.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.8
        """
        self._c_data[7] = (cn_id_source,)

    @property  # get XCN.9
    def assigning_authority(self) -> HD | None:
        """
        id: XCN.9 | len: 227 | use: O | rpt: 1
        ---
        The assigning authority is a unique identifier of the system (or organization or agency of department) that creates the data. User-defined Table 0363 - Assigning authority is used as the HL7 identifier for the user-defined table of values for the first sub-component of the HD component, <namespace ID>.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.9
        """
        return self._c_data[8][0]

    @assigning_authority.setter  # set XCN.9
    def assigning_authority(self, hd: HD | None):
        """
        id: XCN.9 | len: 227 | use: O | rpt: 1
        ---
        The assigning authority is a unique identifier of the system (or organization or agency of department) that creates the data. User-defined Table 0363 - Assigning authority is used as the HL7 identifier for the user-defined table of values for the first sub-component of the HD component, <namespace ID>.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.9
        """
        self._c_data[8] = (hd,)

    @property  # get XCN.10
    def name_type_code(self) -> NameType | None:
        """
        id: XCN.10 | len: 1 | use: O | rpt: 1
        ---
        A code that represents the type of name. Refer to HL7 Table 0200 - Name type for valid values. See Section 2.A.88.7, " Name Type Code (ID) ".
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.10
        """
        return self._c_data[9][0]

    @name_type_code.setter  # set XCN.10
    def name_type_code(self, name_type: NameType | None):
        """
        id: XCN.10 | len: 1 | use: O | rpt: 1
        ---
        A code that represents the type of name. Refer to HL7 Table 0200 - Name type for valid values. See Section 2.A.88.7, " Name Type Code (ID) ".
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.10
        """
        self._c_data[9] = (name_type,)

    @property  # get XCN.11
    def identifier_check_digit(self) -> ST | None:
        """
        id: XCN.11 | len: 1 | use: O | rpt: 1
        ---
        The check digit in this data type is not an add-on produced by the message processor. It is the check digit that is part of the identifying number used in the sending application. If the sending application does not include a self-generated check digit in the identifying number, this component should be valued null.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.11
        """
        return self._c_data[10][0]

    @identifier_check_digit.setter  # set XCN.11
    def identifier_check_digit(self, st: ST | None):
        """
        id: XCN.11 | len: 1 | use: O | rpt: 1
        ---
        The check digit in this data type is not an add-on produced by the message processor. It is the check digit that is part of the identifying number used in the sending application. If the sending application does not include a self-generated check digit in the identifying number, this component should be valued null.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.11
        """
        self._c_data[10] = (st,)

    @property  # get XCN.12
    def check_digit_scheme(self) -> CheckDigitScheme | None:
        """
        id: XCN.12 | len: 3 | use: C | rpt: 1
        ---
        Contains the code identifying the check digit scheme employed.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.12
        """
        return self._c_data[11][0]

    @check_digit_scheme.setter  # set XCN.12
    def check_digit_scheme(self, check_digit_scheme: CheckDigitScheme | None):
        """
        id: XCN.12 | len: 3 | use: C | rpt: 1
        ---
        Contains the code identifying the check digit scheme employed.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.12
        """
        self._c_data[11] = (check_digit_scheme,)

    @property  # get XCN.13
    def identifier_type_code(self) -> IdentifierType | None:
        """
        id: XCN.13 | len: 5 | use: O | rpt: 1
        ---
        A code corresponding to the type of identifier. In some cases, this code may be used as a qualifier to the <assigning authority> component. Refer to HL7 Table 0203 - Identifier type for suggested values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.13
        """
        return self._c_data[12][0]

    @identifier_type_code.setter  # set XCN.13
    def identifier_type_code(self, identifier_type: IdentifierType | None):
        """
        id: XCN.13 | len: 5 | use: O | rpt: 1
        ---
        A code corresponding to the type of identifier. In some cases, this code may be used as a qualifier to the <assigning authority> component. Refer to HL7 Table 0203 - Identifier type for suggested values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.13
        """
        self._c_data[12] = (identifier_type,)

    @property  # get XCN.14
    def assigning_facility(self) -> HD | None:
        """
        id: XCN.14 | len: 227 | use: O | rpt: 1
        ---
        The place or location identifier where the identifier was first assigned to the person. This component is not an inherent part of the identifier but rather part of the history of the identifier: as part of this data type, its existence is a convenience for certain intercommunicating systems.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.14
        """
        return self._c_data[13][0]

    @assigning_facility.setter  # set XCN.14
    def assigning_facility(self, hd: HD | None):
        """
        id: XCN.14 | len: 227 | use: O | rpt: 1
        ---
        The place or location identifier where the identifier was first assigned to the person. This component is not an inherent part of the identifier but rather part of the history of the identifier: as part of this data type, its existence is a convenience for certain intercommunicating systems.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.14
        """
        self._c_data[13] = (hd,)

    @property  # get XCN.15
    def name_representation_code(self) -> NameOrAddressRepresentation | None:
        """
        id: XCN.15 | len: 1 | use: O | rpt: 1
        ---
        Different <name/address types> and representations of the same <name/address> should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.15
        """
        return self._c_data[14][0]

    @name_representation_code.setter  # set XCN.15
    def name_representation_code(
        self, name_or_address_representation: NameOrAddressRepresentation | None
    ):
        """
        id: XCN.15 | len: 1 | use: O | rpt: 1
        ---
        Different <name/address types> and representations of the same <name/address> should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.15
        """
        self._c_data[14] = (name_or_address_representation,)

    @property  # get XCN.16
    def name_context(self) -> CE | None:
        """
        id: XCN.16 | len: 483 | use: O | rpt: 1
        ---
        This component is used to designate the context in which a name is used. The main use case is in Australian healthcare for indigenous patients who prefer to use different names when attending different healthcare institutions. Another use case occurs in the US where health practitioners can be licensed under slightly different names and the reporting of the correct name is vital for administrative purposes. Refer to User-defined Table 0448 - Name context for suggested values.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.16
        """
        return self._c_data[15][0]

    @name_context.setter  # set XCN.16
    def name_context(self, ce: CE | None):
        """
        id: XCN.16 | len: 483 | use: O | rpt: 1
        ---
        This component is used to designate the context in which a name is used. The main use case is in Australian healthcare for indigenous patients who prefer to use different names when attending different healthcare institutions. Another use case occurs in the US where health practitioners can be licensed under slightly different names and the reporting of the correct name is vital for administrative purposes. Refer to User-defined Table 0448 - Name context for suggested values.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.16
        """
        self._c_data[15] = (ce,)

    @property  # get XCN.17
    def name_validity_range(self) -> DR | None:
        """
                id: XCN.17 | len: 53 | use: B | rpt: 1
                ---
                Retained for backward compatibility only as of v 2.5. Refer to XCN.19 Effective Date and XCN.20 Expiration Date instead. This component cannot be fully expressed and has been identified as v 2.4 erratum.

        This component contains the start and end date/times that define the period during which this name was valid. See section 2.A.20, " DR - date/time range " for description of subcomponents.
                ---
                return_type: DR: Date/Time Range
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.17
        """
        return self._c_data[16][0]

    @name_validity_range.setter  # set XCN.17
    def name_validity_range(self, dr: DR | None):
        """
                id: XCN.17 | len: 53 | use: B | rpt: 1
                ---
                Retained for backward compatibility only as of v 2.5. Refer to XCN.19 Effective Date and XCN.20 Expiration Date instead. This component cannot be fully expressed and has been identified as v 2.4 erratum.

        This component contains the start and end date/times that define the period during which this name was valid. See section 2.A.20, " DR - date/time range " for description of subcomponents.
                ---
                param_type: DR: Date/Time Range
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.17
        """
        self._c_data[16] = (dr,)

    @property  # get XCN.18
    def name_assembly_order(self) -> NameAssemblyOrder | None:
        """
        id: XCN.18 | len: 1 | use: O | rpt: 1
        ---
        A code that represents the preferred display order of the components of this person name. Refer to HL7 Table 0444 - Name Assembly Order for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.18
        """
        return self._c_data[17][0]

    @name_assembly_order.setter  # set XCN.18
    def name_assembly_order(self, name_assembly_order: NameAssemblyOrder | None):
        """
        id: XCN.18 | len: 1 | use: O | rpt: 1
        ---
        A code that represents the preferred display order of the components of this person name. Refer to HL7 Table 0444 - Name Assembly Order for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.18
        """
        self._c_data[17] = (name_assembly_order,)

    @property  # get XCN.19
    def effective_date(self) -> TS | None:
        """
        id: XCN.19 | len: 26 | use: O | rpt: 1
        ---
        The first date, if known, on which the address is valid and active.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.19
        """
        return self._c_data[18][0]

    @effective_date.setter  # set XCN.19
    def effective_date(self, ts: TS | None):
        """
        id: XCN.19 | len: 26 | use: O | rpt: 1
        ---
        The first date, if known, on which the address is valid and active.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.19
        """
        self._c_data[18] = (ts,)

    @property  # get XCN.20
    def expiration_date(self) -> TS | None:
        """
        id: XCN.20 | len: 26 | use: O | rpt: 1
        ---
        The last date, if known, on which the address is valid and active.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.20
        """
        return self._c_data[19][0]

    @expiration_date.setter  # set XCN.20
    def expiration_date(self, ts: TS | None):
        """
        id: XCN.20 | len: 26 | use: O | rpt: 1
        ---
        The last date, if known, on which the address is valid and active.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.20
        """
        self._c_data[19] = (ts,)

    @property  # get XCN.21
    def professional_suffix(self) -> ST | None:
        """
        id: XCN.21 | len: 199 | use: O | rpt: 1
        ---
        Used to specify an abbreviation, or a string of abbreviations denoting qualifications that support the persons profession, (e.g., licenses, certificates, degrees, affiliations with professional societies, etc.). The Professional Suffix normally follows the Family Name when the Person Name is used for display purposes. Please note that this component is an unformatted string and is used for display purposes only. Detailed information regarding the contents of Professional Suffix is obtained using appropriate segments in Chapter 15, Personnel Management.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.21
        """
        return self._c_data[20][0]

    @professional_suffix.setter  # set XCN.21
    def professional_suffix(self, st: ST | None):
        """
        id: XCN.21 | len: 199 | use: O | rpt: 1
        ---
        Used to specify an abbreviation, or a string of abbreviations denoting qualifications that support the persons profession, (e.g., licenses, certificates, degrees, affiliations with professional societies, etc.). The Professional Suffix normally follows the Family Name when the Person Name is used for display purposes. Please note that this component is an unformatted string and is used for display purposes only. Detailed information regarding the contents of Professional Suffix is obtained using appropriate segments in Chapter 15, Personnel Management.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.21
        """
        self._c_data[20] = (st,)

    @property  # get XCN.22
    def assigning_jurisdiction(self) -> CWE | None:
        """
        id: XCN.22 | len: 705 | use: O | rpt: 1
        ---
        The geo-political body that assigned the identifier in component 1.
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.22
        """
        return self._c_data[21][0]

    @assigning_jurisdiction.setter  # set XCN.22
    def assigning_jurisdiction(self, cwe: CWE | None):
        """
        id: XCN.22 | len: 705 | use: O | rpt: 1
        ---
        The geo-political body that assigned the identifier in component 1.
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.22
        """
        self._c_data[21] = (cwe,)

    @property  # get XCN.23
    def assigning_agency_or_department(self) -> CWE | None:
        """
        id: XCN.23 | len: 705 | use: O | rpt: 1
        ---
        The agency or department that assigned the identifier in component 1.
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.23
        """
        return self._c_data[22][0]

    @assigning_agency_or_department.setter  # set XCN.23
    def assigning_agency_or_department(self, cwe: CWE | None):
        """
        id: XCN.23 | len: 705 | use: O | rpt: 1
        ---
        The agency or department that assigned the identifier in component 1.
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XCN.23
        """
        self._c_data[22] = (cwe,)
