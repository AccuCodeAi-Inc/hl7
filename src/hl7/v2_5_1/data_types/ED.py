from __future__ import annotations
from ...base import DataType
from .ID import ID
from .TX import TX
from .HD import HD
from ..tables.Encoding import Encoding
from ..tables.TypeOfReferencedData import TypeOfReferencedData
from ..tables.SubtypeOfReferencedData import SubtypeOfReferencedData


"""
DataType - ED
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::ED TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ED,
    ID, TX, HD
)

ed = ED(  # Encapsulated Data - This data type transmits encapsulated data from a source system to a destination system
    source_application=None,  # HD(...) 
    type_of_data=id,  # ID(...)  # Required.
    data_subtype=None,  # ID(...) 
    encoding=id,  # ID(...)  # Required.
    data=tx,  # TX(...)  # Required.
)

-----END COMPOSITE_DATA_TYPE::ED TEMPLATE-----
"""


class ED(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 65536
    _hl7_id = """ED"""
    _hl7_name = """Encapsulated Data"""
    _hl7_description = """This data type transmits encapsulated data from a source system to a destination system"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED"
    _c_length = (227, 9, 18, 6, 65536,)
    _c_rpt = (1, 1, 1, 1, 1,)
    _c_usage = ("O", "R", "O", "R", "R",)
    _c_aliases = ("ED.1", "ED.2", "ED.3", "ED.4", "ED.5",)
    _c_components = (HD, ID, ID, ID, TX,)
    _c_names = ("Source Application", "Type Of Data", "Data Subtype", "Encoding", "Data",)
    _c_attrs = ("source_application", "type_of_data", "data_subtype", "encoding", "data",)
    # fmt: on

    def __init__(
        self,
        type_of_data: TypeOfReferencedData | ID,  # ED.2
        encoding: Encoding | ID,  # ED.4
        data: TX,  # ED.5
        source_application: HD | None = None,  # ED.1
        data_subtype: SubtypeOfReferencedData | ID | None = None,  # ED.3
    ):
        """
        Encapsulated Data - `ED <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ED>`_
        This data type transmits encapsulated data from a source system to a destination system. It contains the identity of the source system, the type of data, the encoding method of the data, and the data itself. This data type is similar to the RP (reference pointer) data type of Section 2.A.65, "RP - reference pointer," except that instead of pointing to the data on another system, it contains the data which is to be sent to that system.

        :param source_application: A unique name that identifies the system which was the source of the data (id: ED.1 | len: 227 | use: O | rpt: 1)
        :param type_of_data: Identical to type of data component in the reference pointer (RP) data type (id: ED.2 | len: 9 | use: R | rpt: 1)
        :param data_subtype: Identical to subtype component in the reference pointer (RP) data type (id: ED.3 | len: 18 | use: O | rpt: 1)
        :param encoding: The type of encoding used to represent successive octets of binary data as displayable ASCII characters (id: ED.4 | len: 6 | use: R | rpt: 1)
        :param data: Displayable ASCII characters which constitute the data to be sent from source application to destination application (id: ED.5 | len: 65536 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.source_application = source_application
        self.type_of_data = type_of_data
        self.data_subtype = data_subtype
        self.encoding = encoding
        self.data = data

    @property  # get ED.1
    def source_application(self) -> HD | None:
        """
        id: ED.1 | len: 227 | use: O | rpt: 1
        ---
        A unique name that identifies the system which was the source of the data. Identical format and restrictions as in reference pointer (see Section 2.A.65.2, "Application ID (HD)").
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED.1
        """
        return self._c_data[0][0]

    @source_application.setter  # set ED.1
    def source_application(self, hd: HD | None):
        """
        id: ED.1 | len: 227 | use: O | rpt: 1
        ---
        A unique name that identifies the system which was the source of the data. Identical format and restrictions as in reference pointer (see Section 2.A.65.2, "Application ID (HD)").
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED.1
        """
        self._c_data[0] = (hd,)

    @property  # get ED.2
    def type_of_data(self) -> TypeOfReferencedData:
        """
        id: ED.2 | len: 9 | use: R | rpt: 1
        ---
        Identical to type of data component in the reference pointer (RP) data type. See Section 2.A.65.3, "Type of Data (ID)".
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED.2
        """
        return self._c_data[1][0]

    @type_of_data.setter  # set ED.2
    def type_of_data(self, type_of_referenced_data: TypeOfReferencedData):
        """
        id: ED.2 | len: 9 | use: R | rpt: 1
        ---
        Identical to type of data component in the reference pointer (RP) data type. See Section 2.A.65.3, "Type of Data (ID)".
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED.2
        """
        self._c_data[1] = (type_of_referenced_data,)

    @property  # get ED.3
    def data_subtype(self) -> SubtypeOfReferencedData | None:
        """
        id: ED.3 | len: 18 | use: O | rpt: 1
        ---
        Identical to subtype component in the reference pointer (RP) data type. See Section 2.A.65.4, "Subtype (ID)".
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED.3
        """
        return self._c_data[2][0]

    @data_subtype.setter  # set ED.3
    def data_subtype(self, subtype_of_referenced_data: SubtypeOfReferencedData | None):
        """
        id: ED.3 | len: 18 | use: O | rpt: 1
        ---
        Identical to subtype component in the reference pointer (RP) data type. See Section 2.A.65.4, "Subtype (ID)".
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED.3
        """
        self._c_data[2] = (subtype_of_referenced_data,)

    @property  # get ED.4
    def encoding(self) -> Encoding:
        """
        id: ED.4 | len: 6 | use: R | rpt: 1
        ---
        The type of encoding used to represent successive octets of binary data as displayable ASCII characters. Refer to HL7 Table 0299 - Encoding for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED.4
        """
        return self._c_data[3][0]

    @encoding.setter  # set ED.4
    def encoding(self, encoding: Encoding):
        """
        id: ED.4 | len: 6 | use: R | rpt: 1
        ---
        The type of encoding used to represent successive octets of binary data as displayable ASCII characters. Refer to HL7 Table 0299 - Encoding for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED.4
        """
        self._c_data[3] = (encoding,)

    @property  # get ED.5
    def data(self) -> TX:
        """
        id: ED.5 | len: 65536 | use: R | rpt: 1
        ---
        Displayable ASCII characters which constitute the data to be sent from source application to destination application. The characters are limited to the legal characters of the ST data type, as defined in Section 2.A.74, " ST - string data ," and, if encoded binary, are encoded according to the method of Section 2.A.24.2, "Type of Data (ID)".
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED.5
        """
        return self._c_data[4][0]

    @data.setter  # set ED.5
    def data(self, tx: TX):
        """
        id: ED.5 | len: 65536 | use: R | rpt: 1
        ---
        Displayable ASCII characters which constitute the data to be sent from source application to destination application. The characters are limited to the legal characters of the ST data type, as defined in Section 2.A.74, " ST - string data ," and, if encoded binary, are encoded according to the method of Section 2.A.24.2, "Type of Data (ID)".
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ED.5
        """
        self._c_data[4] = (tx,)
