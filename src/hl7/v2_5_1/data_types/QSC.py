from __future__ import annotations
from ...base import DataType
from .ID import ID
from .ST import ST
from ..tables.RelationalOperator import RelationalOperator
from ..tables.RelationalConjunction import RelationalConjunction


"""
DataType - QSC
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::QSC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    QSC,
    ID, ST
)

qsc = QSC(  # Query Selection Criteria - This field indicates the conditions that qualify the rows to be returned in the query response
    segment_field_name=st,  # ST(...)  # Required.
    relational_operator=None,  # ID(...) 
    value=None,  # ST(...) 
    relational_conjunction=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::QSC TEMPLATE-----
"""


class QSC(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 219
    _hl7_id = """QSC"""
    _hl7_name = """Query Selection Criteria"""
    _hl7_description = """This field indicates the conditions that qualify the rows to be returned in the query response"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QSC"
    _c_length = (12, 2, 199, 3,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O",)
    _c_aliases = ("QSC.1", "QSC.2", "QSC.3", "QSC.4",)
    _c_components = (ST, ID, ST, ID,)
    _c_names = ("Segment Field Name", "Relational Operator", "Value", "Relational Conjunction",)
    _c_attrs = ("segment_field_name", "relational_operator", "value", "relational_conjunction",)
    # fmt: on

    def __init__(
        self,
        segment_field_name: ST,  # QSC.1
        relational_operator: RelationalOperator | ID | None = None,  # QSC.2
        value: ST | None = None,  # QSC.3
        relational_conjunction: RelationalConjunction | ID | None = None,  # QSC.4
    ):
        """
                Query Selection Criteria - `QSC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QSC>`_
                This field indicates the conditions that qualify the rows to be returned in the query response. Note that this field conveys the same information as the "WHERE" clause in the corresponding SQL expression of the query, but is formatted differently.

        Example: |@PID.5.1^EQ^EVANS|

                :param segment_field_name: The name of the field that is participating as a qualifier (usually the key) (id: QSC.1 | len: 12 | use: R | rpt: 1)
                :param relational_operator:  (id: QSC.2 | len: 2 | use: O | rpt: 1)
                :param value: The value to which the field will be compared (id: QSC.3 | len: 199 | use: O | rpt: 1)
                :param relational_conjunction:  (id: QSC.4 | len: 3 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.segment_field_name = segment_field_name
        self.relational_operator = relational_operator
        self.value = value
        self.relational_conjunction = relational_conjunction

    @property  # get QSC.1
    def segment_field_name(self) -> ST:
        """
        id: QSC.1 | len: 12 | use: R | rpt: 1
        ---
        The name of the field that is participating as a qualifier (usually the "key"). Refer to Section 2.A.59.1,  Segment Field Name (ST) , for segment field name conventions.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QSC.1
        """
        return self._c_data[0][0]

    @segment_field_name.setter  # set QSC.1
    def segment_field_name(self, st: ST):
        """
        id: QSC.1 | len: 12 | use: R | rpt: 1
        ---
        The name of the field that is participating as a qualifier (usually the "key"). Refer to Section 2.A.59.1,  Segment Field Name (ST) , for segment field name conventions.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QSC.1
        """
        self._c_data[0] = (st,)

    @property  # get QSC.2
    def relational_operator(self) -> RelationalOperator | None:
        """
        id: QSC.2 | len: 2 | use: O | rpt: 1
        ---
        None
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QSC.2
        """
        return self._c_data[1][0]

    @relational_operator.setter  # set QSC.2
    def relational_operator(self, relational_operator: RelationalOperator | None):
        """
        id: QSC.2 | len: 2 | use: O | rpt: 1
        ---
        None
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QSC.2
        """
        self._c_data[1] = (relational_operator,)

    @property  # get QSC.3
    def value(self) -> ST | None:
        """
        id: QSC.3 | len: 199 | use: O | rpt: 1
        ---
        The value to which the field will be compared.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QSC.3
        """
        return self._c_data[2][0]

    @value.setter  # set QSC.3
    def value(self, st: ST | None):
        """
        id: QSC.3 | len: 199 | use: O | rpt: 1
        ---
        The value to which the field will be compared.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QSC.3
        """
        self._c_data[2] = (st,)

    @property  # get QSC.4
    def relational_conjunction(self) -> RelationalConjunction | None:
        """
        id: QSC.4 | len: 3 | use: O | rpt: 1
        ---
        None
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QSC.4
        """
        return self._c_data[3][0]

    @relational_conjunction.setter  # set QSC.4
    def relational_conjunction(
        self, relational_conjunction: RelationalConjunction | None
    ):
        """
        id: QSC.4 | len: 3 | use: O | rpt: 1
        ---
        None
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QSC.4
        """
        self._c_data[3] = (relational_conjunction,)
