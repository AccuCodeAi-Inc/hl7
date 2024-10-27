from ...base import HL7Table

"""
HL7 Version: 2.5.1
Insurance Company Contact Reason - 0232
Table Type: User
"""


class InsuranceCompanyContactReason(HL7Table):
    """
    Insurance Company Contact Reason - 0232 // User table type
    - MEDICARE_CLAIM_STATUS
    - MEDICAID_CLAIM_STATUS
    - NAME_OR_ADDRESS_CHANGE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0232
    """

    MEDICARE_CLAIM_STATUS = "01"
    """Medicare claim status"""
    MEDICAID_CLAIM_STATUS = "02"
    """Medicaid claim status"""
    NAME_OR_ADDRESS_CHANGE = "03"
    """Name/address change"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    InsuranceCompanyContactReason.MEDICARE_CLAIM_STATUS: "Medicare claim status",
    InsuranceCompanyContactReason.MEDICAID_CLAIM_STATUS: "Medicaid claim status",
    InsuranceCompanyContactReason.NAME_OR_ADDRESS_CHANGE: "Name/address change",
}
