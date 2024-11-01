from __future__ import annotations
from ...base import DataType
from .TS import TS
from .ID import ID
from .IS import IS
from .ST import ST
from .DR import DR
from .SAD import SAD
from ..tables.Street import Street
from ..tables.CensusTract import CensusTract
from ..tables.State import State
from ..tables.CountryCode import CountryCode
from ..tables.City import City
from ..tables.NameOrAddressRepresentation import NameOrAddressRepresentation
from ..tables.ZipCode import ZipCode
from ..tables.CountyOrParish import CountyOrParish
from ..tables.AddressType import AddressType


"""
DataType - XAD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::XAD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    XAD,
    TS, ID, IS, ST, DR, SAD
)

xad = XAD(  # Extended Address - This data type specifies the address of a person, place or organization plus associated information
    street_address=None,  # SAD(...) 
    other_designation=None,  # ST(...) 
    city=None,  # ST(...) 
    state_or_province=None,  # ST(...) 
    zip_or_postal_code=None,  # ST(...) 
    country=None,  # ID(...) 
    address_type=None,  # ID(...) 
    other_geographic_designation=None,  # ST(...) 
    county_or_parish_code=None,  # IS(...) 
    census_tract=None,  # IS(...) 
    address_representation_code=None,  # ID(...) 
    address_validity_range=None,  # DR(...) 
    effective_date=None,  # TS(...) 
    expiration_date=None,  # TS(...) 
)

-----END COMPOSITE_DATA_TYPE::XAD TEMPLATE-----
"""


class XAD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 631
    _hl7_id = """XAD"""
    _hl7_name = """Extended Address"""
    _hl7_description = """This data type specifies the address of a person, place or organization plus associated information"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD"
    _c_length = (184, 120, 50, 50, 12, 3, 3, 50, 20, 20, 1, 53, 26, 26,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B", "O", "O",)
    _c_aliases = ("XAD.1", "XAD.2", "XAD.3", "XAD.4", "XAD.5", "XAD.6", "XAD.7", "XAD.8", "XAD.9", "XAD.10", "XAD.11", "XAD.12", "XAD.13", "XAD.14",)
    _c_components = (SAD, ST, ST, ST, ST, ID, ID, ST, IS, IS, ID, DR, TS, TS,)
    _c_names = ("Street Address", "Other Designation", "City", "State Or Province", "Zip Or Postal Code", "Country", "Address Type", "Other Geographic Designation", "County/Parish Code", "Census Tract", "Address Representation Code", "Address Validity Range", "Effective Date", "Expiration Date",)
    _c_attrs = ("street_address", "other_designation", "city", "state_or_province", "zip_or_postal_code", "country", "address_type", "other_geographic_designation", "county_or_parish_code", "census_tract", "address_representation_code", "address_validity_range", "effective_date", "expiration_date",)
    # fmt: on

    def __init__(
        self,
        street_address: Street | SAD | tuple[Street | SAD] | None = None,  # XAD.1
        other_designation: ST | tuple[ST] | None = None,  # XAD.2
        city: City | ST | tuple[City | ST] | None = None,  # XAD.3
        state_or_province: State | ST | tuple[State | ST] | None = None,  # XAD.4
        zip_or_postal_code: ZipCode | ST | tuple[ZipCode | ST] | None = None,  # XAD.5
        country: CountryCode | ID | tuple[CountryCode | ID] | None = None,  # XAD.6
        address_type: AddressType | ID | tuple[AddressType | ID] | None = None,  # XAD.7
        other_geographic_designation: ST | tuple[ST] | None = None,  # XAD.8
        county_or_parish_code: CountyOrParish
        | IS
        | tuple[CountyOrParish | IS]
        | None = None,  # XAD.9
        census_tract: CensusTract
        | IS
        | tuple[CensusTract | IS]
        | None = None,  # XAD.10
        address_representation_code: NameOrAddressRepresentation
        | ID
        | tuple[NameOrAddressRepresentation | ID]
        | None = None,  # XAD.11
        address_validity_range: DR | tuple[DR] | None = None,  # XAD.12
        effective_date: TS | tuple[TS] | None = None,  # XAD.13
        expiration_date: TS | tuple[TS] | None = None,  # XAD.14
    ):
        """
                Extended Address - `XAD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/XAD>`_
                This data type specifies the address of a person, place or organization plus associated information.

        Example of usage for US: |1000 Hospital Lane^Ste. 123^Ann Arbor ^MI^99999^USA^B^^WA^|

                :param street_address:  (id: XAD.1 | len: 184 | use: O | rpt: 1)
                :param other_designation: Second line of address (id: XAD.2 | len: 120 | use: O | rpt: 1)
                :param city: This component specifies the city, or district or place where the addressee is located depending upon the national convention for formatting addresses for postal usage (id: XAD.3 | len: 50 | use: O | rpt: 1)
                :param state_or_province: This component specifies the state or province where the addressee is located (id: XAD.4 | len: 50 | use: O | rpt: 1)
                :param zip_or_postal_code: This component specifies the zip or postal code where the addressee is located (id: XAD.5 | len: 12 | use: O | rpt: 1)
                :param country: This component specifies the country where the addressee is locatedHL7 specifies that the 3-character (alphabetic) form of ISO 3166 be used for the country code (id: XAD.6 | len: 3 | use: O | rpt: 1)
                :param address_type: This component specifies the kind or type of address (id: XAD.7 | len: 3 | use: O | rpt: 1)
                :param other_geographic_designation: This component specifies any other geographic designation (id: XAD.8 | len: 50 | use: O | rpt: 1)
                :param county_or_parish_code: A code that represents the county in which the specified address resides (id: XAD.9 | len: 20 | use: O | rpt: 1)
                :param census_tract: A code that represents the census tract in which the specified address resides (id: XAD.10 | len: 20 | use: O | rpt: 1)
                :param address_representation_code: Different <name/address types> and representations of the same name/address should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component (id: XAD.11 | len: 1 | use: O | rpt: 1)
                :param address_validity_range: This component cannot be fully expressed (id: XAD.12 | len: 53 | use: B | rpt: 1)
                :param effective_date: The first date, if known, on which the address is valid and active (id: XAD.13 | len: 26 | use: O | rpt: 1)
                :param expiration_date: The last date, if known, on which the address is valid and active (id: XAD.14 | len: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 14
        self.street_address = street_address
        self.other_designation = other_designation
        self.city = city
        self.state_or_province = state_or_province
        self.zip_or_postal_code = zip_or_postal_code
        self.country = country
        self.address_type = address_type
        self.other_geographic_designation = other_geographic_designation
        self.county_or_parish_code = county_or_parish_code
        self.census_tract = census_tract
        self.address_representation_code = address_representation_code
        self.address_validity_range = address_validity_range
        self.effective_date = effective_date
        self.expiration_date = expiration_date

    @property  # get XAD.1
    def street_address(self) -> SAD | None:
        """
        id: XAD.1 | len: 184 | use: O | rpt: 1
        ---
        None
        ---
        return_type: SAD: Street Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.1
        """
        return self._c_data[0][0]

    @street_address.setter  # set XAD.1
    def street_address(self, sad: SAD | None):
        """
        id: XAD.1 | len: 184 | use: O | rpt: 1
        ---
        None
        ---
        param_type: SAD: Street Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.1
        """
        self._c_data[0] = (sad,)

    @property  # get XAD.2
    def other_designation(self) -> ST | None:
        """
        id: XAD.2 | len: 120 | use: O | rpt: 1
        ---
        Second line of address. In US usage, it qualifies address. Examples: Suite 555 or Fourth Floor. When referencing an institution, this component specifies the street address.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.2
        """
        return self._c_data[1][0]

    @other_designation.setter  # set XAD.2
    def other_designation(self, st: ST | None):
        """
        id: XAD.2 | len: 120 | use: O | rpt: 1
        ---
        Second line of address. In US usage, it qualifies address. Examples: Suite 555 or Fourth Floor. When referencing an institution, this component specifies the street address.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.2
        """
        self._c_data[1] = (st,)

    @property  # get XAD.3
    def city(self) -> City | None:
        """
        id: XAD.3 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the city, or district or place where the addressee is located depending upon the national convention for formatting addresses for postal usage.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.3
        """
        return self._c_data[2][0]

    @city.setter  # set XAD.3
    def city(self, city: City | None):
        """
        id: XAD.3 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the city, or district or place where the addressee is located depending upon the national convention for formatting addresses for postal usage.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.3
        """
        self._c_data[2] = (city,)

    @property  # get XAD.4
    def state_or_province(self) -> State | None:
        """
        id: XAD.4 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the state or province where the addressee is located. State or province should be represented by the official postal service codes for that country.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.4
        """
        return self._c_data[3][0]

    @state_or_province.setter  # set XAD.4
    def state_or_province(self, state: State | None):
        """
        id: XAD.4 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the state or province where the addressee is located. State or province should be represented by the official postal service codes for that country.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.4
        """
        self._c_data[3] = (state,)

    @property  # get XAD.5
    def zip_or_postal_code(self) -> ZipCode | None:
        """
        id: XAD.5 | len: 12 | use: O | rpt: 1
        ---
        This component specifies the zip or postal code where the addressee is located. Zip or postal codes should be represented by the official codes for that country. In the US, the zip code takes the form 99999[-9999], while the Canadian postal code takes the form A9A9A9, and the Australian Postcode takes the form 9999.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.5
        """
        return self._c_data[4][0]

    @zip_or_postal_code.setter  # set XAD.5
    def zip_or_postal_code(self, zip_code: ZipCode | None):
        """
        id: XAD.5 | len: 12 | use: O | rpt: 1
        ---
        This component specifies the zip or postal code where the addressee is located. Zip or postal codes should be represented by the official codes for that country. In the US, the zip code takes the form 99999[-9999], while the Canadian postal code takes the form A9A9A9, and the Australian Postcode takes the form 9999.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.5
        """
        self._c_data[4] = (zip_code,)

    @property  # get XAD.6
    def country(self) -> CountryCode | None:
        """
        id: XAD.6 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the country where the addressee is locatedHL7 specifies that the 3-character (alphabetic) form of ISO 3166 be used for the country code. Refer to HL7 Table 0399 - Country code in section 2.15.9.17 for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.6
        """
        return self._c_data[5][0]

    @country.setter  # set XAD.6
    def country(self, country_code: CountryCode | None):
        """
        id: XAD.6 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the country where the addressee is locatedHL7 specifies that the 3-character (alphabetic) form of ISO 3166 be used for the country code. Refer to HL7 Table 0399 - Country code in section 2.15.9.17 for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.6
        """
        self._c_data[5] = (country_code,)

    @property  # get XAD.7
    def address_type(self) -> AddressType | None:
        """
        id: XAD.7 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the kind or type of address. Refer to HL7 Table 0190 - Address type for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.7
        """
        return self._c_data[6][0]

    @address_type.setter  # set XAD.7
    def address_type(self, address_type: AddressType | None):
        """
        id: XAD.7 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the kind or type of address. Refer to HL7 Table 0190 - Address type for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.7
        """
        self._c_data[6] = (address_type,)

    @property  # get XAD.8
    def other_geographic_designation(self) -> ST | None:
        """
        id: XAD.8 | len: 50 | use: O | rpt: 1
        ---
        This component specifies any other geographic designation. It includes county, bioregion, SMSA, etc.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.8
        """
        return self._c_data[7][0]

    @other_geographic_designation.setter  # set XAD.8
    def other_geographic_designation(self, st: ST | None):
        """
        id: XAD.8 | len: 50 | use: O | rpt: 1
        ---
        This component specifies any other geographic designation. It includes county, bioregion, SMSA, etc.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.8
        """
        self._c_data[7] = (st,)

    @property  # get XAD.9
    def county_or_parish_code(self) -> CountyOrParish | None:
        """
        id: XAD.9 | len: 20 | use: O | rpt: 1
        ---
        A code that represents the county in which the specified address resides. User-defined Table 0289 - County/parish is used as the HL7 identifier for the user-defined table of values for this component. When this component is used to represent the county (or parish), component 8 <other geographic designation> should not duplicate it (i.e., the use of <other geographic designation> to represent the county is allowed only for the purpose of backward compatibility, and should be discouraged in this and future versions of HL7).
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.9
        """
        return self._c_data[8][0]

    @county_or_parish_code.setter  # set XAD.9
    def county_or_parish_code(self, county_or_parish: CountyOrParish | None):
        """
        id: XAD.9 | len: 20 | use: O | rpt: 1
        ---
        A code that represents the county in which the specified address resides. User-defined Table 0289 - County/parish is used as the HL7 identifier for the user-defined table of values for this component. When this component is used to represent the county (or parish), component 8 <other geographic designation> should not duplicate it (i.e., the use of <other geographic designation> to represent the county is allowed only for the purpose of backward compatibility, and should be discouraged in this and future versions of HL7).
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.9
        """
        self._c_data[8] = (county_or_parish,)

    @property  # get XAD.10
    def census_tract(self) -> CensusTract | None:
        """
        id: XAD.10 | len: 20 | use: O | rpt: 1
        ---
        A code that represents the census tract in which the specified address resides. User-defined Table 0288 - Census tract is used as the HL7 identifier for the user-defined table of values for this component.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.10
        """
        return self._c_data[9][0]

    @census_tract.setter  # set XAD.10
    def census_tract(self, census_tract: CensusTract | None):
        """
        id: XAD.10 | len: 20 | use: O | rpt: 1
        ---
        A code that represents the census tract in which the specified address resides. User-defined Table 0288 - Census tract is used as the HL7 identifier for the user-defined table of values for this component.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.10
        """
        self._c_data[9] = (census_tract,)

    @property  # get XAD.11
    def address_representation_code(self) -> NameOrAddressRepresentation | None:
        """
        id: XAD.11 | len: 1 | use: O | rpt: 1
        ---
        Different <name/address types> and representations of the same name/address should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.11
        """
        return self._c_data[10][0]

    @address_representation_code.setter  # set XAD.11
    def address_representation_code(
        self, name_or_address_representation: NameOrAddressRepresentation | None
    ):
        """
        id: XAD.11 | len: 1 | use: O | rpt: 1
        ---
        Different <name/address types> and representations of the same name/address should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.11
        """
        self._c_data[10] = (name_or_address_representation,)

    @property  # get XAD.12
    def address_validity_range(self) -> DR | None:
        """
                id: XAD.12 | len: 53 | use: B | rpt: 1
                ---
                This component cannot be fully expressed. Identified as v 2.4 erratum. Retained for backward compatibility only as of v 2.5. Refer to Effective Date and Expiration Date components.

        This component contains the start and end date/times, which define the period in which this address was valid.
                ---
                return_type: DR: Date/Time Range
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.12
        """
        return self._c_data[11][0]

    @address_validity_range.setter  # set XAD.12
    def address_validity_range(self, dr: DR | None):
        """
                id: XAD.12 | len: 53 | use: B | rpt: 1
                ---
                This component cannot be fully expressed. Identified as v 2.4 erratum. Retained for backward compatibility only as of v 2.5. Refer to Effective Date and Expiration Date components.

        This component contains the start and end date/times, which define the period in which this address was valid.
                ---
                param_type: DR: Date/Time Range
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.12
        """
        self._c_data[11] = (dr,)

    @property  # get XAD.13
    def effective_date(self) -> TS | None:
        """
        id: XAD.13 | len: 26 | use: O | rpt: 1
        ---
        The first date, if known, on which the address is valid and active.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.13
        """
        return self._c_data[12][0]

    @effective_date.setter  # set XAD.13
    def effective_date(self, ts: TS | None):
        """
        id: XAD.13 | len: 26 | use: O | rpt: 1
        ---
        The first date, if known, on which the address is valid and active.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.13
        """
        self._c_data[12] = (ts,)

    @property  # get XAD.14
    def expiration_date(self) -> TS | None:
        """
        id: XAD.14 | len: 26 | use: O | rpt: 1
        ---
        The last date, if known, on which the address is valid and active.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.14
        """
        return self._c_data[13][0]

    @expiration_date.setter  # set XAD.14
    def expiration_date(self, ts: TS | None):
        """
        id: XAD.14 | len: 26 | use: O | rpt: 1
        ---
        The last date, if known, on which the address is valid and active.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XAD.14
        """
        self._c_data[13] = (ts,)
