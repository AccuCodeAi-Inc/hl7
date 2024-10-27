from ...base import HL7Table

"""
HL7 Version: 2.5.1
Price type - 0205
Table Type: HL7
"""


class PriceType(HL7Table):
    """
    Price type - 0205 // HL7 table type
    - ADMINISTRATIVE_PRICE_OR_HANDLING_FEE
    - DIRECT_UNIT_COST
    - INDIRECT_UNIT_COST
    - PROFESSIONAL_FEE_FOR_PERFORMING_PROVIDER
    - TECHNOLOGY_FEE_FOR_USE_OF_EQUIPMENT
    - TOTAL_PRICE
    - UNIT_PRICE_MAY_BE_BASED_ON_LENGTH_OF_PROCEDURE_OR_SERVICE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0205
    """

    ADMINISTRATIVE_PRICE_OR_HANDLING_FEE = "AP"
    """administrative price or handling fee"""
    DIRECT_UNIT_COST = "DC"
    """direct unit cost"""
    INDIRECT_UNIT_COST = "IC"
    """indirect unit cost"""
    PROFESSIONAL_FEE_FOR_PERFORMING_PROVIDER = "PF"
    """professional fee for performing provider"""
    TECHNOLOGY_FEE_FOR_USE_OF_EQUIPMENT = "TF"
    """technology fee for use of equipment"""
    TOTAL_PRICE = "TP"
    """total price"""
    UNIT_PRICE_MAY_BE_BASED_ON_LENGTH_OF_PROCEDURE_OR_SERVICE = "UP"
    """unit price, may be based on length of procedure or service"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PriceType.ADMINISTRATIVE_PRICE_OR_HANDLING_FEE: "administrative price or handling fee",
    PriceType.DIRECT_UNIT_COST: "direct unit cost",
    PriceType.INDIRECT_UNIT_COST: "indirect unit cost",
    PriceType.PROFESSIONAL_FEE_FOR_PERFORMING_PROVIDER: "professional fee for performing provider",
    PriceType.TECHNOLOGY_FEE_FOR_USE_OF_EQUIPMENT: "technology fee for use of equipment",
    PriceType.TOTAL_PRICE: "total price",
    PriceType.UNIT_PRICE_MAY_BE_BASED_ON_LENGTH_OF_PROCEDURE_OR_SERVICE: "unit price, may be based on length of procedure or service",
}
