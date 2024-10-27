from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS


"""
System Clock - NCK
HL7 Version: 2.5.1

-----BEGIN SEGMENT::NCK TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    NCK,
    TS
)

nck = NCK(  #  - The NCK segment is used to allow the various applications on the network to synchronize their system clocks (system date and time)
    system_date_or_time=ts,  # TS(...)  # Required.
)

-----END SEGMENT::NCK TEMPLATE-----
"""


class NCK(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """NCK"""
    _hl7_name = """System Clock"""
    _hl7_description = """The NCK segment is used to allow the various applications on the network to synchronize their system clocks (system date and time)"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NCK"
    _c_length = (26,)
    _c_rpt = (1,)
    _c_usage = ("R",)
    _c_components = (TS,)
    _c_aliases = ("NCK.1",)
    _c_names = ("System Date/Time",)
    _c_attrs = ("system_date_or_time",)
    # fmt: on

    def __init__(
        self,
        system_date_or_time: TS,  # NCK.1
    ):
        """
        System Clock - `NCK <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NCK>`_
        The NCK segment is used to allow the various applications on the network to synchronize their system clocks (system date and time).

        :param system_date_or_time: Time Stamp (id: NCK.1 | len: 26 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 1
        self.system_date_or_time = system_date_or_time

    @property  # get NCK.1
    def system_date_or_time(self) -> TS:
        """
        id: NCK.1 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NCK.1
        """
        return self._c_data[0][0]

    @system_date_or_time.setter  # set NCK.1
    def system_date_or_time(self, ts: TS):
        """
        id: NCK.1 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NCK.1
        """
        self._c_data[0] = (ts,)
