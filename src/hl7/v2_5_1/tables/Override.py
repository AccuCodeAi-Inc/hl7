from ...base import HL7Table

"""
HL7 Version: 2.5.1
Override - 0268
Table Type: User
"""


class Override(HL7Table):
    """
    Override - 0268 // User table type
    - OVERRIDE_ALLOWED
    - OVERRIDE_REQUIRED
    - OVERRIDE_NOT_ALLOWED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0268
    """

    OVERRIDE_ALLOWED = "A"
    """Override allowed"""
    OVERRIDE_REQUIRED = "R"
    """Override required"""
    OVERRIDE_NOT_ALLOWED = "X"
    """Override not allowed"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Override.OVERRIDE_ALLOWED: "Override allowed",
    Override.OVERRIDE_REQUIRED: "Override required",
    Override.OVERRIDE_NOT_ALLOWED: "Override not allowed",
}
