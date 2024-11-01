from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segments.STF import STF
from ..segments.EVN import EVN
from ..segments.SFT import SFT


"""
Delete personnel record - PMU_B03
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::PMU_B03 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PMU_B03
from utils.hl7.v2_5_1.segments import (
    SFT, EVN, STF, MSH
)

pmu_b03 = PMU_B03(  #  - An event B03 signals to delete the record with the healthcare administration information about an individual healthcare practitioner to correct erroneous entries
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    staff_identification=stf,  # STF(...)  # Required.
)

-----END TRIGGER_EVENT::PMU_B03 TEMPLATE-----
"""


class PMU_B03(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """PMU_B03"""
    _hl7_name = """Delete personnel record"""
    _hl7_description = """An event B03 signals to delete the record with the healthcare administration information about an individual healthcare practitioner to correct erroneous entries"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PMU_B03"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "4")
    _c_components = (MSH, SFT, EVN, STF)
    _c_name = ("MSH", "SFT", "EVN", "STF")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "staff_identification",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        staff_identification: STF,  #  Required. STF.4
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `PMU_B03 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PMU_B03>`_
        An event B03 signals to delete the record with the healthcare administration information about an individual healthcare practitioner to correct erroneous entries.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param staff_identification: Staff Identification (id: STF | seq: 4 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.staff_identification = staff_identification

    @property  # get MSH.1
    def message_header(self) -> MSH:
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        return_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        return self._c_data[0][0]

    @message_header.setter  # set MSH.1
    def message_header(self, msh: MSH):
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        param_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        self._c_data[0] = (msh,)

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[1]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        param_type: SFT.2 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[1] = sft
        else:
            self._c_data[1] = (sft,)

    @property  # get EVN.3
    def event_type(self) -> EVN:
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        return_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        return self._c_data[2][0]

    @event_type.setter  # set EVN.3
    def event_type(self, evn: EVN):
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        param_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        self._c_data[2] = (evn,)

    @property  # get STF.4
    def staff_identification(self) -> STF:
        """
        id: STF | use: R | rpt: 1 | seq: 4
        ---
        return_type: STF.4: Staff Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/STF
        """
        return self._c_data[3][0]

    @staff_identification.setter  # set STF.4
    def staff_identification(self, stf: STF):
        """
        id: STF | use: R | rpt: 1 | seq: 4
        ---
        param_type: STF.4: Staff Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/STF
        """
        self._c_data[3] = (stf,)
