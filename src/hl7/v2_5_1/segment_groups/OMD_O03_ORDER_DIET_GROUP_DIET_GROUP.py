from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segment_groups.OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP import (
    OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP,
)
from ..segments.ODS import ODS


"""
DIET - OMD_O03_ORDER_DIET_GROUP_DIET_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMD_O03_ORDER_DIET_GROUP_DIET_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMD_O03_ORDER_DIET_GROUP_DIET_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, ODS
)
from utils.hl7.v2_5_1.segment_groups import (
    OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP
)

omd_o03_order_diet_group_diet_group = OMD_O03_ORDER_DIET_GROUP_DIET_GROUP(  # DIET - Segment group for OMD_O03_ORDER_DIET_GROUP - ORDER DIET consisting of ODS, NTE|None, OBSERVATION|None
    dietary_orders_supplements_and_preferences=ods,  # ODS(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    observation=None,  # OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMD_O03_ORDER_DIET_GROUP_DIET_GROUP TEMPLATE-----
"""


class OMD_O03_ORDER_DIET_GROUP_DIET_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMD_O03_ORDER_DIET_GROUP_DIET_GROUP"""
    _hl7_name = """DIET"""
    _hl7_description = """Segment group for OMD_O03_ORDER_DIET_GROUP - ORDER DIET consisting of ODS, NTE|None, OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMD_O03_ORDER_DIET_GROUP_DIET_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (65535, 65535, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("17", "18", "None")
    _c_components = (ODS, NTE, OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP)
    _c_name = ("ODS", "NTE", "OBSERVATION")
    _c_is_group = (False, False, True)
    _c_attrs = ("dietary_orders_supplements_and_preferences", "notes_and_comments", "observation",)
    # fmt: on

    def __init__(
        self,
        dietary_orders_supplements_and_preferences: ODS
        | tuple[ODS, ...],  #  Required. ODS.17
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.18
        observation: OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP
        | tuple[OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.19, NTE.20, ...)
    ):
        """
        None - `OMD_O03_ORDER_DIET_GROUP_DIET_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMD_O03_ORDER_DIET_GROUP_DIET_GROUP>`_
        Segment group for OMD_O03_ORDER_DIET_GROUP - ORDER DIET consisting of ODS, NTE|None, OBSERVATION|None

        :param dietary_orders_supplements_and_preferences: Dietary Orders, Supplements, and Preferences (id: ODS | seq: 17 | use: R | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 18 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 19, 20 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.dietary_orders_supplements_and_preferences = (
            dietary_orders_supplements_and_preferences
        )
        self.notes_and_comments = notes_and_comments
        self.observation = observation

    @property  # get ODS
    def dietary_orders_supplements_and_preferences(self) -> tuple[ODS, ...]:
        """
        id: ODS SEGMENT GROUP | use: R | rpt: * | seq: 17
        ---
        return_type: tuple[ODS, ...]: (Dietary Orders, Supplements, and Preferences, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODS
        """
        return self._c_data[0]

    @dietary_orders_supplements_and_preferences.setter  # set ODS
    def dietary_orders_supplements_and_preferences(self, ods: ODS | tuple[ODS, ...]):
        """
        id: ODS SEGMENT GROUP | use: R | rpt: * | seq: 17
        ---
        param_type: ODS.17 | tuple[ODS, ...]: (Dietary Orders, Supplements, and Preferences, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODS
        """
        if isinstance(ods, tuple):
            self._c_data[0] = ods
        else:
            self._c_data[0] = (ods,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        param_type: NTE.18 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> (
        tuple[OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP, ...] | tuple[None]
    ):
        """
        id: OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[2]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP
        | tuple[OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP.None | tuple[OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_DIET_GROUP_DIET_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[2] = observation
        else:
            self._c_data[2] = (observation,)
