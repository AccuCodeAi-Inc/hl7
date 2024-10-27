from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.TCC import TCC
from ..segments.SPM import SPM


"""
TEST CONFIGURATION - TCU_U10_TEST_CONFIGURATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::TCU_U10_TEST_CONFIGURATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import TCU_U10_TEST_CONFIGURATION_GROUP
from utils.hl7.v2_5_1.segments import (
    TCC, SPM
)

tcu_u10_test_configuration_group = TCU_U10_TEST_CONFIGURATION_GROUP(  # TEST CONFIGURATION - Segment group for TCU_U10 - Automated equipment test code settings update consisting of SPM|None, TCC
    specimen=None,  # SPM(...) 
    test_code_configuration=tcc,  # TCC(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::TCU_U10_TEST_CONFIGURATION_GROUP TEMPLATE-----
"""


class TCU_U10_TEST_CONFIGURATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """TCU_U10_TEST_CONFIGURATION_GROUP"""
    _hl7_name = """TEST CONFIGURATION"""
    _hl7_description = """Segment group for TCU_U10 - Automated equipment test code settings update consisting of SPM|None, TCC"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/TCU_U10_TEST_CONFIGURATION_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("4", "5")
    _c_components = (SPM, TCC)
    _c_name = ("SPM", "TCC")
    _c_is_group = (False, False)
    _c_attrs = ("specimen", "test_code_configuration",)
    # fmt: on

    def __init__(
        self,
        test_code_configuration: TCC | tuple[TCC, ...],  #  Required. TCC.5
        specimen: SPM | None = None,  #  SPM.4
    ):
        """
        None - `TCU_U10_TEST_CONFIGURATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/TCU_U10_TEST_CONFIGURATION_GROUP>`_
        Segment group for TCU_U10 - Automated equipment test code settings update consisting of SPM|None, TCC

        :param specimen: Specimen (id: SPM | seq: 4 | use: O | rpt: 1)
        :param test_code_configuration: Test Code Configuration (id: TCC | seq: 5 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.specimen = specimen
        self.test_code_configuration = test_code_configuration

    @property  # get SPM.4
    def specimen(self) -> SPM | None:
        """
        id: SPM | use: O | rpt: 1 | seq: 4
        ---
        return_type: SPM.4: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.4
    def specimen(self, spm: SPM | None):
        """
        id: SPM | use: O | rpt: 1 | seq: 4
        ---
        param_type: SPM.4: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get TCC
    def test_code_configuration(self) -> tuple[TCC, ...]:
        """
        id: TCC SEGMENT GROUP | use: R | rpt: * | seq: 5
        ---
        return_type: tuple[TCC, ...]: (Test Code Configuration, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCC
        """
        return self._c_data[1]

    @test_code_configuration.setter  # set TCC
    def test_code_configuration(self, tcc: TCC | tuple[TCC, ...]):
        """
        id: TCC SEGMENT GROUP | use: R | rpt: * | seq: 5
        ---
        param_type: TCC.5 | tuple[TCC, ...]: (Test Code Configuration, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCC
        """
        if isinstance(tcc, tuple):
            self._c_data[1] = tcc
        else:
            self._c_data[1] = (tcc,)
