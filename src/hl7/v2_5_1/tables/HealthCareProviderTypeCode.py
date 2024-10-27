from ...base import HL7Table

"""
HL7 Version: 2.5.1
Health care provider type code - 0452
Table Type: HL7
"""


class HealthCareProviderTypeCode(HL7Table):
    """
    Health care provider type code - 0452 // HL7 table type
    - ANSI_ASC_X12_HEALTH_CARE_PROVIDER_TAXONOMY_LEVEL_1_TYPE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0452
    """

    ANSI_ASC_X12_HEALTH_CARE_PROVIDER_TAXONOMY_LEVEL_1_TYPE = "SUGGESTION"
    """ANSI ASC X12 Health Care Provider Taxonomy, Level 1 - Type"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    HealthCareProviderTypeCode.ANSI_ASC_X12_HEALTH_CARE_PROVIDER_TAXONOMY_LEVEL_1_TYPE: "ANSI ASC X12 Health Care Provider Taxonomy, Level 1 - Type",
}
