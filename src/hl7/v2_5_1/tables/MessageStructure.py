from ...base import HL7Table

"""
HL7 Version: 2.5.1
Message structure - 0354
Table Type: HL7
"""


class MessageStructure(HL7Table):
    """
    Message structure - 0354 // HL7 table type
    - VARIES
    - A19
    - A01_A04_A08_A13
    - A02
    - A03
    - A05_A14_A28_A31
    - A06_A07
    - A09_A10_A11_A12
    - A15
    - A16
    - A17
    - A18
    - A20
    - A21_A22_A23_A25_A26_A27_A29_A32_A33
    - A24
    - A30_A34_A35_A36_A46_A47_A48_A49
    - A37
    - A38
    - A39_A40_A41_A42
    - A43_A44
    - A45
    - A50_A51
    - A52_A53_A55
    - A54
    - A60
    - A61_A62
    - P01
    - P02
    - P05
    - P06
    - P10
    - P12
    - O29
    - O30
    - O32
    - O31
    - C01_C02_C03_C04_C05_C06_C07_C08
    - C09_C10_C11_C12
    - P03
    - P11
    - T12
    - P04
    - Q01
    - Q03
    - U07
    - U09
    - U08
    - R07
    - Q04
    - R09
    - U02
    - U01
    - U06
    - U05
    - U12_U13
    - T01_T03_T05_T07_T09_T11
    - T02_T04_T06_T08_T10
    - MFA
    - M01_M02_M03_M04_M05_M06_M07_M08_M09_M10_M11
    - M01
    - M02
    - M03
    - M04
    - M05
    - M06
    - M07
    - M08
    - M09
    - M10
    - M11
    - M12
    - M13
    - M15
    - M01_M02_M03_M04_M05_M06
    - MFR_M01
    - N02
    - N01
    - NMR_N01
    - O27
    - O03
    - O19
    - O23
    - O21
    - O33
    - O35
    - O07
    - O09
    - O05
    - O28
    - O04
    - R04
    - O20
    - O24
    - O22
    - O34
    - O36
    - O01
    - O08
    - O10
    - O02
    - O06
    - R01
    - R30
    - R31
    - R32
    - W01
    - Q06
    - OSR_Q06
    - R21
    - R22
    - R23
    - R24
    - P07_P08
    - PC6_PC7_PC8
    - B01_B02
    - B03
    - B04_B05_B06
    - B07
    - B08
    - PCC_PCG_PCH_PCJ
    - PCB_PCD
    - PC1_PC2_PC3
    - PCL
    - PCA
    - PC5
    - PCF
    - Q11
    - Q13
    - Q15
    - Q21_Q22_Q23_Q24_Q25
    - Q02
    - J01_J02
    - W02
    - QRY_A19
    - QRY_P04
    - PC4_PC9_PCE_PCK
    - Q01_Q26_Q27_Q28_Q29_Q30
    - QRY_Q02
    - R02
    - QRY_T12
    - Q16
    - Q17
    - RAR
    - O17
    - I05
    - I06
    - RDE_O01
    - O11_O25
    - RDR
    - O13
    - K15
    - I12_I13_I14_I15
    - RER
    - RGR
    - O15
    - ROR
    - I08_I09_I10_I11
    - I01_I04
    - I02
    - I03
    - RQA_I08
    - I05_I06
    - I01_I02_I03_I07
    - I04
    - Q09
    - RRA_O02
    - O18
    - O14
    - O12_O26
    - O16
    - RRI_I12
    - K11
    - K21
    - K22
    - K23_K24
    - K13
    - S12_S13_S14_S15_S16_S17_S18_S19_S20_S21_S22_S23_S24_S26
    - Q08
    - S25
    - SQR_S25
    - S01_S02_S03_S04_S05_S06_S07_S08_S09_S10_S11
    - SRR_S01
    - U04
    - U03
    - P09
    - R08
    - TBR_R09
    - U10_U11
    - Q05
    - Q07
    - V01
    - V03
    - V04
    - V02
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0354
    """

    VARIES = "ACK"
    """Varies"""
    A19 = "ADR_A19"
    """A19"""
    A01_A04_A08_A13 = "ADT_A01"
    """A01, A04, A08, A13"""
    A02 = "ADT_A02"
    """A02"""
    A03 = "ADT_A03"
    """A03"""
    A05_A14_A28_A31 = "ADT_A05"
    """A05, A14, A28, A31"""
    A06_A07 = "ADT_A06"
    """A06, A07"""
    A09_A10_A11_A12 = "ADT_A09"
    """A09, A10, A11, A12"""
    A15 = "ADT_A15"
    """A15"""
    A16 = "ADT_A16"
    """A16"""
    A17 = "ADT_A17"
    """A17"""
    A18 = "ADT_A18"
    """A18"""
    A20 = "ADT_A20"
    """A20"""
    A21_A22_A23_A25_A26_A27_A29_A32_A33 = "ADT_A21"
    """A21, A22, A23, A25, A26, A27, A29, A32, A33"""
    A24 = "ADT_A24"
    """A24"""
    A30_A34_A35_A36_A46_A47_A48_A49 = "ADT_A30"
    """A30, A34, A35, A36, A46, A47, A48, A49"""
    A37 = "ADT_A37"
    """A37"""
    A38 = "ADT_A38"
    """A38"""
    A39_A40_A41_A42 = "ADT_A39"
    """A39, A40, A41, A42"""
    A43_A44 = "ADT_A43"
    """A43, A44"""
    A45 = "ADT_A45"
    """A45"""
    A50_A51 = "ADT_A50"
    """A50, A51"""
    A52_A53_A55 = "ADT_A52"
    """A52, A53, A55"""
    A54 = "ADT_A54"
    """A54"""
    A60 = "ADT_A60"
    """A60"""
    A61_A62 = "ADT_A61"
    """A61, A62"""
    P01 = "BAR_P01"
    """P01"""
    P02 = "BAR_P02"
    """P02"""
    P05 = "BAR_P05"
    """P05"""
    P06 = "BAR_P06"
    """P06"""
    P10 = "BAR_P10"
    """P10"""
    P12 = "BAR_P12"
    """P12"""
    O29 = "BPS_O29"
    """O29"""
    O30 = "BRP_030"
    """O30"""
    O32 = "BRT_O32"
    """O32"""
    O31 = "BTS_O31"
    """O31"""
    C01_C02_C03_C04_C05_C06_C07_C08 = "CRM_C01"
    """C01, C02, C03, C04, C05, C06, C07, C08"""
    C09_C10_C11_C12 = "CSU_C09"
    """C09, C10, C11, C12"""
    P03 = "DFT_P03"
    """P03"""
    P11 = "DFT_P11"
    """P11"""
    T12 = "DOC_T12"
    """T12"""
    P04 = "DSR_P04"
    """P04"""
    Q01 = "DSR_Q01"
    """Q01"""
    Q03 = "DSR_Q03"
    """Q03"""
    U07 = "EAC_U07"
    """U07"""
    U09 = "EAN_U09"
    """U09"""
    U08 = "EAR_U08"
    """U08"""
    R07 = "EDR_R07"
    """R07"""
    Q04 = "EQQ_Q04"
    """Q04"""
    R09 = "ERP_R09"
    """R09"""
    U02 = "ESR_U02"
    """U02"""
    U01 = "ESU_U01"
    """U01"""
    U06 = "INR_U06"
    """U06"""
    U05 = "INU_U05"
    """U05"""
    U12_U13 = "LSU_U12"
    """U12, U13"""
    T01_T03_T05_T07_T09_T11 = "MDM_T01"
    """T01, T03, T05, T07, T09, T11"""
    T02_T04_T06_T08_T10 = "MDM_T02"
    """T02, T04, T06, T08, T10"""
    MFA = "MFD_MFA"
    """MFA"""
    M01_M02_M03_M04_M05_M06_M07_M08_M09_M10_M11 = "MFK_M01"
    """M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11"""
    M01 = "MFN_M01"
    """M01"""
    M02 = "MFN_M02"
    """M02"""
    M03 = "MFN_M03"
    """M03"""
    M04 = "MFN_M04"
    """M04"""
    M05 = "MFN_M05"
    """M05"""
    M06 = "MFN_M06"
    """M06"""
    M07 = "MFN_M07"
    """M07"""
    M08 = "MFN_M08"
    """M08"""
    M09 = "MFN_M09"
    """M09"""
    M10 = "MFN_M10"
    """M10"""
    M11 = "MFN_M11"
    """M11"""
    M12 = "MFN_M12"
    """M12"""
    M13 = "MFN_M13"
    """M13"""
    M15 = "MFN_M15"
    """M15"""
    M01_M02_M03_M04_M05_M06 = "MFQ_M01"
    """M01, M02, M03, M04, M05, M06"""
    MFR_M01 = "MFR_M01"
    """M01, M02, M03, M04, M05, M06"""
    N02 = "NMD_N02"
    """N02"""
    N01 = "NMQ_N01"
    """N01"""
    NMR_N01 = "NMR_N01"
    """N01"""
    O27 = "OMB_O27"
    """O27"""
    O03 = "OMD_O03"
    """O03"""
    O19 = "OMG_O19"
    """O19"""
    O23 = "OMI_O23"
    """O23"""
    O21 = "OML_O21"
    """O21"""
    O33 = "OML_O33"
    """O33"""
    O35 = "OML_O35"
    """O35"""
    O07 = "OMN_O07"
    """O07"""
    O09 = "OMP_O09"
    """O09"""
    O05 = "OMS_O05"
    """O05"""
    O28 = "ORB_O28"
    """O28"""
    O04 = "ORD_O04"
    """O04"""
    R04 = "ORF_R04"
    """R04"""
    O20 = "ORG_O20"
    """O20"""
    O24 = "ORI_O24"
    """O24"""
    O22 = "ORL_O22"
    """O22"""
    O34 = "ORL_O34"
    """O34"""
    O36 = "ORL_O36"
    """O36"""
    O01 = "ORM_O01"
    """O01"""
    O08 = "ORN_O08"
    """O08"""
    O10 = "ORP_O10"
    """O10"""
    O02 = "ORR_R02"
    """O02"""
    O06 = "ORS_O06"
    """O06"""
    R01 = "ORU_R01"
    """R01"""
    R30 = "ORU_R30"
    """R30"""
    R31 = "ORU_R31"
    """R31"""
    R32 = "ORU_R32"
    """R32"""
    W01 = "ORU_W01"
    """W01"""
    Q06 = "OSQ_Q06"
    """Q06"""
    OSR_Q06 = "OSR_Q06"
    """Q06"""
    R21 = "OUL_R21"
    """R21"""
    R22 = "OUL_R22"
    """R22"""
    R23 = "OUL_R23"
    """R23"""
    R24 = "OUL_R24"
    """R24"""
    P07_P08 = "PEX_P07"
    """P07, P08"""
    PC6_PC7_PC8 = "PGL_PC6"
    """PC6, PC7, PC8"""
    B01_B02 = "PMU_B01"
    """B01, B02"""
    B03 = "PMU_B03"
    """B03"""
    B04_B05_B06 = "PMU_B04"
    """B04, B05, B06"""
    B07 = "PMU_B07"
    """B07"""
    B08 = "PMU_B08"
    """B08"""
    PCC_PCG_PCH_PCJ = "PPG_PCG"
    """PCC, PCG, PCH, PCJ"""
    PCB_PCD = "PPP_PCB"
    """PCB, PCD"""
    PC1_PC2_PC3 = "PPR_PC1"
    """PC1, PC2, PC3"""
    PCL = "PPT_PCL"
    """PCL"""
    PCA = "PPV_PCA"
    """PCA"""
    PC5 = "PRR_PC5"
    """PC5"""
    PCF = "PTR_PCF"
    """PCF"""
    Q11 = "QBP_Q11"
    """Q11"""
    Q13 = "QBP_Q13"
    """Q13"""
    Q15 = "QBP_Q15"
    """Q15"""
    Q21_Q22_Q23_Q24_Q25 = "QBP_Q21"
    """Q21, Q22, Q23,Q24, Q25"""
    Q02 = "QCK_Q02"
    """Q02"""
    J01_J02 = "QCN_J01"
    """J01, J02"""
    W02 = "QRF_W02"
    """W02"""
    QRY_A19 = "QRY_A19"
    """A19"""
    QRY_P04 = "QRY_P04"
    """P04"""
    PC4_PC9_PCE_PCK = "QRY_PC4"
    """PC4, PC9, PCE, PCK"""
    Q01_Q26_Q27_Q28_Q29_Q30 = "QRY_Q01"
    """Q01, Q26, Q27, Q28, Q29, Q30"""
    QRY_Q02 = "QRY_Q02"
    """Q02"""
    R02 = "QRY_R02"
    """R02"""
    QRY_T12 = "QRY_T12"
    """T12"""
    Q16 = "QSB_Q16"
    """Q16"""
    Q17 = "QVR_Q17"
    """Q17"""
    RAR = "RAR_RAR"
    """RAR"""
    O17 = "RAS_O17"
    """O17"""
    I05 = "RCI_I05"
    """I05"""
    I06 = "RCL_I06"
    """I06"""
    RDE_O01 = "RDE_O01"
    """O01"""
    O11_O25 = "RDE_O11"
    """O11, O25"""
    RDR = "RDR_RDR"
    """RDR"""
    O13 = "RDS_O13"
    """O13"""
    K15 = "RDY_K15"
    """K15"""
    I12_I13_I14_I15 = "REF_I12"
    """I12, I13, I14, I15"""
    RER = "RER_RER"
    """RER"""
    RGR = "RGR_RGR"
    """RGR"""
    O15 = "RGV_O15"
    """O15"""
    ROR = "ROR_ROR"
    """ROR"""
    I08_I09_I10_I11 = "RPA_I08"
    """I08, I09. I10, I11"""
    I01_I04 = "RPI_I01"
    """I01, I04"""
    I02 = "RPL_I02"
    """I02"""
    I03 = "RPR_I03"
    """I03"""
    RQA_I08 = "RQA_I08"
    """I08, I09, I10, I11"""
    I05_I06 = "RQC_I05"
    """I05, I06"""
    I01_I02_I03_I07 = "RQI_I01"
    """I01, I02, I03, I07"""
    I04 = "RQP_I04"
    """I04"""
    Q09 = "RQQ_Q09"
    """Q09"""
    RRA_O02 = "RRA_O02"
    """O02"""
    O18 = "RRA_O18"
    """O18"""
    O14 = "RRD_O14"
    """O14"""
    O12_O26 = "RRE_O12"
    """O12, O26"""
    O16 = "RRG_O16"
    """O16"""
    RRI_I12 = "RRI_I12"
    """I12, I13, I14, I15"""
    K11 = "RSP_K11"
    """K11"""
    K21 = "RSP_K21"
    """K21"""
    K22 = "RSP_K22"
    """K22"""
    K23_K24 = "RSP_K23"
    """K23, K24"""
    K13 = "RTB_K13"
    """K13"""
    S12_S13_S14_S15_S16_S17_S18_S19_S20_S21_S22_S23_S24_S26 = "SIU_S12"
    """S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S26"""
    Q08 = "SPQ_Q08"
    """Q08"""
    S25 = "SQM_S25"
    """S25"""
    SQR_S25 = "SQR_S25"
    """S25"""
    S01_S02_S03_S04_S05_S06_S07_S08_S09_S10_S11 = "SRM_S01"
    """S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11"""
    SRR_S01 = "SRR_S01"
    """S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11"""
    U04 = "SSR_U04"
    """U04"""
    U03 = "SSU_U03"
    """U03"""
    P09 = "SUR_P09"
    """P09"""
    R08 = "TBR_R08"
    """R08"""
    TBR_R09 = "TBR_R09"
    """R09"""
    U10_U11 = "TCU_U10"
    """U10, U11"""
    Q05 = "UDM_Q05"
    """Q05"""
    Q07 = "VQQ_Q07"
    """Q07"""
    V01 = "VXQ_V01"
    """V01"""
    V03 = "VXR_V03"
    """V03"""
    V04 = "VXU_V04"
    """V04"""
    V02 = "VXX_V02"
    """V02"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MessageStructure.VARIES: "Varies",
    MessageStructure.A19: "A19",
    MessageStructure.A01_A04_A08_A13: "A01, A04, A08, A13",
    MessageStructure.A02: "A02",
    MessageStructure.A03: "A03",
    MessageStructure.A05_A14_A28_A31: "A05, A14, A28, A31",
    MessageStructure.A06_A07: "A06, A07",
    MessageStructure.A09_A10_A11_A12: "A09, A10, A11, A12",
    MessageStructure.A15: "A15",
    MessageStructure.A16: "A16",
    MessageStructure.A17: "A17",
    MessageStructure.A18: "A18",
    MessageStructure.A20: "A20",
    MessageStructure.A21_A22_A23_A25_A26_A27_A29_A32_A33: "A21, A22, A23, A25, A26, A27, A29, A32, A33",
    MessageStructure.A24: "A24",
    MessageStructure.A30_A34_A35_A36_A46_A47_A48_A49: "A30, A34, A35, A36, A46, A47, A48, A49",
    MessageStructure.A37: "A37",
    MessageStructure.A38: "A38",
    MessageStructure.A39_A40_A41_A42: "A39, A40, A41, A42",
    MessageStructure.A43_A44: "A43, A44",
    MessageStructure.A45: "A45",
    MessageStructure.A50_A51: "A50, A51",
    MessageStructure.A52_A53_A55: "A52, A53, A55",
    MessageStructure.A54: "A54",
    MessageStructure.A60: "A60",
    MessageStructure.A61_A62: "A61, A62",
    MessageStructure.P01: "P01",
    MessageStructure.P02: "P02",
    MessageStructure.P05: "P05",
    MessageStructure.P06: "P06",
    MessageStructure.P10: "P10",
    MessageStructure.P12: "P12",
    MessageStructure.O29: "O29",
    MessageStructure.O30: "O30",
    MessageStructure.O32: "O32",
    MessageStructure.O31: "O31",
    MessageStructure.C01_C02_C03_C04_C05_C06_C07_C08: "C01, C02, C03, C04, C05, C06, C07, C08",
    MessageStructure.C09_C10_C11_C12: "C09, C10, C11, C12",
    MessageStructure.P03: "P03",
    MessageStructure.P11: "P11",
    MessageStructure.T12: "T12",
    MessageStructure.P04: "P04",
    MessageStructure.Q01: "Q01",
    MessageStructure.Q03: "Q03",
    MessageStructure.U07: "U07",
    MessageStructure.U09: "U09",
    MessageStructure.U08: "U08",
    MessageStructure.R07: "R07",
    MessageStructure.Q04: "Q04",
    MessageStructure.R09: "R09",
    MessageStructure.U02: "U02",
    MessageStructure.U01: "U01",
    MessageStructure.U06: "U06",
    MessageStructure.U05: "U05",
    MessageStructure.U12_U13: "U12, U13",
    MessageStructure.T01_T03_T05_T07_T09_T11: "T01, T03, T05, T07, T09, T11",
    MessageStructure.T02_T04_T06_T08_T10: "T02, T04, T06, T08, T10",
    MessageStructure.MFA: "MFA",
    MessageStructure.M01_M02_M03_M04_M05_M06_M07_M08_M09_M10_M11: "M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11",
    MessageStructure.M01: "M01",
    MessageStructure.M02: "M02",
    MessageStructure.M03: "M03",
    MessageStructure.M04: "M04",
    MessageStructure.M05: "M05",
    MessageStructure.M06: "M06",
    MessageStructure.M07: "M07",
    MessageStructure.M08: "M08",
    MessageStructure.M09: "M09",
    MessageStructure.M10: "M10",
    MessageStructure.M11: "M11",
    MessageStructure.M12: "M12",
    MessageStructure.M13: "M13",
    MessageStructure.M15: "M15",
    MessageStructure.M01_M02_M03_M04_M05_M06: "M01, M02, M03, M04, M05, M06",
    MessageStructure.MFR_M01: "M01, M02, M03, M04, M05, M06",
    MessageStructure.N02: "N02",
    MessageStructure.N01: "N01",
    MessageStructure.NMR_N01: "N01",
    MessageStructure.O27: "O27",
    MessageStructure.O03: "O03",
    MessageStructure.O19: "O19",
    MessageStructure.O23: "O23",
    MessageStructure.O21: "O21",
    MessageStructure.O33: "O33",
    MessageStructure.O35: "O35",
    MessageStructure.O07: "O07",
    MessageStructure.O09: "O09",
    MessageStructure.O05: "O05",
    MessageStructure.O28: "O28",
    MessageStructure.O04: "O04",
    MessageStructure.R04: "R04",
    MessageStructure.O20: "O20",
    MessageStructure.O24: "O24",
    MessageStructure.O22: "O22",
    MessageStructure.O34: "O34",
    MessageStructure.O36: "O36",
    MessageStructure.O01: "O01",
    MessageStructure.O08: "O08",
    MessageStructure.O10: "O10",
    MessageStructure.O02: "O02",
    MessageStructure.O06: "O06",
    MessageStructure.R01: "R01",
    MessageStructure.R30: "R30",
    MessageStructure.R31: "R31",
    MessageStructure.R32: "R32",
    MessageStructure.W01: "W01",
    MessageStructure.Q06: "Q06",
    MessageStructure.OSR_Q06: "Q06",
    MessageStructure.R21: "R21",
    MessageStructure.R22: "R22",
    MessageStructure.R23: "R23",
    MessageStructure.R24: "R24",
    MessageStructure.P07_P08: "P07, P08",
    MessageStructure.PC6_PC7_PC8: "PC6, PC7, PC8",
    MessageStructure.B01_B02: "B01, B02",
    MessageStructure.B03: "B03",
    MessageStructure.B04_B05_B06: "B04, B05, B06",
    MessageStructure.B07: "B07",
    MessageStructure.B08: "B08",
    MessageStructure.PCC_PCG_PCH_PCJ: "PCC, PCG, PCH, PCJ",
    MessageStructure.PCB_PCD: "PCB, PCD",
    MessageStructure.PC1_PC2_PC3: "PC1, PC2, PC3",
    MessageStructure.PCL: "PCL",
    MessageStructure.PCA: "PCA",
    MessageStructure.PC5: "PC5",
    MessageStructure.PCF: "PCF",
    MessageStructure.Q11: "Q11",
    MessageStructure.Q13: "Q13",
    MessageStructure.Q15: "Q15",
    MessageStructure.Q21_Q22_Q23_Q24_Q25: "Q21, Q22, Q23,Q24, Q25",
    MessageStructure.Q02: "Q02",
    MessageStructure.J01_J02: "J01, J02",
    MessageStructure.W02: "W02",
    MessageStructure.QRY_A19: "A19",
    MessageStructure.QRY_P04: "P04",
    MessageStructure.PC4_PC9_PCE_PCK: "PC4, PC9, PCE, PCK",
    MessageStructure.Q01_Q26_Q27_Q28_Q29_Q30: "Q01, Q26, Q27, Q28, Q29, Q30",
    MessageStructure.QRY_Q02: "Q02",
    MessageStructure.R02: "R02",
    MessageStructure.QRY_T12: "T12",
    MessageStructure.Q16: "Q16",
    MessageStructure.Q17: "Q17",
    MessageStructure.RAR: "RAR",
    MessageStructure.O17: "O17",
    MessageStructure.I05: "I05",
    MessageStructure.I06: "I06",
    MessageStructure.RDE_O01: "O01",
    MessageStructure.O11_O25: "O11, O25",
    MessageStructure.RDR: "RDR",
    MessageStructure.O13: "O13",
    MessageStructure.K15: "K15",
    MessageStructure.I12_I13_I14_I15: "I12, I13, I14, I15",
    MessageStructure.RER: "RER",
    MessageStructure.RGR: "RGR",
    MessageStructure.O15: "O15",
    MessageStructure.ROR: "ROR",
    MessageStructure.I08_I09_I10_I11: "I08, I09. I10, I11",
    MessageStructure.I01_I04: "I01, I04",
    MessageStructure.I02: "I02",
    MessageStructure.I03: "I03",
    MessageStructure.RQA_I08: "I08, I09, I10, I11",
    MessageStructure.I05_I06: "I05, I06",
    MessageStructure.I01_I02_I03_I07: "I01, I02, I03, I07",
    MessageStructure.I04: "I04",
    MessageStructure.Q09: "Q09",
    MessageStructure.RRA_O02: "O02",
    MessageStructure.O18: "O18",
    MessageStructure.O14: "O14",
    MessageStructure.O12_O26: "O12, O26",
    MessageStructure.O16: "O16",
    MessageStructure.RRI_I12: "I12, I13, I14, I15",
    MessageStructure.K11: "K11",
    MessageStructure.K21: "K21",
    MessageStructure.K22: "K22",
    MessageStructure.K23_K24: "K23, K24",
    MessageStructure.K13: "K13",
    MessageStructure.S12_S13_S14_S15_S16_S17_S18_S19_S20_S21_S22_S23_S24_S26: "S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S26",
    MessageStructure.Q08: "Q08",
    MessageStructure.S25: "S25",
    MessageStructure.SQR_S25: "S25",
    MessageStructure.S01_S02_S03_S04_S05_S06_S07_S08_S09_S10_S11: "S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11",
    MessageStructure.SRR_S01: "S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11",
    MessageStructure.U04: "U04",
    MessageStructure.U03: "U03",
    MessageStructure.P09: "P09",
    MessageStructure.R08: "R08",
    MessageStructure.TBR_R09: "R09",
    MessageStructure.U10_U11: "U10, U11",
    MessageStructure.Q05: "Q05",
    MessageStructure.Q07: "Q07",
    MessageStructure.V01: "V01",
    MessageStructure.V03: "V03",
    MessageStructure.V04: "V04",
    MessageStructure.V02: "V02",
}
