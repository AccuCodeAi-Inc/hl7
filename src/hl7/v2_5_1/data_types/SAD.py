from __future__ import annotations
from ...base import DataType
from .ST import ST


"""
DataType - SAD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::SAD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SAD,
    ST
)

sad = SAD(  # Street Address - This data type specifies an entity's street address and associated detail
    street_or_mailing_address=None,  # ST(...) 
    street_name=None,  # ST(...) 
    dwelling_number=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::SAD TEMPLATE-----
"""


class SAD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 184
    _hl7_id = """SAD"""
    _hl7_name = """Street Address"""
    _hl7_description = """This data type specifies an entity's street address and associated detail"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAD"
    _c_length = (120, 50, 12,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("O", "O", "O",)
    _c_aliases = ("SAD.1", "SAD.2", "SAD.3",)
    _c_components = (ST, ST, ST,)
    _c_names = ("Street Or Mailing Address", "Street Name", "Dwelling Number",)
    _c_attrs = ("street_or_mailing_address", "street_name", "dwelling_number",)
    # fmt: on

    def __init__(
        self,
        street_or_mailing_address: ST | None = None,  # SAD.1
        street_name: ST | None = None,  # SAD.2
        dwelling_number: ST | None = None,  # SAD.3
    ):
        """
        Street Address - `SAD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAD>`_
        This data type specifies an entity's street address and associated detail.

        :param street_or_mailing_address: This component specifies the street or mailing address of a person or institution (id: SAD.1 | len: 120 | use: O | rpt: 1)
        :param street_name:  (id: SAD.2 | len: 50 | use: O | rpt: 1)
        :param dwelling_number:  (id: SAD.3 | len: 12 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.street_or_mailing_address = street_or_mailing_address
        self.street_name = street_name
        self.dwelling_number = dwelling_number

    @property  # get SAD.1
    def street_or_mailing_address(self) -> ST | None:
        """
        id: SAD.1 | len: 120 | use: O | rpt: 1
        ---
        This component specifies the street or mailing address of a person or institution. When referencing an institution, this first component is used to specify the institution name. When used in connection with a person, this component specifies the first line of the address.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAD.1
        """
        return self._c_data[0][0]

    @street_or_mailing_address.setter  # set SAD.1
    def street_or_mailing_address(self, st: ST | None):
        """
        id: SAD.1 | len: 120 | use: O | rpt: 1
        ---
        This component specifies the street or mailing address of a person or institution. When referencing an institution, this first component is used to specify the institution name. When used in connection with a person, this component specifies the first line of the address.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAD.1
        """
        self._c_data[0] = (st,)

    @property  # get SAD.2
    def street_name(self) -> ST | None:
        """
        id: SAD.2 | len: 50 | use: O | rpt: 1
        ---
        None
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAD.2
        """
        return self._c_data[1][0]

    @street_name.setter  # set SAD.2
    def street_name(self, st: ST | None):
        """
        id: SAD.2 | len: 50 | use: O | rpt: 1
        ---
        None
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAD.2
        """
        self._c_data[1] = (st,)

    @property  # get SAD.3
    def dwelling_number(self) -> ST | None:
        """
        id: SAD.3 | len: 12 | use: O | rpt: 1
        ---
        None
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAD.3
        """
        return self._c_data[2][0]

    @dwelling_number.setter  # set SAD.3
    def dwelling_number(self, st: ST | None):
        """
        id: SAD.3 | len: 12 | use: O | rpt: 1
        ---
        None
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SAD.3
        """
        self._c_data[2] = (st,)
