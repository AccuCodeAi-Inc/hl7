from __future__ import annotations
from ...base import DataType
from .ID import ID
from .TS import TS
from ..tables.InvocationEvent import InvocationEvent


"""
DataType - CCD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CCD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CCD,
    ID, TS
)

ccd = CCD(  # Charge Code and Date - Specifies whether a charge action is based on an invocation event or is time-based
    invocation_event=id,  # ID(...)  # Required.
    date_or_time=None,  # TS(...) 
)

-----END COMPOSITE_DATA_TYPE::CCD TEMPLATE-----
"""


class CCD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 28
    _hl7_id = """CCD"""
    _hl7_name = """Charge Code and Date"""
    _hl7_description = """Specifies whether a charge action is based on an invocation event or is time-based"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCD"
    _c_length = (1, 26,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "O",)
    _c_aliases = ("CCD.1", "CCD.2",)
    _c_components = (ID, TS,)
    _c_names = ("Invocation Event", "Date/Time",)
    _c_attrs = ("invocation_event", "date_or_time",)
    # fmt: on

    def __init__(
        self,
        invocation_event: InvocationEvent | ID | tuple[InvocationEvent | ID],  # CCD.1
        date_or_time: TS | tuple[TS] | None = None,  # CCD.2
    ):
        """
        Charge Code and Date - `CCD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CCD>`_
        Specifies whether a charge action is based on an invocation event or is time-based.

        :param invocation_event: Specifies the code for the event precipitating/triggering the charge activity (id: CCD.1 | len: 1 | use: R | rpt: 1)
        :param date_or_time: The second component is used to express the exact time to charge for the ordered service; it is used only when the CCD (id: CCD.2 | len: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.invocation_event = invocation_event
        self.date_or_time = date_or_time

    @property  # get CCD.1
    def invocation_event(self) -> InvocationEvent:
        """
        id: CCD.1 | len: 1 | use: R | rpt: 1
        ---
        Specifies the code for the event precipitating/triggering the charge activity. Refer to HL7 Table 0100 - Invocation event for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCD.1
        """
        return self._c_data[0][0]

    @invocation_event.setter  # set CCD.1
    def invocation_event(self, invocation_event: InvocationEvent):
        """
        id: CCD.1 | len: 1 | use: R | rpt: 1
        ---
        Specifies the code for the event precipitating/triggering the charge activity. Refer to HL7 Table 0100 - Invocation event for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCD.1
        """
        self._c_data[0] = (invocation_event,)

    @property  # get CCD.2
    def date_or_time(self) -> TS | None:
        """
        id: CCD.2 | len: 26 | use: O | rpt: 1
        ---
        The second component is used to express the exact time to charge for the ordered service; it is used only when the CCD.1 value is T. When used, it is expressed as a TS data type.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCD.2
        """
        return self._c_data[1][0]

    @date_or_time.setter  # set CCD.2
    def date_or_time(self, ts: TS | None):
        """
        id: CCD.2 | len: 26 | use: O | rpt: 1
        ---
        The second component is used to express the exact time to charge for the ordered service; it is used only when the CCD.1 value is T. When used, it is expressed as a TS data type.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CCD.2
        """
        self._c_data[1] = (ts,)
