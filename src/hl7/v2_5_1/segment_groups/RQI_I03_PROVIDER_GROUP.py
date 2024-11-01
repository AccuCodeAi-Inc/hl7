from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CTD import CTD
from ..segments.PRD import PRD


"""
PROVIDER - RQI_I03_PROVIDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RQI_I03_PROVIDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RQI_I03_PROVIDER_GROUP
from utils.hl7.v2_5_1.segments import (
    CTD, PRD
)

rqi_i03_provider_group = RQI_I03_PROVIDER_GROUP(  # PROVIDER - Segment group for RQI_I03 - Request/receipt of patient selection list consisting of PRD, CTD|None
    provider_data=prd,  # PRD(...)  # Required.
    contact_data=None,  # CTD(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RQI_I03_PROVIDER_GROUP TEMPLATE-----
"""


class RQI_I03_PROVIDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RQI_I03_PROVIDER_GROUP"""
    _hl7_name = """PROVIDER"""
    _hl7_description = """Segment group for RQI_I03 - Request/receipt of patient selection list consisting of PRD, CTD|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQI_I03_PROVIDER_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("3", "4")
    _c_components = (PRD, CTD)
    _c_name = ("PRD", "CTD")
    _c_is_group = (False, False)
    _c_attrs = ("provider_data", "contact_data",)
    # fmt: on

    def __init__(
        self,
        provider_data: PRD,  #  Required. PRD.3
        contact_data: CTD | tuple[CTD, ...] | None = None,  #  CTD.4
    ):
        """
        None - `RQI_I03_PROVIDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQI_I03_PROVIDER_GROUP>`_
        Segment group for RQI_I03 - Request/receipt of patient selection list consisting of PRD, CTD|None

        :param provider_data: Provider Data (id: PRD | seq: 3 | use: R | rpt: 1)
        :param contact_data: Contact Data (id: CTD | seq: 4 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.provider_data = provider_data
        self.contact_data = contact_data

    @property  # get PRD.3
    def provider_data(self) -> PRD:
        """
        id: PRD | use: R | rpt: 1 | seq: 3
        ---
        return_type: PRD.3: Provider Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRD
        """
        return self._c_data[0][0]

    @provider_data.setter  # set PRD.3
    def provider_data(self, prd: PRD):
        """
        id: PRD | use: R | rpt: 1 | seq: 3
        ---
        param_type: PRD.3: Provider Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRD
        """
        self._c_data[0] = (prd,)

    @property  # get CTD
    def contact_data(self) -> tuple[CTD, ...] | tuple[None]:
        """
        id: CTD SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        return_type: tuple[CTD, ...]: (Contact Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[1]

    @contact_data.setter  # set CTD
    def contact_data(self, ctd: CTD | tuple[CTD, ...] | None):
        """
        id: CTD SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        param_type: CTD.4 | tuple[CTD, ...]: (Contact Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        if isinstance(ctd, tuple):
            self._c_data[1] = ctd
        else:
            self._c_data[1] = (ctd,)
