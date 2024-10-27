from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.AFF import AFF
from ..segments.NTE import NTE
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.LAN import LAN
from ..segments.MFE import MFE
from ..segments.STF import STF
from ..segments.CER import CER
from ..segments.EDU import EDU


"""
MF STAFF - MFN_M02_MF_STAFF_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M02_MF_STAFF_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M02_MF_STAFF_GROUP
from utils.hl7.v2_5_1.segments import (
    AFF, NTE, STF, EDU, LAN, MFE, CER, ORG, PRA
)

mfn_m02_mf_staff_group = MFN_M02_MF_STAFF_GROUP(  # MF STAFF - Segment group for MFN_M02 - Master files notification - Staff/practitioner master file consisting of MFE, STF, PRA|None, ORG|None, AFF|None, LAN|None, EDU|None, CER|None, NTE|None
    master_file_entry=mfe,  # MFE(...)  # Required.
    staff_identification=stf,  # STF(...)  # Required.
    practitioner_detail=None,  # PRA(...) 
    practitioner_organization_unit=None,  # ORG(...) 
    professional_affiliation=None,  # AFF(...) 
    language_detail=None,  # LAN(...) 
    educational_detail=None,  # EDU(...) 
    certificate_detail=None,  # CER(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M02_MF_STAFF_GROUP TEMPLATE-----
"""


class MFN_M02_MF_STAFF_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M02_MF_STAFF_GROUP"""
    _hl7_name = """MF STAFF"""
    _hl7_description = """Segment group for MFN_M02 - Master files notification - Staff/practitioner master file consisting of MFE, STF, PRA|None, ORG|None, AFF|None, LAN|None, EDU|None, CER|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M02_MF_STAFF_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "R", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("4", "5", "6", "7", "8", "9", "10", "11", "12")
    _c_components = (MFE, STF, PRA, ORG, AFF, LAN, EDU, CER, NTE)
    _c_name = ("MFE", "STF", "PRA", "ORG", "AFF", "LAN", "EDU", "CER", "NTE")
    _c_is_group = (False, False, False, False, False, False, False, False, False)
    _c_attrs = ("master_file_entry", "staff_identification", "practitioner_detail", "practitioner_organization_unit", "professional_affiliation", "language_detail", "educational_detail", "certificate_detail", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.4
        staff_identification: STF,  #  Required. STF.5
        practitioner_detail: PRA | tuple[PRA, ...] | None = None,  #  PRA.6
        practitioner_organization_unit: ORG | tuple[ORG, ...] | None = None,  #  ORG.7
        professional_affiliation: AFF | tuple[AFF, ...] | None = None,  #  AFF.8
        language_detail: LAN | tuple[LAN, ...] | None = None,  #  LAN.9
        educational_detail: EDU | tuple[EDU, ...] | None = None,  #  EDU.10
        certificate_detail: CER | tuple[CER, ...] | None = None,  #  CER.11
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.12
    ):
        """
        None - `MFN_M02_MF_STAFF_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M02_MF_STAFF_GROUP>`_
        Segment group for MFN_M02 - Master files notification - Staff/practitioner master file consisting of MFE, STF, PRA|None, ORG|None, AFF|None, LAN|None, EDU|None, CER|None, NTE|None

        :param master_file_entry: Master File Entry (id: MFE | seq: 4 | use: R | rpt: 1)
        :param staff_identification: Staff Identification (id: STF | seq: 5 | use: R | rpt: 1)
        :param practitioner_detail: Practitioner Detail (id: PRA | seq: 6 | use: O | rpt: *)
        :param practitioner_organization_unit: Practitioner Organization Unit (id: ORG | seq: 7 | use: O | rpt: *)
        :param professional_affiliation: Professional Affiliation (id: AFF | seq: 8 | use: O | rpt: *)
        :param language_detail: Language Detail (id: LAN | seq: 9 | use: O | rpt: *)
        :param educational_detail: Educational Detail (id: EDU | seq: 10 | use: O | rpt: *)
        :param certificate_detail: Certificate Detail (id: CER | seq: 11 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 12 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.master_file_entry = master_file_entry
        self.staff_identification = staff_identification
        self.practitioner_detail = practitioner_detail
        self.practitioner_organization_unit = practitioner_organization_unit
        self.professional_affiliation = professional_affiliation
        self.language_detail = language_detail
        self.educational_detail = educational_detail
        self.certificate_detail = certificate_detail
        self.notes_and_comments = notes_and_comments

    @property  # get MFE.4
    def master_file_entry(self) -> MFE:
        """
        id: MFE | use: R | rpt: 1 | seq: 4
        ---
        return_type: MFE.4: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        return self._c_data[0][0]

    @master_file_entry.setter  # set MFE.4
    def master_file_entry(self, mfe: MFE):
        """
        id: MFE | use: R | rpt: 1 | seq: 4
        ---
        param_type: MFE.4: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        self._c_data[0] = (mfe,)

    @property  # get STF.5
    def staff_identification(self) -> STF:
        """
        id: STF | use: R | rpt: 1 | seq: 5
        ---
        return_type: STF.5: Staff Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/STF
        """
        return self._c_data[1][0]

    @staff_identification.setter  # set STF.5
    def staff_identification(self, stf: STF):
        """
        id: STF | use: R | rpt: 1 | seq: 5
        ---
        param_type: STF.5: Staff Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/STF
        """
        self._c_data[1] = (stf,)

    @property  # get PRA
    def practitioner_detail(self) -> tuple[PRA, ...] | tuple[None]:
        """
        id: PRA SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[PRA, ...]: (Practitioner Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRA
        """
        return self._c_data[2]

    @practitioner_detail.setter  # set PRA
    def practitioner_detail(self, pra: PRA | tuple[PRA, ...] | None):
        """
        id: PRA SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: PRA.6 | tuple[PRA, ...]: (Practitioner Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRA
        """
        if isinstance(pra, tuple):
            self._c_data[2] = pra
        else:
            self._c_data[2] = (pra,)

    @property  # get ORG
    def practitioner_organization_unit(self) -> tuple[ORG, ...] | tuple[None]:
        """
        id: ORG SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[ORG, ...]: (Practitioner Organization Unit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG
        """
        return self._c_data[3]

    @practitioner_organization_unit.setter  # set ORG
    def practitioner_organization_unit(self, org: ORG | tuple[ORG, ...] | None):
        """
        id: ORG SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: ORG.7 | tuple[ORG, ...]: (Practitioner Organization Unit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG
        """
        if isinstance(org, tuple):
            self._c_data[3] = org
        else:
            self._c_data[3] = (org,)

    @property  # get AFF
    def professional_affiliation(self) -> tuple[AFF, ...] | tuple[None]:
        """
        id: AFF SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[AFF, ...]: (Professional Affiliation, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AFF
        """
        return self._c_data[4]

    @professional_affiliation.setter  # set AFF
    def professional_affiliation(self, aff: AFF | tuple[AFF, ...] | None):
        """
        id: AFF SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: AFF.8 | tuple[AFF, ...]: (Professional Affiliation, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AFF
        """
        if isinstance(aff, tuple):
            self._c_data[4] = aff
        else:
            self._c_data[4] = (aff,)

    @property  # get LAN
    def language_detail(self) -> tuple[LAN, ...] | tuple[None]:
        """
        id: LAN SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[LAN, ...]: (Language Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LAN
        """
        return self._c_data[5]

    @language_detail.setter  # set LAN
    def language_detail(self, lan: LAN | tuple[LAN, ...] | None):
        """
        id: LAN SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: LAN.9 | tuple[LAN, ...]: (Language Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LAN
        """
        if isinstance(lan, tuple):
            self._c_data[5] = lan
        else:
            self._c_data[5] = (lan,)

    @property  # get EDU
    def educational_detail(self) -> tuple[EDU, ...] | tuple[None]:
        """
        id: EDU SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[EDU, ...]: (Educational Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EDU
        """
        return self._c_data[6]

    @educational_detail.setter  # set EDU
    def educational_detail(self, edu: EDU | tuple[EDU, ...] | None):
        """
        id: EDU SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: EDU.10 | tuple[EDU, ...]: (Educational Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EDU
        """
        if isinstance(edu, tuple):
            self._c_data[6] = edu
        else:
            self._c_data[6] = (edu,)

    @property  # get CER
    def certificate_detail(self) -> tuple[CER, ...] | tuple[None]:
        """
        id: CER SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[CER, ...]: (Certificate Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CER
        """
        return self._c_data[7]

    @certificate_detail.setter  # set CER
    def certificate_detail(self, cer: CER | tuple[CER, ...] | None):
        """
        id: CER SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: CER.11 | tuple[CER, ...]: (Certificate Detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CER
        """
        if isinstance(cer, tuple):
            self._c_data[7] = cer
        else:
            self._c_data[7] = (cer,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[8]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: NTE.12 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[8] = nte
        else:
            self._c_data[8] = (nte,)
