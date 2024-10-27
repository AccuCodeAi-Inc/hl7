from ...base import HL7Table

"""
HL7 Version: 2.5.1
Container status - 0370
Table Type: HL7
"""


class ContainerStatus(HL7Table):
    """
    Container status - 0370 // HL7 table type
    - IDENTIFIED
    - LEFT_EQUIPMENT
    - MISSING
    - IN_PROCESS
    - IN_POSITION
    - PROCESS_COMPLETED
    - UNKNOWN
    - CONTAINER_UNAVAILABLE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0370
    """

    IDENTIFIED = "I"
    """Identified"""
    LEFT_EQUIPMENT = "L"
    """Left Equipment"""
    MISSING = "M"
    """Missing"""
    IN_PROCESS = "O"
    """In Process"""
    IN_POSITION = "P"
    """In Position"""
    PROCESS_COMPLETED = "R"
    """Process Completed"""
    UNKNOWN = "U"
    """Unknown"""
    CONTAINER_UNAVAILABLE = "X"
    """Container Unavailable"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ContainerStatus.IDENTIFIED: "Identified",
    ContainerStatus.LEFT_EQUIPMENT: "Left Equipment",
    ContainerStatus.MISSING: "Missing",
    ContainerStatus.IN_PROCESS: "In Process",
    ContainerStatus.IN_POSITION: "In Position",
    ContainerStatus.PROCESS_COMPLETED: "Process Completed",
    ContainerStatus.UNKNOWN: "Unknown",
    ContainerStatus.CONTAINER_UNAVAILABLE: "Container Unavailable",
}
