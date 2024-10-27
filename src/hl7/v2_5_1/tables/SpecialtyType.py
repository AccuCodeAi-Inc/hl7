from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specialty Type - 0265
Table Type: User
"""


class SpecialtyType(HL7Table):
    """
    Specialty Type - 0265 // User table type
    - ALLERGY
    - AMBULATORY
    - CANCER
    - CORONARY_OR_CARDIAC_CARE
    - CRITICAL_CARE
    - CHIROPRACTIC
    - EDUCATION
    - EMERGENCY
    - FAMILY_PLANNING
    - INTENSIVE_CARE
    - ISOLATION
    - NATUROPATHIC
    - NEWBORN_NURSERY_INFANTS
    - OBSTETRICS_GYNECOLOGY
    - OBSERVATION
    - OTHER_SPECIALTY
    - PEDIATRICS
    - GENERAL_OR_FAMILY_PRACTICE
    - PEDIATRIC_OR_NEONATAL_INTENSIVE_CARE
    - PEDIATRIC_PSYCHIATRIC
    - PEDIATRIC_REHABILITATION
    - PSYCHIATRIC_INTENSIVE_CARE
    - PSYCHIATRIC
    - REHABILITATION
    - SURGERY
    - WALK_IN_CLINIC
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0265
    """

    ALLERGY = "ALC"
    """Allergy"""
    AMBULATORY = "AMB"
    """Ambulatory"""
    CANCER = "CAN"
    """Cancer"""
    CORONARY_OR_CARDIAC_CARE = "CAR"
    """Coronary/cardiac care"""
    CRITICAL_CARE = "CCR"
    """Critical care"""
    CHIROPRACTIC = "CHI"
    """Chiropractic"""
    EDUCATION = "EDI"
    """Education"""
    EMERGENCY = "EMR"
    """Emergency"""
    FAMILY_PLANNING = "FPC"
    """Family planning"""
    INTENSIVE_CARE = "INT"
    """Intensive care"""
    ISOLATION = "ISO"
    """Isolation"""
    NATUROPATHIC = "NAT"
    """Naturopathic"""
    NEWBORN_NURSERY_INFANTS = "NBI"
    """Newborn, nursery, infants"""
    OBSTETRICS_GYNECOLOGY = "OBG"
    """Obstetrics, gynecology"""
    OBSERVATION = "OBS"
    """Observation"""
    OTHER_SPECIALTY = "OTH"
    """Other specialty"""
    PEDIATRICS = "PED"
    """Pediatrics"""
    GENERAL_OR_FAMILY_PRACTICE = "PHY"
    """General/family practice"""
    PEDIATRIC_OR_NEONATAL_INTENSIVE_CARE = "PIN"
    """Pediatric/neonatal intensive care"""
    PEDIATRIC_PSYCHIATRIC = "PPS"
    """Pediatric psychiatric"""
    PEDIATRIC_REHABILITATION = "PRE"
    """Pediatric rehabilitation"""
    PSYCHIATRIC_INTENSIVE_CARE = "PSI"
    """Psychiatric intensive care"""
    PSYCHIATRIC = "PSY"
    """Psychiatric"""
    REHABILITATION = "REH"
    """Rehabilitation"""
    SURGERY = "SUR"
    """Surgery"""
    WALK_IN_CLINIC = "WIC"
    """Walk-in clinic"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecialtyType.ALLERGY: "Allergy",
    SpecialtyType.AMBULATORY: "Ambulatory",
    SpecialtyType.CANCER: "Cancer",
    SpecialtyType.CORONARY_OR_CARDIAC_CARE: "Coronary/cardiac care",
    SpecialtyType.CRITICAL_CARE: "Critical care",
    SpecialtyType.CHIROPRACTIC: "Chiropractic",
    SpecialtyType.EDUCATION: "Education",
    SpecialtyType.EMERGENCY: "Emergency",
    SpecialtyType.FAMILY_PLANNING: "Family planning",
    SpecialtyType.INTENSIVE_CARE: "Intensive care",
    SpecialtyType.ISOLATION: "Isolation",
    SpecialtyType.NATUROPATHIC: "Naturopathic",
    SpecialtyType.NEWBORN_NURSERY_INFANTS: "Newborn, nursery, infants",
    SpecialtyType.OBSTETRICS_GYNECOLOGY: "Obstetrics, gynecology",
    SpecialtyType.OBSERVATION: "Observation",
    SpecialtyType.OTHER_SPECIALTY: "Other specialty",
    SpecialtyType.PEDIATRICS: "Pediatrics",
    SpecialtyType.GENERAL_OR_FAMILY_PRACTICE: "General/family practice",
    SpecialtyType.PEDIATRIC_OR_NEONATAL_INTENSIVE_CARE: "Pediatric/neonatal intensive care",
    SpecialtyType.PEDIATRIC_PSYCHIATRIC: "Pediatric psychiatric",
    SpecialtyType.PEDIATRIC_REHABILITATION: "Pediatric rehabilitation",
    SpecialtyType.PSYCHIATRIC_INTENSIVE_CARE: "Psychiatric intensive care",
    SpecialtyType.PSYCHIATRIC: "Psychiatric",
    SpecialtyType.REHABILITATION: "Rehabilitation",
    SpecialtyType.SURGERY: "Surgery",
    SpecialtyType.WALK_IN_CLINIC: "Walk-in clinic",
}
