from ...base import HL7Table

"""
HL7 Version: 2.5.1
Telecommunication use code - 0201
Table Type: HL7
"""


class TelecommunicationUseCode(HL7Table):
    """
    Telecommunication use code - 0201 // HL7 table type
    - ANSWERING_SERVICE_NUMBER
    - BEEPER_NUMBER
    - EMERGENCY_NUMBER
    - NETWORK
    - OTHER_RESIDENCE_NUMBER
    - PRIMARY_RESIDENCE_NUMBER
    - VACATION_HOME_NUMBER
    - WORK_NUMBER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0201
    """

    ANSWERING_SERVICE_NUMBER = "ASN"
    """Answering Service Number"""
    BEEPER_NUMBER = "BPN"
    """Beeper Number"""
    EMERGENCY_NUMBER = "EMR"
    """Emergency Number"""
    NETWORK = "NET"
    """Network (email) Address"""
    OTHER_RESIDENCE_NUMBER = "ORN"
    """Other Residence Number"""
    PRIMARY_RESIDENCE_NUMBER = "PRN"
    """Primary Residence Number"""
    VACATION_HOME_NUMBER = "VHN"
    """Vacation Home Number"""
    WORK_NUMBER = "WPN"
    """Work Number"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TelecommunicationUseCode.ANSWERING_SERVICE_NUMBER: "Answering Service Number",
    TelecommunicationUseCode.BEEPER_NUMBER: "Beeper Number",
    TelecommunicationUseCode.EMERGENCY_NUMBER: "Emergency Number",
    TelecommunicationUseCode.NETWORK: "Network (email) Address",
    TelecommunicationUseCode.OTHER_RESIDENCE_NUMBER: "Other Residence Number",
    TelecommunicationUseCode.PRIMARY_RESIDENCE_NUMBER: "Primary Residence Number",
    TelecommunicationUseCode.VACATION_HOME_NUMBER: "Vacation Home Number",
    TelecommunicationUseCode.WORK_NUMBER: "Work Number",
}
