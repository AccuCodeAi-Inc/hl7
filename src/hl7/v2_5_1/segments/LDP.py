from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TS import TS
from ..data_types.IS import IS
from ..data_types.XTN import XTN
from ..data_types.PL import PL
from ..data_types.VH import VH
from ..data_types.ST import ST
from ..data_types.ID import ID
from ..tables.ActiveOrInactive import ActiveOrInactive
from ..tables.LocationCostCenter import LocationCostCenter
from ..tables.SpecialtyType import SpecialtyType
from ..tables.HospitalService import HospitalService
from ..tables.PatientClass import PatientClass
from ..tables.LocationDepartment import LocationDepartment


"""
Location Department - LDP
HL7 Version: 2.5.1

-----BEGIN SEGMENT::LDP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    LDP,
    CE, TS, IS, XTN, PL, VH, ST, ID
)

ldp = LDP(  #  - The LDP segment identifies how a patient location room is being used by a certain department
    primary_key_value_ldp=pl,  # PL(...)  # Required.
    location_department=ce,  # CE(...)  # Required.
    location_service=None,  # IS(...) 
    specialty_type=None,  # CE(...) 
    valid_patient_classes=None,  # IS(...) 
    active_or_inactive_flag=None,  # ID(...) 
    activation_date_ldp=None,  # TS(...) 
    inactivation_date_ldp=None,  # TS(...) 
    inactivated_reason=None,  # ST(...) 
    visiting_hours=None,  # VH(...) 
    contact_phone=None,  # XTN(...) 
    location_cost_center=None,  # CE(...) 
)

-----END SEGMENT::LDP TEMPLATE-----
"""


class LDP(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """LDP"""
    _hl7_name = """Location Department"""
    _hl7_description = """The LDP segment identifies how a patient location room is being used by a certain department"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LDP"
    _c_length = (200, 250, 3, 250, 1, 1, 26, 26, 80, 80, 250, 250,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 1, 1, 1, 1, 65535, 1, 1,)
    _c_usage = ("R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (PL, CE, IS, CE, IS, ID, TS, TS, ST, VH, XTN, CE,)
    _c_aliases = ("LDP.1", "LDP.2", "LDP.3", "LDP.4", "LDP.5", "LDP.6", "LDP.7", "LDP.8", "LDP.9", "LDP.10", "LDP.11", "LDP.12",)
    _c_names = ("Primary Key Value - LDP", "Location Department", "Location Service", "Specialty Type", "Valid Patient Classes", "Active/Inactive Flag", "Activation Date - LDP", "Inactivation Date - LDP", "Inactivated Reason", "Visiting Hours", "Contact Phone", "Location Cost Center",)
    _c_attrs = ("primary_key_value_ldp", "location_department", "location_service", "specialty_type", "valid_patient_classes", "active_or_inactive_flag", "activation_date_ldp", "inactivation_date_ldp", "inactivated_reason", "visiting_hours", "contact_phone", "location_cost_center",)
    # fmt: on

    def __init__(
        self,
        primary_key_value_ldp: PL | tuple[PL, ...],  # LDP.1
        location_department: LocationDepartment
        | CE
        | tuple[LocationDepartment | CE, ...],  # LDP.2
        location_service: HospitalService
        | IS
        | tuple[HospitalService | IS, ...]
        | None = None,  # LDP.3
        specialty_type: SpecialtyType
        | CE
        | tuple[SpecialtyType | CE, ...]
        | None = None,  # LDP.4
        valid_patient_classes: PatientClass
        | IS
        | tuple[PatientClass | IS, ...]
        | None = None,  # LDP.5
        active_or_inactive_flag: ActiveOrInactive
        | ID
        | tuple[ActiveOrInactive | ID, ...]
        | None = None,  # LDP.6
        activation_date_ldp: TS | tuple[TS, ...] | None = None,  # LDP.7
        inactivation_date_ldp: TS | tuple[TS, ...] | None = None,  # LDP.8
        inactivated_reason: ST | tuple[ST, ...] | None = None,  # LDP.9
        visiting_hours: VH | tuple[VH, ...] | None = None,  # LDP.10
        contact_phone: XTN | tuple[XTN, ...] | None = None,  # LDP.11
        location_cost_center: LocationCostCenter
        | CE
        | tuple[LocationCostCenter | CE, ...]
        | None = None,  # LDP.12
    ):
        """
        Location Department - `LDP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LDP>`_
        The LDP segment identifies how a patient location room is being used by a certain department.  Multiple departments can use the same patient location, so there can be multiple LDP segments following an LOC segment.  There must be at least one LDP segment for each LOC segment.  This is not intended to include any current occupant information.

        :param primary_key_value_ldp: Person Location (id: LDP.1 | len: 200 | use: R | rpt: 1)
        :param location_department: Coded Element (id: LDP.2 | len: 250 | use: R | rpt: 1)
        :param location_service: Coded value for user-defined tables (id: LDP.3 | len: 3 | use: O | rpt: *)
        :param specialty_type: Coded Element (id: LDP.4 | len: 250 | use: O | rpt: *)
        :param valid_patient_classes: Coded value for user-defined tables (id: LDP.5 | len: 1 | use: O | rpt: *)
        :param active_or_inactive_flag: Coded values for HL7 tables (id: LDP.6 | len: 1 | use: O | rpt: 1)
        :param activation_date_ldp: Time Stamp (id: LDP.7 | len: 26 | use: O | rpt: 1)
        :param inactivation_date_ldp: Time Stamp (id: LDP.8 | len: 26 | use: O | rpt: 1)
        :param inactivated_reason: String Data (id: LDP.9 | len: 80 | use: O | rpt: 1)
        :param visiting_hours: Visiting Hours (id: LDP.10 | len: 80 | use: O | rpt: *)
        :param contact_phone: Extended Telecommunication Number (id: LDP.11 | len: 250 | use: O | rpt: 1)
        :param location_cost_center: Coded Element (id: LDP.12 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.primary_key_value_ldp = primary_key_value_ldp
        self.location_department = location_department
        self.location_service = location_service
        self.specialty_type = specialty_type
        self.valid_patient_classes = valid_patient_classes
        self.active_or_inactive_flag = active_or_inactive_flag
        self.activation_date_ldp = activation_date_ldp
        self.inactivation_date_ldp = inactivation_date_ldp
        self.inactivated_reason = inactivated_reason
        self.visiting_hours = visiting_hours
        self.contact_phone = contact_phone
        self.location_cost_center = location_cost_center

    @property  # get LDP.1
    def primary_key_value_ldp(self) -> PL:
        """
        id: LDP.1 | len: 200 | use: R | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.1
        """
        return self._c_data[0][0]

    @primary_key_value_ldp.setter  # set LDP.1
    def primary_key_value_ldp(self, pl: PL):
        """
        id: LDP.1 | len: 200 | use: R | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.1
        """
        self._c_data[0] = (pl,)

    @property  # get LDP.2
    def location_department(self) -> LocationDepartment:
        """
        id: LDP.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.2
        """
        return self._c_data[1][0]

    @location_department.setter  # set LDP.2
    def location_department(self, location_department: LocationDepartment):
        """
        id: LDP.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.2
        """
        self._c_data[1] = (location_department,)

    @property
    def location_service(self) -> tuple[HospitalService, ...] | tuple[None]:
        """
        id: LDP.3 | len: 3 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.3
        """
        return self._c_data[2]

    @location_service.setter  # set LDP.3
    def location_service(
        self, hospital_service: HospitalService | tuple[HospitalService] | None
    ):
        """
        id: LDP.3 | len: 3 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.3
        """
        if isinstance(hospital_service, tuple):
            self._c_data[2] = hospital_service
        else:
            self._c_data[2] = (hospital_service,)

    @property
    def specialty_type(self) -> tuple[SpecialtyType, ...] | tuple[None]:
        """
        id: LDP.4 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.4
        """
        return self._c_data[3]

    @specialty_type.setter  # set LDP.4
    def specialty_type(
        self, specialty_type: SpecialtyType | tuple[SpecialtyType] | None
    ):
        """
        id: LDP.4 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.4
        """
        if isinstance(specialty_type, tuple):
            self._c_data[3] = specialty_type
        else:
            self._c_data[3] = (specialty_type,)

    @property
    def valid_patient_classes(self) -> tuple[PatientClass, ...] | tuple[None]:
        """
        id: LDP.5 | len: 1 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.5
        """
        return self._c_data[4]

    @valid_patient_classes.setter  # set LDP.5
    def valid_patient_classes(
        self, patient_class: PatientClass | tuple[PatientClass] | None
    ):
        """
        id: LDP.5 | len: 1 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.5
        """
        if isinstance(patient_class, tuple):
            self._c_data[4] = patient_class
        else:
            self._c_data[4] = (patient_class,)

    @property  # get LDP.6
    def active_or_inactive_flag(self) -> ActiveOrInactive | None:
        """
        id: LDP.6 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.6
        """
        return self._c_data[5][0]

    @active_or_inactive_flag.setter  # set LDP.6
    def active_or_inactive_flag(self, active_or_inactive: ActiveOrInactive | None):
        """
        id: LDP.6 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.6
        """
        self._c_data[5] = (active_or_inactive,)

    @property  # get LDP.7
    def activation_date_ldp(self) -> TS | None:
        """
        id: LDP.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.7
        """
        return self._c_data[6][0]

    @activation_date_ldp.setter  # set LDP.7
    def activation_date_ldp(self, ts: TS | None):
        """
        id: LDP.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.7
        """
        self._c_data[6] = (ts,)

    @property  # get LDP.8
    def inactivation_date_ldp(self) -> TS | None:
        """
        id: LDP.8 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.8
        """
        return self._c_data[7][0]

    @inactivation_date_ldp.setter  # set LDP.8
    def inactivation_date_ldp(self, ts: TS | None):
        """
        id: LDP.8 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.8
        """
        self._c_data[7] = (ts,)

    @property  # get LDP.9
    def inactivated_reason(self) -> ST | None:
        """
        id: LDP.9 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.9
        """
        return self._c_data[8][0]

    @inactivated_reason.setter  # set LDP.9
    def inactivated_reason(self, st: ST | None):
        """
        id: LDP.9 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.9
        """
        self._c_data[8] = (st,)

    @property
    def visiting_hours(self) -> tuple[VH, ...] | tuple[None]:
        """
        id: LDP.10 | len: 80 | use: O | rpt: *
        ---
        return_type: tuple[VH, ...]: (Visiting Hours, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.10
        """
        return self._c_data[9]

    @visiting_hours.setter  # set LDP.10
    def visiting_hours(self, vh: VH | tuple[VH] | None):
        """
        id: LDP.10 | len: 80 | use: O | rpt: *
        ---
        param_type: VH | tuple[VH, ...]: (Visiting Hours, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.10
        """
        if isinstance(vh, tuple):
            self._c_data[9] = vh
        else:
            self._c_data[9] = (vh,)

    @property  # get LDP.11
    def contact_phone(self) -> XTN | None:
        """
        id: LDP.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.11
        """
        return self._c_data[10][0]

    @contact_phone.setter  # set LDP.11
    def contact_phone(self, xtn: XTN | None):
        """
        id: LDP.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.11
        """
        self._c_data[10] = (xtn,)

    @property  # get LDP.12
    def location_cost_center(self) -> LocationCostCenter | None:
        """
        id: LDP.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.12
        """
        return self._c_data[11][0]

    @location_cost_center.setter  # set LDP.12
    def location_cost_center(self, location_cost_center: LocationCostCenter | None):
        """
        id: LDP.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LDP.12
        """
        self._c_data[11] = (location_cost_center,)
