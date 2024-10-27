from ...base import HL7Table

"""
HL7 Version: 2.5.1
Substitution Status - 0167
Table Type: HL7
"""


class SubstitutionStatus(HL7Table):
    """
    Substitution Status - 0167 // HL7 table type
    - NO_PRODUCT_SELECTION_INDICATED
    - SUBSTITUTION_NOT_ALLOWED_BY_PRESCRIBER
    - SUBSTITUTION_ALLOWED_PATIENT_REQUESTED_PRODUCT_DISPENSED
    - SUBSTITUTION_ALLOWED_PHARMACIST_SELECTED_PRODUCT_DISPENSED
    - SUBSTITUTION_ALLOWED_GENERIC_DRUG_NOT_IN_STOCK
    - SUBSTITUTION_ALLOWED_BRAND_DRUG_DISPENSED_AS_A_GENERIC
    - SUBSTITUTION_NOT_ALLOWED_BRAND_DRUG_MANDATED_BY_LAW
    - SUBSTITUTION_ALLOWED_GENERIC_DRUG_NOT_AVAILABLE_IN_MARKETPLACE
    - A_GENERIC_SUBSTITUTION_WAS_DISPENSED
    - NO_SUBSTITUTE_WAS_DISPENSED_THIS_IS_EQUIVALENT_TO_THE_DEFAULT
    - A_THERAPEUTIC_SUBSTITUTION_WAS_DISPENSED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0167
    """

    NO_PRODUCT_SELECTION_INDICATED = "0"
    """No product selection indicated"""
    SUBSTITUTION_NOT_ALLOWED_BY_PRESCRIBER = "1"
    """Substitution not allowed by prescriber"""
    SUBSTITUTION_ALLOWED_PATIENT_REQUESTED_PRODUCT_DISPENSED = "2"
    """Substitution allowed - patient requested product dispensed"""
    SUBSTITUTION_ALLOWED_PHARMACIST_SELECTED_PRODUCT_DISPENSED = "3"
    """Substitution allowed - pharmacist selected product dispensed"""
    SUBSTITUTION_ALLOWED_GENERIC_DRUG_NOT_IN_STOCK = "4"
    """Substitution allowed - generic drug not in stock"""
    SUBSTITUTION_ALLOWED_BRAND_DRUG_DISPENSED_AS_A_GENERIC = "5"
    """Substitution allowed - brand drug dispensed as a generic"""
    SUBSTITUTION_NOT_ALLOWED_BRAND_DRUG_MANDATED_BY_LAW = "7"
    """Substitution not allowed - brand drug mandated by law"""
    SUBSTITUTION_ALLOWED_GENERIC_DRUG_NOT_AVAILABLE_IN_MARKETPLACE = "8"
    """Substitution allowed - generic drug not available in marketplace"""
    A_GENERIC_SUBSTITUTION_WAS_DISPENSED = "G"
    """A generic substitution was dispensed."""
    NO_SUBSTITUTE_WAS_DISPENSED_THIS_IS_EQUIVALENT_TO_THE_DEFAULT = "N"
    """No substitute was dispensed. This is equivalent to the default (null) value."""
    A_THERAPEUTIC_SUBSTITUTION_WAS_DISPENSED = "T"
    """A therapeutic substitution was dispensed."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SubstitutionStatus.NO_PRODUCT_SELECTION_INDICATED: "No product selection indicated",
    SubstitutionStatus.SUBSTITUTION_NOT_ALLOWED_BY_PRESCRIBER: "Substitution not allowed by prescriber",
    SubstitutionStatus.SUBSTITUTION_ALLOWED_PATIENT_REQUESTED_PRODUCT_DISPENSED: "Substitution allowed - patient requested product dispensed",
    SubstitutionStatus.SUBSTITUTION_ALLOWED_PHARMACIST_SELECTED_PRODUCT_DISPENSED: "Substitution allowed - pharmacist selected product dispensed",
    SubstitutionStatus.SUBSTITUTION_ALLOWED_GENERIC_DRUG_NOT_IN_STOCK: "Substitution allowed - generic drug not in stock",
    SubstitutionStatus.SUBSTITUTION_ALLOWED_BRAND_DRUG_DISPENSED_AS_A_GENERIC: "Substitution allowed - brand drug dispensed as a generic",
    SubstitutionStatus.SUBSTITUTION_NOT_ALLOWED_BRAND_DRUG_MANDATED_BY_LAW: "Substitution not allowed - brand drug mandated by law",
    SubstitutionStatus.SUBSTITUTION_ALLOWED_GENERIC_DRUG_NOT_AVAILABLE_IN_MARKETPLACE: "Substitution allowed - generic drug not available in marketplace",
    SubstitutionStatus.A_GENERIC_SUBSTITUTION_WAS_DISPENSED: "A generic substitution was dispensed.",
    SubstitutionStatus.NO_SUBSTITUTE_WAS_DISPENSED_THIS_IS_EQUIVALENT_TO_THE_DEFAULT: "No substitute was dispensed. This is equivalent to the default (null) value.",
    SubstitutionStatus.A_THERAPEUTIC_SUBSTITUTION_WAS_DISPENSED: "A therapeutic substitution was dispensed.",
}
