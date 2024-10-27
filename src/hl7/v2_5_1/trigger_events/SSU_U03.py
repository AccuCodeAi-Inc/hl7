from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.ROL import ROL
from ..segments.MSH import MSH
from ..segment_groups.SSU_U03_SPECIMEN_CONTAINER_GROUP import (
    SSU_U03_SPECIMEN_CONTAINER_GROUP,
)
from ..segments.EQU import EQU


"""
Specimen status update - SSU_U03
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::SSU_U03 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SSU_U03
from utils.hl7.v2_5_1.segments import (
    SFT, ROL, EQU, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    SSU_U03_SPECIMEN_CONTAINER_GROUP
)

ssu_u03 = SSU_U03(  #  - This message is used to send information concerning the location and status of specimens from one application to another (e
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    equipment_detail=equ,  # EQU(...)  # Required.
    specimen_container=ssu_u03_specimen_container_group,  # SSU_U03_SPECIMEN_CONTAINER_GROUP(...)  # Required.
    role=None,  # ROL(...) 
)

-----END TRIGGER_EVENT::SSU_U03 TEMPLATE-----
"""


class SSU_U03(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """SSU_U03"""
    _hl7_name = """Specimen status update"""
    _hl7_description = """This message is used to send information concerning the location and status of specimens from one application to another (e"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SSU_U03"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "R", "O")
    _c_aliases = ("1", "2", "3", "None", "8")
    _c_components = (MSH, SFT, EQU, SSU_U03_SPECIMEN_CONTAINER_GROUP, ROL)
    _c_name = ("MSH", "SFT", "EQU", "SPECIMEN CONTAINER", "ROL")
    _c_is_group = (False, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "equipment_detail", "specimen_container", "role",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        equipment_detail: EQU,  #  Required. EQU.3
        specimen_container: SSU_U03_SPECIMEN_CONTAINER_GROUP
        | tuple[
            SSU_U03_SPECIMEN_CONTAINER_GROUP, ...
        ],  #  Required. (SAC.4, OBX.5, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        role: ROL | None = None,  #  ROL.8
    ):
        """
         - `SSU_U03 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SSU_U03>`_
        This message is used to send information concerning the location and status of specimens from one application to another (e.g., automated equipment to a Laboratory Automation System). The OBX segments attached to the SAC should be used for transfer of information not included in the SAC segment.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param equipment_detail: Equipment Detail (id: EQU | seq: 3 | use: R | rpt: 1)
        :param specimen_container: Specimen Container segment group: [SAC, OBX|None, SPECIMEN|None] (id: SPECIMEN CONTAINER | seq: 4, 5, None | use: R | rpt: *)
        :param role: Role (id: ROL | seq: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.message_header = message_header
        self.software_segment = software_segment
        self.equipment_detail = equipment_detail
        self.specimen_container = specimen_container
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

    @property  # get SPECIMEN CONTAINER
    def specimen_container(self) -> tuple[SSU_U03_SPECIMEN_CONTAINER_GROUP, ...]:
        """
        id: SSU_U03_SPECIMEN_CONTAINER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[SSU_U03_SPECIMEN_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SSU_U03_SPECIMEN_CONTAINER_GROUP
        """
        return self._c_data[3]

    @specimen_container.setter  # set SPECIMEN CONTAINER
    def specimen_container(
        self,
        specimen_container: SSU_U03_SPECIMEN_CONTAINER_GROUP
        | tuple[SSU_U03_SPECIMEN_CONTAINER_GROUP, ...],
    ):
        """
        id: SPECIMEN CONTAINER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: SSU_U03_SPECIMEN_CONTAINER_GROUP.None | tuple[SSU_U03_SPECIMEN_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SSU_U03_SPECIMEN_CONTAINER_GROUP
        """
        if isinstance(specimen_container, tuple):
            self._c_data[3] = specimen_container
        else:
            self._c_data[3] = (specimen_container,)

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
