from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TS import TS
from ..data_types.IS import IS
from ..data_types.NM import NM
from ..data_types.XTN import XTN
from ..data_types.XAD import XAD
from ..data_types.CWE import CWE
from ..data_types.ST import ST
from ..data_types.ID import ID
from ..data_types.TX import TX
from ..tables.RelationshipModifier import RelationshipModifier
from ..tables.Modality import Modality
from ..tables.NatureOfServiceOrTestOrObservation import (
    NatureOfServiceOrTestOrObservation,
)
from ..tables.ReportingPriority import ReportingPriority
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.KindOfQuantity import KindOfQuantity
from ..tables.ConfidentialityCode import ConfidentialityCode
from ..tables.ProcessingPriority import ProcessingPriority
from ..tables.ValueType import ValueType
from ..tables.DurationCategories import DurationCategories


"""
General Segment - OM1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::OM1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OM1,
    CE, TS, IS, NM, XTN, XAD, CWE, ST, ID, TX
)

om1 = OM1(  #  - The OM1 segment contains the attributes that apply to the definition of most observations
    sequence_number_test_or_observation_master_file=nm,  # NM(...)  # Required.
    producers_service_or_test_or_observation_id=ce,  # CE(...)  # Required.
    permitted_data_types=None,  # ID(...) 
    specimen_required=id,  # ID(...)  # Required.
    producer_id=ce,  # CE(...)  # Required.
    observation_description=None,  # TX(...) 
    other_service_or_test_or_observation_ids_for_the_observation=None,  # CE(...) 
    other_names=st,  # ST(...)  # Required.
    preferred_report_name_for_the_observation=None,  # ST(...) 
    preferred_short_name_or_mnemonic_for_observation=None,  # ST(...) 
    preferred_long_name_for_the_observation=None,  # ST(...) 
    orderability=None,  # ID(...) 
    identity_of_instrument_used_to_perform_this_study=None,  # CE(...) 
    coded_representation_of_method=None,  # CE(...) 
    portable_device_indicator=None,  # ID(...) 
    observation_producing_department_or_section=None,  # CE(...) 
    telephone_number_of_section=None,  # XTN(...) 
    nature_of_service_or_test_or_observation=_is,  # IS(...)  # Required.
    report_subheader=None,  # CE(...) 
    report_display_order=None,  # ST(...) 
    date_or_time_stamp_for_any_change_in_definition_for_the_observation=None,  # TS(...) 
    effective_date_or_time_of_change=None,  # TS(...) 
    typical_turn_around_time=None,  # NM(...) 
    processing_time=None,  # NM(...) 
    processing_priority=None,  # ID(...) 
    reporting_priority=None,  # ID(...) 
    outside_site=None,  # CE(...) 
    address_of_outside_site=None,  # XAD(...) 
    phone_number_of_outside_site=None,  # XTN(...) 
    confidentiality_code=None,  # CWE(...) 
    observations_required_to_interpret_the_observation=None,  # CE(...) 
    interpretation_of_observations=None,  # TX(...) 
    contraindications_to_observations=None,  # CE(...) 
    reflex_tests_or_observations=None,  # CE(...) 
    rules_that_trigger_reflex_testing=None,  # TX(...) 
    fixed_canned_message=None,  # CE(...) 
    patient_preparation=None,  # TX(...) 
    procedure_medication=None,  # CE(...) 
    factors_that_may_affect_the_observation=None,  # TX(...) 
    service_or_test_or_observation_performance_schedule=None,  # ST(...) 
    description_of_test_methods=None,  # TX(...) 
    kind_of_quantity_observed=None,  # CE(...) 
    point_versus_interval=None,  # CE(...) 
    challenge_information=None,  # TX(...) 
    relationship_modifier=None,  # CE(...) 
    target_anatomic_site_of_test=None,  # CE(...) 
    modality_of_imaging_measurement=None,  # CE(...) 
)

-----END SEGMENT::OM1 TEMPLATE-----
"""


class OM1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """OM1"""
    _hl7_name = """General Segment"""
    _hl7_description = """The OM1 segment contains the attributes that apply to the definition of most observations"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM1"
    _c_length = (4, 250, 12, 1, 250, 200, 250, 200, 30, 8, 200, 1, 250, 250, 1, 250, 250, 1, 250, 20, 26, 26, 20, 20, 40, 5, 250, 250, 250, 250, 250, 65536, 250, 250, 80, 250, 200, 250, 200, 60, 65536, 250, 250, 200, 250, 250, 250,)
    _c_rpt = (1, 1, 65535, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 65535, 65535, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 65535, 65535, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "O", "R", "R", "O", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (NM, CE, ID, ID, CE, TX, CE, ST, ST, ST, ST, ID, CE, CE, ID, CE, XTN, IS, CE, ST, TS, TS, NM, NM, ID, ID, CE, XAD, XTN, CWE, CE, TX, CE, CE, TX, CE, TX, CE, TX, ST, TX, CE, CE, TX, CE, CE, CE,)
    _c_aliases = ("OM1.1", "OM1.2", "OM1.3", "OM1.4", "OM1.5", "OM1.6", "OM1.7", "OM1.8", "OM1.9", "OM1.10", "OM1.11", "OM1.12", "OM1.13", "OM1.14", "OM1.15", "OM1.16", "OM1.17", "OM1.18", "OM1.19", "OM1.20", "OM1.21", "OM1.22", "OM1.23", "OM1.24", "OM1.25", "OM1.26", "OM1.27", "OM1.28", "OM1.29", "OM1.30", "OM1.31", "OM1.32", "OM1.33", "OM1.34", "OM1.35", "OM1.36", "OM1.37", "OM1.38", "OM1.39", "OM1.40", "OM1.41", "OM1.42", "OM1.43", "OM1.44", "OM1.45", "OM1.46", "OM1.47",)
    _c_names = ("Sequence Number - Test/Observation Master File", "Producer's Service/Test/Observation ID", "Permitted Data Types", "Specimen Required", "Producer ID", "Observation Description", "Other Service/Test/Observation IDs for the Observation", "Other Names", "Preferred Report Name for the Observation", "Preferred Short Name or Mnemonic for Observation", "Preferred Long Name for the Observation", "Orderability", "Identity of Instrument Used to Perform this Study", "Coded Representation of Method", "Portable Device Indicator", "Observation Producing Department/Section", "Telephone Number of Section", "Nature of Service/Test/Observation", "Report Subheader", "Report Display Order", "Date/Time Stamp for any change in Definition for the Observation", "Effective Date/Time of Change", "Typical Turn-Around Time", "Processing Time", "Processing Priority", "Reporting Priority", "Outside Site(s) Where Observation may be Performed ", "Address of Outside Site(s)", "Phone Number of Outside Site", "Confidentiality Code", "Observations Required to Interpret the Observation", "Interpretation of Observations", "Contraindications to Observations", "Reflex Tests/Observations", "Rules that Trigger Reflex Testing", "Fixed Canned Message", "Patient Preparation", "Procedure Medication", "Factors that may Affect the Observation", "Service/Test/Observation Performance Schedule", "Description of Test Methods", "Kind of Quantity Observed", "Point Versus Interval", "Challenge Information", "Relationship Modifier", "Target Anatomic Site Of Test", "Modality Of Imaging Measurement",)
    _c_attrs = ("sequence_number_test_or_observation_master_file", "producers_service_or_test_or_observation_id", "permitted_data_types", "specimen_required", "producer_id", "observation_description", "other_service_or_test_or_observation_ids_for_the_observation", "other_names", "preferred_report_name_for_the_observation", "preferred_short_name_or_mnemonic_for_observation", "preferred_long_name_for_the_observation", "orderability", "identity_of_instrument_used_to_perform_this_study", "coded_representation_of_method", "portable_device_indicator", "observation_producing_department_or_section", "telephone_number_of_section", "nature_of_service_or_test_or_observation", "report_subheader", "report_display_order", "date_or_time_stamp_for_any_change_in_definition_for_the_observation", "effective_date_or_time_of_change", "typical_turn_around_time", "processing_time", "processing_priority", "reporting_priority", "outside_site", "address_of_outside_site", "phone_number_of_outside_site", "confidentiality_code", "observations_required_to_interpret_the_observation", "interpretation_of_observations", "contraindications_to_observations", "reflex_tests_or_observations", "rules_that_trigger_reflex_testing", "fixed_canned_message", "patient_preparation", "procedure_medication", "factors_that_may_affect_the_observation", "service_or_test_or_observation_performance_schedule", "description_of_test_methods", "kind_of_quantity_observed", "point_versus_interval", "challenge_information", "relationship_modifier", "target_anatomic_site_of_test", "modality_of_imaging_measurement",)
    # fmt: on

    def __init__(
        self,
        sequence_number_test_or_observation_master_file: NM | tuple[NM, ...],  # OM1.1
        producers_service_or_test_or_observation_id: CE | tuple[CE, ...],  # OM1.2
        specimen_required: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...],  # OM1.4
        producer_id: CE | tuple[CE, ...],  # OM1.5
        other_names: ST | tuple[ST, ...],  # OM1.8
        nature_of_service_or_test_or_observation: NatureOfServiceOrTestOrObservation
        | IS
        | tuple[NatureOfServiceOrTestOrObservation | IS, ...],  # OM1.18
        permitted_data_types: ValueType
        | ID
        | tuple[ValueType | ID, ...]
        | None = None,  # OM1.3
        observation_description: TX | tuple[TX, ...] | None = None,  # OM1.6
        other_service_or_test_or_observation_ids_for_the_observation: CE
        | tuple[CE, ...]
        | None = None,  # OM1.7
        preferred_report_name_for_the_observation: ST
        | tuple[ST, ...]
        | None = None,  # OM1.9
        preferred_short_name_or_mnemonic_for_observation: ST
        | tuple[ST, ...]
        | None = None,  # OM1.10
        preferred_long_name_for_the_observation: ST
        | tuple[ST, ...]
        | None = None,  # OM1.11
        orderability: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # OM1.12
        identity_of_instrument_used_to_perform_this_study: CE
        | tuple[CE, ...]
        | None = None,  # OM1.13
        coded_representation_of_method: CE | tuple[CE, ...] | None = None,  # OM1.14
        portable_device_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # OM1.15
        observation_producing_department_or_section: CE
        | tuple[CE, ...]
        | None = None,  # OM1.16
        telephone_number_of_section: XTN | tuple[XTN, ...] | None = None,  # OM1.17
        report_subheader: CE | tuple[CE, ...] | None = None,  # OM1.19
        report_display_order: ST | tuple[ST, ...] | None = None,  # OM1.20
        date_or_time_stamp_for_any_change_in_definition_for_the_observation: TS
        | tuple[TS, ...]
        | None = None,  # OM1.21
        effective_date_or_time_of_change: TS | tuple[TS, ...] | None = None,  # OM1.22
        typical_turn_around_time: NM | tuple[NM, ...] | None = None,  # OM1.23
        processing_time: NM | tuple[NM, ...] | None = None,  # OM1.24
        processing_priority: ProcessingPriority
        | ID
        | tuple[ProcessingPriority | ID, ...]
        | None = None,  # OM1.25
        reporting_priority: ReportingPriority
        | ID
        | tuple[ReportingPriority | ID, ...]
        | None = None,  # OM1.26
        outside_site: CE | tuple[CE, ...] | None = None,  # OM1.27
        address_of_outside_site: XAD | tuple[XAD, ...] | None = None,  # OM1.28
        phone_number_of_outside_site: XTN | tuple[XTN, ...] | None = None,  # OM1.29
        confidentiality_code: ConfidentialityCode
        | CWE
        | tuple[ConfidentialityCode | CWE, ...]
        | None = None,  # OM1.30
        observations_required_to_interpret_the_observation: CE
        | tuple[CE, ...]
        | None = None,  # OM1.31
        interpretation_of_observations: TX | tuple[TX, ...] | None = None,  # OM1.32
        contraindications_to_observations: CE | tuple[CE, ...] | None = None,  # OM1.33
        reflex_tests_or_observations: CE | tuple[CE, ...] | None = None,  # OM1.34
        rules_that_trigger_reflex_testing: TX | tuple[TX, ...] | None = None,  # OM1.35
        fixed_canned_message: CE | tuple[CE, ...] | None = None,  # OM1.36
        patient_preparation: TX | tuple[TX, ...] | None = None,  # OM1.37
        procedure_medication: CE | tuple[CE, ...] | None = None,  # OM1.38
        factors_that_may_affect_the_observation: TX
        | tuple[TX, ...]
        | None = None,  # OM1.39
        service_or_test_or_observation_performance_schedule: ST
        | tuple[ST, ...]
        | None = None,  # OM1.40
        description_of_test_methods: TX | tuple[TX, ...] | None = None,  # OM1.41
        kind_of_quantity_observed: KindOfQuantity
        | CE
        | tuple[KindOfQuantity | CE, ...]
        | None = None,  # OM1.42
        point_versus_interval: DurationCategories
        | CE
        | tuple[DurationCategories | CE, ...]
        | None = None,  # OM1.43
        challenge_information: TX | tuple[TX, ...] | None = None,  # OM1.44
        relationship_modifier: RelationshipModifier
        | CE
        | tuple[RelationshipModifier | CE, ...]
        | None = None,  # OM1.45
        target_anatomic_site_of_test: CE | tuple[CE, ...] | None = None,  # OM1.46
        modality_of_imaging_measurement: Modality
        | CE
        | tuple[Modality | CE, ...]
        | None = None,  # OM1.47
    ):
        """
        General Segment - `OM1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM1>`_
        The OM1 segment contains the attributes that apply to the definition of most observations.  This segment also contains the field attributes that specify what additional segments might also be defined for this observation.

        :param sequence_number_test_or_observation_master_file: Numeric (id: OM1.1 | len: 4 | use: R | rpt: 1)
        :param producers_service_or_test_or_observation_id: Coded Element (id: OM1.2 | len: 250 | use: R | rpt: 1)
        :param permitted_data_types: Coded values for HL7 tables (id: OM1.3 | len: 12 | use: O | rpt: *)
        :param specimen_required: Coded values for HL7 tables (id: OM1.4 | len: 1 | use: R | rpt: 1)
        :param producer_id: Coded Element (id: OM1.5 | len: 250 | use: R | rpt: 1)
        :param observation_description: Text Data (id: OM1.6 | len: 200 | use: O | rpt: 1)
        :param other_service_or_test_or_observation_ids_for_the_observation: Coded Element (id: OM1.7 | len: 250 | use: O | rpt: 1)
        :param other_names: String Data (id: OM1.8 | len: 200 | use: R | rpt: *)
        :param preferred_report_name_for_the_observation: String Data (id: OM1.9 | len: 30 | use: O | rpt: 1)
        :param preferred_short_name_or_mnemonic_for_observation: String Data (id: OM1.10 | len: 8 | use: O | rpt: 1)
        :param preferred_long_name_for_the_observation: String Data (id: OM1.11 | len: 200 | use: O | rpt: 1)
        :param orderability: Coded values for HL7 tables (id: OM1.12 | len: 1 | use: O | rpt: 1)
        :param identity_of_instrument_used_to_perform_this_study: Coded Element (id: OM1.13 | len: 250 | use: O | rpt: *)
        :param coded_representation_of_method: Coded Element (id: OM1.14 | len: 250 | use: O | rpt: *)
        :param portable_device_indicator: Coded values for HL7 tables (id: OM1.15 | len: 1 | use: O | rpt: 1)
        :param observation_producing_department_or_section: Coded Element (id: OM1.16 | len: 250 | use: O | rpt: *)
        :param telephone_number_of_section: Extended Telecommunication Number (id: OM1.17 | len: 250 | use: O | rpt: 1)
        :param nature_of_service_or_test_or_observation: Coded value for user-defined tables (id: OM1.18 | len: 1 | use: R | rpt: 1)
        :param report_subheader: Coded Element (id: OM1.19 | len: 250 | use: O | rpt: 1)
        :param report_display_order: String Data (id: OM1.20 | len: 20 | use: O | rpt: 1)
        :param date_or_time_stamp_for_any_change_in_definition_for_the_observation: Time Stamp (id: OM1.21 | len: 26 | use: O | rpt: 1)
        :param effective_date_or_time_of_change: Time Stamp (id: OM1.22 | len: 26 | use: O | rpt: 1)
        :param typical_turn_around_time: Numeric (id: OM1.23 | len: 20 | use: O | rpt: 1)
        :param processing_time: Numeric (id: OM1.24 | len: 20 | use: O | rpt: 1)
        :param processing_priority: Coded values for HL7 tables (id: OM1.25 | len: 40 | use: O | rpt: *)
        :param reporting_priority: Coded values for HL7 tables (id: OM1.26 | len: 5 | use: O | rpt: 1)
        :param outside_site: Coded Element (id: OM1.27 | len: 250 | use: O | rpt: *)
        :param address_of_outside_site: Extended Address (id: OM1.28 | len: 250 | use: O | rpt: *)
        :param phone_number_of_outside_site: Extended Telecommunication Number (id: OM1.29 | len: 250 | use: O | rpt: 1)
        :param confidentiality_code: Coded with Exceptions (id: OM1.30 | len: 250 | use: O | rpt: 1)
        :param observations_required_to_interpret_the_observation: Coded Element (id: OM1.31 | len: 250 | use: O | rpt: 1)
        :param interpretation_of_observations: Text Data (id: OM1.32 | len: 65536 | use: O | rpt: 1)
        :param contraindications_to_observations: Coded Element (id: OM1.33 | len: 250 | use: O | rpt: 1)
        :param reflex_tests_or_observations: Coded Element (id: OM1.34 | len: 250 | use: O | rpt: *)
        :param rules_that_trigger_reflex_testing: Text Data (id: OM1.35 | len: 80 | use: O | rpt: 1)
        :param fixed_canned_message: Coded Element (id: OM1.36 | len: 250 | use: O | rpt: 1)
        :param patient_preparation: Text Data (id: OM1.37 | len: 200 | use: O | rpt: 1)
        :param procedure_medication: Coded Element (id: OM1.38 | len: 250 | use: O | rpt: 1)
        :param factors_that_may_affect_the_observation: Text Data (id: OM1.39 | len: 200 | use: O | rpt: 1)
        :param service_or_test_or_observation_performance_schedule: String Data (id: OM1.40 | len: 60 | use: O | rpt: *)
        :param description_of_test_methods: Text Data (id: OM1.41 | len: 65536 | use: O | rpt: 1)
        :param kind_of_quantity_observed: Coded Element (id: OM1.42 | len: 250 | use: O | rpt: 1)
        :param point_versus_interval: Coded Element (id: OM1.43 | len: 250 | use: O | rpt: 1)
        :param challenge_information: Text Data (id: OM1.44 | len: 200 | use: O | rpt: 1)
        :param relationship_modifier: Coded Element (id: OM1.45 | len: 250 | use: O | rpt: 1)
        :param target_anatomic_site_of_test: Coded Element (id: OM1.46 | len: 250 | use: O | rpt: 1)
        :param modality_of_imaging_measurement: Coded Element (id: OM1.47 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 47
        self.sequence_number_test_or_observation_master_file = (
            sequence_number_test_or_observation_master_file
        )
        self.producers_service_or_test_or_observation_id = (
            producers_service_or_test_or_observation_id
        )
        self.permitted_data_types = permitted_data_types
        self.specimen_required = specimen_required
        self.producer_id = producer_id
        self.observation_description = observation_description
        self.other_service_or_test_or_observation_ids_for_the_observation = (
            other_service_or_test_or_observation_ids_for_the_observation
        )
        self.other_names = other_names
        self.preferred_report_name_for_the_observation = (
            preferred_report_name_for_the_observation
        )
        self.preferred_short_name_or_mnemonic_for_observation = (
            preferred_short_name_or_mnemonic_for_observation
        )
        self.preferred_long_name_for_the_observation = (
            preferred_long_name_for_the_observation
        )
        self.orderability = orderability
        self.identity_of_instrument_used_to_perform_this_study = (
            identity_of_instrument_used_to_perform_this_study
        )
        self.coded_representation_of_method = coded_representation_of_method
        self.portable_device_indicator = portable_device_indicator
        self.observation_producing_department_or_section = (
            observation_producing_department_or_section
        )
        self.telephone_number_of_section = telephone_number_of_section
        self.nature_of_service_or_test_or_observation = (
            nature_of_service_or_test_or_observation
        )
        self.report_subheader = report_subheader
        self.report_display_order = report_display_order
        self.date_or_time_stamp_for_any_change_in_definition_for_the_observation = (
            date_or_time_stamp_for_any_change_in_definition_for_the_observation
        )
        self.effective_date_or_time_of_change = effective_date_or_time_of_change
        self.typical_turn_around_time = typical_turn_around_time
        self.processing_time = processing_time
        self.processing_priority = processing_priority
        self.reporting_priority = reporting_priority
        self.outside_site = outside_site
        self.address_of_outside_site = address_of_outside_site
        self.phone_number_of_outside_site = phone_number_of_outside_site
        self.confidentiality_code = confidentiality_code
        self.observations_required_to_interpret_the_observation = (
            observations_required_to_interpret_the_observation
        )
        self.interpretation_of_observations = interpretation_of_observations
        self.contraindications_to_observations = contraindications_to_observations
        self.reflex_tests_or_observations = reflex_tests_or_observations
        self.rules_that_trigger_reflex_testing = rules_that_trigger_reflex_testing
        self.fixed_canned_message = fixed_canned_message
        self.patient_preparation = patient_preparation
        self.procedure_medication = procedure_medication
        self.factors_that_may_affect_the_observation = (
            factors_that_may_affect_the_observation
        )
        self.service_or_test_or_observation_performance_schedule = (
            service_or_test_or_observation_performance_schedule
        )
        self.description_of_test_methods = description_of_test_methods
        self.kind_of_quantity_observed = kind_of_quantity_observed
        self.point_versus_interval = point_versus_interval
        self.challenge_information = challenge_information
        self.relationship_modifier = relationship_modifier
        self.target_anatomic_site_of_test = target_anatomic_site_of_test
        self.modality_of_imaging_measurement = modality_of_imaging_measurement

    @property  # get OM1.1
    def sequence_number_test_or_observation_master_file(self) -> NM:
        """
        id: OM1.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.1
        """
        return self._c_data[0][0]

    @sequence_number_test_or_observation_master_file.setter  # set OM1.1
    def sequence_number_test_or_observation_master_file(self, nm: NM):
        """
        id: OM1.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.1
        """
        self._c_data[0] = (nm,)

    @property  # get OM1.2
    def producers_service_or_test_or_observation_id(self) -> CE:
        """
        id: OM1.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.2
        """
        return self._c_data[1][0]

    @producers_service_or_test_or_observation_id.setter  # set OM1.2
    def producers_service_or_test_or_observation_id(self, ce: CE):
        """
        id: OM1.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.2
        """
        self._c_data[1] = (ce,)

    @property
    def permitted_data_types(self) -> tuple[ValueType, ...] | tuple[None]:
        """
        id: OM1.3 | len: 12 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.3
        """
        return self._c_data[2]

    @permitted_data_types.setter  # set OM1.3
    def permitted_data_types(self, value_type: ValueType | tuple[ValueType] | None):
        """
        id: OM1.3 | len: 12 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.3
        """
        if isinstance(value_type, tuple):
            self._c_data[2] = value_type
        else:
            self._c_data[2] = (value_type,)

    @property  # get OM1.4
    def specimen_required(self) -> YesOrNoIndicator:
        """
        id: OM1.4 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.4
        """
        return self._c_data[3][0]

    @specimen_required.setter  # set OM1.4
    def specimen_required(self, yes_or_no_indicator: YesOrNoIndicator):
        """
        id: OM1.4 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.4
        """
        self._c_data[3] = (yes_or_no_indicator,)

    @property  # get OM1.5
    def producer_id(self) -> CE:
        """
        id: OM1.5 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.5
        """
        return self._c_data[4][0]

    @producer_id.setter  # set OM1.5
    def producer_id(self, ce: CE):
        """
        id: OM1.5 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.5
        """
        self._c_data[4] = (ce,)

    @property  # get OM1.6
    def observation_description(self) -> TX | None:
        """
        id: OM1.6 | len: 200 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.6
        """
        return self._c_data[5][0]

    @observation_description.setter  # set OM1.6
    def observation_description(self, tx: TX | None):
        """
        id: OM1.6 | len: 200 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.6
        """
        self._c_data[5] = (tx,)

    @property  # get OM1.7
    def other_service_or_test_or_observation_ids_for_the_observation(self) -> CE | None:
        """
        id: OM1.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.7
        """
        return self._c_data[6][0]

    @other_service_or_test_or_observation_ids_for_the_observation.setter  # set OM1.7
    def other_service_or_test_or_observation_ids_for_the_observation(
        self, ce: CE | None
    ):
        """
        id: OM1.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.7
        """
        self._c_data[6] = (ce,)

    @property
    def other_names(self) -> tuple[ST, ...]:
        """
        id: OM1.8 | len: 200 | use: R | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.8
        """
        return self._c_data[7]

    @other_names.setter  # set OM1.8
    def other_names(self, st: ST | tuple[ST]):
        """
        id: OM1.8 | len: 200 | use: R | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.8
        """
        if isinstance(st, tuple):
            self._c_data[7] = st
        else:
            self._c_data[7] = (st,)

    @property  # get OM1.9
    def preferred_report_name_for_the_observation(self) -> ST | None:
        """
        id: OM1.9 | len: 30 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.9
        """
        return self._c_data[8][0]

    @preferred_report_name_for_the_observation.setter  # set OM1.9
    def preferred_report_name_for_the_observation(self, st: ST | None):
        """
        id: OM1.9 | len: 30 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.9
        """
        self._c_data[8] = (st,)

    @property  # get OM1.10
    def preferred_short_name_or_mnemonic_for_observation(self) -> ST | None:
        """
        id: OM1.10 | len: 8 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.10
        """
        return self._c_data[9][0]

    @preferred_short_name_or_mnemonic_for_observation.setter  # set OM1.10
    def preferred_short_name_or_mnemonic_for_observation(self, st: ST | None):
        """
        id: OM1.10 | len: 8 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.10
        """
        self._c_data[9] = (st,)

    @property  # get OM1.11
    def preferred_long_name_for_the_observation(self) -> ST | None:
        """
        id: OM1.11 | len: 200 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.11
        """
        return self._c_data[10][0]

    @preferred_long_name_for_the_observation.setter  # set OM1.11
    def preferred_long_name_for_the_observation(self, st: ST | None):
        """
        id: OM1.11 | len: 200 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.11
        """
        self._c_data[10] = (st,)

    @property  # get OM1.12
    def orderability(self) -> YesOrNoIndicator | None:
        """
        id: OM1.12 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.12
        """
        return self._c_data[11][0]

    @orderability.setter  # set OM1.12
    def orderability(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: OM1.12 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.12
        """
        self._c_data[11] = (yes_or_no_indicator,)

    @property
    def identity_of_instrument_used_to_perform_this_study(
        self,
    ) -> tuple[CE, ...] | tuple[None]:
        """
        id: OM1.13 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.13
        """
        return self._c_data[12]

    @identity_of_instrument_used_to_perform_this_study.setter  # set OM1.13
    def identity_of_instrument_used_to_perform_this_study(
        self, ce: CE | tuple[CE] | None
    ):
        """
        id: OM1.13 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.13
        """
        if isinstance(ce, tuple):
            self._c_data[12] = ce
        else:
            self._c_data[12] = (ce,)

    @property
    def coded_representation_of_method(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: OM1.14 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.14
        """
        return self._c_data[13]

    @coded_representation_of_method.setter  # set OM1.14
    def coded_representation_of_method(self, ce: CE | tuple[CE] | None):
        """
        id: OM1.14 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.14
        """
        if isinstance(ce, tuple):
            self._c_data[13] = ce
        else:
            self._c_data[13] = (ce,)

    @property  # get OM1.15
    def portable_device_indicator(self) -> YesOrNoIndicator | None:
        """
        id: OM1.15 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.15
        """
        return self._c_data[14][0]

    @portable_device_indicator.setter  # set OM1.15
    def portable_device_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: OM1.15 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.15
        """
        self._c_data[14] = (yes_or_no_indicator,)

    @property
    def observation_producing_department_or_section(
        self,
    ) -> tuple[CE, ...] | tuple[None]:
        """
        id: OM1.16 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.16
        """
        return self._c_data[15]

    @observation_producing_department_or_section.setter  # set OM1.16
    def observation_producing_department_or_section(self, ce: CE | tuple[CE] | None):
        """
        id: OM1.16 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.16
        """
        if isinstance(ce, tuple):
            self._c_data[15] = ce
        else:
            self._c_data[15] = (ce,)

    @property  # get OM1.17
    def telephone_number_of_section(self) -> XTN | None:
        """
        id: OM1.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.17
        """
        return self._c_data[16][0]

    @telephone_number_of_section.setter  # set OM1.17
    def telephone_number_of_section(self, xtn: XTN | None):
        """
        id: OM1.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.17
        """
        self._c_data[16] = (xtn,)

    @property  # get OM1.18
    def nature_of_service_or_test_or_observation(
        self,
    ) -> NatureOfServiceOrTestOrObservation:
        """
        id: OM1.18 | len: 1 | use: R | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.18
        """
        return self._c_data[17][0]

    @nature_of_service_or_test_or_observation.setter  # set OM1.18
    def nature_of_service_or_test_or_observation(
        self,
        nature_of_service_or_test_or_observation: NatureOfServiceOrTestOrObservation,
    ):
        """
        id: OM1.18 | len: 1 | use: R | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.18
        """
        self._c_data[17] = (nature_of_service_or_test_or_observation,)

    @property  # get OM1.19
    def report_subheader(self) -> CE | None:
        """
        id: OM1.19 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.19
        """
        return self._c_data[18][0]

    @report_subheader.setter  # set OM1.19
    def report_subheader(self, ce: CE | None):
        """
        id: OM1.19 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.19
        """
        self._c_data[18] = (ce,)

    @property  # get OM1.20
    def report_display_order(self) -> ST | None:
        """
        id: OM1.20 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.20
        """
        return self._c_data[19][0]

    @report_display_order.setter  # set OM1.20
    def report_display_order(self, st: ST | None):
        """
        id: OM1.20 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.20
        """
        self._c_data[19] = (st,)

    @property  # get OM1.21
    def date_or_time_stamp_for_any_change_in_definition_for_the_observation(
        self,
    ) -> TS | None:
        """
        id: OM1.21 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.21
        """
        return self._c_data[20][0]

    @date_or_time_stamp_for_any_change_in_definition_for_the_observation.setter  # set OM1.21
    def date_or_time_stamp_for_any_change_in_definition_for_the_observation(
        self, ts: TS | None
    ):
        """
        id: OM1.21 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.21
        """
        self._c_data[20] = (ts,)

    @property  # get OM1.22
    def effective_date_or_time_of_change(self) -> TS | None:
        """
        id: OM1.22 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.22
        """
        return self._c_data[21][0]

    @effective_date_or_time_of_change.setter  # set OM1.22
    def effective_date_or_time_of_change(self, ts: TS | None):
        """
        id: OM1.22 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.22
        """
        self._c_data[21] = (ts,)

    @property  # get OM1.23
    def typical_turn_around_time(self) -> NM | None:
        """
        id: OM1.23 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.23
        """
        return self._c_data[22][0]

    @typical_turn_around_time.setter  # set OM1.23
    def typical_turn_around_time(self, nm: NM | None):
        """
        id: OM1.23 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.23
        """
        self._c_data[22] = (nm,)

    @property  # get OM1.24
    def processing_time(self) -> NM | None:
        """
        id: OM1.24 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.24
        """
        return self._c_data[23][0]

    @processing_time.setter  # set OM1.24
    def processing_time(self, nm: NM | None):
        """
        id: OM1.24 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.24
        """
        self._c_data[23] = (nm,)

    @property
    def processing_priority(self) -> tuple[ProcessingPriority, ...] | tuple[None]:
        """
        id: OM1.25 | len: 40 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.25
        """
        return self._c_data[24]

    @processing_priority.setter  # set OM1.25
    def processing_priority(
        self, processing_priority: ProcessingPriority | tuple[ProcessingPriority] | None
    ):
        """
        id: OM1.25 | len: 40 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.25
        """
        if isinstance(processing_priority, tuple):
            self._c_data[24] = processing_priority
        else:
            self._c_data[24] = (processing_priority,)

    @property  # get OM1.26
    def reporting_priority(self) -> ReportingPriority | None:
        """
        id: OM1.26 | len: 5 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.26
        """
        return self._c_data[25][0]

    @reporting_priority.setter  # set OM1.26
    def reporting_priority(self, reporting_priority: ReportingPriority | None):
        """
        id: OM1.26 | len: 5 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.26
        """
        self._c_data[25] = (reporting_priority,)

    @property
    def outside_site(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: OM1.27 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.27
        """
        return self._c_data[26]

    @outside_site.setter  # set OM1.27
    def outside_site(self, ce: CE | tuple[CE] | None):
        """
        id: OM1.27 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.27
        """
        if isinstance(ce, tuple):
            self._c_data[26] = ce
        else:
            self._c_data[26] = (ce,)

    @property
    def address_of_outside_site(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: OM1.28 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.28
        """
        return self._c_data[27]

    @address_of_outside_site.setter  # set OM1.28
    def address_of_outside_site(self, xad: XAD | tuple[XAD] | None):
        """
        id: OM1.28 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.28
        """
        if isinstance(xad, tuple):
            self._c_data[27] = xad
        else:
            self._c_data[27] = (xad,)

    @property  # get OM1.29
    def phone_number_of_outside_site(self) -> XTN | None:
        """
        id: OM1.29 | len: 250 | use: O | rpt: 1
        ---
        return_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.29
        """
        return self._c_data[28][0]

    @phone_number_of_outside_site.setter  # set OM1.29
    def phone_number_of_outside_site(self, xtn: XTN | None):
        """
        id: OM1.29 | len: 250 | use: O | rpt: 1
        ---
        param_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.29
        """
        self._c_data[28] = (xtn,)

    @property  # get OM1.30
    def confidentiality_code(self) -> ConfidentialityCode | None:
        """
        id: OM1.30 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.30
        """
        return self._c_data[29][0]

    @confidentiality_code.setter  # set OM1.30
    def confidentiality_code(self, confidentiality_code: ConfidentialityCode | None):
        """
        id: OM1.30 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.30
        """
        self._c_data[29] = (confidentiality_code,)

    @property  # get OM1.31
    def observations_required_to_interpret_the_observation(self) -> CE | None:
        """
        id: OM1.31 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.31
        """
        return self._c_data[30][0]

    @observations_required_to_interpret_the_observation.setter  # set OM1.31
    def observations_required_to_interpret_the_observation(self, ce: CE | None):
        """
        id: OM1.31 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.31
        """
        self._c_data[30] = (ce,)

    @property  # get OM1.32
    def interpretation_of_observations(self) -> TX | None:
        """
        id: OM1.32 | len: 65536 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.32
        """
        return self._c_data[31][0]

    @interpretation_of_observations.setter  # set OM1.32
    def interpretation_of_observations(self, tx: TX | None):
        """
        id: OM1.32 | len: 65536 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.32
        """
        self._c_data[31] = (tx,)

    @property  # get OM1.33
    def contraindications_to_observations(self) -> CE | None:
        """
        id: OM1.33 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.33
        """
        return self._c_data[32][0]

    @contraindications_to_observations.setter  # set OM1.33
    def contraindications_to_observations(self, ce: CE | None):
        """
        id: OM1.33 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.33
        """
        self._c_data[32] = (ce,)

    @property
    def reflex_tests_or_observations(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: OM1.34 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.34
        """
        return self._c_data[33]

    @reflex_tests_or_observations.setter  # set OM1.34
    def reflex_tests_or_observations(self, ce: CE | tuple[CE] | None):
        """
        id: OM1.34 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.34
        """
        if isinstance(ce, tuple):
            self._c_data[33] = ce
        else:
            self._c_data[33] = (ce,)

    @property  # get OM1.35
    def rules_that_trigger_reflex_testing(self) -> TX | None:
        """
        id: OM1.35 | len: 80 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.35
        """
        return self._c_data[34][0]

    @rules_that_trigger_reflex_testing.setter  # set OM1.35
    def rules_that_trigger_reflex_testing(self, tx: TX | None):
        """
        id: OM1.35 | len: 80 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.35
        """
        self._c_data[34] = (tx,)

    @property  # get OM1.36
    def fixed_canned_message(self) -> CE | None:
        """
        id: OM1.36 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.36
        """
        return self._c_data[35][0]

    @fixed_canned_message.setter  # set OM1.36
    def fixed_canned_message(self, ce: CE | None):
        """
        id: OM1.36 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.36
        """
        self._c_data[35] = (ce,)

    @property  # get OM1.37
    def patient_preparation(self) -> TX | None:
        """
        id: OM1.37 | len: 200 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.37
        """
        return self._c_data[36][0]

    @patient_preparation.setter  # set OM1.37
    def patient_preparation(self, tx: TX | None):
        """
        id: OM1.37 | len: 200 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.37
        """
        self._c_data[36] = (tx,)

    @property  # get OM1.38
    def procedure_medication(self) -> CE | None:
        """
        id: OM1.38 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.38
        """
        return self._c_data[37][0]

    @procedure_medication.setter  # set OM1.38
    def procedure_medication(self, ce: CE | None):
        """
        id: OM1.38 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.38
        """
        self._c_data[37] = (ce,)

    @property  # get OM1.39
    def factors_that_may_affect_the_observation(self) -> TX | None:
        """
        id: OM1.39 | len: 200 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.39
        """
        return self._c_data[38][0]

    @factors_that_may_affect_the_observation.setter  # set OM1.39
    def factors_that_may_affect_the_observation(self, tx: TX | None):
        """
        id: OM1.39 | len: 200 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.39
        """
        self._c_data[38] = (tx,)

    @property
    def service_or_test_or_observation_performance_schedule(
        self,
    ) -> tuple[ST, ...] | tuple[None]:
        """
        id: OM1.40 | len: 60 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.40
        """
        return self._c_data[39]

    @service_or_test_or_observation_performance_schedule.setter  # set OM1.40
    def service_or_test_or_observation_performance_schedule(
        self, st: ST | tuple[ST] | None
    ):
        """
        id: OM1.40 | len: 60 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.40
        """
        if isinstance(st, tuple):
            self._c_data[39] = st
        else:
            self._c_data[39] = (st,)

    @property  # get OM1.41
    def description_of_test_methods(self) -> TX | None:
        """
        id: OM1.41 | len: 65536 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.41
        """
        return self._c_data[40][0]

    @description_of_test_methods.setter  # set OM1.41
    def description_of_test_methods(self, tx: TX | None):
        """
        id: OM1.41 | len: 65536 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.41
        """
        self._c_data[40] = (tx,)

    @property  # get OM1.42
    def kind_of_quantity_observed(self) -> KindOfQuantity | None:
        """
        id: OM1.42 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.42
        """
        return self._c_data[41][0]

    @kind_of_quantity_observed.setter  # set OM1.42
    def kind_of_quantity_observed(self, kind_of_quantity: KindOfQuantity | None):
        """
        id: OM1.42 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.42
        """
        self._c_data[41] = (kind_of_quantity,)

    @property  # get OM1.43
    def point_versus_interval(self) -> DurationCategories | None:
        """
        id: OM1.43 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.43
        """
        return self._c_data[42][0]

    @point_versus_interval.setter  # set OM1.43
    def point_versus_interval(self, duration_categories: DurationCategories | None):
        """
        id: OM1.43 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.43
        """
        self._c_data[42] = (duration_categories,)

    @property  # get OM1.44
    def challenge_information(self) -> TX | None:
        """
        id: OM1.44 | len: 200 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.44
        """
        return self._c_data[43][0]

    @challenge_information.setter  # set OM1.44
    def challenge_information(self, tx: TX | None):
        """
        id: OM1.44 | len: 200 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.44
        """
        self._c_data[43] = (tx,)

    @property  # get OM1.45
    def relationship_modifier(self) -> RelationshipModifier | None:
        """
        id: OM1.45 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.45
        """
        return self._c_data[44][0]

    @relationship_modifier.setter  # set OM1.45
    def relationship_modifier(self, relationship_modifier: RelationshipModifier | None):
        """
        id: OM1.45 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.45
        """
        self._c_data[44] = (relationship_modifier,)

    @property  # get OM1.46
    def target_anatomic_site_of_test(self) -> CE | None:
        """
        id: OM1.46 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.46
        """
        return self._c_data[45][0]

    @target_anatomic_site_of_test.setter  # set OM1.46
    def target_anatomic_site_of_test(self, ce: CE | None):
        """
        id: OM1.46 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.46
        """
        self._c_data[45] = (ce,)

    @property  # get OM1.47
    def modality_of_imaging_measurement(self) -> Modality | None:
        """
        id: OM1.47 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.47
        """
        return self._c_data[46][0]

    @modality_of_imaging_measurement.setter  # set OM1.47
    def modality_of_imaging_measurement(self, modality: Modality | None):
        """
        id: OM1.47 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM1.47
        """
        self._c_data[46] = (modality,)
