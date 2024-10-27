from ...base import HL7Primitive, HL7PrimitiveParseException


"""
HL7 Version: 2.5.1
DataType - TX
"""


class TX(str, HL7Primitive):
    """
        TX - Text Data (len: 0)
        ---
        String data meant for user display (on a terminal or printer). Such data would not necessarily be left justified since leading spaces may contribute greatly to the clarity of the presentation to the user. Because this type of data is intended for display, it may contain certain escape character sequences designed to control the display. Escape sequence formatting is defined in Section 2.7 Use of escape sequences in text fields . Leading spaces should be included. Trailing spaces should be removed.

    Example: |  leading spaces are allowed.|
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TX
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 0
    _hl7_id = """TX"""
    _hl7_name = """Text Data"""
    _hl7_description = (
        """String data meant for user display (on a terminal or printer)"""
    )
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TX"

    def __new__(cls, tx: str):
        return super().__new__(cls, tx)
