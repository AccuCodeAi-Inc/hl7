from __future__ import annotations
from ...base import DataType
from .ST import ST
from .ID import ID
from .NM import NM
from ..tables.PhoneNumber import PhoneNumber
from ..tables.TelecommunicationEquipmentType import TelecommunicationEquipmentType
from ..tables.TelecommunicationUseCode import TelecommunicationUseCode


"""
DataType - XTN
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::XTN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    XTN,
    ST, ID, NM
)

xtn = XTN(  # Extended Telecommunication Number - 
    telephone_number=None,  # ST(...) 
    telecommunication_use_code=None,  # ID(...) 
    telecommunication_equipment_type=None,  # ID(...) 
    email_address=None,  # ST(...) 
    country_code=None,  # NM(...) 
    area_or_city_code=None,  # NM(...) 
    local_number=None,  # NM(...) 
    extension=None,  # NM(...) 
    any_text=None,  # ST(...) 
    extension_prefix=None,  # ST(...) 
    speed_dial_code=None,  # ST(...) 
    unformatted_telephone_number=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::XTN TEMPLATE-----
"""


class XTN(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 850
    _hl7_id = """XTN"""
    _hl7_name = """Extended Telecommunication Number"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN"
    _c_length = (199, 3, 8, 199, 3, 5, 9, 5, 199, 4, 6, 199,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "C",)
    _c_aliases = ("XTN.1", "XTN.2", "XTN.3", "XTN.4", "XTN.5", "XTN.6", "XTN.7", "XTN.8", "XTN.9", "XTN.10", "XTN.11", "XTN.12",)
    _c_components = (ST, ID, ID, ST, NM, NM, NM, NM, ST, ST, ST, ST,)
    _c_names = ("Telephone Number", "Telecommunication Use Code", "Telecommunication Equipment Type", "Email Address", "Country Code", "Area/City Code", "Local Number", "Extension", "Any Text", "Extension Prefix", "Speed Dial Code", "Unformatted Telephone Number",)
    _c_attrs = ("telephone_number", "telecommunication_use_code", "telecommunication_equipment_type", "email_address", "country_code", "area_or_city_code", "local_number", "extension", "any_text", "extension_prefix", "speed_dial_code", "unformatted_telephone_number",)
    # fmt: on

    def __init__(
        self,
        telephone_number: PhoneNumber | ST | None = None,  # XTN.1
        telecommunication_use_code: TelecommunicationUseCode
        | ID
        | None = None,  # XTN.2
        telecommunication_equipment_type: TelecommunicationEquipmentType
        | ID
        | None = None,  # XTN.3
        email_address: ST | None = None,  # XTN.4
        country_code: NM | None = None,  # XTN.5
        area_or_city_code: NM | None = None,  # XTN.6
        local_number: NM | None = None,  # XTN.7
        extension: NM | None = None,  # XTN.8
        any_text: ST | None = None,  # XTN.9
        extension_prefix: ST | None = None,  # XTN.10
        speed_dial_code: ST | None = None,  # XTN.11
        unformatted_telephone_number: ST | None = None,  # XTN.12
    ):
        """
                Extended Telecommunication Number - `XTN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/XTN>`_


                :param telephone_number: This component has been retained for backward compatibility only as of version 2 (id: XTN.1 | len: 199 | use: B | rpt: 1)
                :param telecommunication_use_code: A code that represents a specific use of a telecommunicationnumber (id: XTN.2 | len: 3 | use: O | rpt: 1)
                :param telecommunication_equipment_type: A code that represents the type of telecommunicationequipment (id: XTN.3 | len: 8 | use: O | rpt: 1)
                :param email_address:  (id: XTN.4 | len: 199 | use: O | rpt: 1)
                :param country_code:  (id: XTN.5 | len: 3 | use: O | rpt: 1)
                :param area_or_city_code:  (id: XTN.6 | len: 5 | use: O | rpt: 1)
                :param local_number:  (id: XTN.7 | len: 9 | use: O | rpt: 1)
                :param extension: Contains comments with respect to the telephone number (id: XTN.8 | len: 5 | use: O | rpt: 1)
                :param any_text: The characters established within a companys internal telephone system network used as a prefix to the Extension component for internal dialing (id: XTN.9 | len: 199 | use: O | rpt: 1)
                :param extension_prefix: The characters established within a companys internal telephone system used in place of the (external) telephone number to facilitate calling because its length is shorter than that of the telephone number (id: XTN.10 | len: 4 | use: O | rpt: 1)
                :param speed_dial_code: An expression of the telephone number as an unparsible string (id: XTN.11 | len: 6 | use: O | rpt: 1)
                :param unformatted_telephone_number:  An expression of the telephone number as an unparsible string

        Example: |^^^^^^^^^^^1-800-Dentist|  (id: XTN.12 | len: 199 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.telephone_number = telephone_number
        self.telecommunication_use_code = telecommunication_use_code
        self.telecommunication_equipment_type = telecommunication_equipment_type
        self.email_address = email_address
        self.country_code = country_code
        self.area_or_city_code = area_or_city_code
        self.local_number = local_number
        self.extension = extension
        self.any_text = any_text
        self.extension_prefix = extension_prefix
        self.speed_dial_code = speed_dial_code
        self.unformatted_telephone_number = unformatted_telephone_number

    @property  # get XTN.1
    def telephone_number(self) -> PhoneNumber | None:
        """
                id: XTN.1 | len: 199 | use: B | rpt: 1
                ---
                This component has been retained for backward compatibility only as of version 2.3.

        Specifies the telephone number in a predetermined format that includes an optional extension, beeper number and comment.

        Format: [NNN] [(999)]999-9999 [X99999] [B99999] [C any text]
                ---
                return_type: ST: String Data
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.1
        """
        return self._c_data[0][0]

    @telephone_number.setter  # set XTN.1
    def telephone_number(self, phone_number: PhoneNumber | None):
        """
                id: XTN.1 | len: 199 | use: B | rpt: 1
                ---
                This component has been retained for backward compatibility only as of version 2.3.

        Specifies the telephone number in a predetermined format that includes an optional extension, beeper number and comment.

        Format: [NNN] [(999)]999-9999 [X99999] [B99999] [C any text]
                ---
                param_type: ST: String Data
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.1
        """
        self._c_data[0] = (phone_number,)

    @property  # get XTN.2
    def telecommunication_use_code(self) -> TelecommunicationUseCode | None:
        """
        id: XTN.2 | len: 3 | use: O | rpt: 1
        ---
        A code that represents a specific use of a telecommunicationnumber. Refer to HL7 Table 0201 - Telecommunication use code for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.2
        """
        return self._c_data[1][0]

    @telecommunication_use_code.setter  # set XTN.2
    def telecommunication_use_code(
        self, telecommunication_use_code: TelecommunicationUseCode | None
    ):
        """
        id: XTN.2 | len: 3 | use: O | rpt: 1
        ---
        A code that represents a specific use of a telecommunicationnumber. Refer to HL7 Table 0201 - Telecommunication use code for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.2
        """
        self._c_data[1] = (telecommunication_use_code,)

    @property  # get XTN.3
    def telecommunication_equipment_type(self) -> TelecommunicationEquipmentType | None:
        """
        id: XTN.3 | len: 8 | use: O | rpt: 1
        ---
        A code that represents the type of telecommunicationequipment. Refer to HL7 Table 0202 - Telecommunication equipment type for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.3
        """
        return self._c_data[2][0]

    @telecommunication_equipment_type.setter  # set XTN.3
    def telecommunication_equipment_type(
        self, telecommunication_equipment_type: TelecommunicationEquipmentType | None
    ):
        """
        id: XTN.3 | len: 8 | use: O | rpt: 1
        ---
        A code that represents the type of telecommunicationequipment. Refer to HL7 Table 0202 - Telecommunication equipment type for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.3
        """
        self._c_data[2] = (telecommunication_equipment_type,)

    @property  # get XTN.4
    def email_address(self) -> ST | None:
        """
        id: XTN.4 | len: 199 | use: O | rpt: 1
        ---
        None
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.4
        """
        return self._c_data[3][0]

    @email_address.setter  # set XTN.4
    def email_address(self, st: ST | None):
        """
        id: XTN.4 | len: 199 | use: O | rpt: 1
        ---
        None
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.4
        """
        self._c_data[3] = (st,)

    @property  # get XTN.5
    def country_code(self) -> NM | None:
        """
        id: XTN.5 | len: 3 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.5
        """
        return self._c_data[4][0]

    @country_code.setter  # set XTN.5
    def country_code(self, nm: NM | None):
        """
        id: XTN.5 | len: 3 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.5
        """
        self._c_data[4] = (nm,)

    @property  # get XTN.6
    def area_or_city_code(self) -> NM | None:
        """
        id: XTN.6 | len: 5 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.6
        """
        return self._c_data[5][0]

    @area_or_city_code.setter  # set XTN.6
    def area_or_city_code(self, nm: NM | None):
        """
        id: XTN.6 | len: 5 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.6
        """
        self._c_data[5] = (nm,)

    @property  # get XTN.7
    def local_number(self) -> NM | None:
        """
        id: XTN.7 | len: 9 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.7
        """
        return self._c_data[6][0]

    @local_number.setter  # set XTN.7
    def local_number(self, nm: NM | None):
        """
        id: XTN.7 | len: 9 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.7
        """
        self._c_data[6] = (nm,)

    @property  # get XTN.8
    def extension(self) -> NM | None:
        """
        id: XTN.8 | len: 5 | use: O | rpt: 1
        ---
        Contains comments with respect to the telephone number.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.8
        """
        return self._c_data[7][0]

    @extension.setter  # set XTN.8
    def extension(self, nm: NM | None):
        """
        id: XTN.8 | len: 5 | use: O | rpt: 1
        ---
        Contains comments with respect to the telephone number.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.8
        """
        self._c_data[7] = (nm,)

    @property  # get XTN.9
    def any_text(self) -> ST | None:
        """
        id: XTN.9 | len: 199 | use: O | rpt: 1
        ---
        The characters established within a companys internal telephone system network used as a prefix to the Extension component for internal dialing. Note that the use of Extension Prefix requires that the Extension component be valued and that digits, as well as special characters (e.g., *, #) may be used.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.9
        """
        return self._c_data[8][0]

    @any_text.setter  # set XTN.9
    def any_text(self, st: ST | None):
        """
        id: XTN.9 | len: 199 | use: O | rpt: 1
        ---
        The characters established within a companys internal telephone system network used as a prefix to the Extension component for internal dialing. Note that the use of Extension Prefix requires that the Extension component be valued and that digits, as well as special characters (e.g., *, #) may be used.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.9
        """
        self._c_data[8] = (st,)

    @property  # get XTN.10
    def extension_prefix(self) -> ST | None:
        """
        id: XTN.10 | len: 4 | use: O | rpt: 1
        ---
        The characters established within a companys internal telephone system used in place of the (external) telephone number to facilitate calling because its length is shorter than that of the telephone number. Note that digits, as well as special characters (e.g., *, #) may be used.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.10
        """
        return self._c_data[9][0]

    @extension_prefix.setter  # set XTN.10
    def extension_prefix(self, st: ST | None):
        """
        id: XTN.10 | len: 4 | use: O | rpt: 1
        ---
        The characters established within a companys internal telephone system used in place of the (external) telephone number to facilitate calling because its length is shorter than that of the telephone number. Note that digits, as well as special characters (e.g., *, #) may be used.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.10
        """
        self._c_data[9] = (st,)

    @property  # get XTN.11
    def speed_dial_code(self) -> ST | None:
        """
        id: XTN.11 | len: 6 | use: O | rpt: 1
        ---
        An expression of the telephone number as an unparsible string.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.11
        """
        return self._c_data[10][0]

    @speed_dial_code.setter  # set XTN.11
    def speed_dial_code(self, st: ST | None):
        """
        id: XTN.11 | len: 6 | use: O | rpt: 1
        ---
        An expression of the telephone number as an unparsible string.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.11
        """
        self._c_data[10] = (st,)

    @property  # get XTN.12
    def unformatted_telephone_number(self) -> ST | None:
        """
                id: XTN.12 | len: 199 | use: C | rpt: 1
                ---
                 An expression of the telephone number as an unparsible string

        Example: |^^^^^^^^^^^1-800-Dentist|
                ---
                return_type: ST: String Data
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.12
        """
        return self._c_data[11][0]

    @unformatted_telephone_number.setter  # set XTN.12
    def unformatted_telephone_number(self, st: ST | None):
        """
                id: XTN.12 | len: 199 | use: C | rpt: 1
                ---
                 An expression of the telephone number as an unparsible string

        Example: |^^^^^^^^^^^1-800-Dentist|
                ---
                param_type: ST: String Data
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XTN.12
        """
        self._c_data[11] = (st,)
