from ...base import HL7Table

"""
HL7 Version: 2.5.1
Admission Type - 0007
Table Type: User
"""


class AdmissionType(HL7Table):
    """
    Admission Type - 0007 // User table type
    - ACCIDENT
    - ELECTIVE
    - EMERGENCY
    - LABOR_AND_DELIVERY
    - NEWBORN
    - ROUTINE
    - URGENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0007
    """

    ACCIDENT = "A"
    """Accident"""
    ELECTIVE = "C"  # US UB92 code “3”
    """Elective"""
    EMERGENCY = "E"  # US UB92  code “1”
    """Emergency"""
    LABOR_AND_DELIVERY = "L"
    """Labor and Delivery"""
    NEWBORN = "N"  # US UB92 code “4”
    """Newborn (Birth in healthcare facility)"""
    ROUTINE = "R"
    """Routine"""
    URGENT = "U"  # US UB92 code “2”
    """Urgent"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AdmissionType.ACCIDENT: "Accident",
    AdmissionType.ELECTIVE: "Elective",
    AdmissionType.EMERGENCY: "Emergency",
    AdmissionType.LABOR_AND_DELIVERY: "Labor and Delivery",
    AdmissionType.NEWBORN: "Newborn (Birth in healthcare facility)",
    AdmissionType.ROUTINE: "Routine",
    AdmissionType.URGENT: "Urgent",
}
