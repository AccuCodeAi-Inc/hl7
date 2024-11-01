from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.SPM import SPM
from ..segment_groups.ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP import (
    ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP,
)
from ..segments.OBX import OBX
from ..segments.SAC import SAC


"""
SPECIMEN - ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    SAC, SPM, OBX
)
from utils.hl7.v2_5_1.segment_groups import (
    ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP
)

orl_o34_response_group_patient_group_specimen_group = ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP(  # SPECIMEN - Segment group for ORL_O34_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of SPM, OBX|None, SAC|None, ORDER|None
    specimen=spm,  # SPM(...)  # Required.
    observation_or_result=None,  # OBX(...) 
    specimen_container_detail=None,  # SAC(...) 
    order=None,  # ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP TEMPLATE-----
"""


class ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for ORL_O34_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of SPM, OBX|None, SAC|None, ORDER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("7", "8", "9", "None")
    _c_components = (SPM, OBX, SAC, ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP)
    _c_name = ("SPM", "OBX", "SAC", "ORDER")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("specimen", "observation_or_result", "specimen_container_detail", "order",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.7
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.8
        specimen_container_detail: SAC | tuple[SAC, ...] | None = None,  #  SAC.9
        order: ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP
        | tuple[ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP, ...]
        | None = None,  #  (ORC.10, ...)
    ):
        """
        None - `ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP>`_
        Segment group for ORL_O34_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of SPM, OBX|None, SAC|None, ORDER|None

        :param specimen: Specimen (id: SPM | seq: 7 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 8 | use: O | rpt: *)
        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 9 | use: O | rpt: *)
        :param order: Order segment group: [ORC, TIMING|None, OBSERVATION REQUEST|None] (id: ORDER | seq: 10, None, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.specimen = specimen
        self.observation_or_result = observation_or_result
        self.specimen_container_detail = specimen_container_detail
        self.order = order

    @property  # get SPM.7
    def specimen(self) -> SPM:
        """
        id: SPM | use: R | rpt: 1 | seq: 7
        ---
        return_type: SPM.7: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.7
    def specimen(self, spm: SPM):
        """
        id: SPM | use: R | rpt: 1 | seq: 7
        ---
        param_type: SPM.7: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[1]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: OBX.8 | tuple[OBX, ...]: (Observation/Result, ...)
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
        id: SAC SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[SAC, ...]: (Specimen Container detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[2]

    @specimen_container_detail.setter  # set SAC
    def specimen_container_detail(self, sac: SAC | tuple[SAC, ...] | None):
        """
        id: SAC SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: SAC.9 | tuple[SAC, ...]: (Specimen Container detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        if isinstance(sac, tuple):
            self._c_data[2] = sac
        else:
            self._c_data[2] = (sac,)

    @property  # get ORDER
    def order(
        self,
    ) -> (
        tuple[ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP, ...]
        | tuple[None]
    ):
        """
        id: ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP
        """
        return self._c_data[3]

    @order.setter  # set ORDER
    def order(
        self,
        order: ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP
        | tuple[ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP.None | tuple[ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[3] = order
        else:
            self._c_data[3] = (order,)
