from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.CX import CX
from ..data_types.DT import DT
from ..data_types.IS import IS
from ..data_types.ID import ID
from ..tables.DisabledPersonCode import DisabledPersonCode
from ..tables.YesOrNoIndicator import YesOrNoIndicator


"""
Disability - DB1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::DB1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DB1,
    SI, CX, DT, IS, ID
)

db1 = DB1(  #  - The disability segment contains information related to the disability of a person
    set_id_db1=si,  # SI(...)  # Required.
    disabled_person_code=None,  # IS(...) 
    disabled_person_identifier=None,  # CX(...) 
    disabled_indicator=None,  # ID(...) 
    disability_start_date=None,  # DT(...) 
    disability_end_date=None,  # DT(...) 
    disability_return_to_work_date=None,  # DT(...) 
    disability_unable_to_work_date=None,  # DT(...) 
)

-----END SEGMENT::DB1 TEMPLATE-----
"""


class DB1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """DB1"""
    _hl7_name = """Disability"""
    _hl7_description = """The disability segment contains information related to the disability of a person"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1"
    _c_length = (4, 2, 250, 1, 8, 8, 8, 8,)
    _c_rpt = (1, 1, 65535, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, IS, CX, ID, DT, DT, DT, DT,)
    _c_aliases = ("DB1.1", "DB1.2", "DB1.3", "DB1.4", "DB1.5", "DB1.6", "DB1.7", "DB1.8",)
    _c_names = ("Set ID - DB1", "Disabled Person Code", "Disabled Person Identifier", "Disabled Indicator", "Disability Start Date", "Disability End Date", "Disability Return to Work Date", "Disability Unable to Work Date",)
    _c_attrs = ("set_id_db1", "disabled_person_code", "disabled_person_identifier", "disabled_indicator", "disability_start_date", "disability_end_date", "disability_return_to_work_date", "disability_unable_to_work_date",)
    # fmt: on

    def __init__(
        self,
        set_id_db1: SI | tuple[SI, ...],  # DB1.1
        disabled_person_code: DisabledPersonCode
        | IS
        | tuple[DisabledPersonCode | IS, ...]
        | None = None,  # DB1.2
        disabled_person_identifier: CX | tuple[CX, ...] | None = None,  # DB1.3
        disabled_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # DB1.4
        disability_start_date: DT | tuple[DT, ...] | None = None,  # DB1.5
        disability_end_date: DT | tuple[DT, ...] | None = None,  # DB1.6
        disability_return_to_work_date: DT | tuple[DT, ...] | None = None,  # DB1.7
        disability_unable_to_work_date: DT | tuple[DT, ...] | None = None,  # DB1.8
    ):
        """
        Disability - `DB1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1>`_
        The disability segment contains information related to the disability of a person. This segment was created instead of adding disability attributes to each segment that contains a person (to which disability may apply). This is an optional segment that can be used to send disability information about a person already defined by the Patient Administration Chapter. The disabled person code and identifier allow for the association of the disability information to the person.

        :param set_id_db1: Sequence ID (id: DB1.1 | len: 4 | use: R | rpt: 1)
        :param disabled_person_code: Coded value for user-defined tables (id: DB1.2 | len: 2 | use: O | rpt: 1)
        :param disabled_person_identifier: Extended Composite ID with Check Digit (id: DB1.3 | len: 250 | use: O | rpt: *)
        :param disabled_indicator: Coded values for HL7 tables (id: DB1.4 | len: 1 | use: O | rpt: 1)
        :param disability_start_date: Date (id: DB1.5 | len: 8 | use: O | rpt: 1)
        :param disability_end_date: Date (id: DB1.6 | len: 8 | use: O | rpt: 1)
        :param disability_return_to_work_date: Date (id: DB1.7 | len: 8 | use: O | rpt: 1)
        :param disability_unable_to_work_date: Date (id: DB1.8 | len: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.set_id_db1 = set_id_db1
        self.disabled_person_code = disabled_person_code
        self.disabled_person_identifier = disabled_person_identifier
        self.disabled_indicator = disabled_indicator
        self.disability_start_date = disability_start_date
        self.disability_end_date = disability_end_date
        self.disability_return_to_work_date = disability_return_to_work_date
        self.disability_unable_to_work_date = disability_unable_to_work_date

    @property  # get DB1.1
    def set_id_db1(self) -> SI:
        """
        id: DB1.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.1
        """
        return self._c_data[0][0]

    @set_id_db1.setter  # set DB1.1
    def set_id_db1(self, si: SI):
        """
        id: DB1.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.1
        """
        self._c_data[0] = (si,)

    @property  # get DB1.2
    def disabled_person_code(self) -> DisabledPersonCode | None:
        """
        id: DB1.2 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.2
        """
        return self._c_data[1][0]

    @disabled_person_code.setter  # set DB1.2
    def disabled_person_code(self, disabled_person_code: DisabledPersonCode | None):
        """
        id: DB1.2 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.2
        """
        self._c_data[1] = (disabled_person_code,)

    @property
    def disabled_person_identifier(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: DB1.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.3
        """
        return self._c_data[2]

    @disabled_person_identifier.setter  # set DB1.3
    def disabled_person_identifier(self, cx: CX | tuple[CX] | None):
        """
        id: DB1.3 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.3
        """
        if isinstance(cx, tuple):
            self._c_data[2] = cx
        else:
            self._c_data[2] = (cx,)

    @property  # get DB1.4
    def disabled_indicator(self) -> YesOrNoIndicator | None:
        """
        id: DB1.4 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.4
        """
        return self._c_data[3][0]

    @disabled_indicator.setter  # set DB1.4
    def disabled_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: DB1.4 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.4
        """
        self._c_data[3] = (yes_or_no_indicator,)

    @property  # get DB1.5
    def disability_start_date(self) -> DT | None:
        """
        id: DB1.5 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.5
        """
        return self._c_data[4][0]

    @disability_start_date.setter  # set DB1.5
    def disability_start_date(self, dt: DT | None):
        """
        id: DB1.5 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.5
        """
        self._c_data[4] = (dt,)

    @property  # get DB1.6
    def disability_end_date(self) -> DT | None:
        """
        id: DB1.6 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.6
        """
        return self._c_data[5][0]

    @disability_end_date.setter  # set DB1.6
    def disability_end_date(self, dt: DT | None):
        """
        id: DB1.6 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.6
        """
        self._c_data[5] = (dt,)

    @property  # get DB1.7
    def disability_return_to_work_date(self) -> DT | None:
        """
        id: DB1.7 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.7
        """
        return self._c_data[6][0]

    @disability_return_to_work_date.setter  # set DB1.7
    def disability_return_to_work_date(self, dt: DT | None):
        """
        id: DB1.7 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.7
        """
        self._c_data[6] = (dt,)

    @property  # get DB1.8
    def disability_unable_to_work_date(self) -> DT | None:
        """
        id: DB1.8 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.8
        """
        return self._c_data[7][0]

    @disability_unable_to_work_date.setter  # set DB1.8
    def disability_unable_to_work_date(self, dt: DT | None):
        """
        id: DB1.8 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DB1.8
        """
        self._c_data[7] = (dt,)
