from ...base import HL7Table

"""
HL7 Version: 2.5.1
Product source - 0248
Table Type: HL7
"""


class ProductSource(HL7Table):
    """
    Product source - 0248 // HL7 table type
    - ACTUAL_PRODUCT_INVOLVED_IN_INCIDENT_WAS_EVALUATED
    - A_PRODUCT_FROM_THE_SAME_LOT_AS_THE_ACTUAL_PRODUCT_INVOLVED_WAS_EVALUATED
    - A_PRODUCT_FROM_A_CONTROLLED_OR_NON_RELATED_INVENTORY_WAS_EVALUATED
    - A_PRODUCT_FROM_A_RESERVE_SAMPLE_WAS_EVALUATED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0248
    """

    ACTUAL_PRODUCT_INVOLVED_IN_INCIDENT_WAS_EVALUATED = "A"
    """Actual product involved in incident was evaluated"""
    A_PRODUCT_FROM_THE_SAME_LOT_AS_THE_ACTUAL_PRODUCT_INVOLVED_WAS_EVALUATED = "L"
    """A product from the same lot as the actual product involved was evaluated"""
    A_PRODUCT_FROM_A_CONTROLLED_OR_NON_RELATED_INVENTORY_WAS_EVALUATED = "N"
    """A product from a controlled/non-related inventory was evaluated"""
    A_PRODUCT_FROM_A_RESERVE_SAMPLE_WAS_EVALUATED = "R"
    """A product from a reserve sample was evaluated"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProductSource.ACTUAL_PRODUCT_INVOLVED_IN_INCIDENT_WAS_EVALUATED: "Actual product involved in incident was evaluated",
    ProductSource.A_PRODUCT_FROM_THE_SAME_LOT_AS_THE_ACTUAL_PRODUCT_INVOLVED_WAS_EVALUATED: "A product from the same lot as the actual product involved was evaluated",
    ProductSource.A_PRODUCT_FROM_A_CONTROLLED_OR_NON_RELATED_INVENTORY_WAS_EVALUATED: "A product from a controlled/non-related inventory was evaluated",
    ProductSource.A_PRODUCT_FROM_A_RESERVE_SAMPLE_WAS_EVALUATED: "A product from a reserve sample was evaluated",
}
