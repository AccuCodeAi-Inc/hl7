from __future__ import annotations
from ...base import DataType
from .EI import EI


"""
DataType - EIP
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::EIP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    EIP,
    EI
)

eip = EIP(  # Entity Identifier Pair - Specifies an identifier assigned to an entity by either the placer or the filler system
    placer_assigned_identifier=None,  # EI(...) 
    filler_assigned_identifier=None,  # EI(...) 
)

-----END COMPOSITE_DATA_TYPE::EIP TEMPLATE-----
"""


class EIP(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 855
    _hl7_id = """EIP"""
    _hl7_name = """Entity Identifier Pair"""
    _hl7_description = """Specifies an identifier assigned to an entity by either the placer or the filler system"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EIP"
    _c_length = (427, 427,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_aliases = ("EIP.1", "EIP.2",)
    _c_components = (EI, EI,)
    _c_names = ("Placer Assigned Identifier", "Filler Assigned Identifier",)
    _c_attrs = ("placer_assigned_identifier", "filler_assigned_identifier",)
    # fmt: on

    def __init__(
        self,
        placer_assigned_identifier: EI | tuple[EI, ...] | None = None,  # EIP.1
        filler_assigned_identifier: EI | tuple[EI, ...] | None = None,  # EIP.2
    ):
        """
        Entity Identifier Pair - `EIP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EIP>`_
        Specifies an identifier assigned to an entity by either the placer or the filler system. If both components are populated the identifiers must refer to the same entity.

        :param placer_assigned_identifier: Specifies an identifier assigned to an entity by the placer system (id: EIP.1 | len: 427 | use: O | rpt: 1)
        :param filler_assigned_identifier: Specifies an identifier assigned to an entity by the filler system (id: EIP.2 | len: 427 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.placer_assigned_identifier = placer_assigned_identifier
        self.filler_assigned_identifier = filler_assigned_identifier

    @property  # get EIP.1
    def placer_assigned_identifier(self) -> EI | None:
        """
        id: EIP.1 | len: 427 | use: O | rpt: 1
        ---
        Specifies an identifier assigned to an entity by the placer system.
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EIP.1
        """
        return self._c_data[0][0]

    @placer_assigned_identifier.setter  # set EIP.1
    def placer_assigned_identifier(self, ei: EI | None):
        """
        id: EIP.1 | len: 427 | use: O | rpt: 1
        ---
        Specifies an identifier assigned to an entity by the placer system.
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EIP.1
        """
        self._c_data[0] = (ei,)

    @property  # get EIP.2
    def filler_assigned_identifier(self) -> EI | None:
        """
        id: EIP.2 | len: 427 | use: O | rpt: 1
        ---
        Specifies an identifier assigned to an entity by the filler system.
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EIP.2
        """
        return self._c_data[1][0]

    @filler_assigned_identifier.setter  # set EIP.2
    def filler_assigned_identifier(self, ei: EI | None):
        """
        id: EIP.2 | len: 427 | use: O | rpt: 1
        ---
        Specifies an identifier assigned to an entity by the filler system.
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EIP.2
        """
        self._c_data[1] = (ei,)
