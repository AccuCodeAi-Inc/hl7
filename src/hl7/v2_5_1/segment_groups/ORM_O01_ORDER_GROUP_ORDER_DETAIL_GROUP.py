from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.CTD import CTD
from ..segment_groups.ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP import (
    ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,
)
from ..segment_groups.ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP import (
    ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP,
)
from ..segments.DG1 import DG1


"""
ORDER DETAIL - ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    DG1, NTE, CTD
)
from utils.hl7.v2_5_1.segment_groups import (
    ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP, ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP
)

orm_o01_order_group_order_detail_group = ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP(  # ORDER DETAIL - Segment group for ORM_O01_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, CTD|None, DG1|None, OBSERVATION|None
    order_detail_segment=orm_o01_order_group_order_detail_group_order_detail_segment_group,  # ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    contact_data=None,  # CTD(...) 
    diagnosis=None,  # DG1(...) 
    observation=None,  # ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----
"""


class ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _hl7_name = """ORDER DETAIL"""
    _hl7_description = """Segment group for ORM_O01_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, CTD|None, DG1|None, OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("None", "20", "21", "22", "None")
    _c_components = (ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP, NTE, CTD, DG1, ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP)
    _c_name = ("ORDER DETAIL SEGMENT", "NTE", "CTD", "DG1", "OBSERVATION")
    _c_is_group = (True, False, False, False, True)
    _c_attrs = ("order_detail_segment", "notes_and_comments", "contact_data", "diagnosis", "observation",)
    # fmt: on

    def __init__(
        self,
        order_detail_segment: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,  #  Required. OBR.14, RQD.15, RQ1.16, RXO.17, ODS.18, ODT.19
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.20
        contact_data: CTD | None = None,  #  CTD.21
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.22
        observation: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP
        | tuple[ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.23, NTE.24, ...)
    ):
        """
        None - `ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP>`_
        Segment group for ORM_O01_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, CTD|None, DG1|None, OBSERVATION|None

        :param order_detail_segment: Order Detail Segment segment group: [OBR|None, RQD|None, RQ1|None, RXO|None, ODS|None, ODT|None] (id: ORDER DETAIL SEGMENT | seq: 14, 15, 16, 17, 18, 19 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 20 | use: O | rpt: *)
        :param contact_data: Contact Data (id: CTD | seq: 21 | use: O | rpt: 1)
        :param diagnosis: Diagnosis (id: DG1 | seq: 22 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 23, 24 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.order_detail_segment = order_detail_segment
        self.notes_and_comments = notes_and_comments
        self.contact_data = contact_data
        self.diagnosis = diagnosis
        self.observation = observation

    @property  # get ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
    ) -> ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP:
        """
        id: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: R | rpt: 1 | seq: None
        ---
        return_type: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        return self._c_data[0][0]

    @order_detail_segment.setter  # set ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
        order_detail_segment: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,
    ):
        """
        id: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: R | rpt: 1 | seq: None
        ---
        param_type: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        self._c_data[0] = (order_detail_segment,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        param_type: NTE.20 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get CTD.21
    def contact_data(self) -> CTD | None:
        """
        id: CTD | use: O | rpt: 1 | seq: 21
        ---
        return_type: CTD.21: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[2][0]

    @contact_data.setter  # set CTD.21
    def contact_data(self, ctd: CTD | None):
        """
        id: CTD | use: O | rpt: 1 | seq: 21
        ---
        param_type: CTD.21: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        self._c_data[2] = (ctd,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[3]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        param_type: DG1.22 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[3] = dg1
        else:
            self._c_data[3] = (dg1,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> (
        tuple[ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP, ...]
        | tuple[None]
    ):
        """
        id: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[4]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP
        | tuple[ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP.None | tuple[ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[4] = observation
        else:
            self._c_data[4] = (observation,)
