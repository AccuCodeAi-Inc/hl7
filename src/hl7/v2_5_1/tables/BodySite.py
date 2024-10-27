from ...base import HL7Table

"""
HL7 Version: 2.5.1
Body site - 0163
Table Type: HL7
"""


class BodySite(HL7Table):
    """
    Body site - 0163 // HL7 table type
    - BILATERAL_EARS
    - BILATERAL_NARES
    - BUTTOCK
    - CHEST_TUBE
    - LEFT_ARM
    - LEFT_ANTERIOR_CHEST
    - LEFT_ANTECUBITAL_FOSSA
    - LEFT_DELTOID
    - LEFT_EAR
    - LEFT_EXTERNAL_JUGULAR
    - LEFT_FOOT
    - LEFT_GLUTEUS_MEDIUS
    - LEFT_HAND
    - LEFT_INTERNAL_JUGULAR
    - LEFT_LOWER_ABD_QUADRANT
    - LEFT_LOWER_FOREARM
    - LEFT_MID_FOREARM
    - LEFT_NARIS
    - LEFT_POSTERIOR_CHEST
    - LEFT_SUBCLAVIAN
    - LEFT_THIGH
    - LEFT_UPPER_ARM
    - LEFT_UPPER_ABD_QUADRANT
    - LEFT_UPPER_FOREARM
    - LEFT_VENTRAGLUTEAL
    - LEFT_VASTUS_LATERALIS
    - NEBULIZED
    - RIGHT_EYE
    - LEFT_EYE
    - BILATERAL_EYES
    - PERIANAL
    - PERINEAL
    - RIGHT_ARM
    - RIGHT_ANTERIOR_CHEST
    - RIGHT_ANTECUBITAL_FOSSA
    - RIGHT_DELTOID
    - RIGHT_EAR
    - RIGHT_EXTERNAL_JUGULAR
    - RIGHT_FOOT
    - RIGHT_GLUTEUS_MEDIUS
    - RIGHT_HAND
    - RIGHT_INTERNAL_JUGULAR
    - RT_LOWER_ABD_QUADRANT
    - RIGHT_LOWER_FOREARM
    - RIGHT_MID_FOREARM
    - RIGHT_NARIS
    - RIGHT_POSTERIOR_CHEST
    - RIGHT_SUBCLAVIAN
    - RIGHT_THIGH
    - RIGHT_UPPER_ARM
    - RIGHT_UPPER_ABD_QUADRANT
    - RIGHT_UPPER_FOREARM
    - RIGHT_VENTRAGLUTEAL
    - RIGHT_VASTUS_LATERALIS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0163
    """

    BILATERAL_EARS = "BE"
    """Bilateral Ears"""
    BILATERAL_NARES = "BN"
    """Bilateral Nares"""
    BUTTOCK = "BU"
    """Buttock"""
    CHEST_TUBE = "CT"
    """Chest Tube"""
    LEFT_ARM = "LA"
    """Left Arm"""
    LEFT_ANTERIOR_CHEST = "LAC"
    """Left Anterior Chest"""
    LEFT_ANTECUBITAL_FOSSA = "LACF"
    """Left Antecubital Fossa"""
    LEFT_DELTOID = "LD"
    """Left Deltoid"""
    LEFT_EAR = "LE"
    """Left Ear"""
    LEFT_EXTERNAL_JUGULAR = "LEJ"
    """Left External Jugular"""
    LEFT_FOOT = "LF"
    """Left Foot"""
    LEFT_GLUTEUS_MEDIUS = "LG"
    """Left Gluteus Medius"""
    LEFT_HAND = "LH"
    """Left Hand"""
    LEFT_INTERNAL_JUGULAR = "LIJ"
    """Left Internal Jugular"""
    LEFT_LOWER_ABD_QUADRANT = "LLAQ"
    """Left Lower Abd Quadrant"""
    LEFT_LOWER_FOREARM = "LLFA"
    """Left Lower Forearm"""
    LEFT_MID_FOREARM = "LMFA"
    """Left Mid Forearm"""
    LEFT_NARIS = "LN"
    """Left Naris"""
    LEFT_POSTERIOR_CHEST = "LPC"
    """Left Posterior Chest"""
    LEFT_SUBCLAVIAN = "LSC"
    """Left Subclavian"""
    LEFT_THIGH = "LT"
    """Left Thigh"""
    LEFT_UPPER_ARM = "LUA"
    """Left Upper Arm"""
    LEFT_UPPER_ABD_QUADRANT = "LUAQ"
    """Left Upper Abd Quadrant"""
    LEFT_UPPER_FOREARM = "LUFA"
    """Left Upper Forearm"""
    LEFT_VENTRAGLUTEAL = "LVG"
    """Left Ventragluteal"""
    LEFT_VASTUS_LATERALIS = "LVL"
    """Left Vastus Lateralis"""
    NEBULIZED = "NB"
    """Nebulized"""
    RIGHT_EYE = "OD"
    """Right Eye"""
    LEFT_EYE = "OS"
    """Left Eye"""
    BILATERAL_EYES = "OU"
    """Bilateral Eyes"""
    PERIANAL = "PA"
    """Perianal"""
    PERINEAL = "PERIN"
    """Perineal"""
    RIGHT_ARM = "RA"
    """Right Arm"""
    RIGHT_ANTERIOR_CHEST = "RAC"
    """Right Anterior Chest"""
    RIGHT_ANTECUBITAL_FOSSA = "RACF"
    """Right Antecubital Fossa"""
    RIGHT_DELTOID = "RD"
    """Right Deltoid"""
    RIGHT_EAR = "RE"
    """Right Ear"""
    RIGHT_EXTERNAL_JUGULAR = "REJ"
    """Right External Jugular"""
    RIGHT_FOOT = "RF"
    """Right Foot"""
    RIGHT_GLUTEUS_MEDIUS = "RG"
    """Right Gluteus Medius"""
    RIGHT_HAND = "RH"
    """Right Hand"""
    RIGHT_INTERNAL_JUGULAR = "RIJ"
    """Right Internal Jugular"""
    RT_LOWER_ABD_QUADRANT = "RLAQ"
    """Rt Lower Abd Quadrant"""
    RIGHT_LOWER_FOREARM = "RLFA"
    """Right Lower Forearm"""
    RIGHT_MID_FOREARM = "RMFA"
    """Right Mid Forearm"""
    RIGHT_NARIS = "RN"
    """Right Naris"""
    RIGHT_POSTERIOR_CHEST = "RPC"
    """Right Posterior Chest"""
    RIGHT_SUBCLAVIAN = "RSC"
    """Right Subclavian"""
    RIGHT_THIGH = "RT"
    """Right Thigh"""
    RIGHT_UPPER_ARM = "RUA"
    """Right Upper Arm"""
    RIGHT_UPPER_ABD_QUADRANT = "RUAQ"
    """Right Upper Abd Quadrant"""
    RIGHT_UPPER_FOREARM = "RUFA"
    """Right Upper Forearm"""
    RIGHT_VENTRAGLUTEAL = "RVG"
    """Right Ventragluteal"""
    RIGHT_VASTUS_LATERALIS = "RVL"
    """Right Vastus Lateralis"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    BodySite.BILATERAL_EARS: "Bilateral Ears",
    BodySite.BILATERAL_NARES: "Bilateral Nares",
    BodySite.BUTTOCK: "Buttock",
    BodySite.CHEST_TUBE: "Chest Tube",
    BodySite.LEFT_ARM: "Left Arm",
    BodySite.LEFT_ANTERIOR_CHEST: "Left Anterior Chest",
    BodySite.LEFT_ANTECUBITAL_FOSSA: "Left Antecubital Fossa",
    BodySite.LEFT_DELTOID: "Left Deltoid",
    BodySite.LEFT_EAR: "Left Ear",
    BodySite.LEFT_EXTERNAL_JUGULAR: "Left External Jugular",
    BodySite.LEFT_FOOT: "Left Foot",
    BodySite.LEFT_GLUTEUS_MEDIUS: "Left Gluteus Medius",
    BodySite.LEFT_HAND: "Left Hand",
    BodySite.LEFT_INTERNAL_JUGULAR: "Left Internal Jugular",
    BodySite.LEFT_LOWER_ABD_QUADRANT: "Left Lower Abd Quadrant",
    BodySite.LEFT_LOWER_FOREARM: "Left Lower Forearm",
    BodySite.LEFT_MID_FOREARM: "Left Mid Forearm",
    BodySite.LEFT_NARIS: "Left Naris",
    BodySite.LEFT_POSTERIOR_CHEST: "Left Posterior Chest",
    BodySite.LEFT_SUBCLAVIAN: "Left Subclavian",
    BodySite.LEFT_THIGH: "Left Thigh",
    BodySite.LEFT_UPPER_ARM: "Left Upper Arm",
    BodySite.LEFT_UPPER_ABD_QUADRANT: "Left Upper Abd Quadrant",
    BodySite.LEFT_UPPER_FOREARM: "Left Upper Forearm",
    BodySite.LEFT_VENTRAGLUTEAL: "Left Ventragluteal",
    BodySite.LEFT_VASTUS_LATERALIS: "Left Vastus Lateralis",
    BodySite.NEBULIZED: "Nebulized",
    BodySite.RIGHT_EYE: "Right Eye",
    BodySite.LEFT_EYE: "Left Eye",
    BodySite.BILATERAL_EYES: "Bilateral Eyes",
    BodySite.PERIANAL: "Perianal",
    BodySite.PERINEAL: "Perineal",
    BodySite.RIGHT_ARM: "Right Arm",
    BodySite.RIGHT_ANTERIOR_CHEST: "Right Anterior Chest",
    BodySite.RIGHT_ANTECUBITAL_FOSSA: "Right Antecubital Fossa",
    BodySite.RIGHT_DELTOID: "Right Deltoid",
    BodySite.RIGHT_EAR: "Right Ear",
    BodySite.RIGHT_EXTERNAL_JUGULAR: "Right External Jugular",
    BodySite.RIGHT_FOOT: "Right Foot",
    BodySite.RIGHT_GLUTEUS_MEDIUS: "Right Gluteus Medius",
    BodySite.RIGHT_HAND: "Right Hand",
    BodySite.RIGHT_INTERNAL_JUGULAR: "Right Internal Jugular",
    BodySite.RT_LOWER_ABD_QUADRANT: "Rt Lower Abd Quadrant",
    BodySite.RIGHT_LOWER_FOREARM: "Right Lower Forearm",
    BodySite.RIGHT_MID_FOREARM: "Right Mid Forearm",
    BodySite.RIGHT_NARIS: "Right Naris",
    BodySite.RIGHT_POSTERIOR_CHEST: "Right Posterior Chest",
    BodySite.RIGHT_SUBCLAVIAN: "Right Subclavian",
    BodySite.RIGHT_THIGH: "Right Thigh",
    BodySite.RIGHT_UPPER_ARM: "Right Upper Arm",
    BodySite.RIGHT_UPPER_ABD_QUADRANT: "Right Upper Abd Quadrant",
    BodySite.RIGHT_UPPER_FOREARM: "Right Upper Forearm",
    BodySite.RIGHT_VENTRAGLUTEAL: "Right Ventragluteal",
    BodySite.RIGHT_VASTUS_LATERALIS: "Right Vastus Lateralis",
}
