from __future__ import annotations
from ...base import DataType
from .TS import TS
from .IS import IS
from ..tables.DischargedToLocation import DischargedToLocation


"""
DataType - DLD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::DLD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DLD,
    TS, IS
)

dld = DLD(  # Discharge Location and Date - Specifies the healthcare facility to which the patient was discharged and the date
    discharge_location=_is,  # IS(...)  # Required.
    effective_date=None,  # TS(...) 
)

-----END COMPOSITE_DATA_TYPE::DLD TEMPLATE-----
"""


class DLD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 47
    _hl7_id = """DLD"""
    _hl7_name = """Discharge Location and Date"""
    _hl7_description = """Specifies the healthcare facility to which the patient was discharged and the date"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLD"
    _c_length = (20, 26,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "O",)
    _c_aliases = ("DLD.1", "DLD.2",)
    _c_components = (IS, TS,)
    _c_names = ("Discharge Location", "Effective Date",)
    _c_attrs = ("discharge_location", "effective_date",)
    # fmt: on

    def __init__(
        self,
        discharge_location: DischargedToLocation
        | IS
        | tuple[DischargedToLocation | IS, ...],  # DLD.1
        effective_date: TS | tuple[TS, ...] | None = None,  # DLD.2
    ):
        """
        Discharge Location and Date - `DLD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DLD>`_
        Specifies the healthcare facility to which the patient was discharged and the date.

        :param discharge_location: Specifies the healthcare facility to which the patient was discharged (id: DLD.1 | len: 20 | use: R | rpt: 1)
        :param effective_date: Specifies the date on which the patient was discharged to a healthcare facility (id: DLD.2 | len: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.discharge_location = discharge_location
        self.effective_date = effective_date

    @property  # get DLD.1
    def discharge_location(self) -> DischargedToLocation:
        """
        id: DLD.1 | len: 20 | use: R | rpt: 1
        ---
        Specifies the healthcare facility to which the patient was discharged. Refer to User-defined Table 0113 - Discharged to location for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLD.1
        """
        return self._c_data[0][0]

    @discharge_location.setter  # set DLD.1
    def discharge_location(self, discharged_to_location: DischargedToLocation):
        """
        id: DLD.1 | len: 20 | use: R | rpt: 1
        ---
        Specifies the healthcare facility to which the patient was discharged. Refer to User-defined Table 0113 - Discharged to location for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLD.1
        """
        self._c_data[0] = (discharged_to_location,)

    @property  # get DLD.2
    def effective_date(self) -> TS | None:
        """
        id: DLD.2 | len: 26 | use: O | rpt: 1
        ---
        Specifies the date on which the patient was discharged to a healthcare facility.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLD.2
        """
        return self._c_data[1][0]

    @effective_date.setter  # set DLD.2
    def effective_date(self, ts: TS | None):
        """
        id: DLD.2 | len: 26 | use: O | rpt: 1
        ---
        Specifies the date on which the patient was discharged to a healthcare facility.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLD.2
        """
        self._c_data[1] = (ts,)
