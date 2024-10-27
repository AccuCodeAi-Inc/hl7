from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.EVN import EVN
from ..segments.SFT import SFT
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.MSH import MSH
from ..segments.STF import STF


"""
Active practicing person - PMU_B04
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::PMU_B04 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PMU_B04
from utils.hl7.v2_5_1.segments import (
    STF, ORG, MSH, SFT, PRA, EVN
)

pmu_b04 = PMU_B04(  #  - An event B04 signals that a staff member is available for work (e
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    staff_identification=stf,  # STF(...)  # Required.
    practitioner_detail=None,  # PRA(...) 
    practitioner_organization_unit=None,  # ORG(...) 
)

-----END TRIGGER_EVENT::PMU_B04 TEMPLATE-----
"""


class PMU_B04(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """PMU_B04"""
    _hl7_name = """Active practicing person"""
    _hl7_description = """An event B04 signals that a staff member is available for work (e"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PMU_B04"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6")
    _c_components = (MSH, SFT, EVN, STF, PRA, ORG)
    _c_name = ("MSH", "SFT", "EVN", "STF", "PRA", "ORG")
    _c_is_group = (False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "staff_identification", "practitioner_detail", "practitioner_organization_unit",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        staff_identification: STF,  #  Required. STF.4
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        practitioner_detail: PRA | tuple[PRA, ...] | None = None,  #  PRA.5
        practitioner_organization_unit: ORG | tuple[ORG, ...] | None = None,  #  ORG.6
    ):
        """
         - `PMU_B04 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PMU_B04>`_
        An event B04 signals that a staff member is available for work (e.g. schedules can be created) and has a relationship with the institution.  This message applies to STF-7.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param staff_identification: Staff Identification (id: STF | seq: 4 | use: R | rpt: 1)
        :param practitioner_detail: Practitioner Detail (id: PRA | seq: 5 | use: O | rpt: *)
        :param practitioner_organization_unit: Practitioner Organization Unit (id: ORG | seq: 6 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.staff_identification = staff_identification
        self.practitioner_detail = practitioner_detail
        self.practitioner_organization_unit = practitioner_organization_unit

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

    @property  # get PRA
    def practitioner_detail(self) -> tuple[PRA, ...] | tuple[None]:
        """
        id: PRA SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        return_type: tuple[PRA, ...]: (Practitioner Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRA
        """
        return self._c_data[4]

    @practitioner_detail.setter  # set PRA
    def practitioner_detail(self, pra: PRA | tuple[PRA, ...] | None):
        """
        id: PRA SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        param_type: PRA.5 | tuple[PRA, ...]: (Practitioner Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRA
        """
        if isinstance(pra, tuple):
            self._c_data[4] = pra
        else:
            self._c_data[4] = (pra,)

    @property  # get ORG
    def practitioner_organization_unit(self) -> tuple[ORG, ...] | tuple[None]:
        """
        id: ORG SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[ORG, ...]: (Practitioner Organization Unit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG
        """
        return self._c_data[5]

    @practitioner_organization_unit.setter  # set ORG
    def practitioner_organization_unit(self, org: ORG | tuple[ORG, ...] | None):
        """
        id: ORG SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: ORG.6 | tuple[ORG, ...]: (Practitioner Organization Unit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG
        """
        if isinstance(org, tuple):
            self._c_data[5] = org
        else:
            self._c_data[5] = (org,)
