from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.PL import PL
from ..tables.TransactionCode import TransactionCode
from ..tables.LocationDepartment import LocationDepartment
from ..tables.AccommodationCode import AccommodationCode


"""
Location Charge Code - LCC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::LCC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    LCC,
    CE, PL
)

lcc = LCC(  #  - The optional LCC segment identifies how a patient location room can be billed by a certain department
    primary_key_value_lcc=pl,  # PL(...)  # Required.
    location_department=ce,  # CE(...)  # Required.
    accommodation_type=None,  # CE(...) 
    charge_code=ce,  # CE(...)  # Required.
)

-----END SEGMENT::LCC TEMPLATE-----
"""


class LCC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """LCC"""
    _hl7_name = """Location Charge Code"""
    _hl7_description = """The optional LCC segment identifies how a patient location room can be billed by a certain department"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCC"
    _c_length = (200, 250, 250, 250,)
    _c_rpt = (1, 1, 65535, 65535,)
    _c_usage = ("R", "R", "O", "R",)
    _c_components = (PL, CE, CE, CE,)
    _c_aliases = ("LCC.1", "LCC.2", "LCC.3", "LCC.4",)
    _c_names = ("Primary Key Value - LCC", "Location Department", "Accommodation Type", "Charge Code",)
    _c_attrs = ("primary_key_value_lcc", "location_department", "accommodation_type", "charge_code",)
    # fmt: on

    def __init__(
        self,
        primary_key_value_lcc: PL,  # LCC.1
        location_department: LocationDepartment | CE,  # LCC.2
        charge_code: TransactionCode | CE,  # LCC.4
        accommodation_type: AccommodationCode | CE | None = None,  # LCC.3
    ):
        """
        Location Charge Code - `LCC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCC>`_
        The optional LCC segment identifies how a patient location room can be billed by a certain department.  A department can use different charge codes for the same room or bed, so there can be multiple LCC segments following an LDP segment.

        :param primary_key_value_lcc: Person Location (id: LCC.1 | len: 200 | use: R | rpt: 1)
        :param location_department: Coded Element (id: LCC.2 | len: 250 | use: R | rpt: 1)
        :param accommodation_type: Coded Element (id: LCC.3 | len: 250 | use: O | rpt: *)
        :param charge_code: Coded Element (id: LCC.4 | len: 250 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.primary_key_value_lcc = primary_key_value_lcc
        self.location_department = location_department
        self.accommodation_type = accommodation_type
        self.charge_code = charge_code

    @property  # get LCC.1
    def primary_key_value_lcc(self) -> PL:
        """
        id: LCC.1 | len: 200 | use: R | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCC.1
        """
        return self._c_data[0][0]

    @primary_key_value_lcc.setter  # set LCC.1
    def primary_key_value_lcc(self, pl: PL):
        """
        id: LCC.1 | len: 200 | use: R | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCC.1
        """
        self._c_data[0] = (pl,)

    @property  # get LCC.2
    def location_department(self) -> LocationDepartment:
        """
        id: LCC.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCC.2
        """
        return self._c_data[1][0]

    @location_department.setter  # set LCC.2
    def location_department(self, location_department: LocationDepartment):
        """
        id: LCC.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCC.2
        """
        self._c_data[1] = (location_department,)

    @property
    def accommodation_type(self) -> tuple[AccommodationCode, ...] | tuple[None]:
        """
        id: LCC.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCC.3
        """
        return self._c_data[2]

    @accommodation_type.setter  # set LCC.3
    def accommodation_type(
        self, accommodation_code: AccommodationCode | tuple[AccommodationCode] | None
    ):
        """
        id: LCC.3 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCC.3
        """
        if isinstance(accommodation_code, tuple):
            self._c_data[2] = accommodation_code
        else:
            self._c_data[2] = (accommodation_code,)

    @property
    def charge_code(self) -> tuple[TransactionCode, ...]:
        """
        id: LCC.4 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCC.4
        """
        return self._c_data[3]

    @charge_code.setter  # set LCC.4
    def charge_code(self, transaction_code: TransactionCode | tuple[TransactionCode]):
        """
        id: LCC.4 | len: 250 | use: R | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCC.4
        """
        if isinstance(transaction_code, tuple):
            self._c_data[3] = transaction_code
        else:
            self._c_data[3] = (transaction_code,)
