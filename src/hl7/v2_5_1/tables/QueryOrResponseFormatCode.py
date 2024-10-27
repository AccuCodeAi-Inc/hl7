from ...base import HL7Table

"""
HL7 Version: 2.5.1
Query/response format code - 0106
Table Type: HL7
"""


class QueryOrResponseFormatCode(HL7Table):
    """
    Query/response format code - 0106 // HL7 table type
    - RESPONSE_IS_IN_DISPLAY_FORMAT
    - RESPONSE_IS_IN_RECORD_ORIENTED_FORMAT
    - RESPONSE_IS_IN_TABULAR_FORMAT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0106
    """

    RESPONSE_IS_IN_DISPLAY_FORMAT = "D"
    """Response is in display format"""
    RESPONSE_IS_IN_RECORD_ORIENTED_FORMAT = "R"
    """Response is in record-oriented format"""
    RESPONSE_IS_IN_TABULAR_FORMAT = "T"
    """Response is in tabular format"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    QueryOrResponseFormatCode.RESPONSE_IS_IN_DISPLAY_FORMAT: "Response is in display format",
    QueryOrResponseFormatCode.RESPONSE_IS_IN_RECORD_ORIENTED_FORMAT: "Response is in record-oriented format",
    QueryOrResponseFormatCode.RESPONSE_IS_IN_TABULAR_FORMAT: "Response is in tabular format",
}
