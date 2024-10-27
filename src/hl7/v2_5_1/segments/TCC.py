from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.SN import SN
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..data_types.EI import EI
from ..data_types.SPS import SPS
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.ProcessingType import ProcessingType


"""
Test Code Configuration - TCC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::TCC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    TCC,
    ID, SN, CE, NM, EI, SPS
)

tcc = TCC(  #  - The test (e
    universal_service_identifier=ce,  # CE(...)  # Required.
    test_application_identifier=ei,  # EI(...)  # Required.
    specimen_source=None,  # SPS(...) 
    auto_dilution_factor_default=None,  # SN(...) 
    rerun_dilution_factor_default=None,  # SN(...) 
    pre_dilution_factor_default=None,  # SN(...) 
    endogenous_content_of_pre_dilution_diluent=None,  # SN(...) 
    inventory_limits_warning_level=None,  # NM(...) 
    automatic_rerun_allowed=None,  # ID(...) 
    automatic_repeat_allowed=None,  # ID(...) 
    automatic_reflex_allowed=None,  # ID(...) 
    equipment_dynamic_range=None,  # SN(...) 
    units=None,  # CE(...) 
    processing_type=None,  # CE(...) 
)

-----END SEGMENT::TCC TEMPLATE-----
"""


class TCC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """TCC"""
    _hl7_name = """Test Code Configuration"""
    _hl7_description = """The test (e"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCC"
    _c_length = (250, 80, 300, 20, 20, 20, 20, 10, 1, 1, 1, 20, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, EI, SPS, SN, SN, SN, SN, NM, ID, ID, ID, SN, CE, CE,)
    _c_aliases = ("TCC.1", "TCC.2", "TCC.3", "TCC.4", "TCC.5", "TCC.6", "TCC.7", "TCC.8", "TCC.9", "TCC.10", "TCC.11", "TCC.12", "TCC.13", "TCC.14",)
    _c_names = ("Universal Service Identifier", "Test Application Identifier", "Specimen Source", "Auto-Dilution Factor Default", "Rerun Dilution Factor Default", "Pre-Dilution Factor Default", "Endogenous Content of Pre-Dilution Diluent", "Inventory Limits Warning Level", "Automatic Rerun Allowed", "Automatic Repeat Allowed", "Automatic Reflex Allowed", "Equipment Dynamic Range", "Units", "Processing Type",)
    _c_attrs = ("universal_service_identifier", "test_application_identifier", "specimen_source", "auto_dilution_factor_default", "rerun_dilution_factor_default", "pre_dilution_factor_default", "endogenous_content_of_pre_dilution_diluent", "inventory_limits_warning_level", "automatic_rerun_allowed", "automatic_repeat_allowed", "automatic_reflex_allowed", "equipment_dynamic_range", "units", "processing_type",)
    # fmt: on

    def __init__(
        self,
        universal_service_identifier: CE,  # TCC.1
        test_application_identifier: EI,  # TCC.2
        specimen_source: SPS | None = None,  # TCC.3
        auto_dilution_factor_default: SN | None = None,  # TCC.4
        rerun_dilution_factor_default: SN | None = None,  # TCC.5
        pre_dilution_factor_default: SN | None = None,  # TCC.6
        endogenous_content_of_pre_dilution_diluent: SN | None = None,  # TCC.7
        inventory_limits_warning_level: NM | None = None,  # TCC.8
        automatic_rerun_allowed: YesOrNoIndicator | ID | None = None,  # TCC.9
        automatic_repeat_allowed: YesOrNoIndicator | ID | None = None,  # TCC.10
        automatic_reflex_allowed: YesOrNoIndicator | ID | None = None,  # TCC.11
        equipment_dynamic_range: SN | None = None,  # TCC.12
        units: CE | None = None,  # TCC.13
        processing_type: ProcessingType | CE | None = None,  # TCC.14
    ):
        """
        Test Code Configuration - `TCC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCC>`_
        The test (e.g., analyte) code configuration segment is the data necessary to maintain and transmit information concerning the test entity codes that are being used throughout the "automated system."

        :param universal_service_identifier: Coded Element (id: TCC.1 | len: 250 | use: R | rpt: 1)
        :param test_application_identifier: Entity Identifier (id: TCC.2 | len: 80 | use: R | rpt: 1)
        :param specimen_source: Specimen Source (id: TCC.3 | len: 300 | use: B | rpt: 1)
        :param auto_dilution_factor_default: Structured Numeric (id: TCC.4 | len: 20 | use: O | rpt: 1)
        :param rerun_dilution_factor_default: Structured Numeric (id: TCC.5 | len: 20 | use: O | rpt: 1)
        :param pre_dilution_factor_default: Structured Numeric (id: TCC.6 | len: 20 | use: O | rpt: 1)
        :param endogenous_content_of_pre_dilution_diluent: Structured Numeric (id: TCC.7 | len: 20 | use: O | rpt: 1)
        :param inventory_limits_warning_level: Numeric (id: TCC.8 | len: 10 | use: O | rpt: 1)
        :param automatic_rerun_allowed: Coded values for HL7 tables (id: TCC.9 | len: 1 | use: O | rpt: 1)
        :param automatic_repeat_allowed: Coded values for HL7 tables (id: TCC.10 | len: 1 | use: O | rpt: 1)
        :param automatic_reflex_allowed: Coded values for HL7 tables (id: TCC.11 | len: 1 | use: O | rpt: 1)
        :param equipment_dynamic_range: Structured Numeric (id: TCC.12 | len: 20 | use: O | rpt: 1)
        :param units: Coded Element (id: TCC.13 | len: 250 | use: O | rpt: 1)
        :param processing_type: Coded Element (id: TCC.14 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 14
        self.universal_service_identifier = universal_service_identifier
        self.test_application_identifier = test_application_identifier
        self.specimen_source = specimen_source
        self.auto_dilution_factor_default = auto_dilution_factor_default
        self.rerun_dilution_factor_default = rerun_dilution_factor_default
        self.pre_dilution_factor_default = pre_dilution_factor_default
        self.endogenous_content_of_pre_dilution_diluent = (
            endogenous_content_of_pre_dilution_diluent
        )
        self.inventory_limits_warning_level = inventory_limits_warning_level
        self.automatic_rerun_allowed = automatic_rerun_allowed
        self.automatic_repeat_allowed = automatic_repeat_allowed
        self.automatic_reflex_allowed = automatic_reflex_allowed
        self.equipment_dynamic_range = equipment_dynamic_range
        self.units = units
        self.processing_type = processing_type

    @property  # get TCC.1
    def universal_service_identifier(self) -> CE:
        """
        id: TCC.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.1
        """
        return self._c_data[0][0]

    @universal_service_identifier.setter  # set TCC.1
    def universal_service_identifier(self, ce: CE):
        """
        id: TCC.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.1
        """
        self._c_data[0] = (ce,)

    @property  # get TCC.2
    def test_application_identifier(self) -> EI:
        """
        id: TCC.2 | len: 80 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.2
        """
        return self._c_data[1][0]

    @test_application_identifier.setter  # set TCC.2
    def test_application_identifier(self, ei: EI):
        """
        id: TCC.2 | len: 80 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.2
        """
        self._c_data[1] = (ei,)

    @property  # get TCC.3
    def specimen_source(self) -> SPS | None:
        """
        id: TCC.3 | len: 300 | use: B | rpt: 1
        ---
        return_type: SPS: Specimen Source
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.3
        """
        return self._c_data[2][0]

    @specimen_source.setter  # set TCC.3
    def specimen_source(self, sps: SPS | None):
        """
        id: TCC.3 | len: 300 | use: B | rpt: 1
        ---
        param_type: SPS: Specimen Source
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.3
        """
        self._c_data[2] = (sps,)

    @property  # get TCC.4
    def auto_dilution_factor_default(self) -> SN | None:
        """
        id: TCC.4 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.4
        """
        return self._c_data[3][0]

    @auto_dilution_factor_default.setter  # set TCC.4
    def auto_dilution_factor_default(self, sn: SN | None):
        """
        id: TCC.4 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.4
        """
        self._c_data[3] = (sn,)

    @property  # get TCC.5
    def rerun_dilution_factor_default(self) -> SN | None:
        """
        id: TCC.5 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.5
        """
        return self._c_data[4][0]

    @rerun_dilution_factor_default.setter  # set TCC.5
    def rerun_dilution_factor_default(self, sn: SN | None):
        """
        id: TCC.5 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.5
        """
        self._c_data[4] = (sn,)

    @property  # get TCC.6
    def pre_dilution_factor_default(self) -> SN | None:
        """
        id: TCC.6 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.6
        """
        return self._c_data[5][0]

    @pre_dilution_factor_default.setter  # set TCC.6
    def pre_dilution_factor_default(self, sn: SN | None):
        """
        id: TCC.6 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.6
        """
        self._c_data[5] = (sn,)

    @property  # get TCC.7
    def endogenous_content_of_pre_dilution_diluent(self) -> SN | None:
        """
        id: TCC.7 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.7
        """
        return self._c_data[6][0]

    @endogenous_content_of_pre_dilution_diluent.setter  # set TCC.7
    def endogenous_content_of_pre_dilution_diluent(self, sn: SN | None):
        """
        id: TCC.7 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.7
        """
        self._c_data[6] = (sn,)

    @property  # get TCC.8
    def inventory_limits_warning_level(self) -> NM | None:
        """
        id: TCC.8 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.8
        """
        return self._c_data[7][0]

    @inventory_limits_warning_level.setter  # set TCC.8
    def inventory_limits_warning_level(self, nm: NM | None):
        """
        id: TCC.8 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.8
        """
        self._c_data[7] = (nm,)

    @property  # get TCC.9
    def automatic_rerun_allowed(self) -> YesOrNoIndicator | None:
        """
        id: TCC.9 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.9
        """
        return self._c_data[8][0]

    @automatic_rerun_allowed.setter  # set TCC.9
    def automatic_rerun_allowed(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: TCC.9 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.9
        """
        self._c_data[8] = (yes_or_no_indicator,)

    @property  # get TCC.10
    def automatic_repeat_allowed(self) -> YesOrNoIndicator | None:
        """
        id: TCC.10 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.10
        """
        return self._c_data[9][0]

    @automatic_repeat_allowed.setter  # set TCC.10
    def automatic_repeat_allowed(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: TCC.10 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.10
        """
        self._c_data[9] = (yes_or_no_indicator,)

    @property  # get TCC.11
    def automatic_reflex_allowed(self) -> YesOrNoIndicator | None:
        """
        id: TCC.11 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.11
        """
        return self._c_data[10][0]

    @automatic_reflex_allowed.setter  # set TCC.11
    def automatic_reflex_allowed(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: TCC.11 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.11
        """
        self._c_data[10] = (yes_or_no_indicator,)

    @property  # get TCC.12
    def equipment_dynamic_range(self) -> SN | None:
        """
        id: TCC.12 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.12
        """
        return self._c_data[11][0]

    @equipment_dynamic_range.setter  # set TCC.12
    def equipment_dynamic_range(self, sn: SN | None):
        """
        id: TCC.12 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.12
        """
        self._c_data[11] = (sn,)

    @property  # get TCC.13
    def units(self) -> CE | None:
        """
        id: TCC.13 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.13
        """
        return self._c_data[12][0]

    @units.setter  # set TCC.13
    def units(self, ce: CE | None):
        """
        id: TCC.13 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.13
        """
        self._c_data[12] = (ce,)

    @property  # get TCC.14
    def processing_type(self) -> ProcessingType | None:
        """
        id: TCC.14 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.14
        """
        return self._c_data[13][0]

    @processing_type.setter  # set TCC.14
    def processing_type(self, processing_type: ProcessingType | None):
        """
        id: TCC.14 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCC.14
        """
        self._c_data[13] = (processing_type,)
