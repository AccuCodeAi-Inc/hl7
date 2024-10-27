from __future__ import annotations
from ...base import DataType
from .ID import ID
from ..tables.MessageType import MessageType
from ..tables.EventType import EventType
from ..tables.MessageStructure import MessageStructure


"""
DataType - MSG
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::MSG TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MSG,
    ID
)

msg = MSG(  # Message Type - This field contains the message type, trigger event, and the message structure ID for the message
    message_code=id,  # ID(...)  # Required.
    trigger_event=id,  # ID(...)  # Required.
    message_structure=id,  # ID(...)  # Required.
)

-----END COMPOSITE_DATA_TYPE::MSG TEMPLATE-----
"""


class MSG(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 0
    _hl7_id = """MSG"""
    _hl7_name = """Message Type"""
    _hl7_description = """This field contains the message type, trigger event, and the message structure ID for the message"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSG"
    _c_length = (3, 3, 7,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("R", "R", "R",)
    _c_aliases = ("MSG.1", "MSG.2", "MSG.3",)
    _c_components = (ID, ID, ID,)
    _c_names = ("Message Code", "Trigger Event", "Message Structure",)
    _c_attrs = ("message_code", "trigger_event", "message_structure",)
    # fmt: on

    def __init__(
        self,
        message_code: MessageType | ID,  # MSG.1
        trigger_event: EventType | ID,  # MSG.2
        message_structure: MessageStructure | ID,  # MSG.3
    ):
        """
        Message Type - `MSG <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSG>`_
        This field contains the message type, trigger event, and the message structure ID for the message.

        :param message_code: Specifies the message type code (id: MSG.1 | len: 3 | use: R | rpt: 1)
        :param trigger_event: Specifies the trigger event code (id: MSG.2 | len: 3 | use: R | rpt: 1)
        :param message_structure: Specifies the abstract message structure code (id: MSG.3 | len: 7 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.message_code = message_code
        self.trigger_event = trigger_event
        self.message_structure = message_structure

    @property  # get MSG.1
    def message_code(self) -> MessageType:
        """
        id: MSG.1 | len: 3 | use: R | rpt: 1
        ---
        Specifies the message type code. Refer to HL7 Table - Message Type in section 2.17.1 for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSG.1
        """
        return self._c_data[0][0]

    @message_code.setter  # set MSG.1
    def message_code(self, message_type: MessageType):
        """
        id: MSG.1 | len: 3 | use: R | rpt: 1
        ---
        Specifies the message type code. Refer to HL7 Table - Message Type in section 2.17.1 for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSG.1
        """
        self._c_data[0] = (message_type,)

    @property  # get MSG.2
    def trigger_event(self) -> EventType:
        """
        id: MSG.2 | len: 3 | use: R | rpt: 1
        ---
        Specifies the trigger event code. Refer to HL7 Table - Event Type in section 2.17.2 for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSG.2
        """
        return self._c_data[1][0]

    @trigger_event.setter  # set MSG.2
    def trigger_event(self, event_type: EventType):
        """
        id: MSG.2 | len: 3 | use: R | rpt: 1
        ---
        Specifies the trigger event code. Refer to HL7 Table - Event Type in section 2.17.2 for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSG.2
        """
        self._c_data[1] = (event_type,)

    @property  # get MSG.3
    def message_structure(self) -> MessageStructure:
        """
        id: MSG.3 | len: 7 | use: R | rpt: 1
        ---
        Specifies the abstract message structure code. Refer to HL7 Table 0354 - Message Structure in section 2.17.3 for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSG.3
        """
        return self._c_data[2][0]

    @message_structure.setter  # set MSG.3
    def message_structure(self, message_structure: MessageStructure):
        """
        id: MSG.3 | len: 7 | use: R | rpt: 1
        ---
        Specifies the abstract message structure code. Refer to HL7 Table 0354 - Message Structure in section 2.17.3 for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSG.3
        """
        self._c_data[2] = (message_structure,)
