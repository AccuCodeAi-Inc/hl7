from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.AUT import AUT
from ..segments.CTD import CTD


"""
AUTHORIZATION CONTACT - REF_I15_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::REF_I15_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import REF_I15_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP
from utils.hl7.v2_5_1.segments import (
    CTD, AUT
)

ref_i15_procedure_group_authorization_contact_group = REF_I15_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP(  # AUTHORIZATION CONTACT - Segment group for REF_I15_PROCEDURE_GROUP - PROCEDURE consisting of AUT, CTD|None
    authorization_information=aut,  # AUT(...)  # Required.
    contact_data=None,  # CTD(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::REF_I15_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP TEMPLATE-----
"""


class REF_I15_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """REF_I15_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP"""
    _hl7_name = """AUTHORIZATION CONTACT"""
    _hl7_description = """Segment group for REF_I15_PROCEDURE_GROUP - PROCEDURE consisting of AUT, CTD|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/REF_I15_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("19", "20")
    _c_components = (AUT, CTD)
    _c_name = ("AUT", "CTD")
    _c_is_group = (False, False)
    _c_attrs = ("authorization_information", "contact_data",)
    # fmt: on

    def __init__(
        self,
        authorization_information: AUT,  #  Required. AUT.19
        contact_data: CTD | None = None,  #  CTD.20
    ):
        """
        None - `REF_I15_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/REF_I15_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP>`_
        Segment group for REF_I15_PROCEDURE_GROUP - PROCEDURE consisting of AUT, CTD|None

        :param authorization_information: Authorization Information (id: AUT | seq: 19 | use: R | rpt: 1)
        :param contact_data: Contact Data (id: CTD | seq: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.authorization_information = authorization_information
        self.contact_data = contact_data

    @property  # get AUT.19
    def authorization_information(self) -> AUT:
        """
        id: AUT | use: R | rpt: 1 | seq: 19
        ---
        return_type: AUT.19: Authorization Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AUT
        """
        return self._c_data[0][0]

    @authorization_information.setter  # set AUT.19
    def authorization_information(self, aut: AUT):
        """
        id: AUT | use: R | rpt: 1 | seq: 19
        ---
        param_type: AUT.19: Authorization Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AUT
        """
        self._c_data[0] = (aut,)

    @property  # get CTD.20
    def contact_data(self) -> CTD | None:
        """
        id: CTD | use: O | rpt: 1 | seq: 20
        ---
        return_type: CTD.20: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[1][0]

    @contact_data.setter  # set CTD.20
    def contact_data(self, ctd: CTD | None):
        """
        id: CTD | use: O | rpt: 1 | seq: 20
        ---
        param_type: CTD.20: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        self._c_data[1] = (ctd,)
