from ...base import HL7Primitive, HL7PrimitiveParseException


"""
HL7 Version: 2.5.1
DataType - GTS
"""


class GTS(str, HL7Primitive):
    """
    GTS - General Timing Specification (len: 199)
    ---
    The General Timing Specification data type is used to communicate complex inter-related information Timing information. The value of such a field follows the formatting rules for a ST field. The string data will be structured according to the rules set forth in the Version 3 Data Types Part II Unabridged Specification for the General Timing Specification (GTS) data type.
    ---
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GTS
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 199
    _hl7_id = """GTS"""
    _hl7_name = """General Timing Specification"""
    _hl7_description = """The General Timing Specification data type is used to communicate complex inter-related information Timing information"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GTS"

    def __new__(cls, gts: str):
        if len(gts) > 199:
            raise HL7PrimitiveParseException(
                "GTS - General Timing Specification content exceeds maximum length of 199 characters"
            )
        return super().__new__(cls, gts)
