from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP import (
    EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP,
)
from ..segments.ECR import ECR
from ..segments.ECD import ECD


"""
COMMAND RESPONSE - EAR_U08_COMMAND_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::EAR_U08_COMMAND_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import EAR_U08_COMMAND_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    ECR, ECD
)
from utils.hl7.v2_5_1.segment_groups import (
    EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP
)

ear_u08_command_response_group = EAR_U08_COMMAND_RESPONSE_GROUP(  # COMMAND RESPONSE - Segment group for EAR_U08 - Automated equipment response consisting of ECD, SPECIMEN CONTAINER|None, ECR
    equipment_command=ecd,  # ECD(...)  # Required.
    specimen_container=None,  # EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP(...) 
    equipment_command_response=ecr,  # ECR(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::EAR_U08_COMMAND_RESPONSE_GROUP TEMPLATE-----
"""


class EAR_U08_COMMAND_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """EAR_U08_COMMAND_RESPONSE_GROUP"""
    _hl7_name = """COMMAND RESPONSE"""
    _hl7_description = """Segment group for EAR_U08 - Automated equipment response consisting of ECD, SPECIMEN CONTAINER|None, ECR"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EAR_U08_COMMAND_RESPONSE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 1)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("4", "None", "7")
    _c_components = (ECD, EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP, ECR)
    _c_name = ("ECD", "SPECIMEN CONTAINER", "ECR")
    _c_is_group = (False, True, False)
    _c_attrs = ("equipment_command", "specimen_container", "equipment_command_response",)
    # fmt: on

    def __init__(
        self,
        equipment_command: ECD,  #  Required. ECD.4
        equipment_command_response: ECR,  #  Required. ECR.7
        specimen_container: EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP
        | None = None,  #  SAC.5, SPM.6
    ):
        """
        None - `EAR_U08_COMMAND_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EAR_U08_COMMAND_RESPONSE_GROUP>`_
        Segment group for EAR_U08 - Automated equipment response consisting of ECD, SPECIMEN CONTAINER|None, ECR

        :param equipment_command: Equipment Command (id: ECD | seq: 4 | use: R | rpt: 1)
        :param specimen_container: Specimen Container segment group: [SAC, SPM|None] (id: SPECIMEN CONTAINER | seq: 5, 6 | use: O | rpt: 1)
        :param equipment_command_response: Equipment Command Response (id: ECR | seq: 7 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.equipment_command = equipment_command
        self.specimen_container = specimen_container
        self.equipment_command_response = equipment_command_response

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

    @property  # get EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP.None
    def specimen_container(
        self,
    ) -> EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP | None:
        """
        id: EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP
        """
        return self._c_data[1][0]

    @specimen_container.setter  # set EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP.None
    def specimen_container(
        self,
        specimen_container: EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP
        | None,
    ):
        """
        id: EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP
        """
        self._c_data[1] = (specimen_container,)

    @property  # get ECR.7
    def equipment_command_response(self) -> ECR:
        """
        id: ECR | use: R | rpt: 1 | seq: 7
        ---
        return_type: ECR.7: Equipment Command Response
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ECR
        """
        return self._c_data[2][0]

    @equipment_command_response.setter  # set ECR.7
    def equipment_command_response(self, ecr: ECR):
        """
        id: ECR | use: R | rpt: 1 | seq: 7
        ---
        param_type: ECR.7: Equipment Command Response
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ECR
        """
        self._c_data[2] = (ecr,)
