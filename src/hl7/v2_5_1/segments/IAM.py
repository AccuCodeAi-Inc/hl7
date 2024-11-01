from __future__ import annotations
from ...base import HL7Segment
from ..data_types.XPN import XPN
from ..data_types.TS import TS
from ..data_types.CNE import CNE
from ..data_types.DT import DT
from ..data_types.ST import ST
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.EI import EI
from ..data_types.XCN import XCN
from ..data_types.XON import XON
from ..tables.AllergenType import AllergenType
from ..tables.AllergyClinicalStatus import AllergyClinicalStatus
from ..tables.SensitivityToCausativeAgentCode import SensitivityToCausativeAgentCode
from ..tables.AlertDeviceCode import AlertDeviceCode
from ..tables.AllergySeverity import AllergySeverity
from ..tables.Relationship import Relationship
from ..tables.ActionCode import ActionCode


"""
Patient Adverse Reaction Information - IAM
HL7 Version: 2.5.1

-----BEGIN SEGMENT::IAM TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    IAM,
    XPN, TS, CNE, DT, ST, SI, CE, EI, XCN, XON
)

iam = IAM(  #  - The IAM segment contains person/patient adverse reaction information of various types
    set_id_iam=si,  # SI(...)  # Required.
    allergen_type_code=None,  # CE(...) 
    allergen_code_or_mnemonic_or_description=ce,  # CE(...)  # Required.
    allergy_severity_code=None,  # CE(...) 
    allergy_reaction_code=None,  # ST(...) 
    allergy_action_code=cne,  # CNE(...)  # Required.
    allergy_unique_identifier=None,  # EI(...) 
    action_reason=None,  # ST(...) 
    sensitivity_to_causative_agent_code=None,  # CE(...) 
    allergen_group_code_or_mnemonic_or_description=None,  # CE(...) 
    onset_date=None,  # DT(...) 
    onset_date_text=None,  # ST(...) 
    reported_date_or_time=None,  # TS(...) 
    reported_by=None,  # XPN(...) 
    relationship_to_patient_code=None,  # CE(...) 
    alert_device_code=None,  # CE(...) 
    allergy_clinical_status_code=None,  # CE(...) 
    statused_by_person=None,  # XCN(...) 
    statused_by_organization=None,  # XON(...) 
    statused_at_date_or_time=None,  # TS(...) 
)

-----END SEGMENT::IAM TEMPLATE-----
"""


class IAM(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """IAM"""
    _hl7_name = """Patient Adverse Reaction Information"""
    _hl7_description = """The IAM segment contains person/patient adverse reaction information of various types"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IAM"
    _c_length = (4, 250, 250, 250, 15, 250, 427, 60, 250, 250, 8, 60, 8, 250, 250, 250, 250, 250, 250, 8,)
    _c_rpt = (1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "R", "O", "O", "R", "C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, CE, CE, CE, ST, CNE, EI, ST, CE, CE, DT, ST, TS, XPN, CE, CE, CE, XCN, XON, TS,)
    _c_aliases = ("IAM.1", "IAM.2", "IAM.3", "IAM.4", "IAM.5", "IAM.6", "IAM.7", "IAM.8", "IAM.9", "IAM.10", "IAM.11", "IAM.12", "IAM.13", "IAM.14", "IAM.15", "IAM.16", "IAM.17", "IAM.18", "IAM.19", "IAM.20",)
    _c_names = ("Set ID - IAM", "Allergen Type Code", "Allergen Code/Mnemonic/Description", "Allergy Severity Code", "Allergy Reaction Code", "Allergy Action Code", "Allergy Unique Identifier", "Action Reason", "Sensitivity to Causative Agent Code", "Allergen Group Code/Mnemonic/Description", "Onset Date", "Onset Date Text", "Reported Date/Time", "Reported By", "Relationship to Patient Code", "Alert Device Code", "Allergy Clinical Status Code", "Statused by Person", "Statused by Organization", "Statused at Date/Time",)
    _c_attrs = ("set_id_iam", "allergen_type_code", "allergen_code_or_mnemonic_or_description", "allergy_severity_code", "allergy_reaction_code", "allergy_action_code", "allergy_unique_identifier", "action_reason", "sensitivity_to_causative_agent_code", "allergen_group_code_or_mnemonic_or_description", "onset_date", "onset_date_text", "reported_date_or_time", "reported_by", "relationship_to_patient_code", "alert_device_code", "allergy_clinical_status_code", "statused_by_person", "statused_by_organization", "statused_at_date_or_time",)
    # fmt: on

    def __init__(
        self,
        set_id_iam: SI | tuple[SI],  # IAM.1
        allergen_code_or_mnemonic_or_description: CE | tuple[CE],  # IAM.3
        allergy_action_code: ActionCode | CNE | tuple[ActionCode | CNE],  # IAM.6
        allergen_type_code: AllergenType
        | CE
        | tuple[AllergenType | CE]
        | None = None,  # IAM.2
        allergy_severity_code: AllergySeverity
        | CE
        | tuple[AllergySeverity | CE]
        | None = None,  # IAM.4
        allergy_reaction_code: ST | tuple[ST] | None = None,  # IAM.5
        allergy_unique_identifier: EI | tuple[EI] | None = None,  # IAM.7
        action_reason: ST | tuple[ST] | None = None,  # IAM.8
        sensitivity_to_causative_agent_code: SensitivityToCausativeAgentCode
        | CE
        | tuple[SensitivityToCausativeAgentCode | CE]
        | None = None,  # IAM.9
        allergen_group_code_or_mnemonic_or_description: CE
        | tuple[CE]
        | None = None,  # IAM.10
        onset_date: DT | tuple[DT] | None = None,  # IAM.11
        onset_date_text: ST | tuple[ST] | None = None,  # IAM.12
        reported_date_or_time: TS | tuple[TS] | None = None,  # IAM.13
        reported_by: XPN | tuple[XPN] | None = None,  # IAM.14
        relationship_to_patient_code: Relationship
        | CE
        | tuple[Relationship | CE]
        | None = None,  # IAM.15
        alert_device_code: AlertDeviceCode
        | CE
        | tuple[AlertDeviceCode | CE]
        | None = None,  # IAM.16
        allergy_clinical_status_code: AllergyClinicalStatus
        | CE
        | tuple[AllergyClinicalStatus | CE]
        | None = None,  # IAM.17
        statused_by_person: XCN | tuple[XCN] | None = None,  # IAM.18
        statused_by_organization: XON | tuple[XON] | None = None,  # IAM.19
        statused_at_date_or_time: TS | tuple[TS] | None = None,  # IAM.20
    ):
        """
        Patient Adverse Reaction Information - `IAM <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IAM>`_
        The IAM segment contains person/patient adverse reaction information of various types. Most of this information will be derived from user-defined tables. Each IAM segment describes a single person/patient adverse reaction. This segment is used in lieu of the AL1 - Patient Allergy Information Segment to support action code/unique identifier mode update definition of repeating segments. The AL1 segment is used to support Snapshot mode update definition.

        :param set_id_iam: Sequence ID (id: IAM.1 | len: 4 | use: R | rpt: 1)
        :param allergen_type_code: Coded Element (id: IAM.2 | len: 250 | use: O | rpt: 1)
        :param allergen_code_or_mnemonic_or_description: Coded Element (id: IAM.3 | len: 250 | use: R | rpt: 1)
        :param allergy_severity_code: Coded Element (id: IAM.4 | len: 250 | use: O | rpt: 1)
        :param allergy_reaction_code: String Data (id: IAM.5 | len: 15 | use: O | rpt: *)
        :param allergy_action_code: Coded with No Exceptions (id: IAM.6 | len: 250 | use: R | rpt: 1)
        :param allergy_unique_identifier: Entity Identifier (id: IAM.7 | len: 427 | use: C | rpt: 1)
        :param action_reason: String Data (id: IAM.8 | len: 60 | use: O | rpt: 1)
        :param sensitivity_to_causative_agent_code: Coded Element (id: IAM.9 | len: 250 | use: O | rpt: 1)
        :param allergen_group_code_or_mnemonic_or_description: Coded Element (id: IAM.10 | len: 250 | use: O | rpt: 1)
        :param onset_date: Date (id: IAM.11 | len: 8 | use: O | rpt: 1)
        :param onset_date_text: String Data (id: IAM.12 | len: 60 | use: O | rpt: 1)
        :param reported_date_or_time: Time Stamp (id: IAM.13 | len: 8 | use: O | rpt: 1)
        :param reported_by: Extended Person Name (id: IAM.14 | len: 250 | use: O | rpt: 1)
        :param relationship_to_patient_code: Coded Element (id: IAM.15 | len: 250 | use: O | rpt: 1)
        :param alert_device_code: Coded Element (id: IAM.16 | len: 250 | use: O | rpt: 1)
        :param allergy_clinical_status_code: Coded Element (id: IAM.17 | len: 250 | use: O | rpt: 1)
        :param statused_by_person: Extended Composite ID Number and Name for Persons (id: IAM.18 | len: 250 | use: O | rpt: 1)
        :param statused_by_organization: Extended Composite Name and Identification Number for Organizations (id: IAM.19 | len: 250 | use: O | rpt: 1)
        :param statused_at_date_or_time: Time Stamp (id: IAM.20 | len: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 20
        self.set_id_iam = set_id_iam
        self.allergen_type_code = allergen_type_code
        self.allergen_code_or_mnemonic_or_description = (
            allergen_code_or_mnemonic_or_description
        )
        self.allergy_severity_code = allergy_severity_code
        self.allergy_reaction_code = allergy_reaction_code
        self.allergy_action_code = allergy_action_code
        self.allergy_unique_identifier = allergy_unique_identifier
        self.action_reason = action_reason
        self.sensitivity_to_causative_agent_code = sensitivity_to_causative_agent_code
        self.allergen_group_code_or_mnemonic_or_description = (
            allergen_group_code_or_mnemonic_or_description
        )
        self.onset_date = onset_date
        self.onset_date_text = onset_date_text
        self.reported_date_or_time = reported_date_or_time
        self.reported_by = reported_by
        self.relationship_to_patient_code = relationship_to_patient_code
        self.alert_device_code = alert_device_code
        self.allergy_clinical_status_code = allergy_clinical_status_code
        self.statused_by_person = statused_by_person
        self.statused_by_organization = statused_by_organization
        self.statused_at_date_or_time = statused_at_date_or_time

    @property  # get IAM.1
    def set_id_iam(self) -> SI:
        """
        id: IAM.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.1
        """
        return self._c_data[0][0]

    @set_id_iam.setter  # set IAM.1
    def set_id_iam(self, si: SI):
        """
        id: IAM.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.1
        """
        self._c_data[0] = (si,)

    @property  # get IAM.2
    def allergen_type_code(self) -> AllergenType | None:
        """
        id: IAM.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.2
        """
        return self._c_data[1][0]

    @allergen_type_code.setter  # set IAM.2
    def allergen_type_code(self, allergen_type: AllergenType | None):
        """
        id: IAM.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.2
        """
        self._c_data[1] = (allergen_type,)

    @property  # get IAM.3
    def allergen_code_or_mnemonic_or_description(self) -> CE:
        """
        id: IAM.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.3
        """
        return self._c_data[2][0]

    @allergen_code_or_mnemonic_or_description.setter  # set IAM.3
    def allergen_code_or_mnemonic_or_description(self, ce: CE):
        """
        id: IAM.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.3
        """
        self._c_data[2] = (ce,)

    @property  # get IAM.4
    def allergy_severity_code(self) -> AllergySeverity | None:
        """
        id: IAM.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.4
        """
        return self._c_data[3][0]

    @allergy_severity_code.setter  # set IAM.4
    def allergy_severity_code(self, allergy_severity: AllergySeverity | None):
        """
        id: IAM.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.4
        """
        self._c_data[3] = (allergy_severity,)

    @property
    def allergy_reaction_code(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: IAM.5 | len: 15 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.5
        """
        return self._c_data[4]

    @allergy_reaction_code.setter  # set IAM.5
    def allergy_reaction_code(self, st: ST | tuple[ST] | None):
        """
        id: IAM.5 | len: 15 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.5
        """
        if isinstance(st, tuple):
            self._c_data[4] = st
        else:
            self._c_data[4] = (st,)

    @property  # get IAM.6
    def allergy_action_code(self) -> ActionCode:
        """
        id: IAM.6 | len: 250 | use: R | rpt: 1
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.6
        """
        return self._c_data[5][0]

    @allergy_action_code.setter  # set IAM.6
    def allergy_action_code(self, action_code: ActionCode):
        """
        id: IAM.6 | len: 250 | use: R | rpt: 1
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.6
        """
        self._c_data[5] = (action_code,)

    @property  # get IAM.7
    def allergy_unique_identifier(self) -> EI | None:
        """
        id: IAM.7 | len: 427 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.7
        """
        return self._c_data[6][0]

    @allergy_unique_identifier.setter  # set IAM.7
    def allergy_unique_identifier(self, ei: EI | None):
        """
        id: IAM.7 | len: 427 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.7
        """
        self._c_data[6] = (ei,)

    @property  # get IAM.8
    def action_reason(self) -> ST | None:
        """
        id: IAM.8 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.8
        """
        return self._c_data[7][0]

    @action_reason.setter  # set IAM.8
    def action_reason(self, st: ST | None):
        """
        id: IAM.8 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.8
        """
        self._c_data[7] = (st,)

    @property  # get IAM.9
    def sensitivity_to_causative_agent_code(
        self,
    ) -> SensitivityToCausativeAgentCode | None:
        """
        id: IAM.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.9
        """
        return self._c_data[8][0]

    @sensitivity_to_causative_agent_code.setter  # set IAM.9
    def sensitivity_to_causative_agent_code(
        self,
        sensitivity_to_causative_agent_code: SensitivityToCausativeAgentCode | None,
    ):
        """
        id: IAM.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.9
        """
        self._c_data[8] = (sensitivity_to_causative_agent_code,)

    @property  # get IAM.10
    def allergen_group_code_or_mnemonic_or_description(self) -> CE | None:
        """
        id: IAM.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.10
        """
        return self._c_data[9][0]

    @allergen_group_code_or_mnemonic_or_description.setter  # set IAM.10
    def allergen_group_code_or_mnemonic_or_description(self, ce: CE | None):
        """
        id: IAM.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.10
        """
        self._c_data[9] = (ce,)

    @property  # get IAM.11
    def onset_date(self) -> DT | None:
        """
        id: IAM.11 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.11
        """
        return self._c_data[10][0]

    @onset_date.setter  # set IAM.11
    def onset_date(self, dt: DT | None):
        """
        id: IAM.11 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.11
        """
        self._c_data[10] = (dt,)

    @property  # get IAM.12
    def onset_date_text(self) -> ST | None:
        """
        id: IAM.12 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.12
        """
        return self._c_data[11][0]

    @onset_date_text.setter  # set IAM.12
    def onset_date_text(self, st: ST | None):
        """
        id: IAM.12 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.12
        """
        self._c_data[11] = (st,)

    @property  # get IAM.13
    def reported_date_or_time(self) -> TS | None:
        """
        id: IAM.13 | len: 8 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.13
        """
        return self._c_data[12][0]

    @reported_date_or_time.setter  # set IAM.13
    def reported_date_or_time(self, ts: TS | None):
        """
        id: IAM.13 | len: 8 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.13
        """
        self._c_data[12] = (ts,)

    @property  # get IAM.14
    def reported_by(self) -> XPN | None:
        """
        id: IAM.14 | len: 250 | use: O | rpt: 1
        ---
        return_type: XPN: Extended Person Name
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.14
        """
        return self._c_data[13][0]

    @reported_by.setter  # set IAM.14
    def reported_by(self, xpn: XPN | None):
        """
        id: IAM.14 | len: 250 | use: O | rpt: 1
        ---
        param_type: XPN: Extended Person Name
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.14
        """
        self._c_data[13] = (xpn,)

    @property  # get IAM.15
    def relationship_to_patient_code(self) -> Relationship | None:
        """
        id: IAM.15 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.15
        """
        return self._c_data[14][0]

    @relationship_to_patient_code.setter  # set IAM.15
    def relationship_to_patient_code(self, relationship: Relationship | None):
        """
        id: IAM.15 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.15
        """
        self._c_data[14] = (relationship,)

    @property  # get IAM.16
    def alert_device_code(self) -> AlertDeviceCode | None:
        """
        id: IAM.16 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.16
        """
        return self._c_data[15][0]

    @alert_device_code.setter  # set IAM.16
    def alert_device_code(self, alert_device_code: AlertDeviceCode | None):
        """
        id: IAM.16 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.16
        """
        self._c_data[15] = (alert_device_code,)

    @property  # get IAM.17
    def allergy_clinical_status_code(self) -> AllergyClinicalStatus | None:
        """
        id: IAM.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.17
        """
        return self._c_data[16][0]

    @allergy_clinical_status_code.setter  # set IAM.17
    def allergy_clinical_status_code(
        self, allergy_clinical_status: AllergyClinicalStatus | None
    ):
        """
        id: IAM.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.17
        """
        self._c_data[16] = (allergy_clinical_status,)

    @property  # get IAM.18
    def statused_by_person(self) -> XCN | None:
        """
        id: IAM.18 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.18
        """
        return self._c_data[17][0]

    @statused_by_person.setter  # set IAM.18
    def statused_by_person(self, xcn: XCN | None):
        """
        id: IAM.18 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.18
        """
        self._c_data[17] = (xcn,)

    @property  # get IAM.19
    def statused_by_organization(self) -> XON | None:
        """
        id: IAM.19 | len: 250 | use: O | rpt: 1
        ---
        return_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.19
        """
        return self._c_data[18][0]

    @statused_by_organization.setter  # set IAM.19
    def statused_by_organization(self, xon: XON | None):
        """
        id: IAM.19 | len: 250 | use: O | rpt: 1
        ---
        param_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.19
        """
        self._c_data[18] = (xon,)

    @property  # get IAM.20
    def statused_at_date_or_time(self) -> TS | None:
        """
        id: IAM.20 | len: 8 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.20
        """
        return self._c_data[19][0]

    @statused_at_date_or_time.setter  # set IAM.20
    def statused_at_date_or_time(self, ts: TS | None):
        """
        id: IAM.20 | len: 8 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IAM.20
        """
        self._c_data[19] = (ts,)
