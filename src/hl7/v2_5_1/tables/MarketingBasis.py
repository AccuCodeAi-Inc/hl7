from ...base import HL7Table

"""
HL7 Version: 2.5.1
Marketing basis - 0330
Table Type: HL7
"""


class MarketingBasis(HL7Table):
    """
    Marketing basis - 0330 // HL7 table type
    - _510
    - _510K
    - POST_MARKETING_STUDY
    - PREMARKETING_AUTHORIZATION
    - PREAMENDMENT
    - TRANSITIONAL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0330
    """

    _510 = "510E"
    """510 (K) exempt"""
    _510K = "510K"
    """510 (K)"""
    POST_MARKETING_STUDY = "522S"
    """Post marketing study (522)"""
    PREMARKETING_AUTHORIZATION = "PMA"
    """Premarketing authorization"""
    PREAMENDMENT = "PRE"
    """Preamendment"""
    TRANSITIONAL = "TXN"
    """Transitional"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MarketingBasis._510: "510 (K) exempt",
    MarketingBasis._510K: "510 (K)",
    MarketingBasis.POST_MARKETING_STUDY: "Post marketing study (522)",
    MarketingBasis.PREMARKETING_AUTHORIZATION: "Premarketing authorization",
    MarketingBasis.PREAMENDMENT: "Preamendment",
    MarketingBasis.TRANSITIONAL: "Transitional",
}
