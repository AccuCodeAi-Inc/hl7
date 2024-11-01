from __future__ import annotations
from ...base import DataType
from .ST import ST
from .IS import IS
from .HD import HD
from .EI import EI
from ..tables.LocationStatus import LocationStatus
from ..tables.Floor import Floor
from ..tables.PersonLocationType import PersonLocationType
from ..tables.Building import Building
from ..tables.Bed import Bed
from ..tables.PointOfCare import PointOfCare
from ..tables.Room import Room


"""
DataType - PL
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::PL TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PL,
    ST, IS, HD, EI
)

pl = PL(  # Person Location - This data type is used to specify a patient location within a healthcare institution
    point_of_care=None,  # IS(...) 
    room=None,  # IS(...) 
    bed=None,  # IS(...) 
    facility=None,  # HD(...) 
    location_status=None,  # IS(...) 
    person_location_type=None,  # IS(...) 
    building=None,  # IS(...) 
    floor=None,  # IS(...) 
    location_description=None,  # ST(...) 
    comprehensive_location_identifier=None,  # EI(...) 
    assigning_authority_for_location=None,  # HD(...) 
)

-----END COMPOSITE_DATA_TYPE::PL TEMPLATE-----
"""


class PL(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 1230
    _hl7_id = """PL"""
    _hl7_name = """Person Location"""
    _hl7_description = """This data type is used to specify a patient location within a healthcare institution"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL"
    _c_length = (20, 20, 20, 227, 20, 20, 20, 20, 199, 427, 227,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "C", "O", "O", "O", "O", "O",)
    _c_aliases = ("PL.1", "PL.2", "PL.3", "PL.4", "PL.5", "PL.6", "PL.7", "PL.8", "PL.9", "PL.10", "PL.11",)
    _c_components = (IS, IS, IS, HD, IS, IS, IS, IS, ST, EI, HD,)
    _c_names = ("Point Of Care", "Room", "Bed", "Facility", "Location Status", "Person Location Type", "Building", "Floor", "Location Description", "Comprehensive Location Identifier", "Assigning Authority For Location",)
    _c_attrs = ("point_of_care", "room", "bed", "facility", "location_status", "person_location_type", "building", "floor", "location_description", "comprehensive_location_identifier", "assigning_authority_for_location",)
    # fmt: on

    def __init__(
        self,
        point_of_care: PointOfCare
        | IS
        | tuple[PointOfCare | IS, ...]
        | None = None,  # PL.1
        room: Room | IS | tuple[Room | IS, ...] | None = None,  # PL.2
        bed: Bed | IS | tuple[Bed | IS, ...] | None = None,  # PL.3
        facility: HD | tuple[HD, ...] | None = None,  # PL.4
        location_status: LocationStatus
        | IS
        | tuple[LocationStatus | IS, ...]
        | None = None,  # PL.5
        person_location_type: PersonLocationType
        | IS
        | tuple[PersonLocationType | IS, ...]
        | None = None,  # PL.6
        building: Building | IS | tuple[Building | IS, ...] | None = None,  # PL.7
        floor: Floor | IS | tuple[Floor | IS, ...] | None = None,  # PL.8
        location_description: ST | tuple[ST, ...] | None = None,  # PL.9
        comprehensive_location_identifier: EI | tuple[EI, ...] | None = None,  # PL.10
        assigning_authority_for_location: HD | tuple[HD, ...] | None = None,  # PL.11
    ):
        """
                Person Location - `PL <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PL>`_
                This data type is used to specify a patient location within a healthcare institution. Which components are valued depends on the needs of the site. For example for a patient treated at home, only the person location type is valued. It is most commonly used for specifying patient locations, but may refer to other types of persons within a healthcare setting.

        Example: Nursing Unit
        A nursing unit at Community Hospital: 4 East, room 136, bed B  4E^136^B^CommunityHospital^^N^^^
        A clinic at University Hospitals: Internal Medicine Clinic located in the Briones building, 3rd floor. InternalMedicine^^^UniversityHospitals^^C^Briones^3^

                :param point_of_care: This component specifies the code for the point where patient care is administered (id: PL.1 | len: 20 | use: O | rpt: 1)
                :param room: This component specifies the code for the patient's room (id: PL.2 | len: 20 | use: O | rpt: 1)
                :param bed: This component specifies the code for the patient's bed (id: PL.3 | len: 20 | use: O | rpt: 1)
                :param facility: This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise (id: PL.4 | len: 227 | use: O | rpt: 1)
                :param location_status: This component specifies the code for the status or availability of the location (id: PL.5 | len: 20 | use: O | rpt: 1)
                :param person_location_type: Person location type is the categorization of the persons location defined by facility, building, floor, point of care, room or bed (id: PL.6 | len: 20 | use: C | rpt: 1)
                :param building: This component specifies the code for the building where the person is located (id: PL.7 | len: 20 | use: O | rpt: 1)
                :param floor: This component specifies the code for the floor where the person is located (id: PL.8 | len: 20 | use: O | rpt: 1)
                :param location_description: This component describes the location in free text (id: PL.9 | len: 199 | use: O | rpt: 1)
                :param comprehensive_location_identifier: The unique identifier that represents the physical location as a whole without regard for the individual components (id: PL.10 | len: 427 | use: O | rpt: 1)
                :param assigning_authority_for_location: The entity that creates the data for the individual physical location components (id: PL.11 | len: 227 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 11
        self.point_of_care = point_of_care
        self.room = room
        self.bed = bed
        self.facility = facility
        self.location_status = location_status
        self.person_location_type = person_location_type
        self.building = building
        self.floor = floor
        self.location_description = location_description
        self.comprehensive_location_identifier = comprehensive_location_identifier
        self.assigning_authority_for_location = assigning_authority_for_location

    @property  # get PL.1
    def point_of_care(self) -> PointOfCare | None:
        """
        id: PL.1 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the point where patient care is administered. It is conditional on PL.6 Person Location Type (e.g., nursing unit or department or clinic). After floor, it is the most general patient location designation. Refer to User-defined Table 0302 - Point of care for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.1
        """
        return self._c_data[0][0]

    @point_of_care.setter  # set PL.1
    def point_of_care(self, point_of_care: PointOfCare | None):
        """
        id: PL.1 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the point where patient care is administered. It is conditional on PL.6 Person Location Type (e.g., nursing unit or department or clinic). After floor, it is the most general patient location designation. Refer to User-defined Table 0302 - Point of care for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.1
        """
        self._c_data[0] = (point_of_care,)

    @property  # get PL.2
    def room(self) -> Room | None:
        """
        id: PL.2 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient's room. After point of care, it is the most general person location designation. Refer to User-defined Table 0303 - Room for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.2
        """
        return self._c_data[1][0]

    @room.setter  # set PL.2
    def room(self, room: Room | None):
        """
        id: PL.2 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient's room. After point of care, it is the most general person location designation. Refer to User-defined Table 0303 - Room for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.2
        """
        self._c_data[1] = (room,)

    @property  # get PL.3
    def bed(self) -> Bed | None:
        """
        id: PL.3 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient's bed. After room, it is the most general person location designation. Refer to User-defined Table 0304 - Bed for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.3
        """
        return self._c_data[2][0]

    @bed.setter  # set PL.3
    def bed(self, bed: Bed | None):
        """
        id: PL.3 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient's bed. After room, it is the most general person location designation. Refer to User-defined Table 0304 - Bed for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.3
        """
        self._c_data[2] = (bed,)

    @property  # get PL.4
    def facility(self) -> HD | None:
        """
        id: PL.4 | len: 227 | use: O | rpt: 1
        ---
        This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise. It is the most general person location designation.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.4
        """
        return self._c_data[3][0]

    @facility.setter  # set PL.4
    def facility(self, hd: HD | None):
        """
        id: PL.4 | len: 227 | use: O | rpt: 1
        ---
        This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise. It is the most general person location designation.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.4
        """
        self._c_data[3] = (hd,)

    @property  # get PL.5
    def location_status(self) -> LocationStatus | None:
        """
        id: PL.5 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the status or availability of the location. For example, it may convey bed status. Refer to User-defined Table 0306 - Location status for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.5
        """
        return self._c_data[4][0]

    @location_status.setter  # set PL.5
    def location_status(self, location_status: LocationStatus | None):
        """
        id: PL.5 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the status or availability of the location. For example, it may convey bed status. Refer to User-defined Table 0306 - Location status for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.5
        """
        self._c_data[4] = (location_status,)

    @property  # get PL.6
    def person_location_type(self) -> PersonLocationType | None:
        """
        id: PL.6 | len: 20 | use: C | rpt: 1
        ---
        Person location type is the categorization of the persons location defined by facility, building, floor, point of care, room or bed. Although not a required field, when used, it may be the only populated field. It usually includes values such as nursing unit, department, clinic, SNF, physicians office. Refer to User-defined Table 0305 - Person location type for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.6
        """
        return self._c_data[5][0]

    @person_location_type.setter  # set PL.6
    def person_location_type(self, person_location_type: PersonLocationType | None):
        """
        id: PL.6 | len: 20 | use: C | rpt: 1
        ---
        Person location type is the categorization of the persons location defined by facility, building, floor, point of care, room or bed. Although not a required field, when used, it may be the only populated field. It usually includes values such as nursing unit, department, clinic, SNF, physicians office. Refer to User-defined Table 0305 - Person location type for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.6
        """
        self._c_data[5] = (person_location_type,)

    @property  # get PL.7
    def building(self) -> Building | None:
        """
        id: PL.7 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the building where the person is located. After facility, it is the most general person location designation. Refer to User-defined Table 0307 - Building for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.7
        """
        return self._c_data[6][0]

    @building.setter  # set PL.7
    def building(self, building: Building | None):
        """
        id: PL.7 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the building where the person is located. After facility, it is the most general person location designation. Refer to User-defined Table 0307 - Building for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.7
        """
        self._c_data[6] = (building,)

    @property  # get PL.8
    def floor(self) -> Floor | None:
        """
        id: PL.8 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the floor where the person is located. After building, it is the most general person location designation. Refer to User-defined Table 0308 - Floor for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.8
        """
        return self._c_data[7][0]

    @floor.setter  # set PL.8
    def floor(self, floor: Floor | None):
        """
        id: PL.8 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the floor where the person is located. After building, it is the most general person location designation. Refer to User-defined Table 0308 - Floor for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.8
        """
        self._c_data[7] = (floor,)

    @property  # get PL.9
    def location_description(self) -> ST | None:
        """
        id: PL.9 | len: 199 | use: O | rpt: 1
        ---
        This component describes the location in free text.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.9
        """
        return self._c_data[8][0]

    @location_description.setter  # set PL.9
    def location_description(self, st: ST | None):
        """
        id: PL.9 | len: 199 | use: O | rpt: 1
        ---
        This component describes the location in free text.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.9
        """
        self._c_data[8] = (st,)

    @property  # get PL.10
    def comprehensive_location_identifier(self) -> EI | None:
        """
        id: PL.10 | len: 427 | use: O | rpt: 1
        ---
        The unique identifier that represents the physical location as a whole without regard for the individual components. This accommodates sites that may have a different method of defining physical units or who may code at a less granular level. For example, point of care, room, and bed may be 1 indivisible code.
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.10
        """
        return self._c_data[9][0]

    @comprehensive_location_identifier.setter  # set PL.10
    def comprehensive_location_identifier(self, ei: EI | None):
        """
        id: PL.10 | len: 427 | use: O | rpt: 1
        ---
        The unique identifier that represents the physical location as a whole without regard for the individual components. This accommodates sites that may have a different method of defining physical units or who may code at a less granular level. For example, point of care, room, and bed may be 1 indivisible code.
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.10
        """
        self._c_data[9] = (ei,)

    @property  # get PL.11
    def assigning_authority_for_location(self) -> HD | None:
        """
        id: PL.11 | len: 227 | use: O | rpt: 1
        ---
        The entity that creates the data for the individual physical location components. If populated, it should be the authority for all components populated. Refer to User-defined Table 0363 - Assigning authority for suggested values for the first sub-component of the HD component, <namespace ID>.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.11
        """
        return self._c_data[10][0]

    @assigning_authority_for_location.setter  # set PL.11
    def assigning_authority_for_location(self, hd: HD | None):
        """
        id: PL.11 | len: 227 | use: O | rpt: 1
        ---
        The entity that creates the data for the individual physical location components. If populated, it should be the authority for all components populated. Refer to User-defined Table 0363 - Assigning authority for suggested values for the first sub-component of the HD component, <namespace ID>.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PL.11
        """
        self._c_data[10] = (hd,)
