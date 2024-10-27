from ...base import HL7Table

"""
HL7 Version: 2.5.1
Procedure Functional Type - 0230
Table Type: User
"""


class ProcedureFunctionalType(HL7Table):
    """
    Procedure Functional Type - 0230 // User table type
    - ANESTHESIA
    - DIAGNOSTIC_PROCEDURE
    - INVASIVE_PROCEDURE_NOT_CLASSIFIED_ELSEWHERE
    - PROCEDURE_FOR_TREATMENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0230
    """

    ANESTHESIA = "A"
    """Anesthesia"""
    DIAGNOSTIC_PROCEDURE = "D"
    """Diagnostic procedure"""
    INVASIVE_PROCEDURE_NOT_CLASSIFIED_ELSEWHERE = "I"
    """Invasive procedure not classified elsewhere (e.g., IV, catheter, etc.)"""
    PROCEDURE_FOR_TREATMENT = "P"
    """Procedure for treatment (therapeutic, including operations)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProcedureFunctionalType.ANESTHESIA: "Anesthesia",
    ProcedureFunctionalType.DIAGNOSTIC_PROCEDURE: "Diagnostic procedure",
    ProcedureFunctionalType.INVASIVE_PROCEDURE_NOT_CLASSIFIED_ELSEWHERE: "Invasive procedure not classified elsewhere (e.g., IV, catheter, etc.)",
    ProcedureFunctionalType.PROCEDURE_FOR_TREATMENT: "Procedure for treatment (therapeutic, including operations)",
}
