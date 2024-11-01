from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CTD import CTD
from ..segments.PRD import PRD


"""
PROVIDER - RPL_I02_PROVIDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RPL_I02_PROVIDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RPL_I02_PROVIDER_GROUP
from utils.hl7.v2_5_1.segments import (
    CTD, PRD
)

rpl_i02_provider_group = RPL_I02_PROVIDER_GROUP(  # PROVIDER - Segment group for RPL_I02 - Request/receipt of patient selection display list acknowledgement consisting of PRD, CTD|None
    provider_data=prd,  # PRD(...)  # Required.
    contact_data=None,  # CTD(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RPL_I02_PROVIDER_GROUP TEMPLATE-----
"""


class RPL_I02_PROVIDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RPL_I02_PROVIDER_GROUP"""
    _hl7_name = """PROVIDER"""
    _hl7_description = """Segment group for RPL_I02 - Request/receipt of patient selection display list acknowledgement consisting of PRD, CTD|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPL_I02_PROVIDER_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("4", "5")
    _c_components = (PRD, CTD)
    _c_name = ("PRD", "CTD")
    _c_is_group = (False, False)
    _c_attrs = ("provider_data", "contact_data",)
    # fmt: on

    def __init__(
        self,
        provider_data: PRD,  #  Required. PRD.4
        contact_data: CTD | tuple[CTD, ...] | None = None,  #  CTD.5
    ):
        """
        None - `RPL_I02_PROVIDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPL_I02_PROVIDER_GROUP>`_
        Segment group for RPL_I02 - Request/receipt of patient selection display list acknowledgement consisting of PRD, CTD|None

        :param provider_data: Provider Data (id: PRD | seq: 4 | use: R | rpt: 1)
        :param contact_data: Contact Data (id: CTD | seq: 5 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.provider_data = provider_data
        self.contact_data = contact_data

    @property  # get PRD.4
    def provider_data(self) -> PRD:
        """
        id: PRD | use: R | rpt: 1 | seq: 4
        ---
        return_type: PRD.4: Provider Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRD
        """
        return self._c_data[0][0]

    @provider_data.setter  # set PRD.4
    def provider_data(self, prd: PRD):
        """
        id: PRD | use: R | rpt: 1 | seq: 4
        ---
        param_type: PRD.4: Provider Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRD
        """
        self._c_data[0] = (prd,)

    @property  # get CTD
    def contact_data(self) -> tuple[CTD, ...] | tuple[None]:
        """
        id: CTD SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        return_type: tuple[CTD, ...]: (Contact Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[1]

    @contact_data.setter  # set CTD
    def contact_data(self, ctd: CTD | tuple[CTD, ...] | None):
        """
        id: CTD SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        param_type: CTD.5 | tuple[CTD, ...]: (Contact Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        if isinstance(ctd, tuple):
            self._c_data[1] = ctd
        else:
            self._c_data[1] = (ctd,)
