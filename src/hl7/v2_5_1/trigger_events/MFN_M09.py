from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segment_groups.MFN_M09_MF_TEST_CATEGORICAL_GROUP import (
    MFN_M09_MF_TEST_CATEGORICAL_GROUP,
)
from ..segments.MFI import MFI
from ..segments.SFT import SFT


"""
Master File Notification - Test/Observation (Categorical) - MFN_M09
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::MFN_M09 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M09
from utils.hl7.v2_5_1.segments import (
    SFT, MFI, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    MFN_M09_MF_TEST_CATEGORICAL_GROUP
)

mfn_m09 = MFN_M09(  #  - 
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    master_file_identification=mfi,  # MFI(...)  # Required.
    mf_test_categorical=mfn_m09_mf_test_categorical_group,  # MFN_M09_MF_TEST_CATEGORICAL_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::MFN_M09 TEMPLATE-----
"""


class MFN_M09(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """MFN_M09"""
    _hl7_name = """Master File Notification - Test/Observation (Categorical)"""
    _hl7_description = """"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M09"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "None")
    _c_components = (MSH, SFT, MFI, MFN_M09_MF_TEST_CATEGORICAL_GROUP)
    _c_name = ("MSH", "SFT", "MFI", "MF TEST CATEGORICAL")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "master_file_identification", "mf_test_categorical",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        master_file_identification: MFI,  #  Required. MFI.3
        mf_test_categorical: MFN_M09_MF_TEST_CATEGORICAL_GROUP
        | tuple[
            MFN_M09_MF_TEST_CATEGORICAL_GROUP, ...
        ],  #  Required. (MFE.4, OM1.5, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `MFN_M09 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M09>`_


        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param master_file_identification: Master File Identification (id: MFI | seq: 3 | use: R | rpt: 1)
        :param mf_test_categorical: Mf Test Categorical segment group: [MFE, OM1, MF TEST CAT DETAIL|None] (id: MF TEST CATEGORICAL | seq: 4, 5, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.master_file_identification = master_file_identification
        self.mf_test_categorical = mf_test_categorical

    @property  # get MSH.1
    def message_header(self) -> MSH:
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        return_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        return self._c_data[0][0]

    @message_header.setter  # set MSH.1
    def message_header(self, msh: MSH):
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        param_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        self._c_data[0] = (msh,)

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[1]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        param_type: SFT.2 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[1] = sft
        else:
            self._c_data[1] = (sft,)

    @property  # get MFI.3
    def master_file_identification(self) -> MFI:
        """
        id: MFI | use: R | rpt: 1 | seq: 3
        ---
        return_type: MFI.3: Master File Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI
        """
        return self._c_data[2][0]

    @master_file_identification.setter  # set MFI.3
    def master_file_identification(self, mfi: MFI):
        """
        id: MFI | use: R | rpt: 1 | seq: 3
        ---
        param_type: MFI.3: Master File Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI
        """
        self._c_data[2] = (mfi,)

    @property  # get MF TEST CATEGORICAL
    def mf_test_categorical(self) -> tuple[MFN_M09_MF_TEST_CATEGORICAL_GROUP, ...]:
        """
        id: MFN_M09_MF_TEST_CATEGORICAL_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[MFN_M09_MF_TEST_CATEGORICAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M09_MF_TEST_CATEGORICAL_GROUP
        """
        return self._c_data[3]

    @mf_test_categorical.setter  # set MF TEST CATEGORICAL
    def mf_test_categorical(
        self,
        mf_test_categorical: MFN_M09_MF_TEST_CATEGORICAL_GROUP
        | tuple[MFN_M09_MF_TEST_CATEGORICAL_GROUP, ...],
    ):
        """
        id: MF TEST CATEGORICAL SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: MFN_M09_MF_TEST_CATEGORICAL_GROUP.None | tuple[MFN_M09_MF_TEST_CATEGORICAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M09_MF_TEST_CATEGORICAL_GROUP
        """
        if isinstance(mf_test_categorical, tuple):
            self._c_data[3] = mf_test_categorical
        else:
            self._c_data[3] = (mf_test_categorical,)
