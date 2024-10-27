from __future__ import annotations
from ...base import DataType
from .NM import NM
from .ST import ST


"""
DataType - WVI
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::WVI TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    WVI,
    NM, ST
)

wvi = WVI(  # Channel Identifier - This data type specifies the number and name of the recording channel where waveform data is transmitted
    channel_number=nm,  # NM(...)  # Required.
    channel_name=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::WVI TEMPLATE-----
"""


class WVI(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 22
    _hl7_id = """WVI"""
    _hl7_name = """Channel Identifier"""
    _hl7_description = """This data type specifies the number and name of the recording channel where waveform data is transmitted"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/WVI"
    _c_length = (4, 17,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "O",)
    _c_aliases = ("WVI.1", "WVI.2",)
    _c_components = (NM, ST,)
    _c_names = ("Channel Number", "Channel Name",)
    _c_attrs = ("channel_number", "channel_name",)
    # fmt: on

    def __init__(
        self,
        channel_number: NM,  # WVI.1
        channel_name: ST | None = None,  # WVI.2
    ):
        """
        Channel Identifier - `WVI <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/WVI>`_
        This data type specifies the number and name of the recording channel where waveform data is transmitted.

        :param channel_number: This component specifies the number of the recording channel (id: WVI.1 | len: 4 | use: R | rpt: 1)
        :param channel_name: This component specifies the name of the recording channel (id: WVI.2 | len: 17 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.channel_number = channel_number
        self.channel_name = channel_name

    @property  # get WVI.1
    def channel_number(self) -> NM:
        """
        id: WVI.1 | len: 4 | use: R | rpt: 1
        ---
        This component specifies the number of the recording channel.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/WVI.1
        """
        return self._c_data[0][0]

    @channel_number.setter  # set WVI.1
    def channel_number(self, nm: NM):
        """
        id: WVI.1 | len: 4 | use: R | rpt: 1
        ---
        This component specifies the number of the recording channel.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/WVI.1
        """
        self._c_data[0] = (nm,)

    @property  # get WVI.2
    def channel_name(self) -> ST | None:
        """
        id: WVI.2 | len: 17 | use: O | rpt: 1
        ---
        This component specifies the name of the recording channel.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/WVI.2
        """
        return self._c_data[1][0]

    @channel_name.setter  # set WVI.2
    def channel_name(self, st: ST | None):
        """
        id: WVI.2 | len: 17 | use: O | rpt: 1
        ---
        This component specifies the name of the recording channel.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/WVI.2
        """
        self._c_data[1] = (st,)
