from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PR1 import PR1
from ..segments.GP2 import GP2


"""
PROCEDURE - BAR_P10_PROCEDURE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::BAR_P10_PROCEDURE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BAR_P10_PROCEDURE_GROUP
from utils.hl7.v2_5_1.segments import (
    GP2, PR1
)

bar_p10_procedure_group = BAR_P10_PROCEDURE_GROUP(  # PROCEDURE - Segment group for BAR_P10 - Transmit Ambulatory Payment Classification (APC) Groups consisting of PR1, GP2|None
    procedures=pr1,  # PR1(...)  # Required.
    grouping_or_reimbursement_procedure_line_item=None,  # GP2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::BAR_P10_PROCEDURE_GROUP TEMPLATE-----
"""


class BAR_P10_PROCEDURE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """BAR_P10_PROCEDURE_GROUP"""
    _hl7_name = """PROCEDURE"""
    _hl7_description = """Segment group for BAR_P10 - Transmit Ambulatory Payment Classification (APC) Groups consisting of PR1, GP2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P10_PROCEDURE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("8", "9")
    _c_components = (PR1, GP2)
    _c_name = ("PR1", "GP2")
    _c_is_group = (False, False)
    _c_attrs = ("procedures", "grouping_or_reimbursement_procedure_line_item",)
    # fmt: on

    def __init__(
        self,
        procedures: PR1,  #  Required. PR1.8
        grouping_or_reimbursement_procedure_line_item: GP2 | None = None,  #  GP2.9
    ):
        """
        None - `BAR_P10_PROCEDURE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P10_PROCEDURE_GROUP>`_
        Segment group for BAR_P10 - Transmit Ambulatory Payment Classification (APC) Groups consisting of PR1, GP2|None

        :param procedures: Procedures (id: PR1 | seq: 8 | use: R | rpt: 1)
        :param grouping_or_reimbursement_procedure_line_item: Grouping/Reimbursement - Procedure Line Item (id: GP2 | seq: 9 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.procedures = procedures
        self.grouping_or_reimbursement_procedure_line_item = (
            grouping_or_reimbursement_procedure_line_item
        )

    @property  # get PR1.8
    def procedures(self) -> PR1:
        """
        id: PR1 | use: R | rpt: 1 | seq: 8
        ---
        return_type: PR1.8: Procedures
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1
        """
        return self._c_data[0][0]

    @procedures.setter  # set PR1.8
    def procedures(self, pr1: PR1):
        """
        id: PR1 | use: R | rpt: 1 | seq: 8
        ---
        param_type: PR1.8: Procedures
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1
        """
        self._c_data[0] = (pr1,)

    @property  # get GP2.9
    def grouping_or_reimbursement_procedure_line_item(self) -> GP2 | None:
        """
        id: GP2 | use: O | rpt: 1 | seq: 9
        ---
        return_type: GP2.9: Grouping/Reimbursement - Procedure Line Item
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GP2
        """
        return self._c_data[1][0]

    @grouping_or_reimbursement_procedure_line_item.setter  # set GP2.9
    def grouping_or_reimbursement_procedure_line_item(self, gp2: GP2 | None):
        """
        id: GP2 | use: O | rpt: 1 | seq: 9
        ---
        param_type: GP2.9: Grouping/Reimbursement - Procedure Line Item
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GP2
        """
        self._c_data[1] = (gp2,)
