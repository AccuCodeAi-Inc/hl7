from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP import (
    RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP,
)
from ..segment_groups.RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP import (
    RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP,
)
from ..segment_groups.RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP import (
    RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP,
)
from ..segment_groups.RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP import (
    RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segment_groups.RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP import (
    RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP,
)
from ..segment_groups.RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP import (
    RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP,
)
from ..segment_groups.RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP import (
    RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP,
)
from ..segments.ORC import ORC


"""
COMMON ORDER - RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP
)

rsp_z86_query_response_group_common_order_group = RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP(  # COMMON ORDER - Segment group for RSP_Z86_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODED ORDER|None, DISPENSE|None, GIVE|None, ADMINISTRATION|None, OBSERVATION
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP(...) 
    order_detail=None,  # RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP(...) 
    encoded_order=None,  # RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP(...) 
    dispense=None,  # RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP(...) 
    give=None,  # RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP(...) 
    administration=None,  # RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP(...) 
    observation=rsp_z86_query_response_group_common_order_group_observation_group,  # RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP TEMPLATE-----
"""


class RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP"""
    _hl7_name = """COMMON ORDER"""
    _hl7_description = """Segment group for RSP_Z86_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODED ORDER|None, DISPENSE|None, GIVE|None, ADMINISTRATION|None, OBSERVATION"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "R")
    _c_aliases = ("11", "None", "None", "None", "None", "None", "None", "None")
    _c_components = (ORC, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP)
    _c_name = ("ORC", "TIMING", "ORDER DETAIL", "ENCODED ORDER", "DISPENSE", "GIVE", "ADMINISTRATION", "OBSERVATION")
    _c_is_group = (False, True, True, True, True, True, True, True)
    _c_attrs = ("common_order", "timing", "order_detail", "encoded_order", "dispense", "give", "administration", "observation",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.11
        observation: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[
            RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...
        ],  #  Required. (OBX.31, NTE.32, ...)
        timing: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP
        | tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.12, TQ2.13, ...)
        order_detail: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP
        | None = None,  #  RXO.14, RXR.15, RXC.16
        encoded_order: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP
        | None = None,  #  RXE.17, RXR.20, RXC.21
        dispense: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP
        | None = None,  #  RXD.22, RXR.23, RXC.24
        give: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP
        | None = None,  #  RXG.25, RXR.26, RXC.27
        administration: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP
        | None = None,  #  RXA.28, RXR.29, RXC.30
    ):
        """
        None - `RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP>`_
        Segment group for RSP_Z86_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODED ORDER|None, DISPENSE|None, GIVE|None, ADMINISTRATION|None, OBSERVATION

        :param common_order: Common Order (id: ORC | seq: 11 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 12, 13 | use: O | rpt: *)
        :param order_detail: Order Detail segment group: [RXO, RXR, RXC|None] (id: ORDER DETAIL | seq: 14, 15, 16 | use: O | rpt: 1)
        :param encoded_order: Encoded Order segment group: [RXE, TIMING ENCODED|None, RXR, RXC|None] (id: ENCODED ORDER | seq: 17, None, 20, 21 | use: O | rpt: 1)
        :param dispense: Dispense segment group: [RXD, RXR, RXC|None] (id: DISPENSE | seq: 22, 23, 24 | use: O | rpt: 1)
        :param give: Give segment group: [RXG, RXR, RXC|None] (id: GIVE | seq: 25, 26, 27 | use: O | rpt: 1)
        :param administration: Administration segment group: [RXA, RXR, RXC|None] (id: ADMINISTRATION | seq: 28, 29, 30 | use: O | rpt: 1)
        :param observation: Observation segment group: [OBX|None, NTE|None] (id: OBSERVATION | seq: 31, 32 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.common_order = common_order
        self.timing = timing
        self.order_detail = order_detail
        self.encoded_order = encoded_order
        self.dispense = dispense
        self.give = give
        self.administration = administration
        self.observation = observation

    @property  # get ORC.11
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 11
        ---
        return_type: ORC.11: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.11
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 11
        ---
        param_type: ORC.11: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(
        self,
    ) -> (
        tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, ...]
        | tuple[None]
    ):
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP
        | tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP.None | tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(
        self,
    ) -> RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP | None:
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        return self._c_data[2][0]

    @order_detail.setter  # set RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(
        self,
        order_detail: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP
        | None,
    ):
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        self._c_data[2] = (order_detail,)

    @property  # get RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP.None
    def encoded_order(
        self,
    ) -> RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP | None:
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP
        """
        return self._c_data[3][0]

    @encoded_order.setter  # set RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP.None
    def encoded_order(
        self,
        encoded_order: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP
        | None,
    ):
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP
        """
        self._c_data[3] = (encoded_order,)

    @property  # get RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP.None
    def dispense(
        self,
    ) -> RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP | None:
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP
        """
        return self._c_data[4][0]

    @dispense.setter  # set RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP.None
    def dispense(
        self,
        d_ispense: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP
        | None,
    ):
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_DISPENSE_GROUP
        """
        self._c_data[4] = (d_ispense,)

    @property  # get RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP.None
    def give(self) -> RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP | None:
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP
        """
        return self._c_data[5][0]

    @give.setter  # set RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP.None
    def give(
        self, give: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP | None
    ):
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP
        """
        self._c_data[5] = (give,)

    @property  # get RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP.None
    def administration(
        self,
    ) -> RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP | None:
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP
        """
        return self._c_data[6][0]

    @administration.setter  # set RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP.None
    def administration(
        self,
        admin_istration: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP
        | None,
    ):
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ADMINISTRATION_GROUP
        """
        self._c_data[6] = (admin_istration,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...]:
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[7]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...],
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[7] = observation
        else:
            self._c_data[7] = (observation,)
