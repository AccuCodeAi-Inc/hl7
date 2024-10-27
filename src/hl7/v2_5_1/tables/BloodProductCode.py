from ...base import HL7Table

"""
HL7 Version: 2.5.1
Blood Product Code - 0426
Table Type: User
"""


class BloodProductCode(HL7Table):
    """
    Blood Product Code - 0426 // User table type
    - CRYOPRECIPITATED_AHF
    - POOLED_CRYOPRECIPITATE
    - FRESH_FROZEN_PLASMA
    - FRESH_FROZEN_PLASMA_THAWED
    - PACKED_CELLS
    - AUTOLOGOUS_PACKED_CELLS
    - PACKED_CELLS_NEONATAL
    - WASHED_PACKED_CELLS
    - PLATELET_CONCENTRATE
    - REDUCED_VOLUME_PLATELETS
    - POOLED_PLATELETS
    - PLATELET_PHERESIS
    - LEUKOREDUCED_PLATELET_PHERESIS
    - RECONSTITUTED_WHOLE_BLOOD
    - AUTOLOGOUS_WHOLE_BLOOD
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0426
    """

    CRYOPRECIPITATED_AHF = "CRYO"
    """Cryoprecipitated AHF"""
    POOLED_CRYOPRECIPITATE = "CRYOP"
    """Pooled Cryoprecipitate"""
    FRESH_FROZEN_PLASMA = "FFP"
    """Fresh Frozen Plasma"""
    FRESH_FROZEN_PLASMA_THAWED = "FFPTH"
    """Fresh Frozen Plasma - Thawed"""
    PACKED_CELLS = "PC"
    """Packed Cells"""
    AUTOLOGOUS_PACKED_CELLS = "PCA"
    """Autologous Packed Cells"""
    PACKED_CELLS_NEONATAL = "PCNEO"
    """Packed Cells - Neonatal"""
    WASHED_PACKED_CELLS = "PCW"
    """Washed Packed Cells"""
    PLATELET_CONCENTRATE = "PLT"
    """Platelet Concentrate"""
    REDUCED_VOLUME_PLATELETS = "PLTNEO"
    """Reduced Volume Platelets"""
    POOLED_PLATELETS = "PLTP"
    """Pooled Platelets"""
    PLATELET_PHERESIS = "PLTPH"
    """Platelet Pheresis"""
    LEUKOREDUCED_PLATELET_PHERESIS = "PLTPHLR"
    """Leukoreduced Platelet Pheresis"""
    RECONSTITUTED_WHOLE_BLOOD = "RWB"
    """Reconstituted Whole Blood"""
    AUTOLOGOUS_WHOLE_BLOOD = "WBA"
    """Autologous Whole Blood"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    BloodProductCode.CRYOPRECIPITATED_AHF: "Cryoprecipitated AHF",
    BloodProductCode.POOLED_CRYOPRECIPITATE: "Pooled Cryoprecipitate",
    BloodProductCode.FRESH_FROZEN_PLASMA: "Fresh Frozen Plasma",
    BloodProductCode.FRESH_FROZEN_PLASMA_THAWED: "Fresh Frozen Plasma - Thawed",
    BloodProductCode.PACKED_CELLS: "Packed Cells",
    BloodProductCode.AUTOLOGOUS_PACKED_CELLS: "Autologous Packed Cells",
    BloodProductCode.PACKED_CELLS_NEONATAL: "Packed Cells - Neonatal",
    BloodProductCode.WASHED_PACKED_CELLS: "Washed Packed Cells",
    BloodProductCode.PLATELET_CONCENTRATE: "Platelet Concentrate",
    BloodProductCode.REDUCED_VOLUME_PLATELETS: "Reduced Volume Platelets",
    BloodProductCode.POOLED_PLATELETS: "Pooled Platelets",
    BloodProductCode.PLATELET_PHERESIS: "Platelet Pheresis",
    BloodProductCode.LEUKOREDUCED_PLATELET_PHERESIS: "Leukoreduced Platelet Pheresis",
    BloodProductCode.RECONSTITUTED_WHOLE_BLOOD: "Reconstituted Whole Blood",
    BloodProductCode.AUTOLOGOUS_WHOLE_BLOOD: "Autologous Whole Blood",
}
