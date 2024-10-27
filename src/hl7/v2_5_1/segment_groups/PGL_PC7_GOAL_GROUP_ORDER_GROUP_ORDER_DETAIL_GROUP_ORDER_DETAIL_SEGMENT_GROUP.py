from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ODS import ODS
from ..segments.OBR import OBR
from ..segments.ODT import ODT
from ..segments.RXO import RXO
from ..segments.RQD import RQD
from ..segments.RQ1 import RQ1


"""
ORDER DETAIL SEGMENT - PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR, RXO, ODT, RQ1, RQD, ODS
)

pgl_pc7_goal_group_order_group_order_detail_group_order_detail_segment_group = PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP(  # ORDER DETAIL SEGMENT - Segment group for PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of OBR|None, RQD|None, RQ1|None, RXO|None, ODS|None, ODT|None
    observation_request=None,  # OBR(...) 
    requisition_detail=None,  # RQD(...) 
    requisition_detail_1=None,  # RQ1(...) 
    pharmacy_or_treatment_order=None,  # RXO(...) 
    dietary_orders_supplements_and_preferences=None,  # ODS(...) 
    diet_tray_instructions=None,  # ODT(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP TEMPLATE-----
"""


class PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP"""
    _hl7_name = """ORDER DETAIL SEGMENT"""
    _hl7_description = """Segment group for PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of OBR|None, RQD|None, RQ1|None, RXO|None, ODS|None, ODT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 1, 1, 1)
    _c_usage = ("C", "C", "C", "C", "C", "C")
    _c_aliases = ("23", "24", "25", "26", "27", "28")
    _c_components = (OBR, RQD, RQ1, RXO, ODS, ODT)
    _c_name = ("OBR", "RQD", "RQ1", "RXO", "ODS", "ODT")
    _c_is_group = (False, False, False, False, False, False)
    _c_attrs = ("observation_request", "requisition_detail", "requisition_detail_1", "pharmacy_or_treatment_order", "dietary_orders_supplements_and_preferences", "diet_tray_instructions",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR | None = None,  #  OBR.23
        requisition_detail: RQD | None = None,  #  RQD.24
        requisition_detail_1: RQ1 | None = None,  #  RQ1.25
        pharmacy_or_treatment_order: RXO | None = None,  #  RXO.26
        dietary_orders_supplements_and_preferences: ODS | None = None,  #  ODS.27
        diet_tray_instructions: ODT | None = None,  #  ODT.28
    ):
        """
        None - `PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP>`_
        Segment group for PGL_PC7_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of OBR|None, RQD|None, RQ1|None, RXO|None, ODS|None, ODT|None

        :param observation_request: Observation Request (id: OBR | seq: 23 | use: C | rpt: 1)
        :param requisition_detail: Requisition Detail (id: RQD | seq: 24 | use: C | rpt: 1)
        :param requisition_detail_1: Requisition Detail-1 (id: RQ1 | seq: 25 | use: C | rpt: 1)
        :param pharmacy_or_treatment_order: Pharmacy/Treatment Order (id: RXO | seq: 26 | use: C | rpt: 1)
        :param dietary_orders_supplements_and_preferences: Dietary Orders, Supplements, and Preferences (id: ODS | seq: 27 | use: C | rpt: 1)
        :param diet_tray_instructions: Diet Tray Instructions (id: ODT | seq: 28 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.observation_request = observation_request
        self.requisition_detail = requisition_detail
        self.requisition_detail_1 = requisition_detail_1
        self.pharmacy_or_treatment_order = pharmacy_or_treatment_order
        self.dietary_orders_supplements_and_preferences = (
            dietary_orders_supplements_and_preferences
        )
        self.diet_tray_instructions = diet_tray_instructions

    @property  # get OBR.23
    def observation_request(self) -> OBR | None:
        """
        id: OBR | use: C | rpt: 1 | seq: 23
        ---
        return_type: OBR.23: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[0][0]

    @observation_request.setter  # set OBR.23
    def observation_request(self, obr: OBR | None):
        """
        id: OBR | use: C | rpt: 1 | seq: 23
        ---
        param_type: OBR.23: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[0] = (obr,)

    @property  # get RQD.24
    def requisition_detail(self) -> RQD | None:
        """
        id: RQD | use: C | rpt: 1 | seq: 24
        ---
        return_type: RQD.24: Requisition Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQD
        """
        return self._c_data[1][0]

    @requisition_detail.setter  # set RQD.24
    def requisition_detail(self, rqd: RQD | None):
        """
        id: RQD | use: C | rpt: 1 | seq: 24
        ---
        param_type: RQD.24: Requisition Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQD
        """
        self._c_data[1] = (rqd,)

    @property  # get RQ1.25
    def requisition_detail_1(self) -> RQ1 | None:
        """
        id: RQ1 | use: C | rpt: 1 | seq: 25
        ---
        return_type: RQ1.25: Requisition Detail-1
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQ1
        """
        return self._c_data[2][0]

    @requisition_detail_1.setter  # set RQ1.25
    def requisition_detail_1(self, rq1: RQ1 | None):
        """
        id: RQ1 | use: C | rpt: 1 | seq: 25
        ---
        param_type: RQ1.25: Requisition Detail-1
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQ1
        """
        self._c_data[2] = (rq1,)

    @property  # get RXO.26
    def pharmacy_or_treatment_order(self) -> RXO | None:
        """
        id: RXO | use: C | rpt: 1 | seq: 26
        ---
        return_type: RXO.26: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        return self._c_data[3][0]

    @pharmacy_or_treatment_order.setter  # set RXO.26
    def pharmacy_or_treatment_order(self, rxo: RXO | None):
        """
        id: RXO | use: C | rpt: 1 | seq: 26
        ---
        param_type: RXO.26: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        self._c_data[3] = (rxo,)

    @property  # get ODS.27
    def dietary_orders_supplements_and_preferences(self) -> ODS | None:
        """
        id: ODS | use: C | rpt: 1 | seq: 27
        ---
        return_type: ODS.27: Dietary Orders, Supplements, and Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODS
        """
        return self._c_data[4][0]

    @dietary_orders_supplements_and_preferences.setter  # set ODS.27
    def dietary_orders_supplements_and_preferences(self, ods: ODS | None):
        """
        id: ODS | use: C | rpt: 1 | seq: 27
        ---
        param_type: ODS.27: Dietary Orders, Supplements, and Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODS
        """
        self._c_data[4] = (ods,)

    @property  # get ODT.28
    def diet_tray_instructions(self) -> ODT | None:
        """
        id: ODT | use: C | rpt: 1 | seq: 28
        ---
        return_type: ODT.28: Diet Tray Instructions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODT
        """
        return self._c_data[5][0]

    @diet_tray_instructions.setter  # set ODT.28
    def diet_tray_instructions(self, odt: ODT | None):
        """
        id: ODT | use: C | rpt: 1 | seq: 28
        ---
        param_type: ODT.28: Diet Tray Instructions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODT
        """
        self._c_data[5] = (odt,)
