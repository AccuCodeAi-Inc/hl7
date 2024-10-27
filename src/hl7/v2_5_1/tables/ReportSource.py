from ...base import HL7Table

"""
HL7 Version: 2.5.1
Report source - 0235
Table Type: HL7
"""


class ReportSource(HL7Table):
    """
    Report source - 0235 // HL7 table type
    - CLINICAL_TRIAL
    - DATABASE_OR_REGISTRY_OR_POISON_CONTROL_CENTER
    - DISTRIBUTOR
    - HEALTH_PROFESSIONAL
    - LITERATURE
    - MANUFACTURER_OR_MARKETING_AUTHORITY_HOLDER
    - NON_HEALTHCARE_PROFESSIONAL
    - OTHER
    - PATIENT
    - REGULATORY_AGENCY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0235
    """

    CLINICAL_TRIAL = "C"
    """Clinical trial"""
    DATABASE_OR_REGISTRY_OR_POISON_CONTROL_CENTER = "D"
    """Database/registry/poison control center"""
    DISTRIBUTOR = "E"
    """Distributor"""
    HEALTH_PROFESSIONAL = "H"
    """Health professional"""
    LITERATURE = "L"
    """Literature"""
    MANUFACTURER_OR_MARKETING_AUTHORITY_HOLDER = "M"
    """Manufacturer/marketing authority holder"""
    NON_HEALTHCARE_PROFESSIONAL = "N"
    """Non-healthcare professional"""
    OTHER = "O"
    """Other"""
    PATIENT = "P"
    """Patient"""
    REGULATORY_AGENCY = "R"
    """Regulatory agency"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReportSource.CLINICAL_TRIAL: "Clinical trial",
    ReportSource.DATABASE_OR_REGISTRY_OR_POISON_CONTROL_CENTER: "Database/registry/poison control center",
    ReportSource.DISTRIBUTOR: "Distributor",
    ReportSource.HEALTH_PROFESSIONAL: "Health professional",
    ReportSource.LITERATURE: "Literature",
    ReportSource.MANUFACTURER_OR_MARKETING_AUTHORITY_HOLDER: "Manufacturer/marketing authority holder",
    ReportSource.NON_HEALTHCARE_PROFESSIONAL: "Non-healthcare professional",
    ReportSource.OTHER: "Other",
    ReportSource.PATIENT: "Patient",
    ReportSource.REGULATORY_AGENCY: "Regulatory agency",
}
