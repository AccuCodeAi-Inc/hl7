from ...base import HL7Table

"""
HL7 Version: 2.5.1
Local/remote control state - 0366
Table Type: HL7
"""


class LocalOrRemoteControlState(HL7Table):
    """
    Local/remote control state - 0366 // HL7 table type
    - LOCAL
    - REMOTE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0366
    """

    LOCAL = "L"
    """Local"""
    REMOTE = "R"
    """Remote"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LocalOrRemoteControlState.LOCAL: "Local",
    LocalOrRemoteControlState.REMOTE: "Remote",
}
