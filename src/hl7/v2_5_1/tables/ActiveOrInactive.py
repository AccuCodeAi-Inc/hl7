from ...base import HL7Table

"""
HL7 Version: 2.5.1
Active/Inactive - 0183
Table Type: HL7
"""


class ActiveOrInactive(HL7Table):
    """
    Active/Inactive - 0183 // HL7 table type
    - ACTIVE_STAFF
    - INACTIVE_STAFF
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0183
    """

    ACTIVE_STAFF = "A"
    """Active Staff"""
    INACTIVE_STAFF = "I"
    """Inactive Staff"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ActiveOrInactive.ACTIVE_STAFF: "Active Staff",
    ActiveOrInactive.INACTIVE_STAFF: "Inactive Staff",
}
