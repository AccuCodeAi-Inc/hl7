from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.HD import HD
from ..data_types.TS import TS


"""
File Header Segment - FHS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::FHS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    FHS,
    ST, HD, TS
)

fhs = FHS(  #  - The FHS segment is used to head a file (group of batches)
    file_field_separator=st,  # ST(...)  # Required.
    file_encoding_characters=st,  # ST(...)  # Required.
    file_sending_application=None,  # HD(...) 
    file_sending_facility=None,  # HD(...) 
    file_receiving_application=None,  # HD(...) 
    file_receiving_facility=None,  # HD(...) 
    file_creation_date_or_time=None,  # TS(...) 
    file_security=None,  # ST(...) 
    file_name_or_id=None,  # ST(...) 
    file_header_comment=None,  # ST(...) 
    file_control_id=None,  # ST(...) 
    reference_file_control_id=None,  # ST(...) 
)

-----END SEGMENT::FHS TEMPLATE-----
"""


class FHS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """FHS"""
    _hl7_name = """File Header Segment"""
    _hl7_description = """The FHS segment is used to head a file (group of batches)"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FHS"
    _c_length = (1, 4, 227, 227, 227, 227, 26, 40, 20, 80, 20, 20,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (ST, ST, HD, HD, HD, HD, TS, ST, ST, ST, ST, ST,)
    _c_aliases = ("FHS.1", "FHS.2", "FHS.3", "FHS.4", "FHS.5", "FHS.6", "FHS.7", "FHS.8", "FHS.9", "FHS.10", "FHS.11", "FHS.12",)
    _c_names = ("File Field Separator", "File Encoding Characters", "File Sending Application", "File Sending Facility", "File Receiving Application", "File Receiving Facility", "File Creation Date/Time", "File Security", "File Name/ID", "File Header Comment", "File Control ID", "Reference File Control ID",)
    _c_attrs = ("file_field_separator", "file_encoding_characters", "file_sending_application", "file_sending_facility", "file_receiving_application", "file_receiving_facility", "file_creation_date_or_time", "file_security", "file_name_or_id", "file_header_comment", "file_control_id", "reference_file_control_id",)
    # fmt: on

    def __init__(
        self,
        file_field_separator: ST | tuple[ST, ...],  # FHS.1
        file_encoding_characters: ST | tuple[ST, ...],  # FHS.2
        file_sending_application: HD | tuple[HD, ...] | None = None,  # FHS.3
        file_sending_facility: HD | tuple[HD, ...] | None = None,  # FHS.4
        file_receiving_application: HD | tuple[HD, ...] | None = None,  # FHS.5
        file_receiving_facility: HD | tuple[HD, ...] | None = None,  # FHS.6
        file_creation_date_or_time: TS | tuple[TS, ...] | None = None,  # FHS.7
        file_security: ST | tuple[ST, ...] | None = None,  # FHS.8
        file_name_or_id: ST | tuple[ST, ...] | None = None,  # FHS.9
        file_header_comment: ST | tuple[ST, ...] | None = None,  # FHS.10
        file_control_id: ST | tuple[ST, ...] | None = None,  # FHS.11
        reference_file_control_id: ST | tuple[ST, ...] | None = None,  # FHS.12
    ):
        """
        File Header Segment - `FHS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FHS>`_
        The FHS segment is used to head a file (group of batches).

        :param file_field_separator: String Data (id: FHS.1 | len: 1 | use: R | rpt: 1)
        :param file_encoding_characters: String Data (id: FHS.2 | len: 4 | use: R | rpt: 1)
        :param file_sending_application: Hierarchic Designator (id: FHS.3 | len: 227 | use: O | rpt: 1)
        :param file_sending_facility: Hierarchic Designator (id: FHS.4 | len: 227 | use: O | rpt: 1)
        :param file_receiving_application: Hierarchic Designator (id: FHS.5 | len: 227 | use: O | rpt: 1)
        :param file_receiving_facility: Hierarchic Designator (id: FHS.6 | len: 227 | use: O | rpt: 1)
        :param file_creation_date_or_time: Time Stamp (id: FHS.7 | len: 26 | use: O | rpt: 1)
        :param file_security: String Data (id: FHS.8 | len: 40 | use: O | rpt: 1)
        :param file_name_or_id: String Data (id: FHS.9 | len: 20 | use: O | rpt: 1)
        :param file_header_comment: String Data (id: FHS.10 | len: 80 | use: O | rpt: 1)
        :param file_control_id: String Data (id: FHS.11 | len: 20 | use: O | rpt: 1)
        :param reference_file_control_id: String Data (id: FHS.12 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.file_field_separator = file_field_separator
        self.file_encoding_characters = file_encoding_characters
        self.file_sending_application = file_sending_application
        self.file_sending_facility = file_sending_facility
        self.file_receiving_application = file_receiving_application
        self.file_receiving_facility = file_receiving_facility
        self.file_creation_date_or_time = file_creation_date_or_time
        self.file_security = file_security
        self.file_name_or_id = file_name_or_id
        self.file_header_comment = file_header_comment
        self.file_control_id = file_control_id
        self.reference_file_control_id = reference_file_control_id

    @property  # get FHS.1
    def file_field_separator(self) -> ST:
        """
        id: FHS.1 | len: 1 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.1
        """
        return self._c_data[0][0]

    @file_field_separator.setter  # set FHS.1
    def file_field_separator(self, st: ST):
        """
        id: FHS.1 | len: 1 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.1
        """
        self._c_data[0] = (st,)

    @property  # get FHS.2
    def file_encoding_characters(self) -> ST:
        """
        id: FHS.2 | len: 4 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.2
        """
        return self._c_data[1][0]

    @file_encoding_characters.setter  # set FHS.2
    def file_encoding_characters(self, st: ST):
        """
        id: FHS.2 | len: 4 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.2
        """
        self._c_data[1] = (st,)

    @property  # get FHS.3
    def file_sending_application(self) -> HD | None:
        """
        id: FHS.3 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.3
        """
        return self._c_data[2][0]

    @file_sending_application.setter  # set FHS.3
    def file_sending_application(self, hd: HD | None):
        """
        id: FHS.3 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.3
        """
        self._c_data[2] = (hd,)

    @property  # get FHS.4
    def file_sending_facility(self) -> HD | None:
        """
        id: FHS.4 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.4
        """
        return self._c_data[3][0]

    @file_sending_facility.setter  # set FHS.4
    def file_sending_facility(self, hd: HD | None):
        """
        id: FHS.4 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.4
        """
        self._c_data[3] = (hd,)

    @property  # get FHS.5
    def file_receiving_application(self) -> HD | None:
        """
        id: FHS.5 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.5
        """
        return self._c_data[4][0]

    @file_receiving_application.setter  # set FHS.5
    def file_receiving_application(self, hd: HD | None):
        """
        id: FHS.5 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.5
        """
        self._c_data[4] = (hd,)

    @property  # get FHS.6
    def file_receiving_facility(self) -> HD | None:
        """
        id: FHS.6 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.6
        """
        return self._c_data[5][0]

    @file_receiving_facility.setter  # set FHS.6
    def file_receiving_facility(self, hd: HD | None):
        """
        id: FHS.6 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.6
        """
        self._c_data[5] = (hd,)

    @property  # get FHS.7
    def file_creation_date_or_time(self) -> TS | None:
        """
        id: FHS.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.7
        """
        return self._c_data[6][0]

    @file_creation_date_or_time.setter  # set FHS.7
    def file_creation_date_or_time(self, ts: TS | None):
        """
        id: FHS.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.7
        """
        self._c_data[6] = (ts,)

    @property  # get FHS.8
    def file_security(self) -> ST | None:
        """
        id: FHS.8 | len: 40 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.8
        """
        return self._c_data[7][0]

    @file_security.setter  # set FHS.8
    def file_security(self, st: ST | None):
        """
        id: FHS.8 | len: 40 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.8
        """
        self._c_data[7] = (st,)

    @property  # get FHS.9
    def file_name_or_id(self) -> ST | None:
        """
        id: FHS.9 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.9
        """
        return self._c_data[8][0]

    @file_name_or_id.setter  # set FHS.9
    def file_name_or_id(self, st: ST | None):
        """
        id: FHS.9 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.9
        """
        self._c_data[8] = (st,)

    @property  # get FHS.10
    def file_header_comment(self) -> ST | None:
        """
        id: FHS.10 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.10
        """
        return self._c_data[9][0]

    @file_header_comment.setter  # set FHS.10
    def file_header_comment(self, st: ST | None):
        """
        id: FHS.10 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.10
        """
        self._c_data[9] = (st,)

    @property  # get FHS.11
    def file_control_id(self) -> ST | None:
        """
        id: FHS.11 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.11
        """
        return self._c_data[10][0]

    @file_control_id.setter  # set FHS.11
    def file_control_id(self, st: ST | None):
        """
        id: FHS.11 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.11
        """
        self._c_data[10] = (st,)

    @property  # get FHS.12
    def reference_file_control_id(self) -> ST | None:
        """
        id: FHS.12 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.12
        """
        return self._c_data[11][0]

    @reference_file_control_id.setter  # set FHS.12
    def reference_file_control_id(self, st: ST | None):
        """
        id: FHS.12 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FHS.12
        """
        self._c_data[11] = (st,)
