from ...base import HL7Table

"""
HL7 Version: 2.5.1
Coverage Type - 0309
Table Type: User
"""


class CoverageType(HL7Table):
    """
    Coverage Type - 0309 // User table type
    - BOTH_HOSPITAL_AND_PHYSICIAN
    - HOSPITAL_OR_INSTITUTIONAL
    - PHYSICIAN_OR_PROFESSIONAL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0309
    """

    BOTH_HOSPITAL_AND_PHYSICIAN = "B"
    """Both hospital and physician"""
    HOSPITAL_OR_INSTITUTIONAL = "H"
    """Hospital/institutional"""
    PHYSICIAN_OR_PROFESSIONAL = "P"
    """Physician/professional"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CoverageType.BOTH_HOSPITAL_AND_PHYSICIAN: "Both hospital and physician",
    CoverageType.HOSPITAL_OR_INSTITUTIONAL: "Hospital/institutional",
    CoverageType.PHYSICIAN_OR_PROFESSIONAL: "Physician/professional",
}
