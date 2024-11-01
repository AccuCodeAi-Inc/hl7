from __future__ import annotations
from ...base import DataType
from .IS import IS
from .TS import TS
from ..tables.FinancialClass import FinancialClass


"""
DataType - FC
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::FC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    FC,
    IS, TS
)

fc = FC(  # Financial Class - 
    financial_class_code=_is,  # IS(...)  # Required.
    effective_date=None,  # TS(...) 
)

-----END COMPOSITE_DATA_TYPE::FC TEMPLATE-----
"""


class FC(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 47
    _hl7_id = """FC"""
    _hl7_name = """Financial Class"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FC"
    _c_length = (20, 26,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "O",)
    _c_aliases = ("FC.1", "FC.2",)
    _c_components = (IS, TS,)
    _c_names = ("Financial Class Code", "Effective Date",)
    _c_attrs = ("financial_class_code", "effective_date",)
    # fmt: on

    def __init__(
        self,
        financial_class_code: FinancialClass | IS | tuple[FinancialClass | IS],  # FC.1
        effective_date: TS | tuple[TS] | None = None,  # FC.2
    ):
        """
        Financial Class - `FC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FC>`_


        :param financial_class_code: This component contains the financial class assigned to a person (id: FC.1 | len: 20 | use: R | rpt: 1)
        :param effective_date: This component contains the effective date/time of the persons assignment to the financial class specified in the first component (id: FC.2 | len: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.financial_class_code = financial_class_code
        self.effective_date = effective_date

    @property  # get FC.1
    def financial_class_code(self) -> FinancialClass:
        """
        id: FC.1 | len: 20 | use: R | rpt: 1
        ---
        This component contains the financial class assigned to a person. User-defined Table 0064 - Financial class is used as the HL7 identifier for the user-defined table of values for this component.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FC.1
        """
        return self._c_data[0][0]

    @financial_class_code.setter  # set FC.1
    def financial_class_code(self, financial_class: FinancialClass):
        """
        id: FC.1 | len: 20 | use: R | rpt: 1
        ---
        This component contains the financial class assigned to a person. User-defined Table 0064 - Financial class is used as the HL7 identifier for the user-defined table of values for this component.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FC.1
        """
        self._c_data[0] = (financial_class,)

    @property  # get FC.2
    def effective_date(self) -> TS | None:
        """
        id: FC.2 | len: 26 | use: O | rpt: 1
        ---
        This component contains the effective date/time of the persons assignment to the financial class specified in the first component.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FC.2
        """
        return self._c_data[1][0]

    @effective_date.setter  # set FC.2
    def effective_date(self, ts: TS | None):
        """
        id: FC.2 | len: 26 | use: O | rpt: 1
        ---
        This component contains the effective date/time of the persons assignment to the financial class specified in the first component.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FC.2
        """
        self._c_data[1] = (ts,)
