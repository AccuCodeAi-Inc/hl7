from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.AL1 import AL1
from ..segments.PID import PID
from ..segment_groups.RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP import (
    RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP,
)
from ..segments.NTE import NTE


"""
PATIENT - RGV_O15_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RGV_O15_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RGV_O15_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID, NTE, AL1
)
from utils.hl7.v2_5_1.segment_groups import (
    RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP
)

rgv_o15_patient_group = RGV_O15_PATIENT_GROUP(  # PATIENT - Segment group for RGV_O15 - Pharmacy/Treatment Give consisting of PID, NTE|None, AL1|None, PATIENT VISIT|None
    patient_identification=pid,  # PID(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    patient_allergy_information=None,  # AL1(...) 
    patient_visit=None,  # RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RGV_O15_PATIENT_GROUP TEMPLATE-----
"""


class RGV_O15_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RGV_O15_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for RGV_O15 - Pharmacy/Treatment Give consisting of PID, NTE|None, AL1|None, PATIENT VISIT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGV_O15_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("4", "5", "6", "None")
    _c_components = (PID, NTE, AL1, RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP)
    _c_name = ("PID", "NTE", "AL1", "PATIENT VISIT")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("patient_identification", "notes_and_comments", "patient_allergy_information", "patient_visit",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.4
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.5
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.6
        patient_visit: RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP
        | None = None,  #  PV1.7, PV2.8
    ):
        """
        None - `RGV_O15_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGV_O15_PATIENT_GROUP>`_
        Segment group for RGV_O15 - Pharmacy/Treatment Give consisting of PID, NTE|None, AL1|None, PATIENT VISIT|None

        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 5 | use: O | rpt: *)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 6 | use: O | rpt: *)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 7, 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.patient_identification = patient_identification
        self.notes_and_comments = notes_and_comments
        self.patient_allergy_information = patient_allergy_information
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

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

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
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[2]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: AL1.6 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[2] = al1
        else:
            self._c_data[2] = (al1,)

    @property  # get RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP | None:
        """
        id: RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        return self._c_data[3][0]

    @patient_visit.setter  # set RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(
        self, patient_v_isit: RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP | None
    ):
        """
        id: RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        self._c_data[3] = (patient_v_isit,)