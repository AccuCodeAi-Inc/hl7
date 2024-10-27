from ...base import HL7Table

"""
HL7 Version: 2.5.1
Charge type - 0122
Table Type: HL7
"""


class ChargeType(HL7Table):
    """
    Charge type - 0122 // HL7 table type
    - CHARGE
    - CONTRACT
    - CREDIT
    - DEPARTMENT
    - GRANT
    - NO_CHARGE
    - PROFESSIONAL
    - RESEARCH
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0122
    """

    CHARGE = "CH"
    """Charge"""
    CONTRACT = "CO"
    """Contract"""
    CREDIT = "CR"
    """Credit"""
    DEPARTMENT = "DP"
    """Department"""
    GRANT = "GR"
    """Grant"""
    NO_CHARGE = "NC"
    """No Charge"""
    PROFESSIONAL = "PC"
    """Professional"""
    RESEARCH = "RS"
    """Research"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ChargeType.CHARGE: "Charge",
    ChargeType.CONTRACT: "Contract",
    ChargeType.CREDIT: "Credit",
    ChargeType.DEPARTMENT: "Department",
    ChargeType.GRANT: "Grant",
    ChargeType.NO_CHARGE: "No Charge",
    ChargeType.PROFESSIONAL: "Professional",
    ChargeType.RESEARCH: "Research",
}
