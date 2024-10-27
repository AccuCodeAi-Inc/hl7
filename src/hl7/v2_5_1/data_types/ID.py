from ...base import HL7Primitive, HL7PrimitiveParseException


"""
HL7 Version: 2.5.1
DataType - ID
"""


class ID(str, HL7Primitive):
    """
    ID - Coded values for HL7 tables (len: 0)
    ---
    The value of such a field follows the formatting rules for an ST field except that it is drawn from a table of legal values. There shall be an HL7 table number associated with ID data types. An example of an ID field is OBR-25-result status. This data type should be used only for HL7 tables (see Section 2.5.3.6 -Table). The reverse is not true, since in some circumstances it is more appropriate to use the CNE or CWE data type for HL7 tables.
    ---
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ID
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 0
    _hl7_id = """ID"""
    _hl7_name = """Coded values for HL7 tables"""
    _hl7_description = """The value of such a field follows the formatting rules for an ST field except that it is drawn from a table of legal values"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ID"

    def __new__(cls, id: str):
        return super().__new__(cls, id)
