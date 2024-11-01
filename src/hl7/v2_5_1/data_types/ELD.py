from __future__ import annotations
from ...base import DataType
from .CE import CE
from .ST import ST
from .NM import NM
from ..tables.MessageErrorConditionCodes import MessageErrorConditionCodes


"""
DataType - ELD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::ELD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ELD,
    CE, ST, NM
)

eld = ELD(  # Error Location and Description - Specifies the segment that contains an error and describes the nature of the error
    segment_id=None,  # ST(...) 
    segment_sequence=None,  # NM(...) 
    field_position=None,  # NM(...) 
    code_identifying_error=None,  # CE(...) 
)

-----END COMPOSITE_DATA_TYPE::ELD TEMPLATE-----
"""


class ELD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 493
    _hl7_id = """ELD"""
    _hl7_name = """Error Location and Description"""
    _hl7_description = """Specifies the segment that contains an error and describes the nature of the error"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ELD"
    _c_length = (3, 2, 2, 483,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O",)
    _c_aliases = ("ELD.1", "ELD.2", "ELD.3", "ELD.4",)
    _c_components = (ST, NM, NM, CE,)
    _c_names = ("Segment Id", "Segment Sequence", "Field Position", "Code Identifying Error",)
    _c_attrs = ("segment_id", "segment_sequence", "field_position", "code_identifying_error",)
    # fmt: on

    def __init__(
        self,
        segment_id: ST | None = None,  # ELD.1
        segment_sequence: NM | None = None,  # ELD.2
        field_position: NM | None = None,  # ELD.3
        code_identifying_error: MessageErrorConditionCodes | CE | None = None,  # ELD.4
    ):
        """
        Error Location and Description - `ELD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ELD>`_
        Specifies the segment that contains an error and describes the nature of the error.

        :param segment_id: The segment containing the error in another message (id: ELD.1 | len: 3 | use: O | rpt: 1)
        :param segment_sequence: Specifies the specific occurrence if the segment specified in component 1 occurs more than once in the message (id: ELD.2 | len: 2 | use: O | rpt: 1)
        :param field_position: Ordinal position of the data field within the segment (id: ELD.3 | len: 2 | use: O | rpt: 1)
        :param code_identifying_error: A code that describes the nature of the error (id: ELD.4 | len: 483 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.segment_id = segment_id
        self.segment_sequence = segment_sequence
        self.field_position = field_position
        self.code_identifying_error = code_identifying_error

    @property  # get ELD.1
    def segment_id(self) -> ST | None:
        """
        id: ELD.1 | len: 3 | use: O | rpt: 1
        ---
        The segment containing the error in another message
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ELD.1
        """
        return self._c_data[0][0]

    @segment_id.setter  # set ELD.1
    def segment_id(self, st: ST | None):
        """
        id: ELD.1 | len: 3 | use: O | rpt: 1
        ---
        The segment containing the error in another message
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ELD.1
        """
        self._c_data[0] = (st,)

    @property  # get ELD.2
    def segment_sequence(self) -> NM | None:
        """
        id: ELD.2 | len: 2 | use: O | rpt: 1
        ---
        Specifies the specific occurrence if the segment specified in component 1 occurs more than once in the message.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ELD.2
        """
        return self._c_data[1][0]

    @segment_sequence.setter  # set ELD.2
    def segment_sequence(self, nm: NM | None):
        """
        id: ELD.2 | len: 2 | use: O | rpt: 1
        ---
        Specifies the specific occurrence if the segment specified in component 1 occurs more than once in the message.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ELD.2
        """
        self._c_data[1] = (nm,)

    @property  # get ELD.3
    def field_position(self) -> NM | None:
        """
        id: ELD.3 | len: 2 | use: O | rpt: 1
        ---
        Ordinal position of the data field within the segment. For systems that do not use the HL7 Encoding Rules, the data item number may be used for the third component.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ELD.3
        """
        return self._c_data[2][0]

    @field_position.setter  # set ELD.3
    def field_position(self, nm: NM | None):
        """
        id: ELD.3 | len: 2 | use: O | rpt: 1
        ---
        Ordinal position of the data field within the segment. For systems that do not use the HL7 Encoding Rules, the data item number may be used for the third component.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ELD.3
        """
        self._c_data[2] = (nm,)

    @property  # get ELD.4
    def code_identifying_error(self) -> CE | None:
        """
        id: ELD.4 | len: 483 | use: O | rpt: 1
        ---
        A code that describes the nature of the error. Refer to HL7 Table 0357 - Message error condition codes for valid values.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ELD.4
        """
        return self._c_data[3][0]

    @code_identifying_error.setter  # set ELD.4
    def code_identifying_error(self, ce: CE | None):
        """
        id: ELD.4 | len: 483 | use: O | rpt: 1
        ---
        A code that describes the nature of the error. Refer to HL7 Table 0357 - Message error condition codes for valid values.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ELD.4
        """
        self._c_data[3] = (ce,)
