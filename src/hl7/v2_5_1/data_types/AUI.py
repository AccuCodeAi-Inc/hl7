from __future__ import annotations
from ...base import DataType
from .DT import DT
from .ST import ST


"""
DataType - AUI
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::AUI TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    AUI,
    DT, ST
)

aui = AUI(  # Authorization Information - This data type specifies the identifier or code for an insurance authorization instance and its associated detail
    authorization_number=None,  # ST(...) 
    date=None,  # DT(...) 
    source=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::AUI TEMPLATE-----
"""


class AUI(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 239
    _hl7_id = """AUI"""
    _hl7_name = """Authorization Information"""
    _hl7_description = """This data type specifies the identifier or code for an insurance authorization instance and its associated detail"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUI"
    _c_length = (30, 8, 199,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("O", "O", "O",)
    _c_aliases = ("AUI.1", "AUI.2", "AUI.3",)
    _c_components = (ST, DT, ST,)
    _c_names = ("Authorization Number", "Date", "Source",)
    _c_attrs = ("authorization_number", "date", "source",)
    # fmt: on

    def __init__(
        self,
        authorization_number: ST | None = None,  # AUI.1
        date: DT | None = None,  # AUI.2
        source: ST | None = None,  # AUI.3
    ):
        """
        Authorization Information - `AUI <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AUI>`_
        This data type specifies the identifier or code for an insurance authorization instance and its associated detail.

        :param authorization_number: Identifier assigned to the authorization (id: AUI.1 | len: 30 | use: O | rpt: 1)
        :param date: Date of authorization (id: AUI.2 | len: 8 | use: O | rpt: 1)
        :param source: Source of authorization (id: AUI.3 | len: 199 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.authorization_number = authorization_number
        self.date = date
        self.source = source

    @property  # get AUI.1
    def authorization_number(self) -> ST | None:
        """
        id: AUI.1 | len: 30 | use: O | rpt: 1
        ---
        Identifier assigned to the authorization.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUI.1
        """
        return self._c_data[0][0]

    @authorization_number.setter  # set AUI.1
    def authorization_number(self, st: ST | None):
        """
        id: AUI.1 | len: 30 | use: O | rpt: 1
        ---
        Identifier assigned to the authorization.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUI.1
        """
        self._c_data[0] = (st,)

    @property  # get AUI.2
    def date(self) -> DT | None:
        """
        id: AUI.2 | len: 8 | use: O | rpt: 1
        ---
        Date of authorization.
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUI.2
        """
        return self._c_data[1][0]

    @date.setter  # set AUI.2
    def date(self, dt: DT | None):
        """
        id: AUI.2 | len: 8 | use: O | rpt: 1
        ---
        Date of authorization.
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUI.2
        """
        self._c_data[1] = (dt,)

    @property  # get AUI.3
    def source(self) -> ST | None:
        """
        id: AUI.3 | len: 199 | use: O | rpt: 1
        ---
        Source of authorization.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUI.3
        """
        return self._c_data[2][0]

    @source.setter  # set AUI.3
    def source(self, st: ST | None):
        """
        id: AUI.3 | len: 199 | use: O | rpt: 1
        ---
        Source of authorization.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUI.3
        """
        self._c_data[2] = (st,)
