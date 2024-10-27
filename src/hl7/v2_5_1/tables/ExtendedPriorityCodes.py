from ...base import HL7Table

"""
HL7 Version: 2.5.1
Extended Priority Codes - 0485
Table Type: User
"""


class ExtendedPriorityCodes(HL7Table):
    """
    Extended Priority Codes - 0485 // User table type
    - ASAP
    - CALLBACK
    - PREOP
    - AS_NEEDED
    - ROUTINE
    - STAT
    - TIMING_CRITICAL
    - TD_BELOW_INTEGER_ABOVE
    - TH_BELOW_INTEGER_ABOVE
    - TL_BELOW_INTEGER_ABOVE
    - TM_BELOW_INTEGER_ABOVE
    - TS_BELOW_INTEGER_ABOVE
    - TW_BELOW_INTEGER_ABOVE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0485
    """

    ASAP = "A"  # Fill after S orders
    """ASAP"""
    CALLBACK = "C"
    """Callback"""
    PREOP = "P"
    """Preop"""
    AS_NEEDED = "PRN"
    """As needed"""
    ROUTINE = "R"  # Default
    """Routine"""
    STAT = "S"  # With highest priority
    """Stat"""
    TIMING_CRITICAL = "T"  # A request implying that it is critical to come as close as possible to the requested time, e.g., for a trough anti-microbial level.
    """Timing critical"""
    TD_BELOW_INTEGER_ABOVE = (
        "TD<integer>"  # Timing critical within &lt;integer&gt; days.
    )
    """"""
    TH_BELOW_INTEGER_ABOVE = (
        "TH<integer>"  # Timing critical within &lt;integer&gt; hours.
    )
    """"""
    TL_BELOW_INTEGER_ABOVE = (
        "TL<integer>"  # Timing critical within &lt;integer&gt; months.
    )
    """"""
    TM_BELOW_INTEGER_ABOVE = (
        "TM<integer>"  # Timing critical within &lt;integer&gt; minutes.
    )
    """"""
    TS_BELOW_INTEGER_ABOVE = (
        "TS<integer>"  # Timing critical within &lt;integer&gt; seconds.
    )
    """"""
    TW_BELOW_INTEGER_ABOVE = (
        "TW<integer>"  # Timing critical within &lt;integer&gt; weeks.
    )
    """"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ExtendedPriorityCodes.ASAP: "ASAP",
    ExtendedPriorityCodes.CALLBACK: "Callback",
    ExtendedPriorityCodes.PREOP: "Preop",
    ExtendedPriorityCodes.AS_NEEDED: "As needed",
    ExtendedPriorityCodes.ROUTINE: "Routine",
    ExtendedPriorityCodes.STAT: "Stat",
    ExtendedPriorityCodes.TIMING_CRITICAL: "Timing critical",
    ExtendedPriorityCodes.TD_BELOW_INTEGER_ABOVE: "",
    ExtendedPriorityCodes.TH_BELOW_INTEGER_ABOVE: "",
    ExtendedPriorityCodes.TL_BELOW_INTEGER_ABOVE: "",
    ExtendedPriorityCodes.TM_BELOW_INTEGER_ABOVE: "",
    ExtendedPriorityCodes.TS_BELOW_INTEGER_ABOVE: "",
    ExtendedPriorityCodes.TW_BELOW_INTEGER_ABOVE: "",
}
