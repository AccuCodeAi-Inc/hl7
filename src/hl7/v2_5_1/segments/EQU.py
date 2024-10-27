from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.EI import EI
from ..data_types.CE import CE
from ..tables.EquipmentState import EquipmentState
from ..tables.AlertLevel import AlertLevel
from ..tables.LocalOrRemoteControlState import LocalOrRemoteControlState


"""
Equipment Detail - EQU
HL7 Version: 2.5.1

-----BEGIN SEGMENT::EQU TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    EQU,
    TS, EI, CE
)

equ = EQU(  #  - The equipment detail segment contains the data necessary to identify and maintain the equipment that is being used throughout the Laboratory Automation System
    equipment_instance_identifier=ei,  # EI(...)  # Required.
    event_date_or_time=ts,  # TS(...)  # Required.
    equipment_state=None,  # CE(...) 
    local_or_remote_control_state=None,  # CE(...) 
    alert_level=None,  # CE(...) 
)

-----END SEGMENT::EQU TEMPLATE-----
"""


class EQU(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """EQU"""
    _hl7_name = """Equipment Detail"""
    _hl7_description = """The equipment detail segment contains the data necessary to identify and maintain the equipment that is being used throughout the Laboratory Automation System"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EQU"
    _c_length = (22, 26, 250, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "C", "O", "O",)
    _c_components = (EI, TS, CE, CE, CE,)
    _c_aliases = ("EQU.1", "EQU.2", "EQU.3", "EQU.4", "EQU.5",)
    _c_names = ("Equipment Instance Identifier", "Event Date/Time", "Equipment State", "Local/Remote Control State", "Alert Level",)
    _c_attrs = ("equipment_instance_identifier", "event_date_or_time", "equipment_state", "local_or_remote_control_state", "alert_level",)
    # fmt: on

    def __init__(
        self,
        equipment_instance_identifier: EI,  # EQU.1
        event_date_or_time: TS,  # EQU.2
        equipment_state: EquipmentState | CE | None = None,  # EQU.3
        local_or_remote_control_state: LocalOrRemoteControlState
        | CE
        | None = None,  # EQU.4
        alert_level: AlertLevel | CE | None = None,  # EQU.5
    ):
        """
        Equipment Detail - `EQU <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EQU>`_
        The equipment detail segment contains the data necessary to identify and maintain the equipment that is being used throughout the Laboratory Automation System.

        :param equipment_instance_identifier: Entity Identifier (id: EQU.1 | len: 22 | use: R | rpt: 1)
        :param event_date_or_time: Time Stamp (id: EQU.2 | len: 26 | use: R | rpt: 1)
        :param equipment_state: Coded Element (id: EQU.3 | len: 250 | use: C | rpt: 1)
        :param local_or_remote_control_state: Coded Element (id: EQU.4 | len: 250 | use: O | rpt: 1)
        :param alert_level: Coded Element (id: EQU.5 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.equipment_instance_identifier = equipment_instance_identifier
        self.event_date_or_time = event_date_or_time
        self.equipment_state = equipment_state
        self.local_or_remote_control_state = local_or_remote_control_state
        self.alert_level = alert_level

    @property  # get EQU.1
    def equipment_instance_identifier(self) -> EI:
        """
        id: EQU.1 | len: 22 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQU.1
        """
        return self._c_data[0][0]

    @equipment_instance_identifier.setter  # set EQU.1
    def equipment_instance_identifier(self, ei: EI):
        """
        id: EQU.1 | len: 22 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQU.1
        """
        self._c_data[0] = (ei,)

    @property  # get EQU.2
    def event_date_or_time(self) -> TS:
        """
        id: EQU.2 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQU.2
        """
        return self._c_data[1][0]

    @event_date_or_time.setter  # set EQU.2
    def event_date_or_time(self, ts: TS):
        """
        id: EQU.2 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQU.2
        """
        self._c_data[1] = (ts,)

    @property  # get EQU.3
    def equipment_state(self) -> EquipmentState | None:
        """
        id: EQU.3 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQU.3
        """
        return self._c_data[2][0]

    @equipment_state.setter  # set EQU.3
    def equipment_state(self, equipment_state: EquipmentState | None):
        """
        id: EQU.3 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQU.3
        """
        self._c_data[2] = (equipment_state,)

    @property  # get EQU.4
    def local_or_remote_control_state(self) -> LocalOrRemoteControlState | None:
        """
        id: EQU.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQU.4
        """
        return self._c_data[3][0]

    @local_or_remote_control_state.setter  # set EQU.4
    def local_or_remote_control_state(
        self, local_or_remote_control_state: LocalOrRemoteControlState | None
    ):
        """
        id: EQU.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQU.4
        """
        self._c_data[3] = (local_or_remote_control_state,)

    @property  # get EQU.5
    def alert_level(self) -> AlertLevel | None:
        """
        id: EQU.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQU.5
        """
        return self._c_data[4][0]

    @alert_level.setter  # set EQU.5
    def alert_level(self, alert_level: AlertLevel | None):
        """
        id: EQU.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQU.5
        """
        self._c_data[4] = (alert_level,)
