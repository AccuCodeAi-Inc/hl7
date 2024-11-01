from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.EI import EI
from ..data_types.PL import PL
from ..data_types.CE import CE
from ..tables.SegmentActionCode import SegmentActionCode
from ..tables.LocationCharacteristicId import LocationCharacteristicId


"""
Location Characteristic - LCH
HL7 Version: 2.5.1

-----BEGIN SEGMENT::LCH TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    LCH,
    ID, EI, PL, CE
)

lch = LCH(  #  - The LCH segment is used to identify location characteristics which determine which patients will be assigned to the room or bed
    primary_key_value_lch=pl,  # PL(...)  # Required.
    segment_action_code=None,  # ID(...) 
    segment_unique_key=None,  # EI(...) 
    location_characteristic_id=ce,  # CE(...)  # Required.
    location_characteristic_value_lch=ce,  # CE(...)  # Required.
)

-----END SEGMENT::LCH TEMPLATE-----
"""


class LCH(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """LCH"""
    _hl7_name = """Location Characteristic"""
    _hl7_description = """The LCH segment is used to identify location characteristics which determine which patients will be assigned to the room or bed"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCH"
    _c_length = (200, 3, 80, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "R", "R",)
    _c_components = (PL, ID, EI, CE, CE,)
    _c_aliases = ("LCH.1", "LCH.2", "LCH.3", "LCH.4", "LCH.5",)
    _c_names = ("Primary Key Value - LCH", "Segment Action Code", "Segment Unique Key", "Location Characteristic ID", "Location Characteristic Value-LCH",)
    _c_attrs = ("primary_key_value_lch", "segment_action_code", "segment_unique_key", "location_characteristic_id", "location_characteristic_value_lch",)
    # fmt: on

    def __init__(
        self,
        primary_key_value_lch: PL | tuple[PL],  # LCH.1
        location_characteristic_id: LocationCharacteristicId
        | CE
        | tuple[LocationCharacteristicId | CE],  # LCH.4
        location_characteristic_value_lch: CE | tuple[CE],  # LCH.5
        segment_action_code: SegmentActionCode
        | ID
        | tuple[SegmentActionCode | ID]
        | None = None,  # LCH.2
        segment_unique_key: EI | tuple[EI] | None = None,  # LCH.3
    ):
        """
                Location Characteristic - `LCH <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LCH>`_
                The LCH segment is used to identify location characteristics which determine which patients will be assigned to the room or bed.  It contains the location characteristics of the room or bed identified in the preceding LOC segment. There should be one LCH segment for each attribute.

        When the LCH segment appears immediately following the LOC segment, it communicates characteristics which are the same across multiple departments that may use the same room.  When the LCH segment appears immediately following the LDP segment, it communicates characteristics which differ for different departments that may use the same room.  For example, the following characteristics are more likely to vary by which department is using the room: teaching, gender, staffed, set up, overflow, whereas the other characteristics are likely to remain the same.

                :param primary_key_value_lch: Person Location (id: LCH.1 | len: 200 | use: R | rpt: 1)
                :param segment_action_code: Coded values for HL7 tables (id: LCH.2 | len: 3 | use: O | rpt: 1)
                :param segment_unique_key: Entity Identifier (id: LCH.3 | len: 80 | use: O | rpt: 1)
                :param location_characteristic_id: Coded Element (id: LCH.4 | len: 250 | use: R | rpt: 1)
                :param location_characteristic_value_lch: Coded Element (id: LCH.5 | len: 250 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.primary_key_value_lch = primary_key_value_lch
        self.segment_action_code = segment_action_code
        self.segment_unique_key = segment_unique_key
        self.location_characteristic_id = location_characteristic_id
        self.location_characteristic_value_lch = location_characteristic_value_lch

    @property  # get LCH.1
    def primary_key_value_lch(self) -> PL:
        """
        id: LCH.1 | len: 200 | use: R | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCH.1
        """
        return self._c_data[0][0]

    @primary_key_value_lch.setter  # set LCH.1
    def primary_key_value_lch(self, pl: PL):
        """
        id: LCH.1 | len: 200 | use: R | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCH.1
        """
        self._c_data[0] = (pl,)

    @property  # get LCH.2
    def segment_action_code(self) -> SegmentActionCode | None:
        """
        id: LCH.2 | len: 3 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCH.2
        """
        return self._c_data[1][0]

    @segment_action_code.setter  # set LCH.2
    def segment_action_code(self, segment_action_code: SegmentActionCode | None):
        """
        id: LCH.2 | len: 3 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCH.2
        """
        self._c_data[1] = (segment_action_code,)

    @property  # get LCH.3
    def segment_unique_key(self) -> EI | None:
        """
        id: LCH.3 | len: 80 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCH.3
        """
        return self._c_data[2][0]

    @segment_unique_key.setter  # set LCH.3
    def segment_unique_key(self, ei: EI | None):
        """
        id: LCH.3 | len: 80 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCH.3
        """
        self._c_data[2] = (ei,)

    @property  # get LCH.4
    def location_characteristic_id(self) -> LocationCharacteristicId:
        """
        id: LCH.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCH.4
        """
        return self._c_data[3][0]

    @location_characteristic_id.setter  # set LCH.4
    def location_characteristic_id(
        self, location_characteristic_id: LocationCharacteristicId
    ):
        """
        id: LCH.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCH.4
        """
        self._c_data[3] = (location_characteristic_id,)

    @property  # get LCH.5
    def location_characteristic_value_lch(self) -> CE:
        """
        id: LCH.5 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCH.5
        """
        return self._c_data[4][0]

    @location_characteristic_value_lch.setter  # set LCH.5
    def location_characteristic_value_lch(self, ce: CE):
        """
        id: LCH.5 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LCH.5
        """
        self._c_data[4] = (ce,)
