from ...base import HL7Table

"""
HL7 Version: 2.5.1
Health care provider classification - 0453
Table Type: HL7
"""


class HealthCareProviderClassification(HL7Table):
    """
    Health care provider classification - 0453 // HL7 table type
    - ANSI_ASC_X12_HEALTH_CARE_PROVIDER_TAXONOMY_LEVEL_2_CLASSIFICATION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0453
    """

    ANSI_ASC_X12_HEALTH_CARE_PROVIDER_TAXONOMY_LEVEL_2_CLASSIFICATION = "SUGGESTION"
    """ANSI ASC X12 Health Care Provider Taxonomy, Level 2 - Classification"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    HealthCareProviderClassification.ANSI_ASC_X12_HEALTH_CARE_PROVIDER_TAXONOMY_LEVEL_2_CLASSIFICATION: "ANSI ASC X12 Health Care Provider Taxonomy, Level 2 - Classification",
}
