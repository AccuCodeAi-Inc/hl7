from ...base import HL7Table

"""
HL7 Version: 2.5.1
Allergen Type - 0127
Table Type: User
"""


class AllergenType(HL7Table):
    """
    Allergen Type - 0127 // User table type
    - ANIMAL_ALLERGY
    - DRUG_ALLERGY
    - ENVIRONMENTAL_ALLERGY
    - FOOD_ALLERGY
    - POLLEN_ALLERGY
    - MISCELLANEOUS_ALLERGY
    - MISCELLANEOUS_CONTRAINDICATION
    - PLANT_ALLERGY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0127
    """

    ANIMAL_ALLERGY = "AA"
    """Animal Allergy"""
    DRUG_ALLERGY = "DA"
    """Drug allergy"""
    ENVIRONMENTAL_ALLERGY = "EA"
    """Environmental Allergy"""
    FOOD_ALLERGY = "FA"
    """Food allergy"""
    POLLEN_ALLERGY = "LA"
    """Pollen Allergy"""
    MISCELLANEOUS_ALLERGY = "MA"
    """Miscellaneous allergy"""
    MISCELLANEOUS_CONTRAINDICATION = "MC"
    """Miscellaneous contraindication"""
    PLANT_ALLERGY = "PA"
    """Plant Allergy"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AllergenType.ANIMAL_ALLERGY: "Animal Allergy",
    AllergenType.DRUG_ALLERGY: "Drug allergy",
    AllergenType.ENVIRONMENTAL_ALLERGY: "Environmental Allergy",
    AllergenType.FOOD_ALLERGY: "Food allergy",
    AllergenType.POLLEN_ALLERGY: "Pollen Allergy",
    AllergenType.MISCELLANEOUS_ALLERGY: "Miscellaneous allergy",
    AllergenType.MISCELLANEOUS_CONTRAINDICATION: "Miscellaneous contraindication",
    AllergenType.PLANT_ALLERGY: "Plant Allergy",
}
