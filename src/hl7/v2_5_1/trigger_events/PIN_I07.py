from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.PIN_I07_GUARANTOR_INSURANCE_GROUP import (
    PIN_I07_GUARANTOR_INSURANCE_GROUP,
)
from ..segments.NK1 import NK1
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.NTE import NTE
from ..segment_groups.PIN_I07_PROVIDER_GROUP import PIN_I07_PROVIDER_GROUP
from ..segments.SFT import SFT


"""
Unsolicited insurance information - PIN_I07
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::PIN_I07 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PIN_I07
from utils.hl7.v2_5_1.segments import (
    NK1, NTE, PID, SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    PIN_I07_GUARANTOR_INSURANCE_GROUP, PIN_I07_PROVIDER_GROUP
)

pin_i07 = PIN_I07(  #  - This trigger event is used by an entity or organization to transmit to a healthcare provider the insurance information on a specific patient
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    provider=pin_i07_provider_group,  # PIN_I07_PROVIDER_GROUP(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    guarantor_insurance=None,  # PIN_I07_GUARANTOR_INSURANCE_GROUP(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT::PIN_I07 TEMPLATE-----
"""


class PIN_I07(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """PIN_I07"""
    _hl7_name = """Unsolicited insurance information"""
    _hl7_description = """This trigger event is used by an entity or organization to transmit to a healthcare provider the insurance information on a specific patient"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PIN_I07"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "None", "5", "6", "None", "11")
    _c_components = (MSH, SFT, PIN_I07_PROVIDER_GROUP, PID, NK1, PIN_I07_GUARANTOR_INSURANCE_GROUP, NTE)
    _c_name = ("MSH", "SFT", "PROVIDER", "PID", "NK1", "GUARANTOR INSURANCE", "NTE")
    _c_is_group = (False, False, True, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "provider", "patient_identification", "next_of_kin_or_associated_parties", "guarantor_insurance", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        provider: PIN_I07_PROVIDER_GROUP
        | tuple[PIN_I07_PROVIDER_GROUP, ...],  #  Required. (PRD.3, CTD.4, ...)
        patient_identification: PID,  #  Required. PID.5
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.6
        guarantor_insurance: PIN_I07_GUARANTOR_INSURANCE_GROUP | None = None,  #  GT1.7
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.11
    ):
        """
         - `PIN_I07 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PIN_I07>`_
        This trigger event is used by an entity or organization to transmit to a healthcare provider the insurance information on a specific patient.  Typically, the healthcare provider will be a primary care provider.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param provider: Provider segment group: [PRD, CTD|None] (id: PROVIDER | seq: 3, 4 | use: R | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 5 | use: R | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 6 | use: O | rpt: *)
        :param guarantor_insurance: Guarantor Insurance segment group: [GT1|None, INSURANCE] (id: GUARANTOR INSURANCE | seq: 7, None | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 11 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.message_header = message_header
        self.software_segment = software_segment
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

    @property  # get PROVIDER
    def provider(self) -> tuple[PIN_I07_PROVIDER_GROUP, ...]:
        """
        id: PIN_I07_PROVIDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PIN_I07_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PIN_I07_PROVIDER_GROUP
        """
        return self._c_data[2]

    @provider.setter  # set PROVIDER
    def provider(
        self, provider: PIN_I07_PROVIDER_GROUP | tuple[PIN_I07_PROVIDER_GROUP, ...]
    ):
        """
        id: PROVIDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PIN_I07_PROVIDER_GROUP.None | tuple[PIN_I07_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PIN_I07_PROVIDER_GROUP
        """
        if isinstance(provider, tuple):
            self._c_data[2] = provider
        else:
            self._c_data[2] = (provider,)

    @property  # get PID.5
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 5
        ---
        return_type: PID.5: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[3][0]

    @patient_identification.setter  # set PID.5
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 5
        ---
        param_type: PID.5: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[3] = (pid,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[4]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: NK1.6 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[4] = nk1
        else:
            self._c_data[4] = (nk1,)

    @property  # get PIN_I07_GUARANTOR_INSURANCE_GROUP.None
    def guarantor_insurance(self) -> PIN_I07_GUARANTOR_INSURANCE_GROUP | None:
        """
        id: PIN_I07_GUARANTOR_INSURANCE_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PIN_I07_GUARANTOR_INSURANCE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PIN_I07_GUARANTOR_INSURANCE_GROUP
        """
        return self._c_data[5][0]

    @guarantor_insurance.setter  # set PIN_I07_GUARANTOR_INSURANCE_GROUP.None
    def guarantor_insurance(
        self, guarantor_insurance: PIN_I07_GUARANTOR_INSURANCE_GROUP | None
    ):
        """
        id: PIN_I07_GUARANTOR_INSURANCE_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PIN_I07_GUARANTOR_INSURANCE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PIN_I07_GUARANTOR_INSURANCE_GROUP
        """
        self._c_data[5] = (guarantor_insurance,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[6]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: NTE.11 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[6] = nte
        else:
            self._c_data[6] = (nte,)
