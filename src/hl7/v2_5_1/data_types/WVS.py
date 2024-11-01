from __future__ import annotations
from ...base import DataType
from .ST import ST


"""
DataType - WVS
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::WVS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    WVS,
    ST
)

wvs = WVS(  # Waveform Source - This data type identifies the source of the waveform connected to a channel
    source_one_name=st,  # ST(...)  # Required.
    source_two_name=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::WVS TEMPLATE-----
"""


class WVS(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 17
    _hl7_id = """WVS"""
    _hl7_name = """Waveform Source"""
    _hl7_description = """This data type identifies the source of the waveform connected to a channel"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/WVS"
    _c_length = (8, 8,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "O",)
    _c_aliases = ("WVS.1", "WVS.2",)
    _c_components = (ST, ST,)
    _c_names = ("Source One Name", "Source Two Name",)
    _c_attrs = ("source_one_name", "source_two_name",)
    # fmt: on

    def __init__(
        self,
        source_one_name: ST | tuple[ST, ...],  # WVS.1
        source_two_name: ST | tuple[ST, ...] | None = None,  # WVS.2
    ):
        """
        Waveform Source - `WVS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/WVS>`_
        This data type identifies the source of the waveform connected to a channel.

        :param source_one_name: This component identifies the first input for the waveform source (id: WVS.1 | len: 8 | use: R | rpt: 1)
        :param source_two_name: This component identifies the second input for the waveform source if a differential input is used (id: WVS.2 | len: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.source_one_name = source_one_name
        self.source_two_name = source_two_name

    @property  # get WVS.1
    def source_one_name(self) -> ST:
        """
        id: WVS.1 | len: 8 | use: R | rpt: 1
        ---
        This component identifies the first input for the waveform source.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/WVS.1
        """
        return self._c_data[0][0]

    @source_one_name.setter  # set WVS.1
    def source_one_name(self, st: ST):
        """
        id: WVS.1 | len: 8 | use: R | rpt: 1
        ---
        This component identifies the first input for the waveform source.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/WVS.1
        """
        self._c_data[0] = (st,)

    @property  # get WVS.2
    def source_two_name(self) -> ST | None:
        """
        id: WVS.2 | len: 8 | use: O | rpt: 1
        ---
        This component identifies the second input for the waveform source if a differential input is used.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/WVS.2
        """
        return self._c_data[1][0]

    @source_two_name.setter  # set WVS.2
    def source_two_name(self, st: ST | None):
        """
        id: WVS.2 | len: 8 | use: O | rpt: 1
        ---
        This component identifies the second input for the waveform source if a differential input is used.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/WVS.2
        """
        self._c_data[1] = (st,)
