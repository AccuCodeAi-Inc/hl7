from ...base import HL7Table

"""
HL7 Version: 2.5.1
Patient’s Relationship to Insured - 0344
Table Type: User
"""


class PatientSRelationshipToInsured(HL7Table):
    """
    Patient’s Relationship to Insured - 0344 // User table type
    - PATIENT_IS_INSURED
    - SPOUSE
    - NATURAL_CHILD_OR_INSURED_FINANCIAL_RESPONSIBILITY
    - NATURAL_CHILD_OR_INSURED_DOES_NOT_HAVE_FINANCIAL_RESPONSIBILITY
    - STEP_CHILD
    - FOSTER_CHILD
    - WARD_OF_THE_COURT
    - EMPLOYEE
    - UNKNOWN
    - HANDICAPPED_DEPENDENT
    - ORGAN_DONOR
    - CADAVER_DONOR
    - GRANDCHILD
    - NIECE_OR_NEPHEW
    - INJURED_PLAINTIFF
    - SPONSORED_DEPENDENT
    - MINOR_DEPENDENT_OF_A_MINOR_DEPENDENT
    - PARENT
    - GRANDPARENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0344
    """

    PATIENT_IS_INSURED = "01"
    """Patient is insured"""
    SPOUSE = "02"
    """Spouse"""
    NATURAL_CHILD_OR_INSURED_FINANCIAL_RESPONSIBILITY = "03"
    """Natural child/insured financial responsibility"""
    NATURAL_CHILD_OR_INSURED_DOES_NOT_HAVE_FINANCIAL_RESPONSIBILITY = "04"
    """Natural child/Insured does not have financial responsibility"""
    STEP_CHILD = "05"
    """Step child"""
    FOSTER_CHILD = "06"
    """Foster child"""
    WARD_OF_THE_COURT = "07"
    """Ward of the court"""
    EMPLOYEE = "08"
    """Employee"""
    UNKNOWN = "09"
    """Unknown"""
    HANDICAPPED_DEPENDENT = "10"
    """Handicapped dependent"""
    ORGAN_DONOR = "11"
    """Organ donor"""
    CADAVER_DONOR = "12"
    """Cadaver donor"""
    GRANDCHILD = "13"
    """Grandchild"""
    NIECE_OR_NEPHEW = "14"
    """Niece/nephew"""
    INJURED_PLAINTIFF = "15"
    """Injured plaintiff"""
    SPONSORED_DEPENDENT = "16"
    """Sponsored dependent"""
    MINOR_DEPENDENT_OF_A_MINOR_DEPENDENT = "17"
    """Minor dependent of a minor dependent"""
    PARENT = "18"
    """Parent"""
    GRANDPARENT = "19"
    """Grandparent"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PatientSRelationshipToInsured.PATIENT_IS_INSURED: "Patient is insured",
    PatientSRelationshipToInsured.SPOUSE: "Spouse",
    PatientSRelationshipToInsured.NATURAL_CHILD_OR_INSURED_FINANCIAL_RESPONSIBILITY: "Natural child/insured financial responsibility",
    PatientSRelationshipToInsured.NATURAL_CHILD_OR_INSURED_DOES_NOT_HAVE_FINANCIAL_RESPONSIBILITY: "Natural child/Insured does not have financial responsibility",
    PatientSRelationshipToInsured.STEP_CHILD: "Step child",
    PatientSRelationshipToInsured.FOSTER_CHILD: "Foster child",
    PatientSRelationshipToInsured.WARD_OF_THE_COURT: "Ward of the court",
    PatientSRelationshipToInsured.EMPLOYEE: "Employee",
    PatientSRelationshipToInsured.UNKNOWN: "Unknown",
    PatientSRelationshipToInsured.HANDICAPPED_DEPENDENT: "Handicapped dependent",
    PatientSRelationshipToInsured.ORGAN_DONOR: "Organ donor",
    PatientSRelationshipToInsured.CADAVER_DONOR: "Cadaver donor",
    PatientSRelationshipToInsured.GRANDCHILD: "Grandchild",
    PatientSRelationshipToInsured.NIECE_OR_NEPHEW: "Niece/nephew",
    PatientSRelationshipToInsured.INJURED_PLAINTIFF: "Injured plaintiff",
    PatientSRelationshipToInsured.SPONSORED_DEPENDENT: "Sponsored dependent",
    PatientSRelationshipToInsured.MINOR_DEPENDENT_OF_A_MINOR_DEPENDENT: "Minor dependent of a minor dependent",
    PatientSRelationshipToInsured.PARENT: "Parent",
    PatientSRelationshipToInsured.GRANDPARENT: "Grandparent",
}
