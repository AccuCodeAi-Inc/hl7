from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CP import CP
from ..data_types.IS import IS
from ..tables.TypeOfBillCode import TypeOfBillCode
from ..tables.OverallClaimDispositionCode import OverallClaimDispositionCode
from ..tables.RevenueCode import RevenueCode
from ..tables.OceEditCode import OceEditCode


"""
Grouping/Reimbursement - Visit - GP1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::GP1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    GP1,
    CP, IS
)

gp1 = GP1(  #  - These fields are used in grouping and reimbursement for CMS APCs
    type_of_bill_code=_is,  # IS(...)  # Required.
    revenue_code=None,  # IS(...) 
    overall_claim_disposition_code=None,  # IS(...) 
    oce_edits_per_visit_code=None,  # IS(...) 
    outlier_cost=None,  # CP(...) 
)

-----END SEGMENT::GP1 TEMPLATE-----
"""


class GP1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """GP1"""
    _hl7_name = """Grouping/Reimbursement - Visit"""
    _hl7_description = """These fields are used in grouping and reimbursement for CMS APCs"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GP1"
    _c_length = (3, 3, 1, 2, 12,)
    _c_rpt = (1, 65535, 1, 65535, 1,)
    _c_usage = ("R", "O", "O", "O", "O",)
    _c_components = (IS, IS, IS, IS, CP,)
    _c_aliases = ("GP1.1", "GP1.2", "GP1.3", "GP1.4", "GP1.5",)
    _c_names = ("Type of Bill Code", "Revenue Code", "Overall Claim Disposition Code", "OCE Edits per Visit Code", "Outlier Cost",)
    _c_attrs = ("type_of_bill_code", "revenue_code", "overall_claim_disposition_code", "oce_edits_per_visit_code", "outlier_cost",)
    # fmt: on

    def __init__(
        self,
        type_of_bill_code: TypeOfBillCode | IS,  # GP1.1
        revenue_code: RevenueCode | IS | None = None,  # GP1.2
        overall_claim_disposition_code: OverallClaimDispositionCode
        | IS
        | None = None,  # GP1.3
        oce_edits_per_visit_code: OceEditCode | IS | None = None,  # GP1.4
        outlier_cost: CP | None = None,  # GP1.5
    ):
        """
        Grouping/Reimbursement - Visit - `GP1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GP1>`_
        These fields are used in grouping and reimbursement for CMS APCs. Please refer to the "Outpatient Prospective Payment System Final Rule" ("OPPS Final Rule") issued by CMS.

        :param type_of_bill_code: Coded value for user-defined tables (id: GP1.1 | len: 3 | use: R | rpt: 1)
        :param revenue_code: Coded value for user-defined tables (id: GP1.2 | len: 3 | use: O | rpt: *)
        :param overall_claim_disposition_code: Coded value for user-defined tables (id: GP1.3 | len: 1 | use: O | rpt: 1)
        :param oce_edits_per_visit_code: Coded value for user-defined tables (id: GP1.4 | len: 2 | use: O | rpt: *)
        :param outlier_cost: Composite Price (id: GP1.5 | len: 12 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.type_of_bill_code = type_of_bill_code
        self.revenue_code = revenue_code
        self.overall_claim_disposition_code = overall_claim_disposition_code
        self.oce_edits_per_visit_code = oce_edits_per_visit_code
        self.outlier_cost = outlier_cost

    @property  # get GP1.1
    def type_of_bill_code(self) -> TypeOfBillCode:
        """
        id: GP1.1 | len: 3 | use: R | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP1.1
        """
        return self._c_data[0][0]

    @type_of_bill_code.setter  # set GP1.1
    def type_of_bill_code(self, type_of_bill_code: TypeOfBillCode):
        """
        id: GP1.1 | len: 3 | use: R | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP1.1
        """
        self._c_data[0] = (type_of_bill_code,)

    @property
    def revenue_code(self) -> tuple[RevenueCode, ...] | tuple[None]:
        """
        id: GP1.2 | len: 3 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP1.2
        """
        return self._c_data[1]

    @revenue_code.setter  # set GP1.2
    def revenue_code(self, revenue_code: RevenueCode | tuple[RevenueCode] | None):
        """
        id: GP1.2 | len: 3 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP1.2
        """
        if isinstance(revenue_code, tuple):
            self._c_data[1] = revenue_code
        else:
            self._c_data[1] = (revenue_code,)

    @property  # get GP1.3
    def overall_claim_disposition_code(self) -> OverallClaimDispositionCode | None:
        """
        id: GP1.3 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP1.3
        """
        return self._c_data[2][0]

    @overall_claim_disposition_code.setter  # set GP1.3
    def overall_claim_disposition_code(
        self, overall_claim_disposition_code: OverallClaimDispositionCode | None
    ):
        """
        id: GP1.3 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP1.3
        """
        self._c_data[2] = (overall_claim_disposition_code,)

    @property
    def oce_edits_per_visit_code(self) -> tuple[OceEditCode, ...] | tuple[None]:
        """
        id: GP1.4 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP1.4
        """
        return self._c_data[3]

    @oce_edits_per_visit_code.setter  # set GP1.4
    def oce_edits_per_visit_code(
        self, oce_edit_code: OceEditCode | tuple[OceEditCode] | None
    ):
        """
        id: GP1.4 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP1.4
        """
        if isinstance(oce_edit_code, tuple):
            self._c_data[3] = oce_edit_code
        else:
            self._c_data[3] = (oce_edit_code,)

    @property  # get GP1.5
    def outlier_cost(self) -> CP | None:
        """
        id: GP1.5 | len: 12 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP1.5
        """
        return self._c_data[4][0]

    @outlier_cost.setter  # set GP1.5
    def outlier_cost(self, cp: CP | None):
        """
        id: GP1.5 | len: 12 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP1.5
        """
        self._c_data[4] = (cp,)
