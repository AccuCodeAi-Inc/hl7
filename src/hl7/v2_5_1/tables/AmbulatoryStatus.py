from ...base import HL7Table

"""
HL7 Version: 2.5.1
Ambulatory Status - 0009
Table Type: User
"""


class AmbulatoryStatus(HL7Table):
    """
    Ambulatory Status - 0009 // User table type
    - NO_FUNCTIONAL_LIMITATIONS
    - AMBULATES_WITH_ASSISTIVE_DEVICE
    - WHEELCHAIR_OR_STRETCHER_BOUND
    - COMATOSE_NON_RESPONSIVE
    - DISORIENTED
    - VISION_IMPAIRED
    - HEARING_IMPAIRED
    - SPEECH_IMPAIRED
    - NON_ENGLISH_SPEAKING
    - FUNCTIONAL_LEVEL_UNKNOWN
    - OXYGEN_THERAPY
    - SPECIAL_EQUIPMENT
    - AMPUTEE
    - MASTECTOMY
    - PARAPLEGIC
    - PREGNANT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0009
    """

    NO_FUNCTIONAL_LIMITATIONS = "A0"
    """No functional limitations"""
    AMBULATES_WITH_ASSISTIVE_DEVICE = "A1"
    """Ambulates with assistive device"""
    WHEELCHAIR_OR_STRETCHER_BOUND = "A2"
    """Wheelchair/stretcher bound"""
    COMATOSE_NON_RESPONSIVE = "A3"
    """Comatose; non-responsive"""
    DISORIENTED = "A4"
    """Disoriented"""
    VISION_IMPAIRED = "A5"
    """Vision impaired"""
    HEARING_IMPAIRED = "A6"
    """Hearing impaired"""
    SPEECH_IMPAIRED = "A7"
    """Speech impaired"""
    NON_ENGLISH_SPEAKING = "A8"
    """Non-English speaking"""
    FUNCTIONAL_LEVEL_UNKNOWN = "A9"
    """Functional level unknown"""
    OXYGEN_THERAPY = "B1"
    """Oxygen therapy"""
    SPECIAL_EQUIPMENT = "B2"
    """Special equipment (tubes, IVs, catheters)"""
    AMPUTEE = "B3"
    """Amputee"""
    MASTECTOMY = "B4"
    """Mastectomy"""
    PARAPLEGIC = "B5"
    """Paraplegic"""
    PREGNANT = "B6"
    """Pregnant"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AmbulatoryStatus.NO_FUNCTIONAL_LIMITATIONS: "No functional limitations",
    AmbulatoryStatus.AMBULATES_WITH_ASSISTIVE_DEVICE: "Ambulates with assistive device",
    AmbulatoryStatus.WHEELCHAIR_OR_STRETCHER_BOUND: "Wheelchair/stretcher bound",
    AmbulatoryStatus.COMATOSE_NON_RESPONSIVE: "Comatose; non-responsive",
    AmbulatoryStatus.DISORIENTED: "Disoriented",
    AmbulatoryStatus.VISION_IMPAIRED: "Vision impaired",
    AmbulatoryStatus.HEARING_IMPAIRED: "Hearing impaired",
    AmbulatoryStatus.SPEECH_IMPAIRED: "Speech impaired",
    AmbulatoryStatus.NON_ENGLISH_SPEAKING: "Non-English speaking",
    AmbulatoryStatus.FUNCTIONAL_LEVEL_UNKNOWN: "Functional level unknown",
    AmbulatoryStatus.OXYGEN_THERAPY: "Oxygen therapy",
    AmbulatoryStatus.SPECIAL_EQUIPMENT: "Special equipment (tubes, IVs, catheters)",
    AmbulatoryStatus.AMPUTEE: "Amputee",
    AmbulatoryStatus.MASTECTOMY: "Mastectomy",
    AmbulatoryStatus.PARAPLEGIC: "Paraplegic",
    AmbulatoryStatus.PREGNANT: "Pregnant",
}
