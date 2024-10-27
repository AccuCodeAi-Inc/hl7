from ...base import HL7Table

"""
HL7 Version: 2.5.1
Special Handling Code - 0376
Table Type: User
"""


class SpecialHandlingCode(HL7Table):
    """
    Special Handling Code - 0376 // User table type
    - TOOL
    - BODY_TEMPERATURE
    - CRITICAL_AMBIENT_TEMPERATURE
    - PROTECT_FROM_AIR
    - CRITICAL_FROZEN_TEMPERATURE
    - CRITICAL_REFRIGERATED_TEMPERATURE
    - DEEP_FROZEN
    - DRY
    - FROZEN_TEMPERATURE
    - METAL_FREE
    - LIQUID_NITROGEN
    - PROTECT_FROM_LIGHT
    - DO_NOT_SHAKE
    - NO_SHOCK
    - REFRIGERATED_TEMPERATURE
    - ULTRA_FROZEN
    - UPRIGHT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0376
    """

    TOOL = "AMB"
    """Tool"""
    BODY_TEMPERATURE = "C37"
    """Body temperature"""
    CRITICAL_AMBIENT_TEMPERATURE = "CAMB"
    """Critical ambient temperature"""
    PROTECT_FROM_AIR = "CATM"
    """Protect from air"""
    CRITICAL_FROZEN_TEMPERATURE = "CFRZ"
    """Critical frozen temperature"""
    CRITICAL_REFRIGERATED_TEMPERATURE = "CREF"
    """Critical refrigerated temperature"""
    DEEP_FROZEN = "DFRZ"
    """Deep frozen"""
    DRY = "DRY"
    """Dry"""
    FROZEN_TEMPERATURE = "FRZ"
    """Frozen temperature"""
    METAL_FREE = "MTLF"
    """Metal Free"""
    LIQUID_NITROGEN = "NTR"
    """Liquid nitrogen"""
    PROTECT_FROM_LIGHT = "PRTL"
    """Protect from light"""
    DO_NOT_SHAKE = "PSA"
    """Do not shake"""
    NO_SHOCK = "PSO"
    """No shock"""
    REFRIGERATED_TEMPERATURE = "REF"
    """Refrigerated temperature"""
    ULTRA_FROZEN = "UFRZ"
    """Ultra frozen"""
    UPRIGHT = "UPR"
    """Upright"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecialHandlingCode.TOOL: "Tool",
    SpecialHandlingCode.BODY_TEMPERATURE: "Body temperature",
    SpecialHandlingCode.CRITICAL_AMBIENT_TEMPERATURE: "Critical ambient temperature",
    SpecialHandlingCode.PROTECT_FROM_AIR: "Protect from air",
    SpecialHandlingCode.CRITICAL_FROZEN_TEMPERATURE: "Critical frozen temperature",
    SpecialHandlingCode.CRITICAL_REFRIGERATED_TEMPERATURE: "Critical refrigerated temperature",
    SpecialHandlingCode.DEEP_FROZEN: "Deep frozen",
    SpecialHandlingCode.DRY: "Dry",
    SpecialHandlingCode.FROZEN_TEMPERATURE: "Frozen temperature",
    SpecialHandlingCode.METAL_FREE: "Metal Free",
    SpecialHandlingCode.LIQUID_NITROGEN: "Liquid nitrogen",
    SpecialHandlingCode.PROTECT_FROM_LIGHT: "Protect from light",
    SpecialHandlingCode.DO_NOT_SHAKE: "Do not shake",
    SpecialHandlingCode.NO_SHOCK: "No shock",
    SpecialHandlingCode.REFRIGERATED_TEMPERATURE: "Refrigerated temperature",
    SpecialHandlingCode.ULTRA_FROZEN: "Ultra frozen",
    SpecialHandlingCode.UPRIGHT: "Upright",
}
