from ...base import HL7Table

"""
HL7 Version: 2.5.1
Controlled Substance Schedule* - 0477
Table Type: User
"""


class ControlledSubstanceSchedule_(HL7Table):
    """
    Controlled Substance Schedule* - 0477 // User table type
    - SCHEDULE_I
    - SCHEDULE_II
    - SCHEDULE_III
    - SCHEDULE_IV
    - SCHEDULE_V
    - SCHEDULE_VI
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0477
    """

    SCHEDULE_I = "I"  # Includes drugs that have a high potential for abuse, no currently accepted medical use in the United States and a lack of accepted safety for use under medical supervision.
    """Schedule I"""
    SCHEDULE_II = "II"  # Includes drugs having currently accepted medical use in the United States and a high abuse potential, with severe psychological or physical dependence liability.
    """Schedule II"""
    SCHEDULE_III = "III"  # Includes drugs having an abuse potential less than that of drugs listed in Schedules I and II. All CS III drugs have a currently accepted medical use in the United States.
    """Schedule III"""
    SCHEDULE_IV = "IV"  # Includes drugs having a lesser potential for abuse than those listed in Schedule III. CS IV drugs have a currently accepted medical use in the United States.
    """Schedule IV"""
    SCHEDULE_V = "V"  # Includes drugs having low abuse potential and limited physical or psychological dependence relative to those listed in IV and have an accepted medical use in the United States.
    """Schedule V"""
    SCHEDULE_VI = "VI"  # State defined
    """Schedule VI"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ControlledSubstanceSchedule_.SCHEDULE_I: "Schedule I",
    ControlledSubstanceSchedule_.SCHEDULE_II: "Schedule II",
    ControlledSubstanceSchedule_.SCHEDULE_III: "Schedule III",
    ControlledSubstanceSchedule_.SCHEDULE_IV: "Schedule IV",
    ControlledSubstanceSchedule_.SCHEDULE_V: "Schedule V",
    ControlledSubstanceSchedule_.SCHEDULE_VI: "Schedule VI",
}
