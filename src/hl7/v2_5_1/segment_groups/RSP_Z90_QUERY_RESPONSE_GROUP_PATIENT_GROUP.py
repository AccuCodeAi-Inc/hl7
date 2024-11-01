from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segment_groups.RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP import (
    RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP,
)
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.NK1 import NK1


"""
PATIENT - RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    NK1, NTE, PID, PD1
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP
)

rsp_z90_query_response_group_patient_group = RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP(  # PATIENT - Segment group for RSP_Z90_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of PID, PD1|None, NK1|None, NTE|None, VISIT|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    notes_and_comments=None,  # NTE(...) 
    visit=None,  # RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP TEMPLATE-----
"""


class RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for RSP_Z90_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of PID, PD1|None, NK1|None, NTE|None, VISIT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 1)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("8", "9", "10", "11", "None")
    _c_components = (PID, PD1, NK1, NTE, RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP)
    _c_name = ("PID", "PD1", "NK1", "NTE", "VISIT")
    _c_is_group = (False, False, False, False, True)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "next_of_kin_or_associated_parties", "notes_and_comments", "visit",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.8
        patient_additional_demographic: PD1 | None = None,  #  PD1.9
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.10
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.11
        visit: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP
        | None = None,  #  PV1.12, PV2.13
    ):
        """
        None - `RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP>`_
        Segment group for RSP_Z90_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of PID, PD1|None, NK1|None, NTE|None, VISIT|None

        :param patient_identification: Patient Identification (id: PID | seq: 8 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 9 | use: O | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 10 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 11 | use: O | rpt: *)
        :param visit: Visit segment group: [PV1, PV2|None] (id: VISIT | seq: 12, 13 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.notes_and_comments = notes_and_comments
        self.visit = visit

    @property  # get PID.8
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 8
        ---
        return_type: PID.8: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.8
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 8
        ---
        param_type: PID.8: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get PD1.9
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 9
        ---
        return_type: PD1.9: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[1][0]

    @patient_additional_demographic.setter  # set PD1.9
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 9
        ---
        param_type: PD1.9: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[1] = (pd1,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[2]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: NK1.10 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[2] = nk1
        else:
            self._c_data[2] = (nk1,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: NTE.11 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP.None
    def visit(self) -> RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP | None:
        """
        id: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP
        """
        return self._c_data[4][0]

    @visit.setter  # set RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP.None
    def visit(
        self, v_isit: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP | None
    ):
        """
        id: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP
        """
        self._c_data[4] = (v_isit,)
