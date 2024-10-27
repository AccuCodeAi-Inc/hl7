from __future__ import annotations
from ...base import DataType
from .CNE import CNE
from .DT import DT
from ..tables.OccurrenceCode import OccurrenceCode


"""
DataType - OCD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::OCD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OCD,
    CNE, DT
)

ocd = OCD(  # Occurrence Code and Date - The code and associated date defining a significant event relating to a bill that may affect payer processing
    occurrence_code=cne,  # CNE(...)  # Required.
    occurrence_date=dt,  # DT(...)  # Required.
)

-----END COMPOSITE_DATA_TYPE::OCD TEMPLATE-----
"""


class OCD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 714
    _hl7_id = """OCD"""
    _hl7_name = """Occurrence Code and Date"""
    _hl7_description = """The code and associated date defining a significant event relating to a bill that may affect payer processing"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OCD"
    _c_length = (705, 8,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "R",)
    _c_aliases = ("OCD.1", "OCD.2",)
    _c_components = (CNE, DT,)
    _c_names = ("Occurrence Code", "Occurrence Date",)
    _c_attrs = ("occurrence_code", "occurrence_date",)
    # fmt: on

    def __init__(
        self,
        occurrence_code: OccurrenceCode | CNE,  # OCD.1
        occurrence_date: DT,  # OCD.2
    ):
        """
                Occurrence Code and Date - `OCD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OCD>`_
                The code and associated date defining a significant event relating to a bill that may affect payer processing.

        Example: |23&Benefits Exhausted&NUBC^19920108|

                :param occurrence_code: The NUBC code for the event or occurrence relating to a bill that may affect payer processing (id: OCD.1 | len: 705 | use: R | rpt: 1)
                :param occurrence_date: The date the event, relating to a bill that may affect payer processing, occurred (id: OCD.2 | len: 8 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.occurrence_code = occurrence_code
        self.occurrence_date = occurrence_date

    @property  # get OCD.1
    def occurrence_code(self) -> CNE:
        """
        id: OCD.1 | len: 705 | use: R | rpt: 1
        ---
        The NUBC code for the event or occurrence relating to a bill that may affect payer processing.
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OCD.1
        """
        return self._c_data[0][0]

    @occurrence_code.setter  # set OCD.1
    def occurrence_code(self, cne: CNE):
        """
        id: OCD.1 | len: 705 | use: R | rpt: 1
        ---
        The NUBC code for the event or occurrence relating to a bill that may affect payer processing.
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OCD.1
        """
        self._c_data[0] = (cne,)

    @property  # get OCD.2
    def occurrence_date(self) -> DT:
        """
        id: OCD.2 | len: 8 | use: R | rpt: 1
        ---
        The date the event, relating to a bill that may affect payer processing, occurred.
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OCD.2
        """
        return self._c_data[1][0]

    @occurrence_date.setter  # set OCD.2
    def occurrence_date(self, dt: DT):
        """
        id: OCD.2 | len: 8 | use: R | rpt: 1
        ---
        The date the event, relating to a bill that may affect payer processing, occurred.
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OCD.2
        """
        self._c_data[1] = (dt,)
