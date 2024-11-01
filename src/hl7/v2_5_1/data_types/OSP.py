from __future__ import annotations
from ...base import DataType
from .DT import DT
from .CNE import CNE
from ..tables.OccurrenceSpan import OccurrenceSpan


"""
DataType - OSP
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::OSP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OSP,
    DT, CNE
)

osp = OSP(  # Occurrence Span Code and Date - A code and the related dates that identify an event that relates to the payment of the claim
    occurrence_span_code=cne,  # CNE(...)  # Required.
    occurrence_span_start_date=None,  # DT(...) 
    occurrence_span_stop_date=None,  # DT(...) 
)

-----END COMPOSITE_DATA_TYPE::OSP TEMPLATE-----
"""


class OSP(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 723
    _hl7_id = """OSP"""
    _hl7_name = """Occurrence Span Code and Date"""
    _hl7_description = """A code and the related dates that identify an event that relates to the payment of the claim"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSP"
    _c_length = (705, 8, 8,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("R", "C", "C",)
    _c_aliases = ("OSP.1", "OSP.2", "OSP.3",)
    _c_components = (CNE, DT, DT,)
    _c_names = ("Occurrence Span Code", "Occurrence Span Start Date", "Occurrence Span Stop Date",)
    _c_attrs = ("occurrence_span_code", "occurrence_span_start_date", "occurrence_span_stop_date",)
    # fmt: on

    def __init__(
        self,
        occurrence_span_code: OccurrenceSpan
        | CNE
        | tuple[OccurrenceSpan | CNE],  # OSP.1
        occurrence_span_start_date: DT | tuple[DT] | None = None,  # OSP.2
        occurrence_span_stop_date: DT | tuple[DT] | None = None,  # OSP.3
    ):
        """
               Occurrence Span Code and Date - `OSP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OSP>`_
               A code and the related dates that identify an event that relates to the payment of the claim. For example, Prior Stay Dates which is the from/through dates given by the patient of any hospital stay that ended within 60 days of this hospital or SNF admission.

        Example: |71&Prior Stay Date&NUBC^20030106^20030107|

               :param occurrence_span_code: The date an event started that relates to the payment of a claim (id: OSP.1 | len: 705 | use: R | rpt: 1)
               :param occurrence_span_start_date: The date an event ended that relates to the payment of a claim (id: OSP.2 | len: 8 | use: C | rpt: 1)
               :param occurrence_span_stop_date:  (id: OSP.3 | len: 8 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.occurrence_span_code = occurrence_span_code
        self.occurrence_span_start_date = occurrence_span_start_date
        self.occurrence_span_stop_date = occurrence_span_stop_date

    @property  # get OSP.1
    def occurrence_span_code(self) -> CNE:
        """
        id: OSP.1 | len: 705 | use: R | rpt: 1
        ---
        The date an event started that relates to the payment of a claim.
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSP.1
        """
        return self._c_data[0][0]

    @occurrence_span_code.setter  # set OSP.1
    def occurrence_span_code(self, cne: CNE):
        """
        id: OSP.1 | len: 705 | use: R | rpt: 1
        ---
        The date an event started that relates to the payment of a claim.
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSP.1
        """
        self._c_data[0] = (cne,)

    @property  # get OSP.2
    def occurrence_span_start_date(self) -> DT | None:
        """
        id: OSP.2 | len: 8 | use: C | rpt: 1
        ---
        The date an event ended that relates to the payment of a claim.
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSP.2
        """
        return self._c_data[1][0]

    @occurrence_span_start_date.setter  # set OSP.2
    def occurrence_span_start_date(self, dt: DT | None):
        """
        id: OSP.2 | len: 8 | use: C | rpt: 1
        ---
        The date an event ended that relates to the payment of a claim.
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSP.2
        """
        self._c_data[1] = (dt,)

    @property  # get OSP.3
    def occurrence_span_stop_date(self) -> DT | None:
        """
        id: OSP.3 | len: 8 | use: C | rpt: 1
        ---
        None
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSP.3
        """
        return self._c_data[2][0]

    @occurrence_span_stop_date.setter  # set OSP.3
    def occurrence_span_stop_date(self, dt: DT | None):
        """
        id: OSP.3 | len: 8 | use: C | rpt: 1
        ---
        None
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OSP.3
        """
        self._c_data[2] = (dt,)
