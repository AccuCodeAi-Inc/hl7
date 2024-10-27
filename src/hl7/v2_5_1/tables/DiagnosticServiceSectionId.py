from ...base import HL7Table

"""
HL7 Version: 2.5.1
Diagnostic Service Section ID - 0074
Table Type: HL7
"""


class DiagnosticServiceSectionId(HL7Table):
    """
    Diagnostic Service Section ID - 0074 // HL7 table type
    - AUDIOLOGY
    - BLOOD_GASES
    - BLOOD_BANK
    - CHEMISTRY
    - CYTOPATHOLOGY
    - CAT_SCAN
    - CARDIAC_CATHETERIZATION
    - CARDIAC_ULTRASOUND
    - ELECTROCARDIAC
    - ELECTRONEURO
    - HEMATOLOGY
    - BEDSIDE_ICU_MONITORING
    - IMMUNOLOGY
    - LABORATORY
    - MICROBIOLOGY
    - MYCOBACTERIOLOGY
    - MYCOLOGY
    - NUCLEAR_MAGNETIC_RESONANCE
    - NUCLEAR_MEDICINE_SCAN
    - NURSING_SERVICE_MEASURES
    - OUTSIDE_LAB
    - OCCUPATIONAL_THERAPY
    - OTHER
    - OB_ULTRASOUND
    - PULMONARY_FUNCTION
    - PHARMACY
    - PHYSICIAN
    - PHYSICAL_THERAPY
    - RADIOLOGY
    - RESPIRATORY_CARE
    - RADIATION_THERAPY
    - RADIOLOGY_ULTRASOUND
    - RADIOGRAPH
    - SURGICAL_PATHOLOGY
    - SEROLOGY
    - TOXICOLOGY
    - VIROLOGY
    - VASCULAR_ULTRASOUND
    - CINERADIOGRAPH
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0074
    """

    AUDIOLOGY = "AU"
    """Audiology"""
    BLOOD_GASES = "BG"
    """Blood Gases"""
    BLOOD_BANK = "BLB"
    """Blood Bank"""
    CHEMISTRY = "CH"
    """Chemistry"""
    CYTOPATHOLOGY = "CP"
    """Cytopathology"""
    CAT_SCAN = "CT"
    """CAT Scan"""
    CARDIAC_CATHETERIZATION = "CTH"
    """Cardiac Catheterization"""
    CARDIAC_ULTRASOUND = "CUS"
    """Cardiac Ultrasound"""
    ELECTROCARDIAC = "EC"
    """Electrocardiac (e.g., EKG, EEC, Holter)"""
    ELECTRONEURO = "EN"
    """Electroneuro (EEG, EMG,EP,PSG)"""
    HEMATOLOGY = "HM"
    """Hematology"""
    BEDSIDE_ICU_MONITORING = "ICU"
    """Bedside ICU Monitoring"""
    IMMUNOLOGY = "IMM"
    """Immunology"""
    LABORATORY = "LAB"
    """Laboratory"""
    MICROBIOLOGY = "MB"
    """Microbiology"""
    MYCOBACTERIOLOGY = "MCB"
    """Mycobacteriology"""
    MYCOLOGY = "MYC"
    """Mycology"""
    NUCLEAR_MAGNETIC_RESONANCE = "NMR"
    """Nuclear Magnetic Resonance"""
    NUCLEAR_MEDICINE_SCAN = "NMS"
    """Nuclear Medicine Scan"""
    NURSING_SERVICE_MEASURES = "NRS"
    """Nursing Service Measures"""
    OUTSIDE_LAB = "OSL"
    """Outside Lab"""
    OCCUPATIONAL_THERAPY = "OT"
    """Occupational Therapy"""
    OTHER = "OTH"
    """Other"""
    OB_ULTRASOUND = "OUS"
    """OB Ultrasound"""
    PULMONARY_FUNCTION = "PF"
    """Pulmonary Function"""
    PHARMACY = "PHR"
    """Pharmacy"""
    PHYSICIAN = "PHY"
    """Physician (Hx. Dx, admission note, etc.)"""
    PHYSICAL_THERAPY = "PT"
    """Physical Therapy"""
    RADIOLOGY = "RAD"
    """Radiology"""
    RESPIRATORY_CARE = "RC"
    """Respiratory Care (therapy)"""
    RADIATION_THERAPY = "RT"
    """Radiation Therapy"""
    RADIOLOGY_ULTRASOUND = "RUS"
    """Radiology Ultrasound"""
    RADIOGRAPH = "RX"
    """Radiograph"""
    SURGICAL_PATHOLOGY = "SP"
    """Surgical Pathology"""
    SEROLOGY = "SR"
    """Serology"""
    TOXICOLOGY = "TX"
    """Toxicology"""
    VIROLOGY = "VR"
    """Virology"""
    VASCULAR_ULTRASOUND = "VUS"
    """Vascular Ultrasound"""
    CINERADIOGRAPH = "XRC"
    """Cineradiograph"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DiagnosticServiceSectionId.AUDIOLOGY: "Audiology",
    DiagnosticServiceSectionId.BLOOD_GASES: "Blood Gases",
    DiagnosticServiceSectionId.BLOOD_BANK: "Blood Bank",
    DiagnosticServiceSectionId.CHEMISTRY: "Chemistry",
    DiagnosticServiceSectionId.CYTOPATHOLOGY: "Cytopathology",
    DiagnosticServiceSectionId.CAT_SCAN: "CAT Scan",
    DiagnosticServiceSectionId.CARDIAC_CATHETERIZATION: "Cardiac Catheterization",
    DiagnosticServiceSectionId.CARDIAC_ULTRASOUND: "Cardiac Ultrasound",
    DiagnosticServiceSectionId.ELECTROCARDIAC: "Electrocardiac (e.g., EKG, EEC, Holter)",
    DiagnosticServiceSectionId.ELECTRONEURO: "Electroneuro (EEG, EMG,EP,PSG)",
    DiagnosticServiceSectionId.HEMATOLOGY: "Hematology",
    DiagnosticServiceSectionId.BEDSIDE_ICU_MONITORING: "Bedside ICU Monitoring",
    DiagnosticServiceSectionId.IMMUNOLOGY: "Immunology",
    DiagnosticServiceSectionId.LABORATORY: "Laboratory",
    DiagnosticServiceSectionId.MICROBIOLOGY: "Microbiology",
    DiagnosticServiceSectionId.MYCOBACTERIOLOGY: "Mycobacteriology",
    DiagnosticServiceSectionId.MYCOLOGY: "Mycology",
    DiagnosticServiceSectionId.NUCLEAR_MAGNETIC_RESONANCE: "Nuclear Magnetic Resonance",
    DiagnosticServiceSectionId.NUCLEAR_MEDICINE_SCAN: "Nuclear Medicine Scan",
    DiagnosticServiceSectionId.NURSING_SERVICE_MEASURES: "Nursing Service Measures",
    DiagnosticServiceSectionId.OUTSIDE_LAB: "Outside Lab",
    DiagnosticServiceSectionId.OCCUPATIONAL_THERAPY: "Occupational Therapy",
    DiagnosticServiceSectionId.OTHER: "Other",
    DiagnosticServiceSectionId.OB_ULTRASOUND: "OB Ultrasound",
    DiagnosticServiceSectionId.PULMONARY_FUNCTION: "Pulmonary Function",
    DiagnosticServiceSectionId.PHARMACY: "Pharmacy",
    DiagnosticServiceSectionId.PHYSICIAN: "Physician (Hx. Dx, admission note, etc.)",
    DiagnosticServiceSectionId.PHYSICAL_THERAPY: "Physical Therapy",
    DiagnosticServiceSectionId.RADIOLOGY: "Radiology",
    DiagnosticServiceSectionId.RESPIRATORY_CARE: "Respiratory Care (therapy)",
    DiagnosticServiceSectionId.RADIATION_THERAPY: "Radiation Therapy",
    DiagnosticServiceSectionId.RADIOLOGY_ULTRASOUND: "Radiology Ultrasound",
    DiagnosticServiceSectionId.RADIOGRAPH: "Radiograph",
    DiagnosticServiceSectionId.SURGICAL_PATHOLOGY: "Surgical Pathology",
    DiagnosticServiceSectionId.SEROLOGY: "Serology",
    DiagnosticServiceSectionId.TOXICOLOGY: "Toxicology",
    DiagnosticServiceSectionId.VIROLOGY: "Virology",
    DiagnosticServiceSectionId.VASCULAR_ULTRASOUND: "Vascular Ultrasound",
    DiagnosticServiceSectionId.CINERADIOGRAPH: "Cineradiograph",
}
