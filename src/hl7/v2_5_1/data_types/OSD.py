from __future__ import annotations
from ...base import DataType
from .IS import IS
from .ST import ST
from .ID import ID
from .NM import NM
from ..tables.UniversalIdType import UniversalIdType
from ..tables.SequenceCondition import SequenceCondition
from ..tables.AssigningAuthority import AssigningAuthority


"""
DataType - OSD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::OSD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OSD,
    IS, ST, ID, NM
)

osd = OSD(  # Order Sequence Definition - This data type specifies a fully coded version for forming a relationship between an order and one or more other orders
    sequence_or_results_flag=id,  # ID(...)  # Required.
    placer_order_number_entity_identifier=st,  # ST(...)  # Required.
    placer_order_number_namespace_id=None,  # IS(...) 
    filler_order_number_entity_identifier=st,  # ST(...)  # Required.
    filler_order_number_namespace_id=None,  # IS(...) 
    sequence_condition_value=None,  # ST(...) 
    maximum_number_of_repeats=None,  # NM(...) 
    placer_order_number_universal_id=st,  # ST(...)  # Required.
    placer_order_number_universal_id_type=None,  # ID(...) 
    filler_order_number_universal_id=st,  # ST(...)  # Required.
    filler_order_number_universal_id_type=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::OSD TEMPLATE-----
"""


class OSD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 110
    _hl7_id = """OSD"""
    _hl7_name = """Order Sequence Definition"""
    _hl7_description = """This data type specifies a fully coded version for forming a relationship between an order and one or more other orders"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD"
    _c_length = (1, 15, 6, 15, 6, 12, 3, 15, 6, 15, 6,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "O", "R", "O", "O", "O", "R", "O", "R", "O",)
    _c_aliases = ("OSD.1", "OSD.2", "OSD.3", "OSD.4", "OSD.5", "OSD.6", "OSD.7", "OSD.8", "OSD.9", "OSD.10", "OSD.11",)
    _c_components = (ID, ST, IS, ST, IS, ST, NM, ST, ID, ST, ID,)
    _c_names = ("Sequence/Results Flag", "Placer Order Number: Entity Identifier", "Placer Order Number: Namespace Id", "Filler Order Number: Entity Identifier", "Filler Order Number: Namespace Id", "Sequence Condition Value", "Maximum Number Of Repeats", "Placer Order Number: Universal Id", "Placer Order Number: Universal Id Type", "Filler Order Number: Universal Id", "Filler Order Number: Universal Id Type",)
    _c_attrs = ("sequence_or_results_flag", "placer_order_number_entity_identifier", "placer_order_number_namespace_id", "filler_order_number_entity_identifier", "filler_order_number_namespace_id", "sequence_condition_value", "maximum_number_of_repeats", "placer_order_number_universal_id", "placer_order_number_universal_id_type", "filler_order_number_universal_id", "filler_order_number_universal_id_type",)
    # fmt: on

    def __init__(
        self,
        sequence_or_results_flag: SequenceCondition | ID,  # OSD.1
        placer_order_number_entity_identifier: ST,  # OSD.2
        filler_order_number_entity_identifier: ST,  # OSD.4
        placer_order_number_universal_id: ST,  # OSD.8
        filler_order_number_universal_id: ST,  # OSD.10
        placer_order_number_namespace_id: AssigningAuthority
        | IS
        | None = None,  # OSD.3
        filler_order_number_namespace_id: AssigningAuthority
        | IS
        | None = None,  # OSD.5
        sequence_condition_value: ST | None = None,  # OSD.6
        maximum_number_of_repeats: NM | None = None,  # OSD.7
        placer_order_number_universal_id_type: UniversalIdType
        | ID
        | None = None,  # OSD.9
        filler_order_number_universal_id_type: UniversalIdType
        | ID
        | None = None,  # OSD.11
    ):
        """
        Order Sequence Definition - `OSD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OSD>`_
        This data type specifies a fully coded version for forming a relationship between an order and one or more other orders. The relationship may be sequential or a cyclical pattern.

        :param sequence_or_results_flag: Identifies whether sequence conditions or a repeating cycle of orders is defined (id: OSD.1 | len: 1 | use: R | rpt: 1)
        :param placer_order_number_entity_identifier: Contains the first component of the placer order number, entity identifier  (id: OSD.2 | len: 15 | use: R | rpt: 1)
        :param placer_order_number_namespace_id: Contains the second component of the placer order number, namespace ID (id: OSD.3 | len: 6 | use: O | rpt: 1)
        :param filler_order_number_entity_identifier: Contains the first component of the filler order number, entity identifier (id: OSD.4 | len: 15 | use: R | rpt: 1)
        :param filler_order_number_namespace_id: Contains the second component of the filler order number, namespace ID (id: OSD.5 | len: 6 | use: O | rpt: 1)
        :param sequence_condition_value: Defines the relationship between the start/end of the related predecessor or successor order and the current order from ORC-2, 3 or 4 (id: OSD.6 | len: 12 | use: O | rpt: 1)
        :param maximum_number_of_repeats: The maximum number of repeats to be used only on cyclic groups (id: OSD.7 | len: 3 | use: O | rpt: 1)
        :param placer_order_number_universal_id: Contains the next to the last component of the placer order number, universal ID (id: OSD.8 | len: 15 | use: R | rpt: 1)
        :param placer_order_number_universal_id_type: Contains the last component of the placer order number (id: OSD.9 | len: 6 | use: O | rpt: 1)
        :param filler_order_number_universal_id: Contains the next to the last component of the filler order number, universal ID (id: OSD.10 | len: 15 | use: R | rpt: 1)
        :param filler_order_number_universal_id_type: Contains the last component of the placer order number (id: OSD.11 | len: 6 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 11
        self.sequence_or_results_flag = sequence_or_results_flag
        self.placer_order_number_entity_identifier = (
            placer_order_number_entity_identifier
        )
        self.placer_order_number_namespace_id = placer_order_number_namespace_id
        self.filler_order_number_entity_identifier = (
            filler_order_number_entity_identifier
        )
        self.filler_order_number_namespace_id = filler_order_number_namespace_id
        self.sequence_condition_value = sequence_condition_value
        self.maximum_number_of_repeats = maximum_number_of_repeats
        self.placer_order_number_universal_id = placer_order_number_universal_id
        self.placer_order_number_universal_id_type = (
            placer_order_number_universal_id_type
        )
        self.filler_order_number_universal_id = filler_order_number_universal_id
        self.filler_order_number_universal_id_type = (
            filler_order_number_universal_id_type
        )

    @property  # get OSD.1
    def sequence_or_results_flag(self) -> SequenceCondition:
        """
        id: OSD.1 | len: 1 | use: R | rpt: 1
        ---
        Identifies whether sequence conditions or a repeating cycle of orders is defined. Refer to HL7-defined Table 0524 - Sequence condition for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.1
        """
        return self._c_data[0][0]

    @sequence_or_results_flag.setter  # set OSD.1
    def sequence_or_results_flag(self, sequence_condition: SequenceCondition):
        """
        id: OSD.1 | len: 1 | use: R | rpt: 1
        ---
        Identifies whether sequence conditions or a repeating cycle of orders is defined. Refer to HL7-defined Table 0524 - Sequence condition for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.1
        """
        self._c_data[0] = (sequence_condition,)

    @property  # get OSD.2
    def placer_order_number_entity_identifier(self) -> ST:
        """
        id: OSD.2 | len: 15 | use: R | rpt: 1
        ---
        Contains the first component of the placer order number, entity identifier .
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.2
        """
        return self._c_data[1][0]

    @placer_order_number_entity_identifier.setter  # set OSD.2
    def placer_order_number_entity_identifier(self, st: ST):
        """
        id: OSD.2 | len: 15 | use: R | rpt: 1
        ---
        Contains the first component of the placer order number, entity identifier .
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.2
        """
        self._c_data[1] = (st,)

    @property  # get OSD.3
    def placer_order_number_namespace_id(self) -> AssigningAuthority | None:
        """
        id: OSD.3 | len: 6 | use: O | rpt: 1
        ---
        Contains the second component of the placer order number, namespace ID. Refer to user-defined table 0363 - Assigning Authority for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.3
        """
        return self._c_data[2][0]

    @placer_order_number_namespace_id.setter  # set OSD.3
    def placer_order_number_namespace_id(
        self, assigning_authority: AssigningAuthority | None
    ):
        """
        id: OSD.3 | len: 6 | use: O | rpt: 1
        ---
        Contains the second component of the placer order number, namespace ID. Refer to user-defined table 0363 - Assigning Authority for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.3
        """
        self._c_data[2] = (assigning_authority,)

    @property  # get OSD.4
    def filler_order_number_entity_identifier(self) -> ST:
        """
        id: OSD.4 | len: 15 | use: R | rpt: 1
        ---
        Contains the first component of the filler order number, entity identifier.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.4
        """
        return self._c_data[3][0]

    @filler_order_number_entity_identifier.setter  # set OSD.4
    def filler_order_number_entity_identifier(self, st: ST):
        """
        id: OSD.4 | len: 15 | use: R | rpt: 1
        ---
        Contains the first component of the filler order number, entity identifier.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.4
        """
        self._c_data[3] = (st,)

    @property  # get OSD.5
    def filler_order_number_namespace_id(self) -> AssigningAuthority | None:
        """
        id: OSD.5 | len: 6 | use: O | rpt: 1
        ---
        Contains the second component of the filler order number, namespace ID. Refer to user-defined table 0363 - Assigning Authority for suggested values
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.5
        """
        return self._c_data[4][0]

    @filler_order_number_namespace_id.setter  # set OSD.5
    def filler_order_number_namespace_id(
        self, assigning_authority: AssigningAuthority | None
    ):
        """
        id: OSD.5 | len: 6 | use: O | rpt: 1
        ---
        Contains the second component of the filler order number, namespace ID. Refer to user-defined table 0363 - Assigning Authority for suggested values
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.5
        """
        self._c_data[4] = (assigning_authority,)

    @property  # get OSD.6
    def sequence_condition_value(self) -> ST | None:
        """
        id: OSD.6 | len: 12 | use: O | rpt: 1
        ---
        Defines the relationship between the start/end of the related predecessor or successor order and the current order from ORC-2, 3 or 4.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.6
        """
        return self._c_data[5][0]

    @sequence_condition_value.setter  # set OSD.6
    def sequence_condition_value(self, st: ST | None):
        """
        id: OSD.6 | len: 12 | use: O | rpt: 1
        ---
        Defines the relationship between the start/end of the related predecessor or successor order and the current order from ORC-2, 3 or 4.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.6
        """
        self._c_data[5] = (st,)

    @property  # get OSD.7
    def maximum_number_of_repeats(self) -> NM | None:
        """
        id: OSD.7 | len: 3 | use: O | rpt: 1
        ---
        The maximum number of repeats to be used only on cyclic groups. The total number of repeats is constrained by the end date/time of the last repeat or the end date/time of the parent, whichever is first.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.7
        """
        return self._c_data[6][0]

    @maximum_number_of_repeats.setter  # set OSD.7
    def maximum_number_of_repeats(self, nm: NM | None):
        """
        id: OSD.7 | len: 3 | use: O | rpt: 1
        ---
        The maximum number of repeats to be used only on cyclic groups. The total number of repeats is constrained by the end date/time of the last repeat or the end date/time of the parent, whichever is first.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.7
        """
        self._c_data[6] = (nm,)

    @property  # get OSD.8
    def placer_order_number_universal_id(self) -> ST:
        """
        id: OSD.8 | len: 15 | use: R | rpt: 1
        ---
        Contains the next to the last component of the placer order number, universal ID.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.8
        """
        return self._c_data[7][0]

    @placer_order_number_universal_id.setter  # set OSD.8
    def placer_order_number_universal_id(self, st: ST):
        """
        id: OSD.8 | len: 15 | use: R | rpt: 1
        ---
        Contains the next to the last component of the placer order number, universal ID.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.8
        """
        self._c_data[7] = (st,)

    @property  # get OSD.9
    def placer_order_number_universal_id_type(self) -> UniversalIdType | None:
        """
        id: OSD.9 | len: 6 | use: O | rpt: 1
        ---
        Contains the last component of the placer order number. Refer to HL7 table 0301 - Universal ID Type for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.9
        """
        return self._c_data[8][0]

    @placer_order_number_universal_id_type.setter  # set OSD.9
    def placer_order_number_universal_id_type(
        self, universal_id_type: UniversalIdType | None
    ):
        """
        id: OSD.9 | len: 6 | use: O | rpt: 1
        ---
        Contains the last component of the placer order number. Refer to HL7 table 0301 - Universal ID Type for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.9
        """
        self._c_data[8] = (universal_id_type,)

    @property  # get OSD.10
    def filler_order_number_universal_id(self) -> ST:
        """
        id: OSD.10 | len: 15 | use: R | rpt: 1
        ---
        Contains the next to the last component of the filler order number, universal ID.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.10
        """
        return self._c_data[9][0]

    @filler_order_number_universal_id.setter  # set OSD.10
    def filler_order_number_universal_id(self, st: ST):
        """
        id: OSD.10 | len: 15 | use: R | rpt: 1
        ---
        Contains the next to the last component of the filler order number, universal ID.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.10
        """
        self._c_data[9] = (st,)

    @property  # get OSD.11
    def filler_order_number_universal_id_type(self) -> UniversalIdType | None:
        """
        id: OSD.11 | len: 6 | use: O | rpt: 1
        ---
        Contains the last component of the placer order number. Refer to HL7 table 0301 - Universal ID Type for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.11
        """
        return self._c_data[10][0]

    @filler_order_number_universal_id_type.setter  # set OSD.11
    def filler_order_number_universal_id_type(
        self, universal_id_type: UniversalIdType | None
    ):
        """
        id: OSD.11 | len: 6 | use: O | rpt: 1
        ---
        Contains the last component of the placer order number. Refer to HL7 table 0301 - Universal ID Type for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSD.11
        """
        self._c_data[10] = (universal_id_type,)
