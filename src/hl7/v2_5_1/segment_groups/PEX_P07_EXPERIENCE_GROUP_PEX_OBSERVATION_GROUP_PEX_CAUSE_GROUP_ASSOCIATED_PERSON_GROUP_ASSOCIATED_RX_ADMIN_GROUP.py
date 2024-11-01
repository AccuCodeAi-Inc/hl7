from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXA import RXA
from ..segments.RXR import RXR


"""
ASSOCIATED RX ADMIN - PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP
from utils.hl7.v2_5_1.segments import (
    RXR, RXA
)

pex_p07_experience_group_pex_observation_group_pex_cause_group_associated_person_group_associated_rx_admin_group = PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP(  # ASSOCIATED RX ADMIN - Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP - ASSOCIATED PERSON consisting of RXA, RXR|None
    pharmacy_or_treatment_administration=rxa,  # RXA(...)  # Required.
    pharmacy_or_treatment_route=None,  # RXR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP TEMPLATE-----
"""


class PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP"""
    _hl7_name = """ASSOCIATED RX ADMIN"""
    _hl7_description = """Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP - ASSOCIATED PERSON consisting of RXA, RXR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("26", "27")
    _c_components = (RXA, RXR)
    _c_name = ("RXA", "RXR")
    _c_is_group = (False, False)
    _c_attrs = ("pharmacy_or_treatment_administration", "pharmacy_or_treatment_route",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_administration: RXA,  #  Required. RXA.26
        pharmacy_or_treatment_route: RXR | None = None,  #  RXR.27
    ):
        """
        None - `PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ADMIN_GROUP>`_
        Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP - ASSOCIATED PERSON consisting of RXA, RXR|None

        :param pharmacy_or_treatment_administration: Pharmacy/Treatment Administration (id: RXA | seq: 26 | use: R | rpt: 1)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 27 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.pharmacy_or_treatment_administration = pharmacy_or_treatment_administration
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route

    @property  # get RXA.26
    def pharmacy_or_treatment_administration(self) -> RXA:
        """
        id: RXA | use: R | rpt: 1 | seq: 26
        ---
        return_type: RXA.26: Pharmacy/Treatment Administration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_administration.setter  # set RXA.26
    def pharmacy_or_treatment_administration(self, rxa: RXA):
        """
        id: RXA | use: R | rpt: 1 | seq: 26
        ---
        param_type: RXA.26: Pharmacy/Treatment Administration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        self._c_data[0] = (rxa,)

    @property  # get RXR.27
    def pharmacy_or_treatment_route(self) -> RXR | None:
        """
        id: RXR | use: O | rpt: 1 | seq: 27
        ---
        return_type: RXR.27: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[1][0]

    @pharmacy_or_treatment_route.setter  # set RXR.27
    def pharmacy_or_treatment_route(self, rxr: RXR | None):
        """
        id: RXR | use: O | rpt: 1 | seq: 27
        ---
        param_type: RXR.27: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        self._c_data[1] = (rxr,)
