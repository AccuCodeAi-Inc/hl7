from ...base import HL7Table

"""
HL7 Version: 2.5.1
Organization Unit Type - 0474
Table Type: User
"""


class OrganizationUnitType(HL7Table):
    """
    Organization Unit Type - 0474 // User table type
    - DEPARTMENT
    - FACILITY
    - SUBDIVISION
    - SUBDEPARTMENT
    - DIVISION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0474
    """

    DEPARTMENT = "D"
    """Department"""
    FACILITY = "F"
    """Facility"""
    SUBDIVISION = "S"
    """Subdivision"""
    SUBDEPARTMENT = "U"
    """Subdepartment"""
    DIVISION = "V"
    """Division"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OrganizationUnitType.DEPARTMENT: "Department",
    OrganizationUnitType.FACILITY: "Facility",
    OrganizationUnitType.SUBDIVISION: "Subdivision",
    OrganizationUnitType.SUBDEPARTMENT: "Subdepartment",
    OrganizationUnitType.DIVISION: "Division",
}
