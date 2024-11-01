from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.ERR import ERR
from ..segment_groups.RER_RER_DEFINITION_GROUP import RER_RER_DEFINITION_GROUP
from ..segments.MSH import MSH
from ..segments.MSA import MSA
from ..segments.DSC import DSC
from ..segments.SFT import SFT


"""
Pharmacy/Treatment Encoded Order Information Response - RER_RER
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RER_RER TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RER_RER
from utils.hl7.v2_5_1.segments import (
    SFT, DSC, ERR, MSA, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    RER_RER_DEFINITION_GROUP
)

rer_rer = RER_RER(  #  - This query/response pair is retained for backward compatibility only
    message_header=msh,  # MSH(...)  # Required.
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    software_segment=None,  # SFT(...) 
    definition=rer_rer_definition_group,  # RER_RER_DEFINITION_GROUP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::RER_RER TEMPLATE-----
"""


class RER_RER(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RER_RER"""
    _hl7_name = """Pharmacy/Treatment Encoded Order Information Response"""
    _hl7_description = """This query/response pair is retained for backward compatibility only"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RER_RER"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 1)
    _c_usage = ("R", "R", "O", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "None", "13")
    _c_components = (MSH, MSA, ERR, SFT, RER_RER_DEFINITION_GROUP, DSC)
    _c_name = ("MSH", "MSA", "ERR", "SFT", "DEFINITION", "DSC")
    _c_is_group = (False, False, False, False, True, False)
    _c_attrs = ("message_header", "message_acknowledgment", "error", "software_segment", "definition", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.2
        definition: RER_RER_DEFINITION_GROUP
        | tuple[RER_RER_DEFINITION_GROUP, ...],  #  Required. (QRD.5, QRF.6, ...)
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.3
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.4
        continuation_pointer: DSC | None = None,  #  DSC.13
    ):
        """
         - `RER_RER <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RER_RER>`_
        This query/response pair is retained for backward compatibility only.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 2 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 3 | use: O | rpt: *)
        :param software_segment: Software Segment (id: SFT | seq: 4 | use: O | rpt: *)
        :param definition: Definition segment group: [QRD, QRF|None, PATIENT|None, ORDER] (id: DEFINITION | seq: 5, 6, None, None | use: R | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 13 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.software_segment = software_segment
        self.definition = definition
        self.continuation_pointer = continuation_pointer

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

    @property  # get MSA.2
    def message_acknowledgment(self) -> MSA:
        """
        id: MSA | use: R | rpt: 1 | seq: 2
        ---
        return_type: MSA.2: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        return self._c_data[1][0]

    @message_acknowledgment.setter  # set MSA.2
    def message_acknowledgment(self, msa: MSA):
        """
        id: MSA | use: R | rpt: 1 | seq: 2
        ---
        param_type: MSA.2: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        self._c_data[1] = (msa,)

    @property  # get ERR
    def error(self) -> tuple[ERR, ...] | tuple[None]:
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 3
        ---
        return_type: tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        return self._c_data[2]

    @error.setter  # set ERR
    def error(self, err: ERR | tuple[ERR, ...] | None):
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 3
        ---
        param_type: ERR.3 | tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        if isinstance(err, tuple):
            self._c_data[2] = err
        else:
            self._c_data[2] = (err,)

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[3]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        param_type: SFT.4 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[3] = sft
        else:
            self._c_data[3] = (sft,)

    @property  # get DEFINITION
    def definition(self) -> tuple[RER_RER_DEFINITION_GROUP, ...]:
        """
        id: RER_RER_DEFINITION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RER_RER_DEFINITION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RER_RER_DEFINITION_GROUP
        """
        return self._c_data[4]

    @definition.setter  # set DEFINITION
    def definition(
        self,
        definition: RER_RER_DEFINITION_GROUP | tuple[RER_RER_DEFINITION_GROUP, ...],
    ):
        """
        id: DEFINITION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RER_RER_DEFINITION_GROUP.None | tuple[RER_RER_DEFINITION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RER_RER_DEFINITION_GROUP
        """
        if isinstance(definition, tuple):
            self._c_data[4] = definition
        else:
            self._c_data[4] = (definition,)

    @property  # get DSC.13
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 13
        ---
        return_type: DSC.13: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[5][0]

    @continuation_pointer.setter  # set DSC.13
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 13
        ---
        param_type: DSC.13: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[5] = (dsc,)
