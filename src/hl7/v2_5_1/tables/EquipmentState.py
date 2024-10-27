from ...base import HL7Table

"""
HL7 Version: 2.5.1
Equipment state - 0365
Table Type: HL7
"""


class EquipmentState(HL7Table):
    """
    Equipment state - 0365 // HL7 table type
    - CLEARING
    - CONFIGURING
    - E_STOPPED
    - IDLE
    - INITIALIZING
    - NORMAL_OPERATION
    - PAUSING
    - PAUSED
    - POWERED_UP
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0365
    """

    CLEARING = "CL"
    """Clearing"""
    CONFIGURING = "CO"
    """Configuring"""
    E_STOPPED = "ES"
    """E-stopped"""
    IDLE = "ID"
    """Idle"""
    INITIALIZING = "IN"
    """Initializing"""
    NORMAL_OPERATION = "OP"
    """Normal Operation"""
    PAUSING = "PA"
    """Pausing"""
    PAUSED = "PD"
    """Paused"""
    POWERED_UP = "PU"
    """Powered Up"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EquipmentState.CLEARING: "Clearing",
    EquipmentState.CONFIGURING: "Configuring",
    EquipmentState.E_STOPPED: "E-stopped",
    EquipmentState.IDLE: "Idle",
    EquipmentState.INITIALIZING: "Initializing",
    EquipmentState.NORMAL_OPERATION: "Normal Operation",
    EquipmentState.PAUSING: "Pausing",
    EquipmentState.PAUSED: "Paused",
    EquipmentState.POWERED_UP: "Powered Up",
}
