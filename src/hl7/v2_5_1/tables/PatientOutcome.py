from ...base import HL7Table

"""
HL7 Version: 2.5.1
Patient Outcome - 0241
Table Type: HL7
"""


class PatientOutcome(HL7Table):
    """
    Patient Outcome - 0241 // HL7 table type
    - DIED
    - FULLY_RECOVERED
    - NOT_RECOVERING_OR_UNCHANGED
    - RECOVERING
    - SEQUELAE
    - UNKNOWN
    - WORSENING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0241
    """

    DIED = "D"
    """Died"""
    FULLY_RECOVERED = "F"
    """Fully recovered"""
    NOT_RECOVERING_OR_UNCHANGED = "N"
    """Not recovering/unchanged"""
    RECOVERING = "R"
    """Recovering"""
    SEQUELAE = "S"
    """Sequelae"""
    UNKNOWN = "U"
    """Unknown"""
    WORSENING = "W"
    """Worsening"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PatientOutcome.DIED: "Died",
    PatientOutcome.FULLY_RECOVERED: "Fully recovered",
    PatientOutcome.NOT_RECOVERING_OR_UNCHANGED: "Not recovering/unchanged",
    PatientOutcome.RECOVERING: "Recovering",
    PatientOutcome.SEQUELAE: "Sequelae",
    PatientOutcome.UNKNOWN: "Unknown",
    PatientOutcome.WORSENING: "Worsening",
}
