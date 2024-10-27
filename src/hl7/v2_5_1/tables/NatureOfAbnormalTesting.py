from ...base import HL7Table

"""
HL7 Version: 2.5.1
Nature of Abnormal Testing - 0080
Table Type: HL7
"""


class NatureOfAbnormalTesting(HL7Table):
    """
    Nature of Abnormal Testing - 0080 // HL7 table type
    - AN_AGE_BASED_POPULATION
    - BREED
    - NONE_GENERIC_NORMAL_RANGE
    - A_RACE_BASED_POPULATION
    - A_SEX_BASED_POPULATION
    - SPECIES
    - STRAIN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0080
    """

    AN_AGE_BASED_POPULATION = "A"
    """An age-based population"""
    BREED = "B"
    """Breed"""
    NONE_GENERIC_NORMAL_RANGE = "N"
    """None - generic normal range"""
    A_RACE_BASED_POPULATION = "R"
    """A race-based population"""
    A_SEX_BASED_POPULATION = "S"
    """A sex-based population"""
    SPECIES = "SP"
    """Species"""
    STRAIN = "ST"
    """Strain"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    NatureOfAbnormalTesting.AN_AGE_BASED_POPULATION: "An age-based population",
    NatureOfAbnormalTesting.BREED: "Breed",
    NatureOfAbnormalTesting.NONE_GENERIC_NORMAL_RANGE: "None - generic normal range",
    NatureOfAbnormalTesting.A_RACE_BASED_POPULATION: "A race-based population",
    NatureOfAbnormalTesting.A_SEX_BASED_POPULATION: "A sex-based population",
    NatureOfAbnormalTesting.SPECIES: "Species",
    NatureOfAbnormalTesting.STRAIN: "Strain",
}
