from ...base import HL7Table

"""
HL7 Version: 2.5.1
Hospital Service - 0069
Table Type: User
"""


class HospitalService(HL7Table):
    """
    Hospital Service - 0069 // User table type
    - CARDIAC_SERVICE
    - MEDICAL_SERVICE
    - PULMONARY_SERVICE
    - SURGICAL_SERVICE
    - UROLOGY_SERVICE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0069
    """

    CARDIAC_SERVICE = "CAR"
    """Cardiac Service"""
    MEDICAL_SERVICE = "MED"
    """Medical Service"""
    PULMONARY_SERVICE = "PUL"
    """Pulmonary Service"""
    SURGICAL_SERVICE = "SUR"
    """Surgical Service"""
    UROLOGY_SERVICE = "URO"
    """Urology Service"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    HospitalService.CARDIAC_SERVICE: "Cardiac Service",
    HospitalService.MEDICAL_SERVICE: "Medical Service",
    HospitalService.PULMONARY_SERVICE: "Pulmonary Service",
    HospitalService.SURGICAL_SERVICE: "Surgical Service",
    HospitalService.UROLOGY_SERVICE: "Urology Service",
}
