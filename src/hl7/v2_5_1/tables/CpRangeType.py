from ...base import HL7Table

"""
HL7 Version: 2.5.1
CP range type - 0298
Table Type: HL7
"""


class CpRangeType(HL7Table):
    """
    CP range type - 0298 // HL7 table type
    - FLAT_RATE_APPLY_THE_ENTIRE_PRICE_TO_THIS_INTERVAL_DO_NOT_PRO_RATE_THE_PRICE_IF_THE_FULL_INTERVAL_HAS_NOT_OCCURRED_OR_BEEN_CONSUMED
    - PRO_RATE_APPLY_THIS_PRICE_TO_THIS_INTERVAL_PRO_RATED_BY_WHATEVER_PORTION_OF_THE_INTERVAL_HAS_OCCURRED_OR_BEEN_CONSUMED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0298
    """

    FLAT_RATE_APPLY_THE_ENTIRE_PRICE_TO_THIS_INTERVAL_DO_NOT_PRO_RATE_THE_PRICE_IF_THE_FULL_INTERVAL_HAS_NOT_OCCURRED_OR_BEEN_CONSUMED = "F"
    """Flat-rate. Apply the entire price to this interval, do not pro-rate the price if the full interval has not occurred/been consumed"""
    PRO_RATE_APPLY_THIS_PRICE_TO_THIS_INTERVAL_PRO_RATED_BY_WHATEVER_PORTION_OF_THE_INTERVAL_HAS_OCCURRED_OR_BEEN_CONSUMED = "P"
    """Pro-rate. Apply this price to this interval, pro-rated by whatever portion of the interval has occurred/been consumed"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CpRangeType.FLAT_RATE_APPLY_THE_ENTIRE_PRICE_TO_THIS_INTERVAL_DO_NOT_PRO_RATE_THE_PRICE_IF_THE_FULL_INTERVAL_HAS_NOT_OCCURRED_OR_BEEN_CONSUMED: "Flat-rate. Apply the entire price to this interval, do not pro-rate the price if the full interval has not occurred/been consumed",
    CpRangeType.PRO_RATE_APPLY_THIS_PRICE_TO_THIS_INTERVAL_PRO_RATED_BY_WHATEVER_PORTION_OF_THE_INTERVAL_HAS_OCCURRED_OR_BEEN_CONSUMED: "Pro-rate. Apply this price to this interval, pro-rated by whatever portion of the interval has occurred/been consumed",
}
