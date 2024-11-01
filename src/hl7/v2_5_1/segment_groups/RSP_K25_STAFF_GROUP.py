from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.STF import STF
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.AFF import AFF
from ..segments.EDU import EDU
from ..segments.LAN import LAN
from ..segments.CER import CER


"""
STAFF - RSP_K25_STAFF_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_K25_STAFF_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_K25_STAFF_GROUP
from utils.hl7.v2_5_1.segments import (
    PRA, AFF, ORG, CER, STF, EDU, LAN
)

rsp_k25_staff_group = RSP_K25_STAFF_GROUP(  # STAFF - Segment group for RSP_K25 - Response - Personnel information consisting of STF, PRA|None, ORG|None, AFF|None, LAN|None, EDU|None, CER|None
    staff_identification=stf,  # STF(...)  # Required.
    practitioner_detail=None,  # PRA(...) 
    practitioner_organization_unit=None,  # ORG(...) 
    professional_affiliation=None,  # AFF(...) 
    language_detail=None,  # LAN(...) 
    educational_detail=None,  # EDU(...) 
    certificate_detail=None,  # CER(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_K25_STAFF_GROUP TEMPLATE-----
"""


class RSP_K25_STAFF_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_K25_STAFF_GROUP"""
    _hl7_name = """STAFF"""
    _hl7_description = """Segment group for RSP_K25 - Response - Personnel information consisting of STF, PRA|None, ORG|None, AFF|None, LAN|None, EDU|None, CER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K25_STAFF_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("8", "9", "10", "11", "12", "13", "14")
    _c_components = (STF, PRA, ORG, AFF, LAN, EDU, CER)
    _c_name = ("STF", "PRA", "ORG", "AFF", "LAN", "EDU", "CER")
    _c_is_group = (False, False, False, False, False, False, False)
    _c_attrs = ("staff_identification", "practitioner_detail", "practitioner_organization_unit", "professional_affiliation", "language_detail", "educational_detail", "certificate_detail",)
    # fmt: on

    def __init__(
        self,
        staff_identification: STF,  #  Required. STF.8
        practitioner_detail: PRA | tuple[PRA, ...] | None = None,  #  PRA.9
        practitioner_organization_unit: ORG | tuple[ORG, ...] | None = None,  #  ORG.10
        professional_affiliation: AFF | tuple[AFF, ...] | None = None,  #  AFF.11
        language_detail: LAN | tuple[LAN, ...] | None = None,  #  LAN.12
        educational_detail: EDU | tuple[EDU, ...] | None = None,  #  EDU.13
        certificate_detail: CER | tuple[CER, ...] | None = None,  #  CER.14
    ):
        """
        None - `RSP_K25_STAFF_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K25_STAFF_GROUP>`_
        Segment group for RSP_K25 - Response - Personnel information consisting of STF, PRA|None, ORG|None, AFF|None, LAN|None, EDU|None, CER|None

        :param staff_identification: Staff Identification (id: STF | seq: 8 | use: R | rpt: 1)
        :param practitioner_detail: Practitioner Detail (id: PRA | seq: 9 | use: O | rpt: *)
        :param practitioner_organization_unit: Practitioner Organization Unit (id: ORG | seq: 10 | use: O | rpt: *)
        :param professional_affiliation: Professional Affiliation (id: AFF | seq: 11 | use: O | rpt: *)
        :param language_detail: Language Detail (id: LAN | seq: 12 | use: O | rpt: *)
        :param educational_detail: Educational Detail (id: EDU | seq: 13 | use: O | rpt: *)
        :param certificate_detail: Certificate Detail (id: CER | seq: 14 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.staff_identification = staff_identification
        self.practitioner_detail = practitioner_detail
        self.practitioner_organization_unit = practitioner_organization_unit
        self.professional_affiliation = professional_affiliation
        self.language_detail = language_detail
        self.educational_detail = educational_detail
        self.certificate_detail = certificate_detail

    @property  # get STF.8
    def staff_identification(self) -> STF:
        """
        id: STF | use: R | rpt: 1 | seq: 8
        ---
        return_type: STF.8: Staff Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/STF
        """
        return self._c_data[0][0]

    @staff_identification.setter  # set STF.8
    def staff_identification(self, stf: STF):
        """
        id: STF | use: R | rpt: 1 | seq: 8
        ---
        param_type: STF.8: Staff Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/STF
        """
        self._c_data[0] = (stf,)

    @property  # get PRA
    def practitioner_detail(self) -> tuple[PRA, ...] | tuple[None]:
        """
        id: PRA SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[PRA, ...]: (Practitioner Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRA
        """
        return self._c_data[1]

    @practitioner_detail.setter  # set PRA
    def practitioner_detail(self, pra: PRA | tuple[PRA, ...] | None):
        """
        id: PRA SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: PRA.9 | tuple[PRA, ...]: (Practitioner Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRA
        """
        if isinstance(pra, tuple):
            self._c_data[1] = pra
        else:
            self._c_data[1] = (pra,)

    @property  # get ORG
    def practitioner_organization_unit(self) -> tuple[ORG, ...] | tuple[None]:
        """
        id: ORG SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[ORG, ...]: (Practitioner Organization Unit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG
        """
        return self._c_data[2]

    @practitioner_organization_unit.setter  # set ORG
    def practitioner_organization_unit(self, org: ORG | tuple[ORG, ...] | None):
        """
        id: ORG SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: ORG.10 | tuple[ORG, ...]: (Practitioner Organization Unit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG
        """
        if isinstance(org, tuple):
            self._c_data[2] = org
        else:
            self._c_data[2] = (org,)

    @property  # get AFF
    def professional_affiliation(self) -> tuple[AFF, ...] | tuple[None]:
        """
        id: AFF SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[AFF, ...]: (Professional Affiliation, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AFF
        """
        return self._c_data[3]

    @professional_affiliation.setter  # set AFF
    def professional_affiliation(self, aff: AFF | tuple[AFF, ...] | None):
        """
        id: AFF SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: AFF.11 | tuple[AFF, ...]: (Professional Affiliation, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AFF
        """
        if isinstance(aff, tuple):
            self._c_data[3] = aff
        else:
            self._c_data[3] = (aff,)

    @property  # get LAN
    def language_detail(self) -> tuple[LAN, ...] | tuple[None]:
        """
        id: LAN SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[LAN, ...]: (Language Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LAN
        """
        return self._c_data[4]

    @language_detail.setter  # set LAN
    def language_detail(self, lan: LAN | tuple[LAN, ...] | None):
        """
        id: LAN SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: LAN.12 | tuple[LAN, ...]: (Language Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LAN
        """
        if isinstance(lan, tuple):
            self._c_data[4] = lan
        else:
            self._c_data[4] = (lan,)

    @property  # get EDU
    def educational_detail(self) -> tuple[EDU, ...] | tuple[None]:
        """
        id: EDU SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[EDU, ...]: (Educational Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EDU
        """
        return self._c_data[5]

    @educational_detail.setter  # set EDU
    def educational_detail(self, edu: EDU | tuple[EDU, ...] | None):
        """
        id: EDU SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        param_type: EDU.13 | tuple[EDU, ...]: (Educational Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EDU
        """
        if isinstance(edu, tuple):
            self._c_data[5] = edu
        else:
            self._c_data[5] = (edu,)

    @property  # get CER
    def certificate_detail(self) -> tuple[CER, ...] | tuple[None]:
        """
        id: CER SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        return_type: tuple[CER, ...]: (Certificate Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CER
        """
        return self._c_data[6]

    @certificate_detail.setter  # set CER
    def certificate_detail(self, cer: CER | tuple[CER, ...] | None):
        """
        id: CER SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        param_type: CER.14 | tuple[CER, ...]: (Certificate Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CER
        """
        if isinstance(cer, tuple):
            self._c_data[6] = cer
        else:
            self._c_data[6] = (cer,)
