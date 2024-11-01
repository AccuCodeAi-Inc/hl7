from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CQ import CQ
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.ST import ST
from ..data_types.FT import FT
from ..data_types.TS import TS
from ..tables.QuantityMethod import QuantityMethod


"""
Product Summary Header - PSH
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PSH TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PSH,
    CQ, ID, NM, ST, FT, TS
)

psh = PSH(  #  - 
    report_type=st,  # ST(...)  # Required.
    report_form_identifier=None,  # ST(...) 
    report_date=ts,  # TS(...)  # Required.
    report_interval_start_date=None,  # TS(...) 
    report_interval_end_date=None,  # TS(...) 
    quantity_manufactured=None,  # CQ(...) 
    quantity_distributed=None,  # CQ(...) 
    quantity_distributed_method=None,  # ID(...) 
    quantity_distributed_comment=None,  # FT(...) 
    quantity_in_use=None,  # CQ(...) 
    quantity_in_use_method=None,  # ID(...) 
    quantity_in_use_comment=None,  # FT(...) 
    number_of_product_experience_reports_filed_by_facility=None,  # NM(...) 
    number_of_product_experience_reports_filed_by_distributor=None,  # NM(...) 
)

-----END SEGMENT::PSH TEMPLATE-----
"""


class PSH(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PSH"""
    _hl7_name = """Product Summary Header"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PSH"
    _c_length = (60, 60, 26, 26, 26, 12, 12, 1, 600, 12, 1, 600, 2, 2,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 8,)
    _c_usage = ("R", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (ST, ST, TS, TS, TS, CQ, CQ, ID, FT, CQ, ID, FT, NM, NM,)
    _c_aliases = ("PSH.1", "PSH.2", "PSH.3", "PSH.4", "PSH.5", "PSH.6", "PSH.7", "PSH.8", "PSH.9", "PSH.10", "PSH.11", "PSH.12", "PSH.13", "PSH.14",)
    _c_names = ("Report Type", "Report Form Identifier", "Report Date", "Report Interval Start Date", "Report Interval End Date", "Quantity Manufactured", "Quantity Distributed", "Quantity Distributed Method", "Quantity Distributed Comment", "Quantity in Use", "Quantity in Use Method", "Quantity in Use Comment", "Number of Product Experience Reports Filed by Facility", "Number of Product Experience Reports Filed by Distributor",)
    _c_attrs = ("report_type", "report_form_identifier", "report_date", "report_interval_start_date", "report_interval_end_date", "quantity_manufactured", "quantity_distributed", "quantity_distributed_method", "quantity_distributed_comment", "quantity_in_use", "quantity_in_use_method", "quantity_in_use_comment", "number_of_product_experience_reports_filed_by_facility", "number_of_product_experience_reports_filed_by_distributor",)
    # fmt: on

    def __init__(
        self,
        report_type: ST,  # PSH.1
        report_date: TS,  # PSH.3
        report_form_identifier: ST | None = None,  # PSH.2
        report_interval_start_date: TS | None = None,  # PSH.4
        report_interval_end_date: TS | None = None,  # PSH.5
        quantity_manufactured: CQ | None = None,  # PSH.6
        quantity_distributed: CQ | None = None,  # PSH.7
        quantity_distributed_method: QuantityMethod | ID | None = None,  # PSH.8
        quantity_distributed_comment: FT | None = None,  # PSH.9
        quantity_in_use: CQ | None = None,  # PSH.10
        quantity_in_use_method: QuantityMethod | ID | None = None,  # PSH.11
        quantity_in_use_comment: FT | None = None,  # PSH.12
        number_of_product_experience_reports_filed_by_facility: NM
        | None = None,  # PSH.13
        number_of_product_experience_reports_filed_by_distributor: NM
        | None = None,  # PSH.14
    ):
        """
        Product Summary Header - `PSH <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PSH>`_


        :param report_type: String Data (id: PSH.1 | len: 60 | use: R | rpt: 1)
        :param report_form_identifier: String Data (id: PSH.2 | len: 60 | use: O | rpt: 1)
        :param report_date: Time Stamp (id: PSH.3 | len: 26 | use: R | rpt: 1)
        :param report_interval_start_date: Time Stamp (id: PSH.4 | len: 26 | use: O | rpt: 1)
        :param report_interval_end_date: Time Stamp (id: PSH.5 | len: 26 | use: O | rpt: 1)
        :param quantity_manufactured: Composite Quantity with Units (id: PSH.6 | len: 12 | use: O | rpt: 1)
        :param quantity_distributed: Composite Quantity with Units (id: PSH.7 | len: 12 | use: O | rpt: 1)
        :param quantity_distributed_method: Coded values for HL7 tables (id: PSH.8 | len: 1 | use: O | rpt: 1)
        :param quantity_distributed_comment: Formatted Text Data (id: PSH.9 | len: 600 | use: O | rpt: 1)
        :param quantity_in_use: Composite Quantity with Units (id: PSH.10 | len: 12 | use: O | rpt: 1)
        :param quantity_in_use_method: Coded values for HL7 tables (id: PSH.11 | len: 1 | use: O | rpt: 1)
        :param quantity_in_use_comment: Formatted Text Data (id: PSH.12 | len: 600 | use: O | rpt: 1)
        :param number_of_product_experience_reports_filed_by_facility: Numeric (id: PSH.13 | len: 2 | use: O | rpt: 8)
        :param number_of_product_experience_reports_filed_by_distributor: Numeric (id: PSH.14 | len: 2 | use: O | rpt: 8)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 14
        self.report_type = report_type
        self.report_form_identifier = report_form_identifier
        self.report_date = report_date
        self.report_interval_start_date = report_interval_start_date
        self.report_interval_end_date = report_interval_end_date
        self.quantity_manufactured = quantity_manufactured
        self.quantity_distributed = quantity_distributed
        self.quantity_distributed_method = quantity_distributed_method
        self.quantity_distributed_comment = quantity_distributed_comment
        self.quantity_in_use = quantity_in_use
        self.quantity_in_use_method = quantity_in_use_method
        self.quantity_in_use_comment = quantity_in_use_comment
        self.number_of_product_experience_reports_filed_by_facility = (
            number_of_product_experience_reports_filed_by_facility
        )
        self.number_of_product_experience_reports_filed_by_distributor = (
            number_of_product_experience_reports_filed_by_distributor
        )

    @property  # get PSH.1
    def report_type(self) -> ST:
        """
        id: PSH.1 | len: 60 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.1
        """
        return self._c_data[0][0]

    @report_type.setter  # set PSH.1
    def report_type(self, st: ST):
        """
        id: PSH.1 | len: 60 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.1
        """
        self._c_data[0] = (st,)

    @property  # get PSH.2
    def report_form_identifier(self) -> ST | None:
        """
        id: PSH.2 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.2
        """
        return self._c_data[1][0]

    @report_form_identifier.setter  # set PSH.2
    def report_form_identifier(self, st: ST | None):
        """
        id: PSH.2 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.2
        """
        self._c_data[1] = (st,)

    @property  # get PSH.3
    def report_date(self) -> TS:
        """
        id: PSH.3 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.3
        """
        return self._c_data[2][0]

    @report_date.setter  # set PSH.3
    def report_date(self, ts: TS):
        """
        id: PSH.3 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.3
        """
        self._c_data[2] = (ts,)

    @property  # get PSH.4
    def report_interval_start_date(self) -> TS | None:
        """
        id: PSH.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.4
        """
        return self._c_data[3][0]

    @report_interval_start_date.setter  # set PSH.4
    def report_interval_start_date(self, ts: TS | None):
        """
        id: PSH.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.4
        """
        self._c_data[3] = (ts,)

    @property  # get PSH.5
    def report_interval_end_date(self) -> TS | None:
        """
        id: PSH.5 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.5
        """
        return self._c_data[4][0]

    @report_interval_end_date.setter  # set PSH.5
    def report_interval_end_date(self, ts: TS | None):
        """
        id: PSH.5 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.5
        """
        self._c_data[4] = (ts,)

    @property  # get PSH.6
    def quantity_manufactured(self) -> CQ | None:
        """
        id: PSH.6 | len: 12 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.6
        """
        return self._c_data[5][0]

    @quantity_manufactured.setter  # set PSH.6
    def quantity_manufactured(self, cq: CQ | None):
        """
        id: PSH.6 | len: 12 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.6
        """
        self._c_data[5] = (cq,)

    @property  # get PSH.7
    def quantity_distributed(self) -> CQ | None:
        """
        id: PSH.7 | len: 12 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.7
        """
        return self._c_data[6][0]

    @quantity_distributed.setter  # set PSH.7
    def quantity_distributed(self, cq: CQ | None):
        """
        id: PSH.7 | len: 12 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.7
        """
        self._c_data[6] = (cq,)

    @property  # get PSH.8
    def quantity_distributed_method(self) -> QuantityMethod | None:
        """
        id: PSH.8 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.8
        """
        return self._c_data[7][0]

    @quantity_distributed_method.setter  # set PSH.8
    def quantity_distributed_method(self, quantity_method: QuantityMethod | None):
        """
        id: PSH.8 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.8
        """
        self._c_data[7] = (quantity_method,)

    @property  # get PSH.9
    def quantity_distributed_comment(self) -> FT | None:
        """
        id: PSH.9 | len: 600 | use: O | rpt: 1
        ---
        return_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.9
        """
        return self._c_data[8][0]

    @quantity_distributed_comment.setter  # set PSH.9
    def quantity_distributed_comment(self, ft: FT | None):
        """
        id: PSH.9 | len: 600 | use: O | rpt: 1
        ---
        param_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.9
        """
        self._c_data[8] = (ft,)

    @property  # get PSH.10
    def quantity_in_use(self) -> CQ | None:
        """
        id: PSH.10 | len: 12 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.10
        """
        return self._c_data[9][0]

    @quantity_in_use.setter  # set PSH.10
    def quantity_in_use(self, cq: CQ | None):
        """
        id: PSH.10 | len: 12 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.10
        """
        self._c_data[9] = (cq,)

    @property  # get PSH.11
    def quantity_in_use_method(self) -> QuantityMethod | None:
        """
        id: PSH.11 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.11
        """
        return self._c_data[10][0]

    @quantity_in_use_method.setter  # set PSH.11
    def quantity_in_use_method(self, quantity_method: QuantityMethod | None):
        """
        id: PSH.11 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.11
        """
        self._c_data[10] = (quantity_method,)

    @property  # get PSH.12
    def quantity_in_use_comment(self) -> FT | None:
        """
        id: PSH.12 | len: 600 | use: O | rpt: 1
        ---
        return_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.12
        """
        return self._c_data[11][0]

    @quantity_in_use_comment.setter  # set PSH.12
    def quantity_in_use_comment(self, ft: FT | None):
        """
        id: PSH.12 | len: 600 | use: O | rpt: 1
        ---
        param_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.12
        """
        self._c_data[11] = (ft,)

    @property
    def number_of_product_experience_reports_filed_by_facility(
        self,
    ) -> tuple[NM, ...] | tuple[None]:
        """
        id: PSH.13 | len: 2 | use: O | rpt: 8
        ---
        return_type: tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.13
        """
        return self._c_data[12]

    @number_of_product_experience_reports_filed_by_facility.setter  # set PSH.13
    def number_of_product_experience_reports_filed_by_facility(
        self, nm: NM | tuple[NM] | None
    ):
        """
        id: PSH.13 | len: 2 | use: O | rpt: 8
        ---
        param_type: NM | tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.13
        """
        if isinstance(nm, tuple):
            self._c_data[12] = nm
        else:
            self._c_data[12] = (nm,)

    @property
    def number_of_product_experience_reports_filed_by_distributor(
        self,
    ) -> tuple[NM, ...] | tuple[None]:
        """
        id: PSH.14 | len: 2 | use: O | rpt: 8
        ---
        return_type: tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.14
        """
        return self._c_data[13]

    @number_of_product_experience_reports_filed_by_distributor.setter  # set PSH.14
    def number_of_product_experience_reports_filed_by_distributor(
        self, nm: NM | tuple[NM] | None
    ):
        """
        id: PSH.14 | len: 2 | use: O | rpt: 8
        ---
        param_type: NM | tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PSH.14
        """
        if isinstance(nm, tuple):
            self._c_data[13] = nm
        else:
            self._c_data[13] = (nm,)
