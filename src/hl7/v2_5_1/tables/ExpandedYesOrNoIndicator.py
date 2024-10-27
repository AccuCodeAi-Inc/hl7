from ...base import HL7Table

"""
HL7 Version: 2.5.1
Expanded yes/no indicator - 0532
Table Type: HL7
"""


class ExpandedYesOrNoIndicator(HL7Table):
    """
    Expanded yes/no indicator - 0532 // HL7 table type
    - ASKED_BUT_UNKNOWN
    - NO
    - NOT_APPLICABLE
    - NOT_ASKED
    - TEMPORARILY_UNAVAILABLE
    - NO_INFORMATION
    - NOT_PRESENT
    - UNKNOWN
    - YES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0532
    """

    ASKED_BUT_UNKNOWN = "ASKU"
    """asked but unknown"""
    NO = "N"
    """No"""
    NOT_APPLICABLE = "NA"
    """not applicable"""
    NOT_ASKED = "NASK"
    """not asked"""
    TEMPORARILY_UNAVAILABLE = "NAV"
    """temporarily unavailable"""
    NO_INFORMATION = "NI"
    """No Information"""
    NOT_PRESENT = "NP"
    """not present"""
    UNKNOWN = "UNK"
    """unknown"""
    YES = "Y"
    """Yes"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ExpandedYesOrNoIndicator.ASKED_BUT_UNKNOWN: "asked but unknown",
    ExpandedYesOrNoIndicator.NO: "No",
    ExpandedYesOrNoIndicator.NOT_APPLICABLE: "not applicable",
    ExpandedYesOrNoIndicator.NOT_ASKED: "not asked",
    ExpandedYesOrNoIndicator.TEMPORARILY_UNAVAILABLE: "temporarily unavailable",
    ExpandedYesOrNoIndicator.NO_INFORMATION: "No Information",
    ExpandedYesOrNoIndicator.NOT_PRESENT: "not present",
    ExpandedYesOrNoIndicator.UNKNOWN: "unknown",
    ExpandedYesOrNoIndicator.YES: "Yes",
}
