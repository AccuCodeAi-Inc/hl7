from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.PL import PL
from ..data_types.CE import CE
from ..data_types.EI import EI
from ..data_types.XON import XON
from ..tables.LocationRelationshipId import LocationRelationshipId
from ..tables.SegmentActionCode import SegmentActionCode


"""
Location Relationship - LRL
HL7 Version: 2.5.1

-----BEGIN SEGMENT::LRL TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    LRL,
    ID, PL, CE, EI, XON
)

lrl = LRL(  #  - The LRL segment is used to identify one location’s relationship to another location, the nearest lab, pharmacy, etc
    primary_key_value_lrl=pl,  # PL(...)  # Required.
    segment_action_code=None,  # ID(...) 
    segment_unique_key=None,  # EI(...) 
    location_relationship_id=ce,  # CE(...)  # Required.
    organizational_location_relationship_value=None,  # XON(...) 
    patient_location_relationship_value=None,  # PL(...) 
)

-----END SEGMENT::LRL TEMPLATE-----
"""


class LRL(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """LRL"""
    _hl7_name = """Location Relationship"""
    _hl7_description = """The LRL segment is used to identify one location’s relationship to another location, the nearest lab, pharmacy, etc"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LRL"
    _c_length = (200, 3, 80, 250, 250, 80,)
    _c_rpt = (1, 1, 1, 1, 65535, 1,)
    _c_usage = ("R", "O", "O", "R", "C", "C",)
    _c_components = (PL, ID, EI, CE, XON, PL,)
    _c_aliases = ("LRL.1", "LRL.2", "LRL.3", "LRL.4", "LRL.5", "LRL.6",)
    _c_names = ("Primary Key Value - LRL", "Segment Action Code", "Segment Unique Key", "Location Relationship ID", "Organizational Location Relationship Value", "Patient Location Relationship Value",)
    _c_attrs = ("primary_key_value_lrl", "segment_action_code", "segment_unique_key", "location_relationship_id", "organizational_location_relationship_value", "patient_location_relationship_value",)
    # fmt: on

    def __init__(
        self,
        primary_key_value_lrl: PL | tuple[PL],  # LRL.1
        location_relationship_id: LocationRelationshipId
        | CE
        | tuple[LocationRelationshipId | CE],  # LRL.4
        segment_action_code: SegmentActionCode
        | ID
        | tuple[SegmentActionCode | ID]
        | None = None,  # LRL.2
        segment_unique_key: EI | tuple[EI] | None = None,  # LRL.3
        organizational_location_relationship_value: XON
        | tuple[XON]
        | None = None,  # LRL.5
        patient_location_relationship_value: PL | tuple[PL] | None = None,  # LRL.6
    ):
        """
        Location Relationship - `LRL <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LRL>`_
        The LRL segment is used to identify one location’s relationship to another location, the nearest lab, pharmacy, etc.

        :param primary_key_value_lrl: Person Location (id: LRL.1 | len: 200 | use: R | rpt: 1)
        :param segment_action_code: Coded values for HL7 tables (id: LRL.2 | len: 3 | use: O | rpt: 1)
        :param segment_unique_key: Entity Identifier (id: LRL.3 | len: 80 | use: O | rpt: 1)
        :param location_relationship_id: Coded Element (id: LRL.4 | len: 250 | use: R | rpt: 1)
        :param organizational_location_relationship_value: Extended Composite Name and Identification Number for Organizations (id: LRL.5 | len: 250 | use: C | rpt: *)
        :param patient_location_relationship_value: Person Location (id: LRL.6 | len: 80 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.primary_key_value_lrl = primary_key_value_lrl
        self.segment_action_code = segment_action_code
        self.segment_unique_key = segment_unique_key
        self.location_relationship_id = location_relationship_id
        self.organizational_location_relationship_value = (
            organizational_location_relationship_value
        )
        self.patient_location_relationship_value = patient_location_relationship_value

    @property  # get LRL.1
    def primary_key_value_lrl(self) -> PL:
        """
        id: LRL.1 | len: 200 | use: R | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.1
        """
        return self._c_data[0][0]

    @primary_key_value_lrl.setter  # set LRL.1
    def primary_key_value_lrl(self, pl: PL):
        """
        id: LRL.1 | len: 200 | use: R | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.1
        """
        self._c_data[0] = (pl,)

    @property  # get LRL.2
    def segment_action_code(self) -> SegmentActionCode | None:
        """
        id: LRL.2 | len: 3 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.2
        """
        return self._c_data[1][0]

    @segment_action_code.setter  # set LRL.2
    def segment_action_code(self, segment_action_code: SegmentActionCode | None):
        """
        id: LRL.2 | len: 3 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.2
        """
        self._c_data[1] = (segment_action_code,)

    @property  # get LRL.3
    def segment_unique_key(self) -> EI | None:
        """
        id: LRL.3 | len: 80 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.3
        """
        return self._c_data[2][0]

    @segment_unique_key.setter  # set LRL.3
    def segment_unique_key(self, ei: EI | None):
        """
        id: LRL.3 | len: 80 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.3
        """
        self._c_data[2] = (ei,)

    @property  # get LRL.4
    def location_relationship_id(self) -> LocationRelationshipId:
        """
        id: LRL.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.4
        """
        return self._c_data[3][0]

    @location_relationship_id.setter  # set LRL.4
    def location_relationship_id(
        self, location_relationship_id: LocationRelationshipId
    ):
        """
        id: LRL.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.4
        """
        self._c_data[3] = (location_relationship_id,)

    @property
    def organizational_location_relationship_value(
        self,
    ) -> tuple[XON, ...] | tuple[None]:
        """
        id: LRL.5 | len: 250 | use: C | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.5
        """
        return self._c_data[4]

    @organizational_location_relationship_value.setter  # set LRL.5
    def organizational_location_relationship_value(self, xon: XON | tuple[XON] | None):
        """
        id: LRL.5 | len: 250 | use: C | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.5
        """
        if isinstance(xon, tuple):
            self._c_data[4] = xon
        else:
            self._c_data[4] = (xon,)

    @property  # get LRL.6
    def patient_location_relationship_value(self) -> PL | None:
        """
        id: LRL.6 | len: 80 | use: C | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.6
        """
        return self._c_data[5][0]

    @patient_location_relationship_value.setter  # set LRL.6
    def patient_location_relationship_value(self, pl: PL | None):
        """
        id: LRL.6 | len: 80 | use: C | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LRL.6
        """
        self._c_data[5] = (pl,)
