from __future__ import annotations
from ...base import DataType
from .NM import NM


"""
DataType - CCP
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CCP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CCP,
    NM
)

ccp = CCP(  # Channel Calibration Parameters - This data type identifies the corrections to channel sensitivity, the baseline, and the channel time skew when transmitting waveform results
    channel_calibration_sensitivity_correction_factor=None,  # NM(...) 
    channel_calibration_baseline=None,  # NM(...) 
    channel_calibration_time_skew=None,  # NM(...) 
)

-----END COMPOSITE_DATA_TYPE::CCP TEMPLATE-----
"""


class CCP(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 20
    _hl7_id = """CCP"""
    _hl7_name = """Channel Calibration Parameters"""
    _hl7_description = """This data type identifies the corrections to channel sensitivity, the baseline, and the channel time skew when transmitting waveform results"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCP"
    _c_length = (6, 6, 6,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("O", "O", "O",)
    _c_aliases = ("CCP.1", "CCP.2", "CCP.3",)
    _c_components = (NM, NM, NM,)
    _c_names = ("Channel Calibration Sensitivity Correction Factor", "Channel Calibration Baseline", "Channel Calibration Time Skew",)
    _c_attrs = ("channel_calibration_sensitivity_correction_factor", "channel_calibration_baseline", "channel_calibration_time_skew",)
    # fmt: on

    def __init__(
        self,
        channel_calibration_sensitivity_correction_factor: NM | None = None,  # CCP.1
        channel_calibration_baseline: NM | None = None,  # CCP.2
        channel_calibration_time_skew: NM | None = None,  # CCP.3
    ):
        """
        Channel Calibration Parameters - `CCP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CCP>`_
        This data type identifies the corrections to channel sensitivity, the baseline, and the channel time skew when transmitting waveform results.

        :param channel_calibration_sensitivity_correction_factor: This component defines a correction factor for channel sensitivity, which may be derived from the last calibration procedure performed (id: CCP.1 | len: 6 | use: O | rpt: 1)
        :param channel_calibration_baseline: This component defines the actual channel baseline (the data value which corresponds to a nominal input signal of zero) (id: CCP.2 | len: 6 | use: O | rpt: 1)
        :param channel_calibration_time_skew: This component defines the time difference between the nominal sampling (digitization) time (which would be the same for all channels) and the actual sampling time of the channel, in seconds (or fractions thereof) (id: CCP.3 | len: 6 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.channel_calibration_sensitivity_correction_factor = (
            channel_calibration_sensitivity_correction_factor
        )
        self.channel_calibration_baseline = channel_calibration_baseline
        self.channel_calibration_time_skew = channel_calibration_time_skew

    @property  # get CCP.1
    def channel_calibration_sensitivity_correction_factor(self) -> NM | None:
        """
        id: CCP.1 | len: 6 | use: O | rpt: 1
        ---
        This component defines a correction factor for channel sensitivity, which may be derived from the last calibration procedure performed. The actual channel sensitivity is the nominal channel sensitivity given in the previous component multiplied by the unitless correction factor.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCP.1
        """
        return self._c_data[0][0]

    @channel_calibration_sensitivity_correction_factor.setter  # set CCP.1
    def channel_calibration_sensitivity_correction_factor(self, nm: NM | None):
        """
        id: CCP.1 | len: 6 | use: O | rpt: 1
        ---
        This component defines a correction factor for channel sensitivity, which may be derived from the last calibration procedure performed. The actual channel sensitivity is the nominal channel sensitivity given in the previous component multiplied by the unitless correction factor.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCP.1
        """
        self._c_data[0] = (nm,)

    @property  # get CCP.2
    def channel_calibration_baseline(self) -> NM | None:
        """
        id: CCP.2 | len: 6 | use: O | rpt: 1
        ---
        This component defines the actual channel baseline (the data value which corresponds to a nominal input signal of zero). The actual baseline may differ from the ideal because of a dc offset in the amplifier connected to the ADC. The actual baseline values for all channels (which need not be integers) may be determined at the time of calibration as the average digitized values obtained when a zero input signal is connected to each channel.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCP.2
        """
        return self._c_data[1][0]

    @channel_calibration_baseline.setter  # set CCP.2
    def channel_calibration_baseline(self, nm: NM | None):
        """
        id: CCP.2 | len: 6 | use: O | rpt: 1
        ---
        This component defines the actual channel baseline (the data value which corresponds to a nominal input signal of zero). The actual baseline may differ from the ideal because of a dc offset in the amplifier connected to the ADC. The actual baseline values for all channels (which need not be integers) may be determined at the time of calibration as the average digitized values obtained when a zero input signal is connected to each channel.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCP.2
        """
        self._c_data[1] = (nm,)

    @property  # get CCP.3
    def channel_calibration_time_skew(self) -> NM | None:
        """
        id: CCP.3 | len: 6 | use: O | rpt: 1
        ---
        This component defines the time difference between the nominal sampling (digitization) time (which would be the same for all channels) and the actual sampling time of the channel, in seconds (or fractions thereof). This value will differ from zero when all channels in the montage are not sampled simultaneously, as occurs in systems, which sample successive channels at regular time intervals. This value may be determined from a calibration procedure in which an identical time-varying signal is applied to all channels and interchannel time differences are estimated, or more commonly it may be taken from the manufacturers specifications for the digitizing system used. For example, for a system which samples successive channels at regular time intervals t, the time skew of channel number n would be (n-1)t. The actual time of sampling (digitization) of sample number m of channel number n in such a system would be R + (m-1)/f + (n-1)t, where R is the reference time at the start of the epoch and f is the channel sampling frequency (t < 1/f).
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCP.3
        """
        return self._c_data[2][0]

    @channel_calibration_time_skew.setter  # set CCP.3
    def channel_calibration_time_skew(self, nm: NM | None):
        """
        id: CCP.3 | len: 6 | use: O | rpt: 1
        ---
        This component defines the time difference between the nominal sampling (digitization) time (which would be the same for all channels) and the actual sampling time of the channel, in seconds (or fractions thereof). This value will differ from zero when all channels in the montage are not sampled simultaneously, as occurs in systems, which sample successive channels at regular time intervals. This value may be determined from a calibration procedure in which an identical time-varying signal is applied to all channels and interchannel time differences are estimated, or more commonly it may be taken from the manufacturers specifications for the digitizing system used. For example, for a system which samples successive channels at regular time intervals t, the time skew of channel number n would be (n-1)t. The actual time of sampling (digitization) of sample number m of channel number n in such a system would be R + (m-1)/f + (n-1)t, where R is the reference time at the start of the epoch and f is the channel sampling frequency (t < 1/f).
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCP.3
        """
        self._c_data[2] = (nm,)
