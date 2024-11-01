from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SN import SN
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.AnalyteRepeatStatus import AnalyteRepeatStatus


"""
Test Code Detail - TCD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::TCD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    TCD,
    SN, CE, ID
)

tcd = TCD(  #  - The test code detail segment contains the data necessary to perform operations or calculations, or execute decisions by the laboratory automation system, and which are not supported by the original HL7 segments related to orders (ORC, OBR)
    universal_service_identifier=ce,  # CE(...)  # Required.
    auto_dilution_factor=None,  # SN(...) 
    rerun_dilution_factor=None,  # SN(...) 
    pre_dilution_factor=None,  # SN(...) 
    endogenous_content_of_pre_dilution_diluent=None,  # SN(...) 
    automatic_repeat_allowed=None,  # ID(...) 
    reflex_allowed=None,  # ID(...) 
    analyte_repeat_status=None,  # CE(...) 
)

-----END SEGMENT::TCD TEMPLATE-----
"""


class TCD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """TCD"""
    _hl7_name = """Test Code Detail"""
    _hl7_description = """The test code detail segment contains the data necessary to perform operations or calculations, or execute decisions by the laboratory automation system, and which are not supported by the original HL7 segments related to orders (ORC, OBR)"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCD"
    _c_length = (250, 20, 20, 20, 20, 1, 1, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, SN, SN, SN, SN, ID, ID, CE,)
    _c_aliases = ("TCD.1", "TCD.2", "TCD.3", "TCD.4", "TCD.5", "TCD.6", "TCD.7", "TCD.8",)
    _c_names = ("Universal Service Identifier", "Auto-Dilution Factor", "Rerun Dilution Factor", "Pre-Dilution Factor", "Endogenous Content of Pre-Dilution Diluent", "Automatic Repeat Allowed", "Reflex Allowed", "Analyte Repeat Status",)
    _c_attrs = ("universal_service_identifier", "auto_dilution_factor", "rerun_dilution_factor", "pre_dilution_factor", "endogenous_content_of_pre_dilution_diluent", "automatic_repeat_allowed", "reflex_allowed", "analyte_repeat_status",)
    # fmt: on

    def __init__(
        self,
        universal_service_identifier: CE | tuple[CE, ...],  # TCD.1
        auto_dilution_factor: SN | tuple[SN, ...] | None = None,  # TCD.2
        rerun_dilution_factor: SN | tuple[SN, ...] | None = None,  # TCD.3
        pre_dilution_factor: SN | tuple[SN, ...] | None = None,  # TCD.4
        endogenous_content_of_pre_dilution_diluent: SN
        | tuple[SN, ...]
        | None = None,  # TCD.5
        automatic_repeat_allowed: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # TCD.6
        reflex_allowed: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # TCD.7
        analyte_repeat_status: AnalyteRepeatStatus
        | CE
        | tuple[AnalyteRepeatStatus | CE, ...]
        | None = None,  # TCD.8
    ):
        """
        Test Code Detail - `TCD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCD>`_
        The test code detail segment contains the data necessary to perform operations or calculations, or execute decisions by the laboratory automation system, and which are not supported by the original HL7 segments related to orders (ORC, OBR).

        :param universal_service_identifier: Coded Element (id: TCD.1 | len: 250 | use: R | rpt: 1)
        :param auto_dilution_factor: Structured Numeric (id: TCD.2 | len: 20 | use: O | rpt: 1)
        :param rerun_dilution_factor: Structured Numeric (id: TCD.3 | len: 20 | use: O | rpt: 1)
        :param pre_dilution_factor: Structured Numeric (id: TCD.4 | len: 20 | use: O | rpt: 1)
        :param endogenous_content_of_pre_dilution_diluent: Structured Numeric (id: TCD.5 | len: 20 | use: O | rpt: 1)
        :param automatic_repeat_allowed: Coded values for HL7 tables (id: TCD.6 | len: 1 | use: O | rpt: 1)
        :param reflex_allowed: Coded values for HL7 tables (id: TCD.7 | len: 1 | use: O | rpt: 1)
        :param analyte_repeat_status: Coded Element (id: TCD.8 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.universal_service_identifier = universal_service_identifier
        self.auto_dilution_factor = auto_dilution_factor
        self.rerun_dilution_factor = rerun_dilution_factor
        self.pre_dilution_factor = pre_dilution_factor
        self.endogenous_content_of_pre_dilution_diluent = (
            endogenous_content_of_pre_dilution_diluent
        )
        self.automatic_repeat_allowed = automatic_repeat_allowed
        self.reflex_allowed = reflex_allowed
        self.analyte_repeat_status = analyte_repeat_status

    @property  # get TCD.1
    def universal_service_identifier(self) -> CE:
        """
        id: TCD.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.1
        """
        return self._c_data[0][0]

    @universal_service_identifier.setter  # set TCD.1
    def universal_service_identifier(self, ce: CE):
        """
        id: TCD.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.1
        """
        self._c_data[0] = (ce,)

    @property  # get TCD.2
    def auto_dilution_factor(self) -> SN | None:
        """
        id: TCD.2 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.2
        """
        return self._c_data[1][0]

    @auto_dilution_factor.setter  # set TCD.2
    def auto_dilution_factor(self, sn: SN | None):
        """
        id: TCD.2 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.2
        """
        self._c_data[1] = (sn,)

    @property  # get TCD.3
    def rerun_dilution_factor(self) -> SN | None:
        """
        id: TCD.3 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.3
        """
        return self._c_data[2][0]

    @rerun_dilution_factor.setter  # set TCD.3
    def rerun_dilution_factor(self, sn: SN | None):
        """
        id: TCD.3 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.3
        """
        self._c_data[2] = (sn,)

    @property  # get TCD.4
    def pre_dilution_factor(self) -> SN | None:
        """
        id: TCD.4 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.4
        """
        return self._c_data[3][0]

    @pre_dilution_factor.setter  # set TCD.4
    def pre_dilution_factor(self, sn: SN | None):
        """
        id: TCD.4 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.4
        """
        self._c_data[3] = (sn,)

    @property  # get TCD.5
    def endogenous_content_of_pre_dilution_diluent(self) -> SN | None:
        """
        id: TCD.5 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.5
        """
        return self._c_data[4][0]

    @endogenous_content_of_pre_dilution_diluent.setter  # set TCD.5
    def endogenous_content_of_pre_dilution_diluent(self, sn: SN | None):
        """
        id: TCD.5 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.5
        """
        self._c_data[4] = (sn,)

    @property  # get TCD.6
    def automatic_repeat_allowed(self) -> YesOrNoIndicator | None:
        """
        id: TCD.6 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.6
        """
        return self._c_data[5][0]

    @automatic_repeat_allowed.setter  # set TCD.6
    def automatic_repeat_allowed(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: TCD.6 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.6
        """
        self._c_data[5] = (yes_or_no_indicator,)

    @property  # get TCD.7
    def reflex_allowed(self) -> YesOrNoIndicator | None:
        """
        id: TCD.7 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.7
        """
        return self._c_data[6][0]

    @reflex_allowed.setter  # set TCD.7
    def reflex_allowed(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: TCD.7 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.7
        """
        self._c_data[6] = (yes_or_no_indicator,)

    @property  # get TCD.8
    def analyte_repeat_status(self) -> AnalyteRepeatStatus | None:
        """
        id: TCD.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.8
        """
        return self._c_data[7][0]

    @analyte_repeat_status.setter  # set TCD.8
    def analyte_repeat_status(self, analyte_repeat_status: AnalyteRepeatStatus | None):
        """
        id: TCD.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TCD.8
        """
        self._c_data[7] = (analyte_repeat_status,)
