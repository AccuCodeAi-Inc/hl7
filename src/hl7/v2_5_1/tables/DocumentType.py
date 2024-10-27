from ...base import HL7Table

"""
HL7 Version: 2.5.1
Document Type - 0270
Table Type: User
"""


class DocumentType(HL7Table):
    """
    Document Type - 0270 // User table type
    - AUTOPSY_REPORT
    - CARDIODIAGNOSTICS
    - CONSULTATION
    - DIAGNOSTIC_IMAGING
    - DISCHARGE_SUMMARY
    - EMERGENCY_DEPARTMENT_REPORT
    - HISTORY_AND_PHYSICAL_EXAMINATION
    - OPERATIVE_REPORT
    - PSYCHIATRIC_CONSULTATION
    - PSYCHIATRIC_HISTORY_AND_PHYSICAL_EXAMINATION
    - PROCEDURE_NOTE
    - PROGRESS_NOTE
    - SURGICAL_PATHOLOGY
    - TRANSFER_SUMMARY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0270
    """

    AUTOPSY_REPORT = "AR"
    """Autopsy report"""
    CARDIODIAGNOSTICS = "CD"
    """Cardiodiagnostics"""
    CONSULTATION = "CN"
    """Consultation"""
    DIAGNOSTIC_IMAGING = "DI"
    """Diagnostic imaging"""
    DISCHARGE_SUMMARY = "DS"
    """Discharge summary"""
    EMERGENCY_DEPARTMENT_REPORT = "ED"
    """Emergency department report"""
    HISTORY_AND_PHYSICAL_EXAMINATION = "HP"
    """History and physical examination"""
    OPERATIVE_REPORT = "OP"
    """Operative report"""
    PSYCHIATRIC_CONSULTATION = "PC"
    """Psychiatric consultation"""
    PSYCHIATRIC_HISTORY_AND_PHYSICAL_EXAMINATION = "PH"
    """Psychiatric history and physical examination"""
    PROCEDURE_NOTE = "PN"
    """Procedure note"""
    PROGRESS_NOTE = "PR"
    """Progress note"""
    SURGICAL_PATHOLOGY = "SP"
    """Surgical pathology"""
    TRANSFER_SUMMARY = "TS"
    """Transfer summary"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DocumentType.AUTOPSY_REPORT: "Autopsy report",
    DocumentType.CARDIODIAGNOSTICS: "Cardiodiagnostics",
    DocumentType.CONSULTATION: "Consultation",
    DocumentType.DIAGNOSTIC_IMAGING: "Diagnostic imaging",
    DocumentType.DISCHARGE_SUMMARY: "Discharge summary",
    DocumentType.EMERGENCY_DEPARTMENT_REPORT: "Emergency department report",
    DocumentType.HISTORY_AND_PHYSICAL_EXAMINATION: "History and physical examination",
    DocumentType.OPERATIVE_REPORT: "Operative report",
    DocumentType.PSYCHIATRIC_CONSULTATION: "Psychiatric consultation",
    DocumentType.PSYCHIATRIC_HISTORY_AND_PHYSICAL_EXAMINATION: "Psychiatric history and physical examination",
    DocumentType.PROCEDURE_NOTE: "Procedure note",
    DocumentType.PROGRESS_NOTE: "Progress note",
    DocumentType.SURGICAL_PATHOLOGY: "Surgical pathology",
    DocumentType.TRANSFER_SUMMARY: "Transfer summary",
}
