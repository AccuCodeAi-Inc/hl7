from ...base import HL7Table

"""
HL7 Version: 2.5.1
Relationship - 0063
Table Type: User
"""


class Relationship(HL7Table):
    """
    Relationship - 0063 // User table type
    - ASSOCIATE
    - BROTHER
    - CARE_GIVER
    - CHILD
    - HANDICAPPED_DEPENDENT
    - LIFE_PARTNER
    - EMERGENCY_CONTACT
    - EMPLOYEE
    - EMPLOYER
    - EXTENDED_FAMILY
    - FOSTER_CHILD
    - FRIEND
    - FATHER
    - GRANDCHILD
    - GUARDIAN
    - GRANDPARENT
    - MANAGER
    - MOTHER
    - NATURAL_CHILD
    - NONE
    - OTHER_ADULT
    - OTHER
    - OWNER
    - PARENT
    - STEPCHILD
    - SELF
    - SIBLING
    - SISTER
    - SPOUSE
    - TRAINER
    - UNKNOWN
    - WARD_OF_COURT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0063
    """

    ASSOCIATE = "ASC"
    """Associate"""
    BROTHER = "BRO"
    """Brother"""
    CARE_GIVER = "CGV"
    """Care giver"""
    CHILD = "CHD"
    """Child"""
    HANDICAPPED_DEPENDENT = "DEP"
    """Handicapped dependent"""
    LIFE_PARTNER = "DOM"
    """Life partner"""
    EMERGENCY_CONTACT = "EMC"
    """Emergency contact"""
    EMPLOYEE = "EME"
    """Employee"""
    EMPLOYER = "EMR"
    """Employer"""
    EXTENDED_FAMILY = "EXF"
    """Extended family"""
    FOSTER_CHILD = "FCH"
    """Foster child"""
    FRIEND = "FND"
    """Friend"""
    FATHER = "FTH"
    """Father"""
    GRANDCHILD = "GCH"
    """Grandchild"""
    GUARDIAN = "GRD"
    """Guardian"""
    GRANDPARENT = "GRP"
    """Grandparent"""
    MANAGER = "MGR"
    """Manager"""
    MOTHER = "MTH"
    """Mother"""
    NATURAL_CHILD = "NCH"
    """Natural child"""
    NONE = "NON"
    """None"""
    OTHER_ADULT = "OAD"
    """Other adult"""
    OTHER = "OTH"
    """Other"""
    OWNER = "OWN"
    """Owner"""
    PARENT = "PAR"
    """Parent"""
    STEPCHILD = "SCH"
    """Stepchild"""
    SELF = "SEL"
    """Self"""
    SIBLING = "SIB"
    """Sibling"""
    SISTER = "SIS"
    """Sister"""
    SPOUSE = "SPO"
    """Spouse"""
    TRAINER = "TRA"
    """Trainer"""
    UNKNOWN = "UNK"
    """Unknown"""
    WARD_OF_COURT = "WRD"
    """Ward of court"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Relationship.ASSOCIATE: "Associate",
    Relationship.BROTHER: "Brother",
    Relationship.CARE_GIVER: "Care giver",
    Relationship.CHILD: "Child",
    Relationship.HANDICAPPED_DEPENDENT: "Handicapped dependent",
    Relationship.LIFE_PARTNER: "Life partner",
    Relationship.EMERGENCY_CONTACT: "Emergency contact",
    Relationship.EMPLOYEE: "Employee",
    Relationship.EMPLOYER: "Employer",
    Relationship.EXTENDED_FAMILY: "Extended family",
    Relationship.FOSTER_CHILD: "Foster child",
    Relationship.FRIEND: "Friend",
    Relationship.FATHER: "Father",
    Relationship.GRANDCHILD: "Grandchild",
    Relationship.GUARDIAN: "Guardian",
    Relationship.GRANDPARENT: "Grandparent",
    Relationship.MANAGER: "Manager",
    Relationship.MOTHER: "Mother",
    Relationship.NATURAL_CHILD: "Natural child",
    Relationship.NONE: "None",
    Relationship.OTHER_ADULT: "Other adult",
    Relationship.OTHER: "Other",
    Relationship.OWNER: "Owner",
    Relationship.PARENT: "Parent",
    Relationship.STEPCHILD: "Stepchild",
    Relationship.SELF: "Self",
    Relationship.SIBLING: "Sibling",
    Relationship.SISTER: "Sister",
    Relationship.SPOUSE: "Spouse",
    Relationship.TRAINER: "Trainer",
    Relationship.UNKNOWN: "Unknown",
    Relationship.WARD_OF_COURT: "Ward of court",
}
