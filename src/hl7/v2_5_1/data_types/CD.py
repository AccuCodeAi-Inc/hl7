from __future__ import annotations
from ...base import DataType
from .CSU import CSU
from .NR import NR
from .WVS import WVS
from .NM import NM
from .CCP import CCP
from .WVI import WVI


"""
DataType - CD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CD,
    CSU, NR, WVS, NM, CCP, WVI
)

cd = CD(  # Channel Definition - This data type is used for labeling of digital waveform data
    channel_identifier=None,  # WVI(...) 
    waveform_source=None,  # WVS(...) 
    channel_sensitivity_or_units=None,  # CSU(...) 
    channel_calibration_parameters=None,  # CCP(...) 
    channel_sampling_frequency=None,  # NM(...) 
    minimum_or_maximum_data_values=None,  # NR(...) 
)

-----END COMPOSITE_DATA_TYPE::CD TEMPLATE-----
"""


class CD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 581
    _hl7_id = """CD"""
    _hl7_name = """Channel Definition"""
    _hl7_description = """This data type is used for labeling of digital waveform data"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD"
    _c_length = (22, 17, 478, 20, 6, 33,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O",)
    _c_aliases = ("CD.1", "CD.2", "CD.3", "CD.4", "CD.5", "CD.6",)
    _c_components = (WVI, WVS, CSU, CCP, NM, NR,)
    _c_names = ("Channel Identifier", "Waveform Source", "Channel Sensitivity/Units", "Channel Calibration Parameters", "Channel Sampling Frequency", "Minimum/Maximum Data Values",)
    _c_attrs = ("channel_identifier", "waveform_source", "channel_sensitivity_or_units", "channel_calibration_parameters", "channel_sampling_frequency", "minimum_or_maximum_data_values",)
    # fmt: on

    def __init__(
        self,
        channel_identifier: WVI | None = None,  # CD.1
        waveform_source: WVS | None = None,  # CD.2
        channel_sensitivity_or_units: CSU | None = None,  # CD.3
        channel_calibration_parameters: CCP | None = None,  # CD.4
        channel_sampling_frequency: NM | None = None,  # CD.5
        minimum_or_maximum_data_values: NR | None = None,  # CD.6
    ):
        """
        Channel Definition - `CD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CD>`_
        This data type is used for labeling of digital waveform data. It defines a recording channel, which is associated with one of the values in each time sample of waveform data. Each channel has a number (which generally defines its position in a multichannel display) and an optional name or label (also used in displays). One or two named waveform sources may also be associated with a channel (providing for the use of differential amplifiers with two inputs). The other components of the channel definition data type are optional.

        :param channel_identifier: This component specifies the number and name of the recording channel where waveform data is transmitted (id: CD.1 | len: 22 | use: O | rpt: 1)
        :param waveform_source: This component defines the channel sensitivity (gain) and the units in which it is measured (id: CD.2 | len: 17 | use: O | rpt: 1)
        :param channel_sensitivity_or_units: This component identifies the corrections to channel sensitivity, the baseline, and the channel time skew (id: CD.3 | len: 478 | use: O | rpt: 1)
        :param channel_calibration_parameters: This component defines the sampling frequency in hertz of the channel, that is, the reciprocal of the time in seconds between successive samples (id: CD.4 | len: 20 | use: O | rpt: 1)
        :param channel_sampling_frequency: This component defines the minimum and maximum data values which can occur in this channel in the digital waveform data, that is, the range of the ADC, and also specifies whether or not non-integral data values may occur in this channel in the waveform data (id: CD.5 | len: 6 | use: O | rpt: 1)
        :param minimum_or_maximum_data_values:  (id: CD.6 | len: 33 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.channel_identifier = channel_identifier
        self.waveform_source = waveform_source
        self.channel_sensitivity_or_units = channel_sensitivity_or_units
        self.channel_calibration_parameters = channel_calibration_parameters
        self.channel_sampling_frequency = channel_sampling_frequency
        self.minimum_or_maximum_data_values = minimum_or_maximum_data_values

    @property  # get CD.1
    def channel_identifier(self) -> WVI | None:
        """
        id: CD.1 | len: 22 | use: O | rpt: 1
        ---
        This component specifies the number and name of the recording channel where waveform data is transmitted. Waveform Source (WVS)
        ---
        return_type: WVI: Channel Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.1
        """
        return self._c_data[0][0]

    @channel_identifier.setter  # set CD.1
    def channel_identifier(self, wvi: WVI | None):
        """
        id: CD.1 | len: 22 | use: O | rpt: 1
        ---
        This component specifies the number and name of the recording channel where waveform data is transmitted. Waveform Source (WVS)
        ---
        param_type: WVI: Channel Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.1
        """
        self._c_data[0] = (wvi,)

    @property  # get CD.2
    def waveform_source(self) -> WVS | None:
        """
        id: CD.2 | len: 17 | use: O | rpt: 1
        ---
        This component defines the channel sensitivity (gain) and the units in which it is measured.
        ---
        return_type: WVS: Waveform Source
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.2
        """
        return self._c_data[1][0]

    @waveform_source.setter  # set CD.2
    def waveform_source(self, wvs: WVS | None):
        """
        id: CD.2 | len: 17 | use: O | rpt: 1
        ---
        This component defines the channel sensitivity (gain) and the units in which it is measured.
        ---
        param_type: WVS: Waveform Source
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.2
        """
        self._c_data[1] = (wvs,)

    @property  # get CD.3
    def channel_sensitivity_or_units(self) -> CSU | None:
        """
        id: CD.3 | len: 478 | use: O | rpt: 1
        ---
        This component identifies the corrections to channel sensitivity, the baseline, and the channel time skew.
        ---
        return_type: CSU: Channel Sensitivity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.3
        """
        return self._c_data[2][0]

    @channel_sensitivity_or_units.setter  # set CD.3
    def channel_sensitivity_or_units(self, csu: CSU | None):
        """
        id: CD.3 | len: 478 | use: O | rpt: 1
        ---
        This component identifies the corrections to channel sensitivity, the baseline, and the channel time skew.
        ---
        param_type: CSU: Channel Sensitivity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.3
        """
        self._c_data[2] = (csu,)

    @property  # get CD.4
    def channel_calibration_parameters(self) -> CCP | None:
        """
        id: CD.4 | len: 20 | use: O | rpt: 1
        ---
        This component defines the sampling frequency in hertz of the channel, that is, the reciprocal of the time in seconds between successive samples. Note that this is the frequency of transmitted data, which may or may not be the actual frequency at which the data was acquired by an analog-to-digital converter or other digital data source (i.e. the data transmitted may be subsampled, or interpolated, from the originally acquired data.)
        ---
        return_type: CCP: Channel Calibration Parameters
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.4
        """
        return self._c_data[3][0]

    @channel_calibration_parameters.setter  # set CD.4
    def channel_calibration_parameters(self, ccp: CCP | None):
        """
        id: CD.4 | len: 20 | use: O | rpt: 1
        ---
        This component defines the sampling frequency in hertz of the channel, that is, the reciprocal of the time in seconds between successive samples. Note that this is the frequency of transmitted data, which may or may not be the actual frequency at which the data was acquired by an analog-to-digital converter or other digital data source (i.e. the data transmitted may be subsampled, or interpolated, from the originally acquired data.)
        ---
        param_type: CCP: Channel Calibration Parameters
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.4
        """
        self._c_data[3] = (ccp,)

    @property  # get CD.5
    def channel_sampling_frequency(self) -> NM | None:
        """
        id: CD.5 | len: 6 | use: O | rpt: 1
        ---
        This component defines the minimum and maximum data values which can occur in this channel in the digital waveform data, that is, the range of the ADC, and also specifies whether or not non-integral data values may occur in this channel in the waveform data. If the minimum and maximum values are both integers (or not present), only integral data values may be used in this channel. If either the minimum or the maximum value contains a decimal point, then non-integral as well as integral data values may be used in this channel. For an n-bit signed ADC, the nominal baseline B = 0, and the minimum (L) and maximum (H) values may be calculated as follows:
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.5
        """
        return self._c_data[4][0]

    @channel_sampling_frequency.setter  # set CD.5
    def channel_sampling_frequency(self, nm: NM | None):
        """
        id: CD.5 | len: 6 | use: O | rpt: 1
        ---
        This component defines the minimum and maximum data values which can occur in this channel in the digital waveform data, that is, the range of the ADC, and also specifies whether or not non-integral data values may occur in this channel in the waveform data. If the minimum and maximum values are both integers (or not present), only integral data values may be used in this channel. If either the minimum or the maximum value contains a decimal point, then non-integral as well as integral data values may be used in this channel. For an n-bit signed ADC, the nominal baseline B = 0, and the minimum (L) and maximum (H) values may be calculated as follows:
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.5
        """
        self._c_data[4] = (nm,)

    @property  # get CD.6
    def minimum_or_maximum_data_values(self) -> NR | None:
        """
        id: CD.6 | len: 33 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NR: Numeric Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.6
        """
        return self._c_data[5][0]

    @minimum_or_maximum_data_values.setter  # set CD.6
    def minimum_or_maximum_data_values(self, nr: NR | None):
        """
        id: CD.6 | len: 33 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NR: Numeric Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CD.6
        """
        self._c_data[5] = (nr,)
