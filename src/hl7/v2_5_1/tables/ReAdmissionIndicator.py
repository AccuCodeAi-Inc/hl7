from ...base import HL7Table

"""
HL7 Version: 2.5.1
Re-Admission Indicator - 0092
Table Type: User
"""


class ReAdmissionIndicator(HL7Table):
    """
    Re-Admission Indicator - 0092 // User table type
    - RE_ADMISSION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0092
    """

    RE_ADMISSION = "R"
    """Re-admission"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReAdmissionIndicator.RE_ADMISSION: "Re-admission",
}
