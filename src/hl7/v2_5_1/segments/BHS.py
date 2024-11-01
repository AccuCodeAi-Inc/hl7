from __future__ import annotations
from ...base import HL7Segment
from ..data_types.HD import HD
from ..data_types.ST import ST
from ..data_types.TS import TS


"""
Batch Header Segment - BHS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::BHS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    BHS,
    HD, ST, TS
)

bhs = BHS(  #  - The BHS segment defines the start of a batch
    batch_field_separator=st,  # ST(...)  # Required.
    batch_encoding_characters=st,  # ST(...)  # Required.
    batch_sending_application=None,  # HD(...) 
    batch_sending_facility=None,  # HD(...) 
    batch_receiving_application=None,  # HD(...) 
    batch_receiving_facility=None,  # HD(...) 
    batch_creation_date_or_time=None,  # TS(...) 
    batch_security=None,  # ST(...) 
    batch_name_or_id_or_type=None,  # ST(...) 
    batch_comment=None,  # ST(...) 
    batch_control_id=None,  # ST(...) 
    reference_batch_control_id=None,  # ST(...) 
)

-----END SEGMENT::BHS TEMPLATE-----
"""


class BHS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """BHS"""
    _hl7_name = """Batch Header Segment"""
    _hl7_description = """The BHS segment defines the start of a batch"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BHS"
    _c_length = (1, 3, 227, 227, 227, 227, 26, 40, 20, 80, 20, 20,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (ST, ST, HD, HD, HD, HD, TS, ST, ST, ST, ST, ST,)
    _c_aliases = ("BHS.1", "BHS.2", "BHS.3", "BHS.4", "BHS.5", "BHS.6", "BHS.7", "BHS.8", "BHS.9", "BHS.10", "BHS.11", "BHS.12",)
    _c_names = ("Batch Field Separator", "Batch Encoding Characters", "Batch Sending Application", "Batch Sending Facility", "Batch Receiving Application", "Batch Receiving Facility ", "Batch Creation Date/Time", "Batch Security", "Batch Name/ID/Type", "Batch Comment", "Batch Control ID", "Reference Batch Control ID",)
    _c_attrs = ("batch_field_separator", "batch_encoding_characters", "batch_sending_application", "batch_sending_facility", "batch_receiving_application", "batch_receiving_facility", "batch_creation_date_or_time", "batch_security", "batch_name_or_id_or_type", "batch_comment", "batch_control_id", "reference_batch_control_id",)
    # fmt: on

    def __init__(
        self,
        batch_field_separator: ST | tuple[ST],  # BHS.1
        batch_encoding_characters: ST | tuple[ST],  # BHS.2
        batch_sending_application: HD | tuple[HD] | None = None,  # BHS.3
        batch_sending_facility: HD | tuple[HD] | None = None,  # BHS.4
        batch_receiving_application: HD | tuple[HD] | None = None,  # BHS.5
        batch_receiving_facility: HD | tuple[HD] | None = None,  # BHS.6
        batch_creation_date_or_time: TS | tuple[TS] | None = None,  # BHS.7
        batch_security: ST | tuple[ST] | None = None,  # BHS.8
        batch_name_or_id_or_type: ST | tuple[ST] | None = None,  # BHS.9
        batch_comment: ST | tuple[ST] | None = None,  # BHS.10
        batch_control_id: ST | tuple[ST] | None = None,  # BHS.11
        reference_batch_control_id: ST | tuple[ST] | None = None,  # BHS.12
    ):
        """
        Batch Header Segment - `BHS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BHS>`_
        The BHS segment defines the start of a batch.

        :param batch_field_separator: String Data (id: BHS.1 | len: 1 | use: R | rpt: 1)
        :param batch_encoding_characters: String Data (id: BHS.2 | len: 3 | use: R | rpt: 1)
        :param batch_sending_application: Hierarchic Designator (id: BHS.3 | len: 227 | use: O | rpt: 1)
        :param batch_sending_facility: Hierarchic Designator (id: BHS.4 | len: 227 | use: O | rpt: 1)
        :param batch_receiving_application: Hierarchic Designator (id: BHS.5 | len: 227 | use: O | rpt: 1)
        :param batch_receiving_facility: Hierarchic Designator (id: BHS.6 | len: 227 | use: O | rpt: 1)
        :param batch_creation_date_or_time: Time Stamp (id: BHS.7 | len: 26 | use: O | rpt: 1)
        :param batch_security: String Data (id: BHS.8 | len: 40 | use: O | rpt: 1)
        :param batch_name_or_id_or_type: String Data (id: BHS.9 | len: 20 | use: O | rpt: 1)
        :param batch_comment: String Data (id: BHS.10 | len: 80 | use: O | rpt: 1)
        :param batch_control_id: String Data (id: BHS.11 | len: 20 | use: O | rpt: 1)
        :param reference_batch_control_id: String Data (id: BHS.12 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.batch_field_separator = batch_field_separator
        self.batch_encoding_characters = batch_encoding_characters
        self.batch_sending_application = batch_sending_application
        self.batch_sending_facility = batch_sending_facility
        self.batch_receiving_application = batch_receiving_application
        self.batch_receiving_facility = batch_receiving_facility
        self.batch_creation_date_or_time = batch_creation_date_or_time
        self.batch_security = batch_security
        self.batch_name_or_id_or_type = batch_name_or_id_or_type
        self.batch_comment = batch_comment
        self.batch_control_id = batch_control_id
        self.reference_batch_control_id = reference_batch_control_id

    @property  # get BHS.1
    def batch_field_separator(self) -> ST:
        """
        id: BHS.1 | len: 1 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.1
        """
        return self._c_data[0][0]

    @batch_field_separator.setter  # set BHS.1
    def batch_field_separator(self, st: ST):
        """
        id: BHS.1 | len: 1 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.1
        """
        self._c_data[0] = (st,)

    @property  # get BHS.2
    def batch_encoding_characters(self) -> ST:
        """
        id: BHS.2 | len: 3 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.2
        """
        return self._c_data[1][0]

    @batch_encoding_characters.setter  # set BHS.2
    def batch_encoding_characters(self, st: ST):
        """
        id: BHS.2 | len: 3 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.2
        """
        self._c_data[1] = (st,)

    @property  # get BHS.3
    def batch_sending_application(self) -> HD | None:
        """
        id: BHS.3 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.3
        """
        return self._c_data[2][0]

    @batch_sending_application.setter  # set BHS.3
    def batch_sending_application(self, hd: HD | None):
        """
        id: BHS.3 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.3
        """
        self._c_data[2] = (hd,)

    @property  # get BHS.4
    def batch_sending_facility(self) -> HD | None:
        """
        id: BHS.4 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.4
        """
        return self._c_data[3][0]

    @batch_sending_facility.setter  # set BHS.4
    def batch_sending_facility(self, hd: HD | None):
        """
        id: BHS.4 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.4
        """
        self._c_data[3] = (hd,)

    @property  # get BHS.5
    def batch_receiving_application(self) -> HD | None:
        """
        id: BHS.5 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.5
        """
        return self._c_data[4][0]

    @batch_receiving_application.setter  # set BHS.5
    def batch_receiving_application(self, hd: HD | None):
        """
        id: BHS.5 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.5
        """
        self._c_data[4] = (hd,)

    @property  # get BHS.6
    def batch_receiving_facility(self) -> HD | None:
        """
        id: BHS.6 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.6
        """
        return self._c_data[5][0]

    @batch_receiving_facility.setter  # set BHS.6
    def batch_receiving_facility(self, hd: HD | None):
        """
        id: BHS.6 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.6
        """
        self._c_data[5] = (hd,)

    @property  # get BHS.7
    def batch_creation_date_or_time(self) -> TS | None:
        """
        id: BHS.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.7
        """
        return self._c_data[6][0]

    @batch_creation_date_or_time.setter  # set BHS.7
    def batch_creation_date_or_time(self, ts: TS | None):
        """
        id: BHS.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.7
        """
        self._c_data[6] = (ts,)

    @property  # get BHS.8
    def batch_security(self) -> ST | None:
        """
        id: BHS.8 | len: 40 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.8
        """
        return self._c_data[7][0]

    @batch_security.setter  # set BHS.8
    def batch_security(self, st: ST | None):
        """
        id: BHS.8 | len: 40 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.8
        """
        self._c_data[7] = (st,)

    @property  # get BHS.9
    def batch_name_or_id_or_type(self) -> ST | None:
        """
        id: BHS.9 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.9
        """
        return self._c_data[8][0]

    @batch_name_or_id_or_type.setter  # set BHS.9
    def batch_name_or_id_or_type(self, st: ST | None):
        """
        id: BHS.9 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.9
        """
        self._c_data[8] = (st,)

    @property  # get BHS.10
    def batch_comment(self) -> ST | None:
        """
        id: BHS.10 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.10
        """
        return self._c_data[9][0]

    @batch_comment.setter  # set BHS.10
    def batch_comment(self, st: ST | None):
        """
        id: BHS.10 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.10
        """
        self._c_data[9] = (st,)

    @property  # get BHS.11
    def batch_control_id(self) -> ST | None:
        """
        id: BHS.11 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.11
        """
        return self._c_data[10][0]

    @batch_control_id.setter  # set BHS.11
    def batch_control_id(self, st: ST | None):
        """
        id: BHS.11 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.11
        """
        self._c_data[10] = (st,)

    @property  # get BHS.12
    def reference_batch_control_id(self) -> ST | None:
        """
        id: BHS.12 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.12
        """
        return self._c_data[11][0]

    @reference_batch_control_id.setter  # set BHS.12
    def reference_batch_control_id(self, st: ST | None):
        """
        id: BHS.12 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BHS.12
        """
        self._c_data[11] = (st,)
