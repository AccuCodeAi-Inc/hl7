from __future__ import annotations
from ...base import DataType
from .IS import IS
from .DT import DT
from .ST import ST
from ..tables.PractitionerIdNumberType import PractitionerIdNumberType


"""
DataType - PLN
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::PLN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PLN,
    IS, DT, ST
)

pln = PLN(  # Practitioner License or Other ID Number - This data type specifies a practitioners license number, or other ID number such as UPIN, Medicare and Medicaid number, and associated detail
    id_number=st,  # ST(...)  # Required.
    type_of_id_number=_is,  # IS(...)  # Required.
    state_or_other_qualifying_information=None,  # ST(...) 
    expiration_date=None,  # DT(...) 
)

-----END COMPOSITE_DATA_TYPE::PLN TEMPLATE-----
"""


class PLN(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 101
    _hl7_id = """PLN"""
    _hl7_name = """Practitioner License or Other ID Number"""
    _hl7_description = """This data type specifies a practitioners license number, or other ID number such as UPIN, Medicare and Medicaid number, and associated detail"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PLN"
    _c_length = (20, 8, 62, 8,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("R", "R", "O", "O",)
    _c_aliases = ("PLN.1", "PLN.2", "PLN.3", "PLN.4",)
    _c_components = (ST, IS, ST, DT,)
    _c_names = ("Id Number", "Type Of Id Number", "State/Other Qualifying Information", "Expiration Date",)
    _c_attrs = ("id_number", "type_of_id_number", "state_or_other_qualifying_information", "expiration_date",)
    # fmt: on

    def __init__(
        self,
        id_number: ST,  # PLN.1
        type_of_id_number: PractitionerIdNumberType | IS,  # PLN.2
        state_or_other_qualifying_information: ST | None = None,  # PLN.3
        expiration_date: DT | None = None,  # PLN.4
    ):
        """
        Practitioner License or Other ID Number - `PLN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PLN>`_
        This data type specifies a practitioners license number, or other ID number such as UPIN, Medicare and Medicaid number, and associated detail.

        :param id_number: Specifies the license number or other ID number such as UPIN, Medicare and Medicaid number (id: PLN.1 | len: 20 | use: R | rpt: 1)
        :param type_of_id_number: Specifies the type of number (id: PLN.2 | len: 8 | use: R | rpt: 1)
        :param state_or_other_qualifying_information: Specifies the state or province in which the license or ID is valid, if relevant, or other qualifying information (id: PLN.3 | len: 62 | use: O | rpt: 1)
        :param expiration_date: Specifies the date when the license or ID is no longer valid (id: PLN.4 | len: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.id_number = id_number
        self.type_of_id_number = type_of_id_number
        self.state_or_other_qualifying_information = (
            state_or_other_qualifying_information
        )
        self.expiration_date = expiration_date

    @property  # get PLN.1
    def id_number(self) -> ST:
        """
        id: PLN.1 | len: 20 | use: R | rpt: 1
        ---
        Specifies the license number or other ID number such as UPIN, Medicare and Medicaid number.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PLN.1
        """
        return self._c_data[0][0]

    @id_number.setter  # set PLN.1
    def id_number(self, st: ST):
        """
        id: PLN.1 | len: 20 | use: R | rpt: 1
        ---
        Specifies the license number or other ID number such as UPIN, Medicare and Medicaid number.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PLN.1
        """
        self._c_data[0] = (st,)

    @property  # get PLN.2
    def type_of_id_number(self) -> PractitionerIdNumberType:
        """
        id: PLN.2 | len: 8 | use: R | rpt: 1
        ---
        Specifies the type of number.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PLN.2
        """
        return self._c_data[1][0]

    @type_of_id_number.setter  # set PLN.2
    def type_of_id_number(self, practitioner_id_number_type: PractitionerIdNumberType):
        """
        id: PLN.2 | len: 8 | use: R | rpt: 1
        ---
        Specifies the type of number.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PLN.2
        """
        self._c_data[1] = (practitioner_id_number_type,)

    @property  # get PLN.3
    def state_or_other_qualifying_information(self) -> ST | None:
        """
        id: PLN.3 | len: 62 | use: O | rpt: 1
        ---
        Specifies the state or province in which the license or ID is valid, if relevant, or other qualifying information. It is recommended that state qualifications use the abbreviations from the postal service of the country.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PLN.3
        """
        return self._c_data[2][0]

    @state_or_other_qualifying_information.setter  # set PLN.3
    def state_or_other_qualifying_information(self, st: ST | None):
        """
        id: PLN.3 | len: 62 | use: O | rpt: 1
        ---
        Specifies the state or province in which the license or ID is valid, if relevant, or other qualifying information. It is recommended that state qualifications use the abbreviations from the postal service of the country.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PLN.3
        """
        self._c_data[2] = (st,)

    @property  # get PLN.4
    def expiration_date(self) -> DT | None:
        """
        id: PLN.4 | len: 8 | use: O | rpt: 1
        ---
        Specifies the date when the license or ID is no longer valid.
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PLN.4
        """
        return self._c_data[3][0]

    @expiration_date.setter  # set PLN.4
    def expiration_date(self, dt: DT | None):
        """
        id: PLN.4 | len: 8 | use: O | rpt: 1
        ---
        Specifies the date when the license or ID is no longer valid.
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PLN.4
        """
        self._c_data[3] = (dt,)
