from __future__ import annotations
from ...base import DataType
from .NM import NM
from .ST import ST


"""
DataType - ERL
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::ERL TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ERL,
    NM, ST
)

erl = ERL(  # Error Location - This data type identifies the segment and its constituent where an error has occurred
    segment_id=st,  # ST(...)  # Required.
    segment_sequence=nm,  # NM(...)  # Required.
    field_position=None,  # NM(...) 
    field_repetition=None,  # NM(...) 
    component_number=None,  # NM(...) 
    sub_component_number=None,  # NM(...) 
)

-----END COMPOSITE_DATA_TYPE::ERL TEMPLATE-----
"""


class ERL(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 18
    _hl7_id = """ERL"""
    _hl7_name = """Error Location"""
    _hl7_description = """This data type identifies the segment and its constituent where an error has occurred"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL"
    _c_length = (3, 2, 2, 2, 2, 2,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "O", "O", "O", "O",)
    _c_aliases = ("ERL.1", "ERL.2", "ERL.3", "ERL.4", "ERL.5", "ERL.6",)
    _c_components = (ST, NM, NM, NM, NM, NM,)
    _c_names = ("Segment Id", "Segment Sequence", "Field Position", "Field Repetition", "Component Number", "Sub-component Number",)
    _c_attrs = ("segment_id", "segment_sequence", "field_position", "field_repetition", "component_number", "sub_component_number",)
    # fmt: on

    def __init__(
        self,
        segment_id: ST | tuple[ST],  # ERL.1
        segment_sequence: NM | tuple[NM],  # ERL.2
        field_position: NM | tuple[NM] | None = None,  # ERL.3
        field_repetition: NM | tuple[NM] | None = None,  # ERL.4
        component_number: NM | tuple[NM] | None = None,  # ERL.5
        sub_component_number: NM | tuple[NM] | None = None,  # ERL.6
    ):
        """
        Error Location - `ERL <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERL>`_
        This data type identifies the segment and its constituent where an error has occurred.

        :param segment_id: Specifies the 3-letter name for the segment (id: ERL.1 | len: 3 | use: R | rpt: 1)
        :param segment_sequence: Identifies the segment occurrence within the message (id: ERL.2 | len: 2 | use: R | rpt: 1)
        :param field_position: Identifies the number of the field within the segment (id: ERL.3 | len: 2 | use: O | rpt: 1)
        :param field_repetition: Identifies the repetition number of the field (id: ERL.4 | len: 2 | use: O | rpt: 1)
        :param component_number: Identifies the number of the component within the field (id: ERL.5 | len: 2 | use: O | rpt: 1)
        :param sub_component_number: Identifies the number of the sub-component within the component (id: ERL.6 | len: 2 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.segment_id = segment_id
        self.segment_sequence = segment_sequence
        self.field_position = field_position
        self.field_repetition = field_repetition
        self.component_number = component_number
        self.sub_component_number = sub_component_number

    @property  # get ERL.1
    def segment_id(self) -> ST:
        """
        id: ERL.1 | len: 3 | use: R | rpt: 1
        ---
        Specifies the 3-letter name for the segment.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.1
        """
        return self._c_data[0][0]

    @segment_id.setter  # set ERL.1
    def segment_id(self, st: ST):
        """
        id: ERL.1 | len: 3 | use: R | rpt: 1
        ---
        Specifies the 3-letter name for the segment.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.1
        """
        self._c_data[0] = (st,)

    @property  # get ERL.2
    def segment_sequence(self) -> NM:
        """
        id: ERL.2 | len: 2 | use: R | rpt: 1
        ---
        Identifies the segment occurrence within the message.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.2
        """
        return self._c_data[1][0]

    @segment_sequence.setter  # set ERL.2
    def segment_sequence(self, nm: NM):
        """
        id: ERL.2 | len: 2 | use: R | rpt: 1
        ---
        Identifies the segment occurrence within the message.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.2
        """
        self._c_data[1] = (nm,)

    @property  # get ERL.3
    def field_position(self) -> NM | None:
        """
        id: ERL.3 | len: 2 | use: O | rpt: 1
        ---
        Identifies the number of the field within the segment. The first field is assigned a number of 1. Field number should not be specified when referring to the entire segment.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.3
        """
        return self._c_data[2][0]

    @field_position.setter  # set ERL.3
    def field_position(self, nm: NM | None):
        """
        id: ERL.3 | len: 2 | use: O | rpt: 1
        ---
        Identifies the number of the field within the segment. The first field is assigned a number of 1. Field number should not be specified when referring to the entire segment.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.3
        """
        self._c_data[2] = (nm,)

    @property  # get ERL.4
    def field_repetition(self) -> NM | None:
        """
        id: ERL.4 | len: 2 | use: O | rpt: 1
        ---
        Identifies the repetition number of the field. The first repetition is counted as 1. If a Field Position is specified, but Field Repetition is not, Field Repetition should be assumed to be 1. If Field Position is not specified, Field Repetition should not be specified.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.4
        """
        return self._c_data[3][0]

    @field_repetition.setter  # set ERL.4
    def field_repetition(self, nm: NM | None):
        """
        id: ERL.4 | len: 2 | use: O | rpt: 1
        ---
        Identifies the repetition number of the field. The first repetition is counted as 1. If a Field Position is specified, but Field Repetition is not, Field Repetition should be assumed to be 1. If Field Position is not specified, Field Repetition should not be specified.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.4
        """
        self._c_data[3] = (nm,)

    @property  # get ERL.5
    def component_number(self) -> NM | None:
        """
        id: ERL.5 | len: 2 | use: O | rpt: 1
        ---
        Identifies the number of the component within the field. The first component is assigned a number of 1. Component number should not be specified when referring to the entire field.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.5
        """
        return self._c_data[4][0]

    @component_number.setter  # set ERL.5
    def component_number(self, nm: NM | None):
        """
        id: ERL.5 | len: 2 | use: O | rpt: 1
        ---
        Identifies the number of the component within the field. The first component is assigned a number of 1. Component number should not be specified when referring to the entire field.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.5
        """
        self._c_data[4] = (nm,)

    @property  # get ERL.6
    def sub_component_number(self) -> NM | None:
        """
        id: ERL.6 | len: 2 | use: O | rpt: 1
        ---
        Identifies the number of the sub-component within the component. The first sub-component is assigned a number of 1. Sub-component number should not be specified when referring to the entire component.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.6
        """
        return self._c_data[5][0]

    @sub_component_number.setter  # set ERL.6
    def sub_component_number(self, nm: NM | None):
        """
        id: ERL.6 | len: 2 | use: O | rpt: 1
        ---
        Identifies the number of the sub-component within the component. The first sub-component is assigned a number of 1. Sub-component number should not be specified when referring to the entire component.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERL.6
        """
        self._c_data[5] = (nm,)
