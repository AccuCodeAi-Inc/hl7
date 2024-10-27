from ...base import HL7Table

"""
HL7 Version: 2.5.1
Organization, agency, department - 0530
Table Type: User
"""


class Organization_Agency_Department(HL7Table):
    """
    Organization, agency, department - 0530 // User table type
    - AMERICAN_EXPRESS
    - DRUG_ENFORCEMENT_AGENCY
    - DEPARTMENT_OF_DEFENSE
    - MASTER_CARD
    - VETERANS_AFFAIRS
    - VISA
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0530
    """

    AMERICAN_EXPRESS = "AE"
    """American Express"""
    DRUG_ENFORCEMENT_AGENCY = "DEA"  # The US Drug Enforcement Administration does not solely assign DEA numbers in the United States. Hospitals have the authority to issue DEA numbers to their medical residents. These DEA numbers are based upon the hospital’s DEA number, but the authority rests with the hospital on the assignment to the residents. Thus, DEA as an Assigning Authority is necessary in addition to DEA as an Identifier Type.
    """Drug Enforcement Agency"""
    DEPARTMENT_OF_DEFENSE = "DOD"  # In some countries e.g., the US, more than one department may issue a military identifier. Hence, US is not sufficient as the Assigning Authority.
    """Department of Defense"""
    MASTER_CARD = "MC"
    """Master Card"""
    VETERANS_AFFAIRS = "VA"
    """Veterans Affairs"""
    VISA = "VI"
    """Visa"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Organization_Agency_Department.AMERICAN_EXPRESS: "American Express",
    Organization_Agency_Department.DRUG_ENFORCEMENT_AGENCY: "Drug Enforcement Agency",
    Organization_Agency_Department.DEPARTMENT_OF_DEFENSE: "Department of Defense",
    Organization_Agency_Department.MASTER_CARD: "Master Card",
    Organization_Agency_Department.VETERANS_AFFAIRS: "Veterans Affairs",
    Organization_Agency_Department.VISA: "Visa",
}
