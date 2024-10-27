from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.EVN import EVN
from ..segments.SFT import SFT
from ..segments.ROL import ROL
from ..segment_groups.BAR_P01_VISIT_GROUP import BAR_P01_VISIT_GROUP
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PD1 import PD1


"""
Add Patient Accounts - BAR_P01
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::BAR_P01 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BAR_P01
from utils.hl7.v2_5_1.segments import (
    ROL, PD1, MSH, SFT, PID, EVN
)
from utils.hl7.v2_5_1.segment_groups import (
    BAR_P01_VISIT_GROUP
)

bar_p01 = BAR_P01(  #  - Data are sent from some application (usually a Registration or an ADT system) for example, to the patient accounting or financial system to establish an account for a patient’s billing/accounts receivable record
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    role=None,  # ROL(...) 
    visit=bar_p01_visit_group,  # BAR_P01_VISIT_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::BAR_P01 TEMPLATE-----
"""


class BAR_P01(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """BAR_P01"""
    _hl7_name = """Add Patient Accounts"""
    _hl7_description = """Data are sent from some application (usually a Registration or an ADT system) for example, to the patient accounting or financial system to establish an account for a patient’s billing/accounts receivable record"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P01"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "None")
    _c_components = (MSH, SFT, EVN, PID, PD1, ROL, BAR_P01_VISIT_GROUP)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PD1", "ROL", "VISIT")
    _c_is_group = (False, False, False, False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_additional_demographic", "role", "visit",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        visit: BAR_P01_VISIT_GROUP
        | tuple[
            BAR_P01_VISIT_GROUP, ...
        ],  #  Required. (PV1.7, PV2.8, ROL.9, DB1.10, OBX.11, AL1.12, DG1.13, DRG.14, GT1.17, NK1.18, ACC.23, UB1.24, UB2.25, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        role: ROL | tuple[ROL, ...] | None = None,  #  ROL.6
    ):
        """
                 - `BAR_P01 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P01>`_
                Data are sent from some application (usually a Registration or an ADT system) for example, to the patient accounting or financial system to establish an account for a patient’s billing/accounts receivable record.  Many of the segments associated with this event are optional.  This optionality allows those systems needing these fields to set up transactions that fulfill their requirements and yet satisfy the HL7 requirements.

        When an account’s start and end dates span a period greater than any particular visit, the P01 (add account) event should be used to transmit the opening of an account.  The A01 (admit/visit notification) event can notify systems of the creation of an account as well as notify them of a patient’s arrival in the healthcare facility.  In order to create a new account without notifying systems of a patient’s arrival, use the P01 trigger event.

        From Standard Version 2.3 onward, the P01 event should only be used to add a new account that did not exist before, not to update an existing account.  The new P05 (update account) event should be used to update an existing account.  The new P06 (end account) event should be used to close an account.  With the P01 event, EVN-2 - Recorded Date/Time should contain the account start date.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
                :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
                :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
                :param role: Role (id: ROL | seq: 6 | use: O | rpt: *)
                :param visit: Visit segment group: [PV1|None, PV2|None, ROL|None, DB1|None, OBX|None, AL1|None, DG1|None, DRG|None, PROCEDURE|None, GT1|None, NK1|None, INSURANCE|None, ACC|None, UB1|None, UB2|None] (id: VISIT | seq: 7, 8, 9, 10, 11, 12, 13, 14, None, 17, 18, None, 23, 24, 25 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.role = role
        self.visit = visit

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

    @property  # get EVN.3
    def event_type(self) -> EVN:
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        return_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        return self._c_data[2][0]

    @event_type.setter  # set EVN.3
    def event_type(self, evn: EVN):
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        param_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        self._c_data[2] = (evn,)

    @property  # get PID.4
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        return_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[3][0]

    @patient_identification.setter  # set PID.4
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        param_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[3] = (pid,)

    @property  # get PD1.5
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[4][0]

    @patient_additional_demographic.setter  # set PD1.5
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[4] = (pd1,)

    @property  # get ROL
    def role(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[5]

    @role.setter  # set ROL
    def role(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: ROL.6 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[5] = rol
        else:
            self._c_data[5] = (rol,)

    @property  # get VISIT
    def visit(self) -> tuple[BAR_P01_VISIT_GROUP, ...]:
        """
        id: BAR_P01_VISIT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[BAR_P01_VISIT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P01_VISIT_GROUP
        """
        return self._c_data[6]

    @visit.setter  # set VISIT
    def visit(self, v_isit: BAR_P01_VISIT_GROUP | tuple[BAR_P01_VISIT_GROUP, ...]):
        """
        id: VISIT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: BAR_P01_VISIT_GROUP.None | tuple[BAR_P01_VISIT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P01_VISIT_GROUP
        """
        if isinstance(v_isit, tuple):
            self._c_data[6] = v_isit
        else:
            self._c_data[6] = (v_isit,)
