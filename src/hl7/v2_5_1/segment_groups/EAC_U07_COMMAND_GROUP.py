from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CNS import CNS
from ..segments.ECD import ECD
from ..segment_groups.EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP import (
    EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP,
)
from ..segments.TQ1 import TQ1


"""
COMMAND - EAC_U07_COMMAND_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::EAC_U07_COMMAND_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import EAC_U07_COMMAND_GROUP
from utils.hl7.v2_5_1.segments import (
    TQ1, CNS, ECD
)
from utils.hl7.v2_5_1.segment_groups import (
    EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP
)

eac_u07_command_group = EAC_U07_COMMAND_GROUP(  # COMMAND - Segment group for EAC_U07 - Automated equipment command consisting of ECD, TQ1|None, SPECIMEN CONTAINER|None, CNS|None
    equipment_command=ecd,  # ECD(...)  # Required.
    timing_or_quantity=None,  # TQ1(...) 
    specimen_container=None,  # EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP(...) 
    clear_notification=None,  # CNS(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::EAC_U07_COMMAND_GROUP TEMPLATE-----
"""


class EAC_U07_COMMAND_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """EAC_U07_COMMAND_GROUP"""
    _hl7_name = """COMMAND"""
    _hl7_description = """Segment group for EAC_U07 - Automated equipment command consisting of ECD, TQ1|None, SPECIMEN CONTAINER|None, CNS|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EAC_U07_COMMAND_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 1)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("4", "5", "None", "8")
    _c_components = (ECD, TQ1, EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP, CNS)
    _c_name = ("ECD", "TQ1", "SPECIMEN CONTAINER", "CNS")
    _c_is_group = (False, False, True, False)
    _c_attrs = ("equipment_command", "timing_or_quantity", "specimen_container", "clear_notification",)
    # fmt: on

    def __init__(
        self,
        equipment_command: ECD,  #  Required. ECD.4
        timing_or_quantity: TQ1 | None = None,  #  TQ1.5
        specimen_container: EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP
        | None = None,  #  SAC.6, SPM.7
        clear_notification: CNS | None = None,  #  CNS.8
    ):
        """
        None - `EAC_U07_COMMAND_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EAC_U07_COMMAND_GROUP>`_
        Segment group for EAC_U07 - Automated equipment command consisting of ECD, TQ1|None, SPECIMEN CONTAINER|None, CNS|None

        :param equipment_command: Equipment Command (id: ECD | seq: 4 | use: R | rpt: 1)
        :param timing_or_quantity: Timing/Quantity (id: TQ1 | seq: 5 | use: O | rpt: 1)
        :param specimen_container: Specimen Container segment group: [SAC, SPM|None] (id: SPECIMEN CONTAINER | seq: 6, 7 | use: O | rpt: 1)
        :param clear_notification: Clear Notification (id: CNS | seq: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.equipment_command = equipment_command
        self.timing_or_quantity = timing_or_quantity
        self.specimen_container = specimen_container
        self.clear_notification = clear_notification

    @property  # get ECD.4
    def equipment_command(self) -> ECD:
        """
        id: ECD | use: R | rpt: 1 | seq: 4
        ---
        return_type: ECD.4: Equipment Command
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ECD
        """
        return self._c_data[0][0]

    @equipment_command.setter  # set ECD.4
    def equipment_command(self, ecd: ECD):
        """
        id: ECD | use: R | rpt: 1 | seq: 4
        ---
        param_type: ECD.4: Equipment Command
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ECD
        """
        self._c_data[0] = (ecd,)

    @property  # get TQ1.5
    def timing_or_quantity(self) -> TQ1 | None:
        """
        id: TQ1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: TQ1.5: Timing/Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        return self._c_data[1][0]

    @timing_or_quantity.setter  # set TQ1.5
    def timing_or_quantity(self, tq1: TQ1 | None):
        """
        id: TQ1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: TQ1.5: Timing/Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        self._c_data[1] = (tq1,)

    @property  # get EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP.None
    def specimen_container(
        self,
    ) -> EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP | None:
        """
        id: EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP
        """
        return self._c_data[2][0]

    @specimen_container.setter  # set EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP.None
    def specimen_container(
        self, specimen_container: EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP | None
    ):
        """
        id: EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EAC_U07_COMMAND_GROUP_SPECIMEN_CONTAINER_GROUP
        """
        self._c_data[2] = (specimen_container,)

    @property  # get CNS.8
    def clear_notification(self) -> CNS | None:
        """
        id: CNS | use: O | rpt: 1 | seq: 8
        ---
        return_type: CNS.8: Clear Notification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CNS
        """
        return self._c_data[3][0]

    @clear_notification.setter  # set CNS.8
    def clear_notification(self, cns: CNS | None):
        """
        id: CNS | use: O | rpt: 1 | seq: 8
        ---
        param_type: CNS.8: Clear Notification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CNS
        """
        self._c_data[3] = (cns,)
