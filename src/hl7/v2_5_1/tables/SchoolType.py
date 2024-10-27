from ...base import HL7Table

"""
HL7 Version: 2.5.1
School type - 0402
Table Type: User
"""


class SchoolType(HL7Table):
    """
    School type - 0402 // User table type
    - DENTAL
    - GRADUATE
    - MEDICAL
    - UNDERGRADUATE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0402
    """

    DENTAL = "D"
    """Dental"""
    GRADUATE = "G"
    """Graduate"""
    MEDICAL = "M"
    """Medical"""
    UNDERGRADUATE = "U"
    """Undergraduate"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SchoolType.DENTAL: "Dental",
    SchoolType.GRADUATE: "Graduate",
    SchoolType.MEDICAL: "Medical",
    SchoolType.UNDERGRADUATE: "Undergraduate",
}
