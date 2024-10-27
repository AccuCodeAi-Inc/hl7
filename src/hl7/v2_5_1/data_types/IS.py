from ...base import HL7Primitive, HL7PrimitiveParseException


"""
HL7 Version: 2.5.1
DataType - IS
"""


class IS(str, HL7Primitive):
    """
    IS - Coded value for user-defined tables (len: 20)
    ---
    The value of such a field follows the formatting rules for a ST field except that it is drawn from a site-defined (or user-defined) table of legal values. There shall be an HL7 table number associated with IS data types. An example of an IS field is the Event reason code defined in Section 3.3.1.4, Event reason code. This data type should be used only for user-defined tables (see Section 2.5.3.6 - Table). The reverse is not true, since in some circumstances, it is more appropriate to use the CWE data type for user-defined tables.
    ---
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IS
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 20
    _hl7_id = """IS"""
    _hl7_name = """Coded value for user-defined tables"""
    _hl7_description = """The value of such a field follows the formatting rules for a ST field except that it is drawn from a site-defined (or user-defined) table of legal values"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IS"

    def __new__(cls, is_: str):
        if len(is_) > 20:
            raise HL7PrimitiveParseException(
                "IS - Coded value for user-defined tables content exceeds maximum length of 20 characters"
            )
        return super().__new__(cls, is_)
