from ...base import HL7Table

"""
HL7 Version: 2.5.1
Person location type - 0305
Table Type: User
"""


class PersonLocationType(HL7Table):
    """
    Person location type - 0305 // User table type
    - CLINIC
    - DEPARTMENT
    - HOME
    - NURSING_UNIT
    - PROVIDERS_OFFICE
    - PHONE
    - SNF
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0305
    """

    CLINIC = "C"
    """Clinic"""
    DEPARTMENT = "D"
    """Department"""
    HOME = "H"
    """Home"""
    NURSING_UNIT = "N"
    """Nursing Unit"""
    PROVIDERS_OFFICE = "O"
    """Providers Office"""
    PHONE = "P"
    """Phone"""
    SNF = "S"
    """SNF"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PersonLocationType.CLINIC: "Clinic",
    PersonLocationType.DEPARTMENT: "Department",
    PersonLocationType.HOME: "Home",
    PersonLocationType.NURSING_UNIT: "Nursing Unit",
    PersonLocationType.PROVIDERS_OFFICE: "Providers Office",
    PersonLocationType.PHONE: "Phone",
    PersonLocationType.SNF: "SNF",
}
