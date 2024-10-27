from ...base import HL7Table

"""
HL7 Version: 2.5.1
Precision - 0529
Table Type: HL7
"""


class Precision(HL7Table):
    """
    Precision - 0529 // HL7 table type
    - DAY
    - HOUR
    - MONTH
    - MINUTE
    - SECOND
    - YEAR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0529
    """

    DAY = "D"  # Retained for backward compatibility only
    """day"""
    HOUR = "H"  # Retained for backward compatibility only
    """hour"""
    MONTH = "L"  # Retained for backward compatibility only
    """month"""
    MINUTE = "M"  # Retained for backward compatibility only
    """minute"""
    SECOND = "S"  # Retained for backward compatibility only
    """second"""
    YEAR = "Y"  # Retained for backward compatibility only
    """year"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Precision.DAY: "day",
    Precision.HOUR: "hour",
    Precision.MONTH: "month",
    Precision.MINUTE: "minute",
    Precision.SECOND: "second",
    Precision.YEAR: "year",
}
