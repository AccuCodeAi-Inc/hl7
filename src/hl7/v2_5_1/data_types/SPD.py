from __future__ import annotations
from ...base import DataType
from .DT import DT
from .ST import ST
from .ID import ID
from ..tables.CertificationStatus import CertificationStatus


"""
DataType - SPD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::SPD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SPD,
    DT, ST, ID
)

spd = SPD(  # Specialty Description - This data type specifies the practitioners specialty and related information
    specialty_name=st,  # ST(...)  # Required.
    governing_board=None,  # ST(...) 
    eligible_or_certified=None,  # ID(...) 
    date_of_certification=None,  # DT(...) 
)

-----END COMPOSITE_DATA_TYPE::SPD TEMPLATE-----
"""


class SPD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 112
    _hl7_id = """SPD"""
    _hl7_name = """Specialty Description"""
    _hl7_description = """This data type specifies the practitioners specialty and related information"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPD"
    _c_length = (50, 50, 1, 8,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O",)
    _c_aliases = ("SPD.1", "SPD.2", "SPD.3", "SPD.4",)
    _c_components = (ST, ST, ID, DT,)
    _c_names = ("Specialty Name", "Governing Board", "Eligible Or Certified", "Date Of Certification",)
    _c_attrs = ("specialty_name", "governing_board", "eligible_or_certified", "date_of_certification",)
    # fmt: on

    def __init__(
        self,
        specialty_name: ST,  # SPD.1
        governing_board: ST | None = None,  # SPD.2
        eligible_or_certified: CertificationStatus | ID | None = None,  # SPD.3
        date_of_certification: DT | None = None,  # SPD.4
    ):
        """
        Specialty Description - `SPD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPD>`_
        This data type specifies the practitioners specialty and related information.

        :param specialty_name: Identifies the providers specialty (id: SPD.1 | len: 50 | use: R | rpt: 1)
        :param governing_board: Identifies the governing body providing for the specialty (id: SPD.2 | len: 50 | use: O | rpt: 1)
        :param eligible_or_certified: Specifies the certification status (id: SPD.3 | len: 1 | use: O | rpt: 1)
        :param date_of_certification: Specifies when certification occurred (id: SPD.4 | len: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.specialty_name = specialty_name
        self.governing_board = governing_board
        self.eligible_or_certified = eligible_or_certified
        self.date_of_certification = date_of_certification

    @property  # get SPD.1
    def specialty_name(self) -> ST:
        """
        id: SPD.1 | len: 50 | use: R | rpt: 1
        ---
        Identifies the providers specialty.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPD.1
        """
        return self._c_data[0][0]

    @specialty_name.setter  # set SPD.1
    def specialty_name(self, st: ST):
        """
        id: SPD.1 | len: 50 | use: R | rpt: 1
        ---
        Identifies the providers specialty.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPD.1
        """
        self._c_data[0] = (st,)

    @property  # get SPD.2
    def governing_board(self) -> ST | None:
        """
        id: SPD.2 | len: 50 | use: O | rpt: 1
        ---
        Identifies the governing body providing for the specialty.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPD.2
        """
        return self._c_data[1][0]

    @governing_board.setter  # set SPD.2
    def governing_board(self, st: ST | None):
        """
        id: SPD.2 | len: 50 | use: O | rpt: 1
        ---
        Identifies the governing body providing for the specialty.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPD.2
        """
        self._c_data[1] = (st,)

    @property  # get SPD.3
    def eligible_or_certified(self) -> CertificationStatus | None:
        """
        id: SPD.3 | len: 1 | use: O | rpt: 1
        ---
        Specifies the certification status. Refer to HL7 Table 0337 - Certification status for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPD.3
        """
        return self._c_data[2][0]

    @eligible_or_certified.setter  # set SPD.3
    def eligible_or_certified(self, certification_status: CertificationStatus | None):
        """
        id: SPD.3 | len: 1 | use: O | rpt: 1
        ---
        Specifies the certification status. Refer to HL7 Table 0337 - Certification status for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPD.3
        """
        self._c_data[2] = (certification_status,)

    @property  # get SPD.4
    def date_of_certification(self) -> DT | None:
        """
        id: SPD.4 | len: 8 | use: O | rpt: 1
        ---
        Specifies when certification occurred.
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPD.4
        """
        return self._c_data[3][0]

    @date_of_certification.setter  # set SPD.4
    def date_of_certification(self, dt: DT | None):
        """
        id: SPD.4 | len: 8 | use: O | rpt: 1
        ---
        Specifies when certification occurred.
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPD.4
        """
        self._c_data[3] = (dt,)
