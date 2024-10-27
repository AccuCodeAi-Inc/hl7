from ...base import HL7Table

"""
HL7 Version: 2.5.1
Visit User Code - 0130
Table Type: User
"""


class VisitUserCode(HL7Table):
    """
    Visit User Code - 0130 // User table type
    - HOME
    - MOBILE_UNIT
    - PHONE
    - TEACHING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0130
    """

    HOME = "HO"
    """Home"""
    MOBILE_UNIT = "MO"
    """Mobile Unit"""
    PHONE = "PH"
    """Phone"""
    TEACHING = "TE"
    """Teaching"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    VisitUserCode.HOME: "Home",
    VisitUserCode.MOBILE_UNIT: "Mobile Unit",
    VisitUserCode.PHONE: "Phone",
    VisitUserCode.TEACHING: "Teaching",
}
