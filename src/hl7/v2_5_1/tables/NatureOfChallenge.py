from ...base import HL7Table

"""
HL7 Version: 2.5.1
Nature of challenge - 0257
Table Type: HL7
"""


class NatureOfChallenge(HL7Table):
    """
    Nature of challenge - 0257 // HL7 table type
    - FASTING
    - EXERCISE_UNDERTAKEN_AS_CHALLENGE
    - NO_FLUID_INTAKE_FOR_THE_PERIOD_SPECIFIED_IN_THE_TIME_COMPONENT_OF_THE_TERM
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0257
    """

    FASTING = "CFST"
    """Fasting (no calorie intake) for the period specified in the time component of the term, e.g., 1H POST CFST"""
    EXERCISE_UNDERTAKEN_AS_CHALLENGE = "EXCZ"
    """Exercise undertaken as challenge (can be quantified)"""
    NO_FLUID_INTAKE_FOR_THE_PERIOD_SPECIFIED_IN_THE_TIME_COMPONENT_OF_THE_TERM = "FFST"
    """No fluid intake for the period specified in the time component of the term"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    NatureOfChallenge.FASTING: "Fasting (no calorie intake) for the period specified in the time component of the term, e.g., 1H POST CFST",
    NatureOfChallenge.EXERCISE_UNDERTAKEN_AS_CHALLENGE: "Exercise undertaken as challenge (can be quantified)",
    NatureOfChallenge.NO_FLUID_INTAKE_FOR_THE_PERIOD_SPECIFIED_IN_THE_TIME_COMPONENT_OF_THE_TERM: "No fluid intake for the period specified in the time component of the term",
}
