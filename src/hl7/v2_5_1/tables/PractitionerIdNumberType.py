from ...base import HL7Table

"""
HL7 Version: 2.5.1
Practitioner ID number type - 0338
Table Type: User
"""


class PractitionerIdNumberType(HL7Table):
    """
    Practitioner ID number type - 0338 // User table type
    - COUNTY_NUMBER
    - DRUG_ENFORCEMENT_AGENCY_NO
    - GENERAL_LEDGER_NUMBER
    - LABOR_AND_INDUSTRIES_NUMBER
    - LI
    - MEDICAID_NUMBER
    - MEDICARE_NUMBER
    - QA_NUMBER
    - STATE_LICENSE_NUMBER
    - TAX_ID_NUMBER
    - TRAINING_LICENSE_NUMBER
    - UNIQUE_PHYSICIAN_ID_NO
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0338
    """

    COUNTY_NUMBER = "CY"
    """County number"""
    DRUG_ENFORCEMENT_AGENCY_NO = "DEA"
    """Drug Enforcement Agency no."""
    GENERAL_LEDGER_NUMBER = "GL"
    """General ledger number"""
    LABOR_AND_INDUSTRIES_NUMBER = "L&I"  # Deprecated as of v 2.5; Use LI instead
    """Labor and industries number"""
    LI = "LI"
    """Labor and industries number"""
    MEDICAID_NUMBER = "MCD"
    """Medicaid number"""
    MEDICARE_NUMBER = "MCR"
    """Medicare number"""
    QA_NUMBER = "QA"
    """QA number"""
    STATE_LICENSE_NUMBER = "SL"
    """State license number"""
    TAX_ID_NUMBER = "TAX"
    """Tax ID number"""
    TRAINING_LICENSE_NUMBER = "TRL"
    """Training license number"""
    UNIQUE_PHYSICIAN_ID_NO = "UPIN"
    """Unique physician ID no."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PractitionerIdNumberType.COUNTY_NUMBER: "County number",
    PractitionerIdNumberType.DRUG_ENFORCEMENT_AGENCY_NO: "Drug Enforcement Agency no.",
    PractitionerIdNumberType.GENERAL_LEDGER_NUMBER: "General ledger number",
    PractitionerIdNumberType.LABOR_AND_INDUSTRIES_NUMBER: "Labor and industries number",
    PractitionerIdNumberType.LI: "Labor and industries number",
    PractitionerIdNumberType.MEDICAID_NUMBER: "Medicaid number",
    PractitionerIdNumberType.MEDICARE_NUMBER: "Medicare number",
    PractitionerIdNumberType.QA_NUMBER: "QA number",
    PractitionerIdNumberType.STATE_LICENSE_NUMBER: "State license number",
    PractitionerIdNumberType.TAX_ID_NUMBER: "Tax ID number",
    PractitionerIdNumberType.TRAINING_LICENSE_NUMBER: "Training license number",
    PractitionerIdNumberType.UNIQUE_PHYSICIAN_ID_NO: "Unique physician ID no.",
}
