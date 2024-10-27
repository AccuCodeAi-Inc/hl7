from ...base import HL7Table

"""
HL7 Version: 2.5.1
Administration Device - 0164
Table Type: User
"""


class AdministrationDevice(HL7Table):
    """
    Administration Device - 0164 // User table type
    - APPLICATOR
    - BURETROL
    - HEPARIN_LOCK
    - IPPB
    - IV_PUMP
    - IV_SOLUSET
    - METERED_INHALER
    - NEBULIZER
    - PCA_PUMP
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0164
    """

    APPLICATOR = "AP"
    """Applicator"""
    BURETROL = "BT"
    """Buretrol"""
    HEPARIN_LOCK = "HL"
    """Heparin Lock"""
    IPPB = "IPPB"
    """IPPB"""
    IV_PUMP = "IVP"
    """IV Pump"""
    IV_SOLUSET = "IVS"
    """IV Soluset"""
    METERED_INHALER = "MI"
    """Metered Inhaler"""
    NEBULIZER = "NEB"
    """Nebulizer"""
    PCA_PUMP = "PCA"
    """PCA Pump"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AdministrationDevice.APPLICATOR: "Applicator",
    AdministrationDevice.BURETROL: "Buretrol",
    AdministrationDevice.HEPARIN_LOCK: "Heparin Lock",
    AdministrationDevice.IPPB: "IPPB",
    AdministrationDevice.IV_PUMP: "IV Pump",
    AdministrationDevice.IV_SOLUSET: "IV Soluset",
    AdministrationDevice.METERED_INHALER: "Metered Inhaler",
    AdministrationDevice.NEBULIZER: "Nebulizer",
    AdministrationDevice.PCA_PUMP: "PCA Pump",
}
