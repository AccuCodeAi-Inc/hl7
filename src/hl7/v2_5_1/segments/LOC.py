from __future__ import annotations
from ...base import HL7Segment
from ..data_types.PL import PL
from ..data_types.IS import IS
from ..data_types.ST import ST
from ..data_types.XTN import XTN
from ..data_types.XAD import XAD
from ..data_types.CE import CE
from ..data_types.XON import XON
from ..tables.PatientLocationType import PatientLocationType
from ..tables.LicenseNumber import LicenseNumber
from ..tables.LocationEquipment import LocationEquipment
from ..tables.LocationServiceCode import LocationServiceCode


"""
Location Identification - LOC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::LOC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    LOC,
    PL, IS, ST, XTN, XAD, CE, XON
)

loc = LOC(  #  - The LOC segment can identify any patient location referenced by information systems
    primary_key_value_loc=pl,  # PL(...)  # Required.
    location_description=None,  # ST(...) 
    location_type_loc=_is,  # IS(...)  # Required.
    organization_name_loc=None,  # XON(...) 
    location_address=None,  # XAD(...) 
    location_phone=None,  # XTN(...) 
    license_number=None,  # CE(...) 
    location_equipment=None,  # IS(...) 
    location_service_code=None,  # IS(...) 
)

-----END SEGMENT::LOC TEMPLATE-----
"""


class LOC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """LOC"""
    _hl7_name = """Location Identification"""
    _hl7_description = """The LOC segment can identify any patient location referenced by information systems"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LOC"
    _c_length = (200, 48, 2, 250, 250, 250, 250, 3, 1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535, 65535, 65535, 1,)
    _c_usage = ("R", "O", "R", "O", "O", "O", "O", "O", "O",)
    _c_components = (PL, ST, IS, XON, XAD, XTN, CE, IS, IS,)
    _c_aliases = ("LOC.1", "LOC.2", "LOC.3", "LOC.4", "LOC.5", "LOC.6", "LOC.7", "LOC.8", "LOC.9",)
    _c_names = ("Primary Key Value - LOC", "Location Description", "Location Type - LOC", "Organization Name - LOC", "Location Address", "Location Phone", "License Number", "Location Equipment", "Location Service Code",)
    _c_attrs = ("primary_key_value_loc", "location_description", "location_type_loc", "organization_name_loc", "location_address", "location_phone", "license_number", "location_equipment", "location_service_code",)
    # fmt: on

    def __init__(
        self,
        primary_key_value_loc: PL | tuple[PL],  # LOC.1
        location_type_loc: PatientLocationType
        | IS
        | tuple[PatientLocationType | IS],  # LOC.3
        location_description: ST | tuple[ST] | None = None,  # LOC.2
        organization_name_loc: XON | tuple[XON] | None = None,  # LOC.4
        location_address: XAD | tuple[XAD] | None = None,  # LOC.5
        location_phone: XTN | tuple[XTN] | None = None,  # LOC.6
        license_number: LicenseNumber
        | CE
        | tuple[LicenseNumber | CE]
        | None = None,  # LOC.7
        location_equipment: LocationEquipment
        | IS
        | tuple[LocationEquipment | IS]
        | None = None,  # LOC.8
        location_service_code: LocationServiceCode
        | IS
        | tuple[LocationServiceCode | IS]
        | None = None,  # LOC.9
    ):
        """
        Location Identification - `LOC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LOC>`_
        The LOC segment can identify any patient location referenced by information systems.  This segment gives physical set up information about the location.  This is not intended to include any current occupant or current use information.  There should be one LOC segment for each patient location.  If desired, there can also be one LOC segment for each nursing unit and room.

        :param primary_key_value_loc: Person Location (id: LOC.1 | len: 200 | use: R | rpt: 1)
        :param location_description: String Data (id: LOC.2 | len: 48 | use: O | rpt: 1)
        :param location_type_loc: Coded value for user-defined tables (id: LOC.3 | len: 2 | use: R | rpt: *)
        :param organization_name_loc: Extended Composite Name and Identification Number for Organizations (id: LOC.4 | len: 250 | use: O | rpt: *)
        :param location_address: Extended Address (id: LOC.5 | len: 250 | use: O | rpt: *)
        :param location_phone: Extended Telecommunication Number (id: LOC.6 | len: 250 | use: O | rpt: *)
        :param license_number: Coded Element (id: LOC.7 | len: 250 | use: O | rpt: *)
        :param location_equipment: Coded value for user-defined tables (id: LOC.8 | len: 3 | use: O | rpt: *)
        :param location_service_code: Coded value for user-defined tables (id: LOC.9 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.primary_key_value_loc = primary_key_value_loc
        self.location_description = location_description
        self.location_type_loc = location_type_loc
        self.organization_name_loc = organization_name_loc
        self.location_address = location_address
        self.location_phone = location_phone
        self.license_number = license_number
        self.location_equipment = location_equipment
        self.location_service_code = location_service_code

    @property  # get LOC.1
    def primary_key_value_loc(self) -> PL:
        """
        id: LOC.1 | len: 200 | use: R | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.1
        """
        return self._c_data[0][0]

    @primary_key_value_loc.setter  # set LOC.1
    def primary_key_value_loc(self, pl: PL):
        """
        id: LOC.1 | len: 200 | use: R | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.1
        """
        self._c_data[0] = (pl,)

    @property  # get LOC.2
    def location_description(self) -> ST | None:
        """
        id: LOC.2 | len: 48 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.2
        """
        return self._c_data[1][0]

    @location_description.setter  # set LOC.2
    def location_description(self, st: ST | None):
        """
        id: LOC.2 | len: 48 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.2
        """
        self._c_data[1] = (st,)

    @property
    def location_type_loc(self) -> tuple[PatientLocationType, ...]:
        """
        id: LOC.3 | len: 2 | use: R | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.3
        """
        return self._c_data[2]

    @location_type_loc.setter  # set LOC.3
    def location_type_loc(
        self, patient_location_type: PatientLocationType | tuple[PatientLocationType]
    ):
        """
        id: LOC.3 | len: 2 | use: R | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.3
        """
        if isinstance(patient_location_type, tuple):
            self._c_data[2] = patient_location_type
        else:
            self._c_data[2] = (patient_location_type,)

    @property
    def organization_name_loc(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: LOC.4 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.4
        """
        return self._c_data[3]

    @organization_name_loc.setter  # set LOC.4
    def organization_name_loc(self, xon: XON | tuple[XON] | None):
        """
        id: LOC.4 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.4
        """
        if isinstance(xon, tuple):
            self._c_data[3] = xon
        else:
            self._c_data[3] = (xon,)

    @property
    def location_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: LOC.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.5
        """
        return self._c_data[4]

    @location_address.setter  # set LOC.5
    def location_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: LOC.5 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.5
        """
        if isinstance(xad, tuple):
            self._c_data[4] = xad
        else:
            self._c_data[4] = (xad,)

    @property
    def location_phone(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: LOC.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.6
        """
        return self._c_data[5]

    @location_phone.setter  # set LOC.6
    def location_phone(self, xtn: XTN | tuple[XTN] | None):
        """
        id: LOC.6 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.6
        """
        if isinstance(xtn, tuple):
            self._c_data[5] = xtn
        else:
            self._c_data[5] = (xtn,)

    @property
    def license_number(self) -> tuple[LicenseNumber, ...] | tuple[None]:
        """
        id: LOC.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.7
        """
        return self._c_data[6]

    @license_number.setter  # set LOC.7
    def license_number(
        self, license_number: LicenseNumber | tuple[LicenseNumber] | None
    ):
        """
        id: LOC.7 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.7
        """
        if isinstance(license_number, tuple):
            self._c_data[6] = license_number
        else:
            self._c_data[6] = (license_number,)

    @property
    def location_equipment(self) -> tuple[LocationEquipment, ...] | tuple[None]:
        """
        id: LOC.8 | len: 3 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.8
        """
        return self._c_data[7]

    @location_equipment.setter  # set LOC.8
    def location_equipment(
        self, location_equipment: LocationEquipment | tuple[LocationEquipment] | None
    ):
        """
        id: LOC.8 | len: 3 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.8
        """
        if isinstance(location_equipment, tuple):
            self._c_data[7] = location_equipment
        else:
            self._c_data[7] = (location_equipment,)

    @property  # get LOC.9
    def location_service_code(self) -> LocationServiceCode | None:
        """
        id: LOC.9 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.9
        """
        return self._c_data[8][0]

    @location_service_code.setter  # set LOC.9
    def location_service_code(self, location_service_code: LocationServiceCode | None):
        """
        id: LOC.9 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LOC.9
        """
        self._c_data[8] = (location_service_code,)
