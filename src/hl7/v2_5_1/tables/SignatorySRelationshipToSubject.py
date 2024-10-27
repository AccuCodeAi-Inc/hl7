from ...base import HL7Table

"""
HL7 Version: 2.5.1
Signatory’s Relationship to Subject - 0548
Table Type: User
"""


class SignatorySRelationshipToSubject(HL7Table):
    """
    Signatory’s Relationship to Subject - 0548 // User table type
    - SELF
    - PARENT
    - NEXT_OF_KIN
    - DURABLE_POWER_OF_ATTORNEY_IN_HEALTHCARE_AFFAIRS
    - CONSERVATOR
    - EMERGENT_PRACTITIONER
    - NON_EMERGENT_PRACTITIONER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0548
    """

    SELF = "1"
    """Self"""
    PARENT = "2"
    """Parent"""
    NEXT_OF_KIN = "3"
    """Next of Kin"""
    DURABLE_POWER_OF_ATTORNEY_IN_HEALTHCARE_AFFAIRS = "4"
    """Durable Power of Attorney in Healthcare Affairs"""
    CONSERVATOR = "5"
    """Conservator"""
    EMERGENT_PRACTITIONER = "6"
    """Emergent Practitioner (practitioner judging case as emergency requiring care without a consent)"""
    NON_EMERGENT_PRACTITIONER = "7"
    """Non-Emergent Practitioner (i.e. medical ethics committee)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SignatorySRelationshipToSubject.SELF: "Self",
    SignatorySRelationshipToSubject.PARENT: "Parent",
    SignatorySRelationshipToSubject.NEXT_OF_KIN: "Next of Kin",
    SignatorySRelationshipToSubject.DURABLE_POWER_OF_ATTORNEY_IN_HEALTHCARE_AFFAIRS: "Durable Power of Attorney in Healthcare Affairs",
    SignatorySRelationshipToSubject.CONSERVATOR: "Conservator",
    SignatorySRelationshipToSubject.EMERGENT_PRACTITIONER: "Emergent Practitioner (practitioner judging case as emergency requiring care without a consent)",
    SignatorySRelationshipToSubject.NON_EMERGENT_PRACTITIONER: "Non-Emergent Practitioner (i.e. medical ethics committee)",
}
