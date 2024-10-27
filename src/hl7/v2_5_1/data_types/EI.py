from __future__ import annotations
from ...base import DataType
from .ID import ID
from .ST import ST
from .IS import IS
from ..tables.AssigningAuthority import AssigningAuthority
from ..tables.UniversalIdType import UniversalIdType


"""
DataType - EI
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::EI TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    EI,
    ID, ST, IS
)

ei = EI(  # Entity Identifier - The entity identifier defines a given entity within a specified series of identifiers
    entity_identifier=None,  # ST(...) 
    namespace_id=None,  # IS(...) 
    universal_id=None,  # ST(...) 
    universal_id_type=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::EI TEMPLATE-----
"""


class EI(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 427
    _hl7_id = """EI"""
    _hl7_name = """Entity Identifier"""
    _hl7_description = """The entity identifier defines a given entity within a specified series of identifiers"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EI"
    _c_length = (199, 20, 199, 6,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("O", "O", "C", "C",)
    _c_aliases = ("EI.1", "EI.2", "EI.3", "EI.4",)
    _c_components = (ST, IS, ST, ID,)
    _c_names = ("Entity Identifier", "Namespace Id", "Universal Id", "Universal Id Type",)
    _c_attrs = ("entity_identifier", "namespace_id", "universal_id", "universal_id_type",)
    # fmt: on

    def __init__(
        self,
        entity_identifier: ST | None = None,  # EI.1
        namespace_id: AssigningAuthority | IS | None = None,  # EI.2
        universal_id: ST | None = None,  # EI.3
        universal_id_type: UniversalIdType | ID | None = None,  # EI.4
    ):
        """
        Entity Identifier - `EI <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EI>`_
        The entity identifier defines a given entity within a specified series of identifiers.

        :param entity_identifier: The first component, <entity identifier>, is usually defined to be unique within the series of identifiers created by the <assigning authority>, defined by a hierarchic designator, represented by components 2 through 4 (id: EI.1 | len: 199 | use: O | rpt: 1)
        :param namespace_id: The assigning authority is a unique identifier of the system (or organization or agency or department) that creates the data (id: EI.2 | len: 20 | use: O | rpt: 1)
        :param universal_id:  (id: EI.3 | len: 199 | use: C | rpt: 1)
        :param universal_id_type:  (id: EI.4 | len: 6 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.entity_identifier = entity_identifier
        self.namespace_id = namespace_id
        self.universal_id = universal_id
        self.universal_id_type = universal_id_type

    @property  # get EI.1
    def entity_identifier(self) -> ST | None:
        """
        id: EI.1 | len: 199 | use: O | rpt: 1
        ---
        The first component, <entity identifier>, is usually defined to be unique within the series of identifiers created by the <assigning authority>, defined by a hierarchic designator, represented by components 2 through 4. See Section 2.A.33, "HD - hierarchic designator".
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EI.1
        """
        return self._c_data[0][0]

    @entity_identifier.setter  # set EI.1
    def entity_identifier(self, st: ST | None):
        """
        id: EI.1 | len: 199 | use: O | rpt: 1
        ---
        The first component, <entity identifier>, is usually defined to be unique within the series of identifiers created by the <assigning authority>, defined by a hierarchic designator, represented by components 2 through 4. See Section 2.A.33, "HD - hierarchic designator".
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EI.1
        """
        self._c_data[0] = (st,)

    @property  # get EI.2
    def namespace_id(self) -> AssigningAuthority | None:
        """
        id: EI.2 | len: 20 | use: O | rpt: 1
        ---
        The assigning authority is a unique identifier of the system (or organization or agency or department) that creates the data. Refer to User-defined Table 0363 - Assigning authority for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EI.2
        """
        return self._c_data[1][0]

    @namespace_id.setter  # set EI.2
    def namespace_id(self, assigning_authority: AssigningAuthority | None):
        """
        id: EI.2 | len: 20 | use: O | rpt: 1
        ---
        The assigning authority is a unique identifier of the system (or organization or agency or department) that creates the data. Refer to User-defined Table 0363 - Assigning authority for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EI.2
        """
        self._c_data[1] = (assigning_authority,)

    @property  # get EI.3
    def universal_id(self) -> ST | None:
        """
        id: EI.3 | len: 199 | use: C | rpt: 1
        ---
        None
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EI.3
        """
        return self._c_data[2][0]

    @universal_id.setter  # set EI.3
    def universal_id(self, st: ST | None):
        """
        id: EI.3 | len: 199 | use: C | rpt: 1
        ---
        None
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EI.3
        """
        self._c_data[2] = (st,)

    @property  # get EI.4
    def universal_id_type(self) -> UniversalIdType | None:
        """
        id: EI.4 | len: 6 | use: C | rpt: 1
        ---
        None
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EI.4
        """
        return self._c_data[3][0]

    @universal_id_type.setter  # set EI.4
    def universal_id_type(self, universal_id_type: UniversalIdType | None):
        """
        id: EI.4 | len: 6 | use: C | rpt: 1
        ---
        None
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EI.4
        """
        self._c_data[3] = (universal_id_type,)
