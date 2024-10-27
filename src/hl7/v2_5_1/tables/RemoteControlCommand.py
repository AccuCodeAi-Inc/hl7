from ...base import HL7Table

"""
HL7 Version: 2.5.1
Remote control command - 0368
Table Type: User
"""


class RemoteControlCommand(HL7Table):
    """
    Remote control command - 0368 // User table type
    - ABORT
    - CLEAR
    - CLEAR_NOTIFICATION
    - DISABLE_SENDING_EVENTS
    - ENABLE_SENDING_EVENTS
    - EMERGENCY_STOP
    - EXECUTE
    - INITIALIZE_OR_INITIATE
    - LOCAL_CONTROL_REQUEST
    - LOCK
    - LOAD
    - PAUSE
    - REMOTE_CONTROL_REQUEST
    - RESUME
    - SAMPLING
    - SETUP
    - TRANSPORT_TO
    - UNLOCK
    - UNLOAD
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0368
    """

    ABORT = "AB"
    """Abort"""
    CLEAR = "CL"
    """Clear"""
    CLEAR_NOTIFICATION = "CN"
    """Clear Notification"""
    DISABLE_SENDING_EVENTS = "DI"
    """Disable Sending Events"""
    ENABLE_SENDING_EVENTS = "EN"
    """Enable Sending Events"""
    EMERGENCY_STOP = "ES"
    """Emergency -stop"""
    EXECUTE = "EX"
    """Execute (command specified in field Parameters (ST) 01394)"""
    INITIALIZE_OR_INITIATE = "IN"
    """Initialize/Initiate"""
    LOCAL_CONTROL_REQUEST = "LC"
    """Local Control Request"""
    LOCK = "LK"
    """Lock"""
    LOAD = "LO"
    """Load"""
    PAUSE = "PA"
    """Pause"""
    REMOTE_CONTROL_REQUEST = "RC"
    """Remote Control Request"""
    RESUME = "RE"
    """Resume"""
    SAMPLING = "SA"
    """Sampling"""
    SETUP = "SU"
    """Setup"""
    TRANSPORT_TO = "TT"
    """Transport To"""
    UNLOCK = "UC"
    """Unlock"""
    UNLOAD = "UN"
    """Unload"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RemoteControlCommand.ABORT: "Abort",
    RemoteControlCommand.CLEAR: "Clear",
    RemoteControlCommand.CLEAR_NOTIFICATION: "Clear Notification",
    RemoteControlCommand.DISABLE_SENDING_EVENTS: "Disable Sending Events",
    RemoteControlCommand.ENABLE_SENDING_EVENTS: "Enable Sending Events",
    RemoteControlCommand.EMERGENCY_STOP: "Emergency -stop",
    RemoteControlCommand.EXECUTE: "Execute (command specified in field Parameters (ST) 01394)",
    RemoteControlCommand.INITIALIZE_OR_INITIATE: "Initialize/Initiate",
    RemoteControlCommand.LOCAL_CONTROL_REQUEST: "Local Control Request",
    RemoteControlCommand.LOCK: "Lock",
    RemoteControlCommand.LOAD: "Load",
    RemoteControlCommand.PAUSE: "Pause",
    RemoteControlCommand.REMOTE_CONTROL_REQUEST: "Remote Control Request",
    RemoteControlCommand.RESUME: "Resume",
    RemoteControlCommand.SAMPLING: "Sampling",
    RemoteControlCommand.SETUP: "Setup",
    RemoteControlCommand.TRANSPORT_TO: "Transport To",
    RemoteControlCommand.UNLOCK: "Unlock",
    RemoteControlCommand.UNLOAD: "Unload",
}
