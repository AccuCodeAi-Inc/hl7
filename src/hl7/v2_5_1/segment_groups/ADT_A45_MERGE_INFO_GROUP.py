from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.MRG import MRG
from ..segments.PV1 import PV1


"""
MERGE INFO - ADT_A45_MERGE_INFO_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ADT_A45_MERGE_INFO_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A45_MERGE_INFO_GROUP
from utils.hl7.v2_5_1.segments import (
    PV1, MRG
)

adt_a45_merge_info_group = ADT_A45_MERGE_INFO_GROUP(  # MERGE INFO - Segment group for ADT_A45 - Move Visit Information - Visit Number consisting of MRG, PV1
    merge_patient_information=mrg,  # MRG(...)  # Required.
    patient_visit=pv1,  # PV1(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ADT_A45_MERGE_INFO_GROUP TEMPLATE-----
"""


class ADT_A45_MERGE_INFO_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ADT_A45_MERGE_INFO_GROUP"""
    _hl7_name = """MERGE INFO"""
    _hl7_description = """Segment group for ADT_A45 - Move Visit Information - Visit Number consisting of MRG, PV1"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A45_MERGE_INFO_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "R")
    _c_aliases = ("6", "7")
    _c_components = (MRG, PV1)
    _c_name = ("MRG", "PV1")
    _c_is_group = (False, False)
    _c_attrs = ("merge_patient_information", "patient_visit",)
    # fmt: on

    def __init__(
        self,
        merge_patient_information: MRG,  #  Required. MRG.6
        patient_visit: PV1,  #  Required. PV1.7
    ):
        """
        None - `ADT_A45_MERGE_INFO_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A45_MERGE_INFO_GROUP>`_
        Segment group for ADT_A45 - Move Visit Information - Visit Number consisting of MRG, PV1

        :param merge_patient_information: Merge Patient Information (id: MRG | seq: 6 | use: R | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 7 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.merge_patient_information = merge_patient_information
        self.patient_visit = patient_visit

    @property  # get MRG.6
    def merge_patient_information(self) -> MRG:
        """
        id: MRG | use: R | rpt: 1 | seq: 6
        ---
        return_type: MRG.6: Merge Patient Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MRG
        """
        return self._c_data[0][0]

    @merge_patient_information.setter  # set MRG.6
    def merge_patient_information(self, mrg: MRG):
        """
        id: MRG | use: R | rpt: 1 | seq: 6
        ---
        param_type: MRG.6: Merge Patient Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MRG
        """
        self._c_data[0] = (mrg,)

    @property  # get PV1.7
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 7
        ---
        return_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[1][0]

    @patient_visit.setter  # set PV1.7
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 7
        ---
        param_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[1] = (pv1,)
