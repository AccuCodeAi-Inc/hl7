from __future__ import annotations
from ...base import HL7Segment
from ..data_types.IS import IS
from ..data_types.PL import PL
from ..tables.BedStatus import BedStatus


"""
Bed Status Update - NPU
HL7 Version: 2.5.1

-----BEGIN SEGMENT::NPU TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    NPU,
    IS, PL
)

npu = NPU(  #  - The NPU segment allows the updating of census (bed status) data without sending patient-specific data
    bed_location=pl,  # PL(...)  # Required.
    bed_status=None,  # IS(...) 
)

-----END SEGMENT::NPU TEMPLATE-----
"""


class NPU(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """NPU"""
    _hl7_name = """Bed Status Update"""
    _hl7_description = """The NPU segment allows the updating of census (bed status) data without sending patient-specific data"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NPU"
    _c_length = (80, 1,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "O",)
    _c_components = (PL, IS,)
    _c_aliases = ("NPU.1", "NPU.2",)
    _c_names = ("Bed Location", "Bed Status",)
    _c_attrs = ("bed_location", "bed_status",)
    # fmt: on

    def __init__(
        self,
        bed_location: PL | tuple[PL, ...],  # NPU.1
        bed_status: BedStatus | IS | tuple[BedStatus | IS, ...] | None = None,  # NPU.2
    ):
        """
        Bed Status Update - `NPU <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NPU>`_
        The NPU segment allows the updating of census (bed status) data without sending patient-specific data. An example might include changing the status of a bed from housekeeping to unoccupied.

        :param bed_location: Person Location (id: NPU.1 | len: 80 | use: R | rpt: 1)
        :param bed_status: Coded value for user-defined tables (id: NPU.2 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.bed_location = bed_location
        self.bed_status = bed_status

    @property  # get NPU.1
    def bed_location(self) -> PL:
        """
        id: NPU.1 | len: 80 | use: R | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NPU.1
        """
        return self._c_data[0][0]

    @bed_location.setter  # set NPU.1
    def bed_location(self, pl: PL):
        """
        id: NPU.1 | len: 80 | use: R | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NPU.1
        """
        self._c_data[0] = (pl,)

    @property  # get NPU.2
    def bed_status(self) -> BedStatus | None:
        """
        id: NPU.2 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NPU.2
        """
        return self._c_data[1][0]

    @bed_status.setter  # set NPU.2
    def bed_status(self, bed_status: BedStatus | None):
        """
        id: NPU.2 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NPU.2
        """
        self._c_data[1] = (bed_status,)
