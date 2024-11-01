from __future__ import annotations
from ...base import DataType
from .IS import IS
from .HD import HD
from .CNN import CNN
from .TS import TS
from ..tables.PointOfCare import PointOfCare
from ..tables.Room import Room
from ..tables.LocationStatus import LocationStatus
from ..tables.Floor import Floor
from ..tables.Building import Building
from ..tables.Bed import Bed
from ..tables.PersonLocationType import PersonLocationType


"""
DataType - NDL
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::NDL TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    NDL,
    IS, HD, CNN, TS
)

ndl = NDL(  # Name with Date and Location - Specifies the name of the person performing a service, when the person performed the service and where the person performed the service
    name=None,  # CNN(...) 
    start_date_or_time=None,  # TS(...) 
    end_date_or_time=None,  # TS(...) 
    point_of_care=None,  # IS(...) 
    room=None,  # IS(...) 
    bed=None,  # IS(...) 
    facility=None,  # HD(...) 
    location_status=None,  # IS(...) 
    patient_location_type=None,  # IS(...) 
    building=None,  # IS(...) 
    floor=None,  # IS(...) 
)

-----END COMPOSITE_DATA_TYPE::NDL TEMPLATE-----
"""


class NDL(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 835
    _hl7_id = """NDL"""
    _hl7_name = """Name with Date and Location"""
    _hl7_description = """Specifies the name of the person performing a service, when the person performed the service and where the person performed the service"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL"
    _c_length = (406, 26, 26, 20, 20, 20, 227, 20, 20, 20, 20,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("NDL.1", "NDL.2", "NDL.3", "NDL.4", "NDL.5", "NDL.6", "NDL.7", "NDL.8", "NDL.9", "NDL.10", "NDL.11",)
    _c_components = (CNN, TS, TS, IS, IS, IS, HD, IS, IS, IS, IS,)
    _c_names = ("Name", "Start Date/Time", "End Date/Time", "Point Of Care", "Room", "Bed", "Facility", "Location Status", "Patient Location Type", "Building", "Floor",)
    _c_attrs = ("name", "start_date_or_time", "end_date_or_time", "point_of_care", "room", "bed", "facility", "location_status", "patient_location_type", "building", "floor",)
    # fmt: on

    def __init__(
        self,
        name: CNN | None = None,  # NDL.1
        start_date_or_time: TS | None = None,  # NDL.2
        end_date_or_time: TS | None = None,  # NDL.3
        point_of_care: PointOfCare | IS | None = None,  # NDL.4
        room: Room | IS | None = None,  # NDL.5
        bed: Bed | IS | None = None,  # NDL.6
        facility: HD | None = None,  # NDL.7
        location_status: LocationStatus | IS | None = None,  # NDL.8
        patient_location_type: PersonLocationType | IS | None = None,  # NDL.9
        building: Building | IS | None = None,  # NDL.10
        floor: Floor | IS | None = None,  # NDL.11
    ):
        """
        Name with Date and Location - `NDL <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NDL>`_
        Specifies the name of the person performing a service, when the person performed the service and where the person performed the service.

        :param name: This component specifies the name of the person performing a service (id: NDL.1 | len: 406 | use: O | rpt: 1)
        :param start_date_or_time: This component specifies the starting date and time for when the person is performing the service (id: NDL.2 | len: 26 | use: O | rpt: 1)
        :param end_date_or_time: This component specifies the ending date and time for when the person is performing the service (id: NDL.3 | len: 26 | use: O | rpt: 1)
        :param point_of_care: This component specifies the code for the point where patient care is administered (id: NDL.4 | len: 20 | use: O | rpt: 1)
        :param room: Patient room (id: NDL.5 | len: 20 | use: O | rpt: 1)
        :param bed: This component specifies the code for the patient's bed (id: NDL.6 | len: 20 | use: O | rpt: 1)
        :param facility: This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise (id: NDL.7 | len: 227 | use: O | rpt: 1)
        :param location_status: This component specifies the code for the status or availability of the location (id: NDL.8 | len: 20 | use: O | rpt: 1)
        :param patient_location_type: Location type is the categorization of the location defined by facility, building, floor, point of care, room or bed (id: NDL.9 | len: 20 | use: O | rpt: 1)
        :param building: This component specifies the code for the building where the person is located (id: NDL.10 | len: 20 | use: O | rpt: 1)
        :param floor: This component specifies the code for the floor where the person is located (id: NDL.11 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 11
        self.name = name
        self.start_date_or_time = start_date_or_time
        self.end_date_or_time = end_date_or_time
        self.point_of_care = point_of_care
        self.room = room
        self.bed = bed
        self.facility = facility
        self.location_status = location_status
        self.patient_location_type = patient_location_type
        self.building = building
        self.floor = floor

    @property  # get NDL.1
    def name(self) -> CNN | None:
        """
        id: NDL.1 | len: 406 | use: O | rpt: 1
        ---
        This component specifies the name of the person performing a service.
        ---
        return_type: CNN: Composite ID Number and Name Simplified
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.1
        """
        return self._c_data[0][0]

    @name.setter  # set NDL.1
    def name(self, cnn: CNN | None):
        """
        id: NDL.1 | len: 406 | use: O | rpt: 1
        ---
        This component specifies the name of the person performing a service.
        ---
        param_type: CNN: Composite ID Number and Name Simplified
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.1
        """
        self._c_data[0] = (cnn,)

    @property  # get NDL.2
    def start_date_or_time(self) -> TS | None:
        """
        id: NDL.2 | len: 26 | use: O | rpt: 1
        ---
        This component specifies the starting date and time for when the person is performing the service.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.2
        """
        return self._c_data[1][0]

    @start_date_or_time.setter  # set NDL.2
    def start_date_or_time(self, ts: TS | None):
        """
        id: NDL.2 | len: 26 | use: O | rpt: 1
        ---
        This component specifies the starting date and time for when the person is performing the service.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.2
        """
        self._c_data[1] = (ts,)

    @property  # get NDL.3
    def end_date_or_time(self) -> TS | None:
        """
        id: NDL.3 | len: 26 | use: O | rpt: 1
        ---
        This component specifies the ending date and time for when the person is performing the service.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.3
        """
        return self._c_data[2][0]

    @end_date_or_time.setter  # set NDL.3
    def end_date_or_time(self, ts: TS | None):
        """
        id: NDL.3 | len: 26 | use: O | rpt: 1
        ---
        This component specifies the ending date and time for when the person is performing the service.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.3
        """
        self._c_data[2] = (ts,)

    @property  # get NDL.4
    def point_of_care(self) -> PointOfCare | None:
        """
        id: NDL.4 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the point where patient care is administered. It is conditional on NDL. 9 Person Location Type (e.g., nursing unit or department or clinic). After floor, it is the most general patient location designation. Refer to User-defined Table 0302 - Point of care for suggested values
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.4
        """
        return self._c_data[3][0]

    @point_of_care.setter  # set NDL.4
    def point_of_care(self, point_of_care: PointOfCare | None):
        """
        id: NDL.4 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the point where patient care is administered. It is conditional on NDL. 9 Person Location Type (e.g., nursing unit or department or clinic). After floor, it is the most general patient location designation. Refer to User-defined Table 0302 - Point of care for suggested values
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.4
        """
        self._c_data[3] = (point_of_care,)

    @property  # get NDL.5
    def room(self) -> Room | None:
        """
        id: NDL.5 | len: 20 | use: O | rpt: 1
        ---
        Patient room. After point of care, it is the most general location designation. Refer to User-defined Table 0303 - Room for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.5
        """
        return self._c_data[4][0]

    @room.setter  # set NDL.5
    def room(self, room: Room | None):
        """
        id: NDL.5 | len: 20 | use: O | rpt: 1
        ---
        Patient room. After point of care, it is the most general location designation. Refer to User-defined Table 0303 - Room for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.5
        """
        self._c_data[4] = (room,)

    @property  # get NDL.6
    def bed(self) -> Bed | None:
        """
        id: NDL.6 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient's bed. After room, it is the most general location designation. Refer to User-defined Table 0304 - Bed for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.6
        """
        return self._c_data[5][0]

    @bed.setter  # set NDL.6
    def bed(self, bed: Bed | None):
        """
        id: NDL.6 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the patient's bed. After room, it is the most general location designation. Refer to User-defined Table 0304 - Bed for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.6
        """
        self._c_data[5] = (bed,)

    @property  # get NDL.7
    def facility(self) -> HD | None:
        """
        id: NDL.7 | len: 227 | use: O | rpt: 1
        ---
        This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise. It is the most general location designation.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.7
        """
        return self._c_data[6][0]

    @facility.setter  # set NDL.7
    def facility(self, hd: HD | None):
        """
        id: NDL.7 | len: 227 | use: O | rpt: 1
        ---
        This component is subject to site interpretation but generally describes the highest level physical designation of an institution, medical center or enterprise. It is the most general location designation.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.7
        """
        self._c_data[6] = (hd,)

    @property  # get NDL.8
    def location_status(self) -> LocationStatus | None:
        """
        id: NDL.8 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the status or availability of the location. For example, it may convey bed status. Refer to User-defined Table 0306 - Location status for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.8
        """
        return self._c_data[7][0]

    @location_status.setter  # set NDL.8
    def location_status(self, location_status: LocationStatus | None):
        """
        id: NDL.8 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the status or availability of the location. For example, it may convey bed status. Refer to User-defined Table 0306 - Location status for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.8
        """
        self._c_data[7] = (location_status,)

    @property  # get NDL.9
    def patient_location_type(self) -> PersonLocationType | None:
        """
        id: NDL.9 | len: 20 | use: O | rpt: 1
        ---
        Location type is the categorization of the location defined by facility, building, floor, point of care, room or bed. Although not a required field, when used, it may be the only populated field. Usually includes values such as nursing unit, department, clinic, SNF, physicians office. Refer to User-defined Table 0305 - Person location type for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.9
        """
        return self._c_data[8][0]

    @patient_location_type.setter  # set NDL.9
    def patient_location_type(self, person_location_type: PersonLocationType | None):
        """
        id: NDL.9 | len: 20 | use: O | rpt: 1
        ---
        Location type is the categorization of the location defined by facility, building, floor, point of care, room or bed. Although not a required field, when used, it may be the only populated field. Usually includes values such as nursing unit, department, clinic, SNF, physicians office. Refer to User-defined Table 0305 - Person location type for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.9
        """
        self._c_data[8] = (person_location_type,)

    @property  # get NDL.10
    def building(self) -> Building | None:
        """
        id: NDL.10 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the building where the person is located. After facility, it is the most general location designation. Refer to User-defined Table 0307 - Building for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.10
        """
        return self._c_data[9][0]

    @building.setter  # set NDL.10
    def building(self, building: Building | None):
        """
        id: NDL.10 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the building where the person is located. After facility, it is the most general location designation. Refer to User-defined Table 0307 - Building for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.10
        """
        self._c_data[9] = (building,)

    @property  # get NDL.11
    def floor(self) -> Floor | None:
        """
        id: NDL.11 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the floor where the person is located. After building, it is the most general location designation. Refer to User-defined Table 0308 - Floor for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.11
        """
        return self._c_data[10][0]

    @floor.setter  # set NDL.11
    def floor(self, floor: Floor | None):
        """
        id: NDL.11 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the code for the floor where the person is located. After building, it is the most general location designation. Refer to User-defined Table 0308 - Floor for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDL.11
        """
        self._c_data[10] = (floor,)
