from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segment_groups.DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP import (
    DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP,
)
from ..segments.FT1 import FT1
from ..segment_groups.DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP import (
    DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP,
)


"""
FINANCIAL - DFT_P03_FINANCIAL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::DFT_P03_FINANCIAL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import DFT_P03_FINANCIAL_GROUP
from utils.hl7.v2_5_1.segments import (
    FT1, NTE
)
from utils.hl7.v2_5_1.segment_groups import (
    DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
)

dft_p03_financial_group = DFT_P03_FINANCIAL_GROUP(  # FINANCIAL - Segment group for DFT_P03 - Post Detail Financial Transactions consisting of FT1, NTE|None, FINANCIAL PROCEDURE|None, FINANCIAL COMMON ORDER|None
    financial_transaction=ft1,  # FT1(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    financial_procedure=None,  # DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP(...) 
    financial_common_order=None,  # DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::DFT_P03_FINANCIAL_GROUP TEMPLATE-----
"""


class DFT_P03_FINANCIAL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """DFT_P03_FINANCIAL_GROUP"""
    _hl7_name = """FINANCIAL"""
    _hl7_description = """Segment group for DFT_P03 - Post Detail Financial Transactions consisting of FT1, NTE|None, FINANCIAL PROCEDURE|None, FINANCIAL COMMON ORDER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P03_FINANCIAL_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("18", "19", "None", "None")
    _c_components = (FT1, NTE, DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP)
    _c_name = ("FT1", "NTE", "FINANCIAL PROCEDURE", "FINANCIAL COMMON ORDER")
    _c_is_group = (False, False, True, True)
    _c_attrs = ("financial_transaction", "notes_and_comments", "financial_procedure", "financial_common_order",)
    # fmt: on

    def __init__(
        self,
        financial_transaction: FT1,  #  Required. FT1.18
        notes_and_comments: NTE | None = None,  #  NTE.19
        financial_procedure: DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
        | tuple[DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, ...]
        | None = None,  #  (PR1.20, ROL.21, ...)
        financial_common_order: DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
        | tuple[DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, ...]
        | None = None,  #  (ORC.22, ...)
    ):
        """
        None - `DFT_P03_FINANCIAL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P03_FINANCIAL_GROUP>`_
        Segment group for DFT_P03 - Post Detail Financial Transactions consisting of FT1, NTE|None, FINANCIAL PROCEDURE|None, FINANCIAL COMMON ORDER|None

        :param financial_transaction: Financial Transaction (id: FT1 | seq: 18 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 19 | use: O | rpt: 1)
        :param financial_procedure: Financial Procedure segment group: [PR1, ROL|None] (id: FINANCIAL PROCEDURE | seq: 20, 21 | use: O | rpt: *)
        :param financial_common_order: Financial Common Order segment group: [ORC|None, FINANCIAL TIMING QUANTITY|None, FINANCIAL ORDER|None, FINANCIAL OBSERVATION|None] (id: FINANCIAL COMMON ORDER | seq: 22, None, None, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.financial_transaction = financial_transaction
        self.notes_and_comments = notes_and_comments
        self.financial_procedure = financial_procedure
        self.financial_common_order = financial_common_order

    @property  # get FT1.18
    def financial_transaction(self) -> FT1:
        """
        id: FT1 | use: R | rpt: 1 | seq: 18
        ---
        return_type: FT1.18: Financial Transaction
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        return self._c_data[0][0]

    @financial_transaction.setter  # set FT1.18
    def financial_transaction(self, ft1: FT1):
        """
        id: FT1 | use: R | rpt: 1 | seq: 18
        ---
        param_type: FT1.18: Financial Transaction
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        self._c_data[0] = (ft1,)

    @property  # get NTE.19
    def notes_and_comments(self) -> NTE | None:
        """
        id: NTE | use: O | rpt: 1 | seq: 19
        ---
        return_type: NTE.19: Notes and Comments
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1][0]

    @notes_and_comments.setter  # set NTE.19
    def notes_and_comments(self, nte: NTE | None):
        """
        id: NTE | use: O | rpt: 1 | seq: 19
        ---
        param_type: NTE.19: Notes and Comments
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        self._c_data[1] = (nte,)

    @property  # get FINANCIAL PROCEDURE
    def financial_procedure(
        self,
    ) -> tuple[DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, ...] | tuple[None]:
        """
        id: DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
        """
        return self._c_data[2]

    @financial_procedure.setter  # set FINANCIAL PROCEDURE
    def financial_procedure(
        self,
        financial_procedure: DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
        | tuple[DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, ...]
        | None,
    ):
        """
        id: FINANCIAL PROCEDURE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP.None | tuple[DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
        """
        if isinstance(financial_procedure, tuple):
            self._c_data[2] = financial_procedure
        else:
            self._c_data[2] = (financial_procedure,)

    @property  # get FINANCIAL COMMON ORDER
    def financial_common_order(
        self,
    ) -> tuple[DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, ...] | tuple[None]:
        """
        id: DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
        """
        return self._c_data[3]

    @financial_common_order.setter  # set FINANCIAL COMMON ORDER
    def financial_common_order(
        self,
        financial_common_order: DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
        | tuple[DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: FINANCIAL COMMON ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP.None | tuple[DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
        """
        if isinstance(financial_common_order, tuple):
            self._c_data[3] = financial_common_order
        else:
            self._c_data[3] = (financial_common_order,)
