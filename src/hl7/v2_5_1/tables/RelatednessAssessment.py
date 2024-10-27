from ...base import HL7Table

"""
HL7 Version: 2.5.1
Relatedness Assessment - 0250
Table Type: HL7
"""


class RelatednessAssessment(HL7Table):
    """
    Relatedness Assessment - 0250 // HL7 table type
    - HIGHLY_PROBABLE
    - IMPROBABLE
    - MODERATELY_PROBABLE
    - NOT_RELATED
    - SOMEWHAT_PROBABLE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0250
    """

    HIGHLY_PROBABLE = "H"
    """Highly probable"""
    IMPROBABLE = "I"
    """Improbable"""
    MODERATELY_PROBABLE = "M"
    """Moderately probable"""
    NOT_RELATED = "N"
    """Not related"""
    SOMEWHAT_PROBABLE = "S"
    """Somewhat probable"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RelatednessAssessment.HIGHLY_PROBABLE: "Highly probable",
    RelatednessAssessment.IMPROBABLE: "Improbable",
    RelatednessAssessment.MODERATELY_PROBABLE: "Moderately probable",
    RelatednessAssessment.NOT_RELATED: "Not related",
    RelatednessAssessment.SOMEWHAT_PROBABLE: "Somewhat probable",
}
