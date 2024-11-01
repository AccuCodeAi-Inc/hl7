from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CTD import CTD
from ..segment_groups.OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP import (
    OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP,
)
from ..segments.ORC import ORC
from ..segment_groups.OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP import (
    OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP,
)
from ..segments.NTE import NTE
from ..segments.OBR import OBR


"""
ORDER PRIOR - OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
from utils.hl7.v2_5_1.segments import (
    CTD, OBR, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP, OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP
)

omg_o19_order_group_prior_result_group_order_prior_group = OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP(  # ORDER PRIOR - Segment group for OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP - PRIOR RESULT consisting of ORC|None, OBR, TIMING PRIOR|None, NTE|None, CTD|None, OBSERVATION PRIOR
    common_order=None,  # ORC(...) 
    observation_request=obr,  # OBR(...)  # Required.
    timing_prior=None,  # OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP(...) 
    notes_and_comments=None,  # NTE(...) 
    contact_data=None,  # CTD(...) 
    observation_prior=omg_o19_order_group_prior_result_group_order_prior_group_observation_prior_group,  # OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP TEMPLATE-----
"""


class OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP"""
    _hl7_name = """ORDER PRIOR"""
    _hl7_description = """Segment group for OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP - PRIOR RESULT consisting of ORC|None, OBR, TIMING PRIOR|None, NTE|None, CTD|None, OBSERVATION PRIOR"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 1, 65535)
    _c_usage = ("O", "R", "O", "O", "O", "R")
    _c_aliases = ("33", "34", "None", "37", "38", "None")
    _c_components = (ORC, OBR, OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP, NTE, CTD, OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP)
    _c_name = ("ORC", "OBR", "TIMING PRIOR", "NTE", "CTD", "OBSERVATION PRIOR")
    _c_is_group = (False, False, True, False, False, True)
    _c_attrs = ("common_order", "observation_request", "timing_prior", "notes_and_comments", "contact_data", "observation_prior",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.34
        observation_prior: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP
        | tuple[
            OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP,
            ...,
        ],  #  Required. (OBX.39, NTE.40, ...)
        common_order: ORC | None = None,  #  ORC.33
        timing_prior: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP
        | tuple[
            OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP,
            ...,
        ]
        | None = None,  #  (TQ1.35, TQ2.36, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.37
        contact_data: CTD | None = None,  #  CTD.38
    ):
        """
        None - `OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP>`_
        Segment group for OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP - PRIOR RESULT consisting of ORC|None, OBR, TIMING PRIOR|None, NTE|None, CTD|None, OBSERVATION PRIOR

        :param common_order: Common Order (id: ORC | seq: 33 | use: O | rpt: 1)
        :param observation_request: Observation Request (id: OBR | seq: 34 | use: R | rpt: 1)
        :param timing_prior: Timing Prior segment group: [TQ1, TQ2|None] (id: TIMING PRIOR | seq: 35, 36 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 37 | use: O | rpt: *)
        :param contact_data: Contact Data (id: CTD | seq: 38 | use: O | rpt: 1)
        :param observation_prior: Observation Prior segment group: [OBX, NTE|None] (id: OBSERVATION PRIOR | seq: 39, 40 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.common_order = common_order
        self.observation_request = observation_request
        self.timing_prior = timing_prior
        self.notes_and_comments = notes_and_comments
        self.contact_data = contact_data
        self.observation_prior = observation_prior

    @property  # get ORC.33
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 33
        ---
        return_type: ORC.33: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.33
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 33
        ---
        param_type: ORC.33: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get OBR.34
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 34
        ---
        return_type: OBR.34: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[1][0]

    @observation_request.setter  # set OBR.34
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 34
        ---
        param_type: OBR.34: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[1] = (obr,)

    @property  # get TIMING PRIOR
    def timing_prior(
        self,
    ) -> (
        tuple[
            OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP
        """
        return self._c_data[2]

    @timing_prior.setter  # set TIMING PRIOR
    def timing_prior(
        self,
        timing_prior: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP
        | tuple[
            OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: TIMING PRIOR SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP.None | tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP
        """
        if isinstance(timing_prior, tuple):
            self._c_data[2] = timing_prior
        else:
            self._c_data[2] = (timing_prior,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 37
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 37
        ---
        param_type: NTE.37 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get CTD.38
    def contact_data(self) -> CTD | None:
        """
        id: CTD | use: O | rpt: 1 | seq: 38
        ---
        return_type: CTD.38: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[4][0]

    @contact_data.setter  # set CTD.38
    def contact_data(self, ctd: CTD | None):
        """
        id: CTD | use: O | rpt: 1 | seq: 38
        ---
        param_type: CTD.38: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        self._c_data[4] = (ctd,)

    @property  # get OBSERVATION PRIOR
    def observation_prior(
        self,
    ) -> tuple[
        OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP,
        ...,
    ]:
        """
        id: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP
        """
        return self._c_data[5]

    @observation_prior.setter  # set OBSERVATION PRIOR
    def observation_prior(
        self,
        observation_prior: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP
        | tuple[
            OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP,
            ...,
        ],
    ):
        """
        id: OBSERVATION PRIOR SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP.None | tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP
        """
        if isinstance(observation_prior, tuple):
            self._c_data[5] = observation_prior
        else:
            self._c_data[5] = (observation_prior,)
