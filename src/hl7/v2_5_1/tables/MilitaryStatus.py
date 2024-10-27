from ...base import HL7Table

"""
HL7 Version: 2.5.1
Military Status - 0142
Table Type: User
"""


class MilitaryStatus(HL7Table):
    """
    Military Status - 0142 // User table type
    - ACTIVE_DUTY
    - DECEASED
    - RETIRED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0142
    """

    ACTIVE_DUTY = "ACT"
    """Active duty"""
    DECEASED = "DEC"
    """Deceased"""
    RETIRED = "RET"
    """Retired"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MilitaryStatus.ACTIVE_DUTY: "Active duty",
    MilitaryStatus.DECEASED: "Deceased",
    MilitaryStatus.RETIRED: "Retired",
}
