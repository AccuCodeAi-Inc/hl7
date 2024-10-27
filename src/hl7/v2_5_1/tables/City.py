from ...base import HL7Table

"""
HL7 Version: 2.5.1
City - City
Table Type: PreLoaded
"""


class City(HL7Table):
    """
    City - City // PreLoaded table type
    - ALBUQUERQUE
    - ARLINGTON
    - ATLANTA
    - AUSTIN
    - BALTIMORE
    - BOSTON
    - CHARLOTTE
    - CHICAGO
    - CLEVELAND
    - COLORADO_SPRINGS
    - COLUMBUS
    - DALLAS
    - DENVER
    - DETROIT
    - EL_PASO
    - FORT_WORTH
    - FRESNO
    - HONOLULU
    - HOUSTON
    - INDIANAPOLIS
    - JACKSONVILLE
    - KANSAS_CITY
    - LAS_VEGAS
    - LONG_BEACH
    - LOS_ANGELES
    - LOUISVILLE_JEFFERSON_COUNTY
    - MEMPHIS
    - MESA
    - MIAMI
    - MILWAUKEE
    - MINNEAPOLIS
    - NASHVILLE_DAVIDSON
    - NEW_YORK
    - OAKLAND
    - OKLAHOMA_CITY
    - OMAHA
    - PHILADELPHIA
    - PHOENIX
    - PORTLAND
    - RALEIGH
    - SACRAMENTO
    - SAN_ANTONIO
    - SAN_DIEGO
    - SAN_FRANCISCO
    - SAN_JOSE
    - SEATTLE
    - TUCSON
    - TULSA
    - VIRGINIA_BEACH
    - WASHINGTON
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/City
    """

    ALBUQUERQUE = "Albuquerque"
    """"""
    ARLINGTON = "Arlington"
    """"""
    ATLANTA = "Atlanta"
    """"""
    AUSTIN = "Austin"
    """"""
    BALTIMORE = "Baltimore"
    """"""
    BOSTON = "Boston"
    """"""
    CHARLOTTE = "Charlotte"
    """"""
    CHICAGO = "Chicago"
    """"""
    CLEVELAND = "Cleveland"
    """"""
    COLORADO_SPRINGS = "Colorado Springs"
    """"""
    COLUMBUS = "Columbus"
    """"""
    DALLAS = "Dallas"
    """"""
    DENVER = "Denver"
    """"""
    DETROIT = "Detroit"
    """"""
    EL_PASO = "El Paso"
    """"""
    FORT_WORTH = "Fort Worth"
    """"""
    FRESNO = "Fresno"
    """"""
    HONOLULU = "Honolulu"
    """"""
    HOUSTON = "Houston"
    """"""
    INDIANAPOLIS = "Indianapolis"
    """"""
    JACKSONVILLE = "Jacksonville"
    """"""
    KANSAS_CITY = "Kansas City"
    """"""
    LAS_VEGAS = "Las Vegas"
    """"""
    LONG_BEACH = "Long Beach"
    """"""
    LOS_ANGELES = "Los Angeles"
    """"""
    LOUISVILLE_JEFFERSON_COUNTY = "Louisville-Jefferson County"
    """"""
    MEMPHIS = "Memphis"
    """"""
    MESA = "Mesa"
    """"""
    MIAMI = "Miami"
    """"""
    MILWAUKEE = "Milwaukee"
    """"""
    MINNEAPOLIS = "Minneapolis"
    """"""
    NASHVILLE_DAVIDSON = "Nashville-Davidson"
    """"""
    NEW_YORK = "New York"
    """"""
    OAKLAND = "Oakland"
    """"""
    OKLAHOMA_CITY = "Oklahoma City"
    """"""
    OMAHA = "Omaha"
    """"""
    PHILADELPHIA = "Philadelphia"
    """"""
    PHOENIX = "Phoenix"
    """"""
    PORTLAND = "Portland"
    """"""
    RALEIGH = "Raleigh"
    """"""
    SACRAMENTO = "Sacramento"
    """"""
    SAN_ANTONIO = "San Antonio"
    """"""
    SAN_DIEGO = "San Diego"
    """"""
    SAN_FRANCISCO = "San Francisco"
    """"""
    SAN_JOSE = "San Jose"
    """"""
    SEATTLE = "Seattle"
    """"""
    TUCSON = "Tucson"
    """"""
    TULSA = "Tulsa"
    """"""
    VIRGINIA_BEACH = "Virginia Beach"
    """"""
    WASHINGTON = "Washington"
    """"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    City.ALBUQUERQUE: "",
    City.ARLINGTON: "",
    City.ATLANTA: "",
    City.AUSTIN: "",
    City.BALTIMORE: "",
    City.BOSTON: "",
    City.CHARLOTTE: "",
    City.CHICAGO: "",
    City.CLEVELAND: "",
    City.COLORADO_SPRINGS: "",
    City.COLUMBUS: "",
    City.DALLAS: "",
    City.DENVER: "",
    City.DETROIT: "",
    City.EL_PASO: "",
    City.FORT_WORTH: "",
    City.FRESNO: "",
    City.HONOLULU: "",
    City.HOUSTON: "",
    City.INDIANAPOLIS: "",
    City.JACKSONVILLE: "",
    City.KANSAS_CITY: "",
    City.LAS_VEGAS: "",
    City.LONG_BEACH: "",
    City.LOS_ANGELES: "",
    City.LOUISVILLE_JEFFERSON_COUNTY: "",
    City.MEMPHIS: "",
    City.MESA: "",
    City.MIAMI: "",
    City.MILWAUKEE: "",
    City.MINNEAPOLIS: "",
    City.NASHVILLE_DAVIDSON: "",
    City.NEW_YORK: "",
    City.OAKLAND: "",
    City.OKLAHOMA_CITY: "",
    City.OMAHA: "",
    City.PHILADELPHIA: "",
    City.PHOENIX: "",
    City.PORTLAND: "",
    City.RALEIGH: "",
    City.SACRAMENTO: "",
    City.SAN_ANTONIO: "",
    City.SAN_DIEGO: "",
    City.SAN_FRANCISCO: "",
    City.SAN_JOSE: "",
    City.SEATTLE: "",
    City.TUCSON: "",
    City.TULSA: "",
    City.VIRGINIA_BEACH: "",
    City.WASHINGTON: "",
}
