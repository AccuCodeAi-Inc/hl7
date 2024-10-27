from ...base import HL7Table

"""
HL7 Version: 2.5.1
Match algorithms - 0393
Table Type: User
"""


class MatchAlgorithms(HL7Table):
    """
    Match algorithms - 0393 // User table type
    - PROPRIETARY_ALGORITHM_FOR_LINKSOFT_V2_01
    - PROPRIETARY_ALGORITHM_FOR_MATCHWARE_V1_2
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0393
    """

    PROPRIETARY_ALGORITHM_FOR_LINKSOFT_V2_01 = "LINKSOFT_2.01"
    """Proprietary algorithm for LinkSoft v2.01"""
    PROPRIETARY_ALGORITHM_FOR_MATCHWARE_V1_2 = "MATCHWARE_1.2"
    """Proprietary algorithm for MatchWare v1.2"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MatchAlgorithms.PROPRIETARY_ALGORITHM_FOR_LINKSOFT_V2_01: "Proprietary algorithm for LinkSoft v2.01",
    MatchAlgorithms.PROPRIETARY_ALGORITHM_FOR_MATCHWARE_V1_2: "Proprietary algorithm for MatchWare v1.2",
}
