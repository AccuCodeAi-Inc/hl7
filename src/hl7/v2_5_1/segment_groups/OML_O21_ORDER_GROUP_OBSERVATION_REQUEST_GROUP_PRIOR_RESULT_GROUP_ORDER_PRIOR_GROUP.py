from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segment_groups.OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP import (
    OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP,
)
from ..segments.ORC import ORC
from ..segment_groups.OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP import (
    OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP,
)


"""
ORDER PRIOR - OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, ORC, OBR
)
from utils.hl7.v2_5_1.segment_groups import (
    OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP, OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP
)

oml_o21_order_group_observation_request_group_prior_result_group_order_prior_group = OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP(  # ORDER PRIOR - Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP - PRIOR RESULT consisting of ORC|None, OBR, NTE|None, TIMING PRIOR|None, OBSERVATION PRIOR
    common_order=None,  # ORC(...) 
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    timing_prior=None,  # OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP(...) 
    observation_prior=oml_o21_order_group_observation_request_group_prior_result_group_order_prior_group_observation_prior_group,  # OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP TEMPLATE-----
"""


class OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP"""
    _hl7_name = """ORDER PRIOR"""
    _hl7_description = """Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP - PRIOR RESULT consisting of ORC|None, OBR, NTE|None, TIMING PRIOR|None, OBSERVATION PRIOR"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535)
    _c_usage = ("O", "R", "O", "O", "R")
    _c_aliases = ("35", "36", "37", "None", "None")
    _c_components = (ORC, OBR, NTE, OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP, OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP)
    _c_name = ("ORC", "OBR", "NTE", "TIMING PRIOR", "OBSERVATION PRIOR")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("common_order", "observation_request", "notes_and_comments", "timing_prior", "observation_prior",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.36
        observation_prior: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP
        | tuple[
            OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP,
            ...,
        ],  #  Required. (OBX.40, NTE.41, ...)
        common_order: ORC | None = None,  #  ORC.35
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.37
        timing_prior: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP
        | tuple[
            OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP,
            ...,
        ]
        | None = None,  #  (TQ1.38, TQ2.39, ...)
    ):
        """
        None - `OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP>`_
        Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP - PRIOR RESULT consisting of ORC|None, OBR, NTE|None, TIMING PRIOR|None, OBSERVATION PRIOR

        :param common_order: Common Order (id: ORC | seq: 35 | use: O | rpt: 1)
        :param observation_request: Observation Request (id: OBR | seq: 36 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 37 | use: O | rpt: *)
        :param timing_prior: Timing Prior segment group: [TQ1, TQ2|None] (id: TIMING PRIOR | seq: 38, 39 | use: O | rpt: *)
        :param observation_prior: Observation Prior segment group: [OBX, NTE|None] (id: OBSERVATION PRIOR | seq: 40, 41 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.common_order = common_order
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.timing_prior = timing_prior
        self.observation_prior = observation_prior

    @property  # get ORC.35
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 35
        ---
        return_type: ORC.35: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.35
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 35
        ---
        param_type: ORC.35: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get OBR.36
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 36
        ---
        return_type: OBR.36: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[1][0]

    @observation_request.setter  # set OBR.36
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 36
        ---
        param_type: OBR.36: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[1] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 37
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

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
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get TIMING PRIOR
    def timing_prior(
        self,
    ) -> (
        tuple[
            OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP
        """
        return self._c_data[3]

    @timing_prior.setter  # set TIMING PRIOR
    def timing_prior(
        self,
        timing_prior: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP
        | tuple[
            OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: TIMING PRIOR SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP.None | tuple[OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_TIMING_PRIOR_GROUP
        """
        if isinstance(timing_prior, tuple):
            self._c_data[3] = timing_prior
        else:
            self._c_data[3] = (timing_prior,)

    @property  # get OBSERVATION PRIOR
    def observation_prior(
        self,
    ) -> tuple[
        OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP,
        ...,
    ]:
        """
        id: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP
        """
        return self._c_data[4]

    @observation_prior.setter  # set OBSERVATION PRIOR
    def observation_prior(
        self,
        observation_prior: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP
        | tuple[
            OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP,
            ...,
        ],
    ):
        """
        id: OBSERVATION PRIOR SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP.None | tuple[OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP_OBSERVATION_PRIOR_GROUP
        """
        if isinstance(observation_prior, tuple):
            self._c_data[4] = observation_prior
        else:
            self._c_data[4] = (observation_prior,)
