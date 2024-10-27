from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.NM import NM
from ..data_types.CE import CE
from ..tables.AlertLevel import AlertLevel


"""
Notification Detail - NDS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::NDS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    NDS,
    TS, NM, CE
)

nds = NDS(  #  - The equipment notification detail segment is the data necessary to maintain an adequate audit trail as well as notifications of events, (e
    notification_reference_number=nm,  # NM(...)  # Required.
    notification_date_or_time=ts,  # TS(...)  # Required.
    notification_alert_severity=ce,  # CE(...)  # Required.
    notification_code=ce,  # CE(...)  # Required.
)

-----END SEGMENT::NDS TEMPLATE-----
"""


class NDS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """NDS"""
    _hl7_name = """Notification Detail"""
    _hl7_description = """The equipment notification detail segment is the data necessary to maintain an adequate audit trail as well as notifications of events, (e"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NDS"
    _c_length = (20, 26, 250, 250,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("R", "R", "R", "R",)
    _c_components = (NM, TS, CE, CE,)
    _c_aliases = ("NDS.1", "NDS.2", "NDS.3", "NDS.4",)
    _c_names = ("Notification Reference Number", "Notification Date/Time", "Notification Alert Severity", "Notification Code",)
    _c_attrs = ("notification_reference_number", "notification_date_or_time", "notification_alert_severity", "notification_code",)
    # fmt: on

    def __init__(
        self,
        notification_reference_number: NM,  # NDS.1
        notification_date_or_time: TS,  # NDS.2
        notification_alert_severity: AlertLevel | CE,  # NDS.3
        notification_code: CE,  # NDS.4
    ):
        """
        Notification Detail - `NDS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NDS>`_
        The equipment notification detail segment is the data necessary to maintain an adequate audit trail as well as notifications of events, (e.g., alarms that have occurred on a particular piece of equipment.

        :param notification_reference_number: Numeric (id: NDS.1 | len: 20 | use: R | rpt: 1)
        :param notification_date_or_time: Time Stamp (id: NDS.2 | len: 26 | use: R | rpt: 1)
        :param notification_alert_severity: Coded Element (id: NDS.3 | len: 250 | use: R | rpt: 1)
        :param notification_code: Coded Element (id: NDS.4 | len: 250 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.notification_reference_number = notification_reference_number
        self.notification_date_or_time = notification_date_or_time
        self.notification_alert_severity = notification_alert_severity
        self.notification_code = notification_code

    @property  # get NDS.1
    def notification_reference_number(self) -> NM:
        """
        id: NDS.1 | len: 20 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDS.1
        """
        return self._c_data[0][0]

    @notification_reference_number.setter  # set NDS.1
    def notification_reference_number(self, nm: NM):
        """
        id: NDS.1 | len: 20 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDS.1
        """
        self._c_data[0] = (nm,)

    @property  # get NDS.2
    def notification_date_or_time(self) -> TS:
        """
        id: NDS.2 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDS.2
        """
        return self._c_data[1][0]

    @notification_date_or_time.setter  # set NDS.2
    def notification_date_or_time(self, ts: TS):
        """
        id: NDS.2 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDS.2
        """
        self._c_data[1] = (ts,)

    @property  # get NDS.3
    def notification_alert_severity(self) -> AlertLevel:
        """
        id: NDS.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDS.3
        """
        return self._c_data[2][0]

    @notification_alert_severity.setter  # set NDS.3
    def notification_alert_severity(self, alert_level: AlertLevel):
        """
        id: NDS.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDS.3
        """
        self._c_data[2] = (alert_level,)

    @property  # get NDS.4
    def notification_code(self) -> CE:
        """
        id: NDS.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDS.4
        """
        return self._c_data[3][0]

    @notification_code.setter  # set NDS.4
    def notification_code(self, ce: CE):
        """
        id: NDS.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NDS.4
        """
        self._c_data[3] = (ce,)
