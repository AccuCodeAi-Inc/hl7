from ...base import HL7Primitive, HL7PrimitiveParseException


"""
HL7 Version: 2.5.1
DataType - VARIES
"""


class VARIES(str, HL7Primitive):
    """
    VARIES - Variable Datatype (len: 0)
    ---

    ---
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VARIES
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 0
    _hl7_id = """VARIES"""
    _hl7_name = """Variable Datatype"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VARIES"

    def __new__(cls, varies: str):
        return super().__new__(cls, varies)
