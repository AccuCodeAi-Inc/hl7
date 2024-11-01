from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.EQU import EQU


"""
Automated equipment status request - ESR_U02
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ESR_U02 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ESR_U02
from utils.hl7.v2_5_1.segments import (
    EQU, SFT, MSH, ROL
)

esr_u02 = ESR_U02(  #  - This message is used to request information about a device's or piece of equipment's status from one application to another (e
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    equipment_detail=equ,  # EQU(...)  # Required.
    role=None,  # ROL(...) 
)

-----END TRIGGER_EVENT::ESR_U02 TEMPLATE-----
"""


class ESR_U02(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ESR_U02"""
    _hl7_name = """Automated equipment status request"""
    _hl7_description = """This message is used to request information about a device's or piece of equipment's status from one application to another (e"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ESR_U02"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4")
    _c_components = (MSH, SFT, EQU, ROL)
    _c_name = ("MSH", "SFT", "EQU", "ROL")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "equipment_detail", "role",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        equipment_detail: EQU,  #  Required. EQU.3
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        role: ROL | None = None,  #  ROL.4
    ):
        """
         - `ESR_U02 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ESR_U02>`_
        This message is used to request information about a device's or piece of equipment's status from one application to another (e.g., Laboratory Automation System to automated equipment). The equipment identified in the EQU segment should respond with its status using the "Automated Equipment Status Update."

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param equipment_detail: Equipment Detail (id: EQU | seq: 3 | use: R | rpt: 1)
        :param role: Role (id: ROL | seq: 4 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.equipment_detail = equipment_detail
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

    @property  # get ROL.4
    def role(self) -> ROL | None:
        """
        id: ROL | use: O | rpt: 1 | seq: 4
        ---
        return_type: ROL.4: Role
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[3][0]

    @role.setter  # set ROL.4
    def role(self, rol: ROL | None):
        """
        id: ROL | use: O | rpt: 1 | seq: 4
        ---
        param_type: ROL.4: Role
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        self._c_data[3] = (rol,)
