from __future__ import annotations
from ...base import DataType
from .ID import ID
from .TM import TM
from ..tables.DaysOfTheWeek import DaysOfTheWeek


"""
DataType - VH
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::VH TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    VH,
    ID, TM
)

vh = VH(  # Visiting Hours - This data type contains the hours when a patient location is open for visiting
    start_day_range=None,  # ID(...) 
    end_day_range=None,  # ID(...) 
    start_hour_range=None,  # TM(...) 
    end_hour_range=None,  # TM(...) 
)

-----END COMPOSITE_DATA_TYPE::VH TEMPLATE-----
"""


class VH(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 41
    _hl7_id = """VH"""
    _hl7_name = """Visiting Hours"""
    _hl7_description = """This data type contains the hours when a patient location is open for visiting"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VH"
    _c_length = (3, 3, 16, 16,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O",)
    _c_aliases = ("VH.1", "VH.2", "VH.3", "VH.4",)
    _c_components = (ID, ID, TM, TM,)
    _c_names = ("Start Day Range", "End Day Range", "Start Hour Range", "End Hour Range",)
    _c_attrs = ("start_day_range", "end_day_range", "start_hour_range", "end_hour_range",)
    # fmt: on

    def __init__(
        self,
        start_day_range: DaysOfTheWeek | ID | None = None,  # VH.1
        end_day_range: DaysOfTheWeek | ID | None = None,  # VH.2
        start_hour_range: TM | None = None,  # VH.3
        end_hour_range: TM | None = None,  # VH.4
    ):
        """
        Visiting Hours - `VH <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VH>`_
        This data type contains the hours when a patient location is open for visiting. Refer to HL7 Table 0267 - Days of the week for valid values for the first two components.

        :param start_day_range: Starting day of visiting hours range (id: VH.1 | len: 3 | use: O | rpt: 1)
        :param end_day_range: Ending day of visiting hours range (id: VH.2 | len: 3 | use: O | rpt: 1)
        :param start_hour_range: Starting hour on starting day of visiting hours range (id: VH.3 | len: 16 | use: O | rpt: 1)
        :param end_hour_range: Ending hour on ending day of visiting hours range See second component, 2 (id: VH.4 | len: 16 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.start_day_range = start_day_range
        self.end_day_range = end_day_range
        self.start_hour_range = start_hour_range
        self.end_hour_range = end_hour_range

    @property  # get VH.1
    def start_day_range(self) -> DaysOfTheWeek | None:
        """
        id: VH.1 | len: 3 | use: O | rpt: 1
        ---
        Starting day of visiting hours range. See HL7 Table 0267 - Days of the week for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VH.1
        """
        return self._c_data[0][0]

    @start_day_range.setter  # set VH.1
    def start_day_range(self, days_of_the_week: DaysOfTheWeek | None):
        """
        id: VH.1 | len: 3 | use: O | rpt: 1
        ---
        Starting day of visiting hours range. See HL7 Table 0267 - Days of the week for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VH.1
        """
        self._c_data[0] = (days_of_the_week,)

    @property  # get VH.2
    def end_day_range(self) -> DaysOfTheWeek | None:
        """
        id: VH.2 | len: 3 | use: O | rpt: 1
        ---
        Ending day of visiting hours range. Starting day of visiting hours range. See HL7 Table 0267 - Days of the week for valid values
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VH.2
        """
        return self._c_data[1][0]

    @end_day_range.setter  # set VH.2
    def end_day_range(self, days_of_the_week: DaysOfTheWeek | None):
        """
        id: VH.2 | len: 3 | use: O | rpt: 1
        ---
        Ending day of visiting hours range. Starting day of visiting hours range. See HL7 Table 0267 - Days of the week for valid values
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VH.2
        """
        self._c_data[1] = (days_of_the_week,)

    @property  # get VH.3
    def start_hour_range(self) -> TM | None:
        """
        id: VH.3 | len: 16 | use: O | rpt: 1
        ---
        Starting hour on starting day of visiting hours range. See first component, 2.A.80.1, "Start Day Range (ID)".
        ---
        return_type: TM: Time
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VH.3
        """
        return self._c_data[2][0]

    @start_hour_range.setter  # set VH.3
    def start_hour_range(self, tm: TM | None):
        """
        id: VH.3 | len: 16 | use: O | rpt: 1
        ---
        Starting hour on starting day of visiting hours range. See first component, 2.A.80.1, "Start Day Range (ID)".
        ---
        param_type: TM: Time
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VH.3
        """
        self._c_data[2] = (tm,)

    @property  # get VH.4
    def end_hour_range(self) -> TM | None:
        """
        id: VH.4 | len: 16 | use: O | rpt: 1
        ---
        Ending hour on ending day of visiting hours range See second component, 2.A.80.2, "End Day Range (ID)".
        ---
        return_type: TM: Time
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VH.4
        """
        return self._c_data[3][0]

    @end_hour_range.setter  # set VH.4
    def end_hour_range(self, tm: TM | None):
        """
        id: VH.4 | len: 16 | use: O | rpt: 1
        ---
        Ending hour on ending day of visiting hours range See second component, 2.A.80.2, "End Day Range (ID)".
        ---
        param_type: TM: Time
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VH.4
        """
        self._c_data[3] = (tm,)
