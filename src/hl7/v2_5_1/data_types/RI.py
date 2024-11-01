from __future__ import annotations
from ...base import DataType
from .ST import ST
from .IS import IS
from ..tables.RepeatPattern import RepeatPattern


"""
DataType - RI
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::RI TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RI,
    ST, IS
)

ri = RI(  # Repeat Interval - contains the interval between repeated services
    repeat_pattern=None,  # IS(...) 
    explicit_time_interval=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::RI TEMPLATE-----
"""


class RI(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 206
    _hl7_id = """RI"""
    _hl7_name = """Repeat Interval"""
    _hl7_description = """contains the interval between repeated services"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RI"
    _c_length = (6, 199,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_aliases = ("RI.1", "RI.2",)
    _c_components = (IS, ST,)
    _c_names = ("Repeat Pattern", "Explicit Time Interval",)
    _c_attrs = ("repeat_pattern", "explicit_time_interval",)
    # fmt: on

    def __init__(
        self,
        repeat_pattern: RepeatPattern
        | IS
        | tuple[RepeatPattern | IS, ...]
        | None = None,  # RI.1
        explicit_time_interval: ST | tuple[ST, ...] | None = None,  # RI.2
    ):
        """
        Repeat Interval - `RI <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RI>`_
        contains the interval between repeated services.

        :param repeat_pattern: The repeating frequency with which the treatment is to be administered (id: RI.1 | len: 6 | use: O | rpt: 1)
        :param explicit_time_interval: This component explicitly lists the actual times referenced by the code in the first component, in the following format: HHMM,HHMM,HHMM, (id: RI.2 | len: 199 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.repeat_pattern = repeat_pattern
        self.explicit_time_interval = explicit_time_interval

    @property  # get RI.1
    def repeat_pattern(self) -> RepeatPattern | None:
        """
        id: RI.1 | len: 6 | use: O | rpt: 1
        ---
        The repeating frequency with which the treatment is to be administered. It is similar to the frequency and SIG code tables used in order entry systems.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RI.1
        """
        return self._c_data[0][0]

    @repeat_pattern.setter  # set RI.1
    def repeat_pattern(self, repeat_pattern: RepeatPattern | None):
        """
        id: RI.1 | len: 6 | use: O | rpt: 1
        ---
        The repeating frequency with which the treatment is to be administered. It is similar to the frequency and SIG code tables used in order entry systems.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RI.1
        """
        self._c_data[0] = (repeat_pattern,)

    @property  # get RI.2
    def explicit_time_interval(self) -> ST | None:
        """
        id: RI.2 | len: 199 | use: O | rpt: 1
        ---
        This component explicitly lists the actual times referenced by the code in the first component, in the following format: HHMM,HHMM,HHMM,. This second component will be used to clarify the first component in cases where the actual times vary within an institution. If the time of the order spans more than a single day, this new component is only practical if the same times of administration occur for each day of the order. If the actual start time of the order (as given by the fourth component of the quantity/timing field) is after the first explicit time, the first administration is taken to be the first explicit time after the start time. In the case where the patient moves to a location having a different set of explicit times, the existing order may be updated with a new quantity/timing field showing the changed explicit times.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RI.2
        """
        return self._c_data[1][0]

    @explicit_time_interval.setter  # set RI.2
    def explicit_time_interval(self, st: ST | None):
        """
        id: RI.2 | len: 199 | use: O | rpt: 1
        ---
        This component explicitly lists the actual times referenced by the code in the first component, in the following format: HHMM,HHMM,HHMM,. This second component will be used to clarify the first component in cases where the actual times vary within an institution. If the time of the order spans more than a single day, this new component is only practical if the same times of administration occur for each day of the order. If the actual start time of the order (as given by the fourth component of the quantity/timing field) is after the first explicit time, the first administration is taken to be the first explicit time after the start time. In the case where the patient moves to a location having a different set of explicit times, the existing order may be updated with a new quantity/timing field showing the changed explicit times.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RI.2
        """
        self._c_data[1] = (st,)
