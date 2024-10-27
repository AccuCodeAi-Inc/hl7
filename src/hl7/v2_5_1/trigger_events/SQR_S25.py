from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.ERR import ERR
from ..segment_groups.SQR_S25_SCHEDULE_GROUP import SQR_S25_SCHEDULE_GROUP
from ..segments.MSH import MSH
from ..segments.MSA import MSA
from ..segments.DSC import DSC
from ..segments.QAK import QAK


"""
Schedule query message and response - SQR_S25
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::SQR_S25 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SQR_S25
from utils.hl7.v2_5_1.segments import (
    QAK, ERR, MSA, DSC, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    SQR_S25_SCHEDULE_GROUP
)

sqr_s25 = SQR_S25(  #  - Original Mode record-oriented query transactions are initiated from the querying application using the Schedule Query (SQM) to request information about a filler application's schedule(s)
    message_header=msh,  # MSH(...)  # Required.
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=qak,  # QAK(...)  # Required.
    schedule=None,  # SQR_S25_SCHEDULE_GROUP(...) 
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::SQR_S25 TEMPLATE-----
"""


class SQR_S25(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """SQR_S25"""
    _hl7_name = """Schedule query message and response"""
    _hl7_description = """Original Mode record-oriented query transactions are initiated from the querying application using the Schedule Query (SQM) to request information about a filler application's schedule(s)"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQR_S25"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1, 65535, 1)
    _c_usage = ("R", "R", "O", "R", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "None", "21")
    _c_components = (MSH, MSA, ERR, QAK, SQR_S25_SCHEDULE_GROUP, DSC)
    _c_name = ("MSH", "MSA", "ERR", "QAK", "SCHEDULE", "DSC")
    _c_is_group = (False, False, False, False, True, False)
    _c_attrs = ("message_header", "message_acknowledgment", "error", "query_acknowledgment", "schedule", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.2
        query_acknowledgment: QAK,  #  Required. QAK.4
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.3
        schedule: SQR_S25_SCHEDULE_GROUP
        | tuple[SQR_S25_SCHEDULE_GROUP, ...]
        | None = None,  #  (SCH.5, TQ1.6, NTE.7, ...)
        continuation_pointer: DSC | None = None,  #  DSC.21
    ):
        """
         - `SQR_S25 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQR_S25>`_
        Original Mode record-oriented query transactions are initiated from the querying application using the Schedule Query (SQM) to request information about a filler application's schedule(s).  The filler application responds to these requests, using the Schedule Query Response (SQR) message to either return the requested information, or to signal that an interfacing error of some kind has occurred.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 2 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 3 | use: O | rpt: *)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 4 | use: R | rpt: 1)
        :param schedule: Schedule segment group: [SCH, TQ1|None, NTE|None, PATIENT|None, RESOURCES] (id: SCHEDULE | seq: 5, 6, 7, None, None | use: O | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 21 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.query_acknowledgment = query_acknowledgment
        self.schedule = schedule
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

    @property  # get QAK.4
    def query_acknowledgment(self) -> QAK:
        """
        id: QAK | use: R | rpt: 1 | seq: 4
        ---
        return_type: QAK.4: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        return self._c_data[3][0]

    @query_acknowledgment.setter  # set QAK.4
    def query_acknowledgment(self, qak: QAK):
        """
        id: QAK | use: R | rpt: 1 | seq: 4
        ---
        param_type: QAK.4: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        self._c_data[3] = (qak,)

    @property  # get SCHEDULE
    def schedule(self) -> tuple[SQR_S25_SCHEDULE_GROUP, ...] | tuple[None]:
        """
        id: SQR_S25_SCHEDULE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SQR_S25_SCHEDULE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP
        """
        return self._c_data[4]

    @schedule.setter  # set SCHEDULE
    def schedule(
        self,
        schedule: SQR_S25_SCHEDULE_GROUP | tuple[SQR_S25_SCHEDULE_GROUP, ...] | None,
    ):
        """
        id: SCHEDULE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SQR_S25_SCHEDULE_GROUP.None | tuple[SQR_S25_SCHEDULE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP
        """
        if isinstance(schedule, tuple):
            self._c_data[4] = schedule
        else:
            self._c_data[4] = (schedule,)

    @property  # get DSC.21
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 21
        ---
        return_type: DSC.21: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[5][0]

    @continuation_pointer.setter  # set DSC.21
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 21
        ---
        param_type: DSC.21: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[5] = (dsc,)
