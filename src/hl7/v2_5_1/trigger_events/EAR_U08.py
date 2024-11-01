from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.ROL import ROL
from ..segments.MSH import MSH
from ..segment_groups.EAR_U08_COMMAND_RESPONSE_GROUP import (
    EAR_U08_COMMAND_RESPONSE_GROUP,
)
from ..segments.SFT import SFT
from ..segments.EQU import EQU


"""
Automated equipment response - EAR_U08
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::EAR_U08 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import EAR_U08
from utils.hl7.v2_5_1.segments import (
    SFT, EQU, ROL, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    EAR_U08_COMMAND_RESPONSE_GROUP
)

ear_u08 = EAR_U08(  #  - 
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    equipment_detail=equ,  # EQU(...)  # Required.
    command_response=ear_u08_command_response_group,  # EAR_U08_COMMAND_RESPONSE_GROUP(...)  # Required.
    role=None,  # ROL(...) 
)

-----END TRIGGER_EVENT::EAR_U08 TEMPLATE-----
"""


class EAR_U08(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """EAR_U08"""
    _hl7_name = """Automated equipment response"""
    _hl7_description = """"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EAR_U08"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "R", "O")
    _c_aliases = ("1", "2", "3", "None", "8")
    _c_components = (MSH, SFT, EQU, EAR_U08_COMMAND_RESPONSE_GROUP, ROL)
    _c_name = ("MSH", "SFT", "EQU", "COMMAND RESPONSE", "ROL")
    _c_is_group = (False, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "equipment_detail", "command_response", "role",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        equipment_detail: EQU,  #  Required. EQU.3
        command_response: EAR_U08_COMMAND_RESPONSE_GROUP
        | tuple[EAR_U08_COMMAND_RESPONSE_GROUP, ...],  #  Required. (ECD.4, ECR.7, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        role: ROL | None = None,  #  ROL.8
    ):
        """
         - `EAR_U08 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EAR_U08>`_


        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param equipment_detail: Equipment Detail (id: EQU | seq: 3 | use: R | rpt: 1)
        :param command_response: Command Response segment group: [ECD, SPECIMEN CONTAINER|None, ECR] (id: COMMAND RESPONSE | seq: 4, None, 7 | use: R | rpt: *)
        :param role: Role (id: ROL | seq: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.message_header = message_header
        self.software_segment = software_segment
        self.equipment_detail = equipment_detail
        self.command_response = command_response
        self.role = role

    @property  # get MSH.1
    def message_header(self) -> MSH:
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        return_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        return self._c_data[0][0]

    @message_header.setter  # set MSH.1
    def message_header(self, msh: MSH):
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        param_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        self._c_data[0] = (msh,)

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[1]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        param_type: SFT.2 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[1] = sft
        else:
            self._c_data[1] = (sft,)

    @property  # get EQU.3
    def equipment_detail(self) -> EQU:
        """
        id: EQU | use: R | rpt: 1 | seq: 3
        ---
        return_type: EQU.3: Equipment Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EQU
        """
        return self._c_data[2][0]

    @equipment_detail.setter  # set EQU.3
    def equipment_detail(self, equ: EQU):
        """
        id: EQU | use: R | rpt: 1 | seq: 3
        ---
        param_type: EQU.3: Equipment Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EQU
        """
        self._c_data[2] = (equ,)

    @property  # get COMMAND RESPONSE
    def command_response(self) -> tuple[EAR_U08_COMMAND_RESPONSE_GROUP, ...]:
        """
        id: EAR_U08_COMMAND_RESPONSE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[EAR_U08_COMMAND_RESPONSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EAR_U08_COMMAND_RESPONSE_GROUP
        """
        return self._c_data[3]

    @command_response.setter  # set COMMAND RESPONSE
    def command_response(
        self,
        command_response: EAR_U08_COMMAND_RESPONSE_GROUP
        | tuple[EAR_U08_COMMAND_RESPONSE_GROUP, ...],
    ):
        """
        id: COMMAND RESPONSE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: EAR_U08_COMMAND_RESPONSE_GROUP.None | tuple[EAR_U08_COMMAND_RESPONSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EAR_U08_COMMAND_RESPONSE_GROUP
        """
        if isinstance(command_response, tuple):
            self._c_data[3] = command_response
        else:
            self._c_data[3] = (command_response,)

    @property  # get ROL.8
    def role(self) -> ROL | None:
        """
        id: ROL | use: O | rpt: 1 | seq: 8
        ---
        return_type: ROL.8: Role
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[4][0]

    @role.setter  # set ROL.8
    def role(self, rol: ROL | None):
        """
        id: ROL | use: O | rpt: 1 | seq: 8
        ---
        param_type: ROL.8: Role
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        self._c_data[4] = (rol,)
