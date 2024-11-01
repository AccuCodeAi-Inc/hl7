from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP,
)
from ..segments.PEO import PEO


"""
PEX OBSERVATION - PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    PEO
)
from utils.hl7.v2_5_1.segment_groups import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP
)

pex_p08_experience_group_pex_observation_group = PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP(  # PEX OBSERVATION - Segment group for PEX_P08_EXPERIENCE_GROUP - EXPERIENCE consisting of PEO, PEX CAUSE
    product_experience_observation=peo,  # PEO(...)  # Required.
    pex_cause=pex_p08_experience_group_pex_observation_group_pex_cause_group,  # PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP TEMPLATE-----
"""


class PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP"""
    _hl7_name = """PEX OBSERVATION"""
    _hl7_description = """Segment group for PEX_P08_EXPERIENCE_GROUP - EXPERIENCE consisting of PEO, PEX CAUSE"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "R")
    _c_aliases = ("10", "None")
    _c_components = (PEO, PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP)
    _c_name = ("PEO", "PEX CAUSE")
    _c_is_group = (False, True)
    _c_attrs = ("product_experience_observation", "pex_cause",)
    # fmt: on

    def __init__(
        self,
        product_experience_observation: PEO,  #  Required. PEO.10
        pex_cause: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP
        | tuple[
            PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP, ...
        ],  #  Required. (PCR.11, PRB.18, OBX.19, NTE.20, ...)
    ):
        """
        None - `PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP>`_
        Segment group for PEX_P08_EXPERIENCE_GROUP - EXPERIENCE consisting of PEO, PEX CAUSE

        :param product_experience_observation: Product Experience Observation (id: PEO | seq: 10 | use: R | rpt: 1)
        :param pex_cause: Pex Cause segment group: [PCR, RX ORDER|None, RX ADMINISTRATION|None, PRB|None, OBX|None, NTE|None, ASSOCIATED PERSON|None, STUDY|None] (id: PEX CAUSE | seq: 11, None, None, 18, 19, 20, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.product_experience_observation = product_experience_observation
        self.pex_cause = pex_cause

    @property  # get PEO.10
    def product_experience_observation(self) -> PEO:
        """
        id: PEO | use: R | rpt: 1 | seq: 10
        ---
        return_type: PEO.10: Product Experience Observation
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEO
        """
        return self._c_data[0][0]

    @product_experience_observation.setter  # set PEO.10
    def product_experience_observation(self, peo: PEO):
        """
        id: PEO | use: R | rpt: 1 | seq: 10
        ---
        param_type: PEO.10: Product Experience Observation
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEO
        """
        self._c_data[0] = (peo,)

    @property  # get PEX CAUSE
    def pex_cause(
        self,
    ) -> tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP, ...]:
        """
        id: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP
        """
        return self._c_data[1]

    @pex_cause.setter  # set PEX CAUSE
    def pex_cause(
        self,
        pex_cause: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP
        | tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP, ...],
    ):
        """
        id: PEX CAUSE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP.None | tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP
        """
        if isinstance(pex_cause, tuple):
            self._c_data[1] = pex_cause
        else:
            self._c_data[1] = (pex_cause,)
