from ...base import HL7Table

"""
HL7 Version: 2.5.1
Response flag - 0121
Table Type: HL7
"""


class ResponseFlag(HL7Table):
    """
    Response flag - 0121 // HL7 table type
    - SAME_AS_R_ALSO_OTHER_ASSOCIATED_SEGMENTS
    - REPORT_EXCEPTIONS_ONLY
    - SAME_AS_D_PLUS_CONFIRMATIONS_EXPLICITLY
    - ONLY_THE_MSA_SEGMENT_IS_RETURNED
    - SAME_AS_E_ALSO_REPLACEMENT_AND_PARENT_CHILD
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0121
    """

    SAME_AS_R_ALSO_OTHER_ASSOCIATED_SEGMENTS = "D"
    """Same as R, also other associated segments"""
    REPORT_EXCEPTIONS_ONLY = "E"
    """Report exceptions only"""
    SAME_AS_D_PLUS_CONFIRMATIONS_EXPLICITLY = "F"
    """Same as D, plus confirmations explicitly"""
    ONLY_THE_MSA_SEGMENT_IS_RETURNED = "N"
    """Only the MSA segment is returned"""
    SAME_AS_E_ALSO_REPLACEMENT_AND_PARENT_CHILD = "R"
    """Same as E, also Replacement and Parent-Child"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ResponseFlag.SAME_AS_R_ALSO_OTHER_ASSOCIATED_SEGMENTS: "Same as R, also other associated segments",
    ResponseFlag.REPORT_EXCEPTIONS_ONLY: "Report exceptions only",
    ResponseFlag.SAME_AS_D_PLUS_CONFIRMATIONS_EXPLICITLY: "Same as D, plus confirmations explicitly",
    ResponseFlag.ONLY_THE_MSA_SEGMENT_IS_RETURNED: "Only the MSA segment is returned",
    ResponseFlag.SAME_AS_E_ALSO_REPLACEMENT_AND_PARENT_CHILD: "Same as E, also Replacement and Parent-Child",
}
