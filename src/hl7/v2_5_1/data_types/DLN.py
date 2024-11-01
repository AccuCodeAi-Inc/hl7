from __future__ import annotations
from ...base import DataType
from .IS import IS
from .DT import DT
from .ST import ST
from ..tables.DriverSLicenseIssuingAuthority import DriverSLicenseIssuingAuthority


"""
DataType - DLN
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::DLN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DLN,
    IS, DT, ST
)

dln = DLN(  # Driver License Number - This field contains the drivers license information
    license_number=st,  # ST(...)  # Required.
    issuing_state_province_country=None,  # IS(...) 
    expiration_date=None,  # DT(...) 
)

-----END COMPOSITE_DATA_TYPE::DLN TEMPLATE-----
"""


class DLN(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 66
    _hl7_id = """DLN"""
    _hl7_name = """Driver License Number"""
    _hl7_description = """This field contains the drivers license information"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLN"
    _c_length = (20, 20, 24,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("R", "O", "O",)
    _c_aliases = ("DLN.1", "DLN.2", "DLN.3",)
    _c_components = (ST, IS, DT,)
    _c_names = ("License Number", "Issuing State, Province, Country", "Expiration Date",)
    _c_attrs = ("license_number", "issuing_state_province_country", "expiration_date",)
    # fmt: on

    def __init__(
        self,
        license_number: ST | tuple[ST],  # DLN.1
        issuing_state_province_country: DriverSLicenseIssuingAuthority
        | IS
        | tuple[DriverSLicenseIssuingAuthority | IS]
        | None = None,  # DLN.2
        expiration_date: DT | tuple[DT] | None = None,  # DLN.3
    ):
        """
        Driver License Number - `DLN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DLN>`_
        This field contains the drivers license information. For state or province refer to official postal codes for that country; for country refer to ISO 3166 for codes.

        :param license_number: This field contains the drivers license number (id: DLN.1 | len: 20 | use: R | rpt: 1)
        :param issuing_state_province_country: Issuing authority for drivers license (id: DLN.2 | len: 20 | use: O | rpt: 1)
        :param expiration_date: Expiration date (DT) for drivers license (id: DLN.3 | len: 24 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.license_number = license_number
        self.issuing_state_province_country = issuing_state_province_country
        self.expiration_date = expiration_date

    @property  # get DLN.1
    def license_number(self) -> ST:
        """
        id: DLN.1 | len: 20 | use: R | rpt: 1
        ---
        This field contains the drivers license number.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLN.1
        """
        return self._c_data[0][0]

    @license_number.setter  # set DLN.1
    def license_number(self, st: ST):
        """
        id: DLN.1 | len: 20 | use: R | rpt: 1
        ---
        This field contains the drivers license number.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLN.1
        """
        self._c_data[0] = (st,)

    @property  # get DLN.2
    def issuing_state_province_country(self) -> DriverSLicenseIssuingAuthority | None:
        """
        id: DLN.2 | len: 20 | use: O | rpt: 1
        ---
        Issuing authority for drivers license. For state or province refer to official postal codes for that country; for country refer to ISO 3166 for codes. The ISO 3166 table has three separate forms of the country code: HL7 specifies that the 3-character (alphabetic) form be used for the country code. User-defined Table 0333 - Drivers license issuing authority is used as the HL7 identifier for the user-defined table of values for this component.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLN.2
        """
        return self._c_data[1][0]

    @issuing_state_province_country.setter  # set DLN.2
    def issuing_state_province_country(
        self, drivers_license_issuing_authority: DriverSLicenseIssuingAuthority | None
    ):
        """
        id: DLN.2 | len: 20 | use: O | rpt: 1
        ---
        Issuing authority for drivers license. For state or province refer to official postal codes for that country; for country refer to ISO 3166 for codes. The ISO 3166 table has three separate forms of the country code: HL7 specifies that the 3-character (alphabetic) form be used for the country code. User-defined Table 0333 - Drivers license issuing authority is used as the HL7 identifier for the user-defined table of values for this component.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLN.2
        """
        self._c_data[1] = (drivers_license_issuing_authority,)

    @property  # get DLN.3
    def expiration_date(self) -> DT | None:
        """
        id: DLN.3 | len: 24 | use: O | rpt: 1
        ---
        Expiration date (DT) for drivers license.
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLN.3
        """
        return self._c_data[2][0]

    @expiration_date.setter  # set DLN.3
    def expiration_date(self, dt: DT | None):
        """
        id: DLN.3 | len: 24 | use: O | rpt: 1
        ---
        Expiration date (DT) for drivers license.
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLN.3
        """
        self._c_data[2] = (dt,)
