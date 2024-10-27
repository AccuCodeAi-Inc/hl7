from ...base import HL7Table

"""
HL7 Version: 2.5.1
Health care provider area of specialization - 0454
Table Type: HL7
"""


class HealthCareProviderAreaOfSpecialization(HL7Table):
    """
    Health care provider area of specialization - 0454 // HL7 table type
    - ANSI_ASC_X12_HEALTH_CARE_PROVIDER_TAXONOMY_LEVEL_3_SPECIALIZATION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0454
    """

    ANSI_ASC_X12_HEALTH_CARE_PROVIDER_TAXONOMY_LEVEL_3_SPECIALIZATION = "SUGGESTION"
    """ANSI ASC X12 Health Care Provider Taxonomy, Level 3 - specialization"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    HealthCareProviderAreaOfSpecialization.ANSI_ASC_X12_HEALTH_CARE_PROVIDER_TAXONOMY_LEVEL_3_SPECIALIZATION: "ANSI ASC X12 Health Care Provider Taxonomy, Level 3 - specialization",
}
