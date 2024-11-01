from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.NDS import NDS


"""
NOTIFICATION - EAN_U09_NOTIFICATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::EAN_U09_NOTIFICATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import EAN_U09_NOTIFICATION_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, NDS
)

ean_u09_notification_group = EAN_U09_NOTIFICATION_GROUP(  # NOTIFICATION - Segment group for EAN_U09 - Automated equipment notification consisting of NDS, NTE|None
    notification_detail=nds,  # NDS(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::EAN_U09_NOTIFICATION_GROUP TEMPLATE-----
"""


class EAN_U09_NOTIFICATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """EAN_U09_NOTIFICATION_GROUP"""
    _hl7_name = """NOTIFICATION"""
    _hl7_description = """Segment group for EAN_U09 - Automated equipment notification consisting of NDS, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EAN_U09_NOTIFICATION_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("4", "5")
    _c_components = (NDS, NTE)
    _c_name = ("NDS", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("notification_detail", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        notification_detail: NDS,  #  Required. NDS.4
        notes_and_comments: NTE | None = None,  #  NTE.5
    ):
        """
        None - `EAN_U09_NOTIFICATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EAN_U09_NOTIFICATION_GROUP>`_
        Segment group for EAN_U09 - Automated equipment notification consisting of NDS, NTE|None

        :param notification_detail: Notification Detail (id: NDS | seq: 4 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 5 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.notification_detail = notification_detail
        self.notes_and_comments = notes_and_comments

    @property  # get NDS.4
    def notification_detail(self) -> NDS:
        """
        id: NDS | use: R | rpt: 1 | seq: 4
        ---
        return_type: NDS.4: Notification Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NDS
        """
        return self._c_data[0][0]

    @notification_detail.setter  # set NDS.4
    def notification_detail(self, nds: NDS):
        """
        id: NDS | use: R | rpt: 1 | seq: 4
        ---
        param_type: NDS.4: Notification Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NDS
        """
        self._c_data[0] = (nds,)

    @property  # get NTE.5
    def notes_and_comments(self) -> NTE | None:
        """
        id: NTE | use: O | rpt: 1 | seq: 5
        ---
        return_type: NTE.5: Notes and Comments
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1][0]

    @notes_and_comments.setter  # set NTE.5
    def notes_and_comments(self, nte: NTE | None):
        """
        id: NTE | use: O | rpt: 1 | seq: 5
        ---
        param_type: NTE.5: Notes and Comments
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        self._c_data[1] = (nte,)
