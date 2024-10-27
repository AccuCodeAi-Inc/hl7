from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segment_groups.SUR_P09_FACILITY_GROUP import SUR_P09_FACILITY_GROUP


"""
Summary product experience report - SUR_P09
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::SUR_P09 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SUR_P09
from utils.hl7.v2_5_1.segments import (
    MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    SUR_P09_FACILITY_GROUP
)

sur_p09 = SUR_P09(  #  - Sending summary reports related to products constitutes a P09 event
    message_header=msh,  # MSH(...)  # Required.
    facility=sur_p09_facility_group,  # SUR_P09_FACILITY_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::SUR_P09 TEMPLATE-----
"""


class SUR_P09(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """SUR_P09"""
    _hl7_name = """Summary product experience report"""
    _hl7_description = """Sending summary reports related to products constitutes a P09 event"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SUR_P09"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "R")
    _c_aliases = ("1", "None")
    _c_components = (MSH, SUR_P09_FACILITY_GROUP)
    _c_name = ("MSH", "FACILITY")
    _c_is_group = (False, True)
    _c_attrs = ("message_header", "facility",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        facility: SUR_P09_FACILITY_GROUP
        | tuple[SUR_P09_FACILITY_GROUP, ...],  #  Required. (FAC.2, PSH.5, ...)
    ):
        """
                 - `SUR_P09 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SUR_P09>`_
                Sending summary reports related to products constitutes a P09 event.

        This message and event is deprecated for v2.5:  This message is not consistent with most message definitions and appears flawed for the following reasons:
        - The SUR message structure has no optional segments.  Even the NTE is defined as required.
        - The message contains an invalid ED segment.

        The Message contains sequences of segments that would be difficult if not impossible to parse.  For example the PSH segment is a child of an FAC segment followed by a second PSH that is the parent of another FAC segment.

        This Technical Committee invites users of the existing message and/or domain experts to submit a formal proposal for a replacement message, event and use cases that can be considered for the next v2.x ballot.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param facility: Facility segment group: [FAC, PRODUCT, PSH, FACILITY DETAIL] (id: FACILITY | seq: 2, None, 5, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.message_header = message_header
        self.facility = facility

    @property  # get MSH.1
    def message_header(self) -> MSH:
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        return_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        return self._c_data[0][0]

    @message_header.setter  # set MSH.1
    def message_header(self, msh: MSH):
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        param_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        self._c_data[0] = (msh,)

    @property  # get FACILITY
    def facility(self) -> tuple[SUR_P09_FACILITY_GROUP, ...]:
        """
        id: SUR_P09_FACILITY_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[SUR_P09_FACILITY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SUR_P09_FACILITY_GROUP
        """
        return self._c_data[1]

    @facility.setter  # set FACILITY
    def facility(
        self, facility: SUR_P09_FACILITY_GROUP | tuple[SUR_P09_FACILITY_GROUP, ...]
    ):
        """
        id: FACILITY SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: SUR_P09_FACILITY_GROUP.None | tuple[SUR_P09_FACILITY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SUR_P09_FACILITY_GROUP
        """
        if isinstance(facility, tuple):
            self._c_data[1] = facility
        else:
            self._c_data[1] = (facility,)
