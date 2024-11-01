from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NK1 import NK1
from ..segments.QRI import QRI
from ..segments.PID import PID
from ..segments.PD1 import PD1


"""
QUERY RESPONSE - RSP_K22_QUERY_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_K22_QUERY_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_K22_QUERY_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    QRI, PD1, PID, NK1
)

rsp_k22_query_response_group = RSP_K22_QUERY_RESPONSE_GROUP(  # QUERY RESPONSE - Segment group for RSP_K22 - Find Candidates Response consisting of PID, PD1|None, NK1|None, QRI|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    query_response_instance=None,  # QRI(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_K22_QUERY_RESPONSE_GROUP TEMPLATE-----
"""


class RSP_K22_QUERY_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_K22_QUERY_RESPONSE_GROUP"""
    _hl7_name = """QUERY RESPONSE"""
    _hl7_description = """Segment group for RSP_K22 - Find Candidates Response consisting of PID, PD1|None, NK1|None, QRI|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K22_QUERY_RESPONSE_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("7", "8", "9", "10")
    _c_components = (PID, PD1, NK1, QRI)
    _c_name = ("PID", "PD1", "NK1", "QRI")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "next_of_kin_or_associated_parties", "query_response_instance",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.7
        patient_additional_demographic: PD1 | None = None,  #  PD1.8
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.9
        query_response_instance: QRI | None = None,  #  QRI.10
    ):
        """
        None - `RSP_K22_QUERY_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K22_QUERY_RESPONSE_GROUP>`_
        Segment group for RSP_K22 - Find Candidates Response consisting of PID, PD1|None, NK1|None, QRI|None

        :param patient_identification: Patient Identification (id: PID | seq: 7 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 8 | use: O | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 9 | use: O | rpt: *)
        :param query_response_instance: Query Response Instance (id: QRI | seq: 10 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.query_response_instance = query_response_instance

    @property  # get PID.7
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        return_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.7
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        param_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get PD1.8
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 8
        ---
        return_type: PD1.8: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[1][0]

    @patient_additional_demographic.setter  # set PD1.8
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 8
        ---
        param_type: PD1.8: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[1] = (pd1,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[2]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: NK1.9 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[2] = nk1
        else:
            self._c_data[2] = (nk1,)

    @property  # get QRI.10
    def query_response_instance(self) -> QRI | None:
        """
        id: QRI | use: O | rpt: 1 | seq: 10
        ---
        return_type: QRI.10: Query Response Instance
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRI
        """
        return self._c_data[3][0]

    @query_response_instance.setter  # set QRI.10
    def query_response_instance(self, qri: QRI | None):
        """
        id: QRI | use: O | rpt: 1 | seq: 10
        ---
        param_type: QRI.10: Query Response Instance
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRI
        """
        self._c_data[3] = (qri,)
