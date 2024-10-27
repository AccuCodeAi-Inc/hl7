from ...base import HL7Table

"""
HL7 Version: 2.5.1
Modality - 0259
Table Type: User
"""


class Modality(HL7Table):
    """
    Modality - 0259 // User table type
    - ANGIOSCOPY
    - BIOMAGNETIC_IMAGING
    - COLOR_FLOW_DOPPLER
    - COLPOSCOPY
    - COMPUTED_RADIOGRAPHY
    - CYSTOSCOPY
    - COMPUTED_TOMOGRAPHY
    - DUPLEX_DOPPLER
    - DIAPANOGRAPHY
    - DIGITAL_MICROSCOPY
    - ECHOCARDIOGRAPHY
    - ENDOSCOPY
    - FLUORESCEIN_ANGIOGRAPHY
    - FUNDOSCOPY
    - LAPAROSCOPY
    - LASER_SURFACE_SCAN
    - MAGNETIC_RESONANCE_ANGIOGRAPHY
    - MAGNETIC_RESONANCE_SPECTROSCOPY
    - NUCLEAR_MEDICINE
    - OTHER
    - POSITRON_EMISSION_TOMOGRAPHY
    - RADIO_FLUOROSCOPY
    - SINGLE_PHOTON_EMISSION_COMPUTED_TOMOGRAPHY
    - THERMOGRAPHY
    - ULTRASOUND
    - X_RAY_ANGIOGRAPHY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0259
    """

    ANGIOSCOPY = "AS"
    """Angioscopy"""
    BIOMAGNETIC_IMAGING = "BS"
    """Biomagnetic imaging"""
    COLOR_FLOW_DOPPLER = "CD"
    """Color flow Doppler"""
    COLPOSCOPY = "CP"
    """Colposcopy"""
    COMPUTED_RADIOGRAPHY = "CR"
    """Computed radiography"""
    CYSTOSCOPY = "CS"
    """Cystoscopy"""
    COMPUTED_TOMOGRAPHY = "CT"
    """Computed tomography"""
    DUPLEX_DOPPLER = "DD"
    """Duplex Doppler"""
    DIAPANOGRAPHY = "DG"
    """Diapanography"""
    DIGITAL_MICROSCOPY = "DM"
    """Digital microscopy"""
    ECHOCARDIOGRAPHY = "EC"
    """Echocardiography"""
    ENDOSCOPY = "ES"
    """Endoscopy"""
    FLUORESCEIN_ANGIOGRAPHY = "FA"
    """Fluorescein angiography"""
    FUNDOSCOPY = "FS"
    """Fundoscopy"""
    LAPAROSCOPY = "LP"
    """Laparoscopy"""
    LASER_SURFACE_SCAN = "LS"
    """Laser surface scan"""
    MAGNETIC_RESONANCE_ANGIOGRAPHY = "MA"
    """Magnetic resonance angiography"""
    MAGNETIC_RESONANCE_SPECTROSCOPY = "MS"
    """Magnetic resonance spectroscopy"""
    NUCLEAR_MEDICINE = "NM"
    """Nuclear Medicine (radioisotope study)"""
    OTHER = "OT"
    """Other"""
    POSITRON_EMISSION_TOMOGRAPHY = "PT"
    """Positron emission tomography (PET)"""
    RADIO_FLUOROSCOPY = "RF"
    """Radio fluoroscopy"""
    SINGLE_PHOTON_EMISSION_COMPUTED_TOMOGRAPHY = "ST"
    """Single photon emission computed tomography (SPECT)"""
    THERMOGRAPHY = "TG"
    """Thermography"""
    ULTRASOUND = "US"
    """Ultrasound"""
    X_RAY_ANGIOGRAPHY = "XA"
    """X-ray Angiography"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Modality.ANGIOSCOPY: "Angioscopy",
    Modality.BIOMAGNETIC_IMAGING: "Biomagnetic imaging",
    Modality.COLOR_FLOW_DOPPLER: "Color flow Doppler",
    Modality.COLPOSCOPY: "Colposcopy",
    Modality.COMPUTED_RADIOGRAPHY: "Computed radiography",
    Modality.CYSTOSCOPY: "Cystoscopy",
    Modality.COMPUTED_TOMOGRAPHY: "Computed tomography",
    Modality.DUPLEX_DOPPLER: "Duplex Doppler",
    Modality.DIAPANOGRAPHY: "Diapanography",
    Modality.DIGITAL_MICROSCOPY: "Digital microscopy",
    Modality.ECHOCARDIOGRAPHY: "Echocardiography",
    Modality.ENDOSCOPY: "Endoscopy",
    Modality.FLUORESCEIN_ANGIOGRAPHY: "Fluorescein angiography",
    Modality.FUNDOSCOPY: "Fundoscopy",
    Modality.LAPAROSCOPY: "Laparoscopy",
    Modality.LASER_SURFACE_SCAN: "Laser surface scan",
    Modality.MAGNETIC_RESONANCE_ANGIOGRAPHY: "Magnetic resonance angiography",
    Modality.MAGNETIC_RESONANCE_SPECTROSCOPY: "Magnetic resonance spectroscopy",
    Modality.NUCLEAR_MEDICINE: "Nuclear Medicine (radioisotope study)",
    Modality.OTHER: "Other",
    Modality.POSITRON_EMISSION_TOMOGRAPHY: "Positron emission tomography (PET)",
    Modality.RADIO_FLUOROSCOPY: "Radio fluoroscopy",
    Modality.SINGLE_PHOTON_EMISSION_COMPUTED_TOMOGRAPHY: "Single photon emission computed tomography (SPECT)",
    Modality.THERMOGRAPHY: "Thermography",
    Modality.ULTRASOUND: "Ultrasound",
    Modality.X_RAY_ANGIOGRAPHY: "X-ray Angiography",
}
