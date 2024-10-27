from __future__ import annotations
from ...base import DataType
from .ID import ID
from .ST import ST
from .NM import NM
from .HD import HD
from .IS import IS
from ..tables.AssigningAuthority import AssigningAuthority
from ..tables.CheckDigitScheme import CheckDigitScheme
from ..tables.OrganizationalNameType import OrganizationalNameType
from ..tables.IdentifierType import IdentifierType
from ..tables.NameOrAddressRepresentation import NameOrAddressRepresentation


"""
DataType - XON
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::XON TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    XON,
    ID, ST, NM, HD, IS
)

xon = XON(  # Extended Composite Name and Identification Number for Organizations - This data type is used in fields (e
    organization_name=None,  # ST(...) 
    organization_name_type_code=None,  # IS(...) 
    id_number=None,  # NM(...) 
    check_digit=None,  # NM(...) 
    check_digit_scheme=None,  # ID(...) 
    assigning_authority=None,  # HD(...) 
    identifier_type_code=None,  # ID(...) 
    assigning_facility=None,  # HD(...) 
    name_representation_code=None,  # ID(...) 
    organization_identifier=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::XON TEMPLATE-----
"""


class XON(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 567
    _hl7_id = """XON"""
    _hl7_name = """Extended Composite Name and Identification Number for Organizations"""
    _hl7_description = """This data type is used in fields (e"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON"
    _c_length = (50, 20, 4, 1, 3, 227, 5, 227, 1, 20,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "B", "O", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("XON.1", "XON.2", "XON.3", "XON.4", "XON.5", "XON.6", "XON.7", "XON.8", "XON.9", "XON.10",)
    _c_components = (ST, IS, NM, NM, ID, HD, ID, HD, ID, ST,)
    _c_names = ("Organization Name", "Organization Name Type Code", "Id Number", "Check Digit", "Check Digit Scheme", "Assigning Authority", "Identifier Type Code", "Assigning Facility", "Name Representation Code", "Organization Identifier",)
    _c_attrs = ("organization_name", "organization_name_type_code", "id_number", "check_digit", "check_digit_scheme", "assigning_authority", "identifier_type_code", "assigning_facility", "name_representation_code", "organization_identifier",)
    # fmt: on

    def __init__(
        self,
        organization_name: ST | None = None,  # XON.1
        organization_name_type_code: OrganizationalNameType | IS | None = None,  # XON.2
        id_number: NM | None = None,  # XON.3
        check_digit: NM | None = None,  # XON.4
        check_digit_scheme: CheckDigitScheme | ID | None = None,  # XON.5
        assigning_authority: AssigningAuthority | HD | None = None,  # XON.6
        identifier_type_code: IdentifierType | ID | None = None,  # XON.7
        assigning_facility: HD | None = None,  # XON.8
        name_representation_code: NameOrAddressRepresentation
        | ID
        | None = None,  # XON.9
        organization_identifier: ST | None = None,  # XON.10
    ):
        """
        Extended Composite Name and Identification Number for Organizations - `XON <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/XON>`_
        This data type is used in fields (e.g., PV2-23, NK1-13, PD1-3, OBR-44) to specify the name and ID number of an organization.

        :param organization_name: The name of the specified organization (id: XON.1 | len: 50 | use: O | rpt: 1)
        :param organization_name_type_code: A code that represents the type of name i (id: XON.2 | len: 20 | use: O | rpt: 1)
        :param id_number: This component has been retained for backward compatibility only as of v 2 (id: XON.3 | len: 4 | use: B | rpt: 1)
        :param check_digit: The check digit in this data type is not an add-on produced by the message processor (id: XON.4 | len: 1 | use: O | rpt: 1)
        :param check_digit_scheme: Contains the code identifying the check digit scheme employed (id: XON.5 | len: 3 | use: O | rpt: 1)
        :param assigning_authority: The assigning authority is a unique identifier of the system (or organization or agency or department) that creates the data (id: XON.6 | len: 227 | use: O | rpt: 1)
        :param identifier_type_code: A code corresponding to the type of identifier (id: XON.7 | len: 5 | use: O | rpt: 1)
        :param assigning_facility: The place or location identifier where the identifier was first assigned to the person (id: XON.8 | len: 227 | use: O | rpt: 1)
        :param name_representation_code: Different <name/address types> and representations of the same <name/address> should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component (id: XON.9 | len: 1 | use: O | rpt: 1)
        :param organization_identifier: This component contains the sequence of characters (the code) that uniquely identifies the item being referenced by XON (id: XON.10 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.organization_name = organization_name
        self.organization_name_type_code = organization_name_type_code
        self.id_number = id_number
        self.check_digit = check_digit
        self.check_digit_scheme = check_digit_scheme
        self.assigning_authority = assigning_authority
        self.identifier_type_code = identifier_type_code
        self.assigning_facility = assigning_facility
        self.name_representation_code = name_representation_code
        self.organization_identifier = organization_identifier

    @property  # get XON.1
    def organization_name(self) -> ST | None:
        """
        id: XON.1 | len: 50 | use: O | rpt: 1
        ---
        The name of the specified organization.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.1
        """
        return self._c_data[0][0]

    @organization_name.setter  # set XON.1
    def organization_name(self, st: ST | None):
        """
        id: XON.1 | len: 50 | use: O | rpt: 1
        ---
        The name of the specified organization.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.1
        """
        self._c_data[0] = (st,)

    @property  # get XON.2
    def organization_name_type_code(self) -> OrganizationalNameType | None:
        """
        id: XON.2 | len: 20 | use: O | rpt: 1
        ---
        A code that represents the type of name i.e., legal name, display name. Refer to User-defined Table 0204 - Organizational Name Type for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.2
        """
        return self._c_data[1][0]

    @organization_name_type_code.setter  # set XON.2
    def organization_name_type_code(
        self, organizational_name_type: OrganizationalNameType | None
    ):
        """
        id: XON.2 | len: 20 | use: O | rpt: 1
        ---
        A code that represents the type of name i.e., legal name, display name. Refer to User-defined Table 0204 - Organizational Name Type for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.2
        """
        self._c_data[1] = (organizational_name_type,)

    @property  # get XON.3
    def id_number(self) -> NM | None:
        """
        id: XON.3 | len: 4 | use: B | rpt: 1
        ---
        This component has been retained for backward compatibility only as of v 2.5. It is recommended to use component 10 Organization identifier that accommodates alphanumeric identifiers.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.3
        """
        return self._c_data[2][0]

    @id_number.setter  # set XON.3
    def id_number(self, nm: NM | None):
        """
        id: XON.3 | len: 4 | use: B | rpt: 1
        ---
        This component has been retained for backward compatibility only as of v 2.5. It is recommended to use component 10 Organization identifier that accommodates alphanumeric identifiers.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.3
        """
        self._c_data[2] = (nm,)

    @property  # get XON.4
    def check_digit(self) -> NM | None:
        """
        id: XON.4 | len: 1 | use: O | rpt: 1
        ---
        The check digit in this data type is not an add-on produced by the message processor. It is the check digit that is part of the identifying number used in the sending application. If the sending application does not include a self-generated check digit in the identifying number, this component should be valued null.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.4
        """
        return self._c_data[3][0]

    @check_digit.setter  # set XON.4
    def check_digit(self, nm: NM | None):
        """
        id: XON.4 | len: 1 | use: O | rpt: 1
        ---
        The check digit in this data type is not an add-on produced by the message processor. It is the check digit that is part of the identifying number used in the sending application. If the sending application does not include a self-generated check digit in the identifying number, this component should be valued null.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.4
        """
        self._c_data[3] = (nm,)

    @property  # get XON.5
    def check_digit_scheme(self) -> CheckDigitScheme | None:
        """
        id: XON.5 | len: 3 | use: O | rpt: 1
        ---
        Contains the code identifying the check digit scheme employed.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.5
        """
        return self._c_data[4][0]

    @check_digit_scheme.setter  # set XON.5
    def check_digit_scheme(self, check_digit_scheme: CheckDigitScheme | None):
        """
        id: XON.5 | len: 3 | use: O | rpt: 1
        ---
        Contains the code identifying the check digit scheme employed.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.5
        """
        self._c_data[4] = (check_digit_scheme,)

    @property  # get XON.6
    def assigning_authority(self) -> HD | None:
        """
        id: XON.6 | len: 227 | use: O | rpt: 1
        ---
        The assigning authority is a unique identifier of the system (or organization or agency or department) that creates the data. Assigning authorities are unique across a given HL7 implementation. Refer to User-defined Table 0363 - Assigning Authority for suggested values.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.6
        """
        return self._c_data[5][0]

    @assigning_authority.setter  # set XON.6
    def assigning_authority(self, hd: HD | None):
        """
        id: XON.6 | len: 227 | use: O | rpt: 1
        ---
        The assigning authority is a unique identifier of the system (or organization or agency or department) that creates the data. Assigning authorities are unique across a given HL7 implementation. Refer to User-defined Table 0363 - Assigning Authority for suggested values.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.6
        """
        self._c_data[5] = (hd,)

    @property  # get XON.7
    def identifier_type_code(self) -> IdentifierType | None:
        """
        id: XON.7 | len: 5 | use: O | rpt: 1
        ---
        A code corresponding to the type of identifier. In some cases, this code may be used as a qualifier to the "Assigning authority" component. Refer to HL7 Table 0203 - Identifier type for suggested values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.7
        """
        return self._c_data[6][0]

    @identifier_type_code.setter  # set XON.7
    def identifier_type_code(self, identifier_type: IdentifierType | None):
        """
        id: XON.7 | len: 5 | use: O | rpt: 1
        ---
        A code corresponding to the type of identifier. In some cases, this code may be used as a qualifier to the "Assigning authority" component. Refer to HL7 Table 0203 - Identifier type for suggested values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.7
        """
        self._c_data[6] = (identifier_type,)

    @property  # get XON.8
    def assigning_facility(self) -> HD | None:
        """
        id: XON.8 | len: 227 | use: O | rpt: 1
        ---
        The place or location identifier where the identifier was first assigned to the person. This component is not an inherent part of the identifier but rather part of the history of the identifier: as part of this data type, its existence is a convenience for certain intercommunicating systems.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.8
        """
        return self._c_data[7][0]

    @assigning_facility.setter  # set XON.8
    def assigning_facility(self, hd: HD | None):
        """
        id: XON.8 | len: 227 | use: O | rpt: 1
        ---
        The place or location identifier where the identifier was first assigned to the person. This component is not an inherent part of the identifier but rather part of the history of the identifier: as part of this data type, its existence is a convenience for certain intercommunicating systems.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.8
        """
        self._c_data[7] = (hd,)

    @property  # get XON.9
    def name_representation_code(self) -> NameOrAddressRepresentation | None:
        """
        id: XON.9 | len: 1 | use: O | rpt: 1
        ---
        Different <name/address types> and representations of the same <name/address> should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.9
        """
        return self._c_data[8][0]

    @name_representation_code.setter  # set XON.9
    def name_representation_code(
        self, name_or_address_representation: NameOrAddressRepresentation | None
    ):
        """
        id: XON.9 | len: 1 | use: O | rpt: 1
        ---
        Different <name/address types> and representations of the same <name/address> should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.9
        """
        self._c_data[8] = (name_or_address_representation,)

    @property  # get XON.10
    def organization_identifier(self) -> ST | None:
        """
        id: XON.10 | len: 20 | use: O | rpt: 1
        ---
        This component contains the sequence of characters (the code) that uniquely identifies the item being referenced by XON.1 Organization Name. This component replaces XON.3 ID Number as of v 2.5.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.10
        """
        return self._c_data[9][0]

    @organization_identifier.setter  # set XON.10
    def organization_identifier(self, st: ST | None):
        """
        id: XON.10 | len: 20 | use: O | rpt: 1
        ---
        This component contains the sequence of characters (the code) that uniquely identifies the item being referenced by XON.1 Organization Name. This component replaces XON.3 ID Number as of v 2.5.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XON.10
        """
        self._c_data[9] = (st,)
