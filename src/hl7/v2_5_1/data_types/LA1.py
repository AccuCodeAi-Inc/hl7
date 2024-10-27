from __future__ import annotations
from ...base import DataType
from .AD import AD
from .HD import HD
from .IS import IS
from ..tables.Bed import Bed
from ..tables.Room import Room
from ..tables.Floor import Floor
from ..tables.Building import Building
from ..tables.PersonLocationType import PersonLocationType
from ..tables.PointOfCare import PointOfCare
from ..tables.LocationStatus import LocationStatus


"""
DataType - LA1
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::LA1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    LA1,
    AD, HD, IS
)

la1 = LA1(  # Location with Address Variation 1 - Specifies a location and its address
    point_of_care=None,  # IS(...) 
    room=None,  # IS(...) 
    bed=None,  # IS(...) 
    facility=None,  # HD(...) 
    location_status=None,  # IS(...) 
    patient_location_type=None,  # IS(...) 
    building=None,  # IS(...) 
    floor=None,  # IS(...) 
    address=None,  # AD(...) 
)

-----END COMPOSITE_DATA_TYPE::LA1 TEMPLATE-----
"""


class LA1(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 790
    _hl7_id = """LA1"""
    _hl7_name = """Location with Address Variation 1"""
    _hl7_description = """Specifies a location and its address"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1"
    _c_length = (20, 20, 20, 227, 20, 20, 20, 20, 415,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("LA1.1", "LA1.2", "LA1.3", "LA1.4", "LA1.5", "LA1.6", "LA1.7", "LA1.8", "LA1.9",)
    _c_components = (IS, IS, IS, HD, IS, IS, IS, IS, AD,)
    _c_names = ("Point Of Care", "Room", "Bed", "Facility", "Location Status", "Patient Location Type", "Building", "Floor", "Address",)
    _c_attrs = ("point_of_care", "room", "bed", "facility", "location_status", "patient_location_type", "building", "floor", "address",)
    # fmt: on

    def __init__(
        self,
        point_of_care: PointOfCare | IS | None = None,  # LA1.1
        room: Room | IS | None = None,  # LA1.2
        bed: Bed | IS | None = None,  # LA1.3
        facility: HD | None = None,  # LA1.4
        location_status: LocationStatus | IS | None = None,  # LA1.5
        patient_location_type: PersonLocationType | IS | None = None,  # LA1.6
        building: Building | IS | None = None,  # LA1.7
        floor: Floor | IS | None = None,  # LA1.8
        address: AD | None = None,  # LA1.9
    ):
        """
        Location with Address Variation 1 - `LA1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LA1>`_
        Specifies a location and its address.

        :param point_of_care: This component specifies the code for the point where patient care is administered (id: LA1.1 | len: 20 | use: O | rpt: 1)
        :param room: This component specifies the code for the patient room (id: LA1.2 | len: 20 | use: O | rpt: 1)
        :param bed: This component specifies the code for the patient bed (id: LA1.3 | len: 20 | use: O | rpt: 1)
        :param facility: This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise (id: LA1.4 | len: 227 | use: O | rpt: 1)
        :param location_status: This component specifies the code for the status or availability of the location (id: LA1.5 | len: 20 | use: O | rpt: 1)
        :param patient_location_type: Person location type is the categorization of the persons location defined by facility, building, floor, point of care, room or bed (id: LA1.6 | len: 20 | use: O | rpt: 1)
        :param building: This component specifies the code for the building where the person is located (id: LA1.7 | len: 20 | use: O | rpt: 1)
        :param floor: This component specifies the code for the floor where the person is located (id: LA1.8 | len: 20 | use: O | rpt: 1)
        :param address: This component describes the location in free text (id: LA1.9 | len: 415 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.point_of_care = point_of_care
        self.room = room
        self.bed = bed
        self.facility = facility
        self.location_status = location_status
        self.patient_location_type = patient_location_type
        self.building = building
        self.floor = floor
        self.address = address

    @property  # get LA1.1
    def point_of_care(self) -> PointOfCare | None:
        """
        id: LA1.1 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the point where patient care is administered. It is conditional on person location type (e.g., nursing unit or department or clinic). After floor, it is the most general patient location designation. Refer to User-defined Table 0302 - Point of care for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.1
        """
        return self._c_data[0][0]

    @point_of_care.setter  # set LA1.1
    def point_of_care(self, point_of_care: PointOfCare | None):
        """
        id: LA1.1 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the point where patient care is administered. It is conditional on person location type (e.g., nursing unit or department or clinic). After floor, it is the most general patient location designation. Refer to User-defined Table 0302 - Point of care for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.1
        """
        self._c_data[0] = (point_of_care,)

    @property  # get LA1.2
    def room(self) -> Room | None:
        """
        id: LA1.2 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient room. After point of care, it is the most general person location designation. Refer to User-defined Table 0303 - Room for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.2
        """
        return self._c_data[1][0]

    @room.setter  # set LA1.2
    def room(self, room: Room | None):
        """
        id: LA1.2 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient room. After point of care, it is the most general person location designation. Refer to User-defined Table 0303 - Room for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.2
        """
        self._c_data[1] = (room,)

    @property  # get LA1.3
    def bed(self) -> Bed | None:
        """
        id: LA1.3 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient bed. After room, it is the most general person location designation. Refer to User-defined Table 0304 - Bed for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.3
        """
        return self._c_data[2][0]

    @bed.setter  # set LA1.3
    def bed(self, bed: Bed | None):
        """
        id: LA1.3 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient bed. After room, it is the most general person location designation. Refer to User-defined Table 0304 - Bed for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.3
        """
        self._c_data[2] = (bed,)

    @property  # get LA1.4
    def facility(self) -> HD | None:
        """
        id: LA1.4 | len: 227 | use: O | rpt: 1
        ---
        This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise. It is the most general person location designation.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.4
        """
        return self._c_data[3][0]

    @facility.setter  # set LA1.4
    def facility(self, hd: HD | None):
        """
        id: LA1.4 | len: 227 | use: O | rpt: 1
        ---
        This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise. It is the most general person location designation.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.4
        """
        self._c_data[3] = (hd,)

    @property  # get LA1.5
    def location_status(self) -> LocationStatus | None:
        """
        id: LA1.5 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the status or availability of the location. For example, it may convey bed status. Refer to User-defined Table 0306 - Location status for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.5
        """
        return self._c_data[4][0]

    @location_status.setter  # set LA1.5
    def location_status(self, location_status: LocationStatus | None):
        """
        id: LA1.5 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the status or availability of the location. For example, it may convey bed status. Refer to User-defined Table 0306 - Location status for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.5
        """
        self._c_data[4] = (location_status,)

    @property  # get LA1.6
    def patient_location_type(self) -> PersonLocationType | None:
        """
        id: LA1.6 | len: 20 | use: O | rpt: 1
        ---
        Person location type is the categorization of the persons location defined by facility, building, floor, point of care, room or bed. Although not a required field, when used, it may be the only populated field. It usually includes values such as nursing unit, department, clinic, SNF, physicians office. Refer to User-defined Table 0305 - Person location type for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.6
        """
        return self._c_data[5][0]

    @patient_location_type.setter  # set LA1.6
    def patient_location_type(self, person_location_type: PersonLocationType | None):
        """
        id: LA1.6 | len: 20 | use: O | rpt: 1
        ---
        Person location type is the categorization of the persons location defined by facility, building, floor, point of care, room or bed. Although not a required field, when used, it may be the only populated field. It usually includes values such as nursing unit, department, clinic, SNF, physicians office. Refer to User-defined Table 0305 - Person location type for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.6
        """
        self._c_data[5] = (person_location_type,)

    @property  # get LA1.7
    def building(self) -> Building | None:
        """
        id: LA1.7 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the building where the person is located. After facility, it is the most general person location designation. Refer to User-defined Table 0307 - Building for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.7
        """
        return self._c_data[6][0]

    @building.setter  # set LA1.7
    def building(self, building: Building | None):
        """
        id: LA1.7 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the building where the person is located. After facility, it is the most general person location designation. Refer to User-defined Table 0307 - Building for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.7
        """
        self._c_data[6] = (building,)

    @property  # get LA1.8
    def floor(self) -> Floor | None:
        """
        id: LA1.8 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the floor where the person is located. After building, it is the most general person location designation. Refer to User-defined Table 0308 - Floor for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.8
        """
        return self._c_data[7][0]

    @floor.setter  # set LA1.8
    def floor(self, floor: Floor | None):
        """
        id: LA1.8 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the floor where the person is located. After building, it is the most general person location designation. Refer to User-defined Table 0308 - Floor for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.8
        """
        self._c_data[7] = (floor,)

    @property  # get LA1.9
    def address(self) -> AD | None:
        """
        id: LA1.9 | len: 415 | use: O | rpt: 1
        ---
        This component describes the location in free text.
        ---
        return_type: AD: Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.9
        """
        return self._c_data[8][0]

    @address.setter  # set LA1.9
    def address(self, ad: AD | None):
        """
        id: LA1.9 | len: 415 | use: O | rpt: 1
        ---
        This component describes the location in free text.
        ---
        param_type: AD: Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LA1.9
        """
        self._c_data[8] = (ad,)
