from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segment_groups.ORS_O06_RESPONSE_GROUP import ORS_O06_RESPONSE_GROUP
from ..segments.ERR import ERR
from ..segments.MSH import MSH
from ..segments.MSA import MSA


"""
Stock Requisition Order Acknowledgement - ORS_O06
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ORS_O06 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORS_O06
from utils.hl7.v2_5_1.segments import (
    ERR, NTE, SFT, MSA, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    ORS_O06_RESPONSE_GROUP
)

ors_o06 = ORS_O06(  #  - Stock requisition orders use the ORM where RQD is the detail segment for backward compatibility or can use the OMS and ORS messages
    message_header=msh,  # MSH(...)  # Required.
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    software_segment=None,  # SFT(...) 
    notes_and_comments=None,  # NTE(...) 
    response=None,  # ORS_O06_RESPONSE_GROUP(...) 
)

-----END TRIGGER_EVENT::ORS_O06 TEMPLATE-----
"""


class ORS_O06(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ORS_O06"""
    _hl7_name = """Stock Requisition Order Acknowledgement"""
    _hl7_description = """Stock requisition orders use the ORM where RQD is the detail segment for backward compatibility or can use the OMS and ORS messages"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORS_O06"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 1)
    _c_usage = ("R", "R", "O", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "None")
    _c_components = (MSH, MSA, ERR, SFT, NTE, ORS_O06_RESPONSE_GROUP)
    _c_name = ("MSH", "MSA", "ERR", "SFT", "NTE", "RESPONSE")
    _c_is_group = (False, False, False, False, False, True)
    _c_attrs = ("message_header", "message_acknowledgment", "error", "software_segment", "notes_and_comments", "response",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.2
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.3
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.4
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.5
        response: ORS_O06_RESPONSE_GROUP | None = None,  #
    ):
        """
         - `ORS_O06 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORS_O06>`_
        Stock requisition orders use the ORM where RQD is the detail segment for backward compatibility or can use the OMS and ORS messages.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 2 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 3 | use: O | rpt: *)
        :param software_segment: Software Segment (id: SFT | seq: 4 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 5 | use: O | rpt: *)
        :param response: Response segment group: [PATIENT|None, ORDER] (id: RESPONSE | seq: None, None | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.software_segment = software_segment
        self.notes_and_comments = notes_and_comments
        self.response = response

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

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[4]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        param_type: NTE.5 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[4] = nte
        else:
            self._c_data[4] = (nte,)

    @property  # get ORS_O06_RESPONSE_GROUP.None
    def response(self) -> ORS_O06_RESPONSE_GROUP | None:
        """
        id: ORS_O06_RESPONSE_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORS_O06_RESPONSE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORS_O06_RESPONSE_GROUP
        """
        return self._c_data[5][0]

    @response.setter  # set ORS_O06_RESPONSE_GROUP.None
    def response(self, response: ORS_O06_RESPONSE_GROUP | None):
        """
        id: ORS_O06_RESPONSE_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORS_O06_RESPONSE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORS_O06_RESPONSE_GROUP
        """
        self._c_data[5] = (response,)
