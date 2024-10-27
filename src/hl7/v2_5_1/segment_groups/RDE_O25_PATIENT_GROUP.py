from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.AL1 import AL1
from ..segments.NTE import NTE
from ..segments.GT1 import GT1
from ..segment_groups.RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP import (
    RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP,
)
from ..segments.PID import PID
from ..segment_groups.RDE_O25_PATIENT_GROUP_INSURANCE_GROUP import (
    RDE_O25_PATIENT_GROUP_INSURANCE_GROUP,
)
from ..segments.PD1 import PD1


"""
PATIENT - RDE_O25_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RDE_O25_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RDE_O25_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, GT1, PD1, AL1, PID
)
from utils.hl7.v2_5_1.segment_groups import (
    RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP, RDE_O25_PATIENT_GROUP_INSURANCE_GROUP
)

rde_o25_patient_group = RDE_O25_PATIENT_GROUP(  # PATIENT - Segment group for RDE_O25 - Pharmacy/Treatment Refill Authorization Request consisting of PID, PD1|None, NTE|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    notes_and_comments=None,  # NTE(...) 
    patient_visit=None,  # RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP(...) 
    insurance=None,  # RDE_O25_PATIENT_GROUP_INSURANCE_GROUP(...) 
    guarantor=None,  # GT1(...) 
    patient_allergy_information=None,  # AL1(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RDE_O25_PATIENT_GROUP TEMPLATE-----
"""


class RDE_O25_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RDE_O25_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for RDE_O25 - Pharmacy/Treatment Refill Authorization Request consisting of PID, PD1|None, NTE|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDE_O25_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("4", "5", "6", "None", "None", "12", "13")
    _c_components = (PID, PD1, NTE, RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP, RDE_O25_PATIENT_GROUP_INSURANCE_GROUP, GT1, AL1)
    _c_name = ("PID", "PD1", "NTE", "PATIENT VISIT", "INSURANCE", "GT1", "AL1")
    _c_is_group = (False, False, False, True, True, False, False)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "notes_and_comments", "patient_visit", "insurance", "guarantor", "patient_allergy_information",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.4
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.6
        patient_visit: RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP
        | None = None,  #  PV1.7, PV2.8
        insurance: RDE_O25_PATIENT_GROUP_INSURANCE_GROUP
        | tuple[RDE_O25_PATIENT_GROUP_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.9, IN2.10, IN3.11, ...)
        guarantor: GT1 | None = None,  #  GT1.12
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.13
    ):
        """
        None - `RDE_O25_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDE_O25_PATIENT_GROUP>`_
        Segment group for RDE_O25 - Pharmacy/Treatment Refill Authorization Request consisting of PID, PD1|None, NTE|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None

        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 6 | use: O | rpt: *)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 7, 8 | use: O | rpt: 1)
        :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None] (id: INSURANCE | seq: 9, 10, 11 | use: O | rpt: *)
        :param guarantor: Guarantor (id: GT1 | seq: 12 | use: O | rpt: 1)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 13 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.notes_and_comments = notes_and_comments
        self.patient_visit = patient_visit
        self.insurance = insurance
        self.guarantor = guarantor
        self.patient_allergy_information = patient_allergy_information

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

    @property  # get RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP | None:
        """
        id: RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        return self._c_data[3][0]

    @patient_visit.setter  # set RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(
        self, patient_v_isit: RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP | None
    ):
        """
        id: RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O25_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        self._c_data[3] = (patient_v_isit,)

    @property  # get INSURANCE
    def insurance(
        self,
    ) -> tuple[RDE_O25_PATIENT_GROUP_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: RDE_O25_PATIENT_GROUP_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RDE_O25_PATIENT_GROUP_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O25_PATIENT_GROUP_INSURANCE_GROUP
        """
        return self._c_data[4]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: RDE_O25_PATIENT_GROUP_INSURANCE_GROUP
        | tuple[RDE_O25_PATIENT_GROUP_INSURANCE_GROUP, ...]
        | None,
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RDE_O25_PATIENT_GROUP_INSURANCE_GROUP.None | tuple[RDE_O25_PATIENT_GROUP_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O25_PATIENT_GROUP_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[4] = insurance
        else:
            self._c_data[4] = (insurance,)

    @property  # get GT1.12
    def guarantor(self) -> GT1 | None:
        """
        id: GT1 | use: O | rpt: 1 | seq: 12
        ---
        return_type: GT1.12: Guarantor
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[5][0]

    @guarantor.setter  # set GT1.12
    def guarantor(self, gt1: GT1 | None):
        """
        id: GT1 | use: O | rpt: 1 | seq: 12
        ---
        param_type: GT1.12: Guarantor
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        self._c_data[5] = (gt1,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[6]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        param_type: AL1.13 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[6] = al1
        else:
            self._c_data[6] = (al1,)
