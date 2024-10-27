from ...base import HL7Table

"""
HL7 Version: 2.5.1
Risk Management Incident Code - 0427
Table Type: User
"""


class RiskManagementIncidentCode(HL7Table):
    """
    Risk Management Incident Code - 0427 // User table type
    - BODY_FLUID_EXPOSURE
    - CONTAMINATED_SUBSTANCE
    - DIET_ERRORS
    - EQUIPMENT_PROBLEM
    - PATIENT_FELL
    - PATIENT_FELL_FROM_BED
    - INFUSION_ERROR
    - FOREIGN_OBJECT_LEFT_DURING_SURGERY
    - STERILE_PRECAUTION_VIOLATED
    - OTHER
    - PROCEDURE_ERROR
    - PHARMACEUTICAL_ERROR
    - SUICIDE_ATTEMPT
    - TRANSFUSION_ERROR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0427
    """

    BODY_FLUID_EXPOSURE = "B"
    """Body fluid exposure"""
    CONTAMINATED_SUBSTANCE = "C"
    """Contaminated Substance"""
    DIET_ERRORS = "D"
    """Diet Errors"""
    EQUIPMENT_PROBLEM = "E"
    """Equipment problem"""
    PATIENT_FELL = "F"
    """Patient fell (not from bed)"""
    PATIENT_FELL_FROM_BED = "H"
    """Patient fell from bed"""
    INFUSION_ERROR = "I"
    """Infusion error"""
    FOREIGN_OBJECT_LEFT_DURING_SURGERY = "J"
    """Foreign object left during surgery"""
    STERILE_PRECAUTION_VIOLATED = "K"
    """Sterile precaution violated"""
    OTHER = "O"
    """Other"""
    PROCEDURE_ERROR = "P"
    """Procedure error"""
    PHARMACEUTICAL_ERROR = "R"
    """Pharmaceutical error"""
    SUICIDE_ATTEMPT = "S"
    """Suicide Attempt"""
    TRANSFUSION_ERROR = "T"
    """Transfusion error"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RiskManagementIncidentCode.BODY_FLUID_EXPOSURE: "Body fluid exposure",
    RiskManagementIncidentCode.CONTAMINATED_SUBSTANCE: "Contaminated Substance",
    RiskManagementIncidentCode.DIET_ERRORS: "Diet Errors",
    RiskManagementIncidentCode.EQUIPMENT_PROBLEM: "Equipment problem",
    RiskManagementIncidentCode.PATIENT_FELL: "Patient fell (not from bed)",
    RiskManagementIncidentCode.PATIENT_FELL_FROM_BED: "Patient fell from bed",
    RiskManagementIncidentCode.INFUSION_ERROR: "Infusion error",
    RiskManagementIncidentCode.FOREIGN_OBJECT_LEFT_DURING_SURGERY: "Foreign object left during surgery",
    RiskManagementIncidentCode.STERILE_PRECAUTION_VIOLATED: "Sterile precaution violated",
    RiskManagementIncidentCode.OTHER: "Other",
    RiskManagementIncidentCode.PROCEDURE_ERROR: "Procedure error",
    RiskManagementIncidentCode.PHARMACEUTICAL_ERROR: "Pharmaceutical error",
    RiskManagementIncidentCode.SUICIDE_ATTEMPT: "Suicide Attempt",
    RiskManagementIncidentCode.TRANSFUSION_ERROR: "Transfusion error",
}
