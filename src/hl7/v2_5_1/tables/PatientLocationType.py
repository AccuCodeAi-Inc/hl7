from ...base import HL7Table

"""
HL7 Version: 2.5.1
Patient location type - 0260
Table Type: User
"""


class PatientLocationType(HL7Table):
    """
    Patient location type - 0260 // User table type
    - BED
    - CLINIC
    - DEPARTMENT
    - EXAM_ROOM
    - OTHER_LOCATION
    - NURSING_UNIT
    - OPERATING_ROOM
    - ROOM
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0260
    """

    BED = "B"
    """Bed"""
    CLINIC = "C"
    """Clinic"""
    DEPARTMENT = "D"
    """Department"""
    EXAM_ROOM = "E"
    """Exam Room"""
    OTHER_LOCATION = "L"
    """Other Location"""
    NURSING_UNIT = "N"
    """Nursing Unit"""
    OPERATING_ROOM = "O"
    """Operating Room"""
    ROOM = "R"
    """Room"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PatientLocationType.BED: "Bed",
    PatientLocationType.CLINIC: "Clinic",
    PatientLocationType.DEPARTMENT: "Department",
    PatientLocationType.EXAM_ROOM: "Exam Room",
    PatientLocationType.OTHER_LOCATION: "Other Location",
    PatientLocationType.NURSING_UNIT: "Nursing Unit",
    PatientLocationType.OPERATING_ROOM: "Operating Room",
    PatientLocationType.ROOM: "Room",
}
