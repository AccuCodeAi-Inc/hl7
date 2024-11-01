from __future__ import annotations
from ...base import DataType
from .ID import ID
from .ST import ST
from ..tables.CodingSystem import CodingSystem


"""
DataType - CNE
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CNE TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CNE,
    ID, ST
)

cne = CNE(  # Coded with No Exceptions - Specifies a coded element and its associated detail
    identifier=st,  # ST(...)  # Required.
    text=None,  # ST(...) 
    name_of_coding_system=None,  # ID(...) 
    alternate_identifier=None,  # ST(...) 
    alternate_text=None,  # ST(...) 
    name_of_alternate_coding_system=None,  # ID(...) 
    coding_system_version_id=None,  # ST(...) 
    alternate_coding_system_version_id=None,  # ST(...) 
    original_text=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::CNE TEMPLATE-----
"""


class CNE(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 705
    _hl7_id = """CNE"""
    _hl7_name = """Coded with No Exceptions"""
    _hl7_description = """Specifies a coded element and its associated detail"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE"
    _c_length = (20, 199, 20, 20, 199, 20, 10, 10, 199,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "C", "O", "O",)
    _c_aliases = ("CNE.1", "CNE.2", "CNE.3", "CNE.4", "CNE.5", "CNE.6", "CNE.7", "CNE.8", "CNE.9",)
    _c_components = (ST, ST, ID, ST, ST, ID, ST, ST, ST,)
    _c_names = ("Identifier", "Text", "Name Of Coding System", "Alternate Identifier", "Alternate Text", "Name Of Alternate Coding System", "Coding System Version Id", "Alternate Coding System Version Id", "Original Text",)
    _c_attrs = ("identifier", "text", "name_of_coding_system", "alternate_identifier", "alternate_text", "name_of_alternate_coding_system", "coding_system_version_id", "alternate_coding_system_version_id", "original_text",)
    # fmt: on

    def __init__(
        self,
        identifier: ST | tuple[ST],  # CNE.1
        text: ST | tuple[ST] | None = None,  # CNE.2
        name_of_coding_system: CodingSystem
        | ID
        | tuple[CodingSystem | ID]
        | None = None,  # CNE.3
        alternate_identifier: ST | tuple[ST] | None = None,  # CNE.4
        alternate_text: ST | tuple[ST] | None = None,  # CNE.5
        name_of_alternate_coding_system: CodingSystem
        | ID
        | tuple[CodingSystem | ID]
        | None = None,  # CNE.6
        coding_system_version_id: ST | tuple[ST] | None = None,  # CNE.7
        alternate_coding_system_version_id: ST | tuple[ST] | None = None,  # CNE.8
        original_text: ST | tuple[ST] | None = None,  # CNE.9
    ):
        """
        Coded with No Exceptions - `CNE <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CNE>`_
        Specifies a coded element and its associated detail. The CNE data type is used when a required or mandatory coded field is needed. The specified HL7 or externally defined table must be used and may not be extended with local values. Text may not replace the code. A CNE field must have an HL7 defined or external table associated with it. It must be specified in the standard.

        :param identifier: Sequence of characters (the code) that uniquely identifies the item being referenced by the CNE (id: CNE.1 | len: 20 | use: R | rpt: 1)
        :param text: The descriptive or textual name of the identifier, e (id: CNE.2 | len: 199 | use: O | rpt: 1)
        :param name_of_coding_system: Each coding system is assigned a unique identifier (id: CNE.3 | len: 20 | use: O | rpt: 1)
        :param alternate_identifier: Analogous to Identifier in component 1 (id: CNE.4 | len: 20 | use: O | rpt: 1)
        :param alternate_text: The descriptive or textual name of the alternate identifier (id: CNE.5 | len: 199 | use: O | rpt: 1)
        :param name_of_alternate_coding_system: Identifies the coding scheme being used in the alternate identifier component (id: CNE.6 | len: 20 | use: O | rpt: 1)
        :param coding_system_version_id: the version ID for the coding system identified by component 3 (id: CNE.7 | len: 10 | use: C | rpt: 1)
        :param alternate_coding_system_version_id: the version ID for the coding system identified by component -6 (id: CNE.8 | len: 10 | use: O | rpt: 1)
        :param original_text: The original text that was available to an automated process or a human before a specific code was assigned (id: CNE.9 | len: 199 | use: O | rpt: 1)
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

    @property  # get CNE.1
    def identifier(self) -> ST:
        """
        id: CNE.1 | len: 20 | use: R | rpt: 1
        ---
        Sequence of characters (the code) that uniquely identifies the item being referenced by the CNE.2. Different coding schemes will have different elements here.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.1
        """
        return self._c_data[0][0]

    @identifier.setter  # set CNE.1
    def identifier(self, st: ST):
        """
        id: CNE.1 | len: 20 | use: R | rpt: 1
        ---
        Sequence of characters (the code) that uniquely identifies the item being referenced by the CNE.2. Different coding schemes will have different elements here.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.1
        """
        self._c_data[0] = (st,)

    @property  # get CNE.2
    def text(self) -> ST | None:
        """
        id: CNE.2 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the identifier, e.g., myocardial infarction or X-ray impression. Its data type is string (ST). This is the corresponding text assigned by the coding system to the identifier.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.2
        """
        return self._c_data[1][0]

    @text.setter  # set CNE.2
    def text(self, st: ST | None):
        """
        id: CNE.2 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the identifier, e.g., myocardial infarction or X-ray impression. Its data type is string (ST). This is the corresponding text assigned by the coding system to the identifier.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.2
        """
        self._c_data[1] = (st,)

    @property  # get CNE.3
    def name_of_coding_system(self) -> CodingSystem | None:
        """
        id: CNE.3 | len: 20 | use: O | rpt: 1
        ---
        Each coding system is assigned a unique identifier. This component will serve to identify the coding scheme being used in the identifier component. The combination of the identifier and name of coding system components will be a unique code for a data item. Each system has a unique identifier.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.3
        """
        return self._c_data[2][0]

    @name_of_coding_system.setter  # set CNE.3
    def name_of_coding_system(self, coding_system: CodingSystem | None):
        """
        id: CNE.3 | len: 20 | use: O | rpt: 1
        ---
        Each coding system is assigned a unique identifier. This component will serve to identify the coding scheme being used in the identifier component. The combination of the identifier and name of coding system components will be a unique code for a data item. Each system has a unique identifier.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.3
        """
        self._c_data[2] = (coding_system,)

    @property  # get CNE.4
    def alternate_identifier(self) -> ST | None:
        """
        id: CNE.4 | len: 20 | use: O | rpt: 1
        ---
        Analogous to Identifier in component 1.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.4
        """
        return self._c_data[3][0]

    @alternate_identifier.setter  # set CNE.4
    def alternate_identifier(self, st: ST | None):
        """
        id: CNE.4 | len: 20 | use: O | rpt: 1
        ---
        Analogous to Identifier in component 1.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.4
        """
        self._c_data[3] = (st,)

    @property  # get CNE.5
    def alternate_text(self) -> ST | None:
        """
        id: CNE.5 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the alternate identifier. Analogous to "Text" in component 2. See usage notes in section introduction for further description.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.5
        """
        return self._c_data[4][0]

    @alternate_text.setter  # set CNE.5
    def alternate_text(self, st: ST | None):
        """
        id: CNE.5 | len: 199 | use: O | rpt: 1
        ---
        The descriptive or textual name of the alternate identifier. Analogous to "Text" in component 2. See usage notes in section introduction for further description.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.5
        """
        self._c_data[4] = (st,)

    @property  # get CNE.6
    def name_of_alternate_coding_system(self) -> CodingSystem | None:
        """
        id: CNE.6 | len: 20 | use: O | rpt: 1
        ---
        Identifies the coding scheme being used in the alternate identifier component. Analogous to Name of Coding System in component 3. Refer to HL7 Table 0396 in section 2.17.5 for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.6
        """
        return self._c_data[5][0]

    @name_of_alternate_coding_system.setter  # set CNE.6
    def name_of_alternate_coding_system(self, coding_system: CodingSystem | None):
        """
        id: CNE.6 | len: 20 | use: O | rpt: 1
        ---
        Identifies the coding scheme being used in the alternate identifier component. Analogous to Name of Coding System in component 3. Refer to HL7 Table 0396 in section 2.17.5 for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.6
        """
        self._c_data[5] = (coding_system,)

    @property  # get CNE.7
    def coding_system_version_id(self) -> ST | None:
        """
                id: CNE.7 | len: 10 | use: C | rpt: 1
                ---
                the version ID for the coding system identified by component 3. It belongs conceptually to components 1-3 and appears here only for reasons of backward compatibility.

        Usage Note: If the coding system is any system other than an "HL7 coding system," version ID must be valued with an actual version ID. If the coding system is "HL7 coding system," version ID may have an actual value or it may be absent. If version ID is absent, it will be interpreted to have the same value as the HL7 version number in the message header. Text description of code is optional but its use should be encouraged since it makes messages easier to review for accuracy, especially during interface testing and debugging.
                ---
                return_type: ST: String Data
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.7
        """
        return self._c_data[6][0]

    @coding_system_version_id.setter  # set CNE.7
    def coding_system_version_id(self, st: ST | None):
        """
                id: CNE.7 | len: 10 | use: C | rpt: 1
                ---
                the version ID for the coding system identified by component 3. It belongs conceptually to components 1-3 and appears here only for reasons of backward compatibility.

        Usage Note: If the coding system is any system other than an "HL7 coding system," version ID must be valued with an actual version ID. If the coding system is "HL7 coding system," version ID may have an actual value or it may be absent. If version ID is absent, it will be interpreted to have the same value as the HL7 version number in the message header. Text description of code is optional but its use should be encouraged since it makes messages easier to review for accuracy, especially during interface testing and debugging.
                ---
                param_type: ST: String Data
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.7
        """
        self._c_data[6] = (st,)

    @property  # get CNE.8
    def alternate_coding_system_version_id(self) -> ST | None:
        """
        id: CNE.8 | len: 10 | use: O | rpt: 1
        ---
        the version ID for the coding system identified by component -6. It belongs conceptually to the group of Alternate components (see note 2.A.6.6) and appears here only for reasons of backward compatibility.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.8
        """
        return self._c_data[7][0]

    @alternate_coding_system_version_id.setter  # set CNE.8
    def alternate_coding_system_version_id(self, st: ST | None):
        """
        id: CNE.8 | len: 10 | use: O | rpt: 1
        ---
        the version ID for the coding system identified by component -6. It belongs conceptually to the group of Alternate components (see note 2.A.6.6) and appears here only for reasons of backward compatibility.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.8
        """
        self._c_data[7] = (st,)

    @property  # get CNE.9
    def original_text(self) -> ST | None:
        """
        id: CNE.9 | len: 199 | use: O | rpt: 1
        ---
        The original text that was available to an automated process or a human before a specific code was assigned.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.9
        """
        return self._c_data[8][0]

    @original_text.setter  # set CNE.9
    def original_text(self, st: ST | None):
        """
        id: CNE.9 | len: 199 | use: O | rpt: 1
        ---
        The original text that was available to an automated process or a human before a specific code was assigned.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNE.9
        """
        self._c_data[8] = (st,)
