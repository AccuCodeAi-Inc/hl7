from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PR1 import PR1
from ..segment_groups.RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP import (
    RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP,
)


"""
PROCEDURE - RPA_I08_PROCEDURE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RPA_I08_PROCEDURE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RPA_I08_PROCEDURE_GROUP
from utils.hl7.v2_5_1.segments import (
    PR1
)
from utils.hl7.v2_5_1.segment_groups import (
    RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP
)

rpa_i08_procedure_group = RPA_I08_PROCEDURE_GROUP(  # PROCEDURE - Segment group for RPA_I08 - Request for treatment authorization information acknowledgement consisting of PR1, AUTHORIZATION|None
    procedures=pr1,  # PR1(...)  # Required.
    authorization=None,  # RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RPA_I08_PROCEDURE_GROUP TEMPLATE-----
"""


class RPA_I08_PROCEDURE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RPA_I08_PROCEDURE_GROUP"""
    _hl7_name = """PROCEDURE"""
    _hl7_description = """Segment group for RPA_I08 - Request for treatment authorization information acknowledgement consisting of PR1, AUTHORIZATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPA_I08_PROCEDURE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("19", "None")
    _c_components = (PR1, RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP)
    _c_name = ("PR1", "AUTHORIZATION")
    _c_is_group = (False, True)
    _c_attrs = ("procedures", "authorization",)
    # fmt: on

    def __init__(
        self,
        procedures: PR1,  #  Required. PR1.19
        authorization: RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP
        | None = None,  #  AUT.20, CTD.21
    ):
        """
        None - `RPA_I08_PROCEDURE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPA_I08_PROCEDURE_GROUP>`_
        Segment group for RPA_I08 - Request for treatment authorization information acknowledgement consisting of PR1, AUTHORIZATION|None

        :param procedures: Procedures (id: PR1 | seq: 19 | use: R | rpt: 1)
        :param authorization: Authorization segment group: [AUT, CTD|None] (id: AUTHORIZATION | seq: 20, 21 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.procedures = procedures
        self.authorization = authorization

    @property  # get PR1.19
    def procedures(self) -> PR1:
        """
        id: PR1 | use: R | rpt: 1 | seq: 19
        ---
        return_type: PR1.19: Procedures
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1
        """
        return self._c_data[0][0]

    @procedures.setter  # set PR1.19
    def procedures(self, pr1: PR1):
        """
        id: PR1 | use: R | rpt: 1 | seq: 19
        ---
        param_type: PR1.19: Procedures
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1
        """
        self._c_data[0] = (pr1,)

    @property  # get RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP.None
    def authorization(self) -> RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP | None:
        """
        id: RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP
        """
        return self._c_data[1][0]

    @authorization.setter  # set RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP.None
    def authorization(
        self, authorization: RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP | None
    ):
        """
        id: RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I08_PROCEDURE_GROUP_AUTHORIZATION_GROUP
        """
        self._c_data[1] = (authorization,)
