from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PID import PID
from ..segments.NTE import NTE
from ..segment_groups.BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP import (
    BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP,
)
from ..segments.PD1 import PD1


"""
PATIENT - BTS_O31_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::BTS_O31_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BTS_O31_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, PID, PD1
)
from utils.hl7.v2_5_1.segment_groups import (
    BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP
)

bts_o31_patient_group = BTS_O31_PATIENT_GROUP(  # PATIENT - Segment group for BTS_O31 - Blood Product Transfusion/Disposition consisting of PID, PD1|None, NTE|None, PATIENT VISIT|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    notes_and_comments=None,  # NTE(...) 
    patient_visit=None,  # BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::BTS_O31_PATIENT_GROUP TEMPLATE-----
"""


class BTS_O31_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """BTS_O31_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for BTS_O31 - Blood Product Transfusion/Disposition consisting of PID, PD1|None, NTE|None, PATIENT VISIT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BTS_O31_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("4", "5", "6", "None")
    _c_components = (PID, PD1, NTE, BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP)
    _c_name = ("PID", "PD1", "NTE", "PATIENT VISIT")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "notes_and_comments", "patient_visit",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.4
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.6
        patient_visit: BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP
        | None = None,  #  PV1.7, PV2.8
    ):
        """
        None - `BTS_O31_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BTS_O31_PATIENT_GROUP>`_
        Segment group for BTS_O31 - Blood Product Transfusion/Disposition consisting of PID, PD1|None, NTE|None, PATIENT VISIT|None

        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 6 | use: O | rpt: *)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 7, 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.notes_and_comments = notes_and_comments
        self.patient_visit = patient_visit

    @property  # get PID.4
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        return_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.4
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        param_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get PD1.5
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[1][0]

    @patient_additional_demographic.setter  # set PD1.5
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[1] = (pd1,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: NTE.6 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP | None:
        """
        id: BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        return self._c_data[3][0]

    @patient_visit.setter  # set BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(
        self, patient_v_isit: BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP | None
    ):
        """
        id: BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BTS_O31_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        self._c_data[3] = (patient_v_isit,)
