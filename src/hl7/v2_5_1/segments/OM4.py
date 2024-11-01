from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TX import TX
from ..data_types.CQ import CQ
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.CWE import CWE
from ..tables.DerivedSpecimen import DerivedSpecimen
from ..tables.AdditiveOrPreservative import AdditiveOrPreservative
from ..tables.Priority import Priority


"""
Observations that Require Specimens - OM4
HL7 Version: 2.5.1

-----BEGIN SEGMENT::OM4 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OM4,
    CE, TX, CQ, ID, NM, CWE
)

om4 = OM4(  #  - This segment applies to observations/batteries that require a specimen for their performance
    sequence_number_test_or_observation_master_file=None,  # NM(...) 
    derived_specimen=None,  # ID(...) 
    container_description=None,  # TX(...) 
    container_volume=None,  # NM(...) 
    container_units=None,  # CE(...) 
    specimen=None,  # CE(...) 
    additive=None,  # CWE(...) 
    preparation=None,  # TX(...) 
    special_handling_requirements=None,  # TX(...) 
    normal_collection_volume=None,  # CQ(...) 
    minimum_collection_volume=None,  # CQ(...) 
    specimen_requirements=None,  # TX(...) 
    specimen_priorities=None,  # ID(...) 
    specimen_retention_time=None,  # CQ(...) 
)

-----END SEGMENT::OM4 TEMPLATE-----
"""


class OM4(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """OM4"""
    _hl7_name = """Observations that Require Specimens"""
    _hl7_description = """This segment applies to observations/batteries that require a specimen for their performance"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM4"
    _c_length = (4, 1, 60, 20, 250, 250, 250, 10240, 10240, 20, 20, 10240, 1, 20,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (NM, ID, TX, NM, CE, CE, CWE, TX, TX, CQ, CQ, TX, ID, CQ,)
    _c_aliases = ("OM4.1", "OM4.2", "OM4.3", "OM4.4", "OM4.5", "OM4.6", "OM4.7", "OM4.8", "OM4.9", "OM4.10", "OM4.11", "OM4.12", "OM4.13", "OM4.14",)
    _c_names = ("Sequence Number - Test/Observation Master File", "Derived Specimen", "Container Description", "Container Volume", "Container Units", "Specimen", "Additive", "Preparation", "Special Handling Requirements", "Normal Collection Volume", "Minimum Collection Volume", "Specimen Requirements", "Specimen Priorities", "Specimen Retention Time",)
    _c_attrs = ("sequence_number_test_or_observation_master_file", "derived_specimen", "container_description", "container_volume", "container_units", "specimen", "additive", "preparation", "special_handling_requirements", "normal_collection_volume", "minimum_collection_volume", "specimen_requirements", "specimen_priorities", "specimen_retention_time",)
    # fmt: on

    def __init__(
        self,
        sequence_number_test_or_observation_master_file: NM | None = None,  # OM4.1
        derived_specimen: DerivedSpecimen | ID | None = None,  # OM4.2
        container_description: TX | None = None,  # OM4.3
        container_volume: NM | None = None,  # OM4.4
        container_units: CE | None = None,  # OM4.5
        specimen: CE | None = None,  # OM4.6
        additive: AdditiveOrPreservative | CWE | None = None,  # OM4.7
        preparation: TX | None = None,  # OM4.8
        special_handling_requirements: TX | None = None,  # OM4.9
        normal_collection_volume: CQ | None = None,  # OM4.10
        minimum_collection_volume: CQ | None = None,  # OM4.11
        specimen_requirements: TX | None = None,  # OM4.12
        specimen_priorities: Priority | ID | None = None,  # OM4.13
        specimen_retention_time: CQ | None = None,  # OM4.14
    ):
        """
        Observations that Require Specimens - `OM4 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM4>`_
        This segment applies to observations/batteries that require a specimen for their performance.  When an observation or battery requires multiple specimens for their performance (e.g., creatinine clearance requires a 24-hour urine specimen and a serum specimen), multiple segments may be included, one for each specimen type.

        :param sequence_number_test_or_observation_master_file: Numeric (id: OM4.1 | len: 4 | use: O | rpt: 1)
        :param derived_specimen: Coded values for HL7 tables (id: OM4.2 | len: 1 | use: O | rpt: 1)
        :param container_description: Text Data (id: OM4.3 | len: 60 | use: O | rpt: 1)
        :param container_volume: Numeric (id: OM4.4 | len: 20 | use: O | rpt: 1)
        :param container_units: Coded Element (id: OM4.5 | len: 250 | use: O | rpt: 1)
        :param specimen: Coded Element (id: OM4.6 | len: 250 | use: O | rpt: 1)
        :param additive: Coded with Exceptions (id: OM4.7 | len: 250 | use: O | rpt: 1)
        :param preparation: Text Data (id: OM4.8 | len: 10240 | use: O | rpt: 1)
        :param special_handling_requirements: Text Data (id: OM4.9 | len: 10240 | use: O | rpt: 1)
        :param normal_collection_volume: Composite Quantity with Units (id: OM4.10 | len: 20 | use: O | rpt: 1)
        :param minimum_collection_volume: Composite Quantity with Units (id: OM4.11 | len: 20 | use: O | rpt: 1)
        :param specimen_requirements: Text Data (id: OM4.12 | len: 10240 | use: O | rpt: 1)
        :param specimen_priorities: Coded values for HL7 tables (id: OM4.13 | len: 1 | use: O | rpt: *)
        :param specimen_retention_time: Composite Quantity with Units (id: OM4.14 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 14
        self.sequence_number_test_or_observation_master_file = (
            sequence_number_test_or_observation_master_file
        )
        self.derived_specimen = derived_specimen
        self.container_description = container_description
        self.container_volume = container_volume
        self.container_units = container_units
        self.specimen = specimen
        self.additive = additive
        self.preparation = preparation
        self.special_handling_requirements = special_handling_requirements
        self.normal_collection_volume = normal_collection_volume
        self.minimum_collection_volume = minimum_collection_volume
        self.specimen_requirements = specimen_requirements
        self.specimen_priorities = specimen_priorities
        self.specimen_retention_time = specimen_retention_time

    @property  # get OM4.1
    def sequence_number_test_or_observation_master_file(self) -> NM | None:
        """
        id: OM4.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.1
        """
        return self._c_data[0][0]

    @sequence_number_test_or_observation_master_file.setter  # set OM4.1
    def sequence_number_test_or_observation_master_file(self, nm: NM | None):
        """
        id: OM4.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.1
        """
        self._c_data[0] = (nm,)

    @property  # get OM4.2
    def derived_specimen(self) -> DerivedSpecimen | None:
        """
        id: OM4.2 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.2
        """
        return self._c_data[1][0]

    @derived_specimen.setter  # set OM4.2
    def derived_specimen(self, derived_specimen: DerivedSpecimen | None):
        """
        id: OM4.2 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.2
        """
        self._c_data[1] = (derived_specimen,)

    @property  # get OM4.3
    def container_description(self) -> TX | None:
        """
        id: OM4.3 | len: 60 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.3
        """
        return self._c_data[2][0]

    @container_description.setter  # set OM4.3
    def container_description(self, tx: TX | None):
        """
        id: OM4.3 | len: 60 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.3
        """
        self._c_data[2] = (tx,)

    @property  # get OM4.4
    def container_volume(self) -> NM | None:
        """
        id: OM4.4 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.4
        """
        return self._c_data[3][0]

    @container_volume.setter  # set OM4.4
    def container_volume(self, nm: NM | None):
        """
        id: OM4.4 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.4
        """
        self._c_data[3] = (nm,)

    @property  # get OM4.5
    def container_units(self) -> CE | None:
        """
        id: OM4.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.5
        """
        return self._c_data[4][0]

    @container_units.setter  # set OM4.5
    def container_units(self, ce: CE | None):
        """
        id: OM4.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.5
        """
        self._c_data[4] = (ce,)

    @property  # get OM4.6
    def specimen(self) -> CE | None:
        """
        id: OM4.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.6
        """
        return self._c_data[5][0]

    @specimen.setter  # set OM4.6
    def specimen(self, ce: CE | None):
        """
        id: OM4.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.6
        """
        self._c_data[5] = (ce,)

    @property  # get OM4.7
    def additive(self) -> AdditiveOrPreservative | None:
        """
        id: OM4.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.7
        """
        return self._c_data[6][0]

    @additive.setter  # set OM4.7
    def additive(self, additive_or_preservative: AdditiveOrPreservative | None):
        """
        id: OM4.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.7
        """
        self._c_data[6] = (additive_or_preservative,)

    @property  # get OM4.8
    def preparation(self) -> TX | None:
        """
        id: OM4.8 | len: 10240 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.8
        """
        return self._c_data[7][0]

    @preparation.setter  # set OM4.8
    def preparation(self, tx: TX | None):
        """
        id: OM4.8 | len: 10240 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.8
        """
        self._c_data[7] = (tx,)

    @property  # get OM4.9
    def special_handling_requirements(self) -> TX | None:
        """
        id: OM4.9 | len: 10240 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.9
        """
        return self._c_data[8][0]

    @special_handling_requirements.setter  # set OM4.9
    def special_handling_requirements(self, tx: TX | None):
        """
        id: OM4.9 | len: 10240 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.9
        """
        self._c_data[8] = (tx,)

    @property  # get OM4.10
    def normal_collection_volume(self) -> CQ | None:
        """
        id: OM4.10 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.10
        """
        return self._c_data[9][0]

    @normal_collection_volume.setter  # set OM4.10
    def normal_collection_volume(self, cq: CQ | None):
        """
        id: OM4.10 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.10
        """
        self._c_data[9] = (cq,)

    @property  # get OM4.11
    def minimum_collection_volume(self) -> CQ | None:
        """
        id: OM4.11 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.11
        """
        return self._c_data[10][0]

    @minimum_collection_volume.setter  # set OM4.11
    def minimum_collection_volume(self, cq: CQ | None):
        """
        id: OM4.11 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.11
        """
        self._c_data[10] = (cq,)

    @property  # get OM4.12
    def specimen_requirements(self) -> TX | None:
        """
        id: OM4.12 | len: 10240 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.12
        """
        return self._c_data[11][0]

    @specimen_requirements.setter  # set OM4.12
    def specimen_requirements(self, tx: TX | None):
        """
        id: OM4.12 | len: 10240 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.12
        """
        self._c_data[11] = (tx,)

    @property
    def specimen_priorities(self) -> tuple[Priority, ...] | tuple[None]:
        """
        id: OM4.13 | len: 1 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.13
        """
        return self._c_data[12]

    @specimen_priorities.setter  # set OM4.13
    def specimen_priorities(self, priority: Priority | tuple[Priority] | None):
        """
        id: OM4.13 | len: 1 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.13
        """
        if isinstance(priority, tuple):
            self._c_data[12] = priority
        else:
            self._c_data[12] = (priority,)

    @property  # get OM4.14
    def specimen_retention_time(self) -> CQ | None:
        """
        id: OM4.14 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.14
        """
        return self._c_data[13][0]

    @specimen_retention_time.setter  # set OM4.14
    def specimen_retention_time(self, cq: CQ | None):
        """
        id: OM4.14 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM4.14
        """
        self._c_data[13] = (cq,)
