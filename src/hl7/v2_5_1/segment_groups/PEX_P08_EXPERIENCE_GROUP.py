from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP,
)
from ..segments.PES import PES


"""
EXPERIENCE - PEX_P08_EXPERIENCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PEX_P08_EXPERIENCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PEX_P08_EXPERIENCE_GROUP
from utils.hl7.v2_5_1.segments import (
    PES
)
from utils.hl7.v2_5_1.segment_groups import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP
)

pex_p08_experience_group = PEX_P08_EXPERIENCE_GROUP(  # EXPERIENCE - Segment group for PEX_P08 - Unsolicited update individual product experience report consisting of PES, PEX OBSERVATION
    product_experience_sender=pes,  # PES(...)  # Required.
    pex_observation=pex_p08_experience_group_pex_observation_group,  # PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PEX_P08_EXPERIENCE_GROUP TEMPLATE-----
"""


class PEX_P08_EXPERIENCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PEX_P08_EXPERIENCE_GROUP"""
    _hl7_name = """EXPERIENCE"""
    _hl7_description = """Segment group for PEX_P08 - Unsolicited update individual product experience report consisting of PES, PEX OBSERVATION"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P08_EXPERIENCE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "R")
    _c_aliases = ("9", "None")
    _c_components = (PES, PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP)
    _c_name = ("PES", "PEX OBSERVATION")
    _c_is_group = (False, True)
    _c_attrs = ("product_experience_sender", "pex_observation",)
    # fmt: on

    def __init__(
        self,
        product_experience_sender: PES,  #  Required. PES.9
        pex_observation: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP
        | tuple[
            PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP, ...
        ],  #  Required. (PEO.10, ...)
    ):
        """
        None - `PEX_P08_EXPERIENCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P08_EXPERIENCE_GROUP>`_
        Segment group for PEX_P08 - Unsolicited update individual product experience report consisting of PES, PEX OBSERVATION

        :param product_experience_sender: Product Experience Sender (id: PES | seq: 9 | use: R | rpt: 1)
        :param pex_observation: Pex Observation segment group: [PEO, PEX CAUSE] (id: PEX OBSERVATION | seq: 10, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.product_experience_sender = product_experience_sender
        self.pex_observation = pex_observation

    @property  # get PES.9
    def product_experience_sender(self) -> PES:
        """
        id: PES | use: R | rpt: 1 | seq: 9
        ---
        return_type: PES.9: Product Experience Sender
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PES
        """
        return self._c_data[0][0]

    @product_experience_sender.setter  # set PES.9
    def product_experience_sender(self, pes: PES):
        """
        id: PES | use: R | rpt: 1 | seq: 9
        ---
        param_type: PES.9: Product Experience Sender
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PES
        """
        self._c_data[0] = (pes,)

    @property  # get PEX OBSERVATION
    def pex_observation(
        self,
    ) -> tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP, ...]:
        """
        id: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP
        """
        return self._c_data[1]

    @pex_observation.setter  # set PEX OBSERVATION
    def pex_observation(
        self,
        pex_observation: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP
        | tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP, ...],
    ):
        """
        id: PEX OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP.None | tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP
        """
        if isinstance(pex_observation, tuple):
            self._c_data[1] = pex_observation
        else:
            self._c_data[1] = (pex_observation,)
