from ...base import HL7Table

"""
HL7 Version: 2.5.1
Nature of Service/Test/Observation - 0174
Table Type: User
"""


class NatureOfServiceOrTestOrObservation(HL7Table):
    """
    Nature of Service/Test/Observation - 0174 // User table type
    - ATOMIC_SERVICE_OR_TEST_OR_OBSERVATION
    - SINGLE_OBSERVATION_CALCULATED_VIA_A_RULE_OR_FORMULA_FROM_OTHER_INDEPENDENT_OBSERVATIONS
    - FUNCTIONAL_PROCEDURE_THAT_MAY_CONSIST_OF_ONE_OR_MORE_INTERRELATED_MEASURES
    - PROFILE_OR_BATTERY_CONSISTING_OF_MANY_INDEPENDENT_ATOMIC_OBSERVATIONS
    - SUPERSET_A_SET_OF_BATTERIES_OR_PROCEDURES_ORDERED_UNDER_A_SINGLE_CODE_UNIT_BUT_PROCESSED_AS_SEPARATE_BATTERIES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0174
    """

    ATOMIC_SERVICE_OR_TEST_OR_OBSERVATION = "A"
    """Atomic service/test/observation (test code or treatment code)"""
    SINGLE_OBSERVATION_CALCULATED_VIA_A_RULE_OR_FORMULA_FROM_OTHER_INDEPENDENT_OBSERVATIONS = "C"
    """Single observation calculated via a rule or formula from other independent observations (e.g., Alveolar--arterial ratio, cardiac output)"""
    FUNCTIONAL_PROCEDURE_THAT_MAY_CONSIST_OF_ONE_OR_MORE_INTERRELATED_MEASURES = "F"
    """Functional procedure that may consist of one or more interrelated measures (e.g., glucose tolerance test, creatinine clearance), usually done at different times and/or on different specimens"""
    PROFILE_OR_BATTERY_CONSISTING_OF_MANY_INDEPENDENT_ATOMIC_OBSERVATIONS = "P"
    """Profile or battery consisting of many independent atomic observations (e.g., SMA12, electrolytes), usually done at one instrument on one specimen"""
    SUPERSET_A_SET_OF_BATTERIES_OR_PROCEDURES_ORDERED_UNDER_A_SINGLE_CODE_UNIT_BUT_PROCESSED_AS_SEPARATE_BATTERIES = "S"
    """Superset--a set of batteries or procedures ordered under a single code unit but processed as separate batteries (e.g., routines = CBC, UA, electrolytes) This set indicates that the code being described is used to order multiple service/test/observation batteries. For example, a client who routinely orders a CBC, a differential, and a thyroxine as an outpatient profile might use a single, special code to order all three test batteries, instead of having to submit three separate order codes."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    NatureOfServiceOrTestOrObservation.ATOMIC_SERVICE_OR_TEST_OR_OBSERVATION: "Atomic service/test/observation (test code or treatment code)",
    NatureOfServiceOrTestOrObservation.SINGLE_OBSERVATION_CALCULATED_VIA_A_RULE_OR_FORMULA_FROM_OTHER_INDEPENDENT_OBSERVATIONS: "Single observation calculated via a rule or formula from other independent observations (e.g., Alveolar--arterial ratio, cardiac output)",
    NatureOfServiceOrTestOrObservation.FUNCTIONAL_PROCEDURE_THAT_MAY_CONSIST_OF_ONE_OR_MORE_INTERRELATED_MEASURES: "Functional procedure that may consist of one or more interrelated measures (e.g., glucose tolerance test, creatinine clearance), usually done at different times and/or on different specimens",
    NatureOfServiceOrTestOrObservation.PROFILE_OR_BATTERY_CONSISTING_OF_MANY_INDEPENDENT_ATOMIC_OBSERVATIONS: "Profile or battery consisting of many independent atomic observations (e.g., SMA12, electrolytes), usually done at one instrument on one specimen",
    NatureOfServiceOrTestOrObservation.SUPERSET_A_SET_OF_BATTERIES_OR_PROCEDURES_ORDERED_UNDER_A_SINGLE_CODE_UNIT_BUT_PROCESSED_AS_SEPARATE_BATTERIES: "Superset--a set of batteries or procedures ordered under a single code unit but processed as separate batteries (e.g., routines = CBC, UA, electrolytes) This set indicates that the code being described is used to order multiple service/test/observation batteries. For example, a client who routinely orders a CBC, a differential, and a thyroxine as an outpatient profile might use a single, special code to order all three test batteries, instead of having to submit three separate order codes.",
}
