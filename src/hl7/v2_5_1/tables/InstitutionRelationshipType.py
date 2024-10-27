from ...base import HL7Table

"""
HL7 Version: 2.5.1
Institution Relationship Type - 0538
Table Type: User
"""


class InstitutionRelationshipType(HL7Table):
    """
    Institution Relationship Type - 0538 // User table type
    - CONTRACTOR
    - CONSULTANT
    - EMPLOYEE
    - VOLUNTEER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0538
    """

    CONTRACTOR = "CON"
    """Contractor"""
    CONSULTANT = "CST"
    """Consultant"""
    EMPLOYEE = "EMP"
    """Employee"""
    VOLUNTEER = "VOL"
    """Volunteer"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    InstitutionRelationshipType.CONTRACTOR: "Contractor",
    InstitutionRelationshipType.CONSULTANT: "Consultant",
    InstitutionRelationshipType.EMPLOYEE: "Employee",
    InstitutionRelationshipType.VOLUNTEER: "Volunteer",
}
