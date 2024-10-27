from ...base import HL7Table

"""
HL7 Version: 2.5.1
Segment group - 0391
Table Type: HL7
"""


class SegmentGroup(HL7Table):
    """
    Segment group - 0391 // HL7 table type
    - ETC
    - OBR_GROUP
    - ORC_GROUP
    - PID_GROUP
    - RXA_GROUP
    - RXD_GROUP
    - RXE_GROUP
    - RXO_GROUP
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0391
    """

    ETC = "Etc"
    """"""
    OBR_GROUP = "OBRG"
    """OBR group"""
    ORC_GROUP = "ORCG"
    """ORC group"""
    PID_GROUP = "PIDG"
    """PID group"""
    RXA_GROUP = "RXAG"
    """RXA group"""
    RXD_GROUP = "RXDG"
    """RXD group"""
    RXE_GROUP = "RXEG"
    """RXE group"""
    RXO_GROUP = "RXOG"
    """RXO group"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SegmentGroup.ETC: "",
    SegmentGroup.OBR_GROUP: "OBR group",
    SegmentGroup.ORC_GROUP: "ORC group",
    SegmentGroup.PID_GROUP: "PID group",
    SegmentGroup.RXA_GROUP: "RXA group",
    SegmentGroup.RXD_GROUP: "RXD group",
    SegmentGroup.RXE_GROUP: "RXE group",
    SegmentGroup.RXO_GROUP: "RXO group",
}
