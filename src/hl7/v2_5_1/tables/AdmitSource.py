from ...base import HL7Table

"""
HL7 Version: 2.5.1
Admit Source - 0023
Table Type: User
"""


class AdmitSource(HL7Table):
    """
    Admit Source - 0023 // User table type
    - PHYSICIAN_REFERRAL
    - CLINIC_REFERRAL
    - HMO_REFERRAL
    - TRANSFER_FROM_A_HOSPITAL
    - TRANSFER_FROM_A_SKILLED_NURSING_FACILITY
    - TRANSFER_FROM_ANOTHER_HEALTH_CARE_FACILITY
    - EMERGENCY_ROOM
    - COURT_OR_LAW_ENFORCEMENT
    - INFORMATION_NOT_AVAILABLE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0023
    """

    PHYSICIAN_REFERRAL = "1"
    """Physician referral"""
    CLINIC_REFERRAL = "2"
    """Clinic referral"""
    HMO_REFERRAL = "3"
    """HMO referral"""
    TRANSFER_FROM_A_HOSPITAL = "4"
    """Transfer from a hospital"""
    TRANSFER_FROM_A_SKILLED_NURSING_FACILITY = "5"
    """Transfer from a skilled nursing facility"""
    TRANSFER_FROM_ANOTHER_HEALTH_CARE_FACILITY = "6"
    """Transfer from another health care facility"""
    EMERGENCY_ROOM = "7"
    """Emergency room"""
    COURT_OR_LAW_ENFORCEMENT = "8"
    """Court/law enforcement"""
    INFORMATION_NOT_AVAILABLE = "9"
    """Information not available"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AdmitSource.PHYSICIAN_REFERRAL: "Physician referral",
    AdmitSource.CLINIC_REFERRAL: "Clinic referral",
    AdmitSource.HMO_REFERRAL: "HMO referral",
    AdmitSource.TRANSFER_FROM_A_HOSPITAL: "Transfer from a hospital",
    AdmitSource.TRANSFER_FROM_A_SKILLED_NURSING_FACILITY: "Transfer from a skilled nursing facility",
    AdmitSource.TRANSFER_FROM_ANOTHER_HEALTH_CARE_FACILITY: "Transfer from another health care facility",
    AdmitSource.EMERGENCY_ROOM: "Emergency room",
    AdmitSource.COURT_OR_LAW_ENFORCEMENT: "Court/law enforcement",
    AdmitSource.INFORMATION_NOT_AVAILABLE: "Information not available",
}
