from ...base import HL7Table

"""
HL7 Version: 2.5.1
Diagnosis Classification - 0228
Table Type: User
"""


class DiagnosisClassification(HL7Table):
    """
    Diagnosis Classification - 0228 // User table type
    - CONSULTATION
    - DIAGNOSIS
    - INVASIVE_PROCEDURE_NOT_CLASSIFIED_ELSEWHERE
    - MEDICATION
    - OTHER
    - RADIOLOGICAL_SCHEDULING
    - SIGN_AND_SYMPTOM
    - TISSUE_DIAGNOSIS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0228
    """

    CONSULTATION = "C"
    """Consultation"""
    DIAGNOSIS = "D"
    """Diagnosis"""
    INVASIVE_PROCEDURE_NOT_CLASSIFIED_ELSEWHERE = "I"
    """Invasive procedure not classified elsewhere (I.V., catheter, etc.)"""
    MEDICATION = "M"
    """Medication (antibiotic)"""
    OTHER = "O"
    """Other"""
    RADIOLOGICAL_SCHEDULING = "R"
    """Radiological scheduling (not using ICDA codes)"""
    SIGN_AND_SYMPTOM = "S"
    """Sign and symptom"""
    TISSUE_DIAGNOSIS = "T"
    """Tissue diagnosis"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DiagnosisClassification.CONSULTATION: "Consultation",
    DiagnosisClassification.DIAGNOSIS: "Diagnosis",
    DiagnosisClassification.INVASIVE_PROCEDURE_NOT_CLASSIFIED_ELSEWHERE: "Invasive procedure not classified elsewhere (I.V., catheter, etc.)",
    DiagnosisClassification.MEDICATION: "Medication (antibiotic)",
    DiagnosisClassification.OTHER: "Other",
    DiagnosisClassification.RADIOLOGICAL_SCHEDULING: "Radiological scheduling (not using ICDA codes)",
    DiagnosisClassification.SIGN_AND_SYMPTOM: "Sign and symptom",
    DiagnosisClassification.TISSUE_DIAGNOSIS: "Tissue diagnosis",
}
