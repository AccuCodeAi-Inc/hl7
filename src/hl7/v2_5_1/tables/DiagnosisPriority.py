from ...base import HL7Table

"""
HL7 Version: 2.5.1
Diagnosis Priority - 0359
Table Type: HL7
"""


class DiagnosisPriority(HL7Table):
    """
    Diagnosis Priority - 0359 // HL7 table type
    - NOT_INCLUDED_IN_DIAGNOSIS_RANKING
    - THE_PRIMARY_DIAGNOSIS
    - FOR_RANKED_SECONDARY_DIAGNOSES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0359
    """

    NOT_INCLUDED_IN_DIAGNOSIS_RANKING = "0"
    """Not included in diagnosis ranking"""
    THE_PRIMARY_DIAGNOSIS = "1"
    """The primary diagnosis"""
    FOR_RANKED_SECONDARY_DIAGNOSES = "2 …"
    """For ranked secondary diagnoses"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DiagnosisPriority.NOT_INCLUDED_IN_DIAGNOSIS_RANKING: "Not included in diagnosis ranking",
    DiagnosisPriority.THE_PRIMARY_DIAGNOSIS: "The primary diagnosis",
    DiagnosisPriority.FOR_RANKED_SECONDARY_DIAGNOSES: "For ranked secondary diagnoses",
}
