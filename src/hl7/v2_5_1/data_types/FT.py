from ...base import HL7Primitive, HL7PrimitiveParseException


"""
HL7 Version: 2.5.1
DataType - FT
"""


class FT(str, HL7Primitive):
    """
        FT - Formatted Text Data (len: 65536)
        ---
        This data type is derived from the string data type by allowing the addition of embedded formatting instructions. These instructions are limited to those that are intrinsic and independent of the circumstances under which the field is being used. The actual instructions and their representation are described elsewhere in this chapter. The FT field is of arbitrary length (up to 64k) and may contain formatting commands enclosed in escape characters.

    Example: |\.sp\(skip one vertical line)|
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 65536
    _hl7_id = """FT"""
    _hl7_name = """Formatted Text Data"""
    _hl7_description = """This data type is derived from the string data type by allowing the addition of embedded formatting instructions"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT"

    def __new__(cls, ft: str):
        if len(ft) > 65536:
            raise HL7PrimitiveParseException(
                "FT - Formatted Text Data content exceeds maximum length of 65536 characters"
            )
        return super().__new__(cls, ft)
