from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.OCD import OCD
from ..data_types.IS import IS
from ..data_types.DT import DT
from ..data_types.NM import NM
from ..data_types.ST import ST
from ..data_types.SI import SI
from ..data_types.UVC import UVC
from ..tables.PsroOrUrApprovalIndicator import PsroOrUrApprovalIndicator
from ..tables.OccurrenceSpan import OccurrenceSpan
from ..tables.ConditionCode import ConditionCode
from ..tables.SpecialProgramIndicator import SpecialProgramIndicator


"""
UB82 Data - UB1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::UB1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    UB1,
    CE, OCD, IS, DT, NM, ST, SI, UVC
)

ub1 = UB1(  #  - The UB1 segment contains the data necessary to complete UB82 bills specific to the United States; other realms may choose to implement using regional code sets
    set_id_ub1=None,  # SI(...) 
    blood_deductible=None,  # NM(...) 
    blood_furnished_pints_of=None,  # NM(...) 
    blood_replaced_pints=None,  # NM(...) 
    blood_not_replaced_pints=None,  # NM(...) 
    co_insurance_days=None,  # NM(...) 
    condition_code=None,  # IS(...) 
    covered_days=None,  # NM(...) 
    non_covered_days=None,  # NM(...) 
    value_amount_and_code=None,  # UVC(...) 
    number_of_grace_days=None,  # NM(...) 
    special_program_indicator=None,  # CE(...) 
    psro_or_ur_approval_indicator=None,  # CE(...) 
    psro_or_ur_approved_stay_fm=None,  # DT(...) 
    psro_or_ur_approved_stay_to=None,  # DT(...) 
    occurrence=None,  # OCD(...) 
    occurrence_span=None,  # CE(...) 
    occur_span_start_date=None,  # DT(...) 
    occur_span_end_date=None,  # DT(...) 
    ub_82_locator_2=None,  # ST(...) 
    ub_82_locator_9=None,  # ST(...) 
    ub_82_locator_27=None,  # ST(...) 
    ub_82_locator_45=None,  # ST(...) 
)

-----END SEGMENT::UB1 TEMPLATE-----
"""


class UB1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """UB1"""
    _hl7_name = """UB82 Data"""
    _hl7_description = """The UB1 segment contains the data necessary to complete UB82 bills specific to the United States; other realms may choose to implement using regional code sets"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB1"
    _c_length = (4, 1, 2, 2, 2, 2, 14, 3, 3, 41, 2, 250, 250, 8, 8, 259, 250, 8, 8, 30, 7, 8, 17,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 5, 1, 1, 8, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B", "B", "B", "B",)
    _c_components = (SI, NM, NM, NM, NM, NM, IS, NM, NM, UVC, NM, CE, CE, DT, DT, OCD, CE, DT, DT, ST, ST, ST, ST,)
    _c_aliases = ("UB1.1", "UB1.2", "UB1.3", "UB1.4", "UB1.5", "UB1.6", "UB1.7", "UB1.8", "UB1.9", "UB1.10", "UB1.11", "UB1.12", "UB1.13", "UB1.14", "UB1.15", "UB1.16", "UB1.17", "UB1.18", "UB1.19", "UB1.20", "UB1.21", "UB1.22", "UB1.23",)
    _c_names = ("Set ID - UB1", "Blood Deductible (43)", "Blood Furnished-Pints Of (40)", "Blood Replaced-Pints (41)", "Blood Not Replaced-Pints (42)", "Co-Insurance Days (25)", "Condition Code (35-39)", "Covered Days (23)", "Non Covered Days (24)", "Value Amount and Code (46-49)", "Number Of Grace Days (90)", "Special Program Indicator (44)", "PSRO/UR Approval Indicator (87)", "PSRO/UR Approved Stay-Fm (88)", "PSRO/UR Approved Stay-To (89)", "Occurrence (28-32)", "Occurrence Span (33)", "Occur Span Start Date (33)", "Occur Span End Date (33)", "UB-82 Locator 2", "UB-82 Locator 9", "UB-82 Locator 27", "UB-82 Locator 45",)
    _c_attrs = ("set_id_ub1", "blood_deductible", "blood_furnished_pints_of", "blood_replaced_pints", "blood_not_replaced_pints", "co_insurance_days", "condition_code", "covered_days", "non_covered_days", "value_amount_and_code", "number_of_grace_days", "special_program_indicator", "psro_or_ur_approval_indicator", "psro_or_ur_approved_stay_fm", "psro_or_ur_approved_stay_to", "occurrence", "occurrence_span", "occur_span_start_date", "occur_span_end_date", "ub_82_locator_2", "ub_82_locator_9", "ub_82_locator_27", "ub_82_locator_45",)
    # fmt: on

    def __init__(
        self,
        set_id_ub1: SI | None = None,  # UB1.1
        blood_deductible: NM | None = None,  # UB1.2
        blood_furnished_pints_of: NM | None = None,  # UB1.3
        blood_replaced_pints: NM | None = None,  # UB1.4
        blood_not_replaced_pints: NM | None = None,  # UB1.5
        co_insurance_days: NM | None = None,  # UB1.6
        condition_code: ConditionCode | IS | None = None,  # UB1.7
        covered_days: NM | None = None,  # UB1.8
        non_covered_days: NM | None = None,  # UB1.9
        value_amount_and_code: UVC | None = None,  # UB1.10
        number_of_grace_days: NM | None = None,  # UB1.11
        special_program_indicator: SpecialProgramIndicator | CE | None = None,  # UB1.12
        psro_or_ur_approval_indicator: PsroOrUrApprovalIndicator
        | CE
        | None = None,  # UB1.13
        psro_or_ur_approved_stay_fm: DT | None = None,  # UB1.14
        psro_or_ur_approved_stay_to: DT | None = None,  # UB1.15
        occurrence: OCD | None = None,  # UB1.16
        occurrence_span: OccurrenceSpan | CE | None = None,  # UB1.17
        occur_span_start_date: DT | None = None,  # UB1.18
        occur_span_end_date: DT | None = None,  # UB1.19
        ub_82_locator_2: ST | None = None,  # UB1.20
        ub_82_locator_9: ST | None = None,  # UB1.21
        ub_82_locator_27: ST | None = None,  # UB1.22
        ub_82_locator_45: ST | None = None,  # UB1.23
    ):
        """
                UB82 Data - `UB1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB1>`_
                The UB1 segment contains the data necessary to complete UB82 bills specific to the United States; other realms may choose to implement using regional code sets. Only UB82 fields that do not exist in other HL7 defined segments appear in this segment. Patient Name and Date of Birth are required for UB82 billing; however, they are included in the PID segment and therefore do not appear here. The UB codes listed as examples are not an exhaustive or current list. Refer to a UB specification for additional information.

        The Uniform Billing segments are specific to the US and may not be implemented in non-US systems.

                :param set_id_ub1: Sequence ID (id: UB1.1 | len: 4 | use: O | rpt: 1)
                :param blood_deductible: Numeric (id: UB1.2 | len: 1 | use: B | rpt: 1)
                :param blood_furnished_pints_of: Numeric (id: UB1.3 | len: 2 | use: O | rpt: 1)
                :param blood_replaced_pints: Numeric (id: UB1.4 | len: 2 | use: O | rpt: 1)
                :param blood_not_replaced_pints: Numeric (id: UB1.5 | len: 2 | use: O | rpt: 1)
                :param co_insurance_days: Numeric (id: UB1.6 | len: 2 | use: O | rpt: 1)
                :param condition_code: Coded value for user-defined tables (id: UB1.7 | len: 14 | use: O | rpt: 5)
                :param covered_days: Numeric (id: UB1.8 | len: 3 | use: O | rpt: 1)
                :param non_covered_days: Numeric (id: UB1.9 | len: 3 | use: O | rpt: 1)
                :param value_amount_and_code: UB Value Code and Amount (id: UB1.10 | len: 41 | use: O | rpt: 8)
                :param number_of_grace_days: Numeric (id: UB1.11 | len: 2 | use: O | rpt: 1)
                :param special_program_indicator: Coded Element (id: UB1.12 | len: 250 | use: O | rpt: 1)
                :param psro_or_ur_approval_indicator: Coded Element (id: UB1.13 | len: 250 | use: O | rpt: 1)
                :param psro_or_ur_approved_stay_fm: Date (id: UB1.14 | len: 8 | use: O | rpt: 1)
                :param psro_or_ur_approved_stay_to: Date (id: UB1.15 | len: 8 | use: O | rpt: 1)
                :param occurrence: Occurrence Code and Date (id: UB1.16 | len: 259 | use: O | rpt: 5)
                :param occurrence_span: Coded Element (id: UB1.17 | len: 250 | use: O | rpt: 1)
                :param occur_span_start_date: Date (id: UB1.18 | len: 8 | use: O | rpt: 1)
                :param occur_span_end_date: Date (id: UB1.19 | len: 8 | use: O | rpt: 1)
                :param ub_82_locator_2: String Data (id: UB1.20 | len: 30 | use: B | rpt: 1)
                :param ub_82_locator_9: String Data (id: UB1.21 | len: 7 | use: B | rpt: 1)
                :param ub_82_locator_27: String Data (id: UB1.22 | len: 8 | use: B | rpt: 1)
                :param ub_82_locator_45: String Data (id: UB1.23 | len: 17 | use: B | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 23
        self.set_id_ub1 = set_id_ub1
        self.blood_deductible = blood_deductible
        self.blood_furnished_pints_of = blood_furnished_pints_of
        self.blood_replaced_pints = blood_replaced_pints
        self.blood_not_replaced_pints = blood_not_replaced_pints
        self.co_insurance_days = co_insurance_days
        self.condition_code = condition_code
        self.covered_days = covered_days
        self.non_covered_days = non_covered_days
        self.value_amount_and_code = value_amount_and_code
        self.number_of_grace_days = number_of_grace_days
        self.special_program_indicator = special_program_indicator
        self.psro_or_ur_approval_indicator = psro_or_ur_approval_indicator
        self.psro_or_ur_approved_stay_fm = psro_or_ur_approved_stay_fm
        self.psro_or_ur_approved_stay_to = psro_or_ur_approved_stay_to
        self.occurrence = occurrence
        self.occurrence_span = occurrence_span
        self.occur_span_start_date = occur_span_start_date
        self.occur_span_end_date = occur_span_end_date
        self.ub_82_locator_2 = ub_82_locator_2
        self.ub_82_locator_9 = ub_82_locator_9
        self.ub_82_locator_27 = ub_82_locator_27
        self.ub_82_locator_45 = ub_82_locator_45

    @property  # get UB1.1
    def set_id_ub1(self) -> SI | None:
        """
        id: UB1.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.1
        """
        return self._c_data[0][0]

    @set_id_ub1.setter  # set UB1.1
    def set_id_ub1(self, si: SI | None):
        """
        id: UB1.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.1
        """
        self._c_data[0] = (si,)

    @property  # get UB1.2
    def blood_deductible(self) -> NM | None:
        """
        id: UB1.2 | len: 1 | use: B | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.2
        """
        return self._c_data[1][0]

    @blood_deductible.setter  # set UB1.2
    def blood_deductible(self, nm: NM | None):
        """
        id: UB1.2 | len: 1 | use: B | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.2
        """
        self._c_data[1] = (nm,)

    @property  # get UB1.3
    def blood_furnished_pints_of(self) -> NM | None:
        """
        id: UB1.3 | len: 2 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.3
        """
        return self._c_data[2][0]

    @blood_furnished_pints_of.setter  # set UB1.3
    def blood_furnished_pints_of(self, nm: NM | None):
        """
        id: UB1.3 | len: 2 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.3
        """
        self._c_data[2] = (nm,)

    @property  # get UB1.4
    def blood_replaced_pints(self) -> NM | None:
        """
        id: UB1.4 | len: 2 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.4
        """
        return self._c_data[3][0]

    @blood_replaced_pints.setter  # set UB1.4
    def blood_replaced_pints(self, nm: NM | None):
        """
        id: UB1.4 | len: 2 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.4
        """
        self._c_data[3] = (nm,)

    @property  # get UB1.5
    def blood_not_replaced_pints(self) -> NM | None:
        """
        id: UB1.5 | len: 2 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.5
        """
        return self._c_data[4][0]

    @blood_not_replaced_pints.setter  # set UB1.5
    def blood_not_replaced_pints(self, nm: NM | None):
        """
        id: UB1.5 | len: 2 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.5
        """
        self._c_data[4] = (nm,)

    @property  # get UB1.6
    def co_insurance_days(self) -> NM | None:
        """
        id: UB1.6 | len: 2 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.6
        """
        return self._c_data[5][0]

    @co_insurance_days.setter  # set UB1.6
    def co_insurance_days(self, nm: NM | None):
        """
        id: UB1.6 | len: 2 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.6
        """
        self._c_data[5] = (nm,)

    @property
    def condition_code(self) -> tuple[ConditionCode, ...] | tuple[None]:
        """
        id: UB1.7 | len: 14 | use: O | rpt: 5
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.7
        """
        return self._c_data[6]

    @condition_code.setter  # set UB1.7
    def condition_code(
        self, condition_code: ConditionCode | tuple[ConditionCode] | None
    ):
        """
        id: UB1.7 | len: 14 | use: O | rpt: 5
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.7
        """
        if isinstance(condition_code, tuple):
            self._c_data[6] = condition_code
        else:
            self._c_data[6] = (condition_code,)

    @property  # get UB1.8
    def covered_days(self) -> NM | None:
        """
        id: UB1.8 | len: 3 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.8
        """
        return self._c_data[7][0]

    @covered_days.setter  # set UB1.8
    def covered_days(self, nm: NM | None):
        """
        id: UB1.8 | len: 3 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.8
        """
        self._c_data[7] = (nm,)

    @property  # get UB1.9
    def non_covered_days(self) -> NM | None:
        """
        id: UB1.9 | len: 3 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.9
        """
        return self._c_data[8][0]

    @non_covered_days.setter  # set UB1.9
    def non_covered_days(self, nm: NM | None):
        """
        id: UB1.9 | len: 3 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.9
        """
        self._c_data[8] = (nm,)

    @property
    def value_amount_and_code(self) -> tuple[UVC, ...] | tuple[None]:
        """
        id: UB1.10 | len: 41 | use: O | rpt: 8
        ---
        return_type: tuple[UVC, ...]: (UB Value Code and Amount, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.10
        """
        return self._c_data[9]

    @value_amount_and_code.setter  # set UB1.10
    def value_amount_and_code(self, uvc: UVC | tuple[UVC] | None):
        """
        id: UB1.10 | len: 41 | use: O | rpt: 8
        ---
        param_type: UVC | tuple[UVC, ...]: (UB Value Code and Amount, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.10
        """
        if isinstance(uvc, tuple):
            self._c_data[9] = uvc
        else:
            self._c_data[9] = (uvc,)

    @property  # get UB1.11
    def number_of_grace_days(self) -> NM | None:
        """
        id: UB1.11 | len: 2 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.11
        """
        return self._c_data[10][0]

    @number_of_grace_days.setter  # set UB1.11
    def number_of_grace_days(self, nm: NM | None):
        """
        id: UB1.11 | len: 2 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.11
        """
        self._c_data[10] = (nm,)

    @property  # get UB1.12
    def special_program_indicator(self) -> SpecialProgramIndicator | None:
        """
        id: UB1.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.12
        """
        return self._c_data[11][0]

    @special_program_indicator.setter  # set UB1.12
    def special_program_indicator(
        self, special_program_indicator: SpecialProgramIndicator | None
    ):
        """
        id: UB1.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.12
        """
        self._c_data[11] = (special_program_indicator,)

    @property  # get UB1.13
    def psro_or_ur_approval_indicator(self) -> PsroOrUrApprovalIndicator | None:
        """
        id: UB1.13 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.13
        """
        return self._c_data[12][0]

    @psro_or_ur_approval_indicator.setter  # set UB1.13
    def psro_or_ur_approval_indicator(
        self, psro_or_ur_approval_indicator: PsroOrUrApprovalIndicator | None
    ):
        """
        id: UB1.13 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.13
        """
        self._c_data[12] = (psro_or_ur_approval_indicator,)

    @property  # get UB1.14
    def psro_or_ur_approved_stay_fm(self) -> DT | None:
        """
        id: UB1.14 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.14
        """
        return self._c_data[13][0]

    @psro_or_ur_approved_stay_fm.setter  # set UB1.14
    def psro_or_ur_approved_stay_fm(self, dt: DT | None):
        """
        id: UB1.14 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.14
        """
        self._c_data[13] = (dt,)

    @property  # get UB1.15
    def psro_or_ur_approved_stay_to(self) -> DT | None:
        """
        id: UB1.15 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.15
        """
        return self._c_data[14][0]

    @psro_or_ur_approved_stay_to.setter  # set UB1.15
    def psro_or_ur_approved_stay_to(self, dt: DT | None):
        """
        id: UB1.15 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.15
        """
        self._c_data[14] = (dt,)

    @property
    def occurrence(self) -> tuple[OCD, ...] | tuple[None]:
        """
        id: UB1.16 | len: 259 | use: O | rpt: 5
        ---
        return_type: tuple[OCD, ...]: (Occurrence Code and Date, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.16
        """
        return self._c_data[15]

    @occurrence.setter  # set UB1.16
    def occurrence(self, ocd: OCD | tuple[OCD] | None):
        """
        id: UB1.16 | len: 259 | use: O | rpt: 5
        ---
        param_type: OCD | tuple[OCD, ...]: (Occurrence Code and Date, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.16
        """
        if isinstance(ocd, tuple):
            self._c_data[15] = ocd
        else:
            self._c_data[15] = (ocd,)

    @property  # get UB1.17
    def occurrence_span(self) -> OccurrenceSpan | None:
        """
        id: UB1.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.17
        """
        return self._c_data[16][0]

    @occurrence_span.setter  # set UB1.17
    def occurrence_span(self, occurrence_span: OccurrenceSpan | None):
        """
        id: UB1.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.17
        """
        self._c_data[16] = (occurrence_span,)

    @property  # get UB1.18
    def occur_span_start_date(self) -> DT | None:
        """
        id: UB1.18 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.18
        """
        return self._c_data[17][0]

    @occur_span_start_date.setter  # set UB1.18
    def occur_span_start_date(self, dt: DT | None):
        """
        id: UB1.18 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.18
        """
        self._c_data[17] = (dt,)

    @property  # get UB1.19
    def occur_span_end_date(self) -> DT | None:
        """
        id: UB1.19 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.19
        """
        return self._c_data[18][0]

    @occur_span_end_date.setter  # set UB1.19
    def occur_span_end_date(self, dt: DT | None):
        """
        id: UB1.19 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.19
        """
        self._c_data[18] = (dt,)

    @property  # get UB1.20
    def ub_82_locator_2(self) -> ST | None:
        """
        id: UB1.20 | len: 30 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.20
        """
        return self._c_data[19][0]

    @ub_82_locator_2.setter  # set UB1.20
    def ub_82_locator_2(self, st: ST | None):
        """
        id: UB1.20 | len: 30 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.20
        """
        self._c_data[19] = (st,)

    @property  # get UB1.21
    def ub_82_locator_9(self) -> ST | None:
        """
        id: UB1.21 | len: 7 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.21
        """
        return self._c_data[20][0]

    @ub_82_locator_9.setter  # set UB1.21
    def ub_82_locator_9(self, st: ST | None):
        """
        id: UB1.21 | len: 7 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.21
        """
        self._c_data[20] = (st,)

    @property  # get UB1.22
    def ub_82_locator_27(self) -> ST | None:
        """
        id: UB1.22 | len: 8 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.22
        """
        return self._c_data[21][0]

    @ub_82_locator_27.setter  # set UB1.22
    def ub_82_locator_27(self, st: ST | None):
        """
        id: UB1.22 | len: 8 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.22
        """
        self._c_data[21] = (st,)

    @property  # get UB1.23
    def ub_82_locator_45(self) -> ST | None:
        """
        id: UB1.23 | len: 17 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.23
        """
        return self._c_data[22][0]

    @ub_82_locator_45.setter  # set UB1.23
    def ub_82_locator_45(self, st: ST | None):
        """
        id: UB1.23 | len: 17 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB1.23
        """
        self._c_data[22] = (st,)
