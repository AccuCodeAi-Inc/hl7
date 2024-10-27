from ...base import HL7Table

"""
HL7 Version: 2.5.1
Release Information - 0093
Table Type: User
"""


class ReleaseInformation(HL7Table):
    """
    Release Information - 0093 // User table type
    - USER_DEFINED_CODES
    - NO
    - YES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0093
    """

    USER_DEFINED_CODES = "…"
    """user-defined codes"""
    NO = "N"
    """No"""
    YES = "Y"
    """Yes"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReleaseInformation.USER_DEFINED_CODES: "user-defined codes",
    ReleaseInformation.NO: "No",
    ReleaseInformation.YES: "Yes",
}
