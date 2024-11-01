from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.LAN import LAN
from ..segments.EDU import EDU
from ..segments.MSH import MSH
from ..segments.EVN import EVN
from ..segments.AFF import AFF
from ..segments.CER import CER
from ..segments.PRA import PRA
from ..segments.STF import STF
from ..segments.ORG import ORG
from ..segments.SFT import SFT


"""
Add personnel record - PMU_B01
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::PMU_B01 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PMU_B01
from utils.hl7.v2_5_1.segments import (
    CER, PRA, AFF, EDU, SFT, EVN, MSH, STF, ORG, LAN
)

pmu_b01 = PMU_B01(  #  - An event B01 signals to add a new record for healthcare administration information about an individual healthcare practitioner establishing a relationship between that practitioner and the institution
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    staff_identification=stf,  # STF(...)  # Required.
    practitioner_detail=None,  # PRA(...) 
    practitioner_organization_unit=None,  # ORG(...) 
    professional_affiliation=None,  # AFF(...) 
    language_detail=None,  # LAN(...) 
    educational_detail=None,  # EDU(...) 
    certificate_detail=None,  # CER(...) 
)

-----END TRIGGER_EVENT::PMU_B01 TEMPLATE-----
"""


class PMU_B01(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """PMU_B01"""
    _hl7_name = """Add personnel record"""
    _hl7_description = """An event B01 signals to add a new record for healthcare administration information about an individual healthcare practitioner establishing a relationship between that practitioner and the institution"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PMU_B01"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    _c_components = (MSH, SFT, EVN, STF, PRA, ORG, AFF, LAN, EDU, CER)
    _c_name = ("MSH", "SFT", "EVN", "STF", "PRA", "ORG", "AFF", "LAN", "EDU", "CER")
    _c_is_group = (False, False, False, False, False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "staff_identification", "practitioner_detail", "practitioner_organization_unit", "professional_affiliation", "language_detail", "educational_detail", "certificate_detail",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        staff_identification: STF,  #  Required. STF.4
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        practitioner_detail: PRA | tuple[PRA, ...] | None = None,  #  PRA.5
        practitioner_organization_unit: ORG | tuple[ORG, ...] | None = None,  #  ORG.6
        professional_affiliation: AFF | tuple[AFF, ...] | None = None,  #  AFF.7
        language_detail: LAN | tuple[LAN, ...] | None = None,  #  LAN.8
        educational_detail: EDU | tuple[EDU, ...] | None = None,  #  EDU.9
        certificate_detail: CER | tuple[CER, ...] | None = None,  #  CER.10
    ):
        """
         - `PMU_B01 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PMU_B01>`_
        An event B01 signals to add a new record for healthcare administration information about an individual healthcare practitioner establishing a relationship between that practitioner and the institution.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param staff_identification: Staff Identification (id: STF | seq: 4 | use: R | rpt: 1)
        :param practitioner_detail: Practitioner Detail (id: PRA | seq: 5 | use: O | rpt: *)
        :param practitioner_organization_unit: Practitioner Organization Unit (id: ORG | seq: 6 | use: O | rpt: *)
        :param professional_affiliation: Professional Affiliation (id: AFF | seq: 7 | use: O | rpt: *)
        :param language_detail: Language Detail (id: LAN | seq: 8 | use: O | rpt: *)
        :param educational_detail: Educational Detail (id: EDU | seq: 9 | use: O | rpt: *)
        :param certificate_detail: Certificate Detail (id: CER | seq: 10 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.staff_identification = staff_identification
        self.practitioner_detail = practitioner_detail
        self.practitioner_organization_unit = practitioner_organization_unit
        self.professional_affiliation = professional_affiliation
        self.language_detail = language_detail
        self.educational_detail = educational_detail
        self.certificate_detail = certificate_detail

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

    @property  # get AFF
    def professional_affiliation(self) -> tuple[AFF, ...] | tuple[None]:
        """
        id: AFF SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[AFF, ...]: (Professional Affiliation, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AFF
        """
        return self._c_data[6]

    @professional_affiliation.setter  # set AFF
    def professional_affiliation(self, aff: AFF | tuple[AFF, ...] | None):
        """
        id: AFF SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: AFF.7 | tuple[AFF, ...]: (Professional Affiliation, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AFF
        """
        if isinstance(aff, tuple):
            self._c_data[6] = aff
        else:
            self._c_data[6] = (aff,)

    @property  # get LAN
    def language_detail(self) -> tuple[LAN, ...] | tuple[None]:
        """
        id: LAN SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[LAN, ...]: (Language Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LAN
        """
        return self._c_data[7]

    @language_detail.setter  # set LAN
    def language_detail(self, lan: LAN | tuple[LAN, ...] | None):
        """
        id: LAN SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: LAN.8 | tuple[LAN, ...]: (Language Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LAN
        """
        if isinstance(lan, tuple):
            self._c_data[7] = lan
        else:
            self._c_data[7] = (lan,)

    @property  # get EDU
    def educational_detail(self) -> tuple[EDU, ...] | tuple[None]:
        """
        id: EDU SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[EDU, ...]: (Educational Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EDU
        """
        return self._c_data[8]

    @educational_detail.setter  # set EDU
    def educational_detail(self, edu: EDU | tuple[EDU, ...] | None):
        """
        id: EDU SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: EDU.9 | tuple[EDU, ...]: (Educational Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EDU
        """
        if isinstance(edu, tuple):
            self._c_data[8] = edu
        else:
            self._c_data[8] = (edu,)

    @property  # get CER
    def certificate_detail(self) -> tuple[CER, ...] | tuple[None]:
        """
        id: CER SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[CER, ...]: (Certificate Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CER
        """
        return self._c_data[9]

    @certificate_detail.setter  # set CER
    def certificate_detail(self, cer: CER | tuple[CER, ...] | None):
        """
        id: CER SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: CER.10 | tuple[CER, ...]: (Certificate Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CER
        """
        if isinstance(cer, tuple):
            self._c_data[9] = cer
        else:
            self._c_data[9] = (cer,)
