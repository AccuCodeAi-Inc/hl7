from __future__ import annotations
from ...base import DataType
from .ST import ST
from ..tables.Lastname import Lastname


"""
DataType - FN
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::FN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    FN,
    ST
)

fn = FN(  # Family Name - This data type allows full specification of the surname of a person
    surname=st,  # ST(...)  # Required.
    own_surname_prefix=None,  # ST(...) 
    own_surname=None,  # ST(...) 
    surname_prefix_from_partner_or_spouse=None,  # ST(...) 
    surname_from_partner_or_spouse=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::FN TEMPLATE-----
"""


class FN(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 194
    _hl7_id = """FN"""
    _hl7_name = """Family Name"""
    _hl7_description = """This data type allows full specification of the surname of a person"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN"
    _c_length = (50, 20, 50, 20, 50,)
    _c_rpt = (1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O",)
    _c_aliases = ("FN.1", "FN.2", "FN.3", "FN.4", "FN.5",)
    _c_components = (ST, ST, ST, ST, ST,)
    _c_names = ("Surname", "Own Surname Prefix", "Own Surname", "Surname Prefix From Partner/Spouse", "Surname From Partner/Spouse",)
    _c_attrs = ("surname", "own_surname_prefix", "own_surname", "surname_prefix_from_partner_or_spouse", "surname_from_partner_or_spouse",)
    # fmt: on

    def __init__(
        self,
        surname: Lastname | ST,  # FN.1
        own_surname_prefix: ST | None = None,  # FN.2
        own_surname: ST | None = None,  # FN.3
        surname_prefix_from_partner_or_spouse: ST | None = None,  # FN.4
        surname_from_partner_or_spouse: ST | None = None,  # FN.5
    ):
        """
        Family Name - `FN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FN>`_
        This data type allows full specification of the surname of a person. Where appropriate, it differentiates the person's own surname from that of the person's partner or spouse, in cases where the person's name may contain elements from either name. It also permits messages to distinguish the surname prefix (such as "van" or "de") from the surname root.

        :param surname: The atomic element of the person's family name (id: FN.1 | len: 50 | use: R | rpt: 1)
        :param own_surname_prefix: Internationalization usage for Germanic languages (id: FN.2 | len: 20 | use: O | rpt: 1)
        :param own_surname: The portion of the surname (in most Western usage, the last name) that is derived from the person's own surname, as distinguished from any portion that is derived from the surname of the person's partner or spouse (id: FN.3 | len: 50 | use: O | rpt: 1)
        :param surname_prefix_from_partner_or_spouse: Internationalization usage for Germanic languages (id: FN.4 | len: 20 | use: O | rpt: 1)
        :param surname_from_partner_or_spouse: The portion of the person's surname (in most Western usage, the last name) that is derived from the surname of the person's partner or spouse, as distinguished from the part derived from the person's own surname (id: FN.5 | len: 50 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.surname = surname
        self.own_surname_prefix = own_surname_prefix
        self.own_surname = own_surname
        self.surname_prefix_from_partner_or_spouse = (
            surname_prefix_from_partner_or_spouse
        )
        self.surname_from_partner_or_spouse = surname_from_partner_or_spouse

    @property  # get FN.1
    def surname(self) -> Lastname:
        """
        id: FN.1 | len: 50 | use: R | rpt: 1
        ---
        The atomic element of the person's family name. In most Western usage, this is the person's last name.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN.1
        """
        return self._c_data[0][0]

    @surname.setter  # set FN.1
    def surname(self, lastname: Lastname):
        """
        id: FN.1 | len: 50 | use: R | rpt: 1
        ---
        The atomic element of the person's family name. In most Western usage, this is the person's last name.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN.1
        """
        self._c_data[0] = (lastname,)

    @property  # get FN.2
    def own_surname_prefix(self) -> ST | None:
        """
        id: FN.2 | len: 20 | use: O | rpt: 1
        ---
        Internationalization usage for Germanic languages. This component is optional. An example of a <surname prefix> is the "van" in "Ludwig van Beethoven". Since the <surname prefix> doesn't sort completely alphabetically, it is reasonable to specify it as a separate sub-component of the PN and extended PN data types (XPN and XCN).
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN.2
        """
        return self._c_data[1][0]

    @own_surname_prefix.setter  # set FN.2
    def own_surname_prefix(self, st: ST | None):
        """
        id: FN.2 | len: 20 | use: O | rpt: 1
        ---
        Internationalization usage for Germanic languages. This component is optional. An example of a <surname prefix> is the "van" in "Ludwig van Beethoven". Since the <surname prefix> doesn't sort completely alphabetically, it is reasonable to specify it as a separate sub-component of the PN and extended PN data types (XPN and XCN).
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN.2
        """
        self._c_data[1] = (st,)

    @property  # get FN.3
    def own_surname(self) -> ST | None:
        """
        id: FN.3 | len: 50 | use: O | rpt: 1
        ---
        The portion of the surname (in most Western usage, the last name) that is derived from the person's own surname, as distinguished from any portion that is derived from the surname of the person's partner or spouse. This component is optional.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN.3
        """
        return self._c_data[2][0]

    @own_surname.setter  # set FN.3
    def own_surname(self, st: ST | None):
        """
        id: FN.3 | len: 50 | use: O | rpt: 1
        ---
        The portion of the surname (in most Western usage, the last name) that is derived from the person's own surname, as distinguished from any portion that is derived from the surname of the person's partner or spouse. This component is optional.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN.3
        """
        self._c_data[2] = (st,)

    @property  # get FN.4
    def surname_prefix_from_partner_or_spouse(self) -> ST | None:
        """
        id: FN.4 | len: 20 | use: O | rpt: 1
        ---
        Internationalization usage for Germanic languages. This component is optional. An example of a <surname prefix> is the van in "Ludwig van Beethoven". Since the <surname prefix> doesn't sort completely alphabetically, it is reasonable to specify it as a separate sub-component of the PN and extended PN data types (XPN and XCN).
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN.4
        """
        return self._c_data[3][0]

    @surname_prefix_from_partner_or_spouse.setter  # set FN.4
    def surname_prefix_from_partner_or_spouse(self, st: ST | None):
        """
        id: FN.4 | len: 20 | use: O | rpt: 1
        ---
        Internationalization usage for Germanic languages. This component is optional. An example of a <surname prefix> is the van in "Ludwig van Beethoven". Since the <surname prefix> doesn't sort completely alphabetically, it is reasonable to specify it as a separate sub-component of the PN and extended PN data types (XPN and XCN).
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN.4
        """
        self._c_data[3] = (st,)

    @property  # get FN.5
    def surname_from_partner_or_spouse(self) -> ST | None:
        """
        id: FN.5 | len: 50 | use: O | rpt: 1
        ---
        The portion of the person's surname (in most Western usage, the last name) that is derived from the surname of the person's partner or spouse, as distinguished from the part derived from the person's own surname. This component is optional.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN.5
        """
        return self._c_data[4][0]

    @surname_from_partner_or_spouse.setter  # set FN.5
    def surname_from_partner_or_spouse(self, st: ST | None):
        """
        id: FN.5 | len: 50 | use: O | rpt: 1
        ---
        The portion of the person's surname (in most Western usage, the last name) that is derived from the surname of the person's partner or spouse, as distinguished from the part derived from the person's own surname. This component is optional.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FN.5
        """
        self._c_data[4] = (st,)
