from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.QRF import QRF
from ..segments.NTE import NTE
from ..segments.GT1 import GT1
from ..segments.QRD import QRD
from ..segment_groups.RQC_I06_PROVIDER_GROUP import RQC_I06_PROVIDER_GROUP
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.NK1 import NK1


"""
Request/receipt of clinical data listing - RQC_I06
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RQC_I06 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RQC_I06
from utils.hl7.v2_5_1.segments import (
    NTE, GT1, NK1, QRD, MSH, SFT, PID, QRF
)
from utils.hl7.v2_5_1.segment_groups import (
    RQC_I06_PROVIDER_GROUP
)

rqc_i06 = RQC_I06(  #  - This event code is sent from one healthcare provider to another  (typically a laboratory or radiology, etc
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
    provider=rqc_i06_provider_group,  # RQC_I06_PROVIDER_GROUP(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    guarantor=None,  # GT1(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT::RQC_I06 TEMPLATE-----
"""


class RQC_I06(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RQC_I06"""
    _hl7_name = """Request/receipt of clinical data listing"""
    _hl7_description = """This event code is sent from one healthcare provider to another  (typically a laboratory or radiology, etc"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQC_I06"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535, 1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "O", "R", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "None", "7", "8", "9", "10")
    _c_components = (MSH, SFT, QRD, QRF, RQC_I06_PROVIDER_GROUP, PID, NK1, GT1, NTE)
    _c_name = ("MSH", "SFT", "QRD", "QRF", "PROVIDER", "PID", "NK1", "GT1", "NTE")
    _c_is_group = (False, False, False, False, True, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "original_style_query_definition", "original_style_query_filter", "provider", "patient_identification", "next_of_kin_or_associated_parties", "guarantor", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        original_style_query_definition: QRD,  #  Required. QRD.3
        provider: RQC_I06_PROVIDER_GROUP
        | tuple[RQC_I06_PROVIDER_GROUP, ...],  #  Required. (PRD.5, CTD.6, ...)
        patient_identification: PID,  #  Required. PID.7
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        original_style_query_filter: QRF | None = None,  #  QRF.4
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.8
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.9
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.10
    ):
        """
         - `RQC_I06 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQC_I06>`_
        This event code is sent from one healthcare provider to another  (typically a laboratory or radiology, etc.) to request a list of available clinical observation information.  When the provider is dealing with a community model in which remote requests make transmission of large amounts of data impractical, this event code will provide for interactive lists of transactions from which more specific selections can be made.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 3 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 4 | use: O | rpt: 1)
        :param provider: Provider segment group: [PRD, CTD|None] (id: PROVIDER | seq: 5, 6 | use: R | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 7 | use: R | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 8 | use: O | rpt: *)
        :param guarantor: Guarantor (id: GT1 | seq: 9 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 10 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.message_header = message_header
        self.software_segment = software_segment
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter
        self.provider = provider
        self.patient_identification = patient_identification
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.guarantor = guarantor
        self.notes_and_comments = notes_and_comments

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

    @property  # get QRD.3
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 3
        ---
        return_type: QRD.3: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[2][0]

    @original_style_query_definition.setter  # set QRD.3
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 3
        ---
        param_type: QRD.3: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[2] = (qrd,)

    @property  # get QRF.4
    def original_style_query_filter(self) -> QRF | None:
        """
        id: QRF | use: O | rpt: 1 | seq: 4
        ---
        return_type: QRF.4: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        return self._c_data[3][0]

    @original_style_query_filter.setter  # set QRF.4
    def original_style_query_filter(self, qrf: QRF | None):
        """
        id: QRF | use: O | rpt: 1 | seq: 4
        ---
        param_type: QRF.4: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        self._c_data[3] = (qrf,)

    @property  # get PROVIDER
    def provider(self) -> tuple[RQC_I06_PROVIDER_GROUP, ...]:
        """
        id: RQC_I06_PROVIDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RQC_I06_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQC_I06_PROVIDER_GROUP
        """
        return self._c_data[4]

    @provider.setter  # set PROVIDER
    def provider(
        self, provider: RQC_I06_PROVIDER_GROUP | tuple[RQC_I06_PROVIDER_GROUP, ...]
    ):
        """
        id: PROVIDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RQC_I06_PROVIDER_GROUP.None | tuple[RQC_I06_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQC_I06_PROVIDER_GROUP
        """
        if isinstance(provider, tuple):
            self._c_data[4] = provider
        else:
            self._c_data[4] = (provider,)

    @property  # get PID.7
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        return_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[5][0]

    @patient_identification.setter  # set PID.7
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        param_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[5] = (pid,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[6]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: NK1.8 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[6] = nk1
        else:
            self._c_data[6] = (nk1,)

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[7]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: GT1.9 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[7] = gt1
        else:
            self._c_data[7] = (gt1,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[8]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: NTE.10 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[8] = nte
        else:
            self._c_data[8] = (nte,)
