from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..data_types.HD import HD
from ..tables.FileLevelEventCode import FileLevelEventCode
from ..tables.Application import Application
from ..tables.MasterFileIdentifierCode import MasterFileIdentifierCode
from ..tables.ResponseLevel import ResponseLevel


"""
Master File Identification - MFI
HL7 Version: 2.5.1

-----BEGIN SEGMENT::MFI TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MFI,
    TS, CE, ID, HD
)

mfi = MFI(  #  - The Technical Steward for the MFI segment is CQ
    master_file_identifier=ce,  # CE(...)  # Required.
    master_file_application_identifier=None,  # HD(...) 
    file_level_event_code=id,  # ID(...)  # Required.
    entered_date_or_time=None,  # TS(...) 
    effective_date_or_time=None,  # TS(...) 
    response_level_code=id,  # ID(...)  # Required.
)

-----END SEGMENT::MFI TEMPLATE-----
"""


class MFI(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """MFI"""
    _hl7_name = """Master File Identification"""
    _hl7_description = """The Technical Steward for the MFI segment is CQ"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI"
    _c_length = (250, 180, 3, 26, 26, 2,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "R", "O", "O", "R",)
    _c_components = (CE, HD, ID, TS, TS, ID,)
    _c_aliases = ("MFI.1", "MFI.2", "MFI.3", "MFI.4", "MFI.5", "MFI.6",)
    _c_names = ("Master File Identifier", "Master File Application Identifier", "File-Level Event Code", "Entered Date/Time", "Effective Date/Time", "Response Level Code",)
    _c_attrs = ("master_file_identifier", "master_file_application_identifier", "file_level_event_code", "entered_date_or_time", "effective_date_or_time", "response_level_code",)
    # fmt: on

    def __init__(
        self,
        master_file_identifier: MasterFileIdentifierCode
        | CE
        | tuple[MasterFileIdentifierCode | CE, ...],  # MFI.1
        file_level_event_code: FileLevelEventCode
        | ID
        | tuple[FileLevelEventCode | ID, ...],  # MFI.3
        response_level_code: ResponseLevel
        | ID
        | tuple[ResponseLevel | ID, ...],  # MFI.6
        master_file_application_identifier: Application
        | HD
        | tuple[Application | HD, ...]
        | None = None,  # MFI.2
        entered_date_or_time: TS | tuple[TS, ...] | None = None,  # MFI.4
        effective_date_or_time: TS | tuple[TS, ...] | None = None,  # MFI.5
    ):
        """
        Master File Identification - `MFI <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI>`_
        The Technical Steward for the MFI segment is CQ.

        :param master_file_identifier: Coded Element (id: MFI.1 | len: 250 | use: R | rpt: 1)
        :param master_file_application_identifier: Hierarchic Designator (id: MFI.2 | len: 180 | use: O | rpt: 1)
        :param file_level_event_code: Coded values for HL7 tables (id: MFI.3 | len: 3 | use: R | rpt: 1)
        :param entered_date_or_time: Time Stamp (id: MFI.4 | len: 26 | use: O | rpt: 1)
        :param effective_date_or_time: Time Stamp (id: MFI.5 | len: 26 | use: O | rpt: 1)
        :param response_level_code: Coded values for HL7 tables (id: MFI.6 | len: 2 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.master_file_identifier = master_file_identifier
        self.master_file_application_identifier = master_file_application_identifier
        self.file_level_event_code = file_level_event_code
        self.entered_date_or_time = entered_date_or_time
        self.effective_date_or_time = effective_date_or_time
        self.response_level_code = response_level_code

    @property  # get MFI.1
    def master_file_identifier(self) -> MasterFileIdentifierCode:
        """
        id: MFI.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.1
        """
        return self._c_data[0][0]

    @master_file_identifier.setter  # set MFI.1
    def master_file_identifier(
        self, master_file_identifier_code: MasterFileIdentifierCode
    ):
        """
        id: MFI.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.1
        """
        self._c_data[0] = (master_file_identifier_code,)

    @property  # get MFI.2
    def master_file_application_identifier(self) -> Application | None:
        """
        id: MFI.2 | len: 180 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.2
        """
        return self._c_data[1][0]

    @master_file_application_identifier.setter  # set MFI.2
    def master_file_application_identifier(self, application: Application | None):
        """
        id: MFI.2 | len: 180 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.2
        """
        self._c_data[1] = (application,)

    @property  # get MFI.3
    def file_level_event_code(self) -> FileLevelEventCode:
        """
        id: MFI.3 | len: 3 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.3
        """
        return self._c_data[2][0]

    @file_level_event_code.setter  # set MFI.3
    def file_level_event_code(self, file_level_event_code: FileLevelEventCode):
        """
        id: MFI.3 | len: 3 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.3
        """
        self._c_data[2] = (file_level_event_code,)

    @property  # get MFI.4
    def entered_date_or_time(self) -> TS | None:
        """
        id: MFI.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.4
        """
        return self._c_data[3][0]

    @entered_date_or_time.setter  # set MFI.4
    def entered_date_or_time(self, ts: TS | None):
        """
        id: MFI.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.4
        """
        self._c_data[3] = (ts,)

    @property  # get MFI.5
    def effective_date_or_time(self) -> TS | None:
        """
        id: MFI.5 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.5
        """
        return self._c_data[4][0]

    @effective_date_or_time.setter  # set MFI.5
    def effective_date_or_time(self, ts: TS | None):
        """
        id: MFI.5 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.5
        """
        self._c_data[4] = (ts,)

    @property  # get MFI.6
    def response_level_code(self) -> ResponseLevel:
        """
        id: MFI.6 | len: 2 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.6
        """
        return self._c_data[5][0]

    @response_level_code.setter  # set MFI.6
    def response_level_code(self, response_level: ResponseLevel):
        """
        id: MFI.6 | len: 2 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFI.6
        """
        self._c_data[5] = (response_level,)
