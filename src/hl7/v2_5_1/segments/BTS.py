from __future__ import annotations
from ...base import HL7Segment
from ..data_types.NM import NM
from ..data_types.ST import ST


"""
Batch Trailer Segment - BTS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::BTS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    BTS,
    NM, ST
)

bts = BTS(  #  - The BTS segment defines the end of a batch
    batch_message_count=None,  # ST(...) 
    batch_comment=None,  # ST(...) 
    batch_totals=None,  # NM(...) 
)

-----END SEGMENT::BTS TEMPLATE-----
"""


class BTS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """BTS"""
    _hl7_name = """Batch Trailer Segment"""
    _hl7_description = """The BTS segment defines the end of a batch"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BTS"
    _c_length = (10, 80, 100,)
    _c_rpt = (1, 1, 65535,)
    _c_usage = ("O", "O", "O",)
    _c_components = (ST, ST, NM,)
    _c_aliases = ("BTS.1", "BTS.2", "BTS.3",)
    _c_names = ("Batch Message Count", "Batch Comment", "Batch Totals",)
    _c_attrs = ("batch_message_count", "batch_comment", "batch_totals",)
    # fmt: on

    def __init__(
        self,
        batch_message_count: ST | None = None,  # BTS.1
        batch_comment: ST | None = None,  # BTS.2
        batch_totals: NM | None = None,  # BTS.3
    ):
        """
        Batch Trailer Segment - `BTS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BTS>`_
        The BTS segment defines the end of a batch.

        :param batch_message_count: String Data (id: BTS.1 | len: 10 | use: O | rpt: 1)
        :param batch_comment: String Data (id: BTS.2 | len: 80 | use: O | rpt: 1)
        :param batch_totals: Numeric (id: BTS.3 | len: 100 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.batch_message_count = batch_message_count
        self.batch_comment = batch_comment
        self.batch_totals = batch_totals

    @property  # get BTS.1
    def batch_message_count(self) -> ST | None:
        """
        id: BTS.1 | len: 10 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTS.1
        """
        return self._c_data[0][0]

    @batch_message_count.setter  # set BTS.1
    def batch_message_count(self, st: ST | None):
        """
        id: BTS.1 | len: 10 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTS.1
        """
        self._c_data[0] = (st,)

    @property  # get BTS.2
    def batch_comment(self) -> ST | None:
        """
        id: BTS.2 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTS.2
        """
        return self._c_data[1][0]

    @batch_comment.setter  # set BTS.2
    def batch_comment(self, st: ST | None):
        """
        id: BTS.2 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTS.2
        """
        self._c_data[1] = (st,)

    @property
    def batch_totals(self) -> tuple[NM, ...] | tuple[None]:
        """
        id: BTS.3 | len: 100 | use: O | rpt: *
        ---
        return_type: tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTS.3
        """
        return self._c_data[2]

    @batch_totals.setter  # set BTS.3
    def batch_totals(self, nm: NM | tuple[NM] | None):
        """
        id: BTS.3 | len: 100 | use: O | rpt: *
        ---
        param_type: NM | tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTS.3
        """
        if isinstance(nm, tuple):
            self._c_data[2] = nm
        else:
            self._c_data[2] = (nm,)
