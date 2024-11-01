from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP import (
    RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP,
)
from ..segments.PD1 import PD1
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.AL1 import AL1


"""
PATIENT - RSP_K31_RESPONSE_GROUP_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_K31_RESPONSE_GROUP_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_K31_RESPONSE_GROUP_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, PD1, PID, AL1
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP
)

rsp_k31_response_group_patient_group = RSP_K31_RESPONSE_GROUP_PATIENT_GROUP(  # PATIENT - Segment group for RSP_K31_RESPONSE_GROUP - RESPONSE consisting of PID, PD1|None, NTE|None, AL1|None, PATIENT VISIT|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    notes_and_comments=None,  # NTE(...) 
    patient_allergy_information=None,  # AL1(...) 
    patient_visit=None,  # RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_K31_RESPONSE_GROUP_PATIENT_GROUP TEMPLATE-----
"""


class RSP_K31_RESPONSE_GROUP_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_K31_RESPONSE_GROUP_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for RSP_K31_RESPONSE_GROUP - RESPONSE consisting of PID, PD1|None, NTE|None, AL1|None, PATIENT VISIT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K31_RESPONSE_GROUP_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 1)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("8", "9", "10", "11", "None")
    _c_components = (PID, PD1, NTE, AL1, RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP)
    _c_name = ("PID", "PD1", "NTE", "AL1", "PATIENT VISIT")
    _c_is_group = (False, False, False, False, True)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "notes_and_comments", "patient_allergy_information", "patient_visit",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.8
        patient_additional_demographic: PD1 | None = None,  #  PD1.9
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.10
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.11
        patient_visit: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP
        | None = None,  #  PV1.12, PV2.13
    ):
        """
        None - `RSP_K31_RESPONSE_GROUP_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K31_RESPONSE_GROUP_PATIENT_GROUP>`_
        Segment group for RSP_K31_RESPONSE_GROUP - RESPONSE consisting of PID, PD1|None, NTE|None, AL1|None, PATIENT VISIT|None

        :param patient_identification: Patient Identification (id: PID | seq: 8 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 9 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 10 | use: O | rpt: *)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 11 | use: O | rpt: *)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 12, 13 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.notes_and_comments = notes_and_comments
        self.patient_allergy_information = patient_allergy_information
        self.patient_visit = patient_visit

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

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: NTE.10 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[3]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: AL1.11 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[3] = al1
        else:
            self._c_data[3] = (al1,)

    @property  # get RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(
        self,
    ) -> RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP | None:
        """
        id: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        return self._c_data[4][0]

    @patient_visit.setter  # set RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(
        self,
        patient_v_isit: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP | None,
    ):
        """
        id: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        self._c_data[4] = (patient_v_isit,)
