from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.XCN import XCN
from ..data_types.CE import CE
from ..tables.HospitalService import HospitalService
from ..tables.TriageCode import TriageCode
from ..tables.PhysicianId import PhysicianId
from ..tables.NewbornCode import NewbornCode
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.GestationCategoryCode import GestationCategoryCode
from ..tables.CaseCategoryCode import CaseCategoryCode
from ..tables.SeverityOfIllnessCode import SeverityOfIllnessCode


"""
Abstract - ABS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ABS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ABS,
    TS, ID, NM, XCN, CE
)

abs = ABS(  #  - This segment was created to communicate patient abstract information used for billing and reimbursement purposes
    discharge_care_provider=None,  # XCN(...) 
    transfer_medical_service_code=None,  # CE(...) 
    severity_of_illness_code=None,  # CE(...) 
    date_or_time_of_attestation=None,  # TS(...) 
    attested_by=None,  # XCN(...) 
    triage_code=None,  # CE(...) 
    abstract_completion_date_or_time=None,  # TS(...) 
    abstracted_by=None,  # XCN(...) 
    case_category_code=None,  # CE(...) 
    caesarian_section_indicator=None,  # ID(...) 
    gestation_category_code=None,  # CE(...) 
    gestation_period_weeks=None,  # NM(...) 
    newborn_code=None,  # CE(...) 
    stillborn_indicator=None,  # ID(...) 
)

-----END SEGMENT::ABS TEMPLATE-----
"""


class ABS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ABS"""
    _hl7_name = """Abstract"""
    _hl7_description = """This segment was created to communicate patient abstract information used for billing and reimbursement purposes"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ABS"
    _c_length = (250, 250, 250, 26, 250, 250, 26, 250, 250, 1, 250, 3, 250, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (XCN, CE, CE, TS, XCN, CE, TS, XCN, CE, ID, CE, NM, CE, ID,)
    _c_aliases = ("ABS.1", "ABS.2", "ABS.3", "ABS.4", "ABS.5", "ABS.6", "ABS.7", "ABS.8", "ABS.9", "ABS.10", "ABS.11", "ABS.12", "ABS.13", "ABS.14",)
    _c_names = ("Discharge Care Provider", "Transfer Medical Service Code", "Severity of Illness Code", "Date/Time of Attestation", "Attested By", "Triage Code", "Abstract Completion Date/Time", "Abstracted By", "Case Category Code", "Caesarian Section Indicator", "Gestation Category Code", "Gestation Period - Weeks", "Newborn Code", "Stillborn Indicator",)
    _c_attrs = ("discharge_care_provider", "transfer_medical_service_code", "severity_of_illness_code", "date_or_time_of_attestation", "attested_by", "triage_code", "abstract_completion_date_or_time", "abstracted_by", "case_category_code", "caesarian_section_indicator", "gestation_category_code", "gestation_period_weeks", "newborn_code", "stillborn_indicator",)
    # fmt: on

    def __init__(
        self,
        discharge_care_provider: PhysicianId
        | XCN
        | tuple[PhysicianId | XCN]
        | None = None,  # ABS.1
        transfer_medical_service_code: HospitalService
        | CE
        | tuple[HospitalService | CE]
        | None = None,  # ABS.2
        severity_of_illness_code: SeverityOfIllnessCode
        | CE
        | tuple[SeverityOfIllnessCode | CE]
        | None = None,  # ABS.3
        date_or_time_of_attestation: TS | tuple[TS] | None = None,  # ABS.4
        attested_by: XCN | tuple[XCN] | None = None,  # ABS.5
        triage_code: TriageCode | CE | tuple[TriageCode | CE] | None = None,  # ABS.6
        abstract_completion_date_or_time: TS | tuple[TS] | None = None,  # ABS.7
        abstracted_by: XCN | tuple[XCN] | None = None,  # ABS.8
        case_category_code: CaseCategoryCode
        | CE
        | tuple[CaseCategoryCode | CE]
        | None = None,  # ABS.9
        caesarian_section_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # ABS.10
        gestation_category_code: GestationCategoryCode
        | CE
        | tuple[GestationCategoryCode | CE]
        | None = None,  # ABS.11
        gestation_period_weeks: NM | tuple[NM] | None = None,  # ABS.12
        newborn_code: NewbornCode
        | CE
        | tuple[NewbornCode | CE]
        | None = None,  # ABS.13
        stillborn_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # ABS.14
    ):
        """
        Abstract - `ABS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ABS>`_
        This segment was created to communicate patient abstract information used for billing and reimbursement purposes. Abstract is a condensed form of medical history created for analysis, care planning, etc.

        :param discharge_care_provider: Extended Composite ID Number and Name for Persons (id: ABS.1 | len: 250 | use: O | rpt: 1)
        :param transfer_medical_service_code: Coded Element (id: ABS.2 | len: 250 | use: O | rpt: 1)
        :param severity_of_illness_code: Coded Element (id: ABS.3 | len: 250 | use: O | rpt: 1)
        :param date_or_time_of_attestation: Time Stamp (id: ABS.4 | len: 26 | use: O | rpt: 1)
        :param attested_by: Extended Composite ID Number and Name for Persons (id: ABS.5 | len: 250 | use: O | rpt: 1)
        :param triage_code: Coded Element (id: ABS.6 | len: 250 | use: O | rpt: 1)
        :param abstract_completion_date_or_time: Time Stamp (id: ABS.7 | len: 26 | use: O | rpt: 1)
        :param abstracted_by: Extended Composite ID Number and Name for Persons (id: ABS.8 | len: 250 | use: O | rpt: 1)
        :param case_category_code: Coded Element (id: ABS.9 | len: 250 | use: O | rpt: 1)
        :param caesarian_section_indicator: Coded values for HL7 tables (id: ABS.10 | len: 1 | use: O | rpt: 1)
        :param gestation_category_code: Coded Element (id: ABS.11 | len: 250 | use: O | rpt: 1)
        :param gestation_period_weeks: Numeric (id: ABS.12 | len: 3 | use: O | rpt: 1)
        :param newborn_code: Coded Element (id: ABS.13 | len: 250 | use: O | rpt: 1)
        :param stillborn_indicator: Coded values for HL7 tables (id: ABS.14 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 14
        self.discharge_care_provider = discharge_care_provider
        self.transfer_medical_service_code = transfer_medical_service_code
        self.severity_of_illness_code = severity_of_illness_code
        self.date_or_time_of_attestation = date_or_time_of_attestation
        self.attested_by = attested_by
        self.triage_code = triage_code
        self.abstract_completion_date_or_time = abstract_completion_date_or_time
        self.abstracted_by = abstracted_by
        self.case_category_code = case_category_code
        self.caesarian_section_indicator = caesarian_section_indicator
        self.gestation_category_code = gestation_category_code
        self.gestation_period_weeks = gestation_period_weeks
        self.newborn_code = newborn_code
        self.stillborn_indicator = stillborn_indicator

    @property  # get ABS.1
    def discharge_care_provider(self) -> PhysicianId | None:
        """
        id: ABS.1 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.1
        """
        return self._c_data[0][0]

    @discharge_care_provider.setter  # set ABS.1
    def discharge_care_provider(self, physician_id: PhysicianId | None):
        """
        id: ABS.1 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.1
        """
        self._c_data[0] = (physician_id,)

    @property  # get ABS.2
    def transfer_medical_service_code(self) -> HospitalService | None:
        """
        id: ABS.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.2
        """
        return self._c_data[1][0]

    @transfer_medical_service_code.setter  # set ABS.2
    def transfer_medical_service_code(self, hospital_service: HospitalService | None):
        """
        id: ABS.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.2
        """
        self._c_data[1] = (hospital_service,)

    @property  # get ABS.3
    def severity_of_illness_code(self) -> SeverityOfIllnessCode | None:
        """
        id: ABS.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.3
        """
        return self._c_data[2][0]

    @severity_of_illness_code.setter  # set ABS.3
    def severity_of_illness_code(
        self, severity_of_illness_code: SeverityOfIllnessCode | None
    ):
        """
        id: ABS.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.3
        """
        self._c_data[2] = (severity_of_illness_code,)

    @property  # get ABS.4
    def date_or_time_of_attestation(self) -> TS | None:
        """
        id: ABS.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.4
        """
        return self._c_data[3][0]

    @date_or_time_of_attestation.setter  # set ABS.4
    def date_or_time_of_attestation(self, ts: TS | None):
        """
        id: ABS.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.4
        """
        self._c_data[3] = (ts,)

    @property  # get ABS.5
    def attested_by(self) -> XCN | None:
        """
        id: ABS.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.5
        """
        return self._c_data[4][0]

    @attested_by.setter  # set ABS.5
    def attested_by(self, xcn: XCN | None):
        """
        id: ABS.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.5
        """
        self._c_data[4] = (xcn,)

    @property  # get ABS.6
    def triage_code(self) -> TriageCode | None:
        """
        id: ABS.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.6
        """
        return self._c_data[5][0]

    @triage_code.setter  # set ABS.6
    def triage_code(self, triage_code: TriageCode | None):
        """
        id: ABS.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.6
        """
        self._c_data[5] = (triage_code,)

    @property  # get ABS.7
    def abstract_completion_date_or_time(self) -> TS | None:
        """
        id: ABS.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.7
        """
        return self._c_data[6][0]

    @abstract_completion_date_or_time.setter  # set ABS.7
    def abstract_completion_date_or_time(self, ts: TS | None):
        """
        id: ABS.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.7
        """
        self._c_data[6] = (ts,)

    @property  # get ABS.8
    def abstracted_by(self) -> XCN | None:
        """
        id: ABS.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.8
        """
        return self._c_data[7][0]

    @abstracted_by.setter  # set ABS.8
    def abstracted_by(self, xcn: XCN | None):
        """
        id: ABS.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.8
        """
        self._c_data[7] = (xcn,)

    @property  # get ABS.9
    def case_category_code(self) -> CaseCategoryCode | None:
        """
        id: ABS.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.9
        """
        return self._c_data[8][0]

    @case_category_code.setter  # set ABS.9
    def case_category_code(self, case_category_code: CaseCategoryCode | None):
        """
        id: ABS.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.9
        """
        self._c_data[8] = (case_category_code,)

    @property  # get ABS.10
    def caesarian_section_indicator(self) -> YesOrNoIndicator | None:
        """
        id: ABS.10 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.10
        """
        return self._c_data[9][0]

    @caesarian_section_indicator.setter  # set ABS.10
    def caesarian_section_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: ABS.10 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.10
        """
        self._c_data[9] = (yes_or_no_indicator,)

    @property  # get ABS.11
    def gestation_category_code(self) -> GestationCategoryCode | None:
        """
        id: ABS.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.11
        """
        return self._c_data[10][0]

    @gestation_category_code.setter  # set ABS.11
    def gestation_category_code(
        self, gestation_category_code: GestationCategoryCode | None
    ):
        """
        id: ABS.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.11
        """
        self._c_data[10] = (gestation_category_code,)

    @property  # get ABS.12
    def gestation_period_weeks(self) -> NM | None:
        """
        id: ABS.12 | len: 3 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.12
        """
        return self._c_data[11][0]

    @gestation_period_weeks.setter  # set ABS.12
    def gestation_period_weeks(self, nm: NM | None):
        """
        id: ABS.12 | len: 3 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.12
        """
        self._c_data[11] = (nm,)

    @property  # get ABS.13
    def newborn_code(self) -> NewbornCode | None:
        """
        id: ABS.13 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.13
        """
        return self._c_data[12][0]

    @newborn_code.setter  # set ABS.13
    def newborn_code(self, newborn_code: NewbornCode | None):
        """
        id: ABS.13 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.13
        """
        self._c_data[12] = (newborn_code,)

    @property  # get ABS.14
    def stillborn_indicator(self) -> YesOrNoIndicator | None:
        """
        id: ABS.14 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.14
        """
        return self._c_data[13][0]

    @stillborn_indicator.setter  # set ABS.14
    def stillborn_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: ABS.14 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ABS.14
        """
        self._c_data[13] = (yes_or_no_indicator,)
