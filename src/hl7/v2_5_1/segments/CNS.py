from __future__ import annotations
from ...base import HL7Segment
from ..data_types.NM import NM
from ..data_types.CE import CE
from ..data_types.TS import TS


"""
Clear Notification - CNS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CNS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CNS,
    NM, CE, TS
)

cns = CNS(  #  - The clear equipment notification segment contains the data necessary to allow the receiving equipment to clear any associated notifications
    starting_notification_reference_number=None,  # NM(...) 
    ending_notification_reference_number=None,  # NM(...) 
    starting_notification_date_or_time=None,  # TS(...) 
    ending_notification_date_or_time=None,  # TS(...) 
    starting_notification_code=None,  # CE(...) 
    ending_notification_code=None,  # CE(...) 
)

-----END SEGMENT::CNS TEMPLATE-----
"""


class CNS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CNS"""
    _hl7_name = """Clear Notification"""
    _hl7_description = """The clear equipment notification segment contains the data necessary to allow the receiving equipment to clear any associated notifications"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CNS"
    _c_length = (20, 20, 26, 26, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O",)
    _c_components = (NM, NM, TS, TS, CE, CE,)
    _c_aliases = ("CNS.1", "CNS.2", "CNS.3", "CNS.4", "CNS.5", "CNS.6",)
    _c_names = ("Starting Notification Reference Number", "Ending Notification Reference Number", "Starting Notification Date/Time", "Ending Notification Date/Time", "Starting Notification Code", "Ending Notification Code",)
    _c_attrs = ("starting_notification_reference_number", "ending_notification_reference_number", "starting_notification_date_or_time", "ending_notification_date_or_time", "starting_notification_code", "ending_notification_code",)
    # fmt: on

    def __init__(
        self,
        starting_notification_reference_number: NM | tuple[NM] | None = None,  # CNS.1
        ending_notification_reference_number: NM | tuple[NM] | None = None,  # CNS.2
        starting_notification_date_or_time: TS | tuple[TS] | None = None,  # CNS.3
        ending_notification_date_or_time: TS | tuple[TS] | None = None,  # CNS.4
        starting_notification_code: CE | tuple[CE] | None = None,  # CNS.5
        ending_notification_code: CE | tuple[CE] | None = None,  # CNS.6
    ):
        """
        Clear Notification - `CNS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CNS>`_
        The clear equipment notification segment contains the data necessary to allow the receiving equipment to clear any associated notifications.

        :param starting_notification_reference_number: Numeric (id: CNS.1 | len: 20 | use: O | rpt: 1)
        :param ending_notification_reference_number: Numeric (id: CNS.2 | len: 20 | use: O | rpt: 1)
        :param starting_notification_date_or_time: Time Stamp (id: CNS.3 | len: 26 | use: O | rpt: 1)
        :param ending_notification_date_or_time: Time Stamp (id: CNS.4 | len: 26 | use: O | rpt: 1)
        :param starting_notification_code: Coded Element (id: CNS.5 | len: 250 | use: O | rpt: 1)
        :param ending_notification_code: Coded Element (id: CNS.6 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.starting_notification_reference_number = (
            starting_notification_reference_number
        )
        self.ending_notification_reference_number = ending_notification_reference_number
        self.starting_notification_date_or_time = starting_notification_date_or_time
        self.ending_notification_date_or_time = ending_notification_date_or_time
        self.starting_notification_code = starting_notification_code
        self.ending_notification_code = ending_notification_code

    @property  # get CNS.1
    def starting_notification_reference_number(self) -> NM | None:
        """
        id: CNS.1 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.1
        """
        return self._c_data[0][0]

    @starting_notification_reference_number.setter  # set CNS.1
    def starting_notification_reference_number(self, nm: NM | None):
        """
        id: CNS.1 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.1
        """
        self._c_data[0] = (nm,)

    @property  # get CNS.2
    def ending_notification_reference_number(self) -> NM | None:
        """
        id: CNS.2 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.2
        """
        return self._c_data[1][0]

    @ending_notification_reference_number.setter  # set CNS.2
    def ending_notification_reference_number(self, nm: NM | None):
        """
        id: CNS.2 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.2
        """
        self._c_data[1] = (nm,)

    @property  # get CNS.3
    def starting_notification_date_or_time(self) -> TS | None:
        """
        id: CNS.3 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.3
        """
        return self._c_data[2][0]

    @starting_notification_date_or_time.setter  # set CNS.3
    def starting_notification_date_or_time(self, ts: TS | None):
        """
        id: CNS.3 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.3
        """
        self._c_data[2] = (ts,)

    @property  # get CNS.4
    def ending_notification_date_or_time(self) -> TS | None:
        """
        id: CNS.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.4
        """
        return self._c_data[3][0]

    @ending_notification_date_or_time.setter  # set CNS.4
    def ending_notification_date_or_time(self, ts: TS | None):
        """
        id: CNS.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.4
        """
        self._c_data[3] = (ts,)

    @property  # get CNS.5
    def starting_notification_code(self) -> CE | None:
        """
        id: CNS.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.5
        """
        return self._c_data[4][0]

    @starting_notification_code.setter  # set CNS.5
    def starting_notification_code(self, ce: CE | None):
        """
        id: CNS.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.5
        """
        self._c_data[4] = (ce,)

    @property  # get CNS.6
    def ending_notification_code(self) -> CE | None:
        """
        id: CNS.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.6
        """
        return self._c_data[5][0]

    @ending_notification_code.setter  # set CNS.6
    def ending_notification_code(self, ce: CE | None):
        """
        id: CNS.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNS.6
        """
        self._c_data[5] = (ce,)
