from __future__ import annotations
from ...base import HL7Segment
from ..data_types.OCD import OCD
from ..data_types.IS import IS
from ..data_types.NM import NM
from ..data_types.ST import ST
from ..data_types.OSP import OSP
from ..data_types.SI import SI
from ..data_types.UVC import UVC
from ..tables.ConditionCode import ConditionCode


"""
UB92 Data - UB2
HL7 Version: 2.5.1

-----BEGIN SEGMENT::UB2 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    UB2,
    OCD, IS, NM, ST, OSP, SI, UVC
)

ub2 = UB2(  #  - The UB2 segment contains data necessary to complete UB92 bills specific to the United States; other realms may choose to implement using regional code sets
    set_id_ub2=None,  # SI(...) 
    co_insurance_days=None,  # ST(...) 
    condition_code=None,  # IS(...) 
    covered_days=None,  # ST(...) 
    non_covered_days=None,  # ST(...) 
    value_amount_and_code=None,  # UVC(...) 
    occurrence_code_and_date=None,  # OCD(...) 
    occurrence_span_code_or_dates=None,  # OSP(...) 
    ub92_locator_2=None,  # ST(...) 
    ub92_locator_11=None,  # ST(...) 
    ub92_locator_31=None,  # ST(...) 
    document_control_number=None,  # ST(...) 
    ub92_locator_49=None,  # ST(...) 
    ub92_locator_56=None,  # ST(...) 
    ub92_locator_57=None,  # ST(...) 
    ub92_locator_78=None,  # ST(...) 
    special_visit_count=None,  # NM(...) 
)

-----END SEGMENT::UB2 TEMPLATE-----
"""


class UB2(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """UB2"""
    _hl7_name = """UB92 Data"""
    _hl7_description = """The UB2 segment contains data necessary to complete UB92 bills specific to the United States; other realms may choose to implement using regional code sets"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB2"
    _c_length = (4, 3, 2, 3, 4, 41, 259, 268, 29, 12, 5, 23, 4, 14, 27, 2, 3,)
    _c_rpt = (1, 1, 7, 1, 1, 12, 8, 2, 2, 2, 1, 2, 23, 5, 1, 2, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, ST, IS, ST, ST, UVC, OCD, OSP, ST, ST, ST, ST, ST, ST, ST, ST, NM,)
    _c_aliases = ("UB2.1", "UB2.2", "UB2.3", "UB2.4", "UB2.5", "UB2.6", "UB2.7", "UB2.8", "UB2.9", "UB2.10", "UB2.11", "UB2.12", "UB2.13", "UB2.14", "UB2.15", "UB2.16", "UB2.17",)
    _c_names = ("Set ID - UB2", "Co-Insurance Days (9)", "Condition Code (24-30)", "Covered Days (7)", "Non-Covered Days (8)", "Value Amount and Code (39-41)", "Occurrence Code and Date (32-35)", "Occurrence Span Code/Dates (36)", "UB92 Locator 2 (State)", "UB92 Locator 11 (State)", "UB92 Locator 31 (National)", "Document Control Number", "UB92 Locator 49 (National)", "UB92 Locator 56 (State)", "UB92 Locator 57 (National)", "UB92 Locator 78 (State)", "Special Visit Count",)
    _c_attrs = ("set_id_ub2", "co_insurance_days", "condition_code", "covered_days", "non_covered_days", "value_amount_and_code", "occurrence_code_and_date", "occurrence_span_code_or_dates", "ub92_locator_2", "ub92_locator_11", "ub92_locator_31", "document_control_number", "ub92_locator_49", "ub92_locator_56", "ub92_locator_57", "ub92_locator_78", "special_visit_count",)
    # fmt: on

    def __init__(
        self,
        set_id_ub2: SI | None = None,  # UB2.1
        co_insurance_days: ST | None = None,  # UB2.2
        condition_code: ConditionCode | IS | None = None,  # UB2.3
        covered_days: ST | None = None,  # UB2.4
        non_covered_days: ST | None = None,  # UB2.5
        value_amount_and_code: UVC | None = None,  # UB2.6
        occurrence_code_and_date: OCD | None = None,  # UB2.7
        occurrence_span_code_or_dates: OSP | None = None,  # UB2.8
        ub92_locator_2: ST | None = None,  # UB2.9
        ub92_locator_11: ST | None = None,  # UB2.10
        ub92_locator_31: ST | None = None,  # UB2.11
        document_control_number: ST | None = None,  # UB2.12
        ub92_locator_49: ST | None = None,  # UB2.13
        ub92_locator_56: ST | None = None,  # UB2.14
        ub92_locator_57: ST | None = None,  # UB2.15
        ub92_locator_78: ST | None = None,  # UB2.16
        special_visit_count: NM | None = None,  # UB2.17
    ):
        """
                UB92 Data - `UB2 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB2>`_
                The UB2 segment contains data necessary to complete UB92 bills specific to the United States; other realms may choose to implement using regional code sets. Only UB82 and UB92 fields that do not exist in other HL7 defined segments appear in this segment.  Just as with the UB82 billing, Patient Name and Date of Birth are required; they are included in the PID segment and therefore do not appear here. When the field locators are different on the UB92, as compared to the UB82, the element is listed with its new location in parentheses ( ). The UB codes listed as examples are not an exhaustive or current list; refer to a UB specification for additional information.

        The Uniform Billing segments are specific to the US and may not be implemented in non-US systems.

                :param set_id_ub2: Sequence ID (id: UB2.1 | len: 4 | use: O | rpt: 1)
                :param co_insurance_days: String Data (id: UB2.2 | len: 3 | use: O | rpt: 1)
                :param condition_code: Coded value for user-defined tables (id: UB2.3 | len: 2 | use: O | rpt: 7)
                :param covered_days: String Data (id: UB2.4 | len: 3 | use: O | rpt: 1)
                :param non_covered_days: String Data (id: UB2.5 | len: 4 | use: O | rpt: 1)
                :param value_amount_and_code: UB Value Code and Amount (id: UB2.6 | len: 41 | use: O | rpt: 12)
                :param occurrence_code_and_date: Occurrence Code and Date (id: UB2.7 | len: 259 | use: O | rpt: 8)
                :param occurrence_span_code_or_dates: Occurrence Span Code and Date (id: UB2.8 | len: 268 | use: O | rpt: 2)
                :param ub92_locator_2: String Data (id: UB2.9 | len: 29 | use: O | rpt: 2)
                :param ub92_locator_11: String Data (id: UB2.10 | len: 12 | use: O | rpt: 2)
                :param ub92_locator_31: String Data (id: UB2.11 | len: 5 | use: O | rpt: 1)
                :param document_control_number: String Data (id: UB2.12 | len: 23 | use: O | rpt: 2)
                :param ub92_locator_49: String Data (id: UB2.13 | len: 4 | use: O | rpt: 23)
                :param ub92_locator_56: String Data (id: UB2.14 | len: 14 | use: O | rpt: 5)
                :param ub92_locator_57: String Data (id: UB2.15 | len: 27 | use: O | rpt: 1)
                :param ub92_locator_78: String Data (id: UB2.16 | len: 2 | use: O | rpt: 2)
                :param special_visit_count: Numeric (id: UB2.17 | len: 3 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 17
        self.set_id_ub2 = set_id_ub2
        self.co_insurance_days = co_insurance_days
        self.condition_code = condition_code
        self.covered_days = covered_days
        self.non_covered_days = non_covered_days
        self.value_amount_and_code = value_amount_and_code
        self.occurrence_code_and_date = occurrence_code_and_date
        self.occurrence_span_code_or_dates = occurrence_span_code_or_dates
        self.ub92_locator_2 = ub92_locator_2
        self.ub92_locator_11 = ub92_locator_11
        self.ub92_locator_31 = ub92_locator_31
        self.document_control_number = document_control_number
        self.ub92_locator_49 = ub92_locator_49
        self.ub92_locator_56 = ub92_locator_56
        self.ub92_locator_57 = ub92_locator_57
        self.ub92_locator_78 = ub92_locator_78
        self.special_visit_count = special_visit_count

    @property  # get UB2.1
    def set_id_ub2(self) -> SI | None:
        """
        id: UB2.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.1
        """
        return self._c_data[0][0]

    @set_id_ub2.setter  # set UB2.1
    def set_id_ub2(self, si: SI | None):
        """
        id: UB2.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.1
        """
        self._c_data[0] = (si,)

    @property  # get UB2.2
    def co_insurance_days(self) -> ST | None:
        """
        id: UB2.2 | len: 3 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.2
        """
        return self._c_data[1][0]

    @co_insurance_days.setter  # set UB2.2
    def co_insurance_days(self, st: ST | None):
        """
        id: UB2.2 | len: 3 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.2
        """
        self._c_data[1] = (st,)

    @property
    def condition_code(self) -> tuple[ConditionCode, ...] | tuple[None]:
        """
        id: UB2.3 | len: 2 | use: O | rpt: 7
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.3
        """
        return self._c_data[2]

    @condition_code.setter  # set UB2.3
    def condition_code(
        self, condition_code: ConditionCode | tuple[ConditionCode] | None
    ):
        """
        id: UB2.3 | len: 2 | use: O | rpt: 7
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.3
        """
        if isinstance(condition_code, tuple):
            self._c_data[2] = condition_code
        else:
            self._c_data[2] = (condition_code,)

    @property  # get UB2.4
    def covered_days(self) -> ST | None:
        """
        id: UB2.4 | len: 3 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.4
        """
        return self._c_data[3][0]

    @covered_days.setter  # set UB2.4
    def covered_days(self, st: ST | None):
        """
        id: UB2.4 | len: 3 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.4
        """
        self._c_data[3] = (st,)

    @property  # get UB2.5
    def non_covered_days(self) -> ST | None:
        """
        id: UB2.5 | len: 4 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.5
        """
        return self._c_data[4][0]

    @non_covered_days.setter  # set UB2.5
    def non_covered_days(self, st: ST | None):
        """
        id: UB2.5 | len: 4 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.5
        """
        self._c_data[4] = (st,)

    @property
    def value_amount_and_code(self) -> tuple[UVC, ...] | tuple[None]:
        """
        id: UB2.6 | len: 41 | use: O | rpt: 12
        ---
        return_type: tuple[UVC, ...]: (UB Value Code and Amount, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.6
        """
        return self._c_data[5]

    @value_amount_and_code.setter  # set UB2.6
    def value_amount_and_code(self, uvc: UVC | tuple[UVC] | None):
        """
        id: UB2.6 | len: 41 | use: O | rpt: 12
        ---
        param_type: UVC | tuple[UVC, ...]: (UB Value Code and Amount, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.6
        """
        if isinstance(uvc, tuple):
            self._c_data[5] = uvc
        else:
            self._c_data[5] = (uvc,)

    @property
    def occurrence_code_and_date(self) -> tuple[OCD, ...] | tuple[None]:
        """
        id: UB2.7 | len: 259 | use: O | rpt: 8
        ---
        return_type: tuple[OCD, ...]: (Occurrence Code and Date, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.7
        """
        return self._c_data[6]

    @occurrence_code_and_date.setter  # set UB2.7
    def occurrence_code_and_date(self, ocd: OCD | tuple[OCD] | None):
        """
        id: UB2.7 | len: 259 | use: O | rpt: 8
        ---
        param_type: OCD | tuple[OCD, ...]: (Occurrence Code and Date, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.7
        """
        if isinstance(ocd, tuple):
            self._c_data[6] = ocd
        else:
            self._c_data[6] = (ocd,)

    @property
    def occurrence_span_code_or_dates(self) -> tuple[OSP, ...] | tuple[None]:
        """
        id: UB2.8 | len: 268 | use: O | rpt: 2
        ---
        return_type: tuple[OSP, ...]: (Occurrence Span Code and Date, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.8
        """
        return self._c_data[7]

    @occurrence_span_code_or_dates.setter  # set UB2.8
    def occurrence_span_code_or_dates(self, osp: OSP | tuple[OSP] | None):
        """
        id: UB2.8 | len: 268 | use: O | rpt: 2
        ---
        param_type: OSP | tuple[OSP, ...]: (Occurrence Span Code and Date, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.8
        """
        if isinstance(osp, tuple):
            self._c_data[7] = osp
        else:
            self._c_data[7] = (osp,)

    @property
    def ub92_locator_2(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: UB2.9 | len: 29 | use: O | rpt: 2
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.9
        """
        return self._c_data[8]

    @ub92_locator_2.setter  # set UB2.9
    def ub92_locator_2(self, st: ST | tuple[ST] | None):
        """
        id: UB2.9 | len: 29 | use: O | rpt: 2
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.9
        """
        if isinstance(st, tuple):
            self._c_data[8] = st
        else:
            self._c_data[8] = (st,)

    @property
    def ub92_locator_11(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: UB2.10 | len: 12 | use: O | rpt: 2
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.10
        """
        return self._c_data[9]

    @ub92_locator_11.setter  # set UB2.10
    def ub92_locator_11(self, st: ST | tuple[ST] | None):
        """
        id: UB2.10 | len: 12 | use: O | rpt: 2
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.10
        """
        if isinstance(st, tuple):
            self._c_data[9] = st
        else:
            self._c_data[9] = (st,)

    @property  # get UB2.11
    def ub92_locator_31(self) -> ST | None:
        """
        id: UB2.11 | len: 5 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.11
        """
        return self._c_data[10][0]

    @ub92_locator_31.setter  # set UB2.11
    def ub92_locator_31(self, st: ST | None):
        """
        id: UB2.11 | len: 5 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.11
        """
        self._c_data[10] = (st,)

    @property
    def document_control_number(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: UB2.12 | len: 23 | use: O | rpt: 2
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.12
        """
        return self._c_data[11]

    @document_control_number.setter  # set UB2.12
    def document_control_number(self, st: ST | tuple[ST] | None):
        """
        id: UB2.12 | len: 23 | use: O | rpt: 2
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.12
        """
        if isinstance(st, tuple):
            self._c_data[11] = st
        else:
            self._c_data[11] = (st,)

    @property
    def ub92_locator_49(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: UB2.13 | len: 4 | use: O | rpt: 23
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.13
        """
        return self._c_data[12]

    @ub92_locator_49.setter  # set UB2.13
    def ub92_locator_49(self, st: ST | tuple[ST] | None):
        """
        id: UB2.13 | len: 4 | use: O | rpt: 23
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.13
        """
        if isinstance(st, tuple):
            self._c_data[12] = st
        else:
            self._c_data[12] = (st,)

    @property
    def ub92_locator_56(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: UB2.14 | len: 14 | use: O | rpt: 5
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.14
        """
        return self._c_data[13]

    @ub92_locator_56.setter  # set UB2.14
    def ub92_locator_56(self, st: ST | tuple[ST] | None):
        """
        id: UB2.14 | len: 14 | use: O | rpt: 5
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.14
        """
        if isinstance(st, tuple):
            self._c_data[13] = st
        else:
            self._c_data[13] = (st,)

    @property  # get UB2.15
    def ub92_locator_57(self) -> ST | None:
        """
        id: UB2.15 | len: 27 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.15
        """
        return self._c_data[14][0]

    @ub92_locator_57.setter  # set UB2.15
    def ub92_locator_57(self, st: ST | None):
        """
        id: UB2.15 | len: 27 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.15
        """
        self._c_data[14] = (st,)

    @property
    def ub92_locator_78(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: UB2.16 | len: 2 | use: O | rpt: 2
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.16
        """
        return self._c_data[15]

    @ub92_locator_78.setter  # set UB2.16
    def ub92_locator_78(self, st: ST | tuple[ST] | None):
        """
        id: UB2.16 | len: 2 | use: O | rpt: 2
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.16
        """
        if isinstance(st, tuple):
            self._c_data[15] = st
        else:
            self._c_data[15] = (st,)

    @property  # get UB2.17
    def special_visit_count(self) -> NM | None:
        """
        id: UB2.17 | len: 3 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.17
        """
        return self._c_data[16][0]

    @special_visit_count.setter  # set UB2.17
    def special_visit_count(self, nm: NM | None):
        """
        id: UB2.17 | len: 3 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UB2.17
        """
        self._c_data[16] = (nm,)
