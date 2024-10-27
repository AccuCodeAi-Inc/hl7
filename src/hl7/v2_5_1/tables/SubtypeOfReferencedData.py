from ...base import HL7Table

"""
HL7 Version: 2.5.1
Subtype of referenced data - 0291
Table Type: HL7
"""


class SubtypeOfReferencedData(HL7Table):
    """
    Subtype of referenced data - 0291 // HL7 table type
    - ISDN_PCM_AUDIO_DATA
    - DIGITAL_IMAGING_AND_COMMUNICATIONS_IN_MEDICINE
    - FACSIMILE_DATA
    - GRAPHICS_INTERCHANGE_FORMAT
    - HYPERTEXT_MARKUP_LANGUAGE
    - ELECTRONIC_INK_DATA
    - JOINT_PHOTOGRAPHIC_EXPERTS_GROUP
    - UNINTERPRETED_BINARY_DATA
    - PICT_FORMAT_IMAGE_DATA
    - POSTSCRIPT_PROGRAM
    - RICH_TEXT_FORMAT
    - STANDARD_GENERALIZED_MARKUP_LANGUAGE
    - TIFF_IMAGE_DATA
    - HL7_CLINICAL_DOCUMENT_ARCHITECTURE_LEVEL_ONE_DOCUMENT
    - EXTENSIBLE_MARKUP_LANGUAGE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0291
    """

    ISDN_PCM_AUDIO_DATA = "BASIC"
    """ISDN PCM audio data"""
    DIGITAL_IMAGING_AND_COMMUNICATIONS_IN_MEDICINE = "DICOM"
    """Digital Imaging and Communications in Medicine"""
    FACSIMILE_DATA = "FAX"
    """Facsimile data"""
    GRAPHICS_INTERCHANGE_FORMAT = "GIF"
    """Graphics Interchange Format"""
    HYPERTEXT_MARKUP_LANGUAGE = "HTML"
    """Hypertext Markup Language"""
    ELECTRONIC_INK_DATA = "JOT"
    """Electronic ink data (Jot 1.0 standard)"""
    JOINT_PHOTOGRAPHIC_EXPERTS_GROUP = "JPEG"
    """Joint Photographic Experts Group"""
    UNINTERPRETED_BINARY_DATA = "Octet-stream"
    """Uninterpreted binary data"""
    PICT_FORMAT_IMAGE_DATA = "PICT"
    """PICT format image data"""
    POSTSCRIPT_PROGRAM = "PostScript"
    """PostScript program"""
    RICH_TEXT_FORMAT = "RTF"
    """Rich Text Format"""
    STANDARD_GENERALIZED_MARKUP_LANGUAGE = "SGML"
    """Standard Generalized Markup Language (HL7 V2.3.1 and later)"""
    TIFF_IMAGE_DATA = "TIFF"
    """TIFF image data"""
    HL7_CLINICAL_DOCUMENT_ARCHITECTURE_LEVEL_ONE_DOCUMENT = "x-hl7-cda-level-one"
    """HL7 Clinical Document Architecture Level One document"""
    EXTENSIBLE_MARKUP_LANGUAGE = "XML"
    """Extensible Markup Language (HL7 V2.3.1 and later)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SubtypeOfReferencedData.ISDN_PCM_AUDIO_DATA: "ISDN PCM audio data",
    SubtypeOfReferencedData.DIGITAL_IMAGING_AND_COMMUNICATIONS_IN_MEDICINE: "Digital Imaging and Communications in Medicine",
    SubtypeOfReferencedData.FACSIMILE_DATA: "Facsimile data",
    SubtypeOfReferencedData.GRAPHICS_INTERCHANGE_FORMAT: "Graphics Interchange Format",
    SubtypeOfReferencedData.HYPERTEXT_MARKUP_LANGUAGE: "Hypertext Markup Language",
    SubtypeOfReferencedData.ELECTRONIC_INK_DATA: "Electronic ink data (Jot 1.0 standard)",
    SubtypeOfReferencedData.JOINT_PHOTOGRAPHIC_EXPERTS_GROUP: "Joint Photographic Experts Group",
    SubtypeOfReferencedData.UNINTERPRETED_BINARY_DATA: "Uninterpreted binary data",
    SubtypeOfReferencedData.PICT_FORMAT_IMAGE_DATA: "PICT format image data",
    SubtypeOfReferencedData.POSTSCRIPT_PROGRAM: "PostScript program",
    SubtypeOfReferencedData.RICH_TEXT_FORMAT: "Rich Text Format",
    SubtypeOfReferencedData.STANDARD_GENERALIZED_MARKUP_LANGUAGE: "Standard Generalized Markup Language (HL7 V2.3.1 and later)",
    SubtypeOfReferencedData.TIFF_IMAGE_DATA: "TIFF image data",
    SubtypeOfReferencedData.HL7_CLINICAL_DOCUMENT_ARCHITECTURE_LEVEL_ONE_DOCUMENT: "HL7 Clinical Document Architecture Level One document",
    SubtypeOfReferencedData.EXTENSIBLE_MARKUP_LANGUAGE: "Extensible Markup Language (HL7 V2.3.1 and later)",
}
