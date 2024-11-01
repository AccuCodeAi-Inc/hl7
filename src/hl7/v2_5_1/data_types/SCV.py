from __future__ import annotations
from ...base import DataType
from .ST import ST
from .CWE import CWE


"""
DataType - SCV
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::SCV TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SCV,
    ST, CWE
)

scv = SCV(  # Scheduling Class Value Pair - This data type is used to communicate parameters and preferences to the filler application regarding the selection of an appropriate time slot, resource, location, or filler override criterion for an appointment
    parameter_class=None,  # CWE(...) 
    parameter_value=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::SCV TEMPLATE-----
"""


class SCV(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 41
    _hl7_id = """SCV"""
    _hl7_name = """Scheduling Class Value Pair"""
    _hl7_description = """This data type is used to communicate parameters and preferences to the filler application regarding the selection of an appropriate time slot, resource, location, or filler override criterion for an appointment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCV"
    _c_length = (20, 20,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_aliases = ("SCV.1", "SCV.2",)
    _c_components = (CWE, ST,)
    _c_names = ("Parameter Class", "Parameter Value",)
    _c_attrs = ("parameter_class", "parameter_value",)
    # fmt: on

    def __init__(
        self,
        parameter_class: CWE | tuple[CWE, ...] | None = None,  # SCV.1
        parameter_value: ST | tuple[ST, ...] | None = None,  # SCV.2
    ):
        """
        Scheduling Class Value Pair - `SCV <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SCV>`_
        This data type is used to communicate parameters and preferences to the filler application regarding the selection of an appropriate time slot, resource, location, or filler override criterion for an appointment.

        :param parameter_class: The first component of this field is a code identifying the parameter or preference being passed to the filler application (id: SCV.1 | len: 20 | use: O | rpt: 1)
        :param parameter_value: The second component is the actual data value for that parameter (id: SCV.2 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.parameter_class = parameter_class
        self.parameter_value = parameter_value

    @property  # get SCV.1
    def parameter_class(self) -> CWE | None:
        """
        id: SCV.1 | len: 20 | use: O | rpt: 1
        ---
        The first component of this field is a code identifying the parameter or preference being passed to the filler application. Refer to User-defined Table 0294 - Time selection criteria parameter class codes - Time selection criteria parameter class codes for suggested values.
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCV.1
        """
        return self._c_data[0][0]

    @parameter_class.setter  # set SCV.1
    def parameter_class(self, cwe: CWE | None):
        """
        id: SCV.1 | len: 20 | use: O | rpt: 1
        ---
        The first component of this field is a code identifying the parameter or preference being passed to the filler application. Refer to User-defined Table 0294 - Time selection criteria parameter class codes - Time selection criteria parameter class codes for suggested values.
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCV.1
        """
        self._c_data[0] = (cwe,)

    @property  # get SCV.2
    def parameter_value(self) -> ST | None:
        """
        id: SCV.2 | len: 20 | use: O | rpt: 1
        ---
        The second component is the actual data value for that parameter.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCV.2
        """
        return self._c_data[1][0]

    @parameter_value.setter  # set SCV.2
    def parameter_value(self, st: ST | None):
        """
        id: SCV.2 | len: 20 | use: O | rpt: 1
        ---
        The second component is the actual data value for that parameter.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCV.2
        """
        self._c_data[1] = (st,)
