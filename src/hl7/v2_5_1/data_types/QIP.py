from __future__ import annotations
from ...base import DataType
from .ST import ST


"""
DataType - QIP
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::QIP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    QIP,
    ST
)

qip = QIP(  # Query Input Parameter List - This data type contains a segment field name and the list of values to be passed to the query processor
    segment_field_name=st,  # ST(...)  # Required.
    values=st,  # ST(...)  # Required.
)

-----END COMPOSITE_DATA_TYPE::QIP TEMPLATE-----
"""


class QIP(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 212
    _hl7_id = """QIP"""
    _hl7_name = """Query Input Parameter List"""
    _hl7_description = """This data type contains a segment field name and the list of values to be passed to the query processor"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QIP"
    _c_length = (12, 199,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "R",)
    _c_aliases = ("QIP.1", "QIP.2",)
    _c_components = (ST, ST,)
    _c_names = ("Segment Field Name", "Values",)
    _c_attrs = ("segment_field_name", "values",)
    # fmt: on

    def __init__(
        self,
        segment_field_name: ST | tuple[ST, ...],  # QIP.1
        values: ST | tuple[ST, ...],  # QIP.2
    ):
        """
                Query Input Parameter List - `QIP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QIP>`_
                This data type contains a segment field name and the list of values to be passed to the query processor.

        Example: |@PID.5.1^EVANS|

                :param segment_field_name: This component contains the segment field name (id: QIP.1 | len: 12 | use: R | rpt: 1)
                :param values: This component contains the field value or values in the form value1& value2 & value3 (id: QIP.2 | len: 199 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.segment_field_name = segment_field_name
        self.values = values

    @property  # get QIP.1
    def segment_field_name(self) -> ST:
        """
        id: QIP.1 | len: 12 | use: R | rpt: 1
        ---
        This component contains the segment field name.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QIP.1
        """
        return self._c_data[0][0]

    @segment_field_name.setter  # set QIP.1
    def segment_field_name(self, st: ST):
        """
        id: QIP.1 | len: 12 | use: R | rpt: 1
        ---
        This component contains the segment field name.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QIP.1
        """
        self._c_data[0] = (st,)

    @property  # get QIP.2
    def values(self) -> ST:
        """
        id: QIP.2 | len: 199 | use: R | rpt: 1
        ---
        This component contains the field value or values in the form "value1& value2 & value3"
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QIP.2
        """
        return self._c_data[1][0]

    @values.setter  # set QIP.2
    def values(self, st: ST):
        """
        id: QIP.2 | len: 199 | use: R | rpt: 1
        ---
        This component contains the field value or values in the form "value1& value2 & value3"
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QIP.2
        """
        self._c_data[1] = (st,)
