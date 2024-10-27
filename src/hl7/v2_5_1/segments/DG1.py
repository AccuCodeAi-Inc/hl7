from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.ST import ST
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..data_types.EI import EI
from ..data_types.IS import IS
from ..data_types.XCN import XCN
from ..data_types.CP import CP
from ..tables.DiagnosisCode import DiagnosisCode
from ..tables.DiagnosisClassification import DiagnosisClassification
from ..tables.SegmentActionCode import SegmentActionCode
from ..tables.DrgGrouperReviewCode import DrgGrouperReviewCode
from ..tables.DiagnosisRelatedGroup import DiagnosisRelatedGroup
from ..tables.DiagnosisType import DiagnosisType
from ..tables.DiagnosisCodingMethod import DiagnosisCodingMethod
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.DiagnosisPriority import DiagnosisPriority
from ..tables.MajorDiagnosticCategory import MajorDiagnosticCategory
from ..tables.OutlierType import OutlierType


"""
Diagnosis - DG1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::DG1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DG1,
    ID, TS, ST, SI, CE, NM, EI, IS, XCN, CP
)

dg1 = DG1(  #  - The DG1 segment contains patient diagnosis information of various types, for example, admitting, primary, etc
    set_id_dg1=si,  # SI(...)  # Required.
    diagnosis_coding_method=None,  # ID(...) 
    diagnosis_code_dg1=None,  # CE(...) 
    diagnosis_description=None,  # ST(...) 
    diagnosis_date_or_time=None,  # TS(...) 
    diagnosis_type=_is,  # IS(...)  # Required.
    major_diagnostic_category=None,  # CE(...) 
    diagnostic_related_group=None,  # CE(...) 
    drg_approval_indicator=None,  # ID(...) 
    drg_grouper_review_code=None,  # IS(...) 
    outlier_type=None,  # CE(...) 
    outlier_days=None,  # NM(...) 
    outlier_cost=None,  # CP(...) 
    grouper_version_and_type=None,  # ST(...) 
    diagnosis_priority=None,  # ID(...) 
    diagnosing_clinician=None,  # XCN(...) 
    diagnosis_classification=None,  # IS(...) 
    confidential_indicator=None,  # ID(...) 
    attestation_date_or_time=None,  # TS(...) 
    diagnosis_identifier=None,  # EI(...) 
    diagnosis_action_code=None,  # ID(...) 
)

-----END SEGMENT::DG1 TEMPLATE-----
"""


class DG1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """DG1"""
    _hl7_name = """Diagnosis"""
    _hl7_description = """The DG1 segment contains patient diagnosis information of various types, for example, admitting, primary, etc"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1"
    _c_length = (4, 2, 250, 40, 26, 2, 250, 250, 1, 2, 250, 3, 12, 4, 2, 250, 3, 1, 26, 427, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "B", "O", "B", "O", "R", "B", "B", "B", "B", "B", "B", "B", "B", "O", "O", "O", "O", "O", "C", "C",)
    _c_components = (SI, ID, CE, ST, TS, IS, CE, CE, ID, IS, CE, NM, CP, ST, ID, XCN, IS, ID, TS, EI, ID,)
    _c_aliases = ("DG1.1", "DG1.2", "DG1.3", "DG1.4", "DG1.5", "DG1.6", "DG1.7", "DG1.8", "DG1.9", "DG1.10", "DG1.11", "DG1.12", "DG1.13", "DG1.14", "DG1.15", "DG1.16", "DG1.17", "DG1.18", "DG1.19", "DG1.20", "DG1.21",)
    _c_names = ("Set ID - DG1", "Diagnosis Coding Method", "Diagnosis Code - DG1", "Diagnosis Description", "Diagnosis Date/Time", "Diagnosis Type", "Major Diagnostic Category", "Diagnostic Related Group", "DRG Approval Indicator", "DRG Grouper Review Code", "Outlier Type", "Outlier Days", "Outlier Cost", "Grouper Version And Type", "Diagnosis Priority", "Diagnosing Clinician", "Diagnosis Classification", "Confidential Indicator", "Attestation Date/Time", "Diagnosis Identifier", "Diagnosis Action Code",)
    _c_attrs = ("set_id_dg1", "diagnosis_coding_method", "diagnosis_code_dg1", "diagnosis_description", "diagnosis_date_or_time", "diagnosis_type", "major_diagnostic_category", "diagnostic_related_group", "drg_approval_indicator", "drg_grouper_review_code", "outlier_type", "outlier_days", "outlier_cost", "grouper_version_and_type", "diagnosis_priority", "diagnosing_clinician", "diagnosis_classification", "confidential_indicator", "attestation_date_or_time", "diagnosis_identifier", "diagnosis_action_code",)
    # fmt: on

    def __init__(
        self,
        set_id_dg1: SI,  # DG1.1
        diagnosis_type: DiagnosisType | IS,  # DG1.6
        diagnosis_coding_method: DiagnosisCodingMethod | ID | None = None,  # DG1.2
        diagnosis_code_dg1: DiagnosisCode | CE | None = None,  # DG1.3
        diagnosis_description: ST | None = None,  # DG1.4
        diagnosis_date_or_time: TS | None = None,  # DG1.5
        major_diagnostic_category: MajorDiagnosticCategory | CE | None = None,  # DG1.7
        diagnostic_related_group: DiagnosisRelatedGroup | CE | None = None,  # DG1.8
        drg_approval_indicator: YesOrNoIndicator | ID | None = None,  # DG1.9
        drg_grouper_review_code: DrgGrouperReviewCode | IS | None = None,  # DG1.10
        outlier_type: OutlierType | CE | None = None,  # DG1.11
        outlier_days: NM | None = None,  # DG1.12
        outlier_cost: CP | None = None,  # DG1.13
        grouper_version_and_type: ST | None = None,  # DG1.14
        diagnosis_priority: DiagnosisPriority | ID | None = None,  # DG1.15
        diagnosing_clinician: XCN | None = None,  # DG1.16
        diagnosis_classification: DiagnosisClassification | IS | None = None,  # DG1.17
        confidential_indicator: YesOrNoIndicator | ID | None = None,  # DG1.18
        attestation_date_or_time: TS | None = None,  # DG1.19
        diagnosis_identifier: EI | None = None,  # DG1.20
        diagnosis_action_code: SegmentActionCode | ID | None = None,  # DG1.21
    ):
        """
        Diagnosis - `DG1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1>`_
        The DG1 segment contains patient diagnosis information of various types, for example, admitting, primary, etc. The DG1 segment is used to send multiple diagnoses (for example, for medical records encoding). It is also used when the FT1-19 - Diagnosis Code - FT1 does not provide sufficient information for a billing system. This diagnosis coding should be distinguished from the clinical problem segment used by caregivers to manage the patient (see Chapter 12, Patient Care). Coding methodologies are also defined.

        :param set_id_dg1: Sequence ID (id: DG1.1 | len: 4 | use: R | rpt: 1)
        :param diagnosis_coding_method: Coded values for HL7 tables (id: DG1.2 | len: 2 | use: B | rpt: 1)
        :param diagnosis_code_dg1: Coded Element (id: DG1.3 | len: 250 | use: O | rpt: 1)
        :param diagnosis_description: String Data (id: DG1.4 | len: 40 | use: B | rpt: 1)
        :param diagnosis_date_or_time: Time Stamp (id: DG1.5 | len: 26 | use: O | rpt: 1)
        :param diagnosis_type: Coded value for user-defined tables (id: DG1.6 | len: 2 | use: R | rpt: 1)
        :param major_diagnostic_category: Coded Element (id: DG1.7 | len: 250 | use: B | rpt: 1)
        :param diagnostic_related_group: Coded Element (id: DG1.8 | len: 250 | use: B | rpt: 1)
        :param drg_approval_indicator: Coded values for HL7 tables (id: DG1.9 | len: 1 | use: B | rpt: 1)
        :param drg_grouper_review_code: Coded value for user-defined tables (id: DG1.10 | len: 2 | use: B | rpt: 1)
        :param outlier_type: Coded Element (id: DG1.11 | len: 250 | use: B | rpt: 1)
        :param outlier_days: Numeric (id: DG1.12 | len: 3 | use: B | rpt: 1)
        :param outlier_cost: Composite Price (id: DG1.13 | len: 12 | use: B | rpt: 1)
        :param grouper_version_and_type: String Data (id: DG1.14 | len: 4 | use: B | rpt: 1)
        :param diagnosis_priority: Coded values for HL7 tables (id: DG1.15 | len: 2 | use: O | rpt: 1)
        :param diagnosing_clinician: Extended Composite ID Number and Name for Persons (id: DG1.16 | len: 250 | use: O | rpt: *)
        :param diagnosis_classification: Coded value for user-defined tables (id: DG1.17 | len: 3 | use: O | rpt: 1)
        :param confidential_indicator: Coded values for HL7 tables (id: DG1.18 | len: 1 | use: O | rpt: 1)
        :param attestation_date_or_time: Time Stamp (id: DG1.19 | len: 26 | use: O | rpt: 1)
        :param diagnosis_identifier: Entity Identifier (id: DG1.20 | len: 427 | use: C | rpt: 1)
        :param diagnosis_action_code: Coded values for HL7 tables (id: DG1.21 | len: 1 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 21
        self.set_id_dg1 = set_id_dg1
        self.diagnosis_coding_method = diagnosis_coding_method
        self.diagnosis_code_dg1 = diagnosis_code_dg1
        self.diagnosis_description = diagnosis_description
        self.diagnosis_date_or_time = diagnosis_date_or_time
        self.diagnosis_type = diagnosis_type
        self.major_diagnostic_category = major_diagnostic_category
        self.diagnostic_related_group = diagnostic_related_group
        self.drg_approval_indicator = drg_approval_indicator
        self.drg_grouper_review_code = drg_grouper_review_code
        self.outlier_type = outlier_type
        self.outlier_days = outlier_days
        self.outlier_cost = outlier_cost
        self.grouper_version_and_type = grouper_version_and_type
        self.diagnosis_priority = diagnosis_priority
        self.diagnosing_clinician = diagnosing_clinician
        self.diagnosis_classification = diagnosis_classification
        self.confidential_indicator = confidential_indicator
        self.attestation_date_or_time = attestation_date_or_time
        self.diagnosis_identifier = diagnosis_identifier
        self.diagnosis_action_code = diagnosis_action_code

    @property  # get DG1.1
    def set_id_dg1(self) -> SI:
        """
        id: DG1.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.1
        """
        return self._c_data[0][0]

    @set_id_dg1.setter  # set DG1.1
    def set_id_dg1(self, si: SI):
        """
        id: DG1.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.1
        """
        self._c_data[0] = (si,)

    @property  # get DG1.2
    def diagnosis_coding_method(self) -> DiagnosisCodingMethod | None:
        """
        id: DG1.2 | len: 2 | use: B | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.2
        """
        return self._c_data[1][0]

    @diagnosis_coding_method.setter  # set DG1.2
    def diagnosis_coding_method(
        self, diagnosis_coding_method: DiagnosisCodingMethod | None
    ):
        """
        id: DG1.2 | len: 2 | use: B | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.2
        """
        self._c_data[1] = (diagnosis_coding_method,)

    @property  # get DG1.3
    def diagnosis_code_dg1(self) -> DiagnosisCode | None:
        """
        id: DG1.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.3
        """
        return self._c_data[2][0]

    @diagnosis_code_dg1.setter  # set DG1.3
    def diagnosis_code_dg1(self, diagnosis_code: DiagnosisCode | None):
        """
        id: DG1.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.3
        """
        self._c_data[2] = (diagnosis_code,)

    @property  # get DG1.4
    def diagnosis_description(self) -> ST | None:
        """
        id: DG1.4 | len: 40 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.4
        """
        return self._c_data[3][0]

    @diagnosis_description.setter  # set DG1.4
    def diagnosis_description(self, st: ST | None):
        """
        id: DG1.4 | len: 40 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.4
        """
        self._c_data[3] = (st,)

    @property  # get DG1.5
    def diagnosis_date_or_time(self) -> TS | None:
        """
        id: DG1.5 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.5
        """
        return self._c_data[4][0]

    @diagnosis_date_or_time.setter  # set DG1.5
    def diagnosis_date_or_time(self, ts: TS | None):
        """
        id: DG1.5 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.5
        """
        self._c_data[4] = (ts,)

    @property  # get DG1.6
    def diagnosis_type(self) -> DiagnosisType:
        """
        id: DG1.6 | len: 2 | use: R | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.6
        """
        return self._c_data[5][0]

    @diagnosis_type.setter  # set DG1.6
    def diagnosis_type(self, diagnosis_type: DiagnosisType):
        """
        id: DG1.6 | len: 2 | use: R | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.6
        """
        self._c_data[5] = (diagnosis_type,)

    @property  # get DG1.7
    def major_diagnostic_category(self) -> MajorDiagnosticCategory | None:
        """
        id: DG1.7 | len: 250 | use: B | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.7
        """
        return self._c_data[6][0]

    @major_diagnostic_category.setter  # set DG1.7
    def major_diagnostic_category(
        self, major_diagnostic_category: MajorDiagnosticCategory | None
    ):
        """
        id: DG1.7 | len: 250 | use: B | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.7
        """
        self._c_data[6] = (major_diagnostic_category,)

    @property  # get DG1.8
    def diagnostic_related_group(self) -> DiagnosisRelatedGroup | None:
        """
        id: DG1.8 | len: 250 | use: B | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.8
        """
        return self._c_data[7][0]

    @diagnostic_related_group.setter  # set DG1.8
    def diagnostic_related_group(
        self, diagnosis_related_group: DiagnosisRelatedGroup | None
    ):
        """
        id: DG1.8 | len: 250 | use: B | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.8
        """
        self._c_data[7] = (diagnosis_related_group,)

    @property  # get DG1.9
    def drg_approval_indicator(self) -> YesOrNoIndicator | None:
        """
        id: DG1.9 | len: 1 | use: B | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.9
        """
        return self._c_data[8][0]

    @drg_approval_indicator.setter  # set DG1.9
    def drg_approval_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: DG1.9 | len: 1 | use: B | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.9
        """
        self._c_data[8] = (yes_or_no_indicator,)

    @property  # get DG1.10
    def drg_grouper_review_code(self) -> DrgGrouperReviewCode | None:
        """
        id: DG1.10 | len: 2 | use: B | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.10
        """
        return self._c_data[9][0]

    @drg_grouper_review_code.setter  # set DG1.10
    def drg_grouper_review_code(
        self, drg_grouper_review_code: DrgGrouperReviewCode | None
    ):
        """
        id: DG1.10 | len: 2 | use: B | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.10
        """
        self._c_data[9] = (drg_grouper_review_code,)

    @property  # get DG1.11
    def outlier_type(self) -> OutlierType | None:
        """
        id: DG1.11 | len: 250 | use: B | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.11
        """
        return self._c_data[10][0]

    @outlier_type.setter  # set DG1.11
    def outlier_type(self, outlier_type: OutlierType | None):
        """
        id: DG1.11 | len: 250 | use: B | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.11
        """
        self._c_data[10] = (outlier_type,)

    @property  # get DG1.12
    def outlier_days(self) -> NM | None:
        """
        id: DG1.12 | len: 3 | use: B | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.12
        """
        return self._c_data[11][0]

    @outlier_days.setter  # set DG1.12
    def outlier_days(self, nm: NM | None):
        """
        id: DG1.12 | len: 3 | use: B | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.12
        """
        self._c_data[11] = (nm,)

    @property  # get DG1.13
    def outlier_cost(self) -> CP | None:
        """
        id: DG1.13 | len: 12 | use: B | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.13
        """
        return self._c_data[12][0]

    @outlier_cost.setter  # set DG1.13
    def outlier_cost(self, cp: CP | None):
        """
        id: DG1.13 | len: 12 | use: B | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.13
        """
        self._c_data[12] = (cp,)

    @property  # get DG1.14
    def grouper_version_and_type(self) -> ST | None:
        """
        id: DG1.14 | len: 4 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.14
        """
        return self._c_data[13][0]

    @grouper_version_and_type.setter  # set DG1.14
    def grouper_version_and_type(self, st: ST | None):
        """
        id: DG1.14 | len: 4 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.14
        """
        self._c_data[13] = (st,)

    @property  # get DG1.15
    def diagnosis_priority(self) -> DiagnosisPriority | None:
        """
        id: DG1.15 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.15
        """
        return self._c_data[14][0]

    @diagnosis_priority.setter  # set DG1.15
    def diagnosis_priority(self, diagnosis_priority: DiagnosisPriority | None):
        """
        id: DG1.15 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.15
        """
        self._c_data[14] = (diagnosis_priority,)

    @property
    def diagnosing_clinician(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: DG1.16 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.16
        """
        return self._c_data[15]

    @diagnosing_clinician.setter  # set DG1.16
    def diagnosing_clinician(self, xcn: XCN | tuple[XCN] | None):
        """
        id: DG1.16 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.16
        """
        if isinstance(xcn, tuple):
            self._c_data[15] = xcn
        else:
            self._c_data[15] = (xcn,)

    @property  # get DG1.17
    def diagnosis_classification(self) -> DiagnosisClassification | None:
        """
        id: DG1.17 | len: 3 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.17
        """
        return self._c_data[16][0]

    @diagnosis_classification.setter  # set DG1.17
    def diagnosis_classification(
        self, diagnosis_classification: DiagnosisClassification | None
    ):
        """
        id: DG1.17 | len: 3 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.17
        """
        self._c_data[16] = (diagnosis_classification,)

    @property  # get DG1.18
    def confidential_indicator(self) -> YesOrNoIndicator | None:
        """
        id: DG1.18 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.18
        """
        return self._c_data[17][0]

    @confidential_indicator.setter  # set DG1.18
    def confidential_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: DG1.18 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.18
        """
        self._c_data[17] = (yes_or_no_indicator,)

    @property  # get DG1.19
    def attestation_date_or_time(self) -> TS | None:
        """
        id: DG1.19 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.19
        """
        return self._c_data[18][0]

    @attestation_date_or_time.setter  # set DG1.19
    def attestation_date_or_time(self, ts: TS | None):
        """
        id: DG1.19 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.19
        """
        self._c_data[18] = (ts,)

    @property  # get DG1.20
    def diagnosis_identifier(self) -> EI | None:
        """
        id: DG1.20 | len: 427 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.20
        """
        return self._c_data[19][0]

    @diagnosis_identifier.setter  # set DG1.20
    def diagnosis_identifier(self, ei: EI | None):
        """
        id: DG1.20 | len: 427 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.20
        """
        self._c_data[19] = (ei,)

    @property  # get DG1.21
    def diagnosis_action_code(self) -> SegmentActionCode | None:
        """
        id: DG1.21 | len: 1 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.21
        """
        return self._c_data[20][0]

    @diagnosis_action_code.setter  # set DG1.21
    def diagnosis_action_code(self, segment_action_code: SegmentActionCode | None):
        """
        id: DG1.21 | len: 1 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DG1.21
        """
        self._c_data[20] = (segment_action_code,)
