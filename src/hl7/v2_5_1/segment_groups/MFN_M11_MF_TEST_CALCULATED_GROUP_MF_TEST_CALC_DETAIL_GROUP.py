from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OM2 import OM2
from ..segments.OM6 import OM6


"""
MF TEST CALC DETAIL - MFN_M11_MF_TEST_CALCULATED_GROUP_MF_TEST_CALC_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M11_MF_TEST_CALCULATED_GROUP_MF_TEST_CALC_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M11_MF_TEST_CALCULATED_GROUP_MF_TEST_CALC_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    OM2, OM6
)

mfn_m11_mf_test_calculated_group_mf_test_calc_detail_group = MFN_M11_MF_TEST_CALCULATED_GROUP_MF_TEST_CALC_DETAIL_GROUP(  # MF TEST CALC DETAIL - Segment group for MFN_M11_MF_TEST_CALCULATED_GROUP - MF TEST CALCULATED consisting of OM6, OM2
    observations_that_are_calculated_from_other_observations=om6,  # OM6(...)  # Required.
    numeric_observation=om2,  # OM2(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M11_MF_TEST_CALCULATED_GROUP_MF_TEST_CALC_DETAIL_GROUP TEMPLATE-----
"""


class MFN_M11_MF_TEST_CALCULATED_GROUP_MF_TEST_CALC_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M11_MF_TEST_CALCULATED_GROUP_MF_TEST_CALC_DETAIL_GROUP"""
    _hl7_name = """MF TEST CALC DETAIL"""
    _hl7_description = """Segment group for MFN_M11_MF_TEST_CALCULATED_GROUP - MF TEST CALCULATED consisting of OM6, OM2"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M11_MF_TEST_CALCULATED_GROUP_MF_TEST_CALC_DETAIL_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "R")
    _c_aliases = ("6", "7")
    _c_components = (OM6, OM2)
    _c_name = ("OM6", "OM2")
    _c_is_group = (False, False)
    _c_attrs = ("observations_that_are_calculated_from_other_observations", "numeric_observation",)
    # fmt: on

    def __init__(
        self,
        observations_that_are_calculated_from_other_observations: OM6,  #  Required. OM6.6
        numeric_observation: OM2,  #  Required. OM2.7
    ):
        """
        None - `MFN_M11_MF_TEST_CALCULATED_GROUP_MF_TEST_CALC_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M11_MF_TEST_CALCULATED_GROUP_MF_TEST_CALC_DETAIL_GROUP>`_
        Segment group for MFN_M11_MF_TEST_CALCULATED_GROUP - MF TEST CALCULATED consisting of OM6, OM2

        :param observations_that_are_calculated_from_other_observations: Observations that are Calculated from Other Observations (id: OM6 | seq: 6 | use: R | rpt: 1)
        :param numeric_observation: Numeric Observation (id: OM2 | seq: 7 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.observations_that_are_calculated_from_other_observations = (
            observations_that_are_calculated_from_other_observations
        )
        self.numeric_observation = numeric_observation

    @property  # get OM6.6
    def observations_that_are_calculated_from_other_observations(self) -> OM6:
        """
        id: OM6 | use: R | rpt: 1 | seq: 6
        ---
        return_type: OM6.6: Observations that are Calculated from Other Observations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM6
        """
        return self._c_data[0][0]

    @observations_that_are_calculated_from_other_observations.setter  # set OM6.6
    def observations_that_are_calculated_from_other_observations(self, om6: OM6):
        """
        id: OM6 | use: R | rpt: 1 | seq: 6
        ---
        param_type: OM6.6: Observations that are Calculated from Other Observations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM6
        """
        self._c_data[0] = (om6,)

    @property  # get OM2.7
    def numeric_observation(self) -> OM2:
        """
        id: OM2 | use: R | rpt: 1 | seq: 7
        ---
        return_type: OM2.7: Numeric Observation
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM2
        """
        return self._c_data[1][0]

    @numeric_observation.setter  # set OM2.7
    def numeric_observation(self, om2: OM2):
        """
        id: OM2 | use: R | rpt: 1 | seq: 7
        ---
        param_type: OM2.7: Numeric Observation
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM2
        """
        self._c_data[1] = (om2,)
