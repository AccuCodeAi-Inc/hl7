from ...base import HL7Primitive, HL7PrimitiveParseException


"""
HL7 Version: 2.5.1
DataType - SI
"""


class SI(str, HL7Primitive):
    """
        SI - Sequence ID (len: 0)
        ---
        A non-negative integer in the form of a NM field. The uses of this data type are defined in the chapters defining the segments and messages in which it appears.

    Maximum Length: 4. This allows for a number between 0 and 9999 to be specified
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SI
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 0
    _hl7_id = """SI"""
    _hl7_name = """Sequence ID"""
    _hl7_description = """A non-negative integer in the form of a NM field"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SI"

    def __new__(cls, si: str):
        return super().__new__(cls, si)
