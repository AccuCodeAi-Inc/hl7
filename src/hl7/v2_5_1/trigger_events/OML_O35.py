from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.OML_O35_SPECIMEN_GROUP import OML_O35_SPECIMEN_GROUP
from ..segments.MSH import MSH
from ..segment_groups.OML_O35_PATIENT_GROUP import OML_O35_PATIENT_GROUP
from ..segments.NTE import NTE
from ..segments.SFT import SFT


"""
Laboratory Order for Multiple Orders Related to a Single Container of a Specimen - OML_O35
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::OML_O35 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O35
from utils.hl7.v2_5_1.segments import (
    SFT, NTE, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    OML_O35_SPECIMEN_GROUP, OML_O35_PATIENT_GROUP
)

oml_o35 = OML_O35(  #  - The trigger event for this message is any change to a laboratory order
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # OML_O35_PATIENT_GROUP(...) 
    specimen=oml_o35_specimen_group,  # OML_O35_SPECIMEN_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::OML_O35 TEMPLATE-----
"""


class OML_O35(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """OML_O35"""
    _hl7_name = """Laboratory Order for Multiple Orders Related to a Single Container of a Specimen"""
    _hl7_description = """The trigger event for this message is any change to a laboratory order"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "None", "None")
    _c_components = (MSH, SFT, NTE, OML_O35_PATIENT_GROUP, OML_O35_SPECIMEN_GROUP)
    _c_name = ("MSH", "SFT", "NTE", "PATIENT", "SPECIMEN")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "notes_and_comments", "patient", "specimen",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        specimen: OML_O35_SPECIMEN_GROUP
        | tuple[OML_O35_SPECIMEN_GROUP, ...],  #  Required. (SPM.15, OBX.16, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.3
        patient: OML_O35_PATIENT_GROUP
        | None = None,  #  PID.4, PD1.5, NTE.6, NK1.7, GT1.13, AL1.14
    ):
        """
                 - `OML_O35 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35>`_
                The trigger event for this message is any change to a laboratory order.  Such changes include submission of new orders, cancellations, updates, etc where multiple orders are associated with a single sample which may be carried in multiple containers.  OML messages can originate also with a placer, filler, or an interested third party.

        This allows for a Specimen-centric message with multiple orders per specimen grouped by the specimen.

        The following message structure may be used for the communication of laboratory and other order messages and must be used for lab automation messages where the message requires Specimen/container information to group a number of orders.  While the ORM message with the OBR segment can be used for backwards compatibility for general lab messages, only the OML message should be used to take advantage of the specimen and container extensions required in laboratory automation.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param notes_and_comments: Notes and Comments (id: NTE | seq: 3 | use: O | rpt: *)
                :param patient: Patient segment group: [PID, PD1|None, NTE|None, NK1|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None] (id: PATIENT | seq: 4, 5, 6, 7, None, None, 13, 14 | use: O | rpt: 1)
                :param specimen: Specimen segment group: [SPM, OBX|None, SPECIMEN CONTAINER] (id: SPECIMEN | seq: 15, 16, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.message_header = message_header
        self.software_segment = software_segment
        self.notes_and_comments = notes_and_comments
        self.patient = patient
        self.specimen = specimen

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

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 3
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 3
        ---
        param_type: NTE.3 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get OML_O35_PATIENT_GROUP.None
    def patient(self) -> OML_O35_PATIENT_GROUP | None:
        """
        id: OML_O35_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OML_O35_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_PATIENT_GROUP
        """
        return self._c_data[3][0]

    @patient.setter  # set OML_O35_PATIENT_GROUP.None
    def patient(self, patient: OML_O35_PATIENT_GROUP | None):
        """
        id: OML_O35_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OML_O35_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_PATIENT_GROUP
        """
        self._c_data[3] = (patient,)

    @property  # get SPECIMEN
    def specimen(self) -> tuple[OML_O35_SPECIMEN_GROUP, ...]:
        """
        id: OML_O35_SPECIMEN_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OML_O35_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP
        """
        return self._c_data[4]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self, specimen: OML_O35_SPECIMEN_GROUP | tuple[OML_O35_SPECIMEN_GROUP, ...]
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OML_O35_SPECIMEN_GROUP.None | tuple[OML_O35_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[4] = specimen
        else:
            self._c_data[4] = (specimen,)
