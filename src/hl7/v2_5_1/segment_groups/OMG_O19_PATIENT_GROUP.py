from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.OMG_O19_PATIENT_GROUP_INSURANCE_GROUP import (
    OMG_O19_PATIENT_GROUP_INSURANCE_GROUP,
)
from ..segments.PD1 import PD1
from ..segments.NK1 import NK1
from ..segments.AL1 import AL1
from ..segments.GT1 import GT1
from ..segments.PID import PID
from ..segments.NTE import NTE
from ..segment_groups.OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP import (
    OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP,
)


"""
PATIENT - OMG_O19_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMG_O19_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMG_O19_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    NK1, AL1, NTE, PID, PD1, GT1
)
from utils.hl7.v2_5_1.segment_groups import (
    OMG_O19_PATIENT_GROUP_INSURANCE_GROUP, OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP
)

omg_o19_patient_group = OMG_O19_PATIENT_GROUP(  # PATIENT - Segment group for OMG_O19 - General Clinical Order consisting of PID, PD1|None, NTE|None, NK1|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    notes_and_comments=None,  # NTE(...) 
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    patient_visit=None,  # OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP(...) 
    insurance=None,  # OMG_O19_PATIENT_GROUP_INSURANCE_GROUP(...) 
    guarantor=None,  # GT1(...) 
    patient_allergy_information=None,  # AL1(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMG_O19_PATIENT_GROUP TEMPLATE-----
"""


class OMG_O19_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMG_O19_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for OMG_O19 - General Clinical Order consisting of PID, PD1|None, NTE|None, NK1|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMG_O19_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 1, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("4", "5", "6", "7", "None", "None", "13", "14")
    _c_components = (PID, PD1, NTE, NK1, OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP, OMG_O19_PATIENT_GROUP_INSURANCE_GROUP, GT1, AL1)
    _c_name = ("PID", "PD1", "NTE", "NK1", "PATIENT VISIT", "INSURANCE", "GT1", "AL1")
    _c_is_group = (False, False, False, False, True, True, False, False)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "notes_and_comments", "next_of_kin_or_associated_parties", "patient_visit", "insurance", "guarantor", "patient_allergy_information",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.4
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.6
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.7
        patient_visit: OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP
        | None = None,  #  PV1.8, PV2.9
        insurance: OMG_O19_PATIENT_GROUP_INSURANCE_GROUP
        | tuple[OMG_O19_PATIENT_GROUP_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.10, IN2.11, IN3.12, ...)
        guarantor: GT1 | None = None,  #  GT1.13
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.14
    ):
        """
        None - `OMG_O19_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMG_O19_PATIENT_GROUP>`_
        Segment group for OMG_O19 - General Clinical Order consisting of PID, PD1|None, NTE|None, NK1|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None

        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 6 | use: O | rpt: *)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 7 | use: O | rpt: *)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 8, 9 | use: O | rpt: 1)
        :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None] (id: INSURANCE | seq: 10, 11, 12 | use: O | rpt: *)
        :param guarantor: Guarantor (id: GT1 | seq: 13 | use: O | rpt: 1)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 14 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.notes_and_comments = notes_and_comments
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
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

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[3]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: NK1.7 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[3] = nk1
        else:
            self._c_data[3] = (nk1,)

    @property  # get OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP | None:
        """
        id: OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        return self._c_data[4][0]

    @patient_visit.setter  # set OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(
        self, patient_v_isit: OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP | None
    ):
        """
        id: OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        self._c_data[4] = (patient_v_isit,)

    @property  # get INSURANCE
    def insurance(
        self,
    ) -> tuple[OMG_O19_PATIENT_GROUP_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: OMG_O19_PATIENT_GROUP_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMG_O19_PATIENT_GROUP_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_PATIENT_GROUP_INSURANCE_GROUP
        """
        return self._c_data[5]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: OMG_O19_PATIENT_GROUP_INSURANCE_GROUP
        | tuple[OMG_O19_PATIENT_GROUP_INSURANCE_GROUP, ...]
        | None,
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMG_O19_PATIENT_GROUP_INSURANCE_GROUP.None | tuple[OMG_O19_PATIENT_GROUP_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_PATIENT_GROUP_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[5] = insurance
        else:
            self._c_data[5] = (insurance,)

    @property  # get GT1.13
    def guarantor(self) -> GT1 | None:
        """
        id: GT1 | use: O | rpt: 1 | seq: 13
        ---
        return_type: GT1.13: Guarantor
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[6][0]

    @guarantor.setter  # set GT1.13
    def guarantor(self, gt1: GT1 | None):
        """
        id: GT1 | use: O | rpt: 1 | seq: 13
        ---
        param_type: GT1.13: Guarantor
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        self._c_data[6] = (gt1,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[7]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        param_type: AL1.14 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[7] = al1
        else:
            self._c_data[7] = (al1,)
