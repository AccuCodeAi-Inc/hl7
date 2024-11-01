from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PID import PID
from ..segment_groups.ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP import (
    ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP,
)


"""
PATIENT - ORL_O36_RESPONSE_GROUP_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORL_O36_RESPONSE_GROUP_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORL_O36_RESPONSE_GROUP_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID
)
from utils.hl7.v2_5_1.segment_groups import (
    ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP
)

orl_o36_response_group_patient_group = ORL_O36_RESPONSE_GROUP_PATIENT_GROUP(  # PATIENT - Segment group for ORL_O36_RESPONSE_GROUP - RESPONSE consisting of PID, SPECIMEN
    patient_identification=pid,  # PID(...)  # Required.
    specimen=orl_o36_response_group_patient_group_specimen_group,  # ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORL_O36_RESPONSE_GROUP_PATIENT_GROUP TEMPLATE-----
"""


class ORL_O36_RESPONSE_GROUP_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORL_O36_RESPONSE_GROUP_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for ORL_O36_RESPONSE_GROUP - RESPONSE consisting of PID, SPECIMEN"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "R")
    _c_aliases = ("6", "None")
    _c_components = (PID, ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP)
    _c_name = ("PID", "SPECIMEN")
    _c_is_group = (False, True)
    _c_attrs = ("patient_identification", "specimen",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.6
        specimen: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP
        | tuple[
            ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP, ...
        ],  #  Required. (SPM.7, OBX.8, ...)
    ):
        """
        None - `ORL_O36_RESPONSE_GROUP_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP>`_
        Segment group for ORL_O36_RESPONSE_GROUP - RESPONSE consisting of PID, SPECIMEN

        :param patient_identification: Patient Identification (id: PID | seq: 6 | use: R | rpt: 1)
        :param specimen: Specimen segment group: [SPM, OBX|None, SPECIMEN CONTAINER] (id: SPECIMEN | seq: 7, 8, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient_identification = patient_identification
        self.specimen = specimen

    @property  # get PID.6
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 6
        ---
        return_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.6
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 6
        ---
        param_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get SPECIMEN
    def specimen(
        self,
    ) -> tuple[ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP, ...]:
        """
        id: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP
        """
        return self._c_data[1]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self,
        specimen: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP
        | tuple[ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP, ...],
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP.None | tuple[ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[1] = specimen
        else:
            self._c_data[1] = (specimen,)
