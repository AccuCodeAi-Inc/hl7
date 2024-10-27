from ...base import HL7Table

"""
HL7 Version: 2.5.1
Message error condition codes - 0357
Table Type: HL7
"""


class MessageErrorConditionCodes(HL7Table):
    """
    Message error condition codes - 0357 // HL7 table type
    - MESSAGE_ACCEPTED
    - SEGMENT_SEQUENCE_ERROR
    - REQUIRED_FIELD_MISSING
    - DATA_TYPE_ERROR
    - TABLE_VALUE_NOT_FOUND
    - UNSUPPORTED_MESSAGE_TYPE
    - UNSUPPORTED_EVENT_CODE
    - UNSUPPORTED_PROCESSING_ID
    - UNSUPPORTED_VERSION_ID
    - UNKNOWN_KEY_IDENTIFIER
    - DUPLICATE_KEY_IDENTIFIER
    - APPLICATION_RECORD_LOCKED
    - APPLICATION_INTERNAL_ERROR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0357
    """

    MESSAGE_ACCEPTED = "0"  # Success. Optional, as the AA conveys success. Used for systems that must always return a status code.
    """Message accepted"""
    SEGMENT_SEQUENCE_ERROR = "100"  # Error: The message segments were not in the proper order, or required segments are missing.
    """Segment sequence error"""
    REQUIRED_FIELD_MISSING = "101"  # Error: A required field is missing from a segment
    """Required field missing"""
    DATA_TYPE_ERROR = "102"  # Error: The field contained data of the wrong data type, e.g. an NM field contained FOO.
    """Data type error"""
    TABLE_VALUE_NOT_FOUND = "103"  # Error: A field of data type ID or IS was compared against the corresponding table, and no match was found.
    """Table value not found"""
    UNSUPPORTED_MESSAGE_TYPE = "200"  # Rejection: The Message Type is not supported.
    """Unsupported message type"""
    UNSUPPORTED_EVENT_CODE = "201"  # Rejection: The Event Code is not supported.
    """Unsupported event code"""
    UNSUPPORTED_PROCESSING_ID = "202"  # Rejection: The Processing ID is not supported.
    """Unsupported processing id"""
    UNSUPPORTED_VERSION_ID = "203"  # Rejection:  The Version ID is not supported.
    """Unsupported version id"""
    UNKNOWN_KEY_IDENTIFIER = "204"  # Rejection: The ID of the patient, order, etc., was not found. Used for transactions other than additions, e.g. transfer of a non-existent patient.
    """Unknown key identifier"""
    DUPLICATE_KEY_IDENTIFIER = "205"  # Rejection: The ID of the patient, order, etc., already exists. Used in response to addition transactions (Admit, New Order, etc.).
    """Duplicate key identifier"""
    APPLICATION_RECORD_LOCKED = "206"  # Rejection: The transaction could not be performed at the application storage level, e.g., database locked.
    """Application record locked"""
    APPLICATION_INTERNAL_ERROR = "207"  # Rejection: A catchall for internal errors not explicitly covered by other codes.
    """Application internal error"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MessageErrorConditionCodes.MESSAGE_ACCEPTED: "Message accepted",
    MessageErrorConditionCodes.SEGMENT_SEQUENCE_ERROR: "Segment sequence error",
    MessageErrorConditionCodes.REQUIRED_FIELD_MISSING: "Required field missing",
    MessageErrorConditionCodes.DATA_TYPE_ERROR: "Data type error",
    MessageErrorConditionCodes.TABLE_VALUE_NOT_FOUND: "Table value not found",
    MessageErrorConditionCodes.UNSUPPORTED_MESSAGE_TYPE: "Unsupported message type",
    MessageErrorConditionCodes.UNSUPPORTED_EVENT_CODE: "Unsupported event code",
    MessageErrorConditionCodes.UNSUPPORTED_PROCESSING_ID: "Unsupported processing id",
    MessageErrorConditionCodes.UNSUPPORTED_VERSION_ID: "Unsupported version id",
    MessageErrorConditionCodes.UNKNOWN_KEY_IDENTIFIER: "Unknown key identifier",
    MessageErrorConditionCodes.DUPLICATE_KEY_IDENTIFIER: "Duplicate key identifier",
    MessageErrorConditionCodes.APPLICATION_RECORD_LOCKED: "Application record locked",
    MessageErrorConditionCodes.APPLICATION_INTERNAL_ERROR: "Application internal error",
}
