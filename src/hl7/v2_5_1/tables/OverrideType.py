from ...base import HL7Table

"""
HL7 Version: 2.5.1
Override type - 0518
Table Type: User
"""


class OverrideType(HL7Table):
    """
    Override type - 0518 // User table type
    - EQUIVALENCE_OVERRIDE
    - EXTENSION_OVERRIDE
    - INTERVAL_OVERRIDE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0518
    """

    EQUIVALENCE_OVERRIDE = "EQV"  # Identifies an override where a service is being performed agains t an order that the system does not recognize as equivalent to the ordered service.
    """Equivalence Override"""
    EXTENSION_OVERRIDE = "EXTN"  # Identifies an override where a service is being performed for longe r than the ordered period of time.
    """Extension Override"""
    INTERVAL_OVERRIDE = "INLV"  # Identifies an override where a repetition of service is being performed sooner than the ordered frequency.
    """Interval Override"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OverrideType.EQUIVALENCE_OVERRIDE: "Equivalence Override",
    OverrideType.EXTENSION_OVERRIDE: "Extension Override",
    OverrideType.INTERVAL_OVERRIDE: "Interval Override",
}
