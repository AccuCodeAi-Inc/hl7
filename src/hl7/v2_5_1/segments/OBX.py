from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.VARIES import VARIES
from ..data_types.XAD import XAD
from ..data_types.ST import ST
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..data_types.EI import EI
from ..data_types.IS import IS
from ..data_types.XCN import XCN
from ..data_types.XON import XON
from ..tables.ObservationResultStatusCodesInterpretation import (
    ObservationResultStatusCodesInterpretation,
)
from ..tables.ValueType import ValueType
from ..tables.NatureOfAbnormalTesting import NatureOfAbnormalTesting
from ..tables.AbnormalFlags import AbnormalFlags


"""
Observation/Result - OBX
HL7 Version: 2.5.1

-----BEGIN SEGMENT::OBX TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OBX,
    ID, TS, VARIES, XAD, ST, SI, CE, NM, EI, IS, XCN, XON
)

obx = OBX(  #  - The OBX segment is used to transmit a single observation or observation fragment
    set_id_obx=None,  # SI(...) 
    value_type=None,  # ID(...) 
    observation_identifier=ce,  # CE(...)  # Required.
    observation_sub_id=None,  # ST(...) 
    observation_value=None,  # VARIES(...) 
    units=None,  # CE(...) 
    references_range=None,  # ST(...) 
    abnormal_flags=None,  # IS(...) 
    probability=None,  # NM(...) 
    nature_of_abnormal_test=None,  # ID(...) 
    observation_result_status=id,  # ID(...)  # Required.
    effective_date_of_reference_range=None,  # TS(...) 
    user_defined_access_checks=None,  # ST(...) 
    date_or_time_of_the_observation=None,  # TS(...) 
    producers_id=None,  # CE(...) 
    responsible_observer=None,  # XCN(...) 
    observation_method=None,  # CE(...) 
    equipment_instance_identifier=None,  # EI(...) 
    date_or_time_of_the_analysis=None,  # TS(...) 
    reserved_for_harmonization_with_v2_6=None,  # ST(...) 
    reserved_for_harmonization_with_v2_6_20=None,  # ST(...) 
    reserved_for_harmonization_with_v2_6_21=None,  # ST(...) 
    performing_organization_name=None,  # XON(...) 
    performing_organization_address=None,  # XAD(...) 
    performing_organization_medical_director=None,  # XCN(...) 
)

-----END SEGMENT::OBX TEMPLATE-----
"""


class OBX(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """OBX"""
    _hl7_name = """Observation/Result"""
    _hl7_description = """The OBX segment is used to transmit a single observation or observation fragment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX"
    _c_length = (4, 2, 250, 20, 99999, 250, 60, 5, 5, 2, 1, 26, 20, 26, 250, 250, 250, 22, 26, 0, 0, 0, 567, 631, 3002,)
    _c_rpt = (1, 1, 1, 1, 65535, 1, 1, 65535, 1, 65535, 1, 1, 1, 1, 1, 65535, 65535, 65535, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "C", "R", "C", "C", "O", "O", "O", "O", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "X", "O", "O", "O",)
    _c_components = (SI, ID, CE, ST, VARIES, CE, ST, IS, NM, ID, ID, TS, ST, TS, CE, XCN, CE, EI, TS, ST, ST, ST, XON, XAD, XCN,)
    _c_aliases = ("OBX.1", "OBX.2", "OBX.3", "OBX.4", "OBX.5", "OBX.6", "OBX.7", "OBX.8", "OBX.9", "OBX.10", "OBX.11", "OBX.12", "OBX.13", "OBX.14", "OBX.15", "OBX.16", "OBX.17", "OBX.18", "OBX.19", "OBX.20", "OBX.21", "OBX.22", "OBX.23", "OBX.24", "OBX.25",)
    _c_names = ("Set ID - OBX", "Value Type", "Observation Identifier", "Observation Sub-ID", "Observation Value", "Units", "References Range", "Abnormal Flags", "Probability", "Nature of Abnormal Test", "Observation Result Status", "Effective Date of Reference Range", "User Defined Access Checks", "Date/Time of the Observation", "Producer's ID", "Responsible Observer", "Observation Method", "Equipment Instance Identifier", "Date/Time of the Analysis", "Reserved for harmonization with V2.6 ", "Reserved for harmonization with V2.6", "Reserved for harmonization with V2.6", "Performing Organization Name", "Performing Organization Address", "Performing Organization Medical Director",)
    _c_attrs = ("set_id_obx", "value_type", "observation_identifier", "observation_sub_id", "observation_value", "units", "references_range", "abnormal_flags", "probability", "nature_of_abnormal_test", "observation_result_status", "effective_date_of_reference_range", "user_defined_access_checks", "date_or_time_of_the_observation", "producers_id", "responsible_observer", "observation_method", "equipment_instance_identifier", "date_or_time_of_the_analysis", "reserved_for_harmonization_with_v2_6", "reserved_for_harmonization_with_v2_6_20", "reserved_for_harmonization_with_v2_6_21", "performing_organization_name", "performing_organization_address", "performing_organization_medical_director",)
    # fmt: on

    def __init__(
        self,
        observation_identifier: CE,  # OBX.3
        observation_result_status: ObservationResultStatusCodesInterpretation
        | ID,  # OBX.11
        set_id_obx: SI | None = None,  # OBX.1
        value_type: ValueType | ID | None = None,  # OBX.2
        observation_sub_id: ST | None = None,  # OBX.4
        observation_value: VARIES | None = None,  # OBX.5
        units: CE | None = None,  # OBX.6
        references_range: ST | None = None,  # OBX.7
        abnormal_flags: AbnormalFlags | IS | None = None,  # OBX.8
        probability: NM | None = None,  # OBX.9
        nature_of_abnormal_test: NatureOfAbnormalTesting | ID | None = None,  # OBX.10
        effective_date_of_reference_range: TS | None = None,  # OBX.12
        user_defined_access_checks: ST | None = None,  # OBX.13
        date_or_time_of_the_observation: TS | None = None,  # OBX.14
        producers_id: CE | None = None,  # OBX.15
        responsible_observer: XCN | None = None,  # OBX.16
        observation_method: CE | None = None,  # OBX.17
        equipment_instance_identifier: EI | None = None,  # OBX.18
        date_or_time_of_the_analysis: TS | None = None,  # OBX.19
        reserved_for_harmonization_with_v2_6: ST | None = None,  # OBX.20
        reserved_for_harmonization_with_v2_6_20: ST | None = None,  # OBX.21
        reserved_for_harmonization_with_v2_6_21: ST | None = None,  # OBX.22
        performing_organization_name: XON | None = None,  # OBX.23
        performing_organization_address: XAD | None = None,  # OBX.24
        performing_organization_medical_director: XCN | None = None,  # OBX.25
    ):
        """
                Observation/Result - `OBX <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX>`_
                The OBX segment is used to transmit a single observation or observation fragment. It represents the smallest indivisible unit of a report. The OBX segment can also contain encapsulated data, e.g., a CDA document or a DICOM image.

        Its principal mission is to carry information about observations in report messages.  But the OBX can also be part of an observation order.  In this case, the OBX carries clinical information needed by the filler to interpret the observation the filler makes.  For example, an OBX is needed to report the inspired oxygen on an order for a blood oxygen to a blood gas lab, or to report the menstrual phase information which should be included on an order for a pap smear to a cytology lab.  Appendix 7A includes codes for identifying many of pieces of information needed by observation producing services to properly interpret a test result.  OBX is also found in other HL7 messages that need to include patient clinical information.

                :param set_id_obx: Sequence ID (id: OBX.1 | len: 4 | use: O | rpt: 1)
                :param value_type: Coded values for HL7 tables (id: OBX.2 | len: 2 | use: C | rpt: 1)
                :param observation_identifier: Coded Element (id: OBX.3 | len: 250 | use: R | rpt: 1)
                :param observation_sub_id: String Data (id: OBX.4 | len: 20 | use: C | rpt: 1)
                :param observation_value: Variable Datatype (id: OBX.5 | len: 99999 | use: C | rpt: *)
                :param units: Coded Element (id: OBX.6 | len: 250 | use: O | rpt: 1)
                :param references_range: String Data (id: OBX.7 | len: 60 | use: O | rpt: 1)
                :param abnormal_flags: Coded value for user-defined tables (id: OBX.8 | len: 5 | use: O | rpt: *)
                :param probability: Numeric (id: OBX.9 | len: 5 | use: O | rpt: 1)
                :param nature_of_abnormal_test: Coded values for HL7 tables (id: OBX.10 | len: 2 | use: O | rpt: *)
                :param observation_result_status: Coded values for HL7 tables (id: OBX.11 | len: 1 | use: R | rpt: 1)
                :param effective_date_of_reference_range: Time Stamp (id: OBX.12 | len: 26 | use: O | rpt: 1)
                :param user_defined_access_checks: String Data (id: OBX.13 | len: 20 | use: O | rpt: 1)
                :param date_or_time_of_the_observation: Time Stamp (id: OBX.14 | len: 26 | use: O | rpt: 1)
                :param producers_id: Coded Element (id: OBX.15 | len: 250 | use: O | rpt: 1)
                :param responsible_observer: Extended Composite ID Number and Name for Persons (id: OBX.16 | len: 250 | use: O | rpt: *)
                :param observation_method: Coded Element (id: OBX.17 | len: 250 | use: O | rpt: *)
                :param equipment_instance_identifier: Entity Identifier (id: OBX.18 | len: 22 | use: O | rpt: *)
                :param date_or_time_of_the_analysis: Time Stamp (id: OBX.19 | len: 26 | use: O | rpt: 1)
                :param reserved_for_harmonization_with_v2_6: String Data (id: OBX.20 | len: 0 | use: X | rpt: 1)
                :param reserved_for_harmonization_with_v2_6_20: String Data (id: OBX.21 | len: 0 | use: X | rpt: 1)
                :param reserved_for_harmonization_with_v2_6_21: String Data (id: OBX.22 | len: 0 | use: X | rpt: 1)
                :param performing_organization_name: Extended Composite Name and Identification Number for Organizations (id: OBX.23 | len: 567 | use: O | rpt: 1)
                :param performing_organization_address: Extended Address (id: OBX.24 | len: 631 | use: O | rpt: 1)
                :param performing_organization_medical_director: Extended Composite ID Number and Name for Persons (id: OBX.25 | len: 3002 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 25
        self.set_id_obx = set_id_obx
        self.value_type = value_type
        self.observation_identifier = observation_identifier
        self.observation_sub_id = observation_sub_id
        self.observation_value = observation_value
        self.units = units
        self.references_range = references_range
        self.abnormal_flags = abnormal_flags
        self.probability = probability
        self.nature_of_abnormal_test = nature_of_abnormal_test
        self.observation_result_status = observation_result_status
        self.effective_date_of_reference_range = effective_date_of_reference_range
        self.user_defined_access_checks = user_defined_access_checks
        self.date_or_time_of_the_observation = date_or_time_of_the_observation
        self.producers_id = producers_id
        self.responsible_observer = responsible_observer
        self.observation_method = observation_method
        self.equipment_instance_identifier = equipment_instance_identifier
        self.date_or_time_of_the_analysis = date_or_time_of_the_analysis
        self.reserved_for_harmonization_with_v2_6 = reserved_for_harmonization_with_v2_6
        self.reserved_for_harmonization_with_v2_6_20 = (
            reserved_for_harmonization_with_v2_6_20
        )
        self.reserved_for_harmonization_with_v2_6_21 = (
            reserved_for_harmonization_with_v2_6_21
        )
        self.performing_organization_name = performing_organization_name
        self.performing_organization_address = performing_organization_address
        self.performing_organization_medical_director = (
            performing_organization_medical_director
        )

    @property  # get OBX.1
    def set_id_obx(self) -> SI | None:
        """
        id: OBX.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.1
        """
        return self._c_data[0][0]

    @set_id_obx.setter  # set OBX.1
    def set_id_obx(self, si: SI | None):
        """
        id: OBX.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.1
        """
        self._c_data[0] = (si,)

    @property  # get OBX.2
    def value_type(self) -> ValueType | None:
        """
        id: OBX.2 | len: 2 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.2
        """
        return self._c_data[1][0]

    @value_type.setter  # set OBX.2
    def value_type(self, value_type: ValueType | None):
        """
        id: OBX.2 | len: 2 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.2
        """
        self._c_data[1] = (value_type,)

    @property  # get OBX.3
    def observation_identifier(self) -> CE:
        """
        id: OBX.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.3
        """
        return self._c_data[2][0]

    @observation_identifier.setter  # set OBX.3
    def observation_identifier(self, ce: CE):
        """
        id: OBX.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.3
        """
        self._c_data[2] = (ce,)

    @property  # get OBX.4
    def observation_sub_id(self) -> ST | None:
        """
        id: OBX.4 | len: 20 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.4
        """
        return self._c_data[3][0]

    @observation_sub_id.setter  # set OBX.4
    def observation_sub_id(self, st: ST | None):
        """
        id: OBX.4 | len: 20 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.4
        """
        self._c_data[3] = (st,)

    @property
    def observation_value(self) -> tuple[VARIES, ...] | tuple[None]:
        """
        id: OBX.5 | len: 99999 | use: C | rpt: *
        ---
        return_type: tuple[VARIES, ...]: (Variable Datatype, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.5
        """
        return self._c_data[4]

    @observation_value.setter  # set OBX.5
    def observation_value(self, varies: VARIES | tuple[VARIES] | None):
        """
        id: OBX.5 | len: 99999 | use: C | rpt: *
        ---
        param_type: VARIES | tuple[VARIES, ...]: (Variable Datatype, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.5
        """
        if isinstance(varies, tuple):
            self._c_data[4] = varies
        else:
            self._c_data[4] = (varies,)

    @property  # get OBX.6
    def units(self) -> CE | None:
        """
        id: OBX.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.6
        """
        return self._c_data[5][0]

    @units.setter  # set OBX.6
    def units(self, ce: CE | None):
        """
        id: OBX.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.6
        """
        self._c_data[5] = (ce,)

    @property  # get OBX.7
    def references_range(self) -> ST | None:
        """
        id: OBX.7 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.7
        """
        return self._c_data[6][0]

    @references_range.setter  # set OBX.7
    def references_range(self, st: ST | None):
        """
        id: OBX.7 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.7
        """
        self._c_data[6] = (st,)

    @property
    def abnormal_flags(self) -> tuple[AbnormalFlags, ...] | tuple[None]:
        """
        id: OBX.8 | len: 5 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.8
        """
        return self._c_data[7]

    @abnormal_flags.setter  # set OBX.8
    def abnormal_flags(
        self, abnormal_flags: AbnormalFlags | tuple[AbnormalFlags] | None
    ):
        """
        id: OBX.8 | len: 5 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.8
        """
        if isinstance(abnormal_flags, tuple):
            self._c_data[7] = abnormal_flags
        else:
            self._c_data[7] = (abnormal_flags,)

    @property  # get OBX.9
    def probability(self) -> NM | None:
        """
        id: OBX.9 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.9
        """
        return self._c_data[8][0]

    @probability.setter  # set OBX.9
    def probability(self, nm: NM | None):
        """
        id: OBX.9 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.9
        """
        self._c_data[8] = (nm,)

    @property
    def nature_of_abnormal_test(
        self,
    ) -> tuple[NatureOfAbnormalTesting, ...] | tuple[None]:
        """
        id: OBX.10 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.10
        """
        return self._c_data[9]

    @nature_of_abnormal_test.setter  # set OBX.10
    def nature_of_abnormal_test(
        self,
        nature_of_abnormal_testing: NatureOfAbnormalTesting
        | tuple[NatureOfAbnormalTesting]
        | None,
    ):
        """
        id: OBX.10 | len: 2 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.10
        """
        if isinstance(nature_of_abnormal_testing, tuple):
            self._c_data[9] = nature_of_abnormal_testing
        else:
            self._c_data[9] = (nature_of_abnormal_testing,)

    @property  # get OBX.11
    def observation_result_status(self) -> ObservationResultStatusCodesInterpretation:
        """
        id: OBX.11 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.11
        """
        return self._c_data[10][0]

    @observation_result_status.setter  # set OBX.11
    def observation_result_status(
        self,
        observation_result_status_codes_interpretation: ObservationResultStatusCodesInterpretation,
    ):
        """
        id: OBX.11 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.11
        """
        self._c_data[10] = (observation_result_status_codes_interpretation,)

    @property  # get OBX.12
    def effective_date_of_reference_range(self) -> TS | None:
        """
        id: OBX.12 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.12
        """
        return self._c_data[11][0]

    @effective_date_of_reference_range.setter  # set OBX.12
    def effective_date_of_reference_range(self, ts: TS | None):
        """
        id: OBX.12 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.12
        """
        self._c_data[11] = (ts,)

    @property  # get OBX.13
    def user_defined_access_checks(self) -> ST | None:
        """
        id: OBX.13 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.13
        """
        return self._c_data[12][0]

    @user_defined_access_checks.setter  # set OBX.13
    def user_defined_access_checks(self, st: ST | None):
        """
        id: OBX.13 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.13
        """
        self._c_data[12] = (st,)

    @property  # get OBX.14
    def date_or_time_of_the_observation(self) -> TS | None:
        """
        id: OBX.14 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.14
        """
        return self._c_data[13][0]

    @date_or_time_of_the_observation.setter  # set OBX.14
    def date_or_time_of_the_observation(self, ts: TS | None):
        """
        id: OBX.14 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.14
        """
        self._c_data[13] = (ts,)

    @property  # get OBX.15
    def producers_id(self) -> CE | None:
        """
        id: OBX.15 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.15
        """
        return self._c_data[14][0]

    @producers_id.setter  # set OBX.15
    def producers_id(self, ce: CE | None):
        """
        id: OBX.15 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.15
        """
        self._c_data[14] = (ce,)

    @property
    def responsible_observer(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: OBX.16 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.16
        """
        return self._c_data[15]

    @responsible_observer.setter  # set OBX.16
    def responsible_observer(self, xcn: XCN | tuple[XCN] | None):
        """
        id: OBX.16 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.16
        """
        if isinstance(xcn, tuple):
            self._c_data[15] = xcn
        else:
            self._c_data[15] = (xcn,)

    @property
    def observation_method(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: OBX.17 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.17
        """
        return self._c_data[16]

    @observation_method.setter  # set OBX.17
    def observation_method(self, ce: CE | tuple[CE] | None):
        """
        id: OBX.17 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.17
        """
        if isinstance(ce, tuple):
            self._c_data[16] = ce
        else:
            self._c_data[16] = (ce,)

    @property
    def equipment_instance_identifier(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: OBX.18 | len: 22 | use: O | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.18
        """
        return self._c_data[17]

    @equipment_instance_identifier.setter  # set OBX.18
    def equipment_instance_identifier(self, ei: EI | tuple[EI] | None):
        """
        id: OBX.18 | len: 22 | use: O | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.18
        """
        if isinstance(ei, tuple):
            self._c_data[17] = ei
        else:
            self._c_data[17] = (ei,)

    @property  # get OBX.19
    def date_or_time_of_the_analysis(self) -> TS | None:
        """
        id: OBX.19 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.19
        """
        return self._c_data[18][0]

    @date_or_time_of_the_analysis.setter  # set OBX.19
    def date_or_time_of_the_analysis(self, ts: TS | None):
        """
        id: OBX.19 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.19
        """
        self._c_data[18] = (ts,)

    @property  # get OBX.20
    def reserved_for_harmonization_with_v2_6(self) -> ST | None:
        """
        id: OBX.20 | len: 0 | use: X | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.20
        """
        return self._c_data[19][0]

    @reserved_for_harmonization_with_v2_6.setter  # set OBX.20
    def reserved_for_harmonization_with_v2_6(self, st: ST | None):
        """
        id: OBX.20 | len: 0 | use: X | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.20
        """
        self._c_data[19] = (st,)

    @property  # get OBX.21
    def reserved_for_harmonization_with_v2_6_20(self) -> ST | None:
        """
        id: OBX.21 | len: 0 | use: X | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.21
        """
        return self._c_data[20][0]

    @reserved_for_harmonization_with_v2_6_20.setter  # set OBX.21
    def reserved_for_harmonization_with_v2_6_20(self, st: ST | None):
        """
        id: OBX.21 | len: 0 | use: X | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.21
        """
        self._c_data[20] = (st,)

    @property  # get OBX.22
    def reserved_for_harmonization_with_v2_6_21(self) -> ST | None:
        """
        id: OBX.22 | len: 0 | use: X | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.22
        """
        return self._c_data[21][0]

    @reserved_for_harmonization_with_v2_6_21.setter  # set OBX.22
    def reserved_for_harmonization_with_v2_6_21(self, st: ST | None):
        """
        id: OBX.22 | len: 0 | use: X | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.22
        """
        self._c_data[21] = (st,)

    @property  # get OBX.23
    def performing_organization_name(self) -> XON | None:
        """
        id: OBX.23 | len: 567 | use: O | rpt: 1
        ---
        return_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.23
        """
        return self._c_data[22][0]

    @performing_organization_name.setter  # set OBX.23
    def performing_organization_name(self, xon: XON | None):
        """
        id: OBX.23 | len: 567 | use: O | rpt: 1
        ---
        param_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.23
        """
        self._c_data[22] = (xon,)

    @property  # get OBX.24
    def performing_organization_address(self) -> XAD | None:
        """
        id: OBX.24 | len: 631 | use: O | rpt: 1
        ---
        return_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.24
        """
        return self._c_data[23][0]

    @performing_organization_address.setter  # set OBX.24
    def performing_organization_address(self, xad: XAD | None):
        """
        id: OBX.24 | len: 631 | use: O | rpt: 1
        ---
        param_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.24
        """
        self._c_data[23] = (xad,)

    @property  # get OBX.25
    def performing_organization_medical_director(self) -> XCN | None:
        """
        id: OBX.25 | len: 3002 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.25
        """
        return self._c_data[24][0]

    @performing_organization_medical_director.setter  # set OBX.25
    def performing_organization_medical_director(self, xcn: XCN | None):
        """
        id: OBX.25 | len: 3002 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OBX.25
        """
        self._c_data[24] = (xcn,)
