from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TX import TX
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.PL import PL
from ..data_types.IS import IS
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.XCN import XCN
from ..tables.CategoryIdentifier import CategoryIdentifier
from ..tables.FormularyStatus import FormularyStatus
from ..tables.RepeatPattern import RepeatPattern
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.TransactionCode import TransactionCode
from ..tables.ConsentIdentifier import ConsentIdentifier
from ..tables.UnitsOfTime import UnitsOfTime


"""
Additional Basic Attributes - OM7
HL7 Version: 2.5.1

-----BEGIN SEGMENT::OM7 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OM7,
    TX, TS, ID, NM, PL, IS, ST, CE, XCN
)

om7 = OM7(  #  - The OM7 segment contains additional basic attributes that apply to the definition of most observations/services
    sequence_number_test_or_observation_master_file=nm,  # NM(...)  # Required.
    universal_service_identifier=ce,  # CE(...)  # Required.
    category_identifier=None,  # CE(...) 
    category_description=None,  # TX(...) 
    category_synonym=None,  # ST(...) 
    effective_test_or_service_start_date_or_time=None,  # TS(...) 
    effective_test_or_service_end_date_or_time=None,  # TS(...) 
    test_or_service_default_duration_quantity=None,  # NM(...) 
    test_or_service_default_duration_units=None,  # CE(...) 
    test_or_service_default_frequency=None,  # IS(...) 
    consent_indicator=None,  # ID(...) 
    consent_identifier=None,  # CE(...) 
    consent_effective_start_date_or_time=None,  # TS(...) 
    consent_effective_end_date_or_time=None,  # TS(...) 
    consent_interval_quantity=None,  # NM(...) 
    consent_interval_units=None,  # CE(...) 
    consent_waiting_period_quantity=None,  # NM(...) 
    consent_waiting_period_units=None,  # CE(...) 
    effective_date_or_time_of_change=None,  # TS(...) 
    entered_by=None,  # XCN(...) 
    orderable_at_location=None,  # PL(...) 
    formulary_status=None,  # IS(...) 
    special_order_indicator=None,  # ID(...) 
    primary_key_value_cdm=None,  # CE(...) 
)

-----END SEGMENT::OM7 TEMPLATE-----
"""


class OM7(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """OM7"""
    _hl7_name = """Additional Basic Attributes"""
    _hl7_description = """The OM7 segment contains additional basic attributes that apply to the definition of most observations/services"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM7"
    _c_length = (4, 250, 250, 200, 200, 26, 26, 5, 250, 60, 1, 250, 26, 26, 5, 250, 5, 250, 26, 250, 200, 1, 1, 250,)
    _c_rpt = (1, 1, 65535, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 65535,)
    _c_usage = ("R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "C", "O", "C", "O", "O", "O", "O", "O", "O",)
    _c_components = (NM, CE, CE, TX, ST, TS, TS, NM, CE, IS, ID, CE, TS, TS, NM, CE, NM, CE, TS, XCN, PL, IS, ID, CE,)
    _c_aliases = ("OM7.1", "OM7.2", "OM7.3", "OM7.4", "OM7.5", "OM7.6", "OM7.7", "OM7.8", "OM7.9", "OM7.10", "OM7.11", "OM7.12", "OM7.13", "OM7.14", "OM7.15", "OM7.16", "OM7.17", "OM7.18", "OM7.19", "OM7.20", "OM7.21", "OM7.22", "OM7.23", "OM7.24",)
    _c_names = ("Sequence Number - Test/Observation Master File", "Universal Service Identifier", "Category Identifier", "Category Description", "Category Synonym", "Effective Test/Service Start Date/Time", "Effective Test/Service End Date/Time", "Test/Service Default Duration Quantity", "Test/Service Default Duration Units", "Test/Service Default Frequency", "Consent Indicator", "Consent Identifier", "Consent Effective Start Date/Time", "Consent Effective End Date/Time", "Consent Interval Quantity", "Consent Interval Units", "Consent Waiting Period Quantity", "Consent Waiting Period Units", "Effective Date/Time of Change", "Entered By", "Orderable-at Location", "Formulary Status", "Special Order Indicator", "Primary Key Value - CDM",)
    _c_attrs = ("sequence_number_test_or_observation_master_file", "universal_service_identifier", "category_identifier", "category_description", "category_synonym", "effective_test_or_service_start_date_or_time", "effective_test_or_service_end_date_or_time", "test_or_service_default_duration_quantity", "test_or_service_default_duration_units", "test_or_service_default_frequency", "consent_indicator", "consent_identifier", "consent_effective_start_date_or_time", "consent_effective_end_date_or_time", "consent_interval_quantity", "consent_interval_units", "consent_waiting_period_quantity", "consent_waiting_period_units", "effective_date_or_time_of_change", "entered_by", "orderable_at_location", "formulary_status", "special_order_indicator", "primary_key_value_cdm",)
    # fmt: on

    def __init__(
        self,
        sequence_number_test_or_observation_master_file: NM | tuple[NM],  # OM7.1
        universal_service_identifier: CE | tuple[CE],  # OM7.2
        category_identifier: CategoryIdentifier
        | CE
        | tuple[CategoryIdentifier | CE]
        | None = None,  # OM7.3
        category_description: TX | tuple[TX] | None = None,  # OM7.4
        category_synonym: ST | tuple[ST] | None = None,  # OM7.5
        effective_test_or_service_start_date_or_time: TS
        | tuple[TS]
        | None = None,  # OM7.6
        effective_test_or_service_end_date_or_time: TS
        | tuple[TS]
        | None = None,  # OM7.7
        test_or_service_default_duration_quantity: NM
        | tuple[NM]
        | None = None,  # OM7.8
        test_or_service_default_duration_units: CE | tuple[CE] | None = None,  # OM7.9
        test_or_service_default_frequency: RepeatPattern
        | IS
        | tuple[RepeatPattern | IS]
        | None = None,  # OM7.10
        consent_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # OM7.11
        consent_identifier: ConsentIdentifier
        | CE
        | tuple[ConsentIdentifier | CE]
        | None = None,  # OM7.12
        consent_effective_start_date_or_time: TS | tuple[TS] | None = None,  # OM7.13
        consent_effective_end_date_or_time: TS | tuple[TS] | None = None,  # OM7.14
        consent_interval_quantity: NM | tuple[NM] | None = None,  # OM7.15
        consent_interval_units: UnitsOfTime
        | CE
        | tuple[UnitsOfTime | CE]
        | None = None,  # OM7.16
        consent_waiting_period_quantity: NM | tuple[NM] | None = None,  # OM7.17
        consent_waiting_period_units: UnitsOfTime
        | CE
        | tuple[UnitsOfTime | CE]
        | None = None,  # OM7.18
        effective_date_or_time_of_change: TS | tuple[TS] | None = None,  # OM7.19
        entered_by: XCN | tuple[XCN] | None = None,  # OM7.20
        orderable_at_location: PL | tuple[PL] | None = None,  # OM7.21
        formulary_status: FormularyStatus
        | IS
        | tuple[FormularyStatus | IS]
        | None = None,  # OM7.22
        special_order_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # OM7.23
        primary_key_value_cdm: TransactionCode
        | CE
        | tuple[TransactionCode | CE]
        | None = None,  # OM7.24
    ):
        """
        Additional Basic Attributes - `OM7 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM7>`_
        The OM7 segment contains additional basic attributes that apply to the definition of most observations/services.

        :param sequence_number_test_or_observation_master_file: Numeric (id: OM7.1 | len: 4 | use: R | rpt: 1)
        :param universal_service_identifier: Coded Element (id: OM7.2 | len: 250 | use: R | rpt: 1)
        :param category_identifier: Coded Element (id: OM7.3 | len: 250 | use: O | rpt: *)
        :param category_description: Text Data (id: OM7.4 | len: 200 | use: O | rpt: 1)
        :param category_synonym: String Data (id: OM7.5 | len: 200 | use: O | rpt: *)
        :param effective_test_or_service_start_date_or_time: Time Stamp (id: OM7.6 | len: 26 | use: O | rpt: 1)
        :param effective_test_or_service_end_date_or_time: Time Stamp (id: OM7.7 | len: 26 | use: O | rpt: 1)
        :param test_or_service_default_duration_quantity: Numeric (id: OM7.8 | len: 5 | use: O | rpt: 1)
        :param test_or_service_default_duration_units: Coded Element (id: OM7.9 | len: 250 | use: O | rpt: 1)
        :param test_or_service_default_frequency: Coded value for user-defined tables (id: OM7.10 | len: 60 | use: O | rpt: 1)
        :param consent_indicator: Coded values for HL7 tables (id: OM7.11 | len: 1 | use: O | rpt: 1)
        :param consent_identifier: Coded Element (id: OM7.12 | len: 250 | use: O | rpt: 1)
        :param consent_effective_start_date_or_time: Time Stamp (id: OM7.13 | len: 26 | use: O | rpt: 1)
        :param consent_effective_end_date_or_time: Time Stamp (id: OM7.14 | len: 26 | use: O | rpt: 1)
        :param consent_interval_quantity: Numeric (id: OM7.15 | len: 5 | use: O | rpt: 1)
        :param consent_interval_units: Coded Element (id: OM7.16 | len: 250 | use: C | rpt: 1)
        :param consent_waiting_period_quantity: Numeric (id: OM7.17 | len: 5 | use: O | rpt: 1)
        :param consent_waiting_period_units: Coded Element (id: OM7.18 | len: 250 | use: C | rpt: 1)
        :param effective_date_or_time_of_change: Time Stamp (id: OM7.19 | len: 26 | use: O | rpt: 1)
        :param entered_by: Extended Composite ID Number and Name for Persons (id: OM7.20 | len: 250 | use: O | rpt: 1)
        :param orderable_at_location: Person Location (id: OM7.21 | len: 200 | use: O | rpt: *)
        :param formulary_status: Coded value for user-defined tables (id: OM7.22 | len: 1 | use: O | rpt: 1)
        :param special_order_indicator: Coded values for HL7 tables (id: OM7.23 | len: 1 | use: O | rpt: 1)
        :param primary_key_value_cdm: Coded Element (id: OM7.24 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 24
        self.sequence_number_test_or_observation_master_file = (
            sequence_number_test_or_observation_master_file
        )
        self.universal_service_identifier = universal_service_identifier
        self.category_identifier = category_identifier
        self.category_description = category_description
        self.category_synonym = category_synonym
        self.effective_test_or_service_start_date_or_time = (
            effective_test_or_service_start_date_or_time
        )
        self.effective_test_or_service_end_date_or_time = (
            effective_test_or_service_end_date_or_time
        )
        self.test_or_service_default_duration_quantity = (
            test_or_service_default_duration_quantity
        )
        self.test_or_service_default_duration_units = (
            test_or_service_default_duration_units
        )
        self.test_or_service_default_frequency = test_or_service_default_frequency
        self.consent_indicator = consent_indicator
        self.consent_identifier = consent_identifier
        self.consent_effective_start_date_or_time = consent_effective_start_date_or_time
        self.consent_effective_end_date_or_time = consent_effective_end_date_or_time
        self.consent_interval_quantity = consent_interval_quantity
        self.consent_interval_units = consent_interval_units
        self.consent_waiting_period_quantity = consent_waiting_period_quantity
        self.consent_waiting_period_units = consent_waiting_period_units
        self.effective_date_or_time_of_change = effective_date_or_time_of_change
        self.entered_by = entered_by
        self.orderable_at_location = orderable_at_location
        self.formulary_status = formulary_status
        self.special_order_indicator = special_order_indicator
        self.primary_key_value_cdm = primary_key_value_cdm

    @property  # get OM7.1
    def sequence_number_test_or_observation_master_file(self) -> NM:
        """
        id: OM7.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.1
        """
        return self._c_data[0][0]

    @sequence_number_test_or_observation_master_file.setter  # set OM7.1
    def sequence_number_test_or_observation_master_file(self, nm: NM):
        """
        id: OM7.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.1
        """
        self._c_data[0] = (nm,)

    @property  # get OM7.2
    def universal_service_identifier(self) -> CE:
        """
        id: OM7.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.2
        """
        return self._c_data[1][0]

    @universal_service_identifier.setter  # set OM7.2
    def universal_service_identifier(self, ce: CE):
        """
        id: OM7.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.2
        """
        self._c_data[1] = (ce,)

    @property
    def category_identifier(self) -> tuple[CategoryIdentifier, ...] | tuple[None]:
        """
        id: OM7.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.3
        """
        return self._c_data[2]

    @category_identifier.setter  # set OM7.3
    def category_identifier(
        self, category_identifier: CategoryIdentifier | tuple[CategoryIdentifier] | None
    ):
        """
        id: OM7.3 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.3
        """
        if isinstance(category_identifier, tuple):
            self._c_data[2] = category_identifier
        else:
            self._c_data[2] = (category_identifier,)

    @property  # get OM7.4
    def category_description(self) -> TX | None:
        """
        id: OM7.4 | len: 200 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.4
        """
        return self._c_data[3][0]

    @category_description.setter  # set OM7.4
    def category_description(self, tx: TX | None):
        """
        id: OM7.4 | len: 200 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.4
        """
        self._c_data[3] = (tx,)

    @property
    def category_synonym(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: OM7.5 | len: 200 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.5
        """
        return self._c_data[4]

    @category_synonym.setter  # set OM7.5
    def category_synonym(self, st: ST | tuple[ST] | None):
        """
        id: OM7.5 | len: 200 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.5
        """
        if isinstance(st, tuple):
            self._c_data[4] = st
        else:
            self._c_data[4] = (st,)

    @property  # get OM7.6
    def effective_test_or_service_start_date_or_time(self) -> TS | None:
        """
        id: OM7.6 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.6
        """
        return self._c_data[5][0]

    @effective_test_or_service_start_date_or_time.setter  # set OM7.6
    def effective_test_or_service_start_date_or_time(self, ts: TS | None):
        """
        id: OM7.6 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.6
        """
        self._c_data[5] = (ts,)

    @property  # get OM7.7
    def effective_test_or_service_end_date_or_time(self) -> TS | None:
        """
        id: OM7.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.7
        """
        return self._c_data[6][0]

    @effective_test_or_service_end_date_or_time.setter  # set OM7.7
    def effective_test_or_service_end_date_or_time(self, ts: TS | None):
        """
        id: OM7.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.7
        """
        self._c_data[6] = (ts,)

    @property  # get OM7.8
    def test_or_service_default_duration_quantity(self) -> NM | None:
        """
        id: OM7.8 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.8
        """
        return self._c_data[7][0]

    @test_or_service_default_duration_quantity.setter  # set OM7.8
    def test_or_service_default_duration_quantity(self, nm: NM | None):
        """
        id: OM7.8 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.8
        """
        self._c_data[7] = (nm,)

    @property  # get OM7.9
    def test_or_service_default_duration_units(self) -> CE | None:
        """
        id: OM7.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.9
        """
        return self._c_data[8][0]

    @test_or_service_default_duration_units.setter  # set OM7.9
    def test_or_service_default_duration_units(self, ce: CE | None):
        """
        id: OM7.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.9
        """
        self._c_data[8] = (ce,)

    @property  # get OM7.10
    def test_or_service_default_frequency(self) -> RepeatPattern | None:
        """
        id: OM7.10 | len: 60 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.10
        """
        return self._c_data[9][0]

    @test_or_service_default_frequency.setter  # set OM7.10
    def test_or_service_default_frequency(self, repeat_pattern: RepeatPattern | None):
        """
        id: OM7.10 | len: 60 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.10
        """
        self._c_data[9] = (repeat_pattern,)

    @property  # get OM7.11
    def consent_indicator(self) -> YesOrNoIndicator | None:
        """
        id: OM7.11 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.11
        """
        return self._c_data[10][0]

    @consent_indicator.setter  # set OM7.11
    def consent_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: OM7.11 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.11
        """
        self._c_data[10] = (yes_or_no_indicator,)

    @property  # get OM7.12
    def consent_identifier(self) -> ConsentIdentifier | None:
        """
        id: OM7.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.12
        """
        return self._c_data[11][0]

    @consent_identifier.setter  # set OM7.12
    def consent_identifier(self, consent_identifier: ConsentIdentifier | None):
        """
        id: OM7.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.12
        """
        self._c_data[11] = (consent_identifier,)

    @property  # get OM7.13
    def consent_effective_start_date_or_time(self) -> TS | None:
        """
        id: OM7.13 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.13
        """
        return self._c_data[12][0]

    @consent_effective_start_date_or_time.setter  # set OM7.13
    def consent_effective_start_date_or_time(self, ts: TS | None):
        """
        id: OM7.13 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.13
        """
        self._c_data[12] = (ts,)

    @property  # get OM7.14
    def consent_effective_end_date_or_time(self) -> TS | None:
        """
        id: OM7.14 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.14
        """
        return self._c_data[13][0]

    @consent_effective_end_date_or_time.setter  # set OM7.14
    def consent_effective_end_date_or_time(self, ts: TS | None):
        """
        id: OM7.14 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.14
        """
        self._c_data[13] = (ts,)

    @property  # get OM7.15
    def consent_interval_quantity(self) -> NM | None:
        """
        id: OM7.15 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.15
        """
        return self._c_data[14][0]

    @consent_interval_quantity.setter  # set OM7.15
    def consent_interval_quantity(self, nm: NM | None):
        """
        id: OM7.15 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.15
        """
        self._c_data[14] = (nm,)

    @property  # get OM7.16
    def consent_interval_units(self) -> UnitsOfTime | None:
        """
        id: OM7.16 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.16
        """
        return self._c_data[15][0]

    @consent_interval_units.setter  # set OM7.16
    def consent_interval_units(self, units_of_time: UnitsOfTime | None):
        """
        id: OM7.16 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.16
        """
        self._c_data[15] = (units_of_time,)

    @property  # get OM7.17
    def consent_waiting_period_quantity(self) -> NM | None:
        """
        id: OM7.17 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.17
        """
        return self._c_data[16][0]

    @consent_waiting_period_quantity.setter  # set OM7.17
    def consent_waiting_period_quantity(self, nm: NM | None):
        """
        id: OM7.17 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.17
        """
        self._c_data[16] = (nm,)

    @property  # get OM7.18
    def consent_waiting_period_units(self) -> UnitsOfTime | None:
        """
        id: OM7.18 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.18
        """
        return self._c_data[17][0]

    @consent_waiting_period_units.setter  # set OM7.18
    def consent_waiting_period_units(self, units_of_time: UnitsOfTime | None):
        """
        id: OM7.18 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.18
        """
        self._c_data[17] = (units_of_time,)

    @property  # get OM7.19
    def effective_date_or_time_of_change(self) -> TS | None:
        """
        id: OM7.19 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.19
        """
        return self._c_data[18][0]

    @effective_date_or_time_of_change.setter  # set OM7.19
    def effective_date_or_time_of_change(self, ts: TS | None):
        """
        id: OM7.19 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.19
        """
        self._c_data[18] = (ts,)

    @property  # get OM7.20
    def entered_by(self) -> XCN | None:
        """
        id: OM7.20 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.20
        """
        return self._c_data[19][0]

    @entered_by.setter  # set OM7.20
    def entered_by(self, xcn: XCN | None):
        """
        id: OM7.20 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.20
        """
        self._c_data[19] = (xcn,)

    @property
    def orderable_at_location(self) -> tuple[PL, ...] | tuple[None]:
        """
        id: OM7.21 | len: 200 | use: O | rpt: *
        ---
        return_type: tuple[PL, ...]: (Person Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.21
        """
        return self._c_data[20]

    @orderable_at_location.setter  # set OM7.21
    def orderable_at_location(self, pl: PL | tuple[PL] | None):
        """
        id: OM7.21 | len: 200 | use: O | rpt: *
        ---
        param_type: PL | tuple[PL, ...]: (Person Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.21
        """
        if isinstance(pl, tuple):
            self._c_data[20] = pl
        else:
            self._c_data[20] = (pl,)

    @property  # get OM7.22
    def formulary_status(self) -> FormularyStatus | None:
        """
        id: OM7.22 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.22
        """
        return self._c_data[21][0]

    @formulary_status.setter  # set OM7.22
    def formulary_status(self, formulary_status: FormularyStatus | None):
        """
        id: OM7.22 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.22
        """
        self._c_data[21] = (formulary_status,)

    @property  # get OM7.23
    def special_order_indicator(self) -> YesOrNoIndicator | None:
        """
        id: OM7.23 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.23
        """
        return self._c_data[22][0]

    @special_order_indicator.setter  # set OM7.23
    def special_order_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: OM7.23 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.23
        """
        self._c_data[22] = (yes_or_no_indicator,)

    @property
    def primary_key_value_cdm(self) -> tuple[TransactionCode, ...] | tuple[None]:
        """
        id: OM7.24 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.24
        """
        return self._c_data[23]

    @primary_key_value_cdm.setter  # set OM7.24
    def primary_key_value_cdm(
        self, transaction_code: TransactionCode | tuple[TransactionCode] | None
    ):
        """
        id: OM7.24 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM7.24
        """
        if isinstance(transaction_code, tuple):
            self._c_data[23] = transaction_code
        else:
            self._c_data[23] = (transaction_code,)
