from ...base import HL7Primitive, HL7PrimitiveParseException


"""
HL7 Version: 2.5.1
DataType - DTM
"""


class DTM(str, HL7Primitive):
    """
        DTM - Date/Time (len: 24)
        ---
        Specifies a point in time using a 24-hour clock notation.

    Format: YYYY[MM[DD[HH[MM[SS[.S[S[S[S]]]]]]]]][+/-ZZZZ].
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DTM
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 24
    _hl7_id = """DTM"""
    _hl7_name = """Date/Time"""
    _hl7_description = """Specifies a point in time using a 24-hour clock notation"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DTM"

    def __new__(cls, dtm: str):
        if len(dtm) > 24:
            raise HL7PrimitiveParseException(
                "DTM - Date/Time content exceeds maximum length of 24 characters"
            )
        return super().__new__(cls, dtm)
