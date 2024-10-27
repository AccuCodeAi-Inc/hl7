from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segment_groups.SRR_S05_SCHEDULE_GROUP import SRR_S05_SCHEDULE_GROUP
from ..segments.ERR import ERR
from ..segments.MSA import MSA


"""
Scheduled request response - Appointment discontinuation - SRR_S05
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::SRR_S05 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SRR_S05
from utils.hl7.v2_5_1.segments import (
    ERR, MSA, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    SRR_S05_SCHEDULE_GROUP
)

srr_s05 = SRR_S05(  #  - The request appointment discontinuation is sent by the placer application to the filler application to request that an appointment in progress be stopped, or that the remaining occurrences of a parent appointment not occur as scheduled
    message_header=msh,  # MSH(...)  # Required.
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    schedule=None,  # SRR_S05_SCHEDULE_GROUP(...) 
)

-----END TRIGGER_EVENT::SRR_S05 TEMPLATE-----
"""


class SRR_S05(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """SRR_S05"""
    _hl7_name = """Scheduled request response - Appointment discontinuation"""
    _hl7_description = """The request appointment discontinuation is sent by the placer application to the filler application to request that an appointment in progress be stopped, or that the remaining occurrences of a parent appointment not occur as scheduled"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRR_S05"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1)
    _c_usage = ("R", "R", "O", "O")
    _c_aliases = ("1", "2", "3", "None")
    _c_components = (MSH, MSA, ERR, SRR_S05_SCHEDULE_GROUP)
    _c_name = ("MSH", "MSA", "ERR", "SCHEDULE")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("message_header", "message_acknowledgment", "error", "schedule",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.2
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.3
        schedule: SRR_S05_SCHEDULE_GROUP | None = None,  #  SCH.4, TQ1.5, NTE.6
    ):
        """
         - `SRR_S05 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRR_S05>`_
        The request appointment discontinuation is sent by the placer application to the filler application to request that an appointment in progress be stopped, or that the remaining occurrences of a parent appointment not occur as scheduled.  If none of the child appointments of a parent appointment have occurred, then a cancel trigger event should be sent instead.  If it is successful, an application acknowledgment is returned, optionally containing an SCH segment and related detail segments describing the discontinued appointment.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 2 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 3 | use: O | rpt: *)
        :param schedule: Schedule segment group: [SCH, TQ1|None, NTE|None, PATIENT|None, RESOURCES] (id: SCHEDULE | seq: 4, 5, 6, None, None | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.schedule = schedule

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

    @property  # get SRR_S05_SCHEDULE_GROUP.None
    def schedule(self) -> SRR_S05_SCHEDULE_GROUP | None:
        """
        id: SRR_S05_SCHEDULE_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: SRR_S05_SCHEDULE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRR_S05_SCHEDULE_GROUP
        """
        return self._c_data[3][0]

    @schedule.setter  # set SRR_S05_SCHEDULE_GROUP.None
    def schedule(self, schedule: SRR_S05_SCHEDULE_GROUP | None):
        """
        id: SRR_S05_SCHEDULE_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: SRR_S05_SCHEDULE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRR_S05_SCHEDULE_GROUP
        """
        self._c_data[3] = (schedule,)
