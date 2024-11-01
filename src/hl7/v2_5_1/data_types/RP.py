from __future__ import annotations
from ...base import DataType
from .ID import ID
from .ST import ST
from .HD import HD
from ..tables.TypeOfReferencedData import TypeOfReferencedData
from ..tables.SubtypeOfReferencedData import SubtypeOfReferencedData


"""
DataType - RP
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::RP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RP,
    ID, ST, HD
)

rp = RP(  # Reference Pointer - This data type transmits information about data stored on another system
    pointer=None,  # ST(...) 
    application_id=None,  # HD(...) 
    type_of_data=None,  # ID(...) 
    subtype=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::RP TEMPLATE-----
"""


class RP(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 273
    _hl7_id = """RP"""
    _hl7_name = """Reference Pointer"""
    _hl7_description = """This data type transmits information about data stored on another system"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RP"
    _c_length = (15, 227, 9, 19,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O",)
    _c_aliases = ("RP.1", "RP.2", "RP.3", "RP.4",)
    _c_components = (ST, HD, ID, ID,)
    _c_names = ("Pointer", "Application Id", "Type Of Data", "Subtype",)
    _c_attrs = ("pointer", "application_id", "type_of_data", "subtype",)
    # fmt: on

    def __init__(
        self,
        pointer: ST | None = None,  # RP.1
        application_id: HD | None = None,  # RP.2
        type_of_data: TypeOfReferencedData | ID | None = None,  # RP.3
        subtype: SubtypeOfReferencedData | ID | None = None,  # RP.4
    ):
        """
        Reference Pointer - `RP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RP>`_
        This data type transmits information about data stored on another system. It contains a reference pointer that uniquely identifies the data on the other system, the identity of the other system, and the type of data.

        :param pointer: A unique key assigned by the system that stores the data (id: RP.1 | len: 15 | use: O | rpt: 1)
        :param application_id: A unique designator of the system that stores the data (id: RP.2 | len: 227 | use: O | rpt: 1)
        :param type_of_data: An ID data type that declares the general type of data (id: RP.3 | len: 9 | use: O | rpt: 1)
        :param subtype: An ID data type declaring the format for the data of subcomponent <main type> (id: RP.4 | len: 19 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.pointer = pointer
        self.application_id = application_id
        self.type_of_data = type_of_data
        self.subtype = subtype

    @property  # get RP.1
    def pointer(self) -> ST | None:
        """
        id: RP.1 | len: 15 | use: O | rpt: 1
        ---
        A unique key assigned by the system that stores the data. The key, which is a ST data type, is used to identify and access the data.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RP.1
        """
        return self._c_data[0][0]

    @pointer.setter  # set RP.1
    def pointer(self, st: ST | None):
        """
        id: RP.1 | len: 15 | use: O | rpt: 1
        ---
        A unique key assigned by the system that stores the data. The key, which is a ST data type, is used to identify and access the data.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RP.1
        """
        self._c_data[0] = (st,)

    @property  # get RP.2
    def application_id(self) -> HD | None:
        """
        id: RP.2 | len: 227 | use: O | rpt: 1
        ---
        A unique designator of the system that stores the data. It is a HD data type (See Section 2.A.33, "HD - hierarchic designator"). Application IDs must be unique across a given HL7 implementation.
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RP.2
        """
        return self._c_data[1][0]

    @application_id.setter  # set RP.2
    def application_id(self, hd: HD | None):
        """
        id: RP.2 | len: 227 | use: O | rpt: 1
        ---
        A unique designator of the system that stores the data. It is a HD data type (See Section 2.A.33, "HD - hierarchic designator"). Application IDs must be unique across a given HL7 implementation.
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RP.2
        """
        self._c_data[1] = (hd,)

    @property  # get RP.3
    def type_of_data(self) -> TypeOfReferencedData | None:
        """
        id: RP.3 | len: 9 | use: O | rpt: 1
        ---
        An ID data type that declares the general type of data. Refer to HL7 Table 0191- Type of referenced data for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RP.3
        """
        return self._c_data[2][0]

    @type_of_data.setter  # set RP.3
    def type_of_data(self, type_of_referenced_data: TypeOfReferencedData | None):
        """
        id: RP.3 | len: 9 | use: O | rpt: 1
        ---
        An ID data type that declares the general type of data. Refer to HL7 Table 0191- Type of referenced data for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RP.3
        """
        self._c_data[2] = (type_of_referenced_data,)

    @property  # get RP.4
    def subtype(self) -> SubtypeOfReferencedData | None:
        """
        id: RP.4 | len: 19 | use: O | rpt: 1
        ---
        An ID data type declaring the format for the data of subcomponent <main type>. Refer to HL7 Table 0291 - Subtype of referenced data for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RP.4
        """
        return self._c_data[3][0]

    @subtype.setter  # set RP.4
    def subtype(self, subtype_of_referenced_data: SubtypeOfReferencedData | None):
        """
        id: RP.4 | len: 19 | use: O | rpt: 1
        ---
        An ID data type declaring the format for the data of subcomponent <main type>. Refer to HL7 Table 0291 - Subtype of referenced data for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RP.4
        """
        self._c_data[3] = (subtype_of_referenced_data,)
