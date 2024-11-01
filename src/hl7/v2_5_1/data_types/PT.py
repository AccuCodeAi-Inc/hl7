from __future__ import annotations
from ...base import DataType
from .ID import ID
from ..tables.ProcessingMode import ProcessingMode
from ..tables.ProcessingId import ProcessingId


"""
DataType - PT
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::PT TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PT,
    ID
)

pt = PT(  # Processing Type - This data type indicates whether to process a message as defined in HL7 Application (level 7) Processing rules
    processing_id=None,  # ID(...) 
    processing_mode=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::PT TEMPLATE-----
"""


class PT(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 3
    _hl7_id = """PT"""
    _hl7_name = """Processing Type"""
    _hl7_description = """This data type indicates whether to process a message as defined in HL7 Application (level 7) Processing rules"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PT"
    _c_length = (1, 1,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_aliases = ("PT.1", "PT.2",)
    _c_components = (ID, ID,)
    _c_names = ("Processing Id", "Processing Mode",)
    _c_attrs = ("processing_id", "processing_mode",)
    # fmt: on

    def __init__(
        self,
        processing_id: ProcessingId
        | ID
        | tuple[ProcessingId | ID]
        | None = None,  # PT.1
        processing_mode: ProcessingMode
        | ID
        | tuple[ProcessingMode | ID]
        | None = None,  # PT.2
    ):
        """
        Processing Type - `PT <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PT>`_
        This data type indicates whether to process a message as defined in HL7 Application (level 7) Processing rules.

        :param processing_id: A value that defines whether the message is part of a production, training, or debugging system (id: PT.1 | len: 1 | use: O | rpt: 1)
        :param processing_mode: A value that defines whether the message is part of an archival process or an initial load (id: PT.2 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.processing_id = processing_id
        self.processing_mode = processing_mode

    @property  # get PT.1
    def processing_id(self) -> ProcessingId | None:
        """
        id: PT.1 | len: 1 | use: O | rpt: 1
        ---
        A value that defines whether the message is part of a production, training, or debugging system. Refer to HL7 Table 0103 - Processing ID for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PT.1
        """
        return self._c_data[0][0]

    @processing_id.setter  # set PT.1
    def processing_id(self, processing_id: ProcessingId | None):
        """
        id: PT.1 | len: 1 | use: O | rpt: 1
        ---
        A value that defines whether the message is part of a production, training, or debugging system. Refer to HL7 Table 0103 - Processing ID for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PT.1
        """
        self._c_data[0] = (processing_id,)

    @property  # get PT.2
    def processing_mode(self) -> ProcessingMode | None:
        """
        id: PT.2 | len: 1 | use: O | rpt: 1
        ---
        A value that defines whether the message is part of an archival process or an initial load. Refer to HL7 Table 0207 - Processing mode for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PT.2
        """
        return self._c_data[1][0]

    @processing_mode.setter  # set PT.2
    def processing_mode(self, processing_mode: ProcessingMode | None):
        """
        id: PT.2 | len: 1 | use: O | rpt: 1
        ---
        A value that defines whether the message is part of an archival process or an initial load. Refer to HL7 Table 0207 - Processing mode for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PT.2
        """
        self._c_data[1] = (processing_mode,)
