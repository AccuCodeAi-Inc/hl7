from ...base import HL7Table

"""
HL7 Version: 2.5.1
Formulary Status - 0478
Table Type: HL7
"""


class FormularyStatus(HL7Table):
    """
    Formulary Status - 0478 // HL7 table type
    - PHARMACEUTICAL_SUBSTANCE_IS_IN_THE_FORMULARY_BUT_GUIDELINES_APPLY
    - PHARMACEUTICAL_SUBSTANCE_IS_NOT_IN_THE_FORMULARY
    - PHARMACEUTICAL_SUBSTANCE_IS_IN_THE_FORMULARY_BUT_RESTRICTIONS_APPLY
    - PHARMACEUTICAL_SUBSTANCE_IS_IN_THE_FORMULARY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0478
    """

    PHARMACEUTICAL_SUBSTANCE_IS_IN_THE_FORMULARY_BUT_GUIDELINES_APPLY = "G"
    """Pharmaceutical substance is in the formulary, but guidelines apply"""
    PHARMACEUTICAL_SUBSTANCE_IS_NOT_IN_THE_FORMULARY = "N"
    """Pharmaceutical substance is NOT in the formulary"""
    PHARMACEUTICAL_SUBSTANCE_IS_IN_THE_FORMULARY_BUT_RESTRICTIONS_APPLY = "R"
    """Pharmaceutical substance is in the formulary, but restrictions apply"""
    PHARMACEUTICAL_SUBSTANCE_IS_IN_THE_FORMULARY = "Y"
    """Pharmaceutical substance is in the formulary"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    FormularyStatus.PHARMACEUTICAL_SUBSTANCE_IS_IN_THE_FORMULARY_BUT_GUIDELINES_APPLY: "Pharmaceutical substance is in the formulary, but guidelines apply",
    FormularyStatus.PHARMACEUTICAL_SUBSTANCE_IS_NOT_IN_THE_FORMULARY: "Pharmaceutical substance is NOT in the formulary",
    FormularyStatus.PHARMACEUTICAL_SUBSTANCE_IS_IN_THE_FORMULARY_BUT_RESTRICTIONS_APPLY: "Pharmaceutical substance is in the formulary, but restrictions apply",
    FormularyStatus.PHARMACEUTICAL_SUBSTANCE_IS_IN_THE_FORMULARY: "Pharmaceutical substance is in the formulary",
}
