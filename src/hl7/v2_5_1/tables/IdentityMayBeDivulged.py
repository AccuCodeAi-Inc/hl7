from ...base import HL7Table

"""
HL7 Version: 2.5.1
Identity May Be Divulged - 0243
Table Type: HL7
"""


class IdentityMayBeDivulged(HL7Table):
    """
    Identity May Be Divulged - 0243 // HL7 table type
    - NO
    - NOT_APPLICABLE
    - YES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0243
    """

    NO = "N"
    """No"""
    NOT_APPLICABLE = "NA"
    """Not applicable"""
    YES = "Y"
    """Yes"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    IdentityMayBeDivulged.NO: "No",
    IdentityMayBeDivulged.NOT_APPLICABLE: "Not applicable",
    IdentityMayBeDivulged.YES: "Yes",
}
