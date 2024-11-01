from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP import (
    RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP,
)
from ..segments.PR1 import PR1


"""
PROCEDURE - RRI_I12_PROCEDURE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RRI_I12_PROCEDURE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRI_I12_PROCEDURE_GROUP
from utils.hl7.v2_5_1.segments import (
    PR1
)
from utils.hl7.v2_5_1.segment_groups import (
    RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP
)

rri_i12_procedure_group = RRI_I12_PROCEDURE_GROUP(  # PROCEDURE - Segment group for RRI_I12 - Patient referral acknowledgement consisting of PR1, AUTHORIZATION CONTACT|None
    procedures=pr1,  # PR1(...)  # Required.
    authorization_contact=None,  # RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RRI_I12_PROCEDURE_GROUP TEMPLATE-----
"""


class RRI_I12_PROCEDURE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RRI_I12_PROCEDURE_GROUP"""
    _hl7_name = """PROCEDURE"""
    _hl7_description = """Segment group for RRI_I12 - Patient referral acknowledgement consisting of PR1, AUTHORIZATION CONTACT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRI_I12_PROCEDURE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("14", "None")
    _c_components = (PR1, RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP)
    _c_name = ("PR1", "AUTHORIZATION CONTACT")
    _c_is_group = (False, True)
    _c_attrs = ("procedures", "authorization_contact",)
    # fmt: on

    def __init__(
        self,
        procedures: PR1,  #  Required. PR1.14
        authorization_contact: RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP
        | None = None,  #  AUT.15, CTD.16
    ):
        """
        None - `RRI_I12_PROCEDURE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRI_I12_PROCEDURE_GROUP>`_
        Segment group for RRI_I12 - Patient referral acknowledgement consisting of PR1, AUTHORIZATION CONTACT|None

        :param procedures: Procedures (id: PR1 | seq: 14 | use: R | rpt: 1)
        :param authorization_contact: Authorization Contact segment group: [AUT, CTD|None] (id: AUTHORIZATION CONTACT | seq: 15, 16 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.procedures = procedures
        self.authorization_contact = authorization_contact

    @property  # get PR1.14
    def procedures(self) -> PR1:
        """
        id: PR1 | use: R | rpt: 1 | seq: 14
        ---
        return_type: PR1.14: Procedures
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1
        """
        return self._c_data[0][0]

    @procedures.setter  # set PR1.14
    def procedures(self, pr1: PR1):
        """
        id: PR1 | use: R | rpt: 1 | seq: 14
        ---
        param_type: PR1.14: Procedures
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1
        """
        self._c_data[0] = (pr1,)

    @property  # get RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP.None
    def authorization_contact(
        self,
    ) -> RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP | None:
        """
        id: RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP
        """
        return self._c_data[1][0]

    @authorization_contact.setter  # set RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP.None
    def authorization_contact(
        self,
        authorization_contact: RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP
        | None,
    ):
        """
        id: RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I12_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP
        """
        self._c_data[1] = (authorization_contact,)
