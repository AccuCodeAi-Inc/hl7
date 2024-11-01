from __future__ import annotations
from ...base import HL7Segment
from ..data_types.IS import IS
from ..data_types.CE import CE
from ..data_types.CP import CP
from ..data_types.NM import NM
from ..tables.PaymentAdjustmentCode import PaymentAdjustmentCode
from ..tables.RevenueCode import RevenueCode
from ..tables.OceEditCode import OceEditCode
from ..tables.PackagingStatusCode import PackagingStatusCode
from ..tables.AmbulatoryPaymentClassificationCode import (
    AmbulatoryPaymentClassificationCode,
)
from ..tables.DenialOrRejectionCode import DenialOrRejectionCode
from ..tables.ReimbursementActionCode import ReimbursementActionCode
from ..tables.ModifierEditCode import ModifierEditCode
from ..tables.ReimbursementTypeCode import ReimbursementTypeCode


"""
Grouping/Reimbursement - Procedure Line Item - GP2
HL7 Version: 2.5.1

-----BEGIN SEGMENT::GP2 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    GP2,
    IS, CE, CP, NM
)

gp2 = GP2(  #  - This segment is used for items that pertain to each HCPC/CPT line item
    revenue_code=None,  # IS(...) 
    number_of_service_units=None,  # NM(...) 
    charge=None,  # CP(...) 
    reimbursement_action_code=None,  # IS(...) 
    denial_or_rejection_code=None,  # IS(...) 
    oce_edit_code=None,  # IS(...) 
    ambulatory_payment_classification_code=None,  # CE(...) 
    modifier_edit_code=None,  # IS(...) 
    payment_adjustment_code=None,  # IS(...) 
    packaging_status_code=None,  # IS(...) 
    expected_cms_payment_amount=None,  # CP(...) 
    reimbursement_type_code=None,  # IS(...) 
    co_pay_amount=None,  # CP(...) 
    pay_rate_per_service_unit=None,  # NM(...) 
)

-----END SEGMENT::GP2 TEMPLATE-----
"""


class GP2(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """GP2"""
    _hl7_name = """Grouping/Reimbursement - Procedure Line Item"""
    _hl7_description = """This segment is used for items that pertain to each HCPC/CPT line item"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GP2"
    _c_length = (3, 7, 12, 1, 1, 3, 250, 1, 1, 1, 12, 2, 12, 4,)
    _c_rpt = (1, 1, 1, 1, 1, 65535, 1, 65535, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (IS, NM, CP, IS, IS, IS, CE, IS, IS, IS, CP, IS, CP, NM,)
    _c_aliases = ("GP2.1", "GP2.2", "GP2.3", "GP2.4", "GP2.5", "GP2.6", "GP2.7", "GP2.8", "GP2.9", "GP2.10", "GP2.11", "GP2.12", "GP2.13", "GP2.14",)
    _c_names = ("Revenue Code", "Number of Service Units", "Charge", "Reimbursement Action Code", "Denial or Rejection Code", "OCE Edit Code", "Ambulatory Payment Classification Code", "Modifier Edit Code", "Payment Adjustment Code", "Packaging Status Code", "Expected CMS Payment Amount", "Reimbursement Type Code", "Co-Pay Amount", "Pay Rate per Service Unit",)
    _c_attrs = ("revenue_code", "number_of_service_units", "charge", "reimbursement_action_code", "denial_or_rejection_code", "oce_edit_code", "ambulatory_payment_classification_code", "modifier_edit_code", "payment_adjustment_code", "packaging_status_code", "expected_cms_payment_amount", "reimbursement_type_code", "co_pay_amount", "pay_rate_per_service_unit",)
    # fmt: on

    def __init__(
        self,
        revenue_code: RevenueCode
        | IS
        | tuple[RevenueCode | IS, ...]
        | None = None,  # GP2.1
        number_of_service_units: NM | tuple[NM, ...] | None = None,  # GP2.2
        charge: CP | tuple[CP, ...] | None = None,  # GP2.3
        reimbursement_action_code: ReimbursementActionCode
        | IS
        | tuple[ReimbursementActionCode | IS, ...]
        | None = None,  # GP2.4
        denial_or_rejection_code: DenialOrRejectionCode
        | IS
        | tuple[DenialOrRejectionCode | IS, ...]
        | None = None,  # GP2.5
        oce_edit_code: OceEditCode
        | IS
        | tuple[OceEditCode | IS, ...]
        | None = None,  # GP2.6
        ambulatory_payment_classification_code: AmbulatoryPaymentClassificationCode
        | CE
        | tuple[AmbulatoryPaymentClassificationCode | CE, ...]
        | None = None,  # GP2.7
        modifier_edit_code: ModifierEditCode
        | IS
        | tuple[ModifierEditCode | IS, ...]
        | None = None,  # GP2.8
        payment_adjustment_code: PaymentAdjustmentCode
        | IS
        | tuple[PaymentAdjustmentCode | IS, ...]
        | None = None,  # GP2.9
        packaging_status_code: PackagingStatusCode
        | IS
        | tuple[PackagingStatusCode | IS, ...]
        | None = None,  # GP2.10
        expected_cms_payment_amount: CP | tuple[CP, ...] | None = None,  # GP2.11
        reimbursement_type_code: ReimbursementTypeCode
        | IS
        | tuple[ReimbursementTypeCode | IS, ...]
        | None = None,  # GP2.12
        co_pay_amount: CP | tuple[CP, ...] | None = None,  # GP2.13
        pay_rate_per_service_unit: NM | tuple[NM, ...] | None = None,  # GP2.14
    ):
        """
        Grouping/Reimbursement - Procedure Line Item - `GP2 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GP2>`_
        This segment is used for items that pertain to each HCPC/CPT line item.

        :param revenue_code: Coded value for user-defined tables (id: GP2.1 | len: 3 | use: O | rpt: 1)
        :param number_of_service_units: Numeric (id: GP2.2 | len: 7 | use: O | rpt: 1)
        :param charge: Composite Price (id: GP2.3 | len: 12 | use: O | rpt: 1)
        :param reimbursement_action_code: Coded value for user-defined tables (id: GP2.4 | len: 1 | use: O | rpt: 1)
        :param denial_or_rejection_code: Coded value for user-defined tables (id: GP2.5 | len: 1 | use: O | rpt: 1)
        :param oce_edit_code: Coded value for user-defined tables (id: GP2.6 | len: 3 | use: O | rpt: *)
        :param ambulatory_payment_classification_code: Coded Element (id: GP2.7 | len: 250 | use: O | rpt: 1)
        :param modifier_edit_code: Coded value for user-defined tables (id: GP2.8 | len: 1 | use: O | rpt: *)
        :param payment_adjustment_code: Coded value for user-defined tables (id: GP2.9 | len: 1 | use: O | rpt: 1)
        :param packaging_status_code: Coded value for user-defined tables (id: GP2.10 | len: 1 | use: O | rpt: 1)
        :param expected_cms_payment_amount: Composite Price (id: GP2.11 | len: 12 | use: O | rpt: 1)
        :param reimbursement_type_code: Coded value for user-defined tables (id: GP2.12 | len: 2 | use: O | rpt: 1)
        :param co_pay_amount: Composite Price (id: GP2.13 | len: 12 | use: O | rpt: 1)
        :param pay_rate_per_service_unit: Numeric (id: GP2.14 | len: 4 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 14
        self.revenue_code = revenue_code
        self.number_of_service_units = number_of_service_units
        self.charge = charge
        self.reimbursement_action_code = reimbursement_action_code
        self.denial_or_rejection_code = denial_or_rejection_code
        self.oce_edit_code = oce_edit_code
        self.ambulatory_payment_classification_code = (
            ambulatory_payment_classification_code
        )
        self.modifier_edit_code = modifier_edit_code
        self.payment_adjustment_code = payment_adjustment_code
        self.packaging_status_code = packaging_status_code
        self.expected_cms_payment_amount = expected_cms_payment_amount
        self.reimbursement_type_code = reimbursement_type_code
        self.co_pay_amount = co_pay_amount
        self.pay_rate_per_service_unit = pay_rate_per_service_unit

    @property  # get GP2.1
    def revenue_code(self) -> RevenueCode | None:
        """
        id: GP2.1 | len: 3 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.1
        """
        return self._c_data[0][0]

    @revenue_code.setter  # set GP2.1
    def revenue_code(self, revenue_code: RevenueCode | None):
        """
        id: GP2.1 | len: 3 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.1
        """
        self._c_data[0] = (revenue_code,)

    @property  # get GP2.2
    def number_of_service_units(self) -> NM | None:
        """
        id: GP2.2 | len: 7 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.2
        """
        return self._c_data[1][0]

    @number_of_service_units.setter  # set GP2.2
    def number_of_service_units(self, nm: NM | None):
        """
        id: GP2.2 | len: 7 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.2
        """
        self._c_data[1] = (nm,)

    @property  # get GP2.3
    def charge(self) -> CP | None:
        """
        id: GP2.3 | len: 12 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.3
        """
        return self._c_data[2][0]

    @charge.setter  # set GP2.3
    def charge(self, cp: CP | None):
        """
        id: GP2.3 | len: 12 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.3
        """
        self._c_data[2] = (cp,)

    @property  # get GP2.4
    def reimbursement_action_code(self) -> ReimbursementActionCode | None:
        """
        id: GP2.4 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.4
        """
        return self._c_data[3][0]

    @reimbursement_action_code.setter  # set GP2.4
    def reimbursement_action_code(
        self, reimbursement_action_code: ReimbursementActionCode | None
    ):
        """
        id: GP2.4 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.4
        """
        self._c_data[3] = (reimbursement_action_code,)

    @property  # get GP2.5
    def denial_or_rejection_code(self) -> DenialOrRejectionCode | None:
        """
        id: GP2.5 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.5
        """
        return self._c_data[4][0]

    @denial_or_rejection_code.setter  # set GP2.5
    def denial_or_rejection_code(
        self, denial_or_rejection_code: DenialOrRejectionCode | None
    ):
        """
        id: GP2.5 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.5
        """
        self._c_data[4] = (denial_or_rejection_code,)

    @property
    def oce_edit_code(self) -> tuple[OceEditCode, ...] | tuple[None]:
        """
        id: GP2.6 | len: 3 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.6
        """
        return self._c_data[5]

    @oce_edit_code.setter  # set GP2.6
    def oce_edit_code(self, oce_edit_code: OceEditCode | tuple[OceEditCode] | None):
        """
        id: GP2.6 | len: 3 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.6
        """
        if isinstance(oce_edit_code, tuple):
            self._c_data[5] = oce_edit_code
        else:
            self._c_data[5] = (oce_edit_code,)

    @property  # get GP2.7
    def ambulatory_payment_classification_code(
        self,
    ) -> AmbulatoryPaymentClassificationCode | None:
        """
        id: GP2.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.7
        """
        return self._c_data[6][0]

    @ambulatory_payment_classification_code.setter  # set GP2.7
    def ambulatory_payment_classification_code(
        self,
        ambulatory_payment_classification_code: AmbulatoryPaymentClassificationCode
        | None,
    ):
        """
        id: GP2.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.7
        """
        self._c_data[6] = (ambulatory_payment_classification_code,)

    @property
    def modifier_edit_code(self) -> tuple[ModifierEditCode, ...] | tuple[None]:
        """
        id: GP2.8 | len: 1 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.8
        """
        return self._c_data[7]

    @modifier_edit_code.setter  # set GP2.8
    def modifier_edit_code(
        self, modifier_edit_code: ModifierEditCode | tuple[ModifierEditCode] | None
    ):
        """
        id: GP2.8 | len: 1 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.8
        """
        if isinstance(modifier_edit_code, tuple):
            self._c_data[7] = modifier_edit_code
        else:
            self._c_data[7] = (modifier_edit_code,)

    @property  # get GP2.9
    def payment_adjustment_code(self) -> PaymentAdjustmentCode | None:
        """
        id: GP2.9 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.9
        """
        return self._c_data[8][0]

    @payment_adjustment_code.setter  # set GP2.9
    def payment_adjustment_code(
        self, payment_adjustment_code: PaymentAdjustmentCode | None
    ):
        """
        id: GP2.9 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.9
        """
        self._c_data[8] = (payment_adjustment_code,)

    @property  # get GP2.10
    def packaging_status_code(self) -> PackagingStatusCode | None:
        """
        id: GP2.10 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.10
        """
        return self._c_data[9][0]

    @packaging_status_code.setter  # set GP2.10
    def packaging_status_code(self, packaging_status_code: PackagingStatusCode | None):
        """
        id: GP2.10 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.10
        """
        self._c_data[9] = (packaging_status_code,)

    @property  # get GP2.11
    def expected_cms_payment_amount(self) -> CP | None:
        """
        id: GP2.11 | len: 12 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.11
        """
        return self._c_data[10][0]

    @expected_cms_payment_amount.setter  # set GP2.11
    def expected_cms_payment_amount(self, cp: CP | None):
        """
        id: GP2.11 | len: 12 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.11
        """
        self._c_data[10] = (cp,)

    @property  # get GP2.12
    def reimbursement_type_code(self) -> ReimbursementTypeCode | None:
        """
        id: GP2.12 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.12
        """
        return self._c_data[11][0]

    @reimbursement_type_code.setter  # set GP2.12
    def reimbursement_type_code(
        self, reimbursement_type_code: ReimbursementTypeCode | None
    ):
        """
        id: GP2.12 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.12
        """
        self._c_data[11] = (reimbursement_type_code,)

    @property  # get GP2.13
    def co_pay_amount(self) -> CP | None:
        """
        id: GP2.13 | len: 12 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.13
        """
        return self._c_data[12][0]

    @co_pay_amount.setter  # set GP2.13
    def co_pay_amount(self, cp: CP | None):
        """
        id: GP2.13 | len: 12 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.13
        """
        self._c_data[12] = (cp,)

    @property  # get GP2.14
    def pay_rate_per_service_unit(self) -> NM | None:
        """
        id: GP2.14 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.14
        """
        return self._c_data[13][0]

    @pay_rate_per_service_unit.setter  # set GP2.14
    def pay_rate_per_service_unit(self, nm: NM | None):
        """
        id: GP2.14 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GP2.14
        """
        self._c_data[13] = (nm,)
