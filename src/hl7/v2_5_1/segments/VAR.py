from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.EI import EI
from ..data_types.XCN import XCN


"""
Variance - VAR
HL7 Version: 2.5.1

-----BEGIN SEGMENT::VAR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    VAR,
    TS, ST, CE, EI, XCN
)

var = VAR(  #  - The variance segment contains the data necessary to describe differences that may have occurred at the time when a healthcare event was documented
    variance_instance_id=ei,  # EI(...)  # Required.
    documented_date_or_time=ts,  # TS(...)  # Required.
    stated_variance_date_or_time=None,  # TS(...) 
    variance_originator=None,  # XCN(...) 
    variance_classification=None,  # CE(...) 
    variance_description=None,  # ST(...) 
)

-----END SEGMENT::VAR TEMPLATE-----
"""


class VAR(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """VAR"""
    _hl7_name = """Variance"""
    _hl7_description = """The variance segment contains the data necessary to describe differences that may have occurred at the time when a healthcare event was documented"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR"
    _c_length = (60, 26, 26, 250, 250, 512,)
    _c_rpt = (1, 1, 1, 65535, 1, 65535,)
    _c_usage = ("R", "R", "O", "O", "O", "O",)
    _c_components = (EI, TS, TS, XCN, CE, ST,)
    _c_aliases = ("VAR.1", "VAR.2", "VAR.3", "VAR.4", "VAR.5", "VAR.6",)
    _c_names = ("Variance Instance ID", "Documented Date/Time", "Stated Variance Date/Time", "Variance Originator", "Variance Classification", "Variance Description",)
    _c_attrs = ("variance_instance_id", "documented_date_or_time", "stated_variance_date_or_time", "variance_originator", "variance_classification", "variance_description",)
    # fmt: on

    def __init__(
        self,
        variance_instance_id: EI,  # VAR.1
        documented_date_or_time: TS,  # VAR.2
        stated_variance_date_or_time: TS | None = None,  # VAR.3
        variance_originator: XCN | None = None,  # VAR.4
        variance_classification: CE | None = None,  # VAR.5
        variance_description: ST | None = None,  # VAR.6
    ):
        """
        Variance - `VAR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR>`_
        The variance segment contains the data necessary to describe differences that may have occurred at the time when a healthcare event was documented.

        :param variance_instance_id: Entity Identifier (id: VAR.1 | len: 60 | use: R | rpt: 1)
        :param documented_date_or_time: Time Stamp (id: VAR.2 | len: 26 | use: R | rpt: 1)
        :param stated_variance_date_or_time: Time Stamp (id: VAR.3 | len: 26 | use: O | rpt: 1)
        :param variance_originator: Extended Composite ID Number and Name for Persons (id: VAR.4 | len: 250 | use: O | rpt: *)
        :param variance_classification: Coded Element (id: VAR.5 | len: 250 | use: O | rpt: 1)
        :param variance_description: String Data (id: VAR.6 | len: 512 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.variance_instance_id = variance_instance_id
        self.documented_date_or_time = documented_date_or_time
        self.stated_variance_date_or_time = stated_variance_date_or_time
        self.variance_originator = variance_originator
        self.variance_classification = variance_classification
        self.variance_description = variance_description

    @property  # get VAR.1
    def variance_instance_id(self) -> EI:
        """
        id: VAR.1 | len: 60 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.1
        """
        return self._c_data[0][0]

    @variance_instance_id.setter  # set VAR.1
    def variance_instance_id(self, ei: EI):
        """
        id: VAR.1 | len: 60 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.1
        """
        self._c_data[0] = (ei,)

    @property  # get VAR.2
    def documented_date_or_time(self) -> TS:
        """
        id: VAR.2 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.2
        """
        return self._c_data[1][0]

    @documented_date_or_time.setter  # set VAR.2
    def documented_date_or_time(self, ts: TS):
        """
        id: VAR.2 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.2
        """
        self._c_data[1] = (ts,)

    @property  # get VAR.3
    def stated_variance_date_or_time(self) -> TS | None:
        """
        id: VAR.3 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.3
        """
        return self._c_data[2][0]

    @stated_variance_date_or_time.setter  # set VAR.3
    def stated_variance_date_or_time(self, ts: TS | None):
        """
        id: VAR.3 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.3
        """
        self._c_data[2] = (ts,)

    @property
    def variance_originator(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: VAR.4 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.4
        """
        return self._c_data[3]

    @variance_originator.setter  # set VAR.4
    def variance_originator(self, xcn: XCN | tuple[XCN] | None):
        """
        id: VAR.4 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.4
        """
        if isinstance(xcn, tuple):
            self._c_data[3] = xcn
        else:
            self._c_data[3] = (xcn,)

    @property  # get VAR.5
    def variance_classification(self) -> CE | None:
        """
        id: VAR.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.5
        """
        return self._c_data[4][0]

    @variance_classification.setter  # set VAR.5
    def variance_classification(self, ce: CE | None):
        """
        id: VAR.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.5
        """
        self._c_data[4] = (ce,)

    @property
    def variance_description(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: VAR.6 | len: 512 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.6
        """
        return self._c_data[5]

    @variance_description.setter  # set VAR.6
    def variance_description(self, st: ST | tuple[ST] | None):
        """
        id: VAR.6 | len: 512 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VAR.6
        """
        if isinstance(st, tuple):
            self._c_data[5] = st
        else:
            self._c_data[5] = (st,)
