from __future__ import annotations
from ...base import DataType
from .TS import TS


"""
DataType - DR
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::DR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DR,
    TS
)

dr = DR(  # Date/Time Range - Note: DR cannot be legally expressed when embedded within another data type
    range_start_date_or_time=None,  # TS(...) 
    range_end_date_or_time=None,  # TS(...) 
)

-----END COMPOSITE_DATA_TYPE::DR TEMPLATE-----
"""


class DR(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 53
    _hl7_id = """DR"""
    _hl7_name = """Date/Time Range"""
    _hl7_description = """Note: DR cannot be legally expressed when embedded within another data type"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DR"
    _c_length = (26, 26,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_aliases = ("DR.1", "DR.2",)
    _c_components = (TS, TS,)
    _c_names = ("Range Start Date/Time", "Range End Date/Time",)
    _c_attrs = ("range_start_date_or_time", "range_end_date_or_time",)
    # fmt: on

    def __init__(
        self,
        range_start_date_or_time: TS | None = None,  # DR.1
        range_end_date_or_time: TS | None = None,  # DR.2
    ):
        """
        Date/Time Range - `DR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DR>`_
        Note: DR cannot be legally expressed when embedded within another data type. Its use is constrained to a segment field.

        :param range_start_date_or_time: The first component contains the earliest date/time (time stamp) in the specified range (id: DR.1 | len: 26 | use: O | rpt: 1)
        :param range_end_date_or_time: The second component contains the latest date/time in the specified range (id: DR.2 | len: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.range_start_date_or_time = range_start_date_or_time
        self.range_end_date_or_time = range_end_date_or_time

    @property  # get DR.1
    def range_start_date_or_time(self) -> TS | None:
        """
        id: DR.1 | len: 26 | use: O | rpt: 1
        ---
        The first component contains the earliest date/time (time stamp) in the specified range.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DR.1
        """
        return self._c_data[0][0]

    @range_start_date_or_time.setter  # set DR.1
    def range_start_date_or_time(self, ts: TS | None):
        """
        id: DR.1 | len: 26 | use: O | rpt: 1
        ---
        The first component contains the earliest date/time (time stamp) in the specified range.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DR.1
        """
        self._c_data[0] = (ts,)

    @property  # get DR.2
    def range_end_date_or_time(self) -> TS | None:
        """
        id: DR.2 | len: 26 | use: O | rpt: 1
        ---
        The second component contains the latest date/time in the specified range. Note that the TS (time stamp) data type allows the specification of precision.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DR.2
        """
        return self._c_data[1][0]

    @range_end_date_or_time.setter  # set DR.2
    def range_end_date_or_time(self, ts: TS | None):
        """
        id: DR.2 | len: 26 | use: O | rpt: 1
        ---
        The second component contains the latest date/time in the specified range. Note that the TS (time stamp) data type allows the specification of precision.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DR.2
        """
        self._c_data[1] = (ts,)
