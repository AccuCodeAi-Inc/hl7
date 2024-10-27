from ...base import HL7Table

"""
HL7 Version: 2.5.1
Race - 0005
Table Type: User
"""


class Race(HL7Table):
    """
    Race - 0005 // User table type
    - AMERICAN_INDIAN_OR_ALASKA_NATIVE
    - ASIAN
    - BLACK_OR_AFRICAN_AMERICAN
    - NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER
    - WHITE
    - OTHER_RACE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0005
    """

    AMERICAN_INDIAN_OR_ALASKA_NATIVE = "1002-5"
    """American Indian or Alaska Native"""
    ASIAN = "2028-9"
    """Asian"""
    BLACK_OR_AFRICAN_AMERICAN = "2054-5"
    """Black or African American"""
    NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER = "2076-8"
    """Native Hawaiian or Other Pacific Islander"""
    WHITE = "2106-3"
    """White"""
    OTHER_RACE = "2131-1"
    """Other Race"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Race.AMERICAN_INDIAN_OR_ALASKA_NATIVE: "American Indian or Alaska Native",
    Race.ASIAN: "Asian",
    Race.BLACK_OR_AFRICAN_AMERICAN: "Black or African American",
    Race.NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER: "Native Hawaiian or Other Pacific Islander",
    Race.WHITE: "White",
    Race.OTHER_RACE: "Other Race",
}
