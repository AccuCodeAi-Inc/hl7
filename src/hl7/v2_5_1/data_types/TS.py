from __future__ import annotations
from ...base import DataType
from .ID import ID
from .DTM import DTM
from ..tables.Precision import Precision


"""
DataType - TS
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::TS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    TS,
    ID, DTM
)

ts = TS(  # Time Stamp - Specifies a point in time
    time=dtm,  # DTM(...)  # Required.
    degree_of_precision=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::TS TEMPLATE-----
"""


class TS(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 26
    _hl7_id = """TS"""
    _hl7_name = """Time Stamp"""
    _hl7_description = """Specifies a point in time"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TS"
    _c_length = (24, 1,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "B",)
    _c_aliases = ("TS.1", "TS.2",)
    _c_components = (DTM, ID,)
    _c_names = ("Time", "Degree Of Precision",)
    _c_attrs = ("time", "degree_of_precision",)
    # fmt: on

    def __init__(
        self,
        time: DTM,  # TS.1
        degree_of_precision: Precision | ID | None = None,  # TS.2
    ):
        """
                Time Stamp - `TS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TS>`_
                Specifies a point in time.

        Format: YYYY[MM[DD[HH[MM[SS[.S[S[S[S]]]]]]]]][+/-ZZZZ]^<degree of precision>

                :param time: The point in time (id: TS.1 | len: 24 | use: R | rpt: 1)
                :param degree_of_precision: Retained only for purposes of backward compatibility as of v 2 (id: TS.2 | len: 1 | use: B | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.time = time
        self.degree_of_precision = degree_of_precision

    @property  # get TS.1
    def time(self) -> DTM:
        """
        id: TS.1 | len: 24 | use: R | rpt: 1
        ---
        The point in time.
        ---
        return_type: DTM: Date/Time
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TS.1
        """
        return self._c_data[0][0]

    @time.setter  # set TS.1
    def time(self, dtm: DTM):
        """
        id: TS.1 | len: 24 | use: R | rpt: 1
        ---
        The point in time.
        ---
        param_type: DTM: Date/Time
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TS.1
        """
        self._c_data[0] = (dtm,)

    @property  # get TS.2
    def degree_of_precision(self) -> Precision | None:
        """
                id: TS.2 | len: 1 | use: B | rpt: 1
                ---
                Retained only for purposes of backward compatibility as of v 2.3. Refer to component 1 for current method of designating degree of precision.

        Indicates the degree of precision of the time stamp (Y = year, L = month, D = day, H = hour, M = minute, S = second). Refer to HL7 Table 0529 - Precision for valid value.
                ---
                return_type: ID: Coded values for HL7 tables
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TS.2
        """
        return self._c_data[1][0]

    @degree_of_precision.setter  # set TS.2
    def degree_of_precision(self, precision: Precision | None):
        """
                id: TS.2 | len: 1 | use: B | rpt: 1
                ---
                Retained only for purposes of backward compatibility as of v 2.3. Refer to component 1 for current method of designating degree of precision.

        Indicates the degree of precision of the time stamp (Y = year, L = month, D = day, H = hour, M = minute, S = second). Refer to HL7 Table 0529 - Precision for valid value.
                ---
                param_type: ID: Coded values for HL7 tables
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TS.2
        """
        self._c_data[1] = (precision,)
