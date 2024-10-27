from ...base import HL7Table

"""
HL7 Version: 2.5.1
MFN record-level error return - 0181
Table Type: User
"""


class MfnRecordLevelErrorReturn(HL7Table):
    """
    MFN record-level error return - 0181 // User table type
    - SUCCESSFUL_POSTING_OF_THE_RECORD_DEFINED_BY_THE_MFE_SEGMENT
    - UNSUCCESSFUL_POSTING_OF_THE_RECORD_DEFINED_BY_THE_MFE_SEGMENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0181
    """

    SUCCESSFUL_POSTING_OF_THE_RECORD_DEFINED_BY_THE_MFE_SEGMENT = "S"
    """Successful posting of the record defined by the MFE segment"""
    UNSUCCESSFUL_POSTING_OF_THE_RECORD_DEFINED_BY_THE_MFE_SEGMENT = "U"
    """Unsuccessful posting of the record defined by the MFE segment"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MfnRecordLevelErrorReturn.SUCCESSFUL_POSTING_OF_THE_RECORD_DEFINED_BY_THE_MFE_SEGMENT: "Successful posting of the record defined by the MFE segment",
    MfnRecordLevelErrorReturn.UNSUCCESSFUL_POSTING_OF_THE_RECORD_DEFINED_BY_THE_MFE_SEGMENT: "Unsuccessful posting of the record defined by the MFE segment",
}
