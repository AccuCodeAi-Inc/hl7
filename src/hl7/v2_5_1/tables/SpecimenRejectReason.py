from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen Reject Reason - 0490
Table Type: HL7
"""


class SpecimenRejectReason(HL7Table):
    """
    Specimen Reject Reason - 0490 // HL7 table type
    - EXPIRED
    - QUANTITY_NOT_SUFFICIENT
    - MISSING_PATIENT_ID_NUMBER
    - BROKEN_CONTAINER
    - CLOTTING
    - MISSING_COLLECTION_DATE
    - MISSING_PATIENT_NAME
    - HEMOLYSIS
    - IDENTIFICATION_PROBLEM
    - LABELING
    - CONTAMINATION
    - MISSING_PHLEBOTOMIST_ID
    - IMPROPER_STORAGE
    - NAME_MISSPELLING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0490
    """

    EXPIRED = "EX"
    """Expired"""
    QUANTITY_NOT_SUFFICIENT = "QS"
    """Quantity not sufficient"""
    MISSING_PATIENT_ID_NUMBER = "RA"
    """Missing patient ID number"""
    BROKEN_CONTAINER = "RB"
    """Broken container"""
    CLOTTING = "RC"
    """Clotting"""
    MISSING_COLLECTION_DATE = "RD"
    """Missing collection date"""
    MISSING_PATIENT_NAME = "RE"
    """Missing patient name"""
    HEMOLYSIS = "RH"
    """Hemolysis"""
    IDENTIFICATION_PROBLEM = "RI"
    """Identification problem"""
    LABELING = "RM"
    """Labeling"""
    CONTAMINATION = "RN"
    """Contamination"""
    MISSING_PHLEBOTOMIST_ID = "RP"
    """Missing phlebotomist ID"""
    IMPROPER_STORAGE = "RR"
    """Improper storage"""
    NAME_MISSPELLING = "RS"
    """Name misspelling"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenRejectReason.EXPIRED: "Expired",
    SpecimenRejectReason.QUANTITY_NOT_SUFFICIENT: "Quantity not sufficient",
    SpecimenRejectReason.MISSING_PATIENT_ID_NUMBER: "Missing patient ID number",
    SpecimenRejectReason.BROKEN_CONTAINER: "Broken container",
    SpecimenRejectReason.CLOTTING: "Clotting",
    SpecimenRejectReason.MISSING_COLLECTION_DATE: "Missing collection date",
    SpecimenRejectReason.MISSING_PATIENT_NAME: "Missing patient name",
    SpecimenRejectReason.HEMOLYSIS: "Hemolysis",
    SpecimenRejectReason.IDENTIFICATION_PROBLEM: "Identification problem",
    SpecimenRejectReason.LABELING: "Labeling",
    SpecimenRejectReason.CONTAMINATION: "Contamination",
    SpecimenRejectReason.MISSING_PHLEBOTOMIST_ID: "Missing phlebotomist ID",
    SpecimenRejectReason.IMPROPER_STORAGE: "Improper storage",
    SpecimenRejectReason.NAME_MISSPELLING: "Name misspelling",
}
