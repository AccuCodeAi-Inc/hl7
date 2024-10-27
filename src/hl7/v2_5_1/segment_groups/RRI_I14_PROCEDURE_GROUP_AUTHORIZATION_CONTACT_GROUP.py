from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.AUT import AUT
from ..segments.CTD import CTD


"""
AUTHORIZATION CONTACT - RRI_I14_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RRI_I14_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRI_I14_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP
from utils.hl7.v2_5_1.segments import (
    CTD, AUT
)

rri_i14_procedure_group_authorization_contact_group = RRI_I14_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP(  # AUTHORIZATION CONTACT - Segment group for RRI_I14_PROCEDURE_GROUP - PROCEDURE consisting of AUT, CTD|None
    authorization_information=aut,  # AUT(...)  # Required.
    contact_data=None,  # CTD(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RRI_I14_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP TEMPLATE-----
"""


class RRI_I14_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RRI_I14_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP"""
    _hl7_name = """AUTHORIZATION CONTACT"""
    _hl7_description = """Segment group for RRI_I14_PROCEDURE_GROUP - PROCEDURE consisting of AUT, CTD|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRI_I14_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("15", "16")
    _c_components = (AUT, CTD)
    _c_name = ("AUT", "CTD")
    _c_is_group = (False, False)
    _c_attrs = ("authorization_information", "contact_data",)
    # fmt: on

    def __init__(
        self,
        authorization_information: AUT,  #  Required. AUT.15
        contact_data: CTD | None = None,  #  CTD.16
    ):
        """
        None - `RRI_I14_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRI_I14_PROCEDURE_GROUP_AUTHORIZATION_CONTACT_GROUP>`_
        Segment group for RRI_I14_PROCEDURE_GROUP - PROCEDURE consisting of AUT, CTD|None

        :param authorization_information: Authorization Information (id: AUT | seq: 15 | use: R | rpt: 1)
        :param contact_data: Contact Data (id: CTD | seq: 16 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.authorization_information = authorization_information
        self.contact_data = contact_data

    @property  # get AUT.15
    def authorization_information(self) -> AUT:
        """
        id: AUT | use: R | rpt: 1 | seq: 15
        ---
        return_type: AUT.15: Authorization Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AUT
        """
        return self._c_data[0][0]

    @authorization_information.setter  # set AUT.15
    def authorization_information(self, aut: AUT):
        """
        id: AUT | use: R | rpt: 1 | seq: 15
        ---
        param_type: AUT.15: Authorization Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AUT
        """
        self._c_data[0] = (aut,)

    @property  # get CTD.16
    def contact_data(self) -> CTD | None:
        """
        id: CTD | use: O | rpt: 1 | seq: 16
        ---
        return_type: CTD.16: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[1][0]

    @contact_data.setter  # set CTD.16
    def contact_data(self, ctd: CTD | None):
        """
        id: CTD | use: O | rpt: 1 | seq: 16
        ---
        param_type: CTD.16: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        self._c_data[1] = (ctd,)
