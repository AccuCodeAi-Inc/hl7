from ...base import HL7Table

"""
HL7 Version: 2.5.1
Procedure Practitioner Identifier Code Type - 0133
Table Type: User
"""


class ProcedurePractitionerIdentifierCodeType(HL7Table):
    """
    Procedure Practitioner Identifier Code Type - 0133 // User table type
    - ANESTHESIOLOGIST_OR_ANESTHETIST
    - ASSISTANT_SURGEON
    - CERTIFIED_NURSE_MIDWIFE
    - NURSE_PRACTITIONER
    - PROCEDURE_MD_OR_SURGEON
    - PRIMARY_SURGEON
    - RADIOLOGIST
    - RESIDENT
    - SCRUB_NURSE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0133
    """

    ANESTHESIOLOGIST_OR_ANESTHETIST = "AN"
    """Anesthesiologist/Anesthetist"""
    ASSISTANT_SURGEON = "AS"
    """Assistant Surgeon"""
    CERTIFIED_NURSE_MIDWIFE = "CM"
    """Certified Nurse Midwife"""
    NURSE_PRACTITIONER = "NP"
    """Nurse Practitioner"""
    PROCEDURE_MD_OR_SURGEON = "PR"
    """Procedure MD/ Surgeon"""
    PRIMARY_SURGEON = "PS"
    """Primary Surgeon"""
    RADIOLOGIST = "RD"
    """Radiologist"""
    RESIDENT = "RS"
    """Resident"""
    SCRUB_NURSE = "SN"
    """Scrub Nurse"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProcedurePractitionerIdentifierCodeType.ANESTHESIOLOGIST_OR_ANESTHETIST: "Anesthesiologist/Anesthetist",
    ProcedurePractitionerIdentifierCodeType.ASSISTANT_SURGEON: "Assistant Surgeon",
    ProcedurePractitionerIdentifierCodeType.CERTIFIED_NURSE_MIDWIFE: "Certified Nurse Midwife",
    ProcedurePractitionerIdentifierCodeType.NURSE_PRACTITIONER: "Nurse Practitioner",
    ProcedurePractitionerIdentifierCodeType.PROCEDURE_MD_OR_SURGEON: "Procedure MD/ Surgeon",
    ProcedurePractitionerIdentifierCodeType.PRIMARY_SURGEON: "Primary Surgeon",
    ProcedurePractitionerIdentifierCodeType.RADIOLOGIST: "Radiologist",
    ProcedurePractitionerIdentifierCodeType.RESIDENT: "Resident",
    ProcedurePractitionerIdentifierCodeType.SCRUB_NURSE: "Scrub Nurse",
}
