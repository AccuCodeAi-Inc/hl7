from ...base import HL7Table

"""
HL7 Version: 2.5.1
Administration Method - 0165
Table Type: User
"""


class AdministrationMethod(HL7Table):
    """
    Administration Method - 0165 // User table type
    - CHEW
    - DISSOLVE
    - DUST
    - INFILTRATE
    - IRRIGATE
    - INSERT
    - IV_PUSH
    - IV_PIGGYBACK
    - NEBULIZED
    - PERFUSE
    - PAIN
    - SHAMPOO
    - SOAK
    - WASH
    - WIPE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0165
    """

    CHEW = "CH"
    """Chew"""
    DISSOLVE = "DI"
    """Dissolve"""
    DUST = "DU"
    """Dust"""
    INFILTRATE = "IF"
    """Infiltrate"""
    IRRIGATE = "IR"
    """Irrigate"""
    INSERT = "IS"
    """Insert"""
    IV_PUSH = "IVP"
    """IV Push"""
    IV_PIGGYBACK = "IVPB"
    """IV Piggyback"""
    NEBULIZED = "NB"
    """Nebulized"""
    PERFUSE = "PF"
    """Perfuse"""
    PAIN = "PT"
    """Pain"""
    SHAMPOO = "SH"
    """Shampoo"""
    SOAK = "SO"
    """Soak"""
    WASH = "WA"
    """Wash"""
    WIPE = "WI"
    """Wipe"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AdministrationMethod.CHEW: "Chew",
    AdministrationMethod.DISSOLVE: "Dissolve",
    AdministrationMethod.DUST: "Dust",
    AdministrationMethod.INFILTRATE: "Infiltrate",
    AdministrationMethod.IRRIGATE: "Irrigate",
    AdministrationMethod.INSERT: "Insert",
    AdministrationMethod.IV_PUSH: "IV Push",
    AdministrationMethod.IV_PIGGYBACK: "IV Piggyback",
    AdministrationMethod.NEBULIZED: "Nebulized",
    AdministrationMethod.PERFUSE: "Perfuse",
    AdministrationMethod.PAIN: "Pain",
    AdministrationMethod.SHAMPOO: "Shampoo",
    AdministrationMethod.SOAK: "Soak",
    AdministrationMethod.WASH: "Wash",
    AdministrationMethod.WIPE: "Wipe",
}
