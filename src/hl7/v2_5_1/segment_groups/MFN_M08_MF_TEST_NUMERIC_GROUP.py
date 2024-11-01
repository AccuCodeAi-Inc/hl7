from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.MFE import MFE
from ..segments.OM4 import OM4
from ..segments.OM3 import OM3
from ..segments.OM2 import OM2
from ..segments.OM1 import OM1


"""
MF TEST NUMERIC - MFN_M08_MF_TEST_NUMERIC_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M08_MF_TEST_NUMERIC_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M08_MF_TEST_NUMERIC_GROUP
from utils.hl7.v2_5_1.segments import (
    OM2, OM4, OM3, MFE, OM1
)

mfn_m08_mf_test_numeric_group = MFN_M08_MF_TEST_NUMERIC_GROUP(  # MF TEST NUMERIC - Segment group for MFN_M08 - Master File Notification - Test/Observation (Numeric) consisting of MFE, OM1, OM2|None, OM3|None, OM4|None
    master_file_entry=mfe,  # MFE(...)  # Required.
    general_segment=om1,  # OM1(...)  # Required.
    numeric_observation=None,  # OM2(...) 
    categorical_service_or_test_or_observation=None,  # OM3(...) 
    observations_that_require_specimens=None,  # OM4(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M08_MF_TEST_NUMERIC_GROUP TEMPLATE-----
"""


class MFN_M08_MF_TEST_NUMERIC_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M08_MF_TEST_NUMERIC_GROUP"""
    _hl7_name = """MF TEST NUMERIC"""
    _hl7_description = """Segment group for MFN_M08 - Master File Notification - Test/Observation (Numeric) consisting of MFE, OM1, OM2|None, OM3|None, OM4|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M08_MF_TEST_NUMERIC_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 1, 1)
    _c_usage = ("R", "R", "O", "O", "O")
    _c_aliases = ("4", "5", "6", "7", "8")
    _c_components = (MFE, OM1, OM2, OM3, OM4)
    _c_name = ("MFE", "OM1", "OM2", "OM3", "OM4")
    _c_is_group = (False, False, False, False, False)
    _c_attrs = ("master_file_entry", "general_segment", "numeric_observation", "categorical_service_or_test_or_observation", "observations_that_require_specimens",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.4
        general_segment: OM1,  #  Required. OM1.5
        numeric_observation: OM2 | None = None,  #  OM2.6
        categorical_service_or_test_or_observation: OM3 | None = None,  #  OM3.7
        observations_that_require_specimens: OM4 | None = None,  #  OM4.8
    ):
        """
        None - `MFN_M08_MF_TEST_NUMERIC_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M08_MF_TEST_NUMERIC_GROUP>`_
        Segment group for MFN_M08 - Master File Notification - Test/Observation (Numeric) consisting of MFE, OM1, OM2|None, OM3|None, OM4|None

        :param master_file_entry: Master File Entry (id: MFE | seq: 4 | use: R | rpt: 1)
        :param general_segment: General Segment (id: OM1 | seq: 5 | use: R | rpt: 1)
        :param numeric_observation: Numeric Observation (id: OM2 | seq: 6 | use: O | rpt: 1)
        :param categorical_service_or_test_or_observation: Categorical Service/Test/Observation (id: OM3 | seq: 7 | use: O | rpt: 1)
        :param observations_that_require_specimens: Observations that Require Specimens (id: OM4 | seq: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.master_file_entry = master_file_entry
        self.general_segment = general_segment
        self.numeric_observation = numeric_observation
        self.categorical_service_or_test_or_observation = (
            categorical_service_or_test_or_observation
        )
        self.observations_that_require_specimens = observations_that_require_specimens

    @property  # get MFE.4
    def master_file_entry(self) -> MFE:
        """
        id: MFE | use: R | rpt: 1 | seq: 4
        ---
        return_type: MFE.4: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        return self._c_data[0][0]

    @master_file_entry.setter  # set MFE.4
    def master_file_entry(self, mfe: MFE):
        """
        id: MFE | use: R | rpt: 1 | seq: 4
        ---
        param_type: MFE.4: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        self._c_data[0] = (mfe,)

    @property  # get OM1.5
    def general_segment(self) -> OM1:
        """
        id: OM1 | use: R | rpt: 1 | seq: 5
        ---
        return_type: OM1.5: General Segment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM1
        """
        return self._c_data[1][0]

    @general_segment.setter  # set OM1.5
    def general_segment(self, om1: OM1):
        """
        id: OM1 | use: R | rpt: 1 | seq: 5
        ---
        param_type: OM1.5: General Segment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM1
        """
        self._c_data[1] = (om1,)

    @property  # get OM2.6
    def numeric_observation(self) -> OM2 | None:
        """
        id: OM2 | use: O | rpt: 1 | seq: 6
        ---
        return_type: OM2.6: Numeric Observation
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM2
        """
        return self._c_data[2][0]

    @numeric_observation.setter  # set OM2.6
    def numeric_observation(self, om2: OM2 | None):
        """
        id: OM2 | use: O | rpt: 1 | seq: 6
        ---
        param_type: OM2.6: Numeric Observation
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM2
        """
        self._c_data[2] = (om2,)

    @property  # get OM3.7
    def categorical_service_or_test_or_observation(self) -> OM3 | None:
        """
        id: OM3 | use: O | rpt: 1 | seq: 7
        ---
        return_type: OM3.7: Categorical Service/Test/Observation
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM3
        """
        return self._c_data[3][0]

    @categorical_service_or_test_or_observation.setter  # set OM3.7
    def categorical_service_or_test_or_observation(self, om3: OM3 | None):
        """
        id: OM3 | use: O | rpt: 1 | seq: 7
        ---
        param_type: OM3.7: Categorical Service/Test/Observation
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM3
        """
        self._c_data[3] = (om3,)

    @property  # get OM4.8
    def observations_that_require_specimens(self) -> OM4 | None:
        """
        id: OM4 | use: O | rpt: 1 | seq: 8
        ---
        return_type: OM4.8: Observations that Require Specimens
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM4
        """
        return self._c_data[4][0]

    @observations_that_require_specimens.setter  # set OM4.8
    def observations_that_require_specimens(self, om4: OM4 | None):
        """
        id: OM4 | use: O | rpt: 1 | seq: 8
        ---
        param_type: OM4.8: Observations that Require Specimens
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM4
        """
        self._c_data[4] = (om4,)
