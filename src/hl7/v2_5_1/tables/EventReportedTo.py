from ...base import HL7Table

"""
HL7 Version: 2.5.1
Event Reported To - 0236
Table Type: HL7
"""


class EventReportedTo(HL7Table):
    """
    Event Reported To - 0236 // HL7 table type
    - DISTRIBUTOR
    - LOCAL_FACILITY_OR_USER_FACILITY
    - MANUFACTURER
    - REGULATORY_AGENCY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0236
    """

    DISTRIBUTOR = "D"
    """Distributor"""
    LOCAL_FACILITY_OR_USER_FACILITY = "L"
    """Local facility/user facility"""
    MANUFACTURER = "M"
    """Manufacturer"""
    REGULATORY_AGENCY = "R"
    """Regulatory agency"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EventReportedTo.DISTRIBUTOR: "Distributor",
    EventReportedTo.LOCAL_FACILITY_OR_USER_FACILITY: "Local facility/user facility",
    EventReportedTo.MANUFACTURER: "Manufacturer",
    EventReportedTo.REGULATORY_AGENCY: "Regulatory agency",
}
