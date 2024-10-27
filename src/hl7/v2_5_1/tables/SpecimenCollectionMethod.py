from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen Collection Method - 0488
Table Type: HL7
"""


class SpecimenCollectionMethod(HL7Table):
    """
    Specimen Collection Method - 0488 // HL7 table type
    - PLATES_ANAEROBIC
    - PLATES_BLOOD_AGAR
    - BLOOD_CULTURE_AEROBIC_BOTTLE
    - BLOOD_CULTURE_ANAEROBIC_BOTTLE
    - BLOOD_CULTURE_PEDIATRIC_BOTTLE
    - BIOPSY
    - CAPILLARY_SPECIMEN
    - CATHETERIZED
    - LINE_CVP
    - ENVIRONMENTAL_PLATE
    - ENVIRONMENTAL_SWAB
    - ASPIRATION_FINE_NEEDLE
    - PLATE_COUGH
    - LINE_ARTERIAL
    - LINE_VENOUS
    - MARTIN_LEWIS_AGAR
    - MOD_MARTIN_LEWIS_AGAR
    - PLATE_MARTIN_LEWIS
    - PLATE_NEW_YORK_CITY
    - PACE_GEN_PROBE
    - PINWORM_PREP
    - ATERIAL_PUNCTURE
    - PUMP_PRIME
    - PUMP_SPECIMEN
    - QUALITY_CONTROL_FOR_MICRO
    - SCALP_FETAL_VEIN
    - SCRAPINGS
    - SHAVING
    - SWAB
    - SWAB_DACRON_TIPPED
    - TRANSPORT_MEDIA_ANAEROBIC
    - TRANSPORT_MEDIA_CHALAMYDIA
    - TRANSPORT_MEDIA_M4
    - TRANSPORT_MEDIA_MYCOPLASMA
    - TRANSPORT_MEDIA
    - PLATE_THAYER_MARTIN
    - TRANSPORT_MEDIA_PVA
    - TRANSPORT_MEDIA_STOOL_CULTURE
    - TRANSPORT_MEDIA_UREAPLASMA
    - TRANSPORT_MEDIA_VIRAL
    - VENIPUNCTURE
    - SWAB_WOODEN_SHAFT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0488
    """

    PLATES_ANAEROBIC = "ANP"
    """Plates, Anaerobic"""
    PLATES_BLOOD_AGAR = "BAP"
    """Plates, Blood Agar"""
    BLOOD_CULTURE_AEROBIC_BOTTLE = "BCAE"
    """Blood Culture, Aerobic Bottle"""
    BLOOD_CULTURE_ANAEROBIC_BOTTLE = "BCAN"
    """Blood Culture, Anaerobic Bottle"""
    BLOOD_CULTURE_PEDIATRIC_BOTTLE = "BCPD"
    """Blood Culture, Pediatric Bottle"""
    BIOPSY = "BIO"
    """Biopsy"""
    CAPILLARY_SPECIMEN = "CAP"
    """Capillary Specimen"""
    CATHETERIZED = "CATH"
    """Catheterized"""
    LINE_CVP = "CVP"
    """Line, CVP"""
    ENVIRONMENTAL_PLATE = "EPLA"
    """Environmental, Plate"""
    ENVIRONMENTAL_SWAB = "ESWA"
    """Environmental, Swab"""
    ASPIRATION_FINE_NEEDLE = "FNA"
    """Aspiration, Fine Needle"""
    PLATE_COUGH = "KOFFP"
    """Plate, Cough"""
    LINE_ARTERIAL = "LNA"
    """Line, Arterial"""
    LINE_VENOUS = "LNV"
    """Line, Venous"""
    MARTIN_LEWIS_AGAR = "MARTL"
    """Martin-Lewis Agar"""
    MOD_MARTIN_LEWIS_AGAR = "ML11"
    """Mod. Martin-Lewis Agar"""
    PLATE_MARTIN_LEWIS = "MLP"
    """Plate, Martin-Lewis"""
    PLATE_NEW_YORK_CITY = "NYP"
    """Plate, New York City"""
    PACE_GEN_PROBE = "PACE"
    """Pace, Gen-Probe"""
    PINWORM_PREP = "PIN"
    """Pinworm Prep"""
    ATERIAL_PUNCTURE = "PNA"
    """Aterial puncture"""
    PUMP_PRIME = "PRIME"
    """Pump Prime"""
    PUMP_SPECIMEN = "PUMP"
    """Pump Specimen"""
    QUALITY_CONTROL_FOR_MICRO = "QC5"
    """Quality Control For Micro"""
    SCALP_FETAL_VEIN = "SCLP"
    """Scalp, Fetal Vein"""
    SCRAPINGS = "SCRAPS"
    """Scrapings"""
    SHAVING = "SHA"
    """Shaving"""
    SWAB = "SWA"
    """Swab"""
    SWAB_DACRON_TIPPED = "SWD"
    """Swab, Dacron tipped"""
    TRANSPORT_MEDIA_ANAEROBIC = "TMAN"
    """Transport Media, Anaerobic"""
    TRANSPORT_MEDIA_CHALAMYDIA = "TMCH"
    """Transport Media, Chalamydia"""
    TRANSPORT_MEDIA_M4 = "TMM4"
    """Transport Media, M4"""
    TRANSPORT_MEDIA_MYCOPLASMA = "TMMY"
    """Transport Media, Mycoplasma"""
    TRANSPORT_MEDIA = "TMOT"
    """Transport Media,"""
    PLATE_THAYER_MARTIN = "TMP"
    """Plate, Thayer-Martin"""
    TRANSPORT_MEDIA_PVA = "TMPV"
    """Transport Media, PVA"""
    TRANSPORT_MEDIA_STOOL_CULTURE = "TMSC"
    """Transport Media, Stool Culture"""
    TRANSPORT_MEDIA_UREAPLASMA = "TMUP"
    """Transport Media, Ureaplasma"""
    TRANSPORT_MEDIA_VIRAL = "TMVI"
    """Transport Media, Viral"""
    VENIPUNCTURE = "VENIP"
    """Venipuncture"""
    SWAB_WOODEN_SHAFT = "WOOD"
    """Swab, Wooden Shaft"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenCollectionMethod.PLATES_ANAEROBIC: "Plates, Anaerobic",
    SpecimenCollectionMethod.PLATES_BLOOD_AGAR: "Plates, Blood Agar",
    SpecimenCollectionMethod.BLOOD_CULTURE_AEROBIC_BOTTLE: "Blood Culture, Aerobic Bottle",
    SpecimenCollectionMethod.BLOOD_CULTURE_ANAEROBIC_BOTTLE: "Blood Culture, Anaerobic Bottle",
    SpecimenCollectionMethod.BLOOD_CULTURE_PEDIATRIC_BOTTLE: "Blood Culture, Pediatric Bottle",
    SpecimenCollectionMethod.BIOPSY: "Biopsy",
    SpecimenCollectionMethod.CAPILLARY_SPECIMEN: "Capillary Specimen",
    SpecimenCollectionMethod.CATHETERIZED: "Catheterized",
    SpecimenCollectionMethod.LINE_CVP: "Line, CVP",
    SpecimenCollectionMethod.ENVIRONMENTAL_PLATE: "Environmental, Plate",
    SpecimenCollectionMethod.ENVIRONMENTAL_SWAB: "Environmental, Swab",
    SpecimenCollectionMethod.ASPIRATION_FINE_NEEDLE: "Aspiration, Fine Needle",
    SpecimenCollectionMethod.PLATE_COUGH: "Plate, Cough",
    SpecimenCollectionMethod.LINE_ARTERIAL: "Line, Arterial",
    SpecimenCollectionMethod.LINE_VENOUS: "Line, Venous",
    SpecimenCollectionMethod.MARTIN_LEWIS_AGAR: "Martin-Lewis Agar",
    SpecimenCollectionMethod.MOD_MARTIN_LEWIS_AGAR: "Mod. Martin-Lewis Agar",
    SpecimenCollectionMethod.PLATE_MARTIN_LEWIS: "Plate, Martin-Lewis",
    SpecimenCollectionMethod.PLATE_NEW_YORK_CITY: "Plate, New York City",
    SpecimenCollectionMethod.PACE_GEN_PROBE: "Pace, Gen-Probe",
    SpecimenCollectionMethod.PINWORM_PREP: "Pinworm Prep",
    SpecimenCollectionMethod.ATERIAL_PUNCTURE: "Aterial puncture",
    SpecimenCollectionMethod.PUMP_PRIME: "Pump Prime",
    SpecimenCollectionMethod.PUMP_SPECIMEN: "Pump Specimen",
    SpecimenCollectionMethod.QUALITY_CONTROL_FOR_MICRO: "Quality Control For Micro",
    SpecimenCollectionMethod.SCALP_FETAL_VEIN: "Scalp, Fetal Vein",
    SpecimenCollectionMethod.SCRAPINGS: "Scrapings",
    SpecimenCollectionMethod.SHAVING: "Shaving",
    SpecimenCollectionMethod.SWAB: "Swab",
    SpecimenCollectionMethod.SWAB_DACRON_TIPPED: "Swab, Dacron tipped",
    SpecimenCollectionMethod.TRANSPORT_MEDIA_ANAEROBIC: "Transport Media, Anaerobic",
    SpecimenCollectionMethod.TRANSPORT_MEDIA_CHALAMYDIA: "Transport Media, Chalamydia",
    SpecimenCollectionMethod.TRANSPORT_MEDIA_M4: "Transport Media, M4",
    SpecimenCollectionMethod.TRANSPORT_MEDIA_MYCOPLASMA: "Transport Media, Mycoplasma",
    SpecimenCollectionMethod.TRANSPORT_MEDIA: "Transport Media,",
    SpecimenCollectionMethod.PLATE_THAYER_MARTIN: "Plate, Thayer-Martin",
    SpecimenCollectionMethod.TRANSPORT_MEDIA_PVA: "Transport Media, PVA",
    SpecimenCollectionMethod.TRANSPORT_MEDIA_STOOL_CULTURE: "Transport Media, Stool Culture",
    SpecimenCollectionMethod.TRANSPORT_MEDIA_UREAPLASMA: "Transport Media, Ureaplasma",
    SpecimenCollectionMethod.TRANSPORT_MEDIA_VIRAL: "Transport Media, Viral",
    SpecimenCollectionMethod.VENIPUNCTURE: "Venipuncture",
    SpecimenCollectionMethod.SWAB_WOODEN_SHAFT: "Swab, Wooden Shaft",
}
