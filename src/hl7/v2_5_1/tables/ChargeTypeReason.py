from ...base import HL7Table

"""
HL7 Version: 2.5.1
Charge Type Reason - 0475
Table Type: User
"""


class ChargeTypeReason(HL7Table):
    """
    Charge Type Reason - 0475 // User table type
    - ALLERGY
    - INTOLERANCE
    - TREATMENT_FAILURE
    - PATIENT_REQUEST
    - NO_EXCEPTION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0475
    """

    ALLERGY = "01"
    """Allergy"""
    INTOLERANCE = "02"
    """Intolerance"""
    TREATMENT_FAILURE = "03"
    """Treatment Failure"""
    PATIENT_REQUEST = "04"
    """Patient Request"""
    NO_EXCEPTION = "05"
    """No Exception"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ChargeTypeReason.ALLERGY: "Allergy",
    ChargeTypeReason.INTOLERANCE: "Intolerance",
    ChargeTypeReason.TREATMENT_FAILURE: "Treatment Failure",
    ChargeTypeReason.PATIENT_REQUEST: "Patient Request",
    ChargeTypeReason.NO_EXCEPTION: "No Exception",
}
