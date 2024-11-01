from __future__ import annotations
from ...base import DataType
from .ID import ID
from .ST import ST
from ..tables.CountryCode import CountryCode
from ..tables.AddressType import AddressType


"""
DataType - AD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::AD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    AD,
    ID, ST
)

ad = AD(  # Address - This data type specifies the address of a person, place or organization
    street_address=None,  # ST(...) 
    other_designation=None,  # ST(...) 
    city=None,  # ST(...) 
    state_or_province=None,  # ST(...) 
    zip_or_postal_code=None,  # ST(...) 
    country=None,  # ID(...) 
    address_type=None,  # ID(...) 
    other_geographic_designation=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::AD TEMPLATE-----
"""


class AD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 415
    _hl7_id = """AD"""
    _hl7_name = """Address"""
    _hl7_description = """This data type specifies the address of a person, place or organization"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD"
    _c_length = (120, 120, 50, 50, 12, 3, 3, 50,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("AD.1", "AD.2", "AD.3", "AD.4", "AD.5", "AD.6", "AD.7", "AD.8",)
    _c_components = (ST, ST, ST, ST, ST, ID, ID, ST,)
    _c_names = ("Street Address", "Other Designation", "City", "State Or Province", "Zip Or Postal Code", "Country", "Address Type", "Other Geographic Designation",)
    _c_attrs = ("street_address", "other_designation", "city", "state_or_province", "zip_or_postal_code", "country", "address_type", "other_geographic_designation",)
    # fmt: on

    def __init__(
        self,
        street_address: ST | tuple[ST] | None = None,  # AD.1
        other_designation: ST | tuple[ST] | None = None,  # AD.2
        city: ST | tuple[ST] | None = None,  # AD.3
        state_or_province: ST | tuple[ST] | None = None,  # AD.4
        zip_or_postal_code: ST | tuple[ST] | None = None,  # AD.5
        country: CountryCode | ID | tuple[CountryCode | ID] | None = None,  # AD.6
        address_type: AddressType | ID | tuple[AddressType | ID] | None = None,  # AD.7
        other_geographic_designation: ST | tuple[ST] | None = None,  # AD.8
    ):
        """
                Address - `AD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AD>`_
                This data type specifies the address of a person, place or organization.

        Example: |10 ASH LN^#3^LIMA^OH^48132|

                :param street_address: This component specifies the street or mailing address of a person or institution (id: AD.1 | len: 120 | use: O | rpt: 1)
                :param other_designation: This component specifies the second line of address (id: AD.2 | len: 120 | use: O | rpt: 1)
                :param city: This component specifies the city, district or place where the addressee is located depending upon the national convention for formatting addresses for postal usage (id: AD.3 | len: 50 | use: O | rpt: 1)
                :param state_or_province: This component specifies the state or province where the addressee is located (id: AD.4 | len: 50 | use: O | rpt: 1)
                :param zip_or_postal_code: This component specifies the zip or postal code where the addressee is located (id: AD.5 | len: 12 | use: O | rpt: 1)
                :param country: This component specifies the country where the addressee is located (id: AD.6 | len: 3 | use: O | rpt: 1)
                :param address_type: This component specifies the kind or type of address (id: AD.7 | len: 3 | use: O | rpt: 1)
                :param other_geographic_designation: This component specifies any other geographic designation that may be necessary (id: AD.8 | len: 50 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.street_address = street_address
        self.other_designation = other_designation
        self.city = city
        self.state_or_province = state_or_province
        self.zip_or_postal_code = zip_or_postal_code
        self.country = country
        self.address_type = address_type
        self.other_geographic_designation = other_geographic_designation

    @property  # get AD.1
    def street_address(self) -> ST | None:
        """
        id: AD.1 | len: 120 | use: O | rpt: 1
        ---
        This component specifies the street or mailing address of a person or institution. When referencing an institution, this first component is used to specify the institution name. When used in connection with a person, this component specifies the first line of the address.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.1
        """
        return self._c_data[0][0]

    @street_address.setter  # set AD.1
    def street_address(self, st: ST | None):
        """
        id: AD.1 | len: 120 | use: O | rpt: 1
        ---
        This component specifies the street or mailing address of a person or institution. When referencing an institution, this first component is used to specify the institution name. When used in connection with a person, this component specifies the first line of the address.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.1
        """
        self._c_data[0] = (st,)

    @property  # get AD.2
    def other_designation(self) -> ST | None:
        """
        id: AD.2 | len: 120 | use: O | rpt: 1
        ---
        This component specifies the second line of address. In general, it qualifies address. Examples: Suite 555 or Fourth Floor. When referencing an institution, this component specifies the street address.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.2
        """
        return self._c_data[1][0]

    @other_designation.setter  # set AD.2
    def other_designation(self, st: ST | None):
        """
        id: AD.2 | len: 120 | use: O | rpt: 1
        ---
        This component specifies the second line of address. In general, it qualifies address. Examples: Suite 555 or Fourth Floor. When referencing an institution, this component specifies the street address.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.2
        """
        self._c_data[1] = (st,)

    @property  # get AD.3
    def city(self) -> ST | None:
        """
        id: AD.3 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the city, district or place where the addressee is located depending upon the national convention for formatting addresses for postal usage.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.3
        """
        return self._c_data[2][0]

    @city.setter  # set AD.3
    def city(self, st: ST | None):
        """
        id: AD.3 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the city, district or place where the addressee is located depending upon the national convention for formatting addresses for postal usage.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.3
        """
        self._c_data[2] = (st,)

    @property  # get AD.4
    def state_or_province(self) -> ST | None:
        """
        id: AD.4 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the state or province where the addressee is located. State or province should be represented by the official postal service codes for that country.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.4
        """
        return self._c_data[3][0]

    @state_or_province.setter  # set AD.4
    def state_or_province(self, st: ST | None):
        """
        id: AD.4 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the state or province where the addressee is located. State or province should be represented by the official postal service codes for that country.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.4
        """
        self._c_data[3] = (st,)

    @property  # get AD.5
    def zip_or_postal_code(self) -> ST | None:
        """
        id: AD.5 | len: 12 | use: O | rpt: 1
        ---
        This component specifies the zip or postal code where the addressee is located. Zip or postal codes should be represented by the official codes for that country. In the US, the zip code takes the form 99999[-9999], while the Canadian postal code takes the form A9A9A9 and the Australian Postcode takes the form 9999.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.5
        """
        return self._c_data[4][0]

    @zip_or_postal_code.setter  # set AD.5
    def zip_or_postal_code(self, st: ST | None):
        """
        id: AD.5 | len: 12 | use: O | rpt: 1
        ---
        This component specifies the zip or postal code where the addressee is located. Zip or postal codes should be represented by the official codes for that country. In the US, the zip code takes the form 99999[-9999], while the Canadian postal code takes the form A9A9A9 and the Australian Postcode takes the form 9999.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.5
        """
        self._c_data[4] = (st,)

    @property  # get AD.6
    def country(self) -> CountryCode | None:
        """
        id: AD.6 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the country where the addressee is located. HL7 specifies that the 3-character (alphabetic) form of ISO 3166 be used for the country code. Refer to HL7 Table 0399 - Country Code in section 2.15.9.17 for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.6
        """
        return self._c_data[5][0]

    @country.setter  # set AD.6
    def country(self, country_code: CountryCode | None):
        """
        id: AD.6 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the country where the addressee is located. HL7 specifies that the 3-character (alphabetic) form of ISO 3166 be used for the country code. Refer to HL7 Table 0399 - Country Code in section 2.15.9.17 for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.6
        """
        self._c_data[5] = (country_code,)

    @property  # get AD.7
    def address_type(self) -> AddressType | None:
        """
        id: AD.7 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the kind or type of address. Refer to HL7 Table 0190 - Address Type for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.7
        """
        return self._c_data[6][0]

    @address_type.setter  # set AD.7
    def address_type(self, address_type: AddressType | None):
        """
        id: AD.7 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the kind or type of address. Refer to HL7 Table 0190 - Address Type for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.7
        """
        self._c_data[6] = (address_type,)

    @property  # get AD.8
    def other_geographic_designation(self) -> ST | None:
        """
        id: AD.8 | len: 50 | use: O | rpt: 1
        ---
        This component specifies any other geographic designation that may be necessary. It includes county, bioregion, SMSA, etc.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.8
        """
        return self._c_data[7][0]

    @other_geographic_designation.setter  # set AD.8
    def other_geographic_designation(self, st: ST | None):
        """
        id: AD.8 | len: 50 | use: O | rpt: 1
        ---
        This component specifies any other geographic designation that may be necessary. It includes county, bioregion, SMSA, etc.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AD.8
        """
        self._c_data[7] = (st,)
