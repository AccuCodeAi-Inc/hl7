from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..tables.MessageErrorConditionCodes import MessageErrorConditionCodes
from ..tables.AcknowledgmentCode import AcknowledgmentCode


"""
Message Acknowledgment - MSA
HL7 Version: 2.5.1

-----BEGIN SEGMENT::MSA TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MSA,
    ST, CE, ID, NM
)

msa = MSA(  #  - The MSA segment contains information sent while acknowledging another message
    acknowledgment_code=id,  # ID(...)  # Required.
    message_control_id=st,  # ST(...)  # Required.
    text_message=None,  # ST(...) 
    expected_sequence_number=None,  # NM(...) 
    delayed_acknowledgment_type=None,  # ST(...) 
    error_condition=None,  # CE(...) 
)

-----END SEGMENT::MSA TEMPLATE-----
"""


class MSA(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """MSA"""
    _hl7_name = """Message Acknowledgment"""
    _hl7_description = """The MSA segment contains information sent while acknowledging another message"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA"
    _c_length = (2, 20, 80, 15, 0, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "B", "O", "W", "B",)
    _c_components = (ID, ST, ST, NM, ST, CE,)
    _c_aliases = ("MSA.1", "MSA.2", "MSA.3", "MSA.4", "MSA.5", "MSA.6",)
    _c_names = ("Acknowledgment Code", "Message Control ID", "Text Message", "Expected Sequence Number", "Delayed Acknowledgment Type", "Error Condition",)
    _c_attrs = ("acknowledgment_code", "message_control_id", "text_message", "expected_sequence_number", "delayed_acknowledgment_type", "error_condition",)
    # fmt: on

    def __init__(
        self,
        acknowledgment_code: AcknowledgmentCode
        | ID
        | tuple[AcknowledgmentCode | ID, ...],  # MSA.1
        message_control_id: ST | tuple[ST, ...],  # MSA.2
        text_message: ST | tuple[ST, ...] | None = None,  # MSA.3
        expected_sequence_number: NM | tuple[NM, ...] | None = None,  # MSA.4
        delayed_acknowledgment_type: ST | tuple[ST, ...] | None = None,  # MSA.5
        error_condition: MessageErrorConditionCodes
        | CE
        | tuple[MessageErrorConditionCodes | CE, ...]
        | None = None,  # MSA.6
    ):
        """
        Message Acknowledgment - `MSA <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA>`_
        The MSA segment contains information sent while acknowledging another message.

        :param acknowledgment_code: Coded values for HL7 tables (id: MSA.1 | len: 2 | use: R | rpt: 1)
        :param message_control_id: String Data (id: MSA.2 | len: 20 | use: R | rpt: 1)
        :param text_message: String Data (id: MSA.3 | len: 80 | use: B | rpt: 1)
        :param expected_sequence_number: Numeric (id: MSA.4 | len: 15 | use: O | rpt: 1)
        :param delayed_acknowledgment_type: String Data (id: MSA.5 | len: 0 | use: W | rpt: 1)
        :param error_condition: Coded Element (id: MSA.6 | len: 250 | use: B | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.acknowledgment_code = acknowledgment_code
        self.message_control_id = message_control_id
        self.text_message = text_message
        self.expected_sequence_number = expected_sequence_number
        self.delayed_acknowledgment_type = delayed_acknowledgment_type
        self.error_condition = error_condition

    @property  # get MSA.1
    def acknowledgment_code(self) -> AcknowledgmentCode:
        """
        id: MSA.1 | len: 2 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.1
        """
        return self._c_data[0][0]

    @acknowledgment_code.setter  # set MSA.1
    def acknowledgment_code(self, acknowledgment_code: AcknowledgmentCode):
        """
        id: MSA.1 | len: 2 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.1
        """
        self._c_data[0] = (acknowledgment_code,)

    @property  # get MSA.2
    def message_control_id(self) -> ST:
        """
        id: MSA.2 | len: 20 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.2
        """
        return self._c_data[1][0]

    @message_control_id.setter  # set MSA.2
    def message_control_id(self, st: ST):
        """
        id: MSA.2 | len: 20 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.2
        """
        self._c_data[1] = (st,)

    @property  # get MSA.3
    def text_message(self) -> ST | None:
        """
        id: MSA.3 | len: 80 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.3
        """
        return self._c_data[2][0]

    @text_message.setter  # set MSA.3
    def text_message(self, st: ST | None):
        """
        id: MSA.3 | len: 80 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.3
        """
        self._c_data[2] = (st,)

    @property  # get MSA.4
    def expected_sequence_number(self) -> NM | None:
        """
        id: MSA.4 | len: 15 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.4
        """
        return self._c_data[3][0]

    @expected_sequence_number.setter  # set MSA.4
    def expected_sequence_number(self, nm: NM | None):
        """
        id: MSA.4 | len: 15 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.4
        """
        self._c_data[3] = (nm,)

    @property  # get MSA.5
    def delayed_acknowledgment_type(self) -> ST | None:
        """
        id: MSA.5 | len: 0 | use: W | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.5
        """
        return self._c_data[4][0]

    @delayed_acknowledgment_type.setter  # set MSA.5
    def delayed_acknowledgment_type(self, st: ST | None):
        """
        id: MSA.5 | len: 0 | use: W | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.5
        """
        self._c_data[4] = (st,)

    @property  # get MSA.6
    def error_condition(self) -> MessageErrorConditionCodes | None:
        """
        id: MSA.6 | len: 250 | use: B | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.6
        """
        return self._c_data[5][0]

    @error_condition.setter  # set MSA.6
    def error_condition(
        self, message_error_condition_codes: MessageErrorConditionCodes | None
    ):
        """
        id: MSA.6 | len: 250 | use: B | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSA.6
        """
        self._c_data[5] = (message_error_condition_codes,)
