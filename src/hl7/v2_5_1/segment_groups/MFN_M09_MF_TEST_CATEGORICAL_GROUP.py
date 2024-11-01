from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OM1 import OM1
from ..segments.MFE import MFE
from ..segment_groups.MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP import (
    MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP,
)


"""
MF TEST CATEGORICAL - MFN_M09_MF_TEST_CATEGORICAL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M09_MF_TEST_CATEGORICAL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M09_MF_TEST_CATEGORICAL_GROUP
from utils.hl7.v2_5_1.segments import (
    MFE, OM1
)
from utils.hl7.v2_5_1.segment_groups import (
    MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP
)

mfn_m09_mf_test_categorical_group = MFN_M09_MF_TEST_CATEGORICAL_GROUP(  # MF TEST CATEGORICAL - Segment group for MFN_M09 - Master File Notification - Test/Observation (Categorical) consisting of MFE, OM1, MF TEST CAT DETAIL|None
    master_file_entry=mfe,  # MFE(...)  # Required.
    general_segment=om1,  # OM1(...)  # Required.
    mf_test_cat_detail=None,  # MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M09_MF_TEST_CATEGORICAL_GROUP TEMPLATE-----
"""


class MFN_M09_MF_TEST_CATEGORICAL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M09_MF_TEST_CATEGORICAL_GROUP"""
    _hl7_name = """MF TEST CATEGORICAL"""
    _hl7_description = """Segment group for MFN_M09 - Master File Notification - Test/Observation (Categorical) consisting of MFE, OM1, MF TEST CAT DETAIL|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M09_MF_TEST_CATEGORICAL_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 1)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("4", "5", "None")
    _c_components = (MFE, OM1, MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP)
    _c_name = ("MFE", "OM1", "MF TEST CAT DETAIL")
    _c_is_group = (False, False, True)
    _c_attrs = ("master_file_entry", "general_segment", "mf_test_cat_detail",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.4
        general_segment: OM1,  #  Required. OM1.5
        mf_test_cat_detail: MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP
        | None = None,  #  OM3.6, OM4.7
    ):
        """
        None - `MFN_M09_MF_TEST_CATEGORICAL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M09_MF_TEST_CATEGORICAL_GROUP>`_
        Segment group for MFN_M09 - Master File Notification - Test/Observation (Categorical) consisting of MFE, OM1, MF TEST CAT DETAIL|None

        :param master_file_entry: Master File Entry (id: MFE | seq: 4 | use: R | rpt: 1)
        :param general_segment: General Segment (id: OM1 | seq: 5 | use: R | rpt: 1)
        :param mf_test_cat_detail: Mf Test Cat Detail segment group: [OM3, OM4|None] (id: MF TEST CAT DETAIL | seq: 6, 7 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.master_file_entry = master_file_entry
        self.general_segment = general_segment
        self.mf_test_cat_detail = mf_test_cat_detail

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

    @property  # get MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP.None
    def mf_test_cat_detail(
        self,
    ) -> MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP | None:
        """
        id: MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP
        """
        return self._c_data[2][0]

    @mf_test_cat_detail.setter  # set MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP.None
    def mf_test_cat_detail(
        self,
        mf_test_cat_detail: MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP
        | None,
    ):
        """
        id: MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M09_MF_TEST_CATEGORICAL_GROUP_MF_TEST_CAT_DETAIL_GROUP
        """
        self._c_data[2] = (mf_test_cat_detail,)
