from ...base import HL7Table

"""
HL7 Version: 2.5.1
Type of referenced data - 0191
Table Type: HL7
"""


class TypeOfReferencedData(HL7Table):
    """
    Type of referenced data - 0191 // HL7 table type
    - OTHER_APPLICATION_DATA_TYPICALLY_UNINTERPRETED_BINARY_DATA
    - AUDIO_DATA
    - FORMATTED_TEXT
    - IMAGE_DATA
    - MIME_MULTIPART_PACKAGE
    - NON_SCANNED_IMAGE
    - SCANNED_DOCUMENT
    - SCANNED_IMAGE
    - MACHINE_READABLE_TEXT_DOCUMENT
    - TX
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0191
    """

    OTHER_APPLICATION_DATA_TYPICALLY_UNINTERPRETED_BINARY_DATA = "AP"
    """Other application data, typically uninterpreted binary data (HL7 V2.3 and later)"""
    AUDIO_DATA = "AU"
    """Audio data (HL7 V2.3 and later)"""
    FORMATTED_TEXT = "FT"
    """Formatted text (HL7 V2.2 only)"""
    IMAGE_DATA = "IM"
    """Image data (HL7 V2.3 and later)"""
    MIME_MULTIPART_PACKAGE = "multipart"
    """MIME multipart package"""
    NON_SCANNED_IMAGE = "NS"
    """Non-scanned image (HL7 V2.2 only)"""
    SCANNED_DOCUMENT = "SD"
    """Scanned document (HL7 V2.2 only)"""
    SCANNED_IMAGE = "SI"
    """Scanned image (HL7 V2.2 only)"""
    MACHINE_READABLE_TEXT_DOCUMENT = "TEXT"
    """Machine readable text document (HL7 V2.3.1 and later)"""
    TX = "TX"
    """Machine readable text document (HL7 V2.2 only)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TypeOfReferencedData.OTHER_APPLICATION_DATA_TYPICALLY_UNINTERPRETED_BINARY_DATA: "Other application data, typically uninterpreted binary data (HL7 V2.3 and later)",
    TypeOfReferencedData.AUDIO_DATA: "Audio data (HL7 V2.3 and later)",
    TypeOfReferencedData.FORMATTED_TEXT: "Formatted text (HL7 V2.2 only)",
    TypeOfReferencedData.IMAGE_DATA: "Image data (HL7 V2.3 and later)",
    TypeOfReferencedData.MIME_MULTIPART_PACKAGE: "MIME multipart package",
    TypeOfReferencedData.NON_SCANNED_IMAGE: "Non-scanned image (HL7 V2.2 only)",
    TypeOfReferencedData.SCANNED_DOCUMENT: "Scanned document (HL7 V2.2 only)",
    TypeOfReferencedData.SCANNED_IMAGE: "Scanned image (HL7 V2.2 only)",
    TypeOfReferencedData.MACHINE_READABLE_TEXT_DOCUMENT: "Machine readable text document (HL7 V2.3.1 and later)",
    TypeOfReferencedData.TX: "Machine readable text document (HL7 V2.2 only)",
}
