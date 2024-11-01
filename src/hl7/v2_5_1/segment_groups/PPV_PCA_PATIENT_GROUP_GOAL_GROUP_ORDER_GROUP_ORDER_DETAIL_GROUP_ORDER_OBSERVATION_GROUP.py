from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBX import OBX
from ..segments.NTE import NTE
from ..segments.VAR import VAR


"""
ORDER OBSERVATION - PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, VAR, OBX
)

ppv_pca_patient_group_goal_group_order_group_order_detail_group_order_observation_group = PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP(  # ORDER OBSERVATION - Segment group for PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of OBX, NTE|None, VAR|None
    observation_or_result=obx,  # OBX(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP TEMPLATE-----
"""


class PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP"""
    _hl7_name = """ORDER OBSERVATION"""
    _hl7_description = """Segment group for PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of OBX, NTE|None, VAR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("35", "36", "37")
    _c_components = (OBX, NTE, VAR)
    _c_name = ("OBX", "NTE", "VAR")
    _c_is_group = (False, False, False)
    _c_attrs = ("observation_or_result", "notes_and_comments", "variance",)
    # fmt: on

    def __init__(
        self,
        observation_or_result: OBX,  #  Required. OBX.35
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.36
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.37
    ):
        """
        None - `PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP>`_
        Segment group for PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of OBX, NTE|None, VAR|None

        :param observation_or_result: Observation/Result (id: OBX | seq: 35 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 36 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 37 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.observation_or_result = observation_or_result
        self.notes_and_comments = notes_and_comments
        self.variance = variance

    @property  # get OBX.35
    def observation_or_result(self) -> OBX:
        """
        id: OBX | use: R | rpt: 1 | seq: 35
        ---
        return_type: OBX.35: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[0][0]

    @observation_or_result.setter  # set OBX.35
    def observation_or_result(self, obx: OBX):
        """
        id: OBX | use: R | rpt: 1 | seq: 35
        ---
        param_type: OBX.35: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        self._c_data[0] = (obx,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 36
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 36
        ---
        param_type: NTE.36 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get VAR
    def variance(self) -> tuple[VAR, ...] | tuple[None]:
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 37
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[2]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 37
        ---
        param_type: VAR.37 | tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        if isinstance(var, tuple):
            self._c_data[2] = var
        else:
            self._c_data[2] = (var,)
