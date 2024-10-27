from __future__ import annotations
from ...base import DataType
from .NM import NM


"""
DataType - MA
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::MA TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MA,
    NM
)

ma = MA(  # Multiplexed Array - This data type is used to represent channel-multiplexed waveform data, (e
    sample_1_from_channel_1=None,  # NM(...) 
    sample_1_from_channel_2=None,  # NM(...) 
    sample_1_from_channel_n=None,  # NM(...) 
    sample_2_from_channel_1=None,  # NM(...) 
    sample_2_from_channel_n=None,  # NM(...) 
    sample_n_from_channel_n=None,  # NM(...) 
)

-----END COMPOSITE_DATA_TYPE::MA TEMPLATE-----
"""


class MA(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 65536
    _hl7_id = """MA"""
    _hl7_name = """Multiplexed Array"""
    _hl7_description = """This data type is used to represent channel-multiplexed waveform data, (e"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA"
    _c_length = (16, 16, 16, 16, 16, 16,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O",)
    _c_aliases = ("MA.1", "MA.2", "MA.3", "MA.4", "MA.5", "MA.6",)
    _c_components = (NM, NM, NM, NM, NM, NM,)
    _c_names = ("Sample 1 From Channel 1", "Sample 1 From Channel 2", "Sample 1 From Channel N", "Sample 2 From Channel 1", "Sample 2 From Channel N", "Sample N From Channel N",)
    _c_attrs = ("sample_1_from_channel_1", "sample_1_from_channel_2", "sample_1_from_channel_n", "sample_2_from_channel_1", "sample_2_from_channel_n", "sample_n_from_channel_n",)
    # fmt: on

    def __init__(
        self,
        sample_1_from_channel_1: NM | None = None,  # MA.1
        sample_1_from_channel_2: NM | None = None,  # MA.2
        sample_1_from_channel_n: NM | None = None,  # MA.3
        sample_2_from_channel_1: NM | None = None,  # MA.4
        sample_2_from_channel_n: NM | None = None,  # MA.5
        sample_n_from_channel_n: NM | None = None,  # MA.6
    ):
        """
                Multiplexed Array - `MA <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MA>`_
                This data type is used to represent channel-multiplexed waveform data, (e.g., the digitized values from an analog-to-digital converter or other digital data source). Each value is of type NM, and represents a time sample from a channel. This segment may contain data from one or more channels. The waveform data is in channel-multiplexed format (that is, the values for all channels for the first time sample are transmitted, then the values for the next time sample, and so on until the requisite number of time samples have been transmitted). Time samples are separated by repeat delimiters (~), and channels within a sample are separated by component delimiters (^). The time between samples (the sampling interval) is the reciprocal of the digitization frequency as specified using the CD data type.

        Example 1: 3 channels (identical), 6 time-samples |0^0^0~1^1^1~2^2^2~3^3^3~4^4^4~5^5^5|
        Example 2: 1 channel, 11 time-samples |0~1~2~3~4~5~6~7~8~9~10|

                :param sample_1_from_channel_1:  (id: MA.1 | len: 16 | use: O | rpt: 1)
                :param sample_1_from_channel_2:  (id: MA.2 | len: 16 | use: O | rpt: 1)
                :param sample_1_from_channel_n:  (id: MA.3 | len: 16 | use: O | rpt: 1)
                :param sample_2_from_channel_1:  (id: MA.4 | len: 16 | use: O | rpt: 1)
                :param sample_2_from_channel_n:  (id: MA.5 | len: 16 | use: O | rpt: 1)
                :param sample_n_from_channel_n:  (id: MA.6 | len: 16 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.sample_1_from_channel_1 = sample_1_from_channel_1
        self.sample_1_from_channel_2 = sample_1_from_channel_2
        self.sample_1_from_channel_n = sample_1_from_channel_n
        self.sample_2_from_channel_1 = sample_2_from_channel_1
        self.sample_2_from_channel_n = sample_2_from_channel_n
        self.sample_n_from_channel_n = sample_n_from_channel_n

    @property  # get MA.1
    def sample_1_from_channel_1(self) -> NM | None:
        """
        id: MA.1 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.1
        """
        return self._c_data[0][0]

    @sample_1_from_channel_1.setter  # set MA.1
    def sample_1_from_channel_1(self, nm: NM | None):
        """
        id: MA.1 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.1
        """
        self._c_data[0] = (nm,)

    @property  # get MA.2
    def sample_1_from_channel_2(self) -> NM | None:
        """
        id: MA.2 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.2
        """
        return self._c_data[1][0]

    @sample_1_from_channel_2.setter  # set MA.2
    def sample_1_from_channel_2(self, nm: NM | None):
        """
        id: MA.2 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.2
        """
        self._c_data[1] = (nm,)

    @property  # get MA.3
    def sample_1_from_channel_n(self) -> NM | None:
        """
        id: MA.3 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.3
        """
        return self._c_data[2][0]

    @sample_1_from_channel_n.setter  # set MA.3
    def sample_1_from_channel_n(self, nm: NM | None):
        """
        id: MA.3 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.3
        """
        self._c_data[2] = (nm,)

    @property  # get MA.4
    def sample_2_from_channel_1(self) -> NM | None:
        """
        id: MA.4 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.4
        """
        return self._c_data[3][0]

    @sample_2_from_channel_1.setter  # set MA.4
    def sample_2_from_channel_1(self, nm: NM | None):
        """
        id: MA.4 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.4
        """
        self._c_data[3] = (nm,)

    @property  # get MA.5
    def sample_2_from_channel_n(self) -> NM | None:
        """
        id: MA.5 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.5
        """
        return self._c_data[4][0]

    @sample_2_from_channel_n.setter  # set MA.5
    def sample_2_from_channel_n(self, nm: NM | None):
        """
        id: MA.5 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.5
        """
        self._c_data[4] = (nm,)

    @property  # get MA.6
    def sample_n_from_channel_n(self) -> NM | None:
        """
        id: MA.6 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.6
        """
        return self._c_data[5][0]

    @sample_n_from_channel_n.setter  # set MA.6
    def sample_n_from_channel_n(self, nm: NM | None):
        """
        id: MA.6 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MA.6
        """
        self._c_data[5] = (nm,)
