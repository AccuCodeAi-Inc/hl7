from __future__ import annotations
from ...base import DataType
from .ST import ST
from .ID import ID
from .FT import FT
from ..tables.CodingSystem import CodingSystem


"""
DataType - CF
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CF TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CF,
    ST, ID, FT
)

cf = CF(  # Coded Element with Formatted Values - This data type transmits codes and the formatted text associated with the code
    identifier=None,  # ST(...) 
    formatted_text=None,  # FT(...) 
    name_of_coding_system=None,  # ID(...) 
    alternate_identifier=None,  # ST(...) 
    alternate_formatted_text=None,  # FT(...) 
    name_of_alternate_coding_system=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::CF TEMPLATE-----
"""


class CF(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 65536
    _hl7_id = """CF"""
    _hl7_name = """Coded Element with Formatted Values"""
    _hl7_description = """This data type transmits codes and the formatted text associated with the code"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF"
    _c_length = (20, 65536, 20, 20, 65536, 20,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O",)
    _c_aliases = ("CF.1", "CF.2", "CF.3", "CF.4", "CF.5", "CF.6",)
    _c_components = (ST, FT, ID, ST, FT, ID,)
    _c_names = ("Identifier", "Formatted Text", "Name Of Coding System", "Alternate Identifier", "Alternate Formatted Text", "Name Of Alternate Coding System",)
    _c_attrs = ("identifier", "formatted_text", "name_of_coding_system", "alternate_identifier", "alternate_formatted_text", "name_of_alternate_coding_system",)
    # fmt: on

    def __init__(
        self,
        identifier: ST | None = None,  # CF.1
        formatted_text: FT | None = None,  # CF.2
        name_of_coding_system: CodingSystem | ID | None = None,  # CF.3
        alternate_identifier: ST | None = None,  # CF.4
        alternate_formatted_text: FT | None = None,  # CF.5
        name_of_alternate_coding_system: CodingSystem | ID | None = None,  # CF.6
    ):
        """
                Coded Element with Formatted Values - `CF <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CF>`_
                This data type transmits codes and the formatted text associated with the code. This data type can be used to transmit for the first time the formatted text for the canned text portion of a report, for example, a standard radiological description for a normal chest X-ray. The receiving system can store this information and in subsequent messages only the identifier need be sent. Another potential use of this data type is transmitting master file records that contain formatted text.

        Example:  OBX||CF|71020^CXR^99CPMC||79989^\\H\\Description:\\N\\\\.sp\\\\ti+4\\Heart is not enlarged. There is no evidence of pneumonia, effusion, pneumothorax or any masses. \\.sp+3\\\\H\\Impression:\\N\\\\.sp\\\\.ti+4\\Negative chest.^99CPMC

                :param identifier: Sequence of characters (the code) that uniquely identifies the item being referenced by the <text> (id: CF.1 | len: 20 | use: O | rpt: 1)
                :param formatted_text: Name or description of the item in question with the addition of embedded formatting instructions (id: CF.2 | len: 65536 | use: O | rpt: 1)
                :param name_of_coding_system: Contains the name of the coding system employed (id: CF.3 | len: 20 | use: O | rpt: 1)
                :param alternate_identifier: Alternate sequence of characters (the code) that uniquely identifies the item being referenced by the <text> (id: CF.4 | len: 20 | use: O | rpt: 1)
                :param alternate_formatted_text: Name or description of the alternate identifier in question with the addition of embedded formatting instructions (id: CF.5 | len: 65536 | use: O | rpt: 1)
                :param name_of_alternate_coding_system: Contains the name of the coding system employed for the alternate identifier (id: CF.6 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.identifier = identifier
        self.formatted_text = formatted_text
        self.name_of_coding_system = name_of_coding_system
        self.alternate_identifier = alternate_identifier
        self.alternate_formatted_text = alternate_formatted_text
        self.name_of_alternate_coding_system = name_of_alternate_coding_system

    @property  # get CF.1
    def identifier(self) -> ST | None:
        """
        id: CF.1 | len: 20 | use: O | rpt: 1
        ---
        Sequence of characters (the code) that uniquely identifies the item being referenced by the <text>. Different coding schemes will have different elements here.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.1
        """
        return self._c_data[0][0]

    @identifier.setter  # set CF.1
    def identifier(self, st: ST | None):
        """
        id: CF.1 | len: 20 | use: O | rpt: 1
        ---
        Sequence of characters (the code) that uniquely identifies the item being referenced by the <text>. Different coding schemes will have different elements here.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.1
        """
        self._c_data[0] = (st,)

    @property  # get CF.2
    def formatted_text(self) -> FT | None:
        """
        id: CF.2 | len: 65536 | use: O | rpt: 1
        ---
        Name or description of the item in question with the addition of embedded formatting instructions.
        ---
        return_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.2
        """
        return self._c_data[1][0]

    @formatted_text.setter  # set CF.2
    def formatted_text(self, ft: FT | None):
        """
        id: CF.2 | len: 65536 | use: O | rpt: 1
        ---
        Name or description of the item in question with the addition of embedded formatting instructions.
        ---
        param_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.2
        """
        self._c_data[1] = (ft,)

    @property  # get CF.3
    def name_of_coding_system(self) -> CodingSystem | None:
        """
        id: CF.3 | len: 20 | use: O | rpt: 1
        ---
        Contains the name of the coding system employed.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.3
        """
        return self._c_data[2][0]

    @name_of_coding_system.setter  # set CF.3
    def name_of_coding_system(self, coding_system: CodingSystem | None):
        """
        id: CF.3 | len: 20 | use: O | rpt: 1
        ---
        Contains the name of the coding system employed.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.3
        """
        self._c_data[2] = (coding_system,)

    @property  # get CF.4
    def alternate_identifier(self) -> ST | None:
        """
        id: CF.4 | len: 20 | use: O | rpt: 1
        ---
        Alternate sequence of characters (the code) that uniquely identifies the item being referenced by the <text>. This identifier is the equivalent of component one.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.4
        """
        return self._c_data[3][0]

    @alternate_identifier.setter  # set CF.4
    def alternate_identifier(self, st: ST | None):
        """
        id: CF.4 | len: 20 | use: O | rpt: 1
        ---
        Alternate sequence of characters (the code) that uniquely identifies the item being referenced by the <text>. This identifier is the equivalent of component one.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.4
        """
        self._c_data[3] = (st,)

    @property  # get CF.5
    def alternate_formatted_text(self) -> FT | None:
        """
        id: CF.5 | len: 65536 | use: O | rpt: 1
        ---
        Name or description of the alternate identifier in question with the addition of embedded formatting instructions.
        ---
        return_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.5
        """
        return self._c_data[4][0]

    @alternate_formatted_text.setter  # set CF.5
    def alternate_formatted_text(self, ft: FT | None):
        """
        id: CF.5 | len: 65536 | use: O | rpt: 1
        ---
        Name or description of the alternate identifier in question with the addition of embedded formatting instructions.
        ---
        param_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.5
        """
        self._c_data[4] = (ft,)

    @property  # get CF.6
    def name_of_alternate_coding_system(self) -> CodingSystem | None:
        """
        id: CF.6 | len: 20 | use: O | rpt: 1
        ---
        Contains the name of the coding system employed for the alternate identifier.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.6
        """
        return self._c_data[5][0]

    @name_of_alternate_coding_system.setter  # set CF.6
    def name_of_alternate_coding_system(self, coding_system: CodingSystem | None):
        """
        id: CF.6 | len: 20 | use: O | rpt: 1
        ---
        Contains the name of the coding system employed for the alternate identifier.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CF.6
        """
        self._c_data[5] = (coding_system,)
