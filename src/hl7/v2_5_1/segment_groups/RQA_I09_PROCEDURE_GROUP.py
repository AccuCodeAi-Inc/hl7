from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP import (
    RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP,
)
from ..segments.PR1 import PR1


"""
PROCEDURE - RQA_I09_PROCEDURE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RQA_I09_PROCEDURE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RQA_I09_PROCEDURE_GROUP
from utils.hl7.v2_5_1.segments import (
    PR1
)
from utils.hl7.v2_5_1.segment_groups import (
    RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP
)

rqa_i09_procedure_group = RQA_I09_PROCEDURE_GROUP(  # PROCEDURE - Segment group for RQA_I09 - Request for modification to an authorization consisting of PR1, AUTHORIZATION|None
    procedures=pr1,  # PR1(...)  # Required.
    authorization=None,  # RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RQA_I09_PROCEDURE_GROUP TEMPLATE-----
"""


class RQA_I09_PROCEDURE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RQA_I09_PROCEDURE_GROUP"""
    _hl7_name = """PROCEDURE"""
    _hl7_description = """Segment group for RQA_I09 - Request for modification to an authorization consisting of PR1, AUTHORIZATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQA_I09_PROCEDURE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("18", "None")
    _c_components = (PR1, RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP)
    _c_name = ("PR1", "AUTHORIZATION")
    _c_is_group = (False, True)
    _c_attrs = ("procedures", "authorization",)
    # fmt: on

    def __init__(
        self,
        procedures: PR1,  #  Required. PR1.18
        authorization: RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP
        | None = None,  #  AUT.19, CTD.20
    ):
        """
        None - `RQA_I09_PROCEDURE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQA_I09_PROCEDURE_GROUP>`_
        Segment group for RQA_I09 - Request for modification to an authorization consisting of PR1, AUTHORIZATION|None

        :param procedures: Procedures (id: PR1 | seq: 18 | use: R | rpt: 1)
        :param authorization: Authorization segment group: [AUT, CTD|None] (id: AUTHORIZATION | seq: 19, 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.procedures = procedures
        self.authorization = authorization

    @property  # get PR1.18
    def procedures(self) -> PR1:
        """
        id: PR1 | use: R | rpt: 1 | seq: 18
        ---
        return_type: PR1.18: Procedures
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1
        """
        return self._c_data[0][0]

    @procedures.setter  # set PR1.18
    def procedures(self, pr1: PR1):
        """
        id: PR1 | use: R | rpt: 1 | seq: 18
        ---
        param_type: PR1.18: Procedures
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1
        """
        self._c_data[0] = (pr1,)

    @property  # get RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP.None
    def authorization(self) -> RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP | None:
        """
        id: RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP
        """
        return self._c_data[1][0]

    @authorization.setter  # set RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP.None
    def authorization(
        self, authorization: RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP | None
    ):
        """
        id: RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQA_I09_PROCEDURE_GROUP_AUTHORIZATION_GROUP
        """
        self._c_data[1] = (authorization,)
