from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TX import TX
from ..data_types.XON import XON
from ..data_types.ST import ST
from ..data_types.TS import TS


"""
Software Segment - SFT
HL7 Version: 2.5.1

-----BEGIN SEGMENT::SFT TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SFT,
    TX, XON, ST, TS
)

sft = SFT(  #  - This segment provides additional information about the software product(s) used as a Sending Application
    software_vendor_organization=xon,  # XON(...)  # Required.
    software_certified_version_or_release_number=st,  # ST(...)  # Required.
    software_product_name=st,  # ST(...)  # Required.
    software_binary_id=st,  # ST(...)  # Required.
    software_product_information=None,  # TX(...) 
    software_install_date=None,  # TS(...) 
)

-----END SEGMENT::SFT TEMPLATE-----
"""


class SFT(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """SFT"""
    _hl7_name = """Software Segment"""
    _hl7_description = """This segment provides additional information about the software product(s) used as a Sending Application"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT"
    _c_length = (567, 15, 20, 20, 1024, 26,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "R", "R", "O", "O",)
    _c_components = (XON, ST, ST, ST, TX, TS,)
    _c_aliases = ("SFT.1", "SFT.2", "SFT.3", "SFT.4", "SFT.5", "SFT.6",)
    _c_names = ("Software Vendor Organization", "Software Certified Version or Release Number", "Software Product Name", "Software Binary ID", "Software Product Information", "Software Install Date",)
    _c_attrs = ("software_vendor_organization", "software_certified_version_or_release_number", "software_product_name", "software_binary_id", "software_product_information", "software_install_date",)
    # fmt: on

    def __init__(
        self,
        software_vendor_organization: XON | tuple[XON],  # SFT.1
        software_certified_version_or_release_number: ST | tuple[ST],  # SFT.2
        software_product_name: ST | tuple[ST],  # SFT.3
        software_binary_id: ST | tuple[ST],  # SFT.4
        software_product_information: TX | tuple[TX] | None = None,  # SFT.5
        software_install_date: TS | tuple[TS] | None = None,  # SFT.6
    ):
        """
                Software Segment - `SFT <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT>`_
                This segment provides additional information about the software product(s) used as a Sending Application. The primary purpose of this segment is for diagnostic use. There may be additional uses per site-specific agreements.

        Example: MSH [{ SFT }] …..

                :param software_vendor_organization: Extended Composite Name and Identification Number for Organizations (id: SFT.1 | len: 567 | use: R | rpt: 1)
                :param software_certified_version_or_release_number: String Data (id: SFT.2 | len: 15 | use: R | rpt: 1)
                :param software_product_name: String Data (id: SFT.3 | len: 20 | use: R | rpt: 1)
                :param software_binary_id: String Data (id: SFT.4 | len: 20 | use: R | rpt: 1)
                :param software_product_information: Text Data (id: SFT.5 | len: 1024 | use: O | rpt: 1)
                :param software_install_date: Time Stamp (id: SFT.6 | len: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.software_vendor_organization = software_vendor_organization
        self.software_certified_version_or_release_number = (
            software_certified_version_or_release_number
        )
        self.software_product_name = software_product_name
        self.software_binary_id = software_binary_id
        self.software_product_information = software_product_information
        self.software_install_date = software_install_date

    @property  # get SFT.1
    def software_vendor_organization(self) -> XON:
        """
        id: SFT.1 | len: 567 | use: R | rpt: 1
        ---
        return_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.1
        """
        return self._c_data[0][0]

    @software_vendor_organization.setter  # set SFT.1
    def software_vendor_organization(self, xon: XON):
        """
        id: SFT.1 | len: 567 | use: R | rpt: 1
        ---
        param_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.1
        """
        self._c_data[0] = (xon,)

    @property  # get SFT.2
    def software_certified_version_or_release_number(self) -> ST:
        """
        id: SFT.2 | len: 15 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.2
        """
        return self._c_data[1][0]

    @software_certified_version_or_release_number.setter  # set SFT.2
    def software_certified_version_or_release_number(self, st: ST):
        """
        id: SFT.2 | len: 15 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.2
        """
        self._c_data[1] = (st,)

    @property  # get SFT.3
    def software_product_name(self) -> ST:
        """
        id: SFT.3 | len: 20 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.3
        """
        return self._c_data[2][0]

    @software_product_name.setter  # set SFT.3
    def software_product_name(self, st: ST):
        """
        id: SFT.3 | len: 20 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.3
        """
        self._c_data[2] = (st,)

    @property  # get SFT.4
    def software_binary_id(self) -> ST:
        """
        id: SFT.4 | len: 20 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.4
        """
        return self._c_data[3][0]

    @software_binary_id.setter  # set SFT.4
    def software_binary_id(self, st: ST):
        """
        id: SFT.4 | len: 20 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.4
        """
        self._c_data[3] = (st,)

    @property  # get SFT.5
    def software_product_information(self) -> TX | None:
        """
        id: SFT.5 | len: 1024 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.5
        """
        return self._c_data[4][0]

    @software_product_information.setter  # set SFT.5
    def software_product_information(self, tx: TX | None):
        """
        id: SFT.5 | len: 1024 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.5
        """
        self._c_data[4] = (tx,)

    @property  # get SFT.6
    def software_install_date(self) -> TS | None:
        """
        id: SFT.6 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.6
        """
        return self._c_data[5][0]

    @software_install_date.setter  # set SFT.6
    def software_install_date(self, ts: TS | None):
        """
        id: SFT.6 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SFT.6
        """
        self._c_data[5] = (ts,)
