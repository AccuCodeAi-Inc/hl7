from ...base import HL7Table

"""
HL7 Version: 2.5.1
Query Response Status - 0208
Table Type: HL7
"""


class QueryResponseStatus(HL7Table):
    """
    Query Response Status - 0208 // HL7 table type
    - APPLICATION_ERROR
    - APPLICATION_REJECT
    - NO_DATA_FOUND_NO_ERRORS
    - DATA_FOUND_NO_ERRORS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0208
    """

    APPLICATION_ERROR = "AE"
    """Application error"""
    APPLICATION_REJECT = "AR"
    """Application reject"""
    NO_DATA_FOUND_NO_ERRORS = "NF"
    """No data found, no errors"""
    DATA_FOUND_NO_ERRORS = "OK"
    """Data found, no errors (this is the default)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    QueryResponseStatus.APPLICATION_ERROR: "Application error",
    QueryResponseStatus.APPLICATION_REJECT: "Application reject",
    QueryResponseStatus.NO_DATA_FOUND_NO_ERRORS: "No data found, no errors",
    QueryResponseStatus.DATA_FOUND_NO_ERRORS: "Data found, no errors (this is the default)",
}
