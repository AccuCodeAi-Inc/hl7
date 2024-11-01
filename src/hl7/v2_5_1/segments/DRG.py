from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TS import TS
from ..data_types.IS import IS
from ..data_types.NM import NM
from ..data_types.CP import CP
from ..data_types.ID import ID
from ..tables.DrgTransferType import DrgTransferType
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.DiagnosisRelatedGroup import DiagnosisRelatedGroup
from ..tables.OutlierType import OutlierType
from ..tables.DrgGrouperReviewCode import DrgGrouperReviewCode
from ..tables.DrgPayor import DrgPayor


"""
Diagnosis Related Group - DRG
HL7 Version: 2.5.1

-----BEGIN SEGMENT::DRG TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DRG,
    CE, TS, IS, NM, CP, ID
)

drg = DRG(  #  - The DRG segment contains diagnoses-related grouping information of various types
    diagnostic_related_group=None,  # CE(...) 
    drg_assigned_date_or_time=None,  # TS(...) 
    drg_approval_indicator=None,  # ID(...) 
    drg_grouper_review_code=None,  # IS(...) 
    outlier_type=None,  # CE(...) 
    outlier_days=None,  # NM(...) 
    outlier_cost=None,  # CP(...) 
    drg_payor=None,  # IS(...) 
    outlier_reimbursement=None,  # CP(...) 
    confidential_indicator=None,  # ID(...) 
    drg_transfer_type=None,  # IS(...) 
)

-----END SEGMENT::DRG TEMPLATE-----
"""


class DRG(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """DRG"""
    _hl7_name = """Diagnosis Related Group"""
    _hl7_description = """The DRG segment contains diagnoses-related grouping information of various types"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG"
    _c_length = (250, 26, 1, 2, 250, 3, 12, 1, 9, 1, 21,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, TS, ID, IS, CE, NM, CP, IS, CP, ID, IS,)
    _c_aliases = ("DRG.1", "DRG.2", "DRG.3", "DRG.4", "DRG.5", "DRG.6", "DRG.7", "DRG.8", "DRG.9", "DRG.10", "DRG.11",)
    _c_names = ("Diagnostic Related Group", "DRG Assigned Date/Time", "DRG Approval Indicator", "DRG Grouper Review Code", "Outlier Type", "Outlier Days", "Outlier Cost", "DRG Payor", "Outlier Reimbursement", "Confidential Indicator", "DRG Transfer Type",)
    _c_attrs = ("diagnostic_related_group", "drg_assigned_date_or_time", "drg_approval_indicator", "drg_grouper_review_code", "outlier_type", "outlier_days", "outlier_cost", "drg_payor", "outlier_reimbursement", "confidential_indicator", "drg_transfer_type",)
    # fmt: on

    def __init__(
        self,
        diagnostic_related_group: DiagnosisRelatedGroup
        | CE
        | tuple[DiagnosisRelatedGroup | CE, ...]
        | None = None,  # DRG.1
        drg_assigned_date_or_time: TS | tuple[TS, ...] | None = None,  # DRG.2
        drg_approval_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # DRG.3
        drg_grouper_review_code: DrgGrouperReviewCode
        | IS
        | tuple[DrgGrouperReviewCode | IS, ...]
        | None = None,  # DRG.4
        outlier_type: OutlierType
        | CE
        | tuple[OutlierType | CE, ...]
        | None = None,  # DRG.5
        outlier_days: NM | tuple[NM, ...] | None = None,  # DRG.6
        outlier_cost: CP | tuple[CP, ...] | None = None,  # DRG.7
        drg_payor: DrgPayor | IS | tuple[DrgPayor | IS, ...] | None = None,  # DRG.8
        outlier_reimbursement: CP | tuple[CP, ...] | None = None,  # DRG.9
        confidential_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # DRG.10
        drg_transfer_type: DrgTransferType
        | IS
        | tuple[DrgTransferType | IS, ...]
        | None = None,  # DRG.11
    ):
        """
        Diagnosis Related Group - `DRG <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG>`_
        The DRG segment contains diagnoses-related grouping information of various types. The DRG segment is used to send the DRG information, for example, for billing and medical records encoding.

        :param diagnostic_related_group: Coded Element (id: DRG.1 | len: 250 | use: O | rpt: 1)
        :param drg_assigned_date_or_time: Time Stamp (id: DRG.2 | len: 26 | use: O | rpt: 1)
        :param drg_approval_indicator: Coded values for HL7 tables (id: DRG.3 | len: 1 | use: O | rpt: 1)
        :param drg_grouper_review_code: Coded value for user-defined tables (id: DRG.4 | len: 2 | use: O | rpt: 1)
        :param outlier_type: Coded Element (id: DRG.5 | len: 250 | use: O | rpt: 1)
        :param outlier_days: Numeric (id: DRG.6 | len: 3 | use: O | rpt: 1)
        :param outlier_cost: Composite Price (id: DRG.7 | len: 12 | use: O | rpt: 1)
        :param drg_payor: Coded value for user-defined tables (id: DRG.8 | len: 1 | use: O | rpt: 1)
        :param outlier_reimbursement: Composite Price (id: DRG.9 | len: 9 | use: O | rpt: 1)
        :param confidential_indicator: Coded values for HL7 tables (id: DRG.10 | len: 1 | use: O | rpt: 1)
        :param drg_transfer_type: Coded value for user-defined tables (id: DRG.11 | len: 21 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 11
        self.diagnostic_related_group = diagnostic_related_group
        self.drg_assigned_date_or_time = drg_assigned_date_or_time
        self.drg_approval_indicator = drg_approval_indicator
        self.drg_grouper_review_code = drg_grouper_review_code
        self.outlier_type = outlier_type
        self.outlier_days = outlier_days
        self.outlier_cost = outlier_cost
        self.drg_payor = drg_payor
        self.outlier_reimbursement = outlier_reimbursement
        self.confidential_indicator = confidential_indicator
        self.drg_transfer_type = drg_transfer_type

    @property  # get DRG.1
    def diagnostic_related_group(self) -> DiagnosisRelatedGroup | None:
        """
        id: DRG.1 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.1
        """
        return self._c_data[0][0]

    @diagnostic_related_group.setter  # set DRG.1
    def diagnostic_related_group(
        self, diagnosis_related_group: DiagnosisRelatedGroup | None
    ):
        """
        id: DRG.1 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.1
        """
        self._c_data[0] = (diagnosis_related_group,)

    @property  # get DRG.2
    def drg_assigned_date_or_time(self) -> TS | None:
        """
        id: DRG.2 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.2
        """
        return self._c_data[1][0]

    @drg_assigned_date_or_time.setter  # set DRG.2
    def drg_assigned_date_or_time(self, ts: TS | None):
        """
        id: DRG.2 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.2
        """
        self._c_data[1] = (ts,)

    @property  # get DRG.3
    def drg_approval_indicator(self) -> YesOrNoIndicator | None:
        """
        id: DRG.3 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.3
        """
        return self._c_data[2][0]

    @drg_approval_indicator.setter  # set DRG.3
    def drg_approval_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: DRG.3 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.3
        """
        self._c_data[2] = (yes_or_no_indicator,)

    @property  # get DRG.4
    def drg_grouper_review_code(self) -> DrgGrouperReviewCode | None:
        """
        id: DRG.4 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.4
        """
        return self._c_data[3][0]

    @drg_grouper_review_code.setter  # set DRG.4
    def drg_grouper_review_code(
        self, drg_grouper_review_code: DrgGrouperReviewCode | None
    ):
        """
        id: DRG.4 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.4
        """
        self._c_data[3] = (drg_grouper_review_code,)

    @property  # get DRG.5
    def outlier_type(self) -> OutlierType | None:
        """
        id: DRG.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.5
        """
        return self._c_data[4][0]

    @outlier_type.setter  # set DRG.5
    def outlier_type(self, outlier_type: OutlierType | None):
        """
        id: DRG.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.5
        """
        self._c_data[4] = (outlier_type,)

    @property  # get DRG.6
    def outlier_days(self) -> NM | None:
        """
        id: DRG.6 | len: 3 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.6
        """
        return self._c_data[5][0]

    @outlier_days.setter  # set DRG.6
    def outlier_days(self, nm: NM | None):
        """
        id: DRG.6 | len: 3 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.6
        """
        self._c_data[5] = (nm,)

    @property  # get DRG.7
    def outlier_cost(self) -> CP | None:
        """
        id: DRG.7 | len: 12 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.7
        """
        return self._c_data[6][0]

    @outlier_cost.setter  # set DRG.7
    def outlier_cost(self, cp: CP | None):
        """
        id: DRG.7 | len: 12 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.7
        """
        self._c_data[6] = (cp,)

    @property  # get DRG.8
    def drg_payor(self) -> DrgPayor | None:
        """
        id: DRG.8 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.8
        """
        return self._c_data[7][0]

    @drg_payor.setter  # set DRG.8
    def drg_payor(self, drg_payor: DrgPayor | None):
        """
        id: DRG.8 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.8
        """
        self._c_data[7] = (drg_payor,)

    @property  # get DRG.9
    def outlier_reimbursement(self) -> CP | None:
        """
        id: DRG.9 | len: 9 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.9
        """
        return self._c_data[8][0]

    @outlier_reimbursement.setter  # set DRG.9
    def outlier_reimbursement(self, cp: CP | None):
        """
        id: DRG.9 | len: 9 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.9
        """
        self._c_data[8] = (cp,)

    @property  # get DRG.10
    def confidential_indicator(self) -> YesOrNoIndicator | None:
        """
        id: DRG.10 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.10
        """
        return self._c_data[9][0]

    @confidential_indicator.setter  # set DRG.10
    def confidential_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: DRG.10 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.10
        """
        self._c_data[9] = (yes_or_no_indicator,)

    @property  # get DRG.11
    def drg_transfer_type(self) -> DrgTransferType | None:
        """
        id: DRG.11 | len: 21 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.11
        """
        return self._c_data[10][0]

    @drg_transfer_type.setter  # set DRG.11
    def drg_transfer_type(self, drg_transfer_type: DrgTransferType | None):
        """
        id: DRG.11 | len: 21 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DRG.11
        """
        self._c_data[10] = (drg_transfer_type,)
