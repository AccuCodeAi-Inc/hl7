from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP import (
    DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP,
)
from ..segment_groups.DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP import (
    DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP,
)
from ..segments.DG1 import DG1
from ..segments.GT1 import GT1
from ..segment_groups.DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP import (
    DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP,
)
from ..segments.DRG import DRG
from ..segments.FT1 import FT1


"""
FINANCIAL - DFT_P11_FINANCIAL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::DFT_P11_FINANCIAL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import DFT_P11_FINANCIAL_GROUP
from utils.hl7.v2_5_1.segments import (
    DRG, FT1, DG1, GT1
)
from utils.hl7.v2_5_1.segment_groups import (
    DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP, DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
)

dft_p11_financial_group = DFT_P11_FINANCIAL_GROUP(  # FINANCIAL - Segment group for DFT_P11 - Post Detail Financial Transactions - Expanded consisting of FT1, FINANCIAL PROCEDURE|None, FINANCIAL COMMON ORDER|None, DG1|None, DRG|None, GT1|None, FINANCIAL INSURANCE|None
    financial_transaction=ft1,  # FT1(...)  # Required.
    financial_procedure=None,  # DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP(...) 
    financial_common_order=None,  # DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP(...) 
    diagnosis=None,  # DG1(...) 
    diagnosis_related_group=None,  # DRG(...) 
    guarantor=None,  # GT1(...) 
    financial_insurance=None,  # DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::DFT_P11_FINANCIAL_GROUP TEMPLATE-----
"""


class DFT_P11_FINANCIAL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """DFT_P11_FINANCIAL_GROUP"""
    _hl7_name = """FINANCIAL"""
    _hl7_description = """Segment group for DFT_P11 - Post Detail Financial Transactions - Expanded consisting of FT1, FINANCIAL PROCEDURE|None, FINANCIAL COMMON ORDER|None, DG1|None, DRG|None, GT1|None, FINANCIAL INSURANCE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P11_FINANCIAL_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 1, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("26", "None", "None", "36", "37", "38", "None")
    _c_components = (FT1, DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, DG1, DRG, GT1, DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP)
    _c_name = ("FT1", "FINANCIAL PROCEDURE", "FINANCIAL COMMON ORDER", "DG1", "DRG", "GT1", "FINANCIAL INSURANCE")
    _c_is_group = (False, True, True, False, False, False, True)
    _c_attrs = ("financial_transaction", "financial_procedure", "financial_common_order", "diagnosis", "diagnosis_related_group", "guarantor", "financial_insurance",)
    # fmt: on

    def __init__(
        self,
        financial_transaction: FT1,  #  Required. FT1.26
        financial_procedure: DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
        | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, ...]
        | None = None,  #  (PR1.27, ROL.28, ...)
        financial_common_order: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
        | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, ...]
        | None = None,  #  (ORC.29, ...)
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.36
        diagnosis_related_group: DRG | None = None,  #  DRG.37
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.38
        financial_insurance: DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP
        | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.39, IN2.40, IN3.41, ROL.42, ...)
    ):
        """
        None - `DFT_P11_FINANCIAL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P11_FINANCIAL_GROUP>`_
        Segment group for DFT_P11 - Post Detail Financial Transactions - Expanded consisting of FT1, FINANCIAL PROCEDURE|None, FINANCIAL COMMON ORDER|None, DG1|None, DRG|None, GT1|None, FINANCIAL INSURANCE|None

        :param financial_transaction: Financial Transaction (id: FT1 | seq: 26 | use: R | rpt: 1)
        :param financial_procedure: Financial Procedure segment group: [PR1, ROL|None] (id: FINANCIAL PROCEDURE | seq: 27, 28 | use: O | rpt: *)
        :param financial_common_order: Financial Common Order segment group: [ORC|None, FINANCIAL TIMING QUANTITY|None, FINANCIAL ORDER|None, FINANCIAL OBSERVATION|None] (id: FINANCIAL COMMON ORDER | seq: 29, None, None, None | use: O | rpt: *)
        :param diagnosis: Diagnosis (id: DG1 | seq: 36 | use: O | rpt: *)
        :param diagnosis_related_group: Diagnosis Related Group (id: DRG | seq: 37 | use: O | rpt: 1)
        :param guarantor: Guarantor (id: GT1 | seq: 38 | use: O | rpt: *)
        :param financial_insurance: Financial Insurance segment group: [IN1, IN2|None, IN3|None, ROL|None] (id: FINANCIAL INSURANCE | seq: 39, 40, 41, 42 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.financial_transaction = financial_transaction
        self.financial_procedure = financial_procedure
        self.financial_common_order = financial_common_order
        self.diagnosis = diagnosis
        self.diagnosis_related_group = diagnosis_related_group
        self.guarantor = guarantor
        self.financial_insurance = financial_insurance

    @property  # get FT1.26
    def financial_transaction(self) -> FT1:
        """
        id: FT1 | use: R | rpt: 1 | seq: 26
        ---
        return_type: FT1.26: Financial Transaction
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        return self._c_data[0][0]

    @financial_transaction.setter  # set FT1.26
    def financial_transaction(self, ft1: FT1):
        """
        id: FT1 | use: R | rpt: 1 | seq: 26
        ---
        param_type: FT1.26: Financial Transaction
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        self._c_data[0] = (ft1,)

    @property  # get FINANCIAL PROCEDURE
    def financial_procedure(
        self,
    ) -> tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, ...] | tuple[None]:
        """
        id: DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
        """
        return self._c_data[1]

    @financial_procedure.setter  # set FINANCIAL PROCEDURE
    def financial_procedure(
        self,
        financial_procedure: DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
        | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, ...]
        | None,
    ):
        """
        id: FINANCIAL PROCEDURE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP.None | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_PROCEDURE_GROUP
        """
        if isinstance(financial_procedure, tuple):
            self._c_data[1] = financial_procedure
        else:
            self._c_data[1] = (financial_procedure,)

    @property  # get FINANCIAL COMMON ORDER
    def financial_common_order(
        self,
    ) -> tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, ...] | tuple[None]:
        """
        id: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
        """
        return self._c_data[2]

    @financial_common_order.setter  # set FINANCIAL COMMON ORDER
    def financial_common_order(
        self,
        financial_common_order: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
        | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: FINANCIAL COMMON ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP.None | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
        """
        if isinstance(financial_common_order, tuple):
            self._c_data[2] = financial_common_order
        else:
            self._c_data[2] = (financial_common_order,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 36
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[3]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 36
        ---
        param_type: DG1.36 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[3] = dg1
        else:
            self._c_data[3] = (dg1,)

    @property  # get DRG.37
    def diagnosis_related_group(self) -> DRG | None:
        """
        id: DRG | use: O | rpt: 1 | seq: 37
        ---
        return_type: DRG.37: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        return self._c_data[4][0]

    @diagnosis_related_group.setter  # set DRG.37
    def diagnosis_related_group(self, drg: DRG | None):
        """
        id: DRG | use: O | rpt: 1 | seq: 37
        ---
        param_type: DRG.37: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        self._c_data[4] = (drg,)

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 38
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[5]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 38
        ---
        param_type: GT1.38 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[5] = gt1
        else:
            self._c_data[5] = (gt1,)

    @property  # get FINANCIAL INSURANCE
    def financial_insurance(
        self,
    ) -> tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP
        """
        return self._c_data[6]

    @financial_insurance.setter  # set FINANCIAL INSURANCE
    def financial_insurance(
        self,
        financial_insurance: DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP
        | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP, ...]
        | None,
    ):
        """
        id: FINANCIAL INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP.None | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_INSURANCE_GROUP
        """
        if isinstance(financial_insurance, tuple):
            self._c_data[6] = financial_insurance
        else:
            self._c_data[6] = (financial_insurance,)
