from ...base import HL7Table

"""
HL7 Version: 2.5.1
Reimbursement Type Code - 0470
Table Type: User
"""


class ReimbursementTypeCode(HL7Table):
    """
    Reimbursement Type Code - 0470 // User table type
    - CORNEAL_TISSUE_APC
    - DURABLE_MEDICAL_EQUIPMENT
    - EPOTEIN
    - CLINICAL_LABORATORY_APC
    - SCREENING_MAMMOGRAPHY_APC
    - THIS_APC_IS_NOT_PAID
    - OUTPATIENT_PROSPECTIVE_PAYMENT_SYSTEM
    - PARTIAL_HOSPITALIZATION_APC
    - PACKAGED_APC
    - THERAPY_APC
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0470
    """

    CORNEAL_TISSUE_APC = "Crnl"
    """Corneal Tissue APC"""
    DURABLE_MEDICAL_EQUIPMENT = "DME"
    """Durable Medical Equipment"""
    EPOTEIN = "EPO"
    """Epotein"""
    CLINICAL_LABORATORY_APC = "Lab"
    """Clinical Laboratory APC"""
    SCREENING_MAMMOGRAPHY_APC = "Mamm"
    """Screening Mammography APC"""
    THIS_APC_IS_NOT_PAID = "NoPay"
    """This APC is not paid"""
    OUTPATIENT_PROSPECTIVE_PAYMENT_SYSTEM = "OPPS"
    """Outpatient Prospective Payment System"""
    PARTIAL_HOSPITALIZATION_APC = "PartH"
    """Partial Hospitalization APC"""
    PACKAGED_APC = "Pckg"
    """Packaged APC"""
    THERAPY_APC = "Thrpy"
    """Therapy APC"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReimbursementTypeCode.CORNEAL_TISSUE_APC: "Corneal Tissue APC",
    ReimbursementTypeCode.DURABLE_MEDICAL_EQUIPMENT: "Durable Medical Equipment",
    ReimbursementTypeCode.EPOTEIN: "Epotein",
    ReimbursementTypeCode.CLINICAL_LABORATORY_APC: "Clinical Laboratory APC",
    ReimbursementTypeCode.SCREENING_MAMMOGRAPHY_APC: "Screening Mammography APC",
    ReimbursementTypeCode.THIS_APC_IS_NOT_PAID: "This APC is not paid",
    ReimbursementTypeCode.OUTPATIENT_PROSPECTIVE_PAYMENT_SYSTEM: "Outpatient Prospective Payment System",
    ReimbursementTypeCode.PARTIAL_HOSPITALIZATION_APC: "Partial Hospitalization APC",
    ReimbursementTypeCode.PACKAGED_APC: "Packaged APC",
    ReimbursementTypeCode.THERAPY_APC: "Therapy APC",
}
