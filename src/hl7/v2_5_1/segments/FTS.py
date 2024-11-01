from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.NM import NM


"""
File Trailer Segment - FTS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::FTS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    FTS,
    ST, NM
)

fts = FTS(  #  - The FTS segment defines the end of a file
    file_batch_count=None,  # NM(...) 
    file_trailer_comment=None,  # ST(...) 
)

-----END SEGMENT::FTS TEMPLATE-----
"""


class FTS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """FTS"""
    _hl7_name = """File Trailer Segment"""
    _hl7_description = """The FTS segment defines the end of a file"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FTS"
    _c_length = (10, 80,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_components = (NM, ST,)
    _c_aliases = ("FTS.1", "FTS.2",)
    _c_names = ("File Batch Count", "File Trailer Comment",)
    _c_attrs = ("file_batch_count", "file_trailer_comment",)
    # fmt: on

    def __init__(
        self,
        file_batch_count: NM | tuple[NM, ...] | None = None,  # FTS.1
        file_trailer_comment: ST | tuple[ST, ...] | None = None,  # FTS.2
    ):
        """
        File Trailer Segment - `FTS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FTS>`_
        The FTS segment defines the end of a file.

        :param file_batch_count: Numeric (id: FTS.1 | len: 10 | use: O | rpt: 1)
        :param file_trailer_comment: String Data (id: FTS.2 | len: 80 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.file_batch_count = file_batch_count
        self.file_trailer_comment = file_trailer_comment

    @property  # get FTS.1
    def file_batch_count(self) -> NM | None:
        """
        id: FTS.1 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FTS.1
        """
        return self._c_data[0][0]

    @file_batch_count.setter  # set FTS.1
    def file_batch_count(self, nm: NM | None):
        """
        id: FTS.1 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FTS.1
        """
        self._c_data[0] = (nm,)

    @property  # get FTS.2
    def file_trailer_comment(self) -> ST | None:
        """
        id: FTS.2 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FTS.2
        """
        return self._c_data[1][0]

    @file_trailer_comment.setter  # set FTS.2
    def file_trailer_comment(self, st: ST | None):
        """
        id: FTS.2 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FTS.2
        """
        self._c_data[1] = (st,)
