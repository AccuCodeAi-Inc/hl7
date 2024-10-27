from ...base import HL7Table

"""
HL7 Version: 2.5.1
Document Availability Status - 0273
Table Type: HL7
"""


class DocumentAvailabilityStatus(HL7Table):
    """
    Document Availability Status - 0273 // HL7 table type
    - AVAILABLE_FOR_PATIENT_CARE
    - DELETED
    - OBSOLETE
    - UNAVAILABLE_FOR_PATIENT_CARE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0273
    """

    AVAILABLE_FOR_PATIENT_CARE = "AV"
    """Available for patient care"""
    DELETED = "CA"
    """Deleted"""
    OBSOLETE = "OB"
    """Obsolete"""
    UNAVAILABLE_FOR_PATIENT_CARE = "UN"
    """Unavailable for patient care"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DocumentAvailabilityStatus.AVAILABLE_FOR_PATIENT_CARE: "Available for patient care",
    DocumentAvailabilityStatus.DELETED: "Deleted",
    DocumentAvailabilityStatus.OBSOLETE: "Obsolete",
    DocumentAvailabilityStatus.UNAVAILABLE_FOR_PATIENT_CARE: "Unavailable for patient care",
}
