from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OM1 import OM1
from ..segments.OM7 import OM7
from ..segments.MFE import MFE


"""
MF OBS ATTRIBUTES - MFN_M12_MF_OBS_ATTRIBUTES_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M12_MF_OBS_ATTRIBUTES_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M12_MF_OBS_ATTRIBUTES_GROUP
from utils.hl7.v2_5_1.segments import (
    OM1, OM7, MFE
)

mfn_m12_mf_obs_attributes_group = MFN_M12_MF_OBS_ATTRIBUTES_GROUP(  # MF OBS ATTRIBUTES - Segment group for MFN_M12 - Master File Notification - Additional Basic Observation/Service Attributes consisting of MFE, OM1, OM7|None
    master_file_entry=mfe,  # MFE(...)  # Required.
    general_segment=om1,  # OM1(...)  # Required.
    additional_basic_attributes=None,  # OM7(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M12_MF_OBS_ATTRIBUTES_GROUP TEMPLATE-----
"""


class MFN_M12_MF_OBS_ATTRIBUTES_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M12_MF_OBS_ATTRIBUTES_GROUP"""
    _hl7_name = """MF OBS ATTRIBUTES"""
    _hl7_description = """Segment group for MFN_M12 - Master File Notification - Additional Basic Observation/Service Attributes consisting of MFE, OM1, OM7|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M12_MF_OBS_ATTRIBUTES_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 1)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("4", "5", "6")
    _c_components = (MFE, OM1, OM7)
    _c_name = ("MFE", "OM1", "OM7")
    _c_is_group = (False, False, False)
    _c_attrs = ("master_file_entry", "general_segment", "additional_basic_attributes",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.4
        general_segment: OM1,  #  Required. OM1.5
        additional_basic_attributes: OM7 | None = None,  #  OM7.6
    ):
        """
        None - `MFN_M12_MF_OBS_ATTRIBUTES_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M12_MF_OBS_ATTRIBUTES_GROUP>`_
        Segment group for MFN_M12 - Master File Notification - Additional Basic Observation/Service Attributes consisting of MFE, OM1, OM7|None

        :param master_file_entry: Master File Entry (id: MFE | seq: 4 | use: R | rpt: 1)
        :param general_segment: General Segment (id: OM1 | seq: 5 | use: R | rpt: 1)
        :param additional_basic_attributes: Additional Basic Attributes (id: OM7 | seq: 6 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.master_file_entry = master_file_entry
        self.general_segment = general_segment
        self.additional_basic_attributes = additional_basic_attributes

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

    @property  # get OM7.6
    def additional_basic_attributes(self) -> OM7 | None:
        """
        id: OM7 | use: O | rpt: 1 | seq: 6
        ---
        return_type: OM7.6: Additional Basic Attributes
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM7
        """
        return self._c_data[2][0]

    @additional_basic_attributes.setter  # set OM7.6
    def additional_basic_attributes(self, om7: OM7 | None):
        """
        id: OM7 | use: O | rpt: 1 | seq: 6
        ---
        param_type: OM7.6: Additional Basic Attributes
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM7
        """
        self._c_data[2] = (om7,)
