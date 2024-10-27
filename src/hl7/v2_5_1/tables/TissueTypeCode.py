from ...base import HL7Table

"""
HL7 Version: 2.5.1
Tissue Type Code - 0417
Table Type: User
"""


class TissueTypeCode(HL7Table):
    """
    Tissue Type Code - 0417 // User table type
    - NO_TISSUE_EXPECTED
    - INSUFFICIENT_TISSUE
    - NOT_ABNORMAL
    - ABNORMAL_NOT_CATEGORIZED
    - MECHANICAL_ABNORMAL
    - GROWTH_ALTERATION
    - DEGENERATION_AND_NECROSIS
    - NON_ACUTE_INFLAMMATION
    - NON_MALIGNANT_NEOPLASM
    - MALIGNANT_NEOPLASM
    - BASAL_CELL_CARCINOMA
    - CARCINOMA_UNSPECIFIED_TYPE
    - ADDITIONAL_TISSUE_REQUIRED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0417
    """

    NO_TISSUE_EXPECTED = "0"
    """No tissue expected"""
    INSUFFICIENT_TISSUE = "1"
    """Insufficient Tissue"""
    NOT_ABNORMAL = "2"
    """Not abnormal"""
    ABNORMAL_NOT_CATEGORIZED = "3"
    """Abnormal-not categorized"""
    MECHANICAL_ABNORMAL = "4"
    """Mechanical abnormal"""
    GROWTH_ALTERATION = "5"
    """Growth alteration"""
    DEGENERATION_AND_NECROSIS = "6"
    """Degeneration &amp; necrosis"""
    NON_ACUTE_INFLAMMATION = "7"
    """Non-acute inflammation"""
    NON_MALIGNANT_NEOPLASM = "8"
    """Non-malignant neoplasm"""
    MALIGNANT_NEOPLASM = "9"
    """Malignant neoplasm"""
    BASAL_CELL_CARCINOMA = "B"
    """Basal cell carcinoma"""
    CARCINOMA_UNSPECIFIED_TYPE = "C"
    """Carcinoma-unspecified type"""
    ADDITIONAL_TISSUE_REQUIRED = "G"
    """Additional tissue required"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TissueTypeCode.NO_TISSUE_EXPECTED: "No tissue expected",
    TissueTypeCode.INSUFFICIENT_TISSUE: "Insufficient Tissue",
    TissueTypeCode.NOT_ABNORMAL: "Not abnormal",
    TissueTypeCode.ABNORMAL_NOT_CATEGORIZED: "Abnormal-not categorized",
    TissueTypeCode.MECHANICAL_ABNORMAL: "Mechanical abnormal",
    TissueTypeCode.GROWTH_ALTERATION: "Growth alteration",
    TissueTypeCode.DEGENERATION_AND_NECROSIS: "Degeneration &amp; necrosis",
    TissueTypeCode.NON_ACUTE_INFLAMMATION: "Non-acute inflammation",
    TissueTypeCode.NON_MALIGNANT_NEOPLASM: "Non-malignant neoplasm",
    TissueTypeCode.MALIGNANT_NEOPLASM: "Malignant neoplasm",
    TissueTypeCode.BASAL_CELL_CARCINOMA: "Basal cell carcinoma",
    TissueTypeCode.CARCINOMA_UNSPECIFIED_TYPE: "Carcinoma-unspecified type",
    TissueTypeCode.ADDITIONAL_TISSUE_REQUIRED: "Additional tissue required",
}
