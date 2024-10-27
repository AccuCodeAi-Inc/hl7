from ...base import HL7Table

"""
HL7 Version: 2.5.1
Location Equipment - 0261
Table Type: User
"""


class LocationEquipment(HL7Table):
    """
    Location Equipment - 0261 // User table type
    - ELECTRO_ENCEPHALOGRAM
    - ELECTRO_CARDIOGRAM
    - INFUSION_PUMP
    - IV_PUMP
    - OXYGEN
    - SUCTION
    - VENTILATOR
    - VITAL_SIGNS_MONITOR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0261
    """

    ELECTRO_ENCEPHALOGRAM = "EEG"
    """Electro-Encephalogram"""
    ELECTRO_CARDIOGRAM = "EKG"
    """Electro-Cardiogram"""
    INFUSION_PUMP = "INF"
    """Infusion pump"""
    IV_PUMP = "IVP"
    """IV pump"""
    OXYGEN = "OXY"
    """Oxygen"""
    SUCTION = "SUC"
    """Suction"""
    VENTILATOR = "VEN"
    """Ventilator"""
    VITAL_SIGNS_MONITOR = "VIT"
    """Vital signs monitor"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LocationEquipment.ELECTRO_ENCEPHALOGRAM: "Electro-Encephalogram",
    LocationEquipment.ELECTRO_CARDIOGRAM: "Electro-Cardiogram",
    LocationEquipment.INFUSION_PUMP: "Infusion pump",
    LocationEquipment.IV_PUMP: "IV pump",
    LocationEquipment.OXYGEN: "Oxygen",
    LocationEquipment.SUCTION: "Suction",
    LocationEquipment.VENTILATOR: "Ventilator",
    LocationEquipment.VITAL_SIGNS_MONITOR: "Vital signs monitor",
}
