from __future__ import annotations
from ...base import DataType
from .ST import ST
from .IS import IS
from .ID import ID
from .HD import HD
from ..tables.LocationStatus import LocationStatus
from ..tables.Floor import Floor
from ..tables.AddressType import AddressType
from ..tables.PersonLocationType import PersonLocationType
from ..tables.Building import Building
from ..tables.Bed import Bed
from ..tables.PointOfCare import PointOfCare
from ..tables.CountryCode import CountryCode
from ..tables.Room import Room


"""
DataType - LA2
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::LA2 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    LA2,
    ST, IS, ID, HD
)

la2 = LA2(  # Location with Address Variation 2 - Specifies a location and its address
    point_of_care=None,  # IS(...) 
    room=None,  # IS(...) 
    bed=None,  # IS(...) 
    facility=None,  # HD(...) 
    location_status=None,  # IS(...) 
    patient_location_type=None,  # IS(...) 
    building=None,  # IS(...) 
    floor=None,  # IS(...) 
    street_address=None,  # ST(...) 
    other_designation=None,  # ST(...) 
    city=None,  # ST(...) 
    state_or_province=None,  # ST(...) 
    zip_or_postal_code=None,  # ST(...) 
    country=None,  # ID(...) 
    address_type=None,  # ID(...) 
    other_geographic_designation=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::LA2 TEMPLATE-----
"""


class LA2(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 790
    _hl7_id = """LA2"""
    _hl7_name = """Location with Address Variation 2"""
    _hl7_description = """Specifies a location and its address"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2"
    _c_length = (20, 20, 20, 227, 20, 20, 20, 20, 120, 120, 50, 50, 12, 3, 3, 50,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("LA2.1", "LA2.2", "LA2.3", "LA2.4", "LA2.5", "LA2.6", "LA2.7", "LA2.8", "LA2.9", "LA2.10", "LA2.11", "LA2.12", "LA2.13", "LA2.14", "LA2.15", "LA2.16",)
    _c_components = (IS, IS, IS, HD, IS, IS, IS, IS, ST, ST, ST, ST, ST, ID, ID, ST,)
    _c_names = ("Point Of Care", "Room", "Bed", "Facility", "Location Status", "Patient Location Type", "Building", "Floor", "Street Address", "Other Designation", "City", "State Or Province", "Zip Or Postal Code", "Country", "Address Type", "Other Geographic Designation",)
    _c_attrs = ("point_of_care", "room", "bed", "facility", "location_status", "patient_location_type", "building", "floor", "street_address", "other_designation", "city", "state_or_province", "zip_or_postal_code", "country", "address_type", "other_geographic_designation",)
    # fmt: on

    def __init__(
        self,
        point_of_care: PointOfCare
        | IS
        | tuple[PointOfCare | IS, ...]
        | None = None,  # LA2.1
        room: Room | IS | tuple[Room | IS, ...] | None = None,  # LA2.2
        bed: Bed | IS | tuple[Bed | IS, ...] | None = None,  # LA2.3
        facility: HD | tuple[HD, ...] | None = None,  # LA2.4
        location_status: LocationStatus
        | IS
        | tuple[LocationStatus | IS, ...]
        | None = None,  # LA2.5
        patient_location_type: PersonLocationType
        | IS
        | tuple[PersonLocationType | IS, ...]
        | None = None,  # LA2.6
        building: Building | IS | tuple[Building | IS, ...] | None = None,  # LA2.7
        floor: Floor | IS | tuple[Floor | IS, ...] | None = None,  # LA2.8
        street_address: ST | tuple[ST, ...] | None = None,  # LA2.9
        other_designation: ST | tuple[ST, ...] | None = None,  # LA2.10
        city: ST | tuple[ST, ...] | None = None,  # LA2.11
        state_or_province: ST | tuple[ST, ...] | None = None,  # LA2.12
        zip_or_postal_code: ST | tuple[ST, ...] | None = None,  # LA2.13
        country: CountryCode
        | ID
        | tuple[CountryCode | ID, ...]
        | None = None,  # LA2.14
        address_type: AddressType
        | ID
        | tuple[AddressType | ID, ...]
        | None = None,  # LA2.15
        other_geographic_designation: ST | tuple[ST, ...] | None = None,  # LA2.16
    ):
        """
        Location with Address Variation 2 - `LA2 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LA2>`_
        Specifies a location and its address.

        :param point_of_care: This component specifies the code for the point where patient care is administered (id: LA2.1 | len: 20 | use: O | rpt: 1)
        :param room: This component specifies the code for the patient room (id: LA2.2 | len: 20 | use: O | rpt: 1)
        :param bed: This component specifies the code for the patient's bed (id: LA2.3 | len: 20 | use: O | rpt: 1)
        :param facility: This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise (id: LA2.4 | len: 227 | use: O | rpt: 1)
        :param location_status: This component specifies the code for the status or availability of the location (id: LA2.5 | len: 20 | use: O | rpt: 1)
        :param patient_location_type: Person location type is the categorization of the persons location defined by facility, building, floor, point of care, room or bed (id: LA2.6 | len: 20 | use: O | rpt: 1)
        :param building: This component specifies the code for the building where the person is located (id: LA2.7 | len: 20 | use: O | rpt: 1)
        :param floor: This component specifies the code for the floor where the person is located (id: LA2.8 | len: 20 | use: O | rpt: 1)
        :param street_address: This component specifies the street or mailing address of a person or institution (id: LA2.9 | len: 120 | use: O | rpt: 1)
        :param other_designation: This component specifies the second line of an address (id: LA2.10 | len: 120 | use: O | rpt: 1)
        :param city: This component specifies the city, or district or place where the person or institution is located depending upon the national convention for formatting addresses for postal usage (id: LA2.11 | len: 50 | use: O | rpt: 1)
        :param state_or_province: This component specifies the state or province where the person or institution is located (id: LA2.12 | len: 50 | use: O | rpt: 1)
        :param zip_or_postal_code: This component specifies the zip or postal code where the person or institution is located (id: LA2.13 | len: 12 | use: O | rpt: 1)
        :param country: This component specifies the country where the person or institution is located (id: LA2.14 | len: 3 | use: O | rpt: 1)
        :param address_type: This component specifies the kind or type of address (id: LA2.15 | len: 3 | use: O | rpt: 1)
        :param other_geographic_designation: This component specifies any other geographic designation that may be necessary (id: LA2.16 | len: 50 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 16
        self.point_of_care = point_of_care
        self.room = room
        self.bed = bed
        self.facility = facility
        self.location_status = location_status
        self.patient_location_type = patient_location_type
        self.building = building
        self.floor = floor
        self.street_address = street_address
        self.other_designation = other_designation
        self.city = city
        self.state_or_province = state_or_province
        self.zip_or_postal_code = zip_or_postal_code
        self.country = country
        self.address_type = address_type
        self.other_geographic_designation = other_geographic_designation

    @property  # get LA2.1
    def point_of_care(self) -> PointOfCare | None:
        """
        id: LA2.1 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the point where patient care is administered. It is conditional on LA2. 6 Person Location Type (e.g., nursing unit or department or clinic). After floor, it is the most general patient location designation. Refer to User-defined Table 0302 - Point of care for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.1
        """
        return self._c_data[0][0]

    @point_of_care.setter  # set LA2.1
    def point_of_care(self, point_of_care: PointOfCare | None):
        """
        id: LA2.1 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the point where patient care is administered. It is conditional on LA2. 6 Person Location Type (e.g., nursing unit or department or clinic). After floor, it is the most general patient location designation. Refer to User-defined Table 0302 - Point of care for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.1
        """
        self._c_data[0] = (point_of_care,)

    @property  # get LA2.2
    def room(self) -> Room | None:
        """
        id: LA2.2 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient room. After point of care, it is the most general person location designation. Refer to User-defined Table 0303 - Room for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.2
        """
        return self._c_data[1][0]

    @room.setter  # set LA2.2
    def room(self, room: Room | None):
        """
        id: LA2.2 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient room. After point of care, it is the most general person location designation. Refer to User-defined Table 0303 - Room for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.2
        """
        self._c_data[1] = (room,)

    @property  # get LA2.3
    def bed(self) -> Bed | None:
        """
        id: LA2.3 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient's bed. After room, it is the most general person location designation. Refer to User-defined Table 0304 - Bed for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.3
        """
        return self._c_data[2][0]

    @bed.setter  # set LA2.3
    def bed(self, bed: Bed | None):
        """
        id: LA2.3 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient's bed. After room, it is the most general person location designation. Refer to User-defined Table 0304 - Bed for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.3
        """
        self._c_data[2] = (bed,)

    @property  # get LA2.4
    def facility(self) -> HD | None:
        """
        id: LA2.4 | len: 227 | use: O | rpt: 1
        ---
        This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise. It is the most general person location designation.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.4
        """
        return self._c_data[3][0]

    @facility.setter  # set LA2.4
    def facility(self, hd: HD | None):
        """
        id: LA2.4 | len: 227 | use: O | rpt: 1
        ---
        This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise. It is the most general person location designation.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.4
        """
        self._c_data[3] = (hd,)

    @property  # get LA2.5
    def location_status(self) -> LocationStatus | None:
        """
        id: LA2.5 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the status or availability of the location. For example, it may convey bed status. Refer to User-defined Table 0306 - Location status for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.5
        """
        return self._c_data[4][0]

    @location_status.setter  # set LA2.5
    def location_status(self, location_status: LocationStatus | None):
        """
        id: LA2.5 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the status or availability of the location. For example, it may convey bed status. Refer to User-defined Table 0306 - Location status for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.5
        """
        self._c_data[4] = (location_status,)

    @property  # get LA2.6
    def patient_location_type(self) -> PersonLocationType | None:
        """
        id: LA2.6 | len: 20 | use: O | rpt: 1
        ---
        Person location type is the categorization of the persons location defined by facility, building, floor, point of care, room or bed. Although not a required field, when used, it may be the only populated field. It usually includes values such as nursing unit, department, clinic, SNF, physicians office. Refer to User-defined Table 0305 - Person location type for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.6
        """
        return self._c_data[5][0]

    @patient_location_type.setter  # set LA2.6
    def patient_location_type(self, person_location_type: PersonLocationType | None):
        """
        id: LA2.6 | len: 20 | use: O | rpt: 1
        ---
        Person location type is the categorization of the persons location defined by facility, building, floor, point of care, room or bed. Although not a required field, when used, it may be the only populated field. It usually includes values such as nursing unit, department, clinic, SNF, physicians office. Refer to User-defined Table 0305 - Person location type for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.6
        """
        self._c_data[5] = (person_location_type,)

    @property  # get LA2.7
    def building(self) -> Building | None:
        """
        id: LA2.7 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the building where the person is located. After facility, it is the most general person location designation. Refer to User-defined Table 0307 - Building for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.7
        """
        return self._c_data[6][0]

    @building.setter  # set LA2.7
    def building(self, building: Building | None):
        """
        id: LA2.7 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the building where the person is located. After facility, it is the most general person location designation. Refer to User-defined Table 0307 - Building for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.7
        """
        self._c_data[6] = (building,)

    @property  # get LA2.8
    def floor(self) -> Floor | None:
        """
        id: LA2.8 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the floor where the person is located. After building, it is the most general person location designation. Refer to User-defined Table 0308 - Floor for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.8
        """
        return self._c_data[7][0]

    @floor.setter  # set LA2.8
    def floor(self, floor: Floor | None):
        """
        id: LA2.8 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the floor where the person is located. After building, it is the most general person location designation. Refer to User-defined Table 0308 - Floor for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.8
        """
        self._c_data[7] = (floor,)

    @property  # get LA2.9
    def street_address(self) -> ST | None:
        """
        id: LA2.9 | len: 120 | use: O | rpt: 1
        ---
        This component specifies the street or mailing address of a person or institution. When referencing an institution, it is used to specify the institution name. When used in connection with a person, it specifies the first line of the address.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.9
        """
        return self._c_data[8][0]

    @street_address.setter  # set LA2.9
    def street_address(self, st: ST | None):
        """
        id: LA2.9 | len: 120 | use: O | rpt: 1
        ---
        This component specifies the street or mailing address of a person or institution. When referencing an institution, it is used to specify the institution name. When used in connection with a person, it specifies the first line of the address.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.9
        """
        self._c_data[8] = (st,)

    @property  # get LA2.10
    def other_designation(self) -> ST | None:
        """
        id: LA2.10 | len: 120 | use: O | rpt: 1
        ---
        This component specifies the second line of an address. In general, it qualifies address. Examples: Suite 555 or Fourth Floor. When referencing an institution, this component specifies the street address.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.10
        """
        return self._c_data[9][0]

    @other_designation.setter  # set LA2.10
    def other_designation(self, st: ST | None):
        """
        id: LA2.10 | len: 120 | use: O | rpt: 1
        ---
        This component specifies the second line of an address. In general, it qualifies address. Examples: Suite 555 or Fourth Floor. When referencing an institution, this component specifies the street address.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.10
        """
        self._c_data[9] = (st,)

    @property  # get LA2.11
    def city(self) -> ST | None:
        """
        id: LA2.11 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the city, or district or place where the person or institution is located depending upon the national convention for formatting addresses for postal usage. City should be represented by the official postal service codes for that state.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.11
        """
        return self._c_data[10][0]

    @city.setter  # set LA2.11
    def city(self, st: ST | None):
        """
        id: LA2.11 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the city, or district or place where the person or institution is located depending upon the national convention for formatting addresses for postal usage. City should be represented by the official postal service codes for that state.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.11
        """
        self._c_data[10] = (st,)

    @property  # get LA2.12
    def state_or_province(self) -> ST | None:
        """
        id: LA2.12 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the state or province where the person or institution is located. State or province should be represented by the official postal service codes for that country.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.12
        """
        return self._c_data[11][0]

    @state_or_province.setter  # set LA2.12
    def state_or_province(self, st: ST | None):
        """
        id: LA2.12 | len: 50 | use: O | rpt: 1
        ---
        This component specifies the state or province where the person or institution is located. State or province should be represented by the official postal service codes for that country.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.12
        """
        self._c_data[11] = (st,)

    @property  # get LA2.13
    def zip_or_postal_code(self) -> ST | None:
        """
        id: LA2.13 | len: 12 | use: O | rpt: 1
        ---
        This component specifies the zip or postal code where the person or institution is located. Zip or postal codes should be represented by the official codes for that country. In the US, the zip code takes the form 99999[-9999], while the Canadian postal code takes the form A9A9A9 and the Australian Postcode takes the form 9999.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.13
        """
        return self._c_data[12][0]

    @zip_or_postal_code.setter  # set LA2.13
    def zip_or_postal_code(self, st: ST | None):
        """
        id: LA2.13 | len: 12 | use: O | rpt: 1
        ---
        This component specifies the zip or postal code where the person or institution is located. Zip or postal codes should be represented by the official codes for that country. In the US, the zip code takes the form 99999[-9999], while the Canadian postal code takes the form A9A9A9 and the Australian Postcode takes the form 9999.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.13
        """
        self._c_data[12] = (st,)

    @property  # get LA2.14
    def country(self) -> CountryCode | None:
        """
        id: LA2.14 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the country where the person or institution is located. ISO 3166 provides a list of country codes that may be used.[1] HL7 specifies that the 3-character (alphabetic) form of ISO 3166 be used for the country code. Refer to HL7 Table 0399 - Country code in section 2.15.9.17 for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.14
        """
        return self._c_data[13][0]

    @country.setter  # set LA2.14
    def country(self, country_code: CountryCode | None):
        """
        id: LA2.14 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the country where the person or institution is located. ISO 3166 provides a list of country codes that may be used.[1] HL7 specifies that the 3-character (alphabetic) form of ISO 3166 be used for the country code. Refer to HL7 Table 0399 - Country code in section 2.15.9.17 for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.14
        """
        self._c_data[13] = (country_code,)

    @property  # get LA2.15
    def address_type(self) -> AddressType | None:
        """
        id: LA2.15 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the kind or type of address. Refer to HL7 Table 0190 - Address type for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.15
        """
        return self._c_data[14][0]

    @address_type.setter  # set LA2.15
    def address_type(self, address_type: AddressType | None):
        """
        id: LA2.15 | len: 3 | use: O | rpt: 1
        ---
        This component specifies the kind or type of address. Refer to HL7 Table 0190 - Address type for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.15
        """
        self._c_data[14] = (address_type,)

    @property  # get LA2.16
    def other_geographic_designation(self) -> ST | None:
        """
        id: LA2.16 | len: 50 | use: O | rpt: 1
        ---
        This component specifies any other geographic designation that may be necessary. It includes county, bioregion, SMSA, etc.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.16
        """
        return self._c_data[15][0]

    @other_geographic_designation.setter  # set LA2.16
    def other_geographic_designation(self, st: ST | None):
        """
        id: LA2.16 | len: 50 | use: O | rpt: 1
        ---
        This component specifies any other geographic designation that may be necessary. It includes county, bioregion, SMSA, etc.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA2.16
        """
        self._c_data[15] = (st,)
