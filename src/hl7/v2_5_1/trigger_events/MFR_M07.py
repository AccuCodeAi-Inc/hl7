from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.ERR import ERR
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.MSA import MSA
from ..segments.QAK import QAK
from ..segments.QRF import QRF
from ..segments.MFI import MFI
from ..segment_groups.MFR_M07_MF_QUERY_GROUP import MFR_M07_MF_QUERY_GROUP
from ..segments.DSC import DSC
from ..segments.SFT import SFT


"""
Master Files Response - Clinical study without phases but with schedules master file - MFR_M07
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::MFR_M07 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFR_M07
from utils.hl7.v2_5_1.segments import (
    QAK, QRD, MFI, SFT, QRF, ERR, MSA, DSC, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    MFR_M07_MF_QUERY_GROUP
)

mfr_m07 = MFR_M07(  #  - The MFQ/MFR transaction allows a system to query for a particular record or group records (defined by the primary key) in a particular master file
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=None,  # QAK(...) 
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
    master_file_identification=mfi,  # MFI(...)  # Required.
    mf_query=mfr_m07_mf_query_group,  # MFR_M07_MF_QUERY_GROUP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::MFR_M07 TEMPLATE-----
"""


class MFR_M07(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """MFR_M07"""
    _hl7_name = """Master Files Response - Clinical study without phases but with schedules master file"""
    _hl7_description = """The MFQ/MFR transaction allows a system to query for a particular record or group records (defined by the primary key) in a particular master file"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFR_M07"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 1, 1, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "O", "R", "O", "R", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8", "None", "12")
    _c_components = (MSH, SFT, MSA, ERR, QAK, QRD, QRF, MFI, MFR_M07_MF_QUERY_GROUP, DSC)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "QAK", "QRD", "QRF", "MFI", "MF QUERY", "DSC")
    _c_is_group = (False, False, False, False, False, False, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "query_acknowledgment", "original_style_query_definition", "original_style_query_filter", "master_file_identification", "mf_query", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        original_style_query_definition: QRD,  #  Required. QRD.6
        master_file_identification: MFI,  #  Required. MFI.8
        mf_query: MFR_M07_MF_QUERY_GROUP
        | tuple[MFR_M07_MF_QUERY_GROUP, ...],  #  Required. (MFE.9, CM0.10, CM2.11, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.4
        query_acknowledgment: QAK | None = None,  #  QAK.5
        original_style_query_filter: QRF | None = None,  #  QRF.7
        continuation_pointer: DSC | None = None,  #  DSC.12
    ):
        """
         - `MFR_M07 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFR_M07>`_
        The MFQ/MFR transaction allows a system to query for a particular record or group records (defined by the primary key) in a particular master file.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: *)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 5 | use: O | rpt: 1)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 6 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 7 | use: O | rpt: 1)
        :param master_file_identification: Master File Identification (id: MFI | seq: 8 | use: R | rpt: 1)
        :param mf_query: Mf Query segment group: [MFE, CM0, CM2|None] (id: MF QUERY | seq: 9, 10, 11 | use: R | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 12 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.query_acknowledgment = query_acknowledgment
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter
        self.master_file_identification = master_file_identification
        self.mf_query = mf_query
        self.continuation_pointer = continuation_pointer

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

    @property  # get ERR
    def error(self) -> tuple[ERR, ...] | tuple[None]:
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        return_type: tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        return self._c_data[3]

    @error.setter  # set ERR
    def error(self, err: ERR | tuple[ERR, ...] | None):
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        param_type: ERR.4 | tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        if isinstance(err, tuple):
            self._c_data[3] = err
        else:
            self._c_data[3] = (err,)

    @property  # get QAK.5
    def query_acknowledgment(self) -> QAK | None:
        """
        id: QAK | use: O | rpt: 1 | seq: 5
        ---
        return_type: QAK.5: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        return self._c_data[4][0]

    @query_acknowledgment.setter  # set QAK.5
    def query_acknowledgment(self, qak: QAK | None):
        """
        id: QAK | use: O | rpt: 1 | seq: 5
        ---
        param_type: QAK.5: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        self._c_data[4] = (qak,)

    @property  # get QRD.6
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 6
        ---
        return_type: QRD.6: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[5][0]

    @original_style_query_definition.setter  # set QRD.6
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 6
        ---
        param_type: QRD.6: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[5] = (qrd,)

    @property  # get QRF.7
    def original_style_query_filter(self) -> QRF | None:
        """
        id: QRF | use: O | rpt: 1 | seq: 7
        ---
        return_type: QRF.7: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        return self._c_data[6][0]

    @original_style_query_filter.setter  # set QRF.7
    def original_style_query_filter(self, qrf: QRF | None):
        """
        id: QRF | use: O | rpt: 1 | seq: 7
        ---
        param_type: QRF.7: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        self._c_data[6] = (qrf,)

    @property  # get MFI.8
    def master_file_identification(self) -> MFI:
        """
        id: MFI | use: R | rpt: 1 | seq: 8
        ---
        return_type: MFI.8: Master File Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI
        """
        return self._c_data[7][0]

    @master_file_identification.setter  # set MFI.8
    def master_file_identification(self, mfi: MFI):
        """
        id: MFI | use: R | rpt: 1 | seq: 8
        ---
        param_type: MFI.8: Master File Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI
        """
        self._c_data[7] = (mfi,)

    @property  # get MF QUERY
    def mf_query(self) -> tuple[MFR_M07_MF_QUERY_GROUP, ...]:
        """
        id: MFR_M07_MF_QUERY_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[MFR_M07_MF_QUERY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFR_M07_MF_QUERY_GROUP
        """
        return self._c_data[8]

    @mf_query.setter  # set MF QUERY
    def mf_query(
        self, mf_query: MFR_M07_MF_QUERY_GROUP | tuple[MFR_M07_MF_QUERY_GROUP, ...]
    ):
        """
        id: MF QUERY SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: MFR_M07_MF_QUERY_GROUP.None | tuple[MFR_M07_MF_QUERY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFR_M07_MF_QUERY_GROUP
        """
        if isinstance(mf_query, tuple):
            self._c_data[8] = mf_query
        else:
            self._c_data[8] = (mf_query,)

    @property  # get DSC.12
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 12
        ---
        return_type: DSC.12: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[9][0]

    @continuation_pointer.setter  # set DSC.12
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 12
        ---
        param_type: DSC.12: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[9] = (dsc,)
