from ...base import HL7Table

"""
HL7 Version: 2.5.1
Action Taken in Response to the Event - 0251
Table Type: HL7
"""


class ActionTakenInResponseToTheEvent(HL7Table):
    """
    Action Taken in Response to the Event - 0251 // HL7 table type
    - PRODUCT_DOSE_OR_FREQUENCY_OF_USE_INCREASED
    - PRODUCT_DOSE_OR_FREQUENCY_OF_USE_REDUCED
    - NONE
    - OTHER
    - PRODUCT_WITHDRAWN_PERMANENTLY
    - PRODUCT_WITHDRAWN_TEMPORARILY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0251
    """

    PRODUCT_DOSE_OR_FREQUENCY_OF_USE_INCREASED = "DI"
    """Product dose or frequency of use increased"""
    PRODUCT_DOSE_OR_FREQUENCY_OF_USE_REDUCED = "DR"
    """Product dose or frequency of use reduced"""
    NONE = "N"
    """None"""
    OTHER = "OT"
    """Other"""
    PRODUCT_WITHDRAWN_PERMANENTLY = "WP"
    """Product withdrawn permanently"""
    PRODUCT_WITHDRAWN_TEMPORARILY = "WT"
    """Product withdrawn temporarily"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ActionTakenInResponseToTheEvent.PRODUCT_DOSE_OR_FREQUENCY_OF_USE_INCREASED: "Product dose or frequency of use increased",
    ActionTakenInResponseToTheEvent.PRODUCT_DOSE_OR_FREQUENCY_OF_USE_REDUCED: "Product dose or frequency of use reduced",
    ActionTakenInResponseToTheEvent.NONE: "None",
    ActionTakenInResponseToTheEvent.OTHER: "Other",
    ActionTakenInResponseToTheEvent.PRODUCT_WITHDRAWN_PERMANENTLY: "Product withdrawn permanently",
    ActionTakenInResponseToTheEvent.PRODUCT_WITHDRAWN_TEMPORARILY: "Product withdrawn temporarily",
}
