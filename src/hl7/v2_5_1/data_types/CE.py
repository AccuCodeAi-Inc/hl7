from __future__ import annotations
from ...base import DataType
from .ST import ST
from .ID import ID
from ..tables.CodingSystem import CodingSystem


"""
DataType - CE
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CE TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CE,
    ST, ID
)

ce = CE(  # Coded Element - This data type transmits codes and the text associated with the code
    identifier=None,  # ST(...) 
    text=None,  # ST(...) 
    name_of_coding_system=None,  # ID(...) 
    alternate_identifier=None,  # ST(...) 
    alternate_text=None,  # ST(...) 
    name_of_alternate_coding_system=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::CE TEMPLATE-----
"""


class CE(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 483
    _hl7_id = """CE"""
    _hl7_name = """Coded Element"""
    _hl7_description = """This data type transmits codes and the text associated with the code"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE"
    _c_length = (20, 199, 20, 20, 199, 20,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O",)
    _c_aliases = ("CE.1", "CE.2", "CE.3", "CE.4", "CE.5", "CE.6",)
    _c_components = (ST, ST, ID, ST, ST, ID,)
    _c_names = ("Identifier", "Text", "Name Of Coding System", "Alternate Identifier", "Alternate Text", "Name Of Alternate Coding System",)
    _c_attrs = ("identifier", "text", "name_of_coding_system", "alternate_identifier", "alternate_text", "name_of_alternate_coding_system",)
    # fmt: on

    def __init__(
        self,
        identifier: ST | tuple[ST, ...] | None = None,  # CE.1
        text: ST | tuple[ST, ...] | None = None,  # CE.2
        name_of_coding_system: CodingSystem
        | ID
        | tuple[CodingSystem | ID, ...]
        | None = None,  # CE.3
        alternate_identifier: ST | tuple[ST, ...] | None = None,  # CE.4
        alternate_text: ST | tuple[ST, ...] | None = None,  # CE.5
        name_of_alternate_coding_system: CodingSystem
        | ID
        | tuple[CodingSystem | ID, ...]
        | None = None,  # CE.6
    ):
        """
                Coded Element - `CE <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CE>`_
                This data type transmits codes and the text associated with the code.

        Note: retained for backward compatibility only as of v 2.5. Refer to the CNE and CWE data types.

        Example: |F-11380^CREATININE^I9^2148-5^CREATININE^LN|

                :param identifier: Sequence of characters (the code) that uniquely identifies the item being referenced (id: CE.1 | len: 20 | use: O | rpt: 1)
                :param text: The descriptive or textual name of the identifier, e (id: CE.2 | len: 199 | use: O | rpt: 1)
                :param name_of_coding_system: Identifies the coding scheme being used in the identifier component (id: CE.3 | len: 20 | use: O | rpt: 1)
                :param alternate_identifier: An alternate sequence of characters (the code) that uniquely identifies the item being referenced (id: CE.4 | len: 20 | use: O | rpt: 1)
                :param alternate_text: The descriptive or textual name of the alternate identifier (id: CE.5 | len: 199 | use: O | rpt: 1)
                :param name_of_alternate_coding_system: Identifies the coding scheme being used in the alternate identifier component (id: CE.6 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.identifier = identifier
        self.text = text
        self.name_of_coding_system = name_of_coding_system
        self.alternate_identifier = alternate_identifier
        self.alternate_text = alternate_text
        self.name_of_alternate_coding_system = name_of_alternate_coding_system

    @property  # get CE.1
    def identifier(self) -> ST | None:
        """
        id: CE.1 | len: 20 | use: O | rpt: 1
        ---
        Sequence of characters (the code) that uniquely identifies the item being referenced. Different coding schemes will have different elements here.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.1
        """
        return self._c_data[0][0]

    @identifier.setter  # set CE.1
    def identifier(self, st: ST | None):
        """
        id: CE.1 | len: 20 | use: O | rpt: 1
        ---
        Sequence of characters (the code) that uniquely identifies the item being referenced. Different coding schemes will have different elements here.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.1
        """
        self._c_data[0] = (st,)

    @property  # get CE.2
    def text(self) -> ST | None:
        """
        id: CE.2 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the identifier, e.g., myocardial infarction or X-ray impression.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.2
        """
        return self._c_data[1][0]

    @text.setter  # set CE.2
    def text(self, st: ST | None):
        """
        id: CE.2 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the identifier, e.g., myocardial infarction or X-ray impression.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.2
        """
        self._c_data[1] = (st,)

    @property  # get CE.3
    def name_of_coding_system(self) -> CodingSystem | None:
        """
        id: CE.3 | len: 20 | use: O | rpt: 1
        ---
        Identifies the coding scheme being used in the identifier component. The combination of the identifier and name of coding system components will be a unique code for a data item. Each system has a unique identifier.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.3
        """
        return self._c_data[2][0]

    @name_of_coding_system.setter  # set CE.3
    def name_of_coding_system(self, coding_system: CodingSystem | None):
        """
        id: CE.3 | len: 20 | use: O | rpt: 1
        ---
        Identifies the coding scheme being used in the identifier component. The combination of the identifier and name of coding system components will be a unique code for a data item. Each system has a unique identifier.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.3
        """
        self._c_data[2] = (coding_system,)

    @property  # get CE.4
    def alternate_identifier(self) -> ST | None:
        """
        id: CE.4 | len: 20 | use: O | rpt: 1
        ---
        An alternate sequence of characters (the code) that uniquely identifies the item being referenced. See usage note in section introduction.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.4
        """
        return self._c_data[3][0]

    @alternate_identifier.setter  # set CE.4
    def alternate_identifier(self, st: ST | None):
        """
        id: CE.4 | len: 20 | use: O | rpt: 1
        ---
        An alternate sequence of characters (the code) that uniquely identifies the item being referenced. See usage note in section introduction.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.4
        """
        self._c_data[3] = (st,)

    @property  # get CE.5
    def alternate_text(self) -> ST | None:
        """
        id: CE.5 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the alternate identifier. See usage note in section introduction.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.5
        """
        return self._c_data[4][0]

    @alternate_text.setter  # set CE.5
    def alternate_text(self, st: ST | None):
        """
        id: CE.5 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the alternate identifier. See usage note in section introduction.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.5
        """
        self._c_data[4] = (st,)

    @property  # get CE.6
    def name_of_alternate_coding_system(self) -> CodingSystem | None:
        """
        id: CE.6 | len: 20 | use: O | rpt: 1
        ---
        Identifies the coding scheme being used in the alternate identifier component.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.6
        """
        return self._c_data[5][0]

    @name_of_alternate_coding_system.setter  # set CE.6
    def name_of_alternate_coding_system(self, coding_system: CodingSystem | None):
        """
        id: CE.6 | len: 20 | use: O | rpt: 1
        ---
        Identifies the coding scheme being used in the alternate identifier component.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CE.6
        """
        self._c_data[5] = (coding_system,)
