from ...base import HL7Table

"""
HL7 Version: 2.5.1
Location characteristic ID - 0324
Table Type: User
"""


class LocationCharacteristicId(HL7Table):
    """
    Location characteristic ID - 0324 // User table type
    - GENDER_OF_PATIENT
    - IMPLANT_CAN_BE_USED_FOR_RADIATION_IMPLANT_PATIENTS
    - INFECTIOUS_DISEASE_THIS_LOCATION_CAN_BE_USED_FOR_ISOLATION
    - LEVEL_OF_CARE
    - LICENSED
    - OVERFLOW
    - PRIVACY_LEVEL_INDICATING_THE_LEVEL_OF_PRIVATE_VERSUS_NON_PRIVATE_ROOM
    - BED_IS_SET_UP
    - SHADOW_A_TEMPORARY_HOLDING_LOCATION_THAT_DOES_NOT_PHYSICALLY_EXIST
    - SMOKING
    - BED_IS_STAFFED
    - TEACHING_LOCATION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0324
    """

    GENDER_OF_PATIENT = "GEN"
    """Gender of patient(s)"""
    IMPLANT_CAN_BE_USED_FOR_RADIATION_IMPLANT_PATIENTS = "IMP"
    """Implant: can be used for radiation implant patients"""
    INFECTIOUS_DISEASE_THIS_LOCATION_CAN_BE_USED_FOR_ISOLATION = "INF"
    """Infectious disease: this location can be used for isolation"""
    LEVEL_OF_CARE = "LCR"
    """Level of care"""
    LICENSED = "LIC"
    """Licensed"""
    OVERFLOW = "OVR"
    """Overflow"""
    PRIVACY_LEVEL_INDICATING_THE_LEVEL_OF_PRIVATE_VERSUS_NON_PRIVATE_ROOM = "PRL"
    """Privacy level: indicating the level of private versus non-private room"""
    BED_IS_SET_UP = "SET"
    """Bed is set up"""
    SHADOW_A_TEMPORARY_HOLDING_LOCATION_THAT_DOES_NOT_PHYSICALLY_EXIST = "SHA"
    """Shadow: a temporary holding location that does not physically exist"""
    SMOKING = "SMK"
    """Smoking"""
    BED_IS_STAFFED = "STF"
    """Bed is staffed"""
    TEACHING_LOCATION = "TEA"
    """Teaching location"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LocationCharacteristicId.GENDER_OF_PATIENT: "Gender of patient(s)",
    LocationCharacteristicId.IMPLANT_CAN_BE_USED_FOR_RADIATION_IMPLANT_PATIENTS: "Implant: can be used for radiation implant patients",
    LocationCharacteristicId.INFECTIOUS_DISEASE_THIS_LOCATION_CAN_BE_USED_FOR_ISOLATION: "Infectious disease: this location can be used for isolation",
    LocationCharacteristicId.LEVEL_OF_CARE: "Level of care",
    LocationCharacteristicId.LICENSED: "Licensed",
    LocationCharacteristicId.OVERFLOW: "Overflow",
    LocationCharacteristicId.PRIVACY_LEVEL_INDICATING_THE_LEVEL_OF_PRIVATE_VERSUS_NON_PRIVATE_ROOM: "Privacy level: indicating the level of private versus non-private room",
    LocationCharacteristicId.BED_IS_SET_UP: "Bed is set up",
    LocationCharacteristicId.SHADOW_A_TEMPORARY_HOLDING_LOCATION_THAT_DOES_NOT_PHYSICALLY_EXIST: "Shadow: a temporary holding location that does not physically exist",
    LocationCharacteristicId.SMOKING: "Smoking",
    LocationCharacteristicId.BED_IS_STAFFED: "Bed is staffed",
    LocationCharacteristicId.TEACHING_LOCATION: "Teaching location",
}
