from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NK1 import NK1
from ..segments.PID import PID


"""
PATIENT - VXX_V02_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::VXX_V02_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import VXX_V02_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    NK1, PID
)

vxx_v02_patient_group = VXX_V02_PATIENT_GROUP(  # PATIENT - Segment group for VXX_V02 - Vaccination Record Query Returning Multiple PID Matches consisting of PID, NK1|None
    patient_identification=pid,  # PID(...)  # Required.
    next_of_kin_or_associated_parties=None,  # NK1(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::VXX_V02_PATIENT_GROUP TEMPLATE-----
"""


class VXX_V02_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """VXX_V02_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for VXX_V02 - Vaccination Record Query Returning Multiple PID Matches consisting of PID, NK1|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXX_V02_PATIENT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("6", "7")
    _c_components = (PID, NK1)
    _c_name = ("PID", "NK1")
    _c_is_group = (False, False)
    _c_attrs = ("patient_identification", "next_of_kin_or_associated_parties",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.6
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.7
    ):
        """
        None - `VXX_V02_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXX_V02_PATIENT_GROUP>`_
        Segment group for VXX_V02 - Vaccination Record Query Returning Multiple PID Matches consisting of PID, NK1|None

        :param patient_identification: Patient Identification (id: PID | seq: 6 | use: R | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 7 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient_identification = patient_identification
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties

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

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[1]

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
            self._c_data[1] = nk1
        else:
            self._c_data[1] = (nk1,)
