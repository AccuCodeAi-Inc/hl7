from ...base import HL7Table

"""
HL7 Version: 2.5.1
Manufacturers of Vaccines - 0227
Table Type: HL7
"""


class ManufacturersOfVaccines(HL7Table):
    """
    Manufacturers of Vaccines - 0227 // HL7 table type
    - ABBOTT_LABORATORIES
    - ADAMS_LABORATORIES_INC
    - ALPHA_THERAPEUTIC_CORPORATION
    - ARMOUR
    - AVENTIS_BEHRING_L_L_C
    - AVIRON
    - BAXTER_HEALTHCARE_COPORATION
    - BAXTER_HEALTH_CORPORATION
    - BAYER_CORPORATION
    - BERNA_PRODUCTS
    - BERNA_PRODUCTS_CORPORATION
    - CENTEON_L_L_C
    - CHIRON_CORPORATION
    - CELLTECH_MEDEVA_PHARMACEUTICALS
    - CONNAUGHT
    - EVANS_MEDICAL_LIMITED
    - GREER_LABORATORIES_INC
    - IMMUNO_INTERNATIONAL_AG
    - MERIEUX
    - IMMUNO_U_S_INC
    - THE_RESEARCH_FOUNDATION_FOR_MICROBIAL_DISEASES_OF_OSAKA_UNIVERSITY
    - KOREA_GREEN_CROSS_CORPORATION
    - LEDERLE
    - MASSACHUSETTS_PUBLIC_HEALTH_BIOLOGIC_LABORATORIES
    - MASSACHUSETTS_BIOLOGIC_LABORATORIES
    - MEDIMMUNE_INC
    - MILES
    - BIOPORT_CORPORATION
    - MERCK_AND_CO_INC
    - NABI
    - NORTH_AMERICAN_VACCINE_INC
    - NOVARTIS_PHARMACEUTICAL_CORPORATION
    - NEW_YORK_BLOOD_CENTER
    - ORTHO_CLINICAL_DIAGNOSTICS
    - ORGANON_TEKNIKA_CORPORATION
    - OTHER_MANUFACTURER
    - PARKEDALE_PHARMACEUTICALS
    - AVENTIS_PASTEUR_INC
    - PRAXIS_BIOLOGICS
    - POWERJECT_PHARAMACEUTICALS
    - SCLAVO_INC
    - SWISS_SERUM_AND_VACCINE_INST
    - GLAXOSMITHKLINE
    - UNKNOWN_MANUFACTURER
    - UNITED_STATES_ARMY_MEDICAL_RESEARCH_AND_MATERIAL_COMMAND
    - WYETH_AYERST
    - WAL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0227
    """

    ABBOTT_LABORATORIES = "AB"  # (includes Ross Products Division)
    """Abbott Laboratories"""
    ADAMS_LABORATORIES_INC = "AD"
    """Adams Laboratories, Inc."""
    ALPHA_THERAPEUTIC_CORPORATION = "ALP"
    """Alpha Therapeutic Corporation"""
    ARMOUR = "AR"  # [Inactive-use CEN]
    """Armour"""
    AVENTIS_BEHRING_L_L_C = (
        "AVB"  # (formerly Centeon L.L.C.; includes Armour Pharmaceutical Company)
    )
    """Aventis Behring L.L.C."""
    AVIRON = "AVI"
    """Aviron"""
    BAXTER_HEALTHCARE_COPORATION = "BA"  # [Inactive-use BAH
    """Baxter Healthcare Coporation]"""
    BAXTER_HEALTH_CORPORATION = "BAH"  # (includes Hyland Immuno, Immuno International AG, and North American Vaccine, Inc.)
    """Baxter Health Corporation"""
    BAYER_CORPORATION = "BAY"  # (includes Miles, Inc. and Cutter Laboratories)
    """Bayer Corporation"""
    BERNA_PRODUCTS = "BP"  # [Inactive-use BPC]
    """Berna Products"""
    BERNA_PRODUCTS_CORPORATION = (
        "BPC"  # (includes Swiss Serum and Vaccine Institute Berne)
    )
    """Berna Products Corporation"""
    CENTEON_L_L_C = "CEN"  # [Inactive--use AVB]
    """Centeon L.L.C."""
    CHIRON_CORPORATION = "CHI"
    """Chiron Corporation"""
    CELLTECH_MEDEVA_PHARMACEUTICALS = "CMP"  # [Inactive--use PWJ]
    """Celltech Medeva Pharmaceuticals"""
    CONNAUGHT = "CON"  # [Inactive-use PMC]
    """Connaught"""
    EVANS_MEDICAL_LIMITED = "EVN"  # [Inactive--use PWJ]
    """Evans Medical Limited"""
    GREER_LABORATORIES_INC = "GRE"
    """Greer Laboratories, Inc."""
    IMMUNO_INTERNATIONAL_AG = "IAG"  # [Inactive-use BAH]
    """Immuno International AG"""
    MERIEUX = "IM"  # [Inactive-use PMC]
    """Merieux"""
    IMMUNO_U_S_INC = "IUS"
    """Immuno-U.S., Inc."""
    THE_RESEARCH_FOUNDATION_FOR_MICROBIAL_DISEASES_OF_OSAKA_UNIVERSITY = (
        "JPN"  # (BIKEN)
    )
    """The Research Foundation for Microbial Diseases of Osaka University"""
    KOREA_GREEN_CROSS_CORPORATION = "KGC"
    """Korea Green Cross Corporation"""
    LEDERLE = "LED"  # [Inactive-use WAL]
    """Lederle"""
    MASSACHUSETTS_PUBLIC_HEALTH_BIOLOGIC_LABORATORIES = "MA"  # [Inactive-use MBL]
    """Massachusetts Public Health Biologic Laboratories"""
    MASSACHUSETTS_BIOLOGIC_LABORATORIES = (
        "MBL"  # (formerly Massachusetts Public Health Biologic Laboratories)
    )
    """Massachusetts Biologic Laboratories"""
    MEDIMMUNE_INC = "MED"
    """MedImmune, Inc."""
    MILES = "MIL"  # [Inactive-use BAY]
    """Miles"""
    BIOPORT_CORPORATION = "MIP"  # (formerly Michigan Biologic Products Institute)
    """Bioport Corporation"""
    MERCK_AND_CO_INC = "MSD"
    """Merck &amp; Co., Inc."""
    NABI = "NAB"  # (formerly North American Biologicals, Inc.)
    """NABI"""
    NORTH_AMERICAN_VACCINE_INC = "NAV"  # [Inactive-use BAH]
    """North American Vaccine, Inc."""
    NOVARTIS_PHARMACEUTICAL_CORPORATION = (
        "NOV"  # (includes Ciba-Geigy Limited and Sandoz Limited)
    )
    """Novartis Pharmaceutical Corporation"""
    NEW_YORK_BLOOD_CENTER = "NYB"
    """New York Blood Center"""
    ORTHO_CLINICAL_DIAGNOSTICS = "ORT"  # (formerly Ortho Diagnostics Systems, Inc.)
    """Ortho-Clinical Diagnostics."""
    ORGANON_TEKNIKA_CORPORATION = "OTC"
    """Organon Teknika Corporation"""
    OTHER_MANUFACTURER = "OTH"
    """Other manufacturer"""
    PARKEDALE_PHARMACEUTICALS = "PD"  # (formerly Parke-Davis)
    """Parkedale Pharmaceuticals"""
    AVENTIS_PASTEUR_INC = "PMC"  # (formerly Pasteur Merieux Connaught; includes Connaught Laboratories and Pasteur Merieux)
    """Aventis Pasteur Inc."""
    PRAXIS_BIOLOGICS = "PRX"  # [Inactive-use WAL]
    """Praxis Biologics"""
    POWERJECT_PHARAMACEUTICALS = (
        "PWJ"  # (includes Celltech Medeva Vaccines and Evans Medical Limited)
    )
    """PowerJect Pharamaceuticals"""
    SCLAVO_INC = "SCL"
    """Sclavo, Inc."""
    SWISS_SERUM_AND_VACCINE_INST = "SI"  # [Inactive-use BPC]
    """Swiss Serum and Vaccine Inst."""
    GLAXOSMITHKLINE = "SKB"  # (formerly SmithKline Beecham; includes SmithKline Beecham and Glaxo Wellcome)
    """GlaxoSmithKline"""
    UNKNOWN_MANUFACTURER = "UNK"
    """Unknown manufacturer"""
    UNITED_STATES_ARMY_MEDICAL_RESEARCH_AND_MATERIAL_COMMAND = "USA"
    """United States Army Medical Research and Material Command"""
    WYETH_AYERST = "WA"  # [Inactive-use WAL]
    """Wyeth-Ayerst"""
    WAL = "WAL"  # (includes Weyth-Lederle Vaccines and Pediatrics, Wyeth Laboratories, Lederle Laboratories, and Praxis Biologics)
    """Wyeth-Ayerst"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ManufacturersOfVaccines.ABBOTT_LABORATORIES: "Abbott Laboratories",
    ManufacturersOfVaccines.ADAMS_LABORATORIES_INC: "Adams Laboratories, Inc.",
    ManufacturersOfVaccines.ALPHA_THERAPEUTIC_CORPORATION: "Alpha Therapeutic Corporation",
    ManufacturersOfVaccines.ARMOUR: "Armour",
    ManufacturersOfVaccines.AVENTIS_BEHRING_L_L_C: "Aventis Behring L.L.C.",
    ManufacturersOfVaccines.AVIRON: "Aviron",
    ManufacturersOfVaccines.BAXTER_HEALTHCARE_COPORATION: "Baxter Healthcare Coporation]",
    ManufacturersOfVaccines.BAXTER_HEALTH_CORPORATION: "Baxter Health Corporation",
    ManufacturersOfVaccines.BAYER_CORPORATION: "Bayer Corporation",
    ManufacturersOfVaccines.BERNA_PRODUCTS: "Berna Products",
    ManufacturersOfVaccines.BERNA_PRODUCTS_CORPORATION: "Berna Products Corporation",
    ManufacturersOfVaccines.CENTEON_L_L_C: "Centeon L.L.C.",
    ManufacturersOfVaccines.CHIRON_CORPORATION: "Chiron Corporation",
    ManufacturersOfVaccines.CELLTECH_MEDEVA_PHARMACEUTICALS: "Celltech Medeva Pharmaceuticals",
    ManufacturersOfVaccines.CONNAUGHT: "Connaught",
    ManufacturersOfVaccines.EVANS_MEDICAL_LIMITED: "Evans Medical Limited",
    ManufacturersOfVaccines.GREER_LABORATORIES_INC: "Greer Laboratories, Inc.",
    ManufacturersOfVaccines.IMMUNO_INTERNATIONAL_AG: "Immuno International AG",
    ManufacturersOfVaccines.MERIEUX: "Merieux",
    ManufacturersOfVaccines.IMMUNO_U_S_INC: "Immuno-U.S., Inc.",
    ManufacturersOfVaccines.THE_RESEARCH_FOUNDATION_FOR_MICROBIAL_DISEASES_OF_OSAKA_UNIVERSITY: "The Research Foundation for Microbial Diseases of Osaka University",
    ManufacturersOfVaccines.KOREA_GREEN_CROSS_CORPORATION: "Korea Green Cross Corporation",
    ManufacturersOfVaccines.LEDERLE: "Lederle",
    ManufacturersOfVaccines.MASSACHUSETTS_PUBLIC_HEALTH_BIOLOGIC_LABORATORIES: "Massachusetts Public Health Biologic Laboratories",
    ManufacturersOfVaccines.MASSACHUSETTS_BIOLOGIC_LABORATORIES: "Massachusetts Biologic Laboratories",
    ManufacturersOfVaccines.MEDIMMUNE_INC: "MedImmune, Inc.",
    ManufacturersOfVaccines.MILES: "Miles",
    ManufacturersOfVaccines.BIOPORT_CORPORATION: "Bioport Corporation",
    ManufacturersOfVaccines.MERCK_AND_CO_INC: "Merck &amp; Co., Inc.",
    ManufacturersOfVaccines.NABI: "NABI",
    ManufacturersOfVaccines.NORTH_AMERICAN_VACCINE_INC: "North American Vaccine, Inc.",
    ManufacturersOfVaccines.NOVARTIS_PHARMACEUTICAL_CORPORATION: "Novartis Pharmaceutical Corporation",
    ManufacturersOfVaccines.NEW_YORK_BLOOD_CENTER: "New York Blood Center",
    ManufacturersOfVaccines.ORTHO_CLINICAL_DIAGNOSTICS: "Ortho-Clinical Diagnostics.",
    ManufacturersOfVaccines.ORGANON_TEKNIKA_CORPORATION: "Organon Teknika Corporation",
    ManufacturersOfVaccines.OTHER_MANUFACTURER: "Other manufacturer",
    ManufacturersOfVaccines.PARKEDALE_PHARMACEUTICALS: "Parkedale Pharmaceuticals",
    ManufacturersOfVaccines.AVENTIS_PASTEUR_INC: "Aventis Pasteur Inc.",
    ManufacturersOfVaccines.PRAXIS_BIOLOGICS: "Praxis Biologics",
    ManufacturersOfVaccines.POWERJECT_PHARAMACEUTICALS: "PowerJect Pharamaceuticals",
    ManufacturersOfVaccines.SCLAVO_INC: "Sclavo, Inc.",
    ManufacturersOfVaccines.SWISS_SERUM_AND_VACCINE_INST: "Swiss Serum and Vaccine Inst.",
    ManufacturersOfVaccines.GLAXOSMITHKLINE: "GlaxoSmithKline",
    ManufacturersOfVaccines.UNKNOWN_MANUFACTURER: "Unknown manufacturer",
    ManufacturersOfVaccines.UNITED_STATES_ARMY_MEDICAL_RESEARCH_AND_MATERIAL_COMMAND: "United States Army Medical Research and Material Command",
    ManufacturersOfVaccines.WYETH_AYERST: "Wyeth-Ayerst",
    ManufacturersOfVaccines.WAL: "Wyeth-Ayerst",
}
