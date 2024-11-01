from __future__ import annotations
from ...base import HL7Segment
from ..data_types.XTN import XTN
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.DT import DT
from ..data_types.CX import CX
from ..data_types.DTN import DTN
from ..data_types.MOP import MOP
from ..data_types.ICD import ICD
from ..data_types.IS import IS
from ..data_types.XCN import XCN
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.ST import ST
from ..tables.CertificationAgency import CertificationAgency
from ..tables.SecondOpinionDocumentationReceived import (
    SecondOpinionDocumentationReceived,
)
from ..tables.NonConcurCodeOrDescription import NonConcurCodeOrDescription
from ..tables.SecondOpinionStatus import SecondOpinionStatus
from ..tables.PhysicianId import PhysicianId
from ..tables.AppealReason import AppealReason
from ..tables.YesOrNoIndicator import YesOrNoIndicator


"""
Insurance Additional Information, Certification - IN3
HL7 Version: 2.5.1

-----BEGIN SEGMENT::IN3 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    IN3,
    XTN, TS, ID, DT, CX, DTN, MOP, ICD, IS, XCN, SI, CE, ST
)

in3 = IN3(  #  - The IN3 segment contains additional insurance information for certifying the need for patient care
    set_id_in3=si,  # SI(...)  # Required.
    certification_number=None,  # CX(...) 
    certified_by=None,  # XCN(...) 
    certification_required=None,  # ID(...) 
    penalty=None,  # MOP(...) 
    certification_date_or_time=None,  # TS(...) 
    certification_modify_date_or_time=None,  # TS(...) 
    operator=None,  # XCN(...) 
    certification_begin_date=None,  # DT(...) 
    certification_end_date=None,  # DT(...) 
    days=None,  # DTN(...) 
    non_concur_code_or_description=None,  # CE(...) 
    non_concur_effective_date_or_time=None,  # TS(...) 
    physician_reviewer=None,  # XCN(...) 
    certification_contact=None,  # ST(...) 
    certification_contact_phone_number=None,  # XTN(...) 
    appeal_reason=None,  # CE(...) 
    certification_agency=None,  # CE(...) 
    certification_agency_phone_number=None,  # XTN(...) 
    pre_certification_requirement=None,  # ICD(...) 
    case_manager=None,  # ST(...) 
    second_opinion_date=None,  # DT(...) 
    second_opinion_status=None,  # IS(...) 
    second_opinion_documentation_received=None,  # IS(...) 
    second_opinion_physician=None,  # XCN(...) 
)

-----END SEGMENT::IN3 TEMPLATE-----
"""


class IN3(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """IN3"""
    _hl7_name = """Insurance Additional Information, Certification"""
    _hl7_description = """The IN3 segment contains additional insurance information for certifying the need for patient care"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN3"
    _c_length = (4, 250, 250, 1, 23, 26, 26, 250, 8, 8, 6, 250, 26, 250, 48, 250, 250, 250, 250, 40, 48, 8, 1, 1, 250,)
    _c_rpt = (1, 1, 65535, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 65535, 1, 65535, 1, 1, 65535, 65535, 1, 1, 1, 65535, 65535,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, CX, XCN, ID, MOP, TS, TS, XCN, DT, DT, DTN, CE, TS, XCN, ST, XTN, CE, CE, XTN, ICD, ST, DT, IS, IS, XCN,)
    _c_aliases = ("IN3.1", "IN3.2", "IN3.3", "IN3.4", "IN3.5", "IN3.6", "IN3.7", "IN3.8", "IN3.9", "IN3.10", "IN3.11", "IN3.12", "IN3.13", "IN3.14", "IN3.15", "IN3.16", "IN3.17", "IN3.18", "IN3.19", "IN3.20", "IN3.21", "IN3.22", "IN3.23", "IN3.24", "IN3.25",)
    _c_names = ("Set ID - IN3", "Certification Number", "Certified By", "Certification Required", "Penalty", "Certification Date/Time", "Certification Modify Date/Time", "Operator", "Certification Begin Date", "Certification End Date", "Days", "Non-Concur Code/Description", "Non-Concur Effective Date/Time", "Physician Reviewer", "Certification Contact", "Certification Contact Phone Number", "Appeal Reason", "Certification Agency", "Certification Agency Phone Number", "Pre-Certification Requirement", "Case Manager", "Second Opinion Date", "Second Opinion Status", "Second Opinion Documentation Received", "Second Opinion Physician",)
    _c_attrs = ("set_id_in3", "certification_number", "certified_by", "certification_required", "penalty", "certification_date_or_time", "certification_modify_date_or_time", "operator", "certification_begin_date", "certification_end_date", "days", "non_concur_code_or_description", "non_concur_effective_date_or_time", "physician_reviewer", "certification_contact", "certification_contact_phone_number", "appeal_reason", "certification_agency", "certification_agency_phone_number", "pre_certification_requirement", "case_manager", "second_opinion_date", "second_opinion_status", "second_opinion_documentation_received", "second_opinion_physician",)
    # fmt: on

    def __init__(
        self,
        set_id_in3: SI | tuple[SI],  # IN3.1
        certification_number: CX | tuple[CX] | None = None,  # IN3.2
        certified_by: XCN | tuple[XCN] | None = None,  # IN3.3
        certification_required: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # IN3.4
        penalty: MOP | tuple[MOP] | None = None,  # IN3.5
        certification_date_or_time: TS | tuple[TS] | None = None,  # IN3.6
        certification_modify_date_or_time: TS | tuple[TS] | None = None,  # IN3.7
        operator: XCN | tuple[XCN] | None = None,  # IN3.8
        certification_begin_date: DT | tuple[DT] | None = None,  # IN3.9
        certification_end_date: DT | tuple[DT] | None = None,  # IN3.10
        days: DTN | tuple[DTN] | None = None,  # IN3.11
        non_concur_code_or_description: NonConcurCodeOrDescription
        | CE
        | tuple[NonConcurCodeOrDescription | CE]
        | None = None,  # IN3.12
        non_concur_effective_date_or_time: TS | tuple[TS] | None = None,  # IN3.13
        physician_reviewer: PhysicianId
        | XCN
        | tuple[PhysicianId | XCN]
        | None = None,  # IN3.14
        certification_contact: ST | tuple[ST] | None = None,  # IN3.15
        certification_contact_phone_number: XTN | tuple[XTN] | None = None,  # IN3.16
        appeal_reason: AppealReason
        | CE
        | tuple[AppealReason | CE]
        | None = None,  # IN3.17
        certification_agency: CertificationAgency
        | CE
        | tuple[CertificationAgency | CE]
        | None = None,  # IN3.18
        certification_agency_phone_number: XTN | tuple[XTN] | None = None,  # IN3.19
        pre_certification_requirement: ICD | tuple[ICD] | None = None,  # IN3.20
        case_manager: ST | tuple[ST] | None = None,  # IN3.21
        second_opinion_date: DT | tuple[DT] | None = None,  # IN3.22
        second_opinion_status: SecondOpinionStatus
        | IS
        | tuple[SecondOpinionStatus | IS]
        | None = None,  # IN3.23
        second_opinion_documentation_received: SecondOpinionDocumentationReceived
        | IS
        | tuple[SecondOpinionDocumentationReceived | IS]
        | None = None,  # IN3.24
        second_opinion_physician: PhysicianId
        | XCN
        | tuple[PhysicianId | XCN]
        | None = None,  # IN3.25
    ):
        """
        Insurance Additional Information, Certification - `IN3 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN3>`_
        The IN3 segment contains additional insurance information for certifying the need for patient care. Fields used by this segment are defined by CMS, or other regulatory agencies.

        :param set_id_in3: Sequence ID (id: IN3.1 | len: 4 | use: R | rpt: 1)
        :param certification_number: Extended Composite ID with Check Digit (id: IN3.2 | len: 250 | use: O | rpt: 1)
        :param certified_by: Extended Composite ID Number and Name for Persons (id: IN3.3 | len: 250 | use: O | rpt: *)
        :param certification_required: Coded values for HL7 tables (id: IN3.4 | len: 1 | use: O | rpt: 1)
        :param penalty: Money or Percentage (id: IN3.5 | len: 23 | use: O | rpt: 1)
        :param certification_date_or_time: Time Stamp (id: IN3.6 | len: 26 | use: O | rpt: 1)
        :param certification_modify_date_or_time: Time Stamp (id: IN3.7 | len: 26 | use: O | rpt: 1)
        :param operator: Extended Composite ID Number and Name for Persons (id: IN3.8 | len: 250 | use: O | rpt: *)
        :param certification_begin_date: Date (id: IN3.9 | len: 8 | use: O | rpt: 1)
        :param certification_end_date: Date (id: IN3.10 | len: 8 | use: O | rpt: 1)
        :param days: Day Type and Number (id: IN3.11 | len: 6 | use: O | rpt: 1)
        :param non_concur_code_or_description: Coded Element (id: IN3.12 | len: 250 | use: O | rpt: 1)
        :param non_concur_effective_date_or_time: Time Stamp (id: IN3.13 | len: 26 | use: O | rpt: 1)
        :param physician_reviewer: Extended Composite ID Number and Name for Persons (id: IN3.14 | len: 250 | use: O | rpt: *)
        :param certification_contact: String Data (id: IN3.15 | len: 48 | use: O | rpt: 1)
        :param certification_contact_phone_number: Extended Telecommunication Number (id: IN3.16 | len: 250 | use: O | rpt: *)
        :param appeal_reason: Coded Element (id: IN3.17 | len: 250 | use: O | rpt: 1)
        :param certification_agency: Coded Element (id: IN3.18 | len: 250 | use: O | rpt: 1)
        :param certification_agency_phone_number: Extended Telecommunication Number (id: IN3.19 | len: 250 | use: O | rpt: *)
        :param pre_certification_requirement: Insurance Certification Definition (id: IN3.20 | len: 40 | use: O | rpt: *)
        :param case_manager: String Data (id: IN3.21 | len: 48 | use: O | rpt: 1)
        :param second_opinion_date: Date (id: IN3.22 | len: 8 | use: O | rpt: 1)
        :param second_opinion_status: Coded value for user-defined tables (id: IN3.23 | len: 1 | use: O | rpt: 1)
        :param second_opinion_documentation_received: Coded value for user-defined tables (id: IN3.24 | len: 1 | use: O | rpt: *)
        :param second_opinion_physician: Extended Composite ID Number and Name for Persons (id: IN3.25 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 25
        self.set_id_in3 = set_id_in3
        self.certification_number = certification_number
        self.certified_by = certified_by
        self.certification_required = certification_required
        self.penalty = penalty
        self.certification_date_or_time = certification_date_or_time
        self.certification_modify_date_or_time = certification_modify_date_or_time
        self.operator = operator
        self.certification_begin_date = certification_begin_date
        self.certification_end_date = certification_end_date
        self.days = days
        self.non_concur_code_or_description = non_concur_code_or_description
        self.non_concur_effective_date_or_time = non_concur_effective_date_or_time
        self.physician_reviewer = physician_reviewer
        self.certification_contact = certification_contact
        self.certification_contact_phone_number = certification_contact_phone_number
        self.appeal_reason = appeal_reason
        self.certification_agency = certification_agency
        self.certification_agency_phone_number = certification_agency_phone_number
        self.pre_certification_requirement = pre_certification_requirement
        self.case_manager = case_manager
        self.second_opinion_date = second_opinion_date
        self.second_opinion_status = second_opinion_status
        self.second_opinion_documentation_received = (
            second_opinion_documentation_received
        )
        self.second_opinion_physician = second_opinion_physician

    @property  # get IN3.1
    def set_id_in3(self) -> SI:
        """
        id: IN3.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.1
        """
        return self._c_data[0][0]

    @set_id_in3.setter  # set IN3.1
    def set_id_in3(self, si: SI):
        """
        id: IN3.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.1
        """
        self._c_data[0] = (si,)

    @property  # get IN3.2
    def certification_number(self) -> CX | None:
        """
        id: IN3.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.2
        """
        return self._c_data[1][0]

    @certification_number.setter  # set IN3.2
    def certification_number(self, cx: CX | None):
        """
        id: IN3.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.2
        """
        self._c_data[1] = (cx,)

    @property
    def certified_by(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: IN3.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.3
        """
        return self._c_data[2]

    @certified_by.setter  # set IN3.3
    def certified_by(self, xcn: XCN | tuple[XCN] | None):
        """
        id: IN3.3 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.3
        """
        if isinstance(xcn, tuple):
            self._c_data[2] = xcn
        else:
            self._c_data[2] = (xcn,)

    @property  # get IN3.4
    def certification_required(self) -> YesOrNoIndicator | None:
        """
        id: IN3.4 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.4
        """
        return self._c_data[3][0]

    @certification_required.setter  # set IN3.4
    def certification_required(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: IN3.4 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.4
        """
        self._c_data[3] = (yes_or_no_indicator,)

    @property  # get IN3.5
    def penalty(self) -> MOP | None:
        """
        id: IN3.5 | len: 23 | use: O | rpt: 1
        ---
        return_type: MOP: Money or Percentage
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.5
        """
        return self._c_data[4][0]

    @penalty.setter  # set IN3.5
    def penalty(self, mop: MOP | None):
        """
        id: IN3.5 | len: 23 | use: O | rpt: 1
        ---
        param_type: MOP: Money or Percentage
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.5
        """
        self._c_data[4] = (mop,)

    @property  # get IN3.6
    def certification_date_or_time(self) -> TS | None:
        """
        id: IN3.6 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.6
        """
        return self._c_data[5][0]

    @certification_date_or_time.setter  # set IN3.6
    def certification_date_or_time(self, ts: TS | None):
        """
        id: IN3.6 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.6
        """
        self._c_data[5] = (ts,)

    @property  # get IN3.7
    def certification_modify_date_or_time(self) -> TS | None:
        """
        id: IN3.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.7
        """
        return self._c_data[6][0]

    @certification_modify_date_or_time.setter  # set IN3.7
    def certification_modify_date_or_time(self, ts: TS | None):
        """
        id: IN3.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.7
        """
        self._c_data[6] = (ts,)

    @property
    def operator(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: IN3.8 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.8
        """
        return self._c_data[7]

    @operator.setter  # set IN3.8
    def operator(self, xcn: XCN | tuple[XCN] | None):
        """
        id: IN3.8 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.8
        """
        if isinstance(xcn, tuple):
            self._c_data[7] = xcn
        else:
            self._c_data[7] = (xcn,)

    @property  # get IN3.9
    def certification_begin_date(self) -> DT | None:
        """
        id: IN3.9 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.9
        """
        return self._c_data[8][0]

    @certification_begin_date.setter  # set IN3.9
    def certification_begin_date(self, dt: DT | None):
        """
        id: IN3.9 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.9
        """
        self._c_data[8] = (dt,)

    @property  # get IN3.10
    def certification_end_date(self) -> DT | None:
        """
        id: IN3.10 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.10
        """
        return self._c_data[9][0]

    @certification_end_date.setter  # set IN3.10
    def certification_end_date(self, dt: DT | None):
        """
        id: IN3.10 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.10
        """
        self._c_data[9] = (dt,)

    @property  # get IN3.11
    def days(self) -> DTN | None:
        """
        id: IN3.11 | len: 6 | use: O | rpt: 1
        ---
        return_type: DTN: Day Type and Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.11
        """
        return self._c_data[10][0]

    @days.setter  # set IN3.11
    def days(self, dtn: DTN | None):
        """
        id: IN3.11 | len: 6 | use: O | rpt: 1
        ---
        param_type: DTN: Day Type and Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.11
        """
        self._c_data[10] = (dtn,)

    @property  # get IN3.12
    def non_concur_code_or_description(self) -> NonConcurCodeOrDescription | None:
        """
        id: IN3.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.12
        """
        return self._c_data[11][0]

    @non_concur_code_or_description.setter  # set IN3.12
    def non_concur_code_or_description(
        self, nonconcur_code_or_description: NonConcurCodeOrDescription | None
    ):
        """
        id: IN3.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.12
        """
        self._c_data[11] = (nonconcur_code_or_description,)

    @property  # get IN3.13
    def non_concur_effective_date_or_time(self) -> TS | None:
        """
        id: IN3.13 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.13
        """
        return self._c_data[12][0]

    @non_concur_effective_date_or_time.setter  # set IN3.13
    def non_concur_effective_date_or_time(self, ts: TS | None):
        """
        id: IN3.13 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.13
        """
        self._c_data[12] = (ts,)

    @property
    def physician_reviewer(self) -> tuple[PhysicianId, ...] | tuple[None]:
        """
        id: IN3.14 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.14
        """
        return self._c_data[13]

    @physician_reviewer.setter  # set IN3.14
    def physician_reviewer(self, physician_id: PhysicianId | tuple[PhysicianId] | None):
        """
        id: IN3.14 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.14
        """
        if isinstance(physician_id, tuple):
            self._c_data[13] = physician_id
        else:
            self._c_data[13] = (physician_id,)

    @property  # get IN3.15
    def certification_contact(self) -> ST | None:
        """
        id: IN3.15 | len: 48 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.15
        """
        return self._c_data[14][0]

    @certification_contact.setter  # set IN3.15
    def certification_contact(self, st: ST | None):
        """
        id: IN3.15 | len: 48 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.15
        """
        self._c_data[14] = (st,)

    @property
    def certification_contact_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: IN3.16 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.16
        """
        return self._c_data[15]

    @certification_contact_phone_number.setter  # set IN3.16
    def certification_contact_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: IN3.16 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.16
        """
        if isinstance(xtn, tuple):
            self._c_data[15] = xtn
        else:
            self._c_data[15] = (xtn,)

    @property  # get IN3.17
    def appeal_reason(self) -> AppealReason | None:
        """
        id: IN3.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.17
        """
        return self._c_data[16][0]

    @appeal_reason.setter  # set IN3.17
    def appeal_reason(self, appeal_reason: AppealReason | None):
        """
        id: IN3.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.17
        """
        self._c_data[16] = (appeal_reason,)

    @property  # get IN3.18
    def certification_agency(self) -> CertificationAgency | None:
        """
        id: IN3.18 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.18
        """
        return self._c_data[17][0]

    @certification_agency.setter  # set IN3.18
    def certification_agency(self, certification_agency: CertificationAgency | None):
        """
        id: IN3.18 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.18
        """
        self._c_data[17] = (certification_agency,)

    @property
    def certification_agency_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: IN3.19 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.19
        """
        return self._c_data[18]

    @certification_agency_phone_number.setter  # set IN3.19
    def certification_agency_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: IN3.19 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.19
        """
        if isinstance(xtn, tuple):
            self._c_data[18] = xtn
        else:
            self._c_data[18] = (xtn,)

    @property
    def pre_certification_requirement(self) -> tuple[ICD, ...] | tuple[None]:
        """
        id: IN3.20 | len: 40 | use: O | rpt: *
        ---
        return_type: tuple[ICD, ...]: (Insurance Certification Definition, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.20
        """
        return self._c_data[19]

    @pre_certification_requirement.setter  # set IN3.20
    def pre_certification_requirement(self, icd: ICD | tuple[ICD] | None):
        """
        id: IN3.20 | len: 40 | use: O | rpt: *
        ---
        param_type: ICD | tuple[ICD, ...]: (Insurance Certification Definition, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.20
        """
        if isinstance(icd, tuple):
            self._c_data[19] = icd
        else:
            self._c_data[19] = (icd,)

    @property  # get IN3.21
    def case_manager(self) -> ST | None:
        """
        id: IN3.21 | len: 48 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.21
        """
        return self._c_data[20][0]

    @case_manager.setter  # set IN3.21
    def case_manager(self, st: ST | None):
        """
        id: IN3.21 | len: 48 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.21
        """
        self._c_data[20] = (st,)

    @property  # get IN3.22
    def second_opinion_date(self) -> DT | None:
        """
        id: IN3.22 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.22
        """
        return self._c_data[21][0]

    @second_opinion_date.setter  # set IN3.22
    def second_opinion_date(self, dt: DT | None):
        """
        id: IN3.22 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.22
        """
        self._c_data[21] = (dt,)

    @property  # get IN3.23
    def second_opinion_status(self) -> SecondOpinionStatus | None:
        """
        id: IN3.23 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.23
        """
        return self._c_data[22][0]

    @second_opinion_status.setter  # set IN3.23
    def second_opinion_status(self, second_opinion_status: SecondOpinionStatus | None):
        """
        id: IN3.23 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.23
        """
        self._c_data[22] = (second_opinion_status,)

    @property
    def second_opinion_documentation_received(
        self,
    ) -> tuple[SecondOpinionDocumentationReceived, ...] | tuple[None]:
        """
        id: IN3.24 | len: 1 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.24
        """
        return self._c_data[23]

    @second_opinion_documentation_received.setter  # set IN3.24
    def second_opinion_documentation_received(
        self,
        second_opinion_documentation_received: SecondOpinionDocumentationReceived
        | tuple[SecondOpinionDocumentationReceived]
        | None,
    ):
        """
        id: IN3.24 | len: 1 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.24
        """
        if isinstance(second_opinion_documentation_received, tuple):
            self._c_data[23] = second_opinion_documentation_received
        else:
            self._c_data[23] = (second_opinion_documentation_received,)

    @property
    def second_opinion_physician(self) -> tuple[PhysicianId, ...] | tuple[None]:
        """
        id: IN3.25 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.25
        """
        return self._c_data[24]

    @second_opinion_physician.setter  # set IN3.25
    def second_opinion_physician(
        self, physician_id: PhysicianId | tuple[PhysicianId] | None
    ):
        """
        id: IN3.25 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN3.25
        """
        if isinstance(physician_id, tuple):
            self._c_data[24] = physician_id
        else:
            self._c_data[24] = (physician_id,)
