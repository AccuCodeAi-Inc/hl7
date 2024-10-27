from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.CWE import CWE
from ..data_types.PRL import PRL
from ..data_types.TQ import TQ
from ..data_types.NDL import NDL
from ..data_types.XTN import XTN
from ..data_types.MOC import MOC
from ..data_types.IS import IS
from ..data_types.ST import ST
from ..data_types.CQ import CQ
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..data_types.EI import EI
from ..data_types.SPS import SPS
from ..data_types.EIP import EIP
from ..data_types.XCN import XCN
from ..tables.ResultStatus import ResultStatus
from ..tables.ProcedureCode import ProcedureCode
from ..tables.EscortRequired import EscortRequired
from ..tables.ProcedureCodeModifier import ProcedureCodeModifier
from ..tables.SupplementalServiceInformationValues import (
    SupplementalServiceInformationValues,
)
from ..tables.ObservationResultHandling import ObservationResultHandling
from ..tables.SpecimenActionCode import SpecimenActionCode
from ..tables.DiagnosticServiceSectionId import DiagnosticServiceSectionId
from ..tables.TransportationMode import TransportationMode
from ..tables.TransportArranged import TransportArranged
from ..tables.MedicallyNecessaryDuplicateProcedureReason import (
    MedicallyNecessaryDuplicateProcedureReason,
)


"""
Observation Request - OBR
HL7 Version: 2.5.1

-----BEGIN SEGMENT::OBR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OBR,
    ID, TS, CWE, PRL, TQ, NDL, XTN, MOC, IS, ST, CQ, SI, CE, NM, EI, SPS, EIP, XCN
)

obr = OBR(  #  - The Observation Request (OBR) segment is used to transmit information specific to an order for a diagnostic study or observation, physical exam, or assessment
    set_id_obr=None,  # SI(...) 
    placer_order_number=None,  # EI(...) 
    filler_order_number=None,  # EI(...) 
    universal_service_identifier=ce,  # CE(...)  # Required.
    priority_obr=None,  # ID(...) 
    requested_date_or_time=None,  # TS(...) 
    observation_date_or_time=None,  # TS(...) 
    observation_end_date_or_time=None,  # TS(...) 
    collection_volume=None,  # CQ(...) 
    collector_identifier=None,  # XCN(...) 
    specimen_action_code=None,  # ID(...) 
    danger_code=None,  # CE(...) 
    relevant_clinical_information=None,  # ST(...) 
    specimen_received_date_or_time=None,  # TS(...) 
    specimen_source=None,  # SPS(...) 
    ordering_provider=None,  # XCN(...) 
    order_callback_phone_number=None,  # XTN(...) 
    placer_field_1=None,  # ST(...) 
    placer_field_2=None,  # ST(...) 
    filler_field_1=None,  # ST(...) 
    filler_field_2=None,  # ST(...) 
    results_rpt_or_status_chng_date_or_time=None,  # TS(...) 
    charge_to_practice=None,  # MOC(...) 
    diagnostic_serv_sect_id=None,  # ID(...) 
    result_status=None,  # ID(...) 
    parent_result=None,  # PRL(...) 
    quantity_or_timing=None,  # TQ(...) 
    result_copies_to=None,  # XCN(...) 
    parent=None,  # EIP(...) 
    transportation_mode=None,  # ID(...) 
    reason_for_study=None,  # CE(...) 
    principal_result_interpreter=None,  # NDL(...) 
    assistant_result_interpreter=None,  # NDL(...) 
    technician=None,  # NDL(...) 
    transcriptionist=None,  # NDL(...) 
    scheduled_date_or_time=None,  # TS(...) 
    number_of_sample_containers=None,  # NM(...) 
    transport_logistics_of_collected_sample=None,  # CE(...) 
    collectors_comment=None,  # CE(...) 
    transport_arrangement_responsibility=None,  # CE(...) 
    transport_arranged=None,  # ID(...) 
    escort_required=None,  # ID(...) 
    planned_patient_transport_comment=None,  # CE(...) 
    procedure_code=None,  # CE(...) 
    procedure_code_modifier=None,  # CE(...) 
    placer_supplemental_service_information=None,  # CE(...) 
    filler_supplemental_service_information=None,  # CE(...) 
    medically_necessary_duplicate_procedure_reason=None,  # CWE(...) 
    result_handling=None,  # IS(...) 
    parent_universal_service_identifier=None,  # CWE(...) 
)

-----END SEGMENT::OBR TEMPLATE-----
"""


class OBR(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """OBR"""
    _hl7_name = """Observation Request"""
    _hl7_description = """The Observation Request (OBR) segment is used to transmit information specific to an order for a diagnostic study or observation, physical exam, or assessment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR"
    _c_length = (4, 22, 22, 250, 2, 26, 26, 26, 20, 250, 1, 250, 300, 26, 300, 250, 250, 60, 60, 60, 60, 26, 40, 10, 1, 400, 200, 250, 200, 20, 250, 200, 200, 200, 200, 26, 4, 250, 250, 250, 30, 1, 250, 250, 250, 250, 250, 250, 2, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 65535, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 65535, 1, 1, 65535, 1, 65535, 65535, 65535, 1, 1, 65535, 65535, 1, 1, 1, 65535, 1, 65535, 65535, 65535, 1, 1, 1,)
    _c_usage = ("O", "C", "C", "R", "B", "B", "C", "O", "O", "O", "O", "O", "O", "B", "B", "O", "O", "O", "O", "O", "O", "C", "O", "O", "C", "O", "B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "C", "O", "O",)
    _c_components = (SI, EI, EI, CE, ID, TS, TS, TS, CQ, XCN, ID, CE, ST, TS, SPS, XCN, XTN, ST, ST, ST, ST, TS, MOC, ID, ID, PRL, TQ, XCN, EIP, ID, CE, NDL, NDL, NDL, NDL, TS, NM, CE, CE, CE, ID, ID, CE, CE, CE, CE, CE, CWE, IS, CWE,)
    _c_aliases = ("OBR.1", "OBR.2", "OBR.3", "OBR.4", "OBR.5", "OBR.6", "OBR.7", "OBR.8", "OBR.9", "OBR.10", "OBR.11", "OBR.12", "OBR.13", "OBR.14", "OBR.15", "OBR.16", "OBR.17", "OBR.18", "OBR.19", "OBR.20", "OBR.21", "OBR.22", "OBR.23", "OBR.24", "OBR.25", "OBR.26", "OBR.27", "OBR.28", "OBR.29", "OBR.30", "OBR.31", "OBR.32", "OBR.33", "OBR.34", "OBR.35", "OBR.36", "OBR.37", "OBR.38", "OBR.39", "OBR.40", "OBR.41", "OBR.42", "OBR.43", "OBR.44", "OBR.45", "OBR.46", "OBR.47", "OBR.48", "OBR.49", "OBR.50",)
    _c_names = ("Set ID - OBR", "Placer Order Number", "Filler Order Number", "Universal Service Identifier", "Priority - OBR", "Requested Date/Time", "Observation Date/Time", "Observation End Date/Time", "Collection Volume", "Collector Identifier", "Specimen Action Code", "Danger Code", "Relevant Clinical Information", "Specimen Received Date/Time", "Specimen Source", "Ordering Provider", "Order Callback Phone Number", "Placer Field 1", "Placer Field 2", "Filler Field 1", "Filler Field 2", "Results Rpt/Status Chng - Date/Time", "Charge to Practice", "Diagnostic Serv Sect ID", "Result Status", "Parent Result", "Quantity/Timing", "Result Copies To", "Parent", "Transportation Mode", "Reason for Study", "Principal Result Interpreter", "Assistant Result Interpreter", "Technician", "Transcriptionist", "Scheduled Date/Time", "Number of Sample Containers", "Transport Logistics of Collected Sample", "Collector's Comment", "Transport Arrangement Responsibility", "Transport Arranged", "Escort Required", "Planned Patient Transport Comment", "Procedure Code", "Procedure Code Modifier", "Placer Supplemental Service Information", "Filler Supplemental Service Information", "Medically Necessary Duplicate Procedure Reason.", "Result Handling", "Parent Universal Service Identifier",)
    _c_attrs = ("set_id_obr", "placer_order_number", "filler_order_number", "universal_service_identifier", "priority_obr", "requested_date_or_time", "observation_date_or_time", "observation_end_date_or_time", "collection_volume", "collector_identifier", "specimen_action_code", "danger_code", "relevant_clinical_information", "specimen_received_date_or_time", "specimen_source", "ordering_provider", "order_callback_phone_number", "placer_field_1", "placer_field_2", "filler_field_1", "filler_field_2", "results_rpt_or_status_chng_date_or_time", "charge_to_practice", "diagnostic_serv_sect_id", "result_status", "parent_result", "quantity_or_timing", "result_copies_to", "parent", "transportation_mode", "reason_for_study", "principal_result_interpreter", "assistant_result_interpreter", "technician", "transcriptionist", "scheduled_date_or_time", "number_of_sample_containers", "transport_logistics_of_collected_sample", "collectors_comment", "transport_arrangement_responsibility", "transport_arranged", "escort_required", "planned_patient_transport_comment", "procedure_code", "procedure_code_modifier", "placer_supplemental_service_information", "filler_supplemental_service_information", "medically_necessary_duplicate_procedure_reason", "result_handling", "parent_universal_service_identifier",)
    # fmt: on

    def __init__(
        self,
        universal_service_identifier: CE,  # OBR.4
        set_id_obr: SI | None = None,  # OBR.1
        placer_order_number: EI | None = None,  # OBR.2
        filler_order_number: EI | None = None,  # OBR.3
        priority_obr: ID | None = None,  # OBR.5
        requested_date_or_time: TS | None = None,  # OBR.6
        observation_date_or_time: TS | None = None,  # OBR.7
        observation_end_date_or_time: TS | None = None,  # OBR.8
        collection_volume: CQ | None = None,  # OBR.9
        collector_identifier: XCN | None = None,  # OBR.10
        specimen_action_code: SpecimenActionCode | ID | None = None,  # OBR.11
        danger_code: CE | None = None,  # OBR.12
        relevant_clinical_information: ST | None = None,  # OBR.13
        specimen_received_date_or_time: TS | None = None,  # OBR.14
        specimen_source: SPS | None = None,  # OBR.15
        ordering_provider: XCN | None = None,  # OBR.16
        order_callback_phone_number: XTN | None = None,  # OBR.17
        placer_field_1: ST | None = None,  # OBR.18
        placer_field_2: ST | None = None,  # OBR.19
        filler_field_1: ST | None = None,  # OBR.20
        filler_field_2: ST | None = None,  # OBR.21
        results_rpt_or_status_chng_date_or_time: TS | None = None,  # OBR.22
        charge_to_practice: MOC | None = None,  # OBR.23
        diagnostic_serv_sect_id: DiagnosticServiceSectionId
        | ID
        | None = None,  # OBR.24
        result_status: ResultStatus | ID | None = None,  # OBR.25
        parent_result: PRL | None = None,  # OBR.26
        quantity_or_timing: TQ | None = None,  # OBR.27
        result_copies_to: XCN | None = None,  # OBR.28
        parent: EIP | None = None,  # OBR.29
        transportation_mode: TransportationMode | ID | None = None,  # OBR.30
        reason_for_study: CE | None = None,  # OBR.31
        principal_result_interpreter: NDL | None = None,  # OBR.32
        assistant_result_interpreter: NDL | None = None,  # OBR.33
        technician: NDL | None = None,  # OBR.34
        transcriptionist: NDL | None = None,  # OBR.35
        scheduled_date_or_time: TS | None = None,  # OBR.36
        number_of_sample_containers: NM | None = None,  # OBR.37
        transport_logistics_of_collected_sample: CE | None = None,  # OBR.38
        collectors_comment: CE | None = None,  # OBR.39
        transport_arrangement_responsibility: CE | None = None,  # OBR.40
        transport_arranged: TransportArranged | ID | None = None,  # OBR.41
        escort_required: EscortRequired | ID | None = None,  # OBR.42
        planned_patient_transport_comment: CE | None = None,  # OBR.43
        procedure_code: ProcedureCode | CE | None = None,  # OBR.44
        procedure_code_modifier: ProcedureCodeModifier | CE | None = None,  # OBR.45
        placer_supplemental_service_information: SupplementalServiceInformationValues
        | CE
        | None = None,  # OBR.46
        filler_supplemental_service_information: SupplementalServiceInformationValues
        | CE
        | None = None,  # OBR.47
        medically_necessary_duplicate_procedure_reason: MedicallyNecessaryDuplicateProcedureReason
        | CWE
        | None = None,  # OBR.48
        result_handling: ObservationResultHandling | IS | None = None,  # OBR.49
        parent_universal_service_identifier: CWE | None = None,  # OBR.50
    ):
        """
        Observation Request - `OBR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR>`_
        The Observation Request (OBR) segment is used to transmit information specific to an order for a diagnostic study or observation, physical exam, or assessment.

        :param set_id_obr: Sequence ID (id: OBR.1 | len: 4 | use: O | rpt: 1)
        :param placer_order_number: Entity Identifier (id: OBR.2 | len: 22 | use: C | rpt: 1)
        :param filler_order_number: Entity Identifier (id: OBR.3 | len: 22 | use: C | rpt: 1)
        :param universal_service_identifier: Coded Element (id: OBR.4 | len: 250 | use: R | rpt: 1)
        :param priority_obr: Coded values for HL7 tables (id: OBR.5 | len: 2 | use: B | rpt: 1)
        :param requested_date_or_time: Time Stamp (id: OBR.6 | len: 26 | use: B | rpt: 1)
        :param observation_date_or_time: Time Stamp (id: OBR.7 | len: 26 | use: C | rpt: 1)
        :param observation_end_date_or_time: Time Stamp (id: OBR.8 | len: 26 | use: O | rpt: 1)
        :param collection_volume: Composite Quantity with Units (id: OBR.9 | len: 20 | use: O | rpt: 1)
        :param collector_identifier: Extended Composite ID Number and Name for Persons (id: OBR.10 | len: 250 | use: O | rpt: *)
        :param specimen_action_code: Coded values for HL7 tables (id: OBR.11 | len: 1 | use: O | rpt: 1)
        :param danger_code: Coded Element (id: OBR.12 | len: 250 | use: O | rpt: 1)
        :param relevant_clinical_information: String Data (id: OBR.13 | len: 300 | use: O | rpt: 1)
        :param specimen_received_date_or_time: Time Stamp (id: OBR.14 | len: 26 | use: B | rpt: 1)
        :param specimen_source: Specimen Source (id: OBR.15 | len: 300 | use: B | rpt: 1)
        :param ordering_provider: Extended Composite ID Number and Name for Persons (id: OBR.16 | len: 250 | use: O | rpt: *)
        :param order_callback_phone_number: Extended Telecommunication Number (id: OBR.17 | len: 250 | use: O | rpt: 2)
        :param placer_field_1: String Data (id: OBR.18 | len: 60 | use: O | rpt: 1)
        :param placer_field_2: String Data (id: OBR.19 | len: 60 | use: O | rpt: 1)
        :param filler_field_1: String Data (id: OBR.20 | len: 60 | use: O | rpt: 1)
        :param filler_field_2: String Data (id: OBR.21 | len: 60 | use: O | rpt: 1)
        :param results_rpt_or_status_chng_date_or_time: Time Stamp (id: OBR.22 | len: 26 | use: C | rpt: 1)
        :param charge_to_practice: Money and Code (id: OBR.23 | len: 40 | use: O | rpt: 1)
        :param diagnostic_serv_sect_id: Coded values for HL7 tables (id: OBR.24 | len: 10 | use: O | rpt: 1)
        :param result_status: Coded values for HL7 tables (id: OBR.25 | len: 1 | use: C | rpt: 1)
        :param parent_result: Parent Result Link (id: OBR.26 | len: 400 | use: O | rpt: 1)
        :param quantity_or_timing: Timing Quantity (id: OBR.27 | len: 200 | use: B | rpt: *)
        :param result_copies_to: Extended Composite ID Number and Name for Persons (id: OBR.28 | len: 250 | use: O | rpt: *)
        :param parent: Entity Identifier Pair (id: OBR.29 | len: 200 | use: O | rpt: 1)
        :param transportation_mode: Coded values for HL7 tables (id: OBR.30 | len: 20 | use: O | rpt: 1)
        :param reason_for_study: Coded Element (id: OBR.31 | len: 250 | use: O | rpt: *)
        :param principal_result_interpreter: Name with Date and Location (id: OBR.32 | len: 200 | use: O | rpt: 1)
        :param assistant_result_interpreter: Name with Date and Location (id: OBR.33 | len: 200 | use: O | rpt: *)
        :param technician: Name with Date and Location (id: OBR.34 | len: 200 | use: O | rpt: *)
        :param transcriptionist: Name with Date and Location (id: OBR.35 | len: 200 | use: O | rpt: *)
        :param scheduled_date_or_time: Time Stamp (id: OBR.36 | len: 26 | use: O | rpt: 1)
        :param number_of_sample_containers: Numeric (id: OBR.37 | len: 4 | use: O | rpt: 1)
        :param transport_logistics_of_collected_sample: Coded Element (id: OBR.38 | len: 250 | use: O | rpt: *)
        :param collectors_comment: Coded Element (id: OBR.39 | len: 250 | use: O | rpt: *)
        :param transport_arrangement_responsibility: Coded Element (id: OBR.40 | len: 250 | use: O | rpt: 1)
        :param transport_arranged: Coded values for HL7 tables (id: OBR.41 | len: 30 | use: O | rpt: 1)
        :param escort_required: Coded values for HL7 tables (id: OBR.42 | len: 1 | use: O | rpt: 1)
        :param planned_patient_transport_comment: Coded Element (id: OBR.43 | len: 250 | use: O | rpt: *)
        :param procedure_code: Coded Element (id: OBR.44 | len: 250 | use: O | rpt: 1)
        :param procedure_code_modifier: Coded Element (id: OBR.45 | len: 250 | use: O | rpt: *)
        :param placer_supplemental_service_information: Coded Element (id: OBR.46 | len: 250 | use: O | rpt: *)
        :param filler_supplemental_service_information: Coded Element (id: OBR.47 | len: 250 | use: O | rpt: *)
        :param medically_necessary_duplicate_procedure_reason: Coded with Exceptions (id: OBR.48 | len: 250 | use: C | rpt: 1)
        :param result_handling: Coded value for user-defined tables (id: OBR.49 | len: 2 | use: O | rpt: 1)
        :param parent_universal_service_identifier: Coded with Exceptions (id: OBR.50 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 50
        self.set_id_obr = set_id_obr
        self.placer_order_number = placer_order_number
        self.filler_order_number = filler_order_number
        self.universal_service_identifier = universal_service_identifier
        self.priority_obr = priority_obr
        self.requested_date_or_time = requested_date_or_time
        self.observation_date_or_time = observation_date_or_time
        self.observation_end_date_or_time = observation_end_date_or_time
        self.collection_volume = collection_volume
        self.collector_identifier = collector_identifier
        self.specimen_action_code = specimen_action_code
        self.danger_code = danger_code
        self.relevant_clinical_information = relevant_clinical_information
        self.specimen_received_date_or_time = specimen_received_date_or_time
        self.specimen_source = specimen_source
        self.ordering_provider = ordering_provider
        self.order_callback_phone_number = order_callback_phone_number
        self.placer_field_1 = placer_field_1
        self.placer_field_2 = placer_field_2
        self.filler_field_1 = filler_field_1
        self.filler_field_2 = filler_field_2
        self.results_rpt_or_status_chng_date_or_time = (
            results_rpt_or_status_chng_date_or_time
        )
        self.charge_to_practice = charge_to_practice
        self.diagnostic_serv_sect_id = diagnostic_serv_sect_id
        self.result_status = result_status
        self.parent_result = parent_result
        self.quantity_or_timing = quantity_or_timing
        self.result_copies_to = result_copies_to
        self.parent = parent
        self.transportation_mode = transportation_mode
        self.reason_for_study = reason_for_study
        self.principal_result_interpreter = principal_result_interpreter
        self.assistant_result_interpreter = assistant_result_interpreter
        self.technician = technician
        self.transcriptionist = transcriptionist
        self.scheduled_date_or_time = scheduled_date_or_time
        self.number_of_sample_containers = number_of_sample_containers
        self.transport_logistics_of_collected_sample = (
            transport_logistics_of_collected_sample
        )
        self.collectors_comment = collectors_comment
        self.transport_arrangement_responsibility = transport_arrangement_responsibility
        self.transport_arranged = transport_arranged
        self.escort_required = escort_required
        self.planned_patient_transport_comment = planned_patient_transport_comment
        self.procedure_code = procedure_code
        self.procedure_code_modifier = procedure_code_modifier
        self.placer_supplemental_service_information = (
            placer_supplemental_service_information
        )
        self.filler_supplemental_service_information = (
            filler_supplemental_service_information
        )
        self.medically_necessary_duplicate_procedure_reason = (
            medically_necessary_duplicate_procedure_reason
        )
        self.result_handling = result_handling
        self.parent_universal_service_identifier = parent_universal_service_identifier

    @property  # get OBR.1
    def set_id_obr(self) -> SI | None:
        """
        id: OBR.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.1
        """
        return self._c_data[0][0]

    @set_id_obr.setter  # set OBR.1
    def set_id_obr(self, si: SI | None):
        """
        id: OBR.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.1
        """
        self._c_data[0] = (si,)

    @property  # get OBR.2
    def placer_order_number(self) -> EI | None:
        """
        id: OBR.2 | len: 22 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.2
        """
        return self._c_data[1][0]

    @placer_order_number.setter  # set OBR.2
    def placer_order_number(self, ei: EI | None):
        """
        id: OBR.2 | len: 22 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.2
        """
        self._c_data[1] = (ei,)

    @property  # get OBR.3
    def filler_order_number(self) -> EI | None:
        """
        id: OBR.3 | len: 22 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.3
        """
        return self._c_data[2][0]

    @filler_order_number.setter  # set OBR.3
    def filler_order_number(self, ei: EI | None):
        """
        id: OBR.3 | len: 22 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.3
        """
        self._c_data[2] = (ei,)

    @property  # get OBR.4
    def universal_service_identifier(self) -> CE:
        """
        id: OBR.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.4
        """
        return self._c_data[3][0]

    @universal_service_identifier.setter  # set OBR.4
    def universal_service_identifier(self, ce: CE):
        """
        id: OBR.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.4
        """
        self._c_data[3] = (ce,)

    @property  # get OBR.5
    def priority_obr(self) -> ID | None:
        """
        id: OBR.5 | len: 2 | use: B | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.5
        """
        return self._c_data[4][0]

    @priority_obr.setter  # set OBR.5
    def priority_obr(self, id: ID | None):
        """
        id: OBR.5 | len: 2 | use: B | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.5
        """
        self._c_data[4] = (id,)

    @property  # get OBR.6
    def requested_date_or_time(self) -> TS | None:
        """
        id: OBR.6 | len: 26 | use: B | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.6
        """
        return self._c_data[5][0]

    @requested_date_or_time.setter  # set OBR.6
    def requested_date_or_time(self, ts: TS | None):
        """
        id: OBR.6 | len: 26 | use: B | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.6
        """
        self._c_data[5] = (ts,)

    @property  # get OBR.7
    def observation_date_or_time(self) -> TS | None:
        """
        id: OBR.7 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.7
        """
        return self._c_data[6][0]

    @observation_date_or_time.setter  # set OBR.7
    def observation_date_or_time(self, ts: TS | None):
        """
        id: OBR.7 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.7
        """
        self._c_data[6] = (ts,)

    @property  # get OBR.8
    def observation_end_date_or_time(self) -> TS | None:
        """
        id: OBR.8 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.8
        """
        return self._c_data[7][0]

    @observation_end_date_or_time.setter  # set OBR.8
    def observation_end_date_or_time(self, ts: TS | None):
        """
        id: OBR.8 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.8
        """
        self._c_data[7] = (ts,)

    @property  # get OBR.9
    def collection_volume(self) -> CQ | None:
        """
        id: OBR.9 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.9
        """
        return self._c_data[8][0]

    @collection_volume.setter  # set OBR.9
    def collection_volume(self, cq: CQ | None):
        """
        id: OBR.9 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.9
        """
        self._c_data[8] = (cq,)

    @property
    def collector_identifier(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: OBR.10 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.10
        """
        return self._c_data[9]

    @collector_identifier.setter  # set OBR.10
    def collector_identifier(self, xcn: XCN | tuple[XCN] | None):
        """
        id: OBR.10 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.10
        """
        if isinstance(xcn, tuple):
            self._c_data[9] = xcn
        else:
            self._c_data[9] = (xcn,)

    @property  # get OBR.11
    def specimen_action_code(self) -> SpecimenActionCode | None:
        """
        id: OBR.11 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.11
        """
        return self._c_data[10][0]

    @specimen_action_code.setter  # set OBR.11
    def specimen_action_code(self, specimen_action_code: SpecimenActionCode | None):
        """
        id: OBR.11 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.11
        """
        self._c_data[10] = (specimen_action_code,)

    @property  # get OBR.12
    def danger_code(self) -> CE | None:
        """
        id: OBR.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.12
        """
        return self._c_data[11][0]

    @danger_code.setter  # set OBR.12
    def danger_code(self, ce: CE | None):
        """
        id: OBR.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.12
        """
        self._c_data[11] = (ce,)

    @property  # get OBR.13
    def relevant_clinical_information(self) -> ST | None:
        """
        id: OBR.13 | len: 300 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.13
        """
        return self._c_data[12][0]

    @relevant_clinical_information.setter  # set OBR.13
    def relevant_clinical_information(self, st: ST | None):
        """
        id: OBR.13 | len: 300 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.13
        """
        self._c_data[12] = (st,)

    @property  # get OBR.14
    def specimen_received_date_or_time(self) -> TS | None:
        """
        id: OBR.14 | len: 26 | use: B | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.14
        """
        return self._c_data[13][0]

    @specimen_received_date_or_time.setter  # set OBR.14
    def specimen_received_date_or_time(self, ts: TS | None):
        """
        id: OBR.14 | len: 26 | use: B | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.14
        """
        self._c_data[13] = (ts,)

    @property  # get OBR.15
    def specimen_source(self) -> SPS | None:
        """
        id: OBR.15 | len: 300 | use: B | rpt: 1
        ---
        return_type: SPS: Specimen Source
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.15
        """
        return self._c_data[14][0]

    @specimen_source.setter  # set OBR.15
    def specimen_source(self, sps: SPS | None):
        """
        id: OBR.15 | len: 300 | use: B | rpt: 1
        ---
        param_type: SPS: Specimen Source
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.15
        """
        self._c_data[14] = (sps,)

    @property
    def ordering_provider(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: OBR.16 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.16
        """
        return self._c_data[15]

    @ordering_provider.setter  # set OBR.16
    def ordering_provider(self, xcn: XCN | tuple[XCN] | None):
        """
        id: OBR.16 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.16
        """
        if isinstance(xcn, tuple):
            self._c_data[15] = xcn
        else:
            self._c_data[15] = (xcn,)

    @property
    def order_callback_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: OBR.17 | len: 250 | use: O | rpt: 2
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.17
        """
        return self._c_data[16]

    @order_callback_phone_number.setter  # set OBR.17
    def order_callback_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: OBR.17 | len: 250 | use: O | rpt: 2
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.17
        """
        if isinstance(xtn, tuple):
            self._c_data[16] = xtn
        else:
            self._c_data[16] = (xtn,)

    @property  # get OBR.18
    def placer_field_1(self) -> ST | None:
        """
        id: OBR.18 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.18
        """
        return self._c_data[17][0]

    @placer_field_1.setter  # set OBR.18
    def placer_field_1(self, st: ST | None):
        """
        id: OBR.18 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.18
        """
        self._c_data[17] = (st,)

    @property  # get OBR.19
    def placer_field_2(self) -> ST | None:
        """
        id: OBR.19 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.19
        """
        return self._c_data[18][0]

    @placer_field_2.setter  # set OBR.19
    def placer_field_2(self, st: ST | None):
        """
        id: OBR.19 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.19
        """
        self._c_data[18] = (st,)

    @property  # get OBR.20
    def filler_field_1(self) -> ST | None:
        """
        id: OBR.20 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.20
        """
        return self._c_data[19][0]

    @filler_field_1.setter  # set OBR.20
    def filler_field_1(self, st: ST | None):
        """
        id: OBR.20 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.20
        """
        self._c_data[19] = (st,)

    @property  # get OBR.21
    def filler_field_2(self) -> ST | None:
        """
        id: OBR.21 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.21
        """
        return self._c_data[20][0]

    @filler_field_2.setter  # set OBR.21
    def filler_field_2(self, st: ST | None):
        """
        id: OBR.21 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.21
        """
        self._c_data[20] = (st,)

    @property  # get OBR.22
    def results_rpt_or_status_chng_date_or_time(self) -> TS | None:
        """
        id: OBR.22 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.22
        """
        return self._c_data[21][0]

    @results_rpt_or_status_chng_date_or_time.setter  # set OBR.22
    def results_rpt_or_status_chng_date_or_time(self, ts: TS | None):
        """
        id: OBR.22 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.22
        """
        self._c_data[21] = (ts,)

    @property  # get OBR.23
    def charge_to_practice(self) -> MOC | None:
        """
        id: OBR.23 | len: 40 | use: O | rpt: 1
        ---
        return_type: MOC: Money and Code
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.23
        """
        return self._c_data[22][0]

    @charge_to_practice.setter  # set OBR.23
    def charge_to_practice(self, moc: MOC | None):
        """
        id: OBR.23 | len: 40 | use: O | rpt: 1
        ---
        param_type: MOC: Money and Code
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.23
        """
        self._c_data[22] = (moc,)

    @property  # get OBR.24
    def diagnostic_serv_sect_id(self) -> DiagnosticServiceSectionId | None:
        """
        id: OBR.24 | len: 10 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.24
        """
        return self._c_data[23][0]

    @diagnostic_serv_sect_id.setter  # set OBR.24
    def diagnostic_serv_sect_id(
        self, diagnostic_service_section_id: DiagnosticServiceSectionId | None
    ):
        """
        id: OBR.24 | len: 10 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.24
        """
        self._c_data[23] = (diagnostic_service_section_id,)

    @property  # get OBR.25
    def result_status(self) -> ResultStatus | None:
        """
        id: OBR.25 | len: 1 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.25
        """
        return self._c_data[24][0]

    @result_status.setter  # set OBR.25
    def result_status(self, result_status: ResultStatus | None):
        """
        id: OBR.25 | len: 1 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.25
        """
        self._c_data[24] = (result_status,)

    @property  # get OBR.26
    def parent_result(self) -> PRL | None:
        """
        id: OBR.26 | len: 400 | use: O | rpt: 1
        ---
        return_type: PRL: Parent Result Link
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.26
        """
        return self._c_data[25][0]

    @parent_result.setter  # set OBR.26
    def parent_result(self, prl: PRL | None):
        """
        id: OBR.26 | len: 400 | use: O | rpt: 1
        ---
        param_type: PRL: Parent Result Link
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.26
        """
        self._c_data[25] = (prl,)

    @property
    def quantity_or_timing(self) -> tuple[TQ, ...] | tuple[None]:
        """
        id: OBR.27 | len: 200 | use: B | rpt: *
        ---
        return_type: tuple[TQ, ...]: (Timing Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.27
        """
        return self._c_data[26]

    @quantity_or_timing.setter  # set OBR.27
    def quantity_or_timing(self, tq: TQ | tuple[TQ] | None):
        """
        id: OBR.27 | len: 200 | use: B | rpt: *
        ---
        param_type: TQ | tuple[TQ, ...]: (Timing Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.27
        """
        if isinstance(tq, tuple):
            self._c_data[26] = tq
        else:
            self._c_data[26] = (tq,)

    @property
    def result_copies_to(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: OBR.28 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.28
        """
        return self._c_data[27]

    @result_copies_to.setter  # set OBR.28
    def result_copies_to(self, xcn: XCN | tuple[XCN] | None):
        """
        id: OBR.28 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.28
        """
        if isinstance(xcn, tuple):
            self._c_data[27] = xcn
        else:
            self._c_data[27] = (xcn,)

    @property  # get OBR.29
    def parent(self) -> EIP | None:
        """
        id: OBR.29 | len: 200 | use: O | rpt: 1
        ---
        return_type: EIP: Entity Identifier Pair
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.29
        """
        return self._c_data[28][0]

    @parent.setter  # set OBR.29
    def parent(self, eip: EIP | None):
        """
        id: OBR.29 | len: 200 | use: O | rpt: 1
        ---
        param_type: EIP: Entity Identifier Pair
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.29
        """
        self._c_data[28] = (eip,)

    @property  # get OBR.30
    def transportation_mode(self) -> TransportationMode | None:
        """
        id: OBR.30 | len: 20 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.30
        """
        return self._c_data[29][0]

    @transportation_mode.setter  # set OBR.30
    def transportation_mode(self, transportation_mode: TransportationMode | None):
        """
        id: OBR.30 | len: 20 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.30
        """
        self._c_data[29] = (transportation_mode,)

    @property
    def reason_for_study(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: OBR.31 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.31
        """
        return self._c_data[30]

    @reason_for_study.setter  # set OBR.31
    def reason_for_study(self, ce: CE | tuple[CE] | None):
        """
        id: OBR.31 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.31
        """
        if isinstance(ce, tuple):
            self._c_data[30] = ce
        else:
            self._c_data[30] = (ce,)

    @property  # get OBR.32
    def principal_result_interpreter(self) -> NDL | None:
        """
        id: OBR.32 | len: 200 | use: O | rpt: 1
        ---
        return_type: NDL: Name with Date and Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.32
        """
        return self._c_data[31][0]

    @principal_result_interpreter.setter  # set OBR.32
    def principal_result_interpreter(self, ndl: NDL | None):
        """
        id: OBR.32 | len: 200 | use: O | rpt: 1
        ---
        param_type: NDL: Name with Date and Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.32
        """
        self._c_data[31] = (ndl,)

    @property
    def assistant_result_interpreter(self) -> tuple[NDL, ...] | tuple[None]:
        """
        id: OBR.33 | len: 200 | use: O | rpt: *
        ---
        return_type: tuple[NDL, ...]: (Name with Date and Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.33
        """
        return self._c_data[32]

    @assistant_result_interpreter.setter  # set OBR.33
    def assistant_result_interpreter(self, ndl: NDL | tuple[NDL] | None):
        """
        id: OBR.33 | len: 200 | use: O | rpt: *
        ---
        param_type: NDL | tuple[NDL, ...]: (Name with Date and Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.33
        """
        if isinstance(ndl, tuple):
            self._c_data[32] = ndl
        else:
            self._c_data[32] = (ndl,)

    @property
    def technician(self) -> tuple[NDL, ...] | tuple[None]:
        """
        id: OBR.34 | len: 200 | use: O | rpt: *
        ---
        return_type: tuple[NDL, ...]: (Name with Date and Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.34
        """
        return self._c_data[33]

    @technician.setter  # set OBR.34
    def technician(self, ndl: NDL | tuple[NDL] | None):
        """
        id: OBR.34 | len: 200 | use: O | rpt: *
        ---
        param_type: NDL | tuple[NDL, ...]: (Name with Date and Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.34
        """
        if isinstance(ndl, tuple):
            self._c_data[33] = ndl
        else:
            self._c_data[33] = (ndl,)

    @property
    def transcriptionist(self) -> tuple[NDL, ...] | tuple[None]:
        """
        id: OBR.35 | len: 200 | use: O | rpt: *
        ---
        return_type: tuple[NDL, ...]: (Name with Date and Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.35
        """
        return self._c_data[34]

    @transcriptionist.setter  # set OBR.35
    def transcriptionist(self, ndl: NDL | tuple[NDL] | None):
        """
        id: OBR.35 | len: 200 | use: O | rpt: *
        ---
        param_type: NDL | tuple[NDL, ...]: (Name with Date and Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.35
        """
        if isinstance(ndl, tuple):
            self._c_data[34] = ndl
        else:
            self._c_data[34] = (ndl,)

    @property  # get OBR.36
    def scheduled_date_or_time(self) -> TS | None:
        """
        id: OBR.36 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.36
        """
        return self._c_data[35][0]

    @scheduled_date_or_time.setter  # set OBR.36
    def scheduled_date_or_time(self, ts: TS | None):
        """
        id: OBR.36 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.36
        """
        self._c_data[35] = (ts,)

    @property  # get OBR.37
    def number_of_sample_containers(self) -> NM | None:
        """
        id: OBR.37 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.37
        """
        return self._c_data[36][0]

    @number_of_sample_containers.setter  # set OBR.37
    def number_of_sample_containers(self, nm: NM | None):
        """
        id: OBR.37 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.37
        """
        self._c_data[36] = (nm,)

    @property
    def transport_logistics_of_collected_sample(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: OBR.38 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.38
        """
        return self._c_data[37]

    @transport_logistics_of_collected_sample.setter  # set OBR.38
    def transport_logistics_of_collected_sample(self, ce: CE | tuple[CE] | None):
        """
        id: OBR.38 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.38
        """
        if isinstance(ce, tuple):
            self._c_data[37] = ce
        else:
            self._c_data[37] = (ce,)

    @property
    def collectors_comment(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: OBR.39 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.39
        """
        return self._c_data[38]

    @collectors_comment.setter  # set OBR.39
    def collectors_comment(self, ce: CE | tuple[CE] | None):
        """
        id: OBR.39 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.39
        """
        if isinstance(ce, tuple):
            self._c_data[38] = ce
        else:
            self._c_data[38] = (ce,)

    @property  # get OBR.40
    def transport_arrangement_responsibility(self) -> CE | None:
        """
        id: OBR.40 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.40
        """
        return self._c_data[39][0]

    @transport_arrangement_responsibility.setter  # set OBR.40
    def transport_arrangement_responsibility(self, ce: CE | None):
        """
        id: OBR.40 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.40
        """
        self._c_data[39] = (ce,)

    @property  # get OBR.41
    def transport_arranged(self) -> TransportArranged | None:
        """
        id: OBR.41 | len: 30 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.41
        """
        return self._c_data[40][0]

    @transport_arranged.setter  # set OBR.41
    def transport_arranged(self, transport_arranged: TransportArranged | None):
        """
        id: OBR.41 | len: 30 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.41
        """
        self._c_data[40] = (transport_arranged,)

    @property  # get OBR.42
    def escort_required(self) -> EscortRequired | None:
        """
        id: OBR.42 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.42
        """
        return self._c_data[41][0]

    @escort_required.setter  # set OBR.42
    def escort_required(self, escort_required: EscortRequired | None):
        """
        id: OBR.42 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.42
        """
        self._c_data[41] = (escort_required,)

    @property
    def planned_patient_transport_comment(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: OBR.43 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.43
        """
        return self._c_data[42]

    @planned_patient_transport_comment.setter  # set OBR.43
    def planned_patient_transport_comment(self, ce: CE | tuple[CE] | None):
        """
        id: OBR.43 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.43
        """
        if isinstance(ce, tuple):
            self._c_data[42] = ce
        else:
            self._c_data[42] = (ce,)

    @property  # get OBR.44
    def procedure_code(self) -> ProcedureCode | None:
        """
        id: OBR.44 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.44
        """
        return self._c_data[43][0]

    @procedure_code.setter  # set OBR.44
    def procedure_code(self, procedure_code: ProcedureCode | None):
        """
        id: OBR.44 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.44
        """
        self._c_data[43] = (procedure_code,)

    @property
    def procedure_code_modifier(
        self,
    ) -> tuple[ProcedureCodeModifier, ...] | tuple[None]:
        """
        id: OBR.45 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.45
        """
        return self._c_data[44]

    @procedure_code_modifier.setter  # set OBR.45
    def procedure_code_modifier(
        self,
        procedure_code_modifier: ProcedureCodeModifier
        | tuple[ProcedureCodeModifier]
        | None,
    ):
        """
        id: OBR.45 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.45
        """
        if isinstance(procedure_code_modifier, tuple):
            self._c_data[44] = procedure_code_modifier
        else:
            self._c_data[44] = (procedure_code_modifier,)

    @property
    def placer_supplemental_service_information(
        self,
    ) -> tuple[SupplementalServiceInformationValues, ...] | tuple[None]:
        """
        id: OBR.46 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.46
        """
        return self._c_data[45]

    @placer_supplemental_service_information.setter  # set OBR.46
    def placer_supplemental_service_information(
        self,
        supplemental_service_information_values: SupplementalServiceInformationValues
        | tuple[SupplementalServiceInformationValues]
        | None,
    ):
        """
        id: OBR.46 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.46
        """
        if isinstance(supplemental_service_information_values, tuple):
            self._c_data[45] = supplemental_service_information_values
        else:
            self._c_data[45] = (supplemental_service_information_values,)

    @property
    def filler_supplemental_service_information(
        self,
    ) -> tuple[SupplementalServiceInformationValues, ...] | tuple[None]:
        """
        id: OBR.47 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.47
        """
        return self._c_data[46]

    @filler_supplemental_service_information.setter  # set OBR.47
    def filler_supplemental_service_information(
        self,
        supplemental_service_information_values: SupplementalServiceInformationValues
        | tuple[SupplementalServiceInformationValues]
        | None,
    ):
        """
        id: OBR.47 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.47
        """
        if isinstance(supplemental_service_information_values, tuple):
            self._c_data[46] = supplemental_service_information_values
        else:
            self._c_data[46] = (supplemental_service_information_values,)

    @property  # get OBR.48
    def medically_necessary_duplicate_procedure_reason(
        self,
    ) -> MedicallyNecessaryDuplicateProcedureReason | None:
        """
        id: OBR.48 | len: 250 | use: C | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.48
        """
        return self._c_data[47][0]

    @medically_necessary_duplicate_procedure_reason.setter  # set OBR.48
    def medically_necessary_duplicate_procedure_reason(
        self,
        medically_necessary_duplicate_procedure_reason: MedicallyNecessaryDuplicateProcedureReason
        | None,
    ):
        """
        id: OBR.48 | len: 250 | use: C | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.48
        """
        self._c_data[47] = (medically_necessary_duplicate_procedure_reason,)

    @property  # get OBR.49
    def result_handling(self) -> ObservationResultHandling | None:
        """
        id: OBR.49 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.49
        """
        return self._c_data[48][0]

    @result_handling.setter  # set OBR.49
    def result_handling(
        self, observation_result_handling: ObservationResultHandling | None
    ):
        """
        id: OBR.49 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.49
        """
        self._c_data[48] = (observation_result_handling,)

    @property  # get OBR.50
    def parent_universal_service_identifier(self) -> CWE | None:
        """
        id: OBR.50 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.50
        """
        return self._c_data[49][0]

    @parent_universal_service_identifier.setter  # set OBR.50
    def parent_universal_service_identifier(self, cwe: CWE | None):
        """
        id: OBR.50 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBR.50
        """
        self._c_data[49] = (cwe,)
