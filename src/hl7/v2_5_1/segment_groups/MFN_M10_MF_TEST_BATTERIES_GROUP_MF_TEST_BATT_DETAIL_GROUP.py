from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OM5 import OM5
from ..segments.OM4 import OM4


"""
MF TEST BATT DETAIL - MFN_M10_MF_TEST_BATTERIES_GROUP_MF_TEST_BATT_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M10_MF_TEST_BATTERIES_GROUP_MF_TEST_BATT_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M10_MF_TEST_BATTERIES_GROUP_MF_TEST_BATT_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    OM4, OM5
)

mfn_m10_mf_test_batteries_group_mf_test_batt_detail_group = MFN_M10_MF_TEST_BATTERIES_GROUP_MF_TEST_BATT_DETAIL_GROUP(  # MF TEST BATT DETAIL - Segment group for MFN_M10_MF_TEST_BATTERIES_GROUP - MF TEST BATTERIES consisting of OM5, OM4|None
    observation_batteries=om5,  # OM5(...)  # Required.
    observations_that_require_specimens=None,  # OM4(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M10_MF_TEST_BATTERIES_GROUP_MF_TEST_BATT_DETAIL_GROUP TEMPLATE-----
"""


class MFN_M10_MF_TEST_BATTERIES_GROUP_MF_TEST_BATT_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M10_MF_TEST_BATTERIES_GROUP_MF_TEST_BATT_DETAIL_GROUP"""
    _hl7_name = """MF TEST BATT DETAIL"""
    _hl7_description = """Segment group for MFN_M10_MF_TEST_BATTERIES_GROUP - MF TEST BATTERIES consisting of OM5, OM4|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M10_MF_TEST_BATTERIES_GROUP_MF_TEST_BATT_DETAIL_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("6", "7")
    _c_components = (OM5, OM4)
    _c_name = ("OM5", "OM4")
    _c_is_group = (False, False)
    _c_attrs = ("observation_batteries", "observations_that_require_specimens",)
    # fmt: on

    def __init__(
        self,
        observation_batteries: OM5,  #  Required. OM5.6
        observations_that_require_specimens: OM4
        | tuple[OM4, ...]
        | None = None,  #  OM4.7
    ):
        """
        None - `MFN_M10_MF_TEST_BATTERIES_GROUP_MF_TEST_BATT_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M10_MF_TEST_BATTERIES_GROUP_MF_TEST_BATT_DETAIL_GROUP>`_
        Segment group for MFN_M10_MF_TEST_BATTERIES_GROUP - MF TEST BATTERIES consisting of OM5, OM4|None

        :param observation_batteries: Observation Batteries (Sets) (id: OM5 | seq: 6 | use: R | rpt: 1)
        :param observations_that_require_specimens: Observations that Require Specimens (id: OM4 | seq: 7 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.observation_batteries = observation_batteries
        self.observations_that_require_specimens = observations_that_require_specimens

    @property  # get OM5.6
    def observation_batteries(self) -> OM5:
        """
        id: OM5 | use: R | rpt: 1 | seq: 6
        ---
        return_type: OM5.6: Observation Batteries (Sets)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM5
        """
        return self._c_data[0][0]

    @observation_batteries.setter  # set OM5.6
    def observation_batteries(self, om5: OM5):
        """
        id: OM5 | use: R | rpt: 1 | seq: 6
        ---
        param_type: OM5.6: Observation Batteries (Sets)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM5
        """
        self._c_data[0] = (om5,)

    @property  # get OM4
    def observations_that_require_specimens(self) -> tuple[OM4, ...] | tuple[None]:
        """
        id: OM4 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[OM4, ...]: (Observations that Require Specimens, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM4
        """
        return self._c_data[1]

    @observations_that_require_specimens.setter  # set OM4
    def observations_that_require_specimens(self, om4: OM4 | tuple[OM4, ...] | None):
        """
        id: OM4 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: OM4.7 | tuple[OM4, ...]: (Observations that Require Specimens, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM4
        """
        if isinstance(om4, tuple):
            self._c_data[1] = om4
        else:
            self._c_data[1] = (om4,)
