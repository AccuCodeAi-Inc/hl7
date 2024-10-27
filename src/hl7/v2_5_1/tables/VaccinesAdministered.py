from ...base import HL7Table

"""
HL7 Version: 2.5.1
Vaccines administered - 0292
Table Type: HL7
"""


class VaccinesAdministered(HL7Table):
    """
    Vaccines administered - 0292 // HL7 table type
    - DTP
    - OPV
    - MMR
    - M_OR_R
    - MEASLES
    - RUBELLA
    - MUMPS
    - HEP_B_ADOLESCENT_OR_PEDIATRIC
    - TD
    - IPV
    - PNEUMOCOCCAL_CONJUGATE
    - TYPHOID_VICPS
    - DTP_HIB_HEP_B
    - MENINGOCOCCAL_C_CONJUGATE
    - HEP_A_HEP_B
    - SMALLPOX_DILUTED
    - DTAP_5_PERTUSSIS_ANTIGENS_I
    - DTAP_NOS
    - MENINGOCOCCAL_NOS
    - PNEUMOCOCCAL_NOS
    - PERTUSSIS
    - DIPHTHERIA_ANTITOXIN
    - TIG
    - IG_NOS
    - INFLUENZA_SPLIT
    - INFLUENZA_WHOLE
    - HIB_NOS
    - RABIES_INTRAMUSCULAR_INJECTION
    - BCG
    - DTAP
    - VARICELLA
    - DTP_HIB
    - PLAGUE
    - ANTHRAX
    - TYPHOID_ORAL
    - CHOLERA
    - BOTULINUM_ANTITOXIN
    - DT
    - CMVIG
    - HBIG
    - HEP_A_PEDIATRIC_NOS
    - MENINGOCOCCAL
    - PNEUMOCOCCAL
    - RIG
    - TETANUS_TOXOID
    - VZIG
    - YELLOW_FEVER
    - RUBELLA_OR_MUMPS
    - JAPANESE_ENCEPHALITIS
    - RABIES_INTRADERMAL_INJECTION
    - TYPHOID_PARENTERAL
    - HEP_B_ADOLESCENT_OR_HIGH_RISK_INFANT_2
    - HEP_B_ADULT4
    - HEP_B_DIALYSIS
    - HEP_B_NOS
    - HIB
    - _47
    - _48
    - _49
    - DTAP_HIB
    - HIB_HEP_B
    - HEP_A_ADULT
    - TYPHOID_PARENTERAL_AKD
    - ADENOVIRUS_TYPE_4
    - ADENOVIRUS_TYPE_7
    - DENGUE_FEVER
    - HANTAVIRUS
    - HEP_C
    - HEP_E
    - HERPES_SIMPLEX_2
    - HIV
    - HPV
    - JUNIN_VIRUS
    - LEISHMANIASIS
    - LEPROSY
    - LYME_DISEASE
    - MALARIA
    - MELANOMA
    - PARAINFLUENZA_3
    - Q_FEVER
    - RSV_IGIV
    - RHEUMATIC_FEVER
    - RIFT_VALLEY_FEVER
    - ROTAVIRUS
    - SMALLPOX
    - STAPHYLOCOCCUS_BACTERIO_LYSATE
    - TICK_BORNE_ENCEPHALITIS
    - TULAREMIA_VACCINE
    - VACCINIA_IMMUNE_GLOBULIN
    - VEE_LIVE
    - VEE_INACTIVATED
    - ADENOVIRUS_NOS1
    - HEP_A_PED_OR_ADOL_2_DOSE
    - HEP_A_PED_OR_ADOL_3_DOSE
    - HEP_A_NOS
    - IG
    - IGIV
    - INFLUENZA_NOS
    - POLIO_NOS
    - RABIES_NOS
    - TYPHOID_NOS
    - VEE_NOS
    - RSV_MAB
    - MMRV
    - TST_OT_TINE_TEST
    - TST_PPD_INTRADERMAL
    - TST_PPD_TINE_TEST
    - TST_NOS
    - RESERVED_DO_NOT_USE
    - NO_VACCINE_ADMINISTERED
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0292
    """

    DTP = "01"  # diphtheria, tetanus toxoids and pertussis vaccine
    """DTP"""
    OPV = "02"  # poliovirus vaccine, live, oral
    """OPV"""
    MMR = "03"  # measles, mumps and rubella virus vaccine
    """MMR"""
    M_OR_R = "04"  # measles and rubella virus vaccine
    """M/R"""
    MEASLES = "05"  # measles virus vaccine
    """measles"""
    RUBELLA = "06"  # rubella virus vaccine
    """rubella"""
    MUMPS = "07"  # mumps virus vaccine
    """mumps"""
    HEP_B_ADOLESCENT_OR_PEDIATRIC = (
        "08"  # hepatitis B vaccine, pediatric or pediatric/adolescent dosage
    )
    """Hep B, adolescent or pediatric"""
    TD = "09"  # tetanus and diphtheria toxoids, adsorbed for adult use
    """Td (adult)"""
    IPV = "10"  # poliovirus vaccine, inactivated
    """IPV"""
    PNEUMOCOCCAL_CONJUGATE = "100"  # pneumococcal conjugate vaccine, polyvalent
    """pneumococcal conjugate"""
    TYPHOID_VICPS = "101"  # typhoid Vi capsular polysaccharide vaccine
    """typhoid, ViCPs"""
    DTP_HIB_HEP_B = (
        "102"  # DTP- Haemophilus influenzae type b conjugate and hepatitis b vaccine
    )
    """DTP-Hib-Hep B"""
    MENINGOCOCCAL_C_CONJUGATE = "103"  # meningococcal C conjugate vaccine
    """meningococcal C conjugate"""
    HEP_A_HEP_B = "104"  # hepatitis A and hepatitis B vaccine
    """Hep A-Hep B"""
    SMALLPOX_DILUTED = "105"  # smallpox vaccine, diluted
    """smallpox, diluted"""
    DTAP_5_PERTUSSIS_ANTIGENS_I = "106"  # diphtheria, tetanus toxoids and acellular pertussis vaccine, 5 pertussis antigens
    """DTaP, 5 pertussis antigens [i]"""
    DTAP_NOS = "107"  # diphtheria, tetanus toxoids and acellular pertussis vaccine, NOS
    """DTaP, NOS"""
    MENINGOCOCCAL_NOS = "108"  # meningococcal vaccine, NOS
    """meningococcal, NOS"""
    PNEUMOCOCCAL_NOS = "109"  # pneumococcal vaccine, NOS
    """pneumococcal, NOS"""
    PERTUSSIS = "11"  # pertussis vaccine
    """pertussis"""
    DIPHTHERIA_ANTITOXIN = "12"  # diphtheria antitoxin
    """diphtheria antitoxin"""
    TIG = "13"  # tetanus immune globulin
    """TIG"""
    IG_NOS = "14"  # immune globulin, NOS
    """IG, NOS"""
    INFLUENZA_SPLIT = (
        "15"  # influenza virus vaccine, split virus (incl. purified surface antigen)
    )
    """influenza, split (incl. purified surface antigen)"""
    INFLUENZA_WHOLE = "16"  # influenza virus vaccine, whole virus
    """influenza, whole"""
    HIB_NOS = "17"  # Haemophilus influenzae type b vaccine, conjugate NOS
    """Hib, NOS"""
    RABIES_INTRAMUSCULAR_INJECTION = "18"  # rabies vaccine, for intramuscular injection
    """rabies, intramuscular injection"""
    BCG = "19"  # Bacillus Calmette-Guerin vaccine
    """BCG"""
    DTAP = "20"  # diphtheria, tetanus toxoids and acellular pertussis vaccine
    """DTaP"""
    VARICELLA = "21"  # varicella virus vaccine
    """Varicella"""
    DTP_HIB = "22"  # DTP-Haemophilus influenzae type b conjugate vaccine
    """DTP-Hib"""
    PLAGUE = "23"  # plague vaccine
    """plague"""
    ANTHRAX = "24"  # anthrax vaccine
    """anthrax"""
    TYPHOID_ORAL = "25"  # typhoid vaccine, live, oral
    """typhoid, oral"""
    CHOLERA = "26"  # cholera vaccine
    """cholera"""
    BOTULINUM_ANTITOXIN = "27"  # botulinum antitoxin
    """botulinum antitoxin"""
    DT = "28"  # diphtheria and tetanus toxoids, adsorbed for pediatric use
    """DT (pediatric)"""
    CMVIG = "29"  # cytomegalovirus immune globulin, intravenous
    """CMVIG"""
    HBIG = "30"  # hepatitis B immune globulin
    """HBIG"""
    HEP_A_PEDIATRIC_NOS = "31"  # hepatitis A vaccine, pediatric dosage, NOS
    """Hep A, pediatric, NOS"""
    MENINGOCOCCAL = "32"  # meningococcal polysaccharide vaccine
    """meningococcal"""
    PNEUMOCOCCAL = "33"  # pneumococcal polysaccharide vaccine
    """pneumococcal"""
    RIG = "34"  # rabies immune globulin
    """RIG"""
    TETANUS_TOXOID = "35"  # tetanus toxoid
    """tetanus toxoid"""
    VZIG = "36"  # varicella zoster immune globulin
    """VZIG"""
    YELLOW_FEVER = "37"  # yellow fever vaccine
    """yellow fever"""
    RUBELLA_OR_MUMPS = "38"  # rubella and mumps virus vaccine
    """rubella/mumps"""
    JAPANESE_ENCEPHALITIS = "39"  # Japanese encephalitis vaccine
    """Japanese encephalitis"""
    RABIES_INTRADERMAL_INJECTION = "40"  # rabies vaccine, for intradermal injection
    """rabies, intradermal injection"""
    TYPHOID_PARENTERAL = (
        "41"  # typhoid vaccine, parenteral, other than acetone-killed, dried
    )
    """typhoid, parenteral"""
    HEP_B_ADOLESCENT_OR_HIGH_RISK_INFANT_2 = (
        "42"  # hepatitis B vaccine, adolescent/high risk infant dosage
    )
    """Hep B, adolescent/high risk infant 2"""
    HEP_B_ADULT4 = "43"  # hepatitis B vaccine, adult dosage
    """Hep B, adult4"""
    HEP_B_DIALYSIS = "44"  # hepatitis B vaccine, dialysis patient dosage
    """Hep B, dialysis"""
    HEP_B_NOS = "45"  # hepatitis B vaccine, NOS
    """Hep B, NOS"""
    HIB = "46"  # Haemophilus influenzae type b vaccine, PRP-D conjugate
    """Hib (PRP-D)"""
    _47 = "47"  # Haemophilus influenzae type b vaccine, HbOC conjugate
    """Hib (HbOC)"""
    _48 = "48"  # Haemophilus influenzae type b vaccine, PRP-T conjugate
    """Hib (PRP-T)"""
    _49 = "49"  # Haemophilus influenzae type b vaccine, PRP-OMP conjugate
    """Hib (PRP-OMP)"""
    DTAP_HIB = "50"  # DTaP-Haemophilus influenzae type b conjugate vaccine
    """DTaP-Hib"""
    HIB_HEP_B = "51"  # Haemophilus influenzae type b conjugate and Hepatitis B vaccine
    """Hib-Hep B"""
    HEP_A_ADULT = "52"  # hepatitis A vaccine, adult dosage
    """Hep A, adult"""
    TYPHOID_PARENTERAL_AKD = (
        "53"  # typhoid vaccine, parenteral, acetone-killed, dried (U.S. military)
    )
    """typhoid, parenteral, AKD (U.S. military)"""
    ADENOVIRUS_TYPE_4 = "54"  # adenovirus vaccine, type 4, live, oral
    """adenovirus, type 4"""
    ADENOVIRUS_TYPE_7 = "55"  # adenovirus vaccine, type 7, live, oral
    """adenovirus, type 7"""
    DENGUE_FEVER = "56"  # dengue fever vaccine
    """dengue fever"""
    HANTAVIRUS = "57"  # hantavirus vaccine
    """hantavirus"""
    HEP_C = "58"  # hepatitis C vaccine
    """Hep C"""
    HEP_E = "59"  # hepatitis E vaccine
    """Hep E"""
    HERPES_SIMPLEX_2 = "60"  # herpes simplex virus, type 2 vaccine
    """herpes simplex 2"""
    HIV = "61"  # human immunodeficiency virus vaccine
    """HIV"""
    HPV = "62"  # human papilloma virus vaccine
    """HPV"""
    JUNIN_VIRUS = "63"  # Junin virus vaccine
    """Junin virus"""
    LEISHMANIASIS = "64"  # leishmaniasis vaccine
    """leishmaniasis"""
    LEPROSY = "65"  # leprosy vaccine
    """leprosy"""
    LYME_DISEASE = "66"  # Lyme disease vaccine
    """Lyme disease"""
    MALARIA = "67"  # malaria vaccine
    """malaria"""
    MELANOMA = "68"  # melanoma vaccine
    """melanoma"""
    PARAINFLUENZA_3 = "69"  # parainfluenza-3 virus vaccine
    """parainfluenza-3"""
    Q_FEVER = "70"  # Q fever vaccine
    """Q fever"""
    RSV_IGIV = "71"  # respiratory syncytial virus immune globulin, intravenous
    """RSV-IGIV"""
    RHEUMATIC_FEVER = "72"  # rheumatic fever vaccine
    """rheumatic fever"""
    RIFT_VALLEY_FEVER = "73"  # Rift Valley fever vaccine
    """Rift Valley fever"""
    ROTAVIRUS = "74"  # rotavirus vaccine, tetravalent, live, oral
    """rotavirus"""
    SMALLPOX = "75"  # smallpox vaccine
    """smallpox"""
    STAPHYLOCOCCUS_BACTERIO_LYSATE = "76"  # Staphylococcus bacteriophage lysate
    """Staphylococcus bacterio lysate"""
    TICK_BORNE_ENCEPHALITIS = "77"  # tick-borne encephalitis vaccine
    """tick-borne encephalitis"""
    TULAREMIA_VACCINE = "78"  # tularemia vaccine
    """tularemia vaccine"""
    VACCINIA_IMMUNE_GLOBULIN = "79"  # vaccinia immune globulin
    """vaccinia immune globulin"""
    VEE_LIVE = "80"  # Venezuelan equine encephalitis, live, attenuated
    """VEE, live"""
    VEE_INACTIVATED = "81"  # Venezuelan equine encephalitis, inactivated
    """VEE, inactivated"""
    ADENOVIRUS_NOS1 = "82"  # adenovirus vaccine, NOS
    """adenovirus, NOS1"""
    HEP_A_PED_OR_ADOL_2_DOSE = (
        "83"  # hepatitis A vaccine, pediatric/adolescent dosage, 2 dose schedule
    )
    """Hep A, ped/adol, 2 dose"""
    HEP_A_PED_OR_ADOL_3_DOSE = (
        "84"  # hepatitis A vaccine, pediatric/adolescent dosage, 3 dose schedule
    )
    """Hep A, ped/adol, 3 dose"""
    HEP_A_NOS = "85"  # hepatitis A vaccine, NOS
    """Hep A, NOS"""
    IG = "86"  # immune globulin, intramuscular
    """IG"""
    IGIV = "87"  # immune globulin, intravenous
    """IGIV"""
    INFLUENZA_NOS = "88"  # influenza virus vaccine, NOS
    """influenza, NOS"""
    POLIO_NOS = "89"  # poliovirus vaccine, NOS
    """polio, NOS"""
    RABIES_NOS = "90"  # rabies vaccine, NOS
    """rabies, NOS"""
    TYPHOID_NOS = "91"  # typhoid vaccine, NOS
    """typhoid, NOS"""
    VEE_NOS = "92"  # Venezuelan equine encephalitis vaccine, NOS
    """VEE, NOS"""
    RSV_MAB = "93"  # respiratory syncytial virus monoclonal antibody (palivizumab), intramuscular
    """RSV-MAb"""
    MMRV = "94"  # measles, mumps, rubella, and varicella virus vaccine
    """MMRV"""
    TST_OT_TINE_TEST = (
        "95"  # tuberculin skin test; old tuberculin, multipuncture device
    )
    """TST-OT tine test"""
    TST_PPD_INTRADERMAL = (
        "96"  # tuberculin skin test; purified protein derivative solution, intradermal
    )
    """TST-PPD intradermal"""
    TST_PPD_TINE_TEST = (
        "97"  # tuberculin skin test; purified protein derivative, multipuncture device
    )
    """TST-PPD tine test"""
    TST_NOS = "98"  # tuberculin skin test; NOS
    """TST, NOS"""
    RESERVED_DO_NOT_USE = "99"  # RESERVED - do not use
    """RESERVED - do not use"""
    NO_VACCINE_ADMINISTERED = "998"  # no vaccine administered
    """no vaccine administered"""
    UNKNOWN = "999"  # unknown vaccine or immune globulin
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    VaccinesAdministered.DTP: "DTP",
    VaccinesAdministered.OPV: "OPV",
    VaccinesAdministered.MMR: "MMR",
    VaccinesAdministered.M_OR_R: "M/R",
    VaccinesAdministered.MEASLES: "measles",
    VaccinesAdministered.RUBELLA: "rubella",
    VaccinesAdministered.MUMPS: "mumps",
    VaccinesAdministered.HEP_B_ADOLESCENT_OR_PEDIATRIC: "Hep B, adolescent or pediatric",
    VaccinesAdministered.TD: "Td (adult)",
    VaccinesAdministered.IPV: "IPV",
    VaccinesAdministered.PNEUMOCOCCAL_CONJUGATE: "pneumococcal conjugate",
    VaccinesAdministered.TYPHOID_VICPS: "typhoid, ViCPs",
    VaccinesAdministered.DTP_HIB_HEP_B: "DTP-Hib-Hep B",
    VaccinesAdministered.MENINGOCOCCAL_C_CONJUGATE: "meningococcal C conjugate",
    VaccinesAdministered.HEP_A_HEP_B: "Hep A-Hep B",
    VaccinesAdministered.SMALLPOX_DILUTED: "smallpox, diluted",
    VaccinesAdministered.DTAP_5_PERTUSSIS_ANTIGENS_I: "DTaP, 5 pertussis antigens [i]",
    VaccinesAdministered.DTAP_NOS: "DTaP, NOS",
    VaccinesAdministered.MENINGOCOCCAL_NOS: "meningococcal, NOS",
    VaccinesAdministered.PNEUMOCOCCAL_NOS: "pneumococcal, NOS",
    VaccinesAdministered.PERTUSSIS: "pertussis",
    VaccinesAdministered.DIPHTHERIA_ANTITOXIN: "diphtheria antitoxin",
    VaccinesAdministered.TIG: "TIG",
    VaccinesAdministered.IG_NOS: "IG, NOS",
    VaccinesAdministered.INFLUENZA_SPLIT: "influenza, split (incl. purified surface antigen)",
    VaccinesAdministered.INFLUENZA_WHOLE: "influenza, whole",
    VaccinesAdministered.HIB_NOS: "Hib, NOS",
    VaccinesAdministered.RABIES_INTRAMUSCULAR_INJECTION: "rabies, intramuscular injection",
    VaccinesAdministered.BCG: "BCG",
    VaccinesAdministered.DTAP: "DTaP",
    VaccinesAdministered.VARICELLA: "Varicella",
    VaccinesAdministered.DTP_HIB: "DTP-Hib",
    VaccinesAdministered.PLAGUE: "plague",
    VaccinesAdministered.ANTHRAX: "anthrax",
    VaccinesAdministered.TYPHOID_ORAL: "typhoid, oral",
    VaccinesAdministered.CHOLERA: "cholera",
    VaccinesAdministered.BOTULINUM_ANTITOXIN: "botulinum antitoxin",
    VaccinesAdministered.DT: "DT (pediatric)",
    VaccinesAdministered.CMVIG: "CMVIG",
    VaccinesAdministered.HBIG: "HBIG",
    VaccinesAdministered.HEP_A_PEDIATRIC_NOS: "Hep A, pediatric, NOS",
    VaccinesAdministered.MENINGOCOCCAL: "meningococcal",
    VaccinesAdministered.PNEUMOCOCCAL: "pneumococcal",
    VaccinesAdministered.RIG: "RIG",
    VaccinesAdministered.TETANUS_TOXOID: "tetanus toxoid",
    VaccinesAdministered.VZIG: "VZIG",
    VaccinesAdministered.YELLOW_FEVER: "yellow fever",
    VaccinesAdministered.RUBELLA_OR_MUMPS: "rubella/mumps",
    VaccinesAdministered.JAPANESE_ENCEPHALITIS: "Japanese encephalitis",
    VaccinesAdministered.RABIES_INTRADERMAL_INJECTION: "rabies, intradermal injection",
    VaccinesAdministered.TYPHOID_PARENTERAL: "typhoid, parenteral",
    VaccinesAdministered.HEP_B_ADOLESCENT_OR_HIGH_RISK_INFANT_2: "Hep B, adolescent/high risk infant 2",
    VaccinesAdministered.HEP_B_ADULT4: "Hep B, adult4",
    VaccinesAdministered.HEP_B_DIALYSIS: "Hep B, dialysis",
    VaccinesAdministered.HEP_B_NOS: "Hep B, NOS",
    VaccinesAdministered.HIB: "Hib (PRP-D)",
    VaccinesAdministered._47: "Hib (HbOC)",
    VaccinesAdministered._48: "Hib (PRP-T)",
    VaccinesAdministered._49: "Hib (PRP-OMP)",
    VaccinesAdministered.DTAP_HIB: "DTaP-Hib",
    VaccinesAdministered.HIB_HEP_B: "Hib-Hep B",
    VaccinesAdministered.HEP_A_ADULT: "Hep A, adult",
    VaccinesAdministered.TYPHOID_PARENTERAL_AKD: "typhoid, parenteral, AKD (U.S. military)",
    VaccinesAdministered.ADENOVIRUS_TYPE_4: "adenovirus, type 4",
    VaccinesAdministered.ADENOVIRUS_TYPE_7: "adenovirus, type 7",
    VaccinesAdministered.DENGUE_FEVER: "dengue fever",
    VaccinesAdministered.HANTAVIRUS: "hantavirus",
    VaccinesAdministered.HEP_C: "Hep C",
    VaccinesAdministered.HEP_E: "Hep E",
    VaccinesAdministered.HERPES_SIMPLEX_2: "herpes simplex 2",
    VaccinesAdministered.HIV: "HIV",
    VaccinesAdministered.HPV: "HPV",
    VaccinesAdministered.JUNIN_VIRUS: "Junin virus",
    VaccinesAdministered.LEISHMANIASIS: "leishmaniasis",
    VaccinesAdministered.LEPROSY: "leprosy",
    VaccinesAdministered.LYME_DISEASE: "Lyme disease",
    VaccinesAdministered.MALARIA: "malaria",
    VaccinesAdministered.MELANOMA: "melanoma",
    VaccinesAdministered.PARAINFLUENZA_3: "parainfluenza-3",
    VaccinesAdministered.Q_FEVER: "Q fever",
    VaccinesAdministered.RSV_IGIV: "RSV-IGIV",
    VaccinesAdministered.RHEUMATIC_FEVER: "rheumatic fever",
    VaccinesAdministered.RIFT_VALLEY_FEVER: "Rift Valley fever",
    VaccinesAdministered.ROTAVIRUS: "rotavirus",
    VaccinesAdministered.SMALLPOX: "smallpox",
    VaccinesAdministered.STAPHYLOCOCCUS_BACTERIO_LYSATE: "Staphylococcus bacterio lysate",
    VaccinesAdministered.TICK_BORNE_ENCEPHALITIS: "tick-borne encephalitis",
    VaccinesAdministered.TULAREMIA_VACCINE: "tularemia vaccine",
    VaccinesAdministered.VACCINIA_IMMUNE_GLOBULIN: "vaccinia immune globulin",
    VaccinesAdministered.VEE_LIVE: "VEE, live",
    VaccinesAdministered.VEE_INACTIVATED: "VEE, inactivated",
    VaccinesAdministered.ADENOVIRUS_NOS1: "adenovirus, NOS1",
    VaccinesAdministered.HEP_A_PED_OR_ADOL_2_DOSE: "Hep A, ped/adol, 2 dose",
    VaccinesAdministered.HEP_A_PED_OR_ADOL_3_DOSE: "Hep A, ped/adol, 3 dose",
    VaccinesAdministered.HEP_A_NOS: "Hep A, NOS",
    VaccinesAdministered.IG: "IG",
    VaccinesAdministered.IGIV: "IGIV",
    VaccinesAdministered.INFLUENZA_NOS: "influenza, NOS",
    VaccinesAdministered.POLIO_NOS: "polio, NOS",
    VaccinesAdministered.RABIES_NOS: "rabies, NOS",
    VaccinesAdministered.TYPHOID_NOS: "typhoid, NOS",
    VaccinesAdministered.VEE_NOS: "VEE, NOS",
    VaccinesAdministered.RSV_MAB: "RSV-MAb",
    VaccinesAdministered.MMRV: "MMRV",
    VaccinesAdministered.TST_OT_TINE_TEST: "TST-OT tine test",
    VaccinesAdministered.TST_PPD_INTRADERMAL: "TST-PPD intradermal",
    VaccinesAdministered.TST_PPD_TINE_TEST: "TST-PPD tine test",
    VaccinesAdministered.TST_NOS: "TST, NOS",
    VaccinesAdministered.RESERVED_DO_NOT_USE: "RESERVED - do not use",
    VaccinesAdministered.NO_VACCINE_ADMINISTERED: "no vaccine administered",
    VaccinesAdministered.UNKNOWN: "Unknown",
}
