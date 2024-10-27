from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CWE import CWE
from ..data_types.TS import TS
from ..data_types.SN import SN
from ..data_types.NA import NA
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..data_types.EI import EI
from ..data_types.SPS import SPS
from ..tables.SeparatorType import SeparatorType
from ..tables.Treatment import Treatment
from ..tables.TrayType import TrayType
from ..tables.SystemInducedContaminants import SystemInducedContaminants
from ..tables.SpecialHandlingCode import SpecialHandlingCode
from ..tables.ArtificialBlood import ArtificialBlood
from ..tables.OtherEnvironmentalFactors import OtherEnvironmentalFactors
from ..tables.CarrierType import CarrierType
from ..tables.DrugInterference import DrugInterference
from ..tables.ContainerStatus import ContainerStatus
from ..tables.CapType import CapType
from ..tables.AdditiveOrPreservative import AdditiveOrPreservative


"""
Specimen Container detail - SAC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::SAC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SAC,
    CWE, TS, SN, NA, CE, NM, EI, SPS
)

sac = SAC(  #  - The container detail segment is the data necessary to maintain the containers that are being used throughout the Laboratory Automation System
    external_accession_identifier=None,  # EI(...) 
    accession_identifier=None,  # EI(...) 
    container_identifier=None,  # EI(...) 
    primary=None,  # EI(...) 
    equipment_container_identifier=None,  # EI(...) 
    specimen_source=None,  # SPS(...) 
    registration_date_or_time=None,  # TS(...) 
    container_status=None,  # CE(...) 
    carrier_type=None,  # CE(...) 
    carrier_identifier=None,  # EI(...) 
    position_in_carrier=None,  # NA(...) 
    tray_type_sac=None,  # CE(...) 
    tray_identifier=None,  # EI(...) 
    position_in_tray=None,  # NA(...) 
    location=None,  # CE(...) 
    container_height=None,  # NM(...) 
    container_diameter=None,  # NM(...) 
    barrier_delta=None,  # NM(...) 
    bottom_delta=None,  # NM(...) 
    container_height_or_diameter_or_delta_units=None,  # CE(...) 
    container_volume=None,  # NM(...) 
    available_specimen_volume=None,  # NM(...) 
    initial_specimen_volume=None,  # NM(...) 
    volume_units=None,  # CE(...) 
    separator_type=None,  # CE(...) 
    cap_type=None,  # CE(...) 
    additive=None,  # CWE(...) 
    specimen_component=None,  # CE(...) 
    dilution_factor=None,  # SN(...) 
    treatment=None,  # CE(...) 
    temperature=None,  # SN(...) 
    hemolysis_index=None,  # NM(...) 
    hemolysis_index_units=None,  # CE(...) 
    lipemia_index=None,  # NM(...) 
    lipemia_index_units=None,  # CE(...) 
    icterus_index=None,  # NM(...) 
    icterus_index_units=None,  # CE(...) 
    fibrin_index=None,  # NM(...) 
    fibrin_index_units=None,  # CE(...) 
    system_induced_contaminants=None,  # CE(...) 
    drug_interference=None,  # CE(...) 
    artificial_blood=None,  # CE(...) 
    special_handling_code=None,  # CWE(...) 
    other_environmental_factors=None,  # CE(...) 
)

-----END SEGMENT::SAC TEMPLATE-----
"""


class SAC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """SAC"""
    _hl7_name = """Specimen Container detail"""
    _hl7_description = """The container detail segment is the data necessary to maintain the containers that are being used throughout the Laboratory Automation System"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC"
    _c_length = (80, 80, 80, 80, 80, 300, 26, 250, 250, 80, 80, 250, 80, 80, 250, 20, 20, 20, 20, 250, 20, 20, 20, 250, 250, 250, 250, 250, 20, 250, 20, 20, 250, 20, 250, 20, 250, 20, 250, 250, 250, 250, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 65535, 1, 65535, 65535,)
    _c_usage = ("O", "O", "C", "C", "O", "C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (EI, EI, EI, EI, EI, SPS, TS, CE, CE, EI, NA, CE, EI, NA, CE, NM, NM, NM, NM, CE, NM, NM, NM, CE, CE, CE, CWE, CE, SN, CE, SN, NM, CE, NM, CE, NM, CE, NM, CE, CE, CE, CE, CWE, CE,)
    _c_aliases = ("SAC.1", "SAC.2", "SAC.3", "SAC.4", "SAC.5", "SAC.6", "SAC.7", "SAC.8", "SAC.9", "SAC.10", "SAC.11", "SAC.12", "SAC.13", "SAC.14", "SAC.15", "SAC.16", "SAC.17", "SAC.18", "SAC.19", "SAC.20", "SAC.21", "SAC.22", "SAC.23", "SAC.24", "SAC.25", "SAC.26", "SAC.27", "SAC.28", "SAC.29", "SAC.30", "SAC.31", "SAC.32", "SAC.33", "SAC.34", "SAC.35", "SAC.36", "SAC.37", "SAC.38", "SAC.39", "SAC.40", "SAC.41", "SAC.42", "SAC.43", "SAC.44",)
    _c_names = ("External Accession Identifier", "Accession Identifier", "Container Identifier", "Primary (parent) Container Identifier ", "Equipment Container Identifier", "Specimen Source", "Registration Date/Time", "Container Status", "Carrier Type", "Carrier Identifier", "Position in Carrier", "Tray Type - SAC", "Tray Identifier", "Position in Tray", "Location", "Container Height", "Container Diameter", "Barrier Delta", "Bottom Delta", "Container Height/Diameter/Delta Units", "Container Volume", "Available Specimen Volume", "Initial Specimen Volume", "Volume Units", "Separator Type", "Cap Type", "Additive", "Specimen Component", "Dilution Factor", "Treatment", "Temperature", "Hemolysis Index", "Hemolysis Index Units", "Lipemia Index", "Lipemia Index Units", "Icterus Index", "Icterus Index Units", "Fibrin Index", "Fibrin Index Units", "System Induced Contaminants", "Drug Interference", "Artificial Blood", "Special Handling Code", "Other Environmental Factors",)
    _c_attrs = ("external_accession_identifier", "accession_identifier", "container_identifier", "primary", "equipment_container_identifier", "specimen_source", "registration_date_or_time", "container_status", "carrier_type", "carrier_identifier", "position_in_carrier", "tray_type_sac", "tray_identifier", "position_in_tray", "location", "container_height", "container_diameter", "barrier_delta", "bottom_delta", "container_height_or_diameter_or_delta_units", "container_volume", "available_specimen_volume", "initial_specimen_volume", "volume_units", "separator_type", "cap_type", "additive", "specimen_component", "dilution_factor", "treatment", "temperature", "hemolysis_index", "hemolysis_index_units", "lipemia_index", "lipemia_index_units", "icterus_index", "icterus_index_units", "fibrin_index", "fibrin_index_units", "system_induced_contaminants", "drug_interference", "artificial_blood", "special_handling_code", "other_environmental_factors",)
    # fmt: on

    def __init__(
        self,
        external_accession_identifier: EI | None = None,  # SAC.1
        accession_identifier: EI | None = None,  # SAC.2
        container_identifier: EI | None = None,  # SAC.3
        primary: EI | None = None,  # SAC.4
        equipment_container_identifier: EI | None = None,  # SAC.5
        specimen_source: SPS | None = None,  # SAC.6
        registration_date_or_time: TS | None = None,  # SAC.7
        container_status: ContainerStatus | CE | None = None,  # SAC.8
        carrier_type: CarrierType | CE | None = None,  # SAC.9
        carrier_identifier: EI | None = None,  # SAC.10
        position_in_carrier: NA | None = None,  # SAC.11
        tray_type_sac: TrayType | CE | None = None,  # SAC.12
        tray_identifier: EI | None = None,  # SAC.13
        position_in_tray: NA | None = None,  # SAC.14
        location: CE | None = None,  # SAC.15
        container_height: NM | None = None,  # SAC.16
        container_diameter: NM | None = None,  # SAC.17
        barrier_delta: NM | None = None,  # SAC.18
        bottom_delta: NM | None = None,  # SAC.19
        container_height_or_diameter_or_delta_units: CE | None = None,  # SAC.20
        container_volume: NM | None = None,  # SAC.21
        available_specimen_volume: NM | None = None,  # SAC.22
        initial_specimen_volume: NM | None = None,  # SAC.23
        volume_units: CE | None = None,  # SAC.24
        separator_type: SeparatorType | CE | None = None,  # SAC.25
        cap_type: CapType | CE | None = None,  # SAC.26
        additive: AdditiveOrPreservative | CWE | None = None,  # SAC.27
        specimen_component: CE | None = None,  # SAC.28
        dilution_factor: SN | None = None,  # SAC.29
        treatment: Treatment | CE | None = None,  # SAC.30
        temperature: SN | None = None,  # SAC.31
        hemolysis_index: NM | None = None,  # SAC.32
        hemolysis_index_units: CE | None = None,  # SAC.33
        lipemia_index: NM | None = None,  # SAC.34
        lipemia_index_units: CE | None = None,  # SAC.35
        icterus_index: NM | None = None,  # SAC.36
        icterus_index_units: CE | None = None,  # SAC.37
        fibrin_index: NM | None = None,  # SAC.38
        fibrin_index_units: CE | None = None,  # SAC.39
        system_induced_contaminants: SystemInducedContaminants
        | CE
        | None = None,  # SAC.40
        drug_interference: DrugInterference | CE | None = None,  # SAC.41
        artificial_blood: ArtificialBlood | CE | None = None,  # SAC.42
        special_handling_code: SpecialHandlingCode | CWE | None = None,  # SAC.43
        other_environmental_factors: OtherEnvironmentalFactors
        | CE
        | None = None,  # SAC.44
    ):
        """
        Specimen Container detail - `SAC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC>`_
        The container detail segment is the data necessary to maintain the containers that are being used throughout the Laboratory Automation System.

        :param external_accession_identifier: Entity Identifier (id: SAC.1 | len: 80 | use: O | rpt: 1)
        :param accession_identifier: Entity Identifier (id: SAC.2 | len: 80 | use: O | rpt: 1)
        :param container_identifier: Entity Identifier (id: SAC.3 | len: 80 | use: C | rpt: 1)
        :param primary: Entity Identifier (id: SAC.4 | len: 80 | use: C | rpt: 1)
        :param equipment_container_identifier: Entity Identifier (id: SAC.5 | len: 80 | use: O | rpt: 1)
        :param specimen_source: Specimen Source (id: SAC.6 | len: 300 | use: C | rpt: 1)
        :param registration_date_or_time: Time Stamp (id: SAC.7 | len: 26 | use: O | rpt: 1)
        :param container_status: Coded Element (id: SAC.8 | len: 250 | use: O | rpt: 1)
        :param carrier_type: Coded Element (id: SAC.9 | len: 250 | use: O | rpt: 1)
        :param carrier_identifier: Entity Identifier (id: SAC.10 | len: 80 | use: O | rpt: 1)
        :param position_in_carrier: Numeric Array (id: SAC.11 | len: 80 | use: O | rpt: 1)
        :param tray_type_sac: Coded Element (id: SAC.12 | len: 250 | use: O | rpt: 1)
        :param tray_identifier: Entity Identifier (id: SAC.13 | len: 80 | use: O | rpt: 1)
        :param position_in_tray: Numeric Array (id: SAC.14 | len: 80 | use: O | rpt: 1)
        :param location: Coded Element (id: SAC.15 | len: 250 | use: O | rpt: *)
        :param container_height: Numeric (id: SAC.16 | len: 20 | use: O | rpt: 1)
        :param container_diameter: Numeric (id: SAC.17 | len: 20 | use: O | rpt: 1)
        :param barrier_delta: Numeric (id: SAC.18 | len: 20 | use: O | rpt: 1)
        :param bottom_delta: Numeric (id: SAC.19 | len: 20 | use: O | rpt: 1)
        :param container_height_or_diameter_or_delta_units: Coded Element (id: SAC.20 | len: 250 | use: O | rpt: 1)
        :param container_volume: Numeric (id: SAC.21 | len: 20 | use: O | rpt: 1)
        :param available_specimen_volume: Numeric (id: SAC.22 | len: 20 | use: O | rpt: 1)
        :param initial_specimen_volume: Numeric (id: SAC.23 | len: 20 | use: O | rpt: 1)
        :param volume_units: Coded Element (id: SAC.24 | len: 250 | use: O | rpt: 1)
        :param separator_type: Coded Element (id: SAC.25 | len: 250 | use: O | rpt: 1)
        :param cap_type: Coded Element (id: SAC.26 | len: 250 | use: O | rpt: 1)
        :param additive: Coded with Exceptions (id: SAC.27 | len: 250 | use: O | rpt: *)
        :param specimen_component: Coded Element (id: SAC.28 | len: 250 | use: O | rpt: 1)
        :param dilution_factor: Structured Numeric (id: SAC.29 | len: 20 | use: O | rpt: 1)
        :param treatment: Coded Element (id: SAC.30 | len: 250 | use: O | rpt: 1)
        :param temperature: Structured Numeric (id: SAC.31 | len: 20 | use: O | rpt: 1)
        :param hemolysis_index: Numeric (id: SAC.32 | len: 20 | use: O | rpt: 1)
        :param hemolysis_index_units: Coded Element (id: SAC.33 | len: 250 | use: O | rpt: 1)
        :param lipemia_index: Numeric (id: SAC.34 | len: 20 | use: O | rpt: 1)
        :param lipemia_index_units: Coded Element (id: SAC.35 | len: 250 | use: O | rpt: 1)
        :param icterus_index: Numeric (id: SAC.36 | len: 20 | use: O | rpt: 1)
        :param icterus_index_units: Coded Element (id: SAC.37 | len: 250 | use: O | rpt: 1)
        :param fibrin_index: Numeric (id: SAC.38 | len: 20 | use: O | rpt: 1)
        :param fibrin_index_units: Coded Element (id: SAC.39 | len: 250 | use: O | rpt: 1)
        :param system_induced_contaminants: Coded Element (id: SAC.40 | len: 250 | use: O | rpt: *)
        :param drug_interference: Coded Element (id: SAC.41 | len: 250 | use: O | rpt: *)
        :param artificial_blood: Coded Element (id: SAC.42 | len: 250 | use: O | rpt: 1)
        :param special_handling_code: Coded with Exceptions (id: SAC.43 | len: 250 | use: O | rpt: *)
        :param other_environmental_factors: Coded Element (id: SAC.44 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 44
        self.external_accession_identifier = external_accession_identifier
        self.accession_identifier = accession_identifier
        self.container_identifier = container_identifier
        self.primary = primary
        self.equipment_container_identifier = equipment_container_identifier
        self.specimen_source = specimen_source
        self.registration_date_or_time = registration_date_or_time
        self.container_status = container_status
        self.carrier_type = carrier_type
        self.carrier_identifier = carrier_identifier
        self.position_in_carrier = position_in_carrier
        self.tray_type_sac = tray_type_sac
        self.tray_identifier = tray_identifier
        self.position_in_tray = position_in_tray
        self.location = location
        self.container_height = container_height
        self.container_diameter = container_diameter
        self.barrier_delta = barrier_delta
        self.bottom_delta = bottom_delta
        self.container_height_or_diameter_or_delta_units = (
            container_height_or_diameter_or_delta_units
        )
        self.container_volume = container_volume
        self.available_specimen_volume = available_specimen_volume
        self.initial_specimen_volume = initial_specimen_volume
        self.volume_units = volume_units
        self.separator_type = separator_type
        self.cap_type = cap_type
        self.additive = additive
        self.specimen_component = specimen_component
        self.dilution_factor = dilution_factor
        self.treatment = treatment
        self.temperature = temperature
        self.hemolysis_index = hemolysis_index
        self.hemolysis_index_units = hemolysis_index_units
        self.lipemia_index = lipemia_index
        self.lipemia_index_units = lipemia_index_units
        self.icterus_index = icterus_index
        self.icterus_index_units = icterus_index_units
        self.fibrin_index = fibrin_index
        self.fibrin_index_units = fibrin_index_units
        self.system_induced_contaminants = system_induced_contaminants
        self.drug_interference = drug_interference
        self.artificial_blood = artificial_blood
        self.special_handling_code = special_handling_code
        self.other_environmental_factors = other_environmental_factors

    @property  # get SAC.1
    def external_accession_identifier(self) -> EI | None:
        """
        id: SAC.1 | len: 80 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.1
        """
        return self._c_data[0][0]

    @external_accession_identifier.setter  # set SAC.1
    def external_accession_identifier(self, ei: EI | None):
        """
        id: SAC.1 | len: 80 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.1
        """
        self._c_data[0] = (ei,)

    @property  # get SAC.2
    def accession_identifier(self) -> EI | None:
        """
        id: SAC.2 | len: 80 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.2
        """
        return self._c_data[1][0]

    @accession_identifier.setter  # set SAC.2
    def accession_identifier(self, ei: EI | None):
        """
        id: SAC.2 | len: 80 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.2
        """
        self._c_data[1] = (ei,)

    @property  # get SAC.3
    def container_identifier(self) -> EI | None:
        """
        id: SAC.3 | len: 80 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.3
        """
        return self._c_data[2][0]

    @container_identifier.setter  # set SAC.3
    def container_identifier(self, ei: EI | None):
        """
        id: SAC.3 | len: 80 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.3
        """
        self._c_data[2] = (ei,)

    @property  # get SAC.4
    def primary(self) -> EI | None:
        """
        id: SAC.4 | len: 80 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.4
        """
        return self._c_data[3][0]

    @primary.setter  # set SAC.4
    def primary(self, ei: EI | None):
        """
        id: SAC.4 | len: 80 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.4
        """
        self._c_data[3] = (ei,)

    @property  # get SAC.5
    def equipment_container_identifier(self) -> EI | None:
        """
        id: SAC.5 | len: 80 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.5
        """
        return self._c_data[4][0]

    @equipment_container_identifier.setter  # set SAC.5
    def equipment_container_identifier(self, ei: EI | None):
        """
        id: SAC.5 | len: 80 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.5
        """
        self._c_data[4] = (ei,)

    @property  # get SAC.6
    def specimen_source(self) -> SPS | None:
        """
        id: SAC.6 | len: 300 | use: C | rpt: 1
        ---
        return_type: SPS: Specimen Source
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.6
        """
        return self._c_data[5][0]

    @specimen_source.setter  # set SAC.6
    def specimen_source(self, sps: SPS | None):
        """
        id: SAC.6 | len: 300 | use: C | rpt: 1
        ---
        param_type: SPS: Specimen Source
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.6
        """
        self._c_data[5] = (sps,)

    @property  # get SAC.7
    def registration_date_or_time(self) -> TS | None:
        """
        id: SAC.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.7
        """
        return self._c_data[6][0]

    @registration_date_or_time.setter  # set SAC.7
    def registration_date_or_time(self, ts: TS | None):
        """
        id: SAC.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.7
        """
        self._c_data[6] = (ts,)

    @property  # get SAC.8
    def container_status(self) -> ContainerStatus | None:
        """
        id: SAC.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.8
        """
        return self._c_data[7][0]

    @container_status.setter  # set SAC.8
    def container_status(self, container_status: ContainerStatus | None):
        """
        id: SAC.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.8
        """
        self._c_data[7] = (container_status,)

    @property  # get SAC.9
    def carrier_type(self) -> CarrierType | None:
        """
        id: SAC.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.9
        """
        return self._c_data[8][0]

    @carrier_type.setter  # set SAC.9
    def carrier_type(self, carrier_type: CarrierType | None):
        """
        id: SAC.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.9
        """
        self._c_data[8] = (carrier_type,)

    @property  # get SAC.10
    def carrier_identifier(self) -> EI | None:
        """
        id: SAC.10 | len: 80 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.10
        """
        return self._c_data[9][0]

    @carrier_identifier.setter  # set SAC.10
    def carrier_identifier(self, ei: EI | None):
        """
        id: SAC.10 | len: 80 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.10
        """
        self._c_data[9] = (ei,)

    @property  # get SAC.11
    def position_in_carrier(self) -> NA | None:
        """
        id: SAC.11 | len: 80 | use: O | rpt: 1
        ---
        return_type: NA: Numeric Array
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.11
        """
        return self._c_data[10][0]

    @position_in_carrier.setter  # set SAC.11
    def position_in_carrier(self, na: NA | None):
        """
        id: SAC.11 | len: 80 | use: O | rpt: 1
        ---
        param_type: NA: Numeric Array
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.11
        """
        self._c_data[10] = (na,)

    @property  # get SAC.12
    def tray_type_sac(self) -> TrayType | None:
        """
        id: SAC.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.12
        """
        return self._c_data[11][0]

    @tray_type_sac.setter  # set SAC.12
    def tray_type_sac(self, tray_type: TrayType | None):
        """
        id: SAC.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.12
        """
        self._c_data[11] = (tray_type,)

    @property  # get SAC.13
    def tray_identifier(self) -> EI | None:
        """
        id: SAC.13 | len: 80 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.13
        """
        return self._c_data[12][0]

    @tray_identifier.setter  # set SAC.13
    def tray_identifier(self, ei: EI | None):
        """
        id: SAC.13 | len: 80 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.13
        """
        self._c_data[12] = (ei,)

    @property  # get SAC.14
    def position_in_tray(self) -> NA | None:
        """
        id: SAC.14 | len: 80 | use: O | rpt: 1
        ---
        return_type: NA: Numeric Array
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.14
        """
        return self._c_data[13][0]

    @position_in_tray.setter  # set SAC.14
    def position_in_tray(self, na: NA | None):
        """
        id: SAC.14 | len: 80 | use: O | rpt: 1
        ---
        param_type: NA: Numeric Array
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.14
        """
        self._c_data[13] = (na,)

    @property
    def location(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: SAC.15 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.15
        """
        return self._c_data[14]

    @location.setter  # set SAC.15
    def location(self, ce: CE | tuple[CE] | None):
        """
        id: SAC.15 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.15
        """
        if isinstance(ce, tuple):
            self._c_data[14] = ce
        else:
            self._c_data[14] = (ce,)

    @property  # get SAC.16
    def container_height(self) -> NM | None:
        """
        id: SAC.16 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.16
        """
        return self._c_data[15][0]

    @container_height.setter  # set SAC.16
    def container_height(self, nm: NM | None):
        """
        id: SAC.16 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.16
        """
        self._c_data[15] = (nm,)

    @property  # get SAC.17
    def container_diameter(self) -> NM | None:
        """
        id: SAC.17 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.17
        """
        return self._c_data[16][0]

    @container_diameter.setter  # set SAC.17
    def container_diameter(self, nm: NM | None):
        """
        id: SAC.17 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.17
        """
        self._c_data[16] = (nm,)

    @property  # get SAC.18
    def barrier_delta(self) -> NM | None:
        """
        id: SAC.18 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.18
        """
        return self._c_data[17][0]

    @barrier_delta.setter  # set SAC.18
    def barrier_delta(self, nm: NM | None):
        """
        id: SAC.18 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.18
        """
        self._c_data[17] = (nm,)

    @property  # get SAC.19
    def bottom_delta(self) -> NM | None:
        """
        id: SAC.19 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.19
        """
        return self._c_data[18][0]

    @bottom_delta.setter  # set SAC.19
    def bottom_delta(self, nm: NM | None):
        """
        id: SAC.19 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.19
        """
        self._c_data[18] = (nm,)

    @property  # get SAC.20
    def container_height_or_diameter_or_delta_units(self) -> CE | None:
        """
        id: SAC.20 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.20
        """
        return self._c_data[19][0]

    @container_height_or_diameter_or_delta_units.setter  # set SAC.20
    def container_height_or_diameter_or_delta_units(self, ce: CE | None):
        """
        id: SAC.20 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.20
        """
        self._c_data[19] = (ce,)

    @property  # get SAC.21
    def container_volume(self) -> NM | None:
        """
        id: SAC.21 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.21
        """
        return self._c_data[20][0]

    @container_volume.setter  # set SAC.21
    def container_volume(self, nm: NM | None):
        """
        id: SAC.21 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.21
        """
        self._c_data[20] = (nm,)

    @property  # get SAC.22
    def available_specimen_volume(self) -> NM | None:
        """
        id: SAC.22 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.22
        """
        return self._c_data[21][0]

    @available_specimen_volume.setter  # set SAC.22
    def available_specimen_volume(self, nm: NM | None):
        """
        id: SAC.22 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.22
        """
        self._c_data[21] = (nm,)

    @property  # get SAC.23
    def initial_specimen_volume(self) -> NM | None:
        """
        id: SAC.23 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.23
        """
        return self._c_data[22][0]

    @initial_specimen_volume.setter  # set SAC.23
    def initial_specimen_volume(self, nm: NM | None):
        """
        id: SAC.23 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.23
        """
        self._c_data[22] = (nm,)

    @property  # get SAC.24
    def volume_units(self) -> CE | None:
        """
        id: SAC.24 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.24
        """
        return self._c_data[23][0]

    @volume_units.setter  # set SAC.24
    def volume_units(self, ce: CE | None):
        """
        id: SAC.24 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.24
        """
        self._c_data[23] = (ce,)

    @property  # get SAC.25
    def separator_type(self) -> SeparatorType | None:
        """
        id: SAC.25 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.25
        """
        return self._c_data[24][0]

    @separator_type.setter  # set SAC.25
    def separator_type(self, separator_type: SeparatorType | None):
        """
        id: SAC.25 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.25
        """
        self._c_data[24] = (separator_type,)

    @property  # get SAC.26
    def cap_type(self) -> CapType | None:
        """
        id: SAC.26 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.26
        """
        return self._c_data[25][0]

    @cap_type.setter  # set SAC.26
    def cap_type(self, cap_type: CapType | None):
        """
        id: SAC.26 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.26
        """
        self._c_data[25] = (cap_type,)

    @property
    def additive(self) -> tuple[AdditiveOrPreservative, ...] | tuple[None]:
        """
        id: SAC.27 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.27
        """
        return self._c_data[26]

    @additive.setter  # set SAC.27
    def additive(
        self,
        additive_or_preservative: AdditiveOrPreservative
        | tuple[AdditiveOrPreservative]
        | None,
    ):
        """
        id: SAC.27 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.27
        """
        if isinstance(additive_or_preservative, tuple):
            self._c_data[26] = additive_or_preservative
        else:
            self._c_data[26] = (additive_or_preservative,)

    @property  # get SAC.28
    def specimen_component(self) -> CE | None:
        """
        id: SAC.28 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.28
        """
        return self._c_data[27][0]

    @specimen_component.setter  # set SAC.28
    def specimen_component(self, ce: CE | None):
        """
        id: SAC.28 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.28
        """
        self._c_data[27] = (ce,)

    @property  # get SAC.29
    def dilution_factor(self) -> SN | None:
        """
        id: SAC.29 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.29
        """
        return self._c_data[28][0]

    @dilution_factor.setter  # set SAC.29
    def dilution_factor(self, sn: SN | None):
        """
        id: SAC.29 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.29
        """
        self._c_data[28] = (sn,)

    @property  # get SAC.30
    def treatment(self) -> Treatment | None:
        """
        id: SAC.30 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.30
        """
        return self._c_data[29][0]

    @treatment.setter  # set SAC.30
    def treatment(self, treatment: Treatment | None):
        """
        id: SAC.30 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.30
        """
        self._c_data[29] = (treatment,)

    @property  # get SAC.31
    def temperature(self) -> SN | None:
        """
        id: SAC.31 | len: 20 | use: O | rpt: 1
        ---
        return_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.31
        """
        return self._c_data[30][0]

    @temperature.setter  # set SAC.31
    def temperature(self, sn: SN | None):
        """
        id: SAC.31 | len: 20 | use: O | rpt: 1
        ---
        param_type: SN: Structured Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.31
        """
        self._c_data[30] = (sn,)

    @property  # get SAC.32
    def hemolysis_index(self) -> NM | None:
        """
        id: SAC.32 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.32
        """
        return self._c_data[31][0]

    @hemolysis_index.setter  # set SAC.32
    def hemolysis_index(self, nm: NM | None):
        """
        id: SAC.32 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.32
        """
        self._c_data[31] = (nm,)

    @property  # get SAC.33
    def hemolysis_index_units(self) -> CE | None:
        """
        id: SAC.33 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.33
        """
        return self._c_data[32][0]

    @hemolysis_index_units.setter  # set SAC.33
    def hemolysis_index_units(self, ce: CE | None):
        """
        id: SAC.33 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.33
        """
        self._c_data[32] = (ce,)

    @property  # get SAC.34
    def lipemia_index(self) -> NM | None:
        """
        id: SAC.34 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.34
        """
        return self._c_data[33][0]

    @lipemia_index.setter  # set SAC.34
    def lipemia_index(self, nm: NM | None):
        """
        id: SAC.34 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.34
        """
        self._c_data[33] = (nm,)

    @property  # get SAC.35
    def lipemia_index_units(self) -> CE | None:
        """
        id: SAC.35 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.35
        """
        return self._c_data[34][0]

    @lipemia_index_units.setter  # set SAC.35
    def lipemia_index_units(self, ce: CE | None):
        """
        id: SAC.35 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.35
        """
        self._c_data[34] = (ce,)

    @property  # get SAC.36
    def icterus_index(self) -> NM | None:
        """
        id: SAC.36 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.36
        """
        return self._c_data[35][0]

    @icterus_index.setter  # set SAC.36
    def icterus_index(self, nm: NM | None):
        """
        id: SAC.36 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.36
        """
        self._c_data[35] = (nm,)

    @property  # get SAC.37
    def icterus_index_units(self) -> CE | None:
        """
        id: SAC.37 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.37
        """
        return self._c_data[36][0]

    @icterus_index_units.setter  # set SAC.37
    def icterus_index_units(self, ce: CE | None):
        """
        id: SAC.37 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.37
        """
        self._c_data[36] = (ce,)

    @property  # get SAC.38
    def fibrin_index(self) -> NM | None:
        """
        id: SAC.38 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.38
        """
        return self._c_data[37][0]

    @fibrin_index.setter  # set SAC.38
    def fibrin_index(self, nm: NM | None):
        """
        id: SAC.38 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.38
        """
        self._c_data[37] = (nm,)

    @property  # get SAC.39
    def fibrin_index_units(self) -> CE | None:
        """
        id: SAC.39 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.39
        """
        return self._c_data[38][0]

    @fibrin_index_units.setter  # set SAC.39
    def fibrin_index_units(self, ce: CE | None):
        """
        id: SAC.39 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.39
        """
        self._c_data[38] = (ce,)

    @property
    def system_induced_contaminants(
        self,
    ) -> tuple[SystemInducedContaminants, ...] | tuple[None]:
        """
        id: SAC.40 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.40
        """
        return self._c_data[39]

    @system_induced_contaminants.setter  # set SAC.40
    def system_induced_contaminants(
        self,
        system_induced_contaminants: SystemInducedContaminants
        | tuple[SystemInducedContaminants]
        | None,
    ):
        """
        id: SAC.40 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.40
        """
        if isinstance(system_induced_contaminants, tuple):
            self._c_data[39] = system_induced_contaminants
        else:
            self._c_data[39] = (system_induced_contaminants,)

    @property
    def drug_interference(self) -> tuple[DrugInterference, ...] | tuple[None]:
        """
        id: SAC.41 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.41
        """
        return self._c_data[40]

    @drug_interference.setter  # set SAC.41
    def drug_interference(
        self, drug_interference: DrugInterference | tuple[DrugInterference] | None
    ):
        """
        id: SAC.41 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.41
        """
        if isinstance(drug_interference, tuple):
            self._c_data[40] = drug_interference
        else:
            self._c_data[40] = (drug_interference,)

    @property  # get SAC.42
    def artificial_blood(self) -> ArtificialBlood | None:
        """
        id: SAC.42 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.42
        """
        return self._c_data[41][0]

    @artificial_blood.setter  # set SAC.42
    def artificial_blood(self, artificial_blood: ArtificialBlood | None):
        """
        id: SAC.42 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.42
        """
        self._c_data[41] = (artificial_blood,)

    @property
    def special_handling_code(self) -> tuple[SpecialHandlingCode, ...] | tuple[None]:
        """
        id: SAC.43 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.43
        """
        return self._c_data[42]

    @special_handling_code.setter  # set SAC.43
    def special_handling_code(
        self,
        special_handling_code: SpecialHandlingCode | tuple[SpecialHandlingCode] | None,
    ):
        """
        id: SAC.43 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.43
        """
        if isinstance(special_handling_code, tuple):
            self._c_data[42] = special_handling_code
        else:
            self._c_data[42] = (special_handling_code,)

    @property
    def other_environmental_factors(
        self,
    ) -> tuple[OtherEnvironmentalFactors, ...] | tuple[None]:
        """
        id: SAC.44 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.44
        """
        return self._c_data[43]

    @other_environmental_factors.setter  # set SAC.44
    def other_environmental_factors(
        self,
        other_environmental_factors: OtherEnvironmentalFactors
        | tuple[OtherEnvironmentalFactors]
        | None,
    ):
        """
        id: SAC.44 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAC.44
        """
        if isinstance(other_environmental_factors, tuple):
            self._c_data[43] = other_environmental_factors
        else:
            self._c_data[43] = (other_environmental_factors,)
