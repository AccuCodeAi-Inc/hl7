from ...base import HL7Primitive, HL7PrimitiveParseException


"""
HL7 Version: 2.5.1
DataType - ST
"""


class ST(str, HL7Primitive):
    """
        ST - String Data (len: 199)
        ---
        String data is left justified with trailing blanks optional. Any displayable (printable) ACSII characters (hexadecimal values between 20 and 7E, inclusive, or ASCII decimal values between 32 and 126), except the defined escape characters and defined delimiter characters.

    Example: |almost any data at all|

    Usage note: The ST data type is intended for short strings (e.g., less than 200 characters). For longer strings the TX or FT data types should be used (see Sections 2.A.78, “TX - text data” or 2.A.31, “FT - formatted text data”).
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ST
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 199
    _hl7_id = """ST"""
    _hl7_name = """String Data"""
    _hl7_description = """String data is left justified with trailing blanks optional"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ST"

    def __new__(cls, st: str):
        if len(st) > 199:
            raise HL7PrimitiveParseException(
                "ST - String Data content exceeds maximum length of 199 characters"
            )
        return super().__new__(cls, st)
