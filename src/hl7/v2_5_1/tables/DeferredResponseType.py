from ...base import HL7Table

"""
HL7 Version: 2.5.1
Deferred response type - 0107
Table Type: HL7
"""


class DeferredResponseType(HL7Table):
    """
    Deferred response type - 0107 // HL7 table type
    - BEFORE_THE_DATE_OR_TIME_SPECIFIED
    - LATER_THAN_THE_DATE_OR_TIME_SPECIFIED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0107
    """

    BEFORE_THE_DATE_OR_TIME_SPECIFIED = "B"
    """Before the Date/Time specified"""
    LATER_THAN_THE_DATE_OR_TIME_SPECIFIED = "L"
    """Later than the Date/Time specified"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DeferredResponseType.BEFORE_THE_DATE_OR_TIME_SPECIFIED: "Before the Date/Time specified",
    DeferredResponseType.LATER_THAN_THE_DATE_OR_TIME_SPECIFIED: "Later than the Date/Time specified",
}
