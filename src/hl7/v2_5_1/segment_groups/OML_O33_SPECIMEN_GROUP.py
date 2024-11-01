from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBX import OBX
from ..segments.SAC import SAC
from ..segments.SPM import SPM
from ..segment_groups.OML_O33_SPECIMEN_GROUP_ORDER_GROUP import (
    OML_O33_SPECIMEN_GROUP_ORDER_GROUP,
)


"""
SPECIMEN - OML_O33_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OML_O33_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O33_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    SAC, OBX, SPM
)
from utils.hl7.v2_5_1.segment_groups import (
    OML_O33_SPECIMEN_GROUP_ORDER_GROUP
)

oml_o33_specimen_group = OML_O33_SPECIMEN_GROUP(  # SPECIMEN - Segment group for OML_O33 - Laboratory Order for Multiple Orders Related to a Single Specimen  consisting of SPM, OBX|None, SAC|None, ORDER
    specimen=spm,  # SPM(...)  # Required.
    observation_or_result=None,  # OBX(...) 
    specimen_container_detail=None,  # SAC(...) 
    order=oml_o33_specimen_group_order_group,  # OML_O33_SPECIMEN_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OML_O33_SPECIMEN_GROUP TEMPLATE-----
"""


class OML_O33_SPECIMEN_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OML_O33_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for OML_O33 - Laboratory Order for Multiple Orders Related to a Single Specimen  consisting of SPM, OBX|None, SAC|None, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O33_SPECIMEN_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "R")
    _c_aliases = ("15", "16", "17", "None")
    _c_components = (SPM, OBX, SAC, OML_O33_SPECIMEN_GROUP_ORDER_GROUP)
    _c_name = ("SPM", "OBX", "SAC", "ORDER")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("specimen", "observation_or_result", "specimen_container_detail", "order",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.15
        order: OML_O33_SPECIMEN_GROUP_ORDER_GROUP
        | tuple[
            OML_O33_SPECIMEN_GROUP_ORDER_GROUP, ...
        ],  #  Required. (ORC.18, FT1.40, CTI.41, BLG.42, ...)
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.16
        specimen_container_detail: SAC | tuple[SAC, ...] | None = None,  #  SAC.17
    ):
        """
        None - `OML_O33_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O33_SPECIMEN_GROUP>`_
        Segment group for OML_O33 - Laboratory Order for Multiple Orders Related to a Single Specimen  consisting of SPM, OBX|None, SAC|None, ORDER

        :param specimen: Specimen (id: SPM | seq: 15 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 16 | use: O | rpt: *)
        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 17 | use: O | rpt: *)
        :param order: Order segment group: [ORC, TIIMING|None, OBSERVATION REQUEST|None, FT1|None, CTI|None, BLG|None] (id: ORDER | seq: 18, None, None, 40, 41, 42 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.specimen = specimen
        self.observation_or_result = observation_or_result
        self.specimen_container_detail = specimen_container_detail
        self.order = order

    @property  # get SPM.15
    def specimen(self) -> SPM:
        """
        id: SPM | use: R | rpt: 1 | seq: 15
        ---
        return_type: SPM.15: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.15
    def specimen(self, spm: SPM):
        """
        id: SPM | use: R | rpt: 1 | seq: 15
        ---
        param_type: SPM.15: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[1]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: OBX.16 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[1] = obx
        else:
            self._c_data[1] = (obx,)

    @property  # get SAC
    def specimen_container_detail(self) -> tuple[SAC, ...] | tuple[None]:
        """
        id: SAC SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        return_type: tuple[SAC, ...]: (Specimen Container detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[2]

    @specimen_container_detail.setter  # set SAC
    def specimen_container_detail(self, sac: SAC | tuple[SAC, ...] | None):
        """
        id: SAC SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        param_type: SAC.17 | tuple[SAC, ...]: (Specimen Container detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        if isinstance(sac, tuple):
            self._c_data[2] = sac
        else:
            self._c_data[2] = (sac,)

    @property  # get ORDER
    def order(self) -> tuple[OML_O33_SPECIMEN_GROUP_ORDER_GROUP, ...]:
        """
        id: OML_O33_SPECIMEN_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OML_O33_SPECIMEN_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O33_SPECIMEN_GROUP_ORDER_GROUP
        """
        return self._c_data[3]

    @order.setter  # set ORDER
    def order(
        self,
        order: OML_O33_SPECIMEN_GROUP_ORDER_GROUP
        | tuple[OML_O33_SPECIMEN_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OML_O33_SPECIMEN_GROUP_ORDER_GROUP.None | tuple[OML_O33_SPECIMEN_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O33_SPECIMEN_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[3] = order
        else:
            self._c_data[3] = (order,)
