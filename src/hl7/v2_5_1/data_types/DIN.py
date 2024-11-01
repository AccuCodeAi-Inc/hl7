from __future__ import annotations
from ...base import DataType
from .TS import TS
from .CE import CE
from ..tables.Institution import Institution


"""
DataType - DIN
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::DIN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DIN,
    TS, CE
)

din = DIN(  # Date and Institution Name - Specifies the date and institution information where a staff member became active or inactive
    date=ts,  # TS(...)  # Required.
    institution_name=ce,  # CE(...)  # Required.
)

-----END COMPOSITE_DATA_TYPE::DIN TEMPLATE-----
"""


class DIN(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 510
    _hl7_id = """DIN"""
    _hl7_name = """Date and Institution Name"""
    _hl7_description = """Specifies the date and institution information where a staff member became active or inactive"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DIN"
    _c_length = (26, 483,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "R",)
    _c_aliases = ("DIN.1", "DIN.2",)
    _c_components = (TS, CE,)
    _c_names = ("Date", "Institution Name",)
    _c_attrs = ("date", "institution_name",)
    # fmt: on

    def __init__(
        self,
        date: TS | tuple[TS, ...],  # DIN.1
        institution_name: Institution | CE | tuple[Institution | CE, ...],  # DIN.2
    ):
        """
        Date and Institution Name - `DIN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DIN>`_
        Specifies the date and institution information where a staff member became active or inactive.

        :param date: Specifies the date when a staff member became active or inactive (id: DIN.1 | len: 26 | use: R | rpt: 1)
        :param institution_name: Specifies the institution where a staff member is or was active (id: DIN.2 | len: 483 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.date = date
        self.institution_name = institution_name

    @property  # get DIN.1
    def date(self) -> TS:
        """
        id: DIN.1 | len: 26 | use: R | rpt: 1
        ---
        Specifies the date when a staff member became active or inactive.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DIN.1
        """
        return self._c_data[0][0]

    @date.setter  # set DIN.1
    def date(self, ts: TS):
        """
        id: DIN.1 | len: 26 | use: R | rpt: 1
        ---
        Specifies the date when a staff member became active or inactive.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DIN.1
        """
        self._c_data[0] = (ts,)

    @property  # get DIN.2
    def institution_name(self) -> CE:
        """
        id: DIN.2 | len: 483 | use: R | rpt: 1
        ---
        Specifies the institution where a staff member is or was active. Refer to User-Defined Table0531 - Institutions for suggested values.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DIN.2
        """
        return self._c_data[1][0]

    @institution_name.setter  # set DIN.2
    def institution_name(self, ce: CE):
        """
        id: DIN.2 | len: 483 | use: R | rpt: 1
        ---
        Specifies the institution where a staff member is or was active. Refer to User-Defined Table0531 - Institutions for suggested values.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DIN.2
        """
        self._c_data[1] = (ce,)
