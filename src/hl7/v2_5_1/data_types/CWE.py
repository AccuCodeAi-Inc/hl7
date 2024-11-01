from __future__ import annotations
from ...base import DataType
from .ID import ID
from .ST import ST
from ..tables.CodingSystem import CodingSystem


"""
DataType - CWE
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CWE TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CWE,
    ID, ST
)

cwe = CWE(  # Coded with Exceptions - Specifies a coded element and its associated detail
    identifier=None,  # ST(...) 
    text=None,  # ST(...) 
    name_of_coding_system=None,  # ID(...) 
    alternate_identifier=None,  # ST(...) 
    alternate_text=None,  # ST(...) 
    name_of_alternate_coding_system=None,  # ID(...) 
    coding_system_version_id=None,  # ST(...) 
    alternate_coding_system_version_id=None,  # ST(...) 
    original_text=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::CWE TEMPLATE-----
"""


class CWE(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 705
    _hl7_id = """CWE"""
    _hl7_name = """Coded with Exceptions"""
    _hl7_description = """Specifies a coded element and its associated detail"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE"
    _c_length = (20, 199, 20, 20, 199, 20, 10, 10, 199,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "C", "O", "O",)
    _c_aliases = ("CWE.1", "CWE.2", "CWE.3", "CWE.4", "CWE.5", "CWE.6", "CWE.7", "CWE.8", "CWE.9",)
    _c_components = (ST, ST, ID, ST, ST, ID, ST, ST, ST,)
    _c_names = ("Identifier", "Text", "Name Of Coding System", "Alternate Identifier", "Alternate Text", "Name Of Alternate Coding System", "Coding System Version Id", "Alternate Coding System Version Id", "Original Text",)
    _c_attrs = ("identifier", "text", "name_of_coding_system", "alternate_identifier", "alternate_text", "name_of_alternate_coding_system", "coding_system_version_id", "alternate_coding_system_version_id", "original_text",)
    # fmt: on

    def __init__(
        self,
        identifier: ST | tuple[ST] | None = None,  # CWE.1
        text: ST | tuple[ST] | None = None,  # CWE.2
        name_of_coding_system: CodingSystem
        | ID
        | tuple[CodingSystem | ID]
        | None = None,  # CWE.3
        alternate_identifier: ST | tuple[ST] | None = None,  # CWE.4
        alternate_text: ST | tuple[ST] | None = None,  # CWE.5
        name_of_alternate_coding_system: CodingSystem
        | ID
        | tuple[CodingSystem | ID]
        | None = None,  # CWE.6
        coding_system_version_id: ST | tuple[ST] | None = None,  # CWE.7
        alternate_coding_system_version_id: ST | tuple[ST] | None = None,  # CWE.8
        original_text: ST | tuple[ST] | None = None,  # CWE.9
    ):
        """
        Coded with Exceptions - `CWE <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CWE>`_
        Specifies a coded element and its associated detail. The CWE data type is used when 1) more than one table may be applicable or 2) the specified HL7 or externally defined table may be extended with local values or 3) when text is in place, the code may be omitted.

        :param identifier: Sequence of characters (the code) that uniquely identifies the item being referenced (id: CWE.1 | len: 20 | use: O | rpt: 1)
        :param text: The descriptive or textual name of the identifier, e (id: CWE.2 | len: 199 | use: O | rpt: 1)
        :param name_of_coding_system: Identifies the coding scheme being used in the identifier component (id: CWE.3 | len: 20 | use: O | rpt: 1)
        :param alternate_identifier: An alternate sequence of characters (the code) that uniquely identifies the item being referenced (id: CWE.4 | len: 20 | use: O | rpt: 1)
        :param alternate_text: The descriptive or textual name of the alternate identifier (id: CWE.5 | len: 199 | use: O | rpt: 1)
        :param name_of_alternate_coding_system: Identifies the coding scheme being used in the alternate identifier component (id: CWE.6 | len: 20 | use: O | rpt: 1)
        :param coding_system_version_id: This is the version ID for the coding system identified by components 1-3 (id: CWE.7 | len: 10 | use: C | rpt: 1)
        :param alternate_coding_system_version_id: This is the version ID for the coding system identified by components 4-6 (id: CWE.8 | len: 10 | use: O | rpt: 1)
        :param original_text: The original text that was available to an automated process or a human before a specific code was assigned (id: CWE.9 | len: 199 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.identifier = identifier
        self.text = text
        self.name_of_coding_system = name_of_coding_system
        self.alternate_identifier = alternate_identifier
        self.alternate_text = alternate_text
        self.name_of_alternate_coding_system = name_of_alternate_coding_system
        self.coding_system_version_id = coding_system_version_id
        self.alternate_coding_system_version_id = alternate_coding_system_version_id
        self.original_text = original_text

    @property  # get CWE.1
    def identifier(self) -> ST | None:
        """
        id: CWE.1 | len: 20 | use: O | rpt: 1
        ---
        Sequence of characters (the code) that uniquely identifies the item being referenced. Different coding schemes will have different elements here.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.1
        """
        return self._c_data[0][0]

    @identifier.setter  # set CWE.1
    def identifier(self, st: ST | None):
        """
        id: CWE.1 | len: 20 | use: O | rpt: 1
        ---
        Sequence of characters (the code) that uniquely identifies the item being referenced. Different coding schemes will have different elements here.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.1
        """
        self._c_data[0] = (st,)

    @property  # get CWE.2
    def text(self) -> ST | None:
        """
        id: CWE.2 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the identifier, e.g., myocardial infarction or X-ray impression.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.2
        """
        return self._c_data[1][0]

    @text.setter  # set CWE.2
    def text(self, st: ST | None):
        """
        id: CWE.2 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the identifier, e.g., myocardial infarction or X-ray impression.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.2
        """
        self._c_data[1] = (st,)

    @property  # get CWE.3
    def name_of_coding_system(self) -> CodingSystem | None:
        """
        id: CWE.3 | len: 20 | use: O | rpt: 1
        ---
        Identifies the coding scheme being used in the identifier component.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.3
        """
        return self._c_data[2][0]

    @name_of_coding_system.setter  # set CWE.3
    def name_of_coding_system(self, coding_system: CodingSystem | None):
        """
        id: CWE.3 | len: 20 | use: O | rpt: 1
        ---
        Identifies the coding scheme being used in the identifier component.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.3
        """
        self._c_data[2] = (coding_system,)

    @property  # get CWE.4
    def alternate_identifier(self) -> ST | None:
        """
        id: CWE.4 | len: 20 | use: O | rpt: 1
        ---
        An alternate sequence of characters (the code) that uniquely identifies the item being referenced. Analogous to "Identifier" in component 1. See usage note in section introduction.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.4
        """
        return self._c_data[3][0]

    @alternate_identifier.setter  # set CWE.4
    def alternate_identifier(self, st: ST | None):
        """
        id: CWE.4 | len: 20 | use: O | rpt: 1
        ---
        An alternate sequence of characters (the code) that uniquely identifies the item being referenced. Analogous to "Identifier" in component 1. See usage note in section introduction.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.4
        """
        self._c_data[3] = (st,)

    @property  # get CWE.5
    def alternate_text(self) -> ST | None:
        """
        id: CWE.5 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the alternate identifier. Analogous to "Text" in component 2. See usage note in section introduction.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.5
        """
        return self._c_data[4][0]

    @alternate_text.setter  # set CWE.5
    def alternate_text(self, st: ST | None):
        """
        id: CWE.5 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the alternate identifier. Analogous to "Text" in component 2. See usage note in section introduction.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.5
        """
        self._c_data[4] = (st,)

    @property  # get CWE.6
    def name_of_alternate_coding_system(self) -> CodingSystem | None:
        """
        id: CWE.6 | len: 20 | use: O | rpt: 1
        ---
        Identifies the coding scheme being used in the alternate identifier component. Analogous to Name of Coding System above. See usage note in section introduction.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.6
        """
        return self._c_data[5][0]

    @name_of_alternate_coding_system.setter  # set CWE.6
    def name_of_alternate_coding_system(self, coding_system: CodingSystem | None):
        """
        id: CWE.6 | len: 20 | use: O | rpt: 1
        ---
        Identifies the coding scheme being used in the alternate identifier component. Analogous to Name of Coding System above. See usage note in section introduction.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.6
        """
        self._c_data[5] = (coding_system,)

    @property  # get CWE.7
    def coding_system_version_id(self) -> ST | None:
        """
        id: CWE.7 | len: 10 | use: C | rpt: 1
        ---
        This is the version ID for the coding system identified by components 1-3. It belongs conceptually to the group of component 1-3 and appears here only for reasons of backward compatibility.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.7
        """
        return self._c_data[6][0]

    @coding_system_version_id.setter  # set CWE.7
    def coding_system_version_id(self, st: ST | None):
        """
        id: CWE.7 | len: 10 | use: C | rpt: 1
        ---
        This is the version ID for the coding system identified by components 1-3. It belongs conceptually to the group of component 1-3 and appears here only for reasons of backward compatibility.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.7
        """
        self._c_data[6] = (st,)

    @property  # get CWE.8
    def alternate_coding_system_version_id(self) -> ST | None:
        """
        id: CWE.8 | len: 10 | use: O | rpt: 1
        ---
        This is the version ID for the coding system identified by components 4-6. It belongs conceptually to the group of alternate components (See usage note in section introduction) and appears here only for reasons of backward compatibility.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.8
        """
        return self._c_data[7][0]

    @alternate_coding_system_version_id.setter  # set CWE.8
    def alternate_coding_system_version_id(self, st: ST | None):
        """
        id: CWE.8 | len: 10 | use: O | rpt: 1
        ---
        This is the version ID for the coding system identified by components 4-6. It belongs conceptually to the group of alternate components (See usage note in section introduction) and appears here only for reasons of backward compatibility.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.8
        """
        self._c_data[7] = (st,)

    @property  # get CWE.9
    def original_text(self) -> ST | None:
        """
        id: CWE.9 | len: 199 | use: O | rpt: 1
        ---
        The original text that was available to an automated process or a human before a specific code was assigned.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.9
        """
        return self._c_data[8][0]

    @original_text.setter  # set CWE.9
    def original_text(self, st: ST | None):
        """
        id: CWE.9 | len: 199 | use: O | rpt: 1
        ---
        The original text that was available to an automated process or a human before a specific code was assigned.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CWE.9
        """
        self._c_data[8] = (st,)
