from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.RPI_I04_GUARANTOR_INSURANCE_GROUP import (
    RPI_I04_GUARANTOR_INSURANCE_GROUP,
)
from ..segments.SFT import SFT
from ..segments.NTE import NTE
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.MSA import MSA
from ..segments.NK1 import NK1
from ..segment_groups.RPI_I04_PROVIDER_GROUP import RPI_I04_PROVIDER_GROUP


"""
Request for patient demographic data acknowledgement - RPI_I04
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RPI_I04 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RPI_I04
from utils.hl7.v2_5_1.segments import (
    NTE, MSA, NK1, MSH, SFT, PID
)
from utils.hl7.v2_5_1.segment_groups import (
    RPI_I04_PROVIDER_GROUP, RPI_I04_GUARANTOR_INSURANCE_GROUP
)

rpi_i04 = RPI_I04(  #  - This event triggers a request from one healthcare provider to another for patient demographic information, including insurance and billing information
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    provider=rpi_i04_provider_group,  # RPI_I04_PROVIDER_GROUP(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    guarantor_insurance=None,  # RPI_I04_GUARANTOR_INSURANCE_GROUP(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT::RPI_I04 TEMPLATE-----
"""


class RPI_I04(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RPI_I04"""
    _hl7_name = """Request for patient demographic data acknowledgement"""
    _hl7_description = """This event triggers a request from one healthcare provider to another for patient demographic information, including insurance and billing information"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPI_I04"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "None", "6", "7", "None", "12")
    _c_components = (MSH, SFT, MSA, RPI_I04_PROVIDER_GROUP, PID, NK1, RPI_I04_GUARANTOR_INSURANCE_GROUP, NTE)
    _c_name = ("MSH", "SFT", "MSA", "PROVIDER", "PID", "NK1", "GUARANTOR INSURANCE", "NTE")
    _c_is_group = (False, False, False, True, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "provider", "patient_identification", "next_of_kin_or_associated_parties", "guarantor_insurance", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        provider: RPI_I04_PROVIDER_GROUP
        | tuple[RPI_I04_PROVIDER_GROUP, ...],  #  Required. (PRD.4, CTD.5, ...)
        patient_identification: PID,  #  Required. PID.6
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.7
        guarantor_insurance: RPI_I04_GUARANTOR_INSURANCE_GROUP | None = None,  #  GT1.8
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.12
    ):
        """
         - `RPI_I04 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPI_I04>`_
        This event triggers a request from one healthcare provider to another for patient demographic information, including insurance and billing information.  Typically, this transaction would occur between one provider to another, but it could also be directed to a payor.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param provider: Provider segment group: [PRD, CTD|None] (id: PROVIDER | seq: 4, 5 | use: R | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 6 | use: R | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 7 | use: O | rpt: *)
        :param guarantor_insurance: Guarantor Insurance segment group: [GT1|None, INSURANCE] (id: GUARANTOR INSURANCE | seq: 8, None | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 12 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.provider = provider
        self.patient_identification = patient_identification
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.guarantor_insurance = guarantor_insurance
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

    @property  # get MSA.3
    def message_acknowledgment(self) -> MSA:
        """
        id: MSA | use: R | rpt: 1 | seq: 3
        ---
        return_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        return self._c_data[2][0]

    @message_acknowledgment.setter  # set MSA.3
    def message_acknowledgment(self, msa: MSA):
        """
        id: MSA | use: R | rpt: 1 | seq: 3
        ---
        param_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        self._c_data[2] = (msa,)

    @property  # get PROVIDER
    def provider(self) -> tuple[RPI_I04_PROVIDER_GROUP, ...]:
        """
        id: RPI_I04_PROVIDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RPI_I04_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPI_I04_PROVIDER_GROUP
        """
        return self._c_data[3]

    @provider.setter  # set PROVIDER
    def provider(
        self, provider: RPI_I04_PROVIDER_GROUP | tuple[RPI_I04_PROVIDER_GROUP, ...]
    ):
        """
        id: PROVIDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RPI_I04_PROVIDER_GROUP.None | tuple[RPI_I04_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPI_I04_PROVIDER_GROUP
        """
        if isinstance(provider, tuple):
            self._c_data[3] = provider
        else:
            self._c_data[3] = (provider,)

    @property  # get PID.6
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 6
        ---
        return_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[4][0]

    @patient_identification.setter  # set PID.6
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 6
        ---
        param_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[4] = (pid,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[5]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: NK1.7 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[5] = nk1
        else:
            self._c_data[5] = (nk1,)

    @property  # get RPI_I04_GUARANTOR_INSURANCE_GROUP.None
    def guarantor_insurance(self) -> RPI_I04_GUARANTOR_INSURANCE_GROUP | None:
        """
        id: RPI_I04_GUARANTOR_INSURANCE_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RPI_I04_GUARANTOR_INSURANCE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPI_I04_GUARANTOR_INSURANCE_GROUP
        """
        return self._c_data[6][0]

    @guarantor_insurance.setter  # set RPI_I04_GUARANTOR_INSURANCE_GROUP.None
    def guarantor_insurance(
        self, guarantor_insurance: RPI_I04_GUARANTOR_INSURANCE_GROUP | None
    ):
        """
        id: RPI_I04_GUARANTOR_INSURANCE_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RPI_I04_GUARANTOR_INSURANCE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPI_I04_GUARANTOR_INSURANCE_GROUP
        """
        self._c_data[6] = (guarantor_insurance,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[7]

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
            self._c_data[7] = nte
        else:
            self._c_data[7] = (nte,)
