from ...base import HL7Table

"""
HL7 Version: 2.5.1
Blood Product Processing Requirements - 0508
Table Type: User
"""


class BloodProductProcessingRequirements(HL7Table):
    """
    Blood Product Processing Requirements - 0508 // User table type
    - AUTOLOGOUS_UNIT
    - CMV_NEGATIVE
    - CMV_SAFE
    - DIRECTED_UNIT
    - FRESH_UNIT
    - HEMOGLOBIN_S_NEGATIVE
    - HLA_MATCHED
    - IGA_DEFICIENT
    - IRRADIATED
    - LEUKOREDUCED
    - WASHED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0508
    """

    AUTOLOGOUS_UNIT = "AU"
    """Autologous Unit"""
    CMV_NEGATIVE = "CM"
    """CMV Negative"""
    CMV_SAFE = "CS"
    """CMV Safe"""
    DIRECTED_UNIT = "DI"
    """Directed Unit"""
    FRESH_UNIT = "FR"
    """Fresh unit"""
    HEMOGLOBIN_S_NEGATIVE = "HB"
    """Hemoglobin S Negative"""
    HLA_MATCHED = "HL"
    """HLA Matched"""
    IGA_DEFICIENT = "IG"
    """IgA Deficient"""
    IRRADIATED = "IR"
    """Irradiated"""
    LEUKOREDUCED = "LR"
    """Leukoreduced"""
    WASHED = "WA"
    """Washed"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    BloodProductProcessingRequirements.AUTOLOGOUS_UNIT: "Autologous Unit",
    BloodProductProcessingRequirements.CMV_NEGATIVE: "CMV Negative",
    BloodProductProcessingRequirements.CMV_SAFE: "CMV Safe",
    BloodProductProcessingRequirements.DIRECTED_UNIT: "Directed Unit",
    BloodProductProcessingRequirements.FRESH_UNIT: "Fresh unit",
    BloodProductProcessingRequirements.HEMOGLOBIN_S_NEGATIVE: "Hemoglobin S Negative",
    BloodProductProcessingRequirements.HLA_MATCHED: "HLA Matched",
    BloodProductProcessingRequirements.IGA_DEFICIENT: "IgA Deficient",
    BloodProductProcessingRequirements.IRRADIATED: "Irradiated",
    BloodProductProcessingRequirements.LEUKOREDUCED: "Leukoreduced",
    BloodProductProcessingRequirements.WASHED: "Washed",
}
