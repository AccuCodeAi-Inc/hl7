from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.IS import IS
from ..data_types.PPN import PPN
from ..data_types.XCN import XCN
from ..data_types.SI import SI
from ..data_types.ST import ST
from ..data_types.EI import EI
from ..tables.DocumentStorageStatus import DocumentStorageStatus
from ..tables.DocumentCompletionStatus import DocumentCompletionStatus
from ..tables.DocumentAvailabilityStatus import DocumentAvailabilityStatus
from ..tables.DocumentConfidentialityStatus import DocumentConfidentialityStatus
from ..tables.TypeOfReferencedData import TypeOfReferencedData
from ..tables.DocumentType import DocumentType


"""
Transcription Document Header - TXA
HL7 Version: 2.5.1

-----BEGIN SEGMENT::TXA TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    TXA,
    TS, ID, IS, PPN, XCN, SI, ST, EI
)

txa = TXA(  #  - The TXA segment contains information specific to a transcribed document but does not include the text of the document
    set_id_txa=si,  # SI(...)  # Required.
    document_type=_is,  # IS(...)  # Required.
    document_content_presentation=None,  # ID(...) 
    activity_date_or_time=None,  # TS(...) 
    primary_activity_provider_code_or_name=None,  # XCN(...) 
    origination_date_or_time=None,  # TS(...) 
    transcription_date_or_time=None,  # TS(...) 
    edit_date_or_time=None,  # TS(...) 
    originator_code_or_name=None,  # XCN(...) 
    assigned_document_authenticator=None,  # XCN(...) 
    transcriptionist_code_or_name=None,  # XCN(...) 
    unique_document_number=ei,  # EI(...)  # Required.
    parent_document_number=None,  # EI(...) 
    placer_order_number=None,  # EI(...) 
    filler_order_number=None,  # EI(...) 
    unique_document_file_name=None,  # ST(...) 
    document_completion_status=id,  # ID(...)  # Required.
    document_confidentiality_status=None,  # ID(...) 
    document_availability_status=None,  # ID(...) 
    document_storage_status=None,  # ID(...) 
    document_change_reason=None,  # ST(...) 
    authentication_person_time_stamp=None,  # PPN(...) 
    distributed_copies=None,  # XCN(...) 
)

-----END SEGMENT::TXA TEMPLATE-----
"""


class TXA(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """TXA"""
    _hl7_name = """Transcription Document Header"""
    _hl7_description = """The TXA segment contains information specific to a transcribed document but does not include the text of the document"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TXA"
    _c_length = (4, 30, 2, 26, 250, 26, 26, 26, 250, 250, 250, 30, 30, 22, 22, 30, 2, 2, 2, 2, 30, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 65535, 1, 1, 65535, 65535, 65535, 65535, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 65535, 65535,)
    _c_usage = ("R", "R", "C", "O", "C", "O", "C", "O", "O", "O", "C", "R", "C", "O", "O", "O", "R", "O", "O", "O", "C", "C", "O",)
    _c_components = (SI, IS, ID, TS, XCN, TS, TS, TS, XCN, XCN, XCN, EI, EI, EI, EI, ST, ID, ID, ID, ID, ST, PPN, XCN,)
    _c_aliases = ("TXA.1", "TXA.2", "TXA.3", "TXA.4", "TXA.5", "TXA.6", "TXA.7", "TXA.8", "TXA.9", "TXA.10", "TXA.11", "TXA.12", "TXA.13", "TXA.14", "TXA.15", "TXA.16", "TXA.17", "TXA.18", "TXA.19", "TXA.20", "TXA.21", "TXA.22", "TXA.23",)
    _c_names = ("Set ID - TXA", "Document Type", "Document Content Presentation", "Activity Date/Time", "Primary Activity Provider Code/Name", "Origination Date/Time", "Transcription Date/Time", "Edit Date/Time", "Originator Code/Name", "Assigned Document Authenticator", "Transcriptionist Code/Name", "Unique Document Number", "Parent Document Number", "Placer Order Number", "Filler Order Number", "Unique Document File Name", "Document Completion Status", "Document Confidentiality Status", "Document Availability Status", "Document Storage Status", "Document Change Reason", "Authentication Person, Time Stamp", "Distributed Copies (Code and Name of Recipients) ",)
    _c_attrs = ("set_id_txa", "document_type", "document_content_presentation", "activity_date_or_time", "primary_activity_provider_code_or_name", "origination_date_or_time", "transcription_date_or_time", "edit_date_or_time", "originator_code_or_name", "assigned_document_authenticator", "transcriptionist_code_or_name", "unique_document_number", "parent_document_number", "placer_order_number", "filler_order_number", "unique_document_file_name", "document_completion_status", "document_confidentiality_status", "document_availability_status", "document_storage_status", "document_change_reason", "authentication_person_time_stamp", "distributed_copies",)
    # fmt: on

    def __init__(
        self,
        set_id_txa: SI | tuple[SI],  # TXA.1
        document_type: DocumentType | IS | tuple[DocumentType | IS],  # TXA.2
        unique_document_number: EI | tuple[EI],  # TXA.12
        document_completion_status: DocumentCompletionStatus
        | ID
        | tuple[DocumentCompletionStatus | ID],  # TXA.17
        document_content_presentation: TypeOfReferencedData
        | ID
        | tuple[TypeOfReferencedData | ID]
        | None = None,  # TXA.3
        activity_date_or_time: TS | tuple[TS] | None = None,  # TXA.4
        primary_activity_provider_code_or_name: XCN | tuple[XCN] | None = None,  # TXA.5
        origination_date_or_time: TS | tuple[TS] | None = None,  # TXA.6
        transcription_date_or_time: TS | tuple[TS] | None = None,  # TXA.7
        edit_date_or_time: TS | tuple[TS] | None = None,  # TXA.8
        originator_code_or_name: XCN | tuple[XCN] | None = None,  # TXA.9
        assigned_document_authenticator: XCN | tuple[XCN] | None = None,  # TXA.10
        transcriptionist_code_or_name: XCN | tuple[XCN] | None = None,  # TXA.11
        parent_document_number: EI | tuple[EI] | None = None,  # TXA.13
        placer_order_number: EI | tuple[EI] | None = None,  # TXA.14
        filler_order_number: EI | tuple[EI] | None = None,  # TXA.15
        unique_document_file_name: ST | tuple[ST] | None = None,  # TXA.16
        document_confidentiality_status: DocumentConfidentialityStatus
        | ID
        | tuple[DocumentConfidentialityStatus | ID]
        | None = None,  # TXA.18
        document_availability_status: DocumentAvailabilityStatus
        | ID
        | tuple[DocumentAvailabilityStatus | ID]
        | None = None,  # TXA.19
        document_storage_status: DocumentStorageStatus
        | ID
        | tuple[DocumentStorageStatus | ID]
        | None = None,  # TXA.20
        document_change_reason: ST | tuple[ST] | None = None,  # TXA.21
        authentication_person_time_stamp: PPN | tuple[PPN] | None = None,  # TXA.22
        distributed_copies: XCN | tuple[XCN] | None = None,  # TXA.23
    ):
        """
        Transcription Document Header - `TXA <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TXA>`_
        The TXA segment contains information specific to a transcribed document but does not include the text of the document. The message is created as a result of a document status change. This information updates other healthcare systems and allows them to identify reports that are available in the transcription system. By maintaining the TXA message information in these systems, the information is available when constructing queries to the transcription system requesting the full document text.

        :param set_id_txa: Sequence ID (id: TXA.1 | len: 4 | use: R | rpt: 1)
        :param document_type: Coded value for user-defined tables (id: TXA.2 | len: 30 | use: R | rpt: 1)
        :param document_content_presentation: Coded values for HL7 tables (id: TXA.3 | len: 2 | use: C | rpt: 1)
        :param activity_date_or_time: Time Stamp (id: TXA.4 | len: 26 | use: O | rpt: 1)
        :param primary_activity_provider_code_or_name: Extended Composite ID Number and Name for Persons (id: TXA.5 | len: 250 | use: C | rpt: *)
        :param origination_date_or_time: Time Stamp (id: TXA.6 | len: 26 | use: O | rpt: 1)
        :param transcription_date_or_time: Time Stamp (id: TXA.7 | len: 26 | use: C | rpt: 1)
        :param edit_date_or_time: Time Stamp (id: TXA.8 | len: 26 | use: O | rpt: *)
        :param originator_code_or_name: Extended Composite ID Number and Name for Persons (id: TXA.9 | len: 250 | use: O | rpt: *)
        :param assigned_document_authenticator: Extended Composite ID Number and Name for Persons (id: TXA.10 | len: 250 | use: O | rpt: *)
        :param transcriptionist_code_or_name: Extended Composite ID Number and Name for Persons (id: TXA.11 | len: 250 | use: C | rpt: *)
        :param unique_document_number: Entity Identifier (id: TXA.12 | len: 30 | use: R | rpt: 1)
        :param parent_document_number: Entity Identifier (id: TXA.13 | len: 30 | use: C | rpt: 1)
        :param placer_order_number: Entity Identifier (id: TXA.14 | len: 22 | use: O | rpt: *)
        :param filler_order_number: Entity Identifier (id: TXA.15 | len: 22 | use: O | rpt: 1)
        :param unique_document_file_name: String Data (id: TXA.16 | len: 30 | use: O | rpt: 1)
        :param document_completion_status: Coded values for HL7 tables (id: TXA.17 | len: 2 | use: R | rpt: 1)
        :param document_confidentiality_status: Coded values for HL7 tables (id: TXA.18 | len: 2 | use: O | rpt: 1)
        :param document_availability_status: Coded values for HL7 tables (id: TXA.19 | len: 2 | use: O | rpt: 1)
        :param document_storage_status: Coded values for HL7 tables (id: TXA.20 | len: 2 | use: O | rpt: 1)
        :param document_change_reason: String Data (id: TXA.21 | len: 30 | use: C | rpt: 1)
        :param authentication_person_time_stamp: Performing Person Time Stamp (id: TXA.22 | len: 250 | use: C | rpt: *)
        :param distributed_copies: Extended Composite ID Number and Name for Persons (id: TXA.23 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 23
        self.set_id_txa = set_id_txa
        self.document_type = document_type
        self.document_content_presentation = document_content_presentation
        self.activity_date_or_time = activity_date_or_time
        self.primary_activity_provider_code_or_name = (
            primary_activity_provider_code_or_name
        )
        self.origination_date_or_time = origination_date_or_time
        self.transcription_date_or_time = transcription_date_or_time
        self.edit_date_or_time = edit_date_or_time
        self.originator_code_or_name = originator_code_or_name
        self.assigned_document_authenticator = assigned_document_authenticator
        self.transcriptionist_code_or_name = transcriptionist_code_or_name
        self.unique_document_number = unique_document_number
        self.parent_document_number = parent_document_number
        self.placer_order_number = placer_order_number
        self.filler_order_number = filler_order_number
        self.unique_document_file_name = unique_document_file_name
        self.document_completion_status = document_completion_status
        self.document_confidentiality_status = document_confidentiality_status
        self.document_availability_status = document_availability_status
        self.document_storage_status = document_storage_status
        self.document_change_reason = document_change_reason
        self.authentication_person_time_stamp = authentication_person_time_stamp
        self.distributed_copies = distributed_copies

    @property  # get TXA.1
    def set_id_txa(self) -> SI:
        """
        id: TXA.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.1
        """
        return self._c_data[0][0]

    @set_id_txa.setter  # set TXA.1
    def set_id_txa(self, si: SI):
        """
        id: TXA.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.1
        """
        self._c_data[0] = (si,)

    @property  # get TXA.2
    def document_type(self) -> DocumentType:
        """
        id: TXA.2 | len: 30 | use: R | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.2
        """
        return self._c_data[1][0]

    @document_type.setter  # set TXA.2
    def document_type(self, document_type: DocumentType):
        """
        id: TXA.2 | len: 30 | use: R | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.2
        """
        self._c_data[1] = (document_type,)

    @property  # get TXA.3
    def document_content_presentation(self) -> TypeOfReferencedData | None:
        """
        id: TXA.3 | len: 2 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.3
        """
        return self._c_data[2][0]

    @document_content_presentation.setter  # set TXA.3
    def document_content_presentation(
        self, type_of_referenced_data: TypeOfReferencedData | None
    ):
        """
        id: TXA.3 | len: 2 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.3
        """
        self._c_data[2] = (type_of_referenced_data,)

    @property  # get TXA.4
    def activity_date_or_time(self) -> TS | None:
        """
        id: TXA.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.4
        """
        return self._c_data[3][0]

    @activity_date_or_time.setter  # set TXA.4
    def activity_date_or_time(self, ts: TS | None):
        """
        id: TXA.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.4
        """
        self._c_data[3] = (ts,)

    @property
    def primary_activity_provider_code_or_name(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: TXA.5 | len: 250 | use: C | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.5
        """
        return self._c_data[4]

    @primary_activity_provider_code_or_name.setter  # set TXA.5
    def primary_activity_provider_code_or_name(self, xcn: XCN | tuple[XCN] | None):
        """
        id: TXA.5 | len: 250 | use: C | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.5
        """
        if isinstance(xcn, tuple):
            self._c_data[4] = xcn
        else:
            self._c_data[4] = (xcn,)

    @property  # get TXA.6
    def origination_date_or_time(self) -> TS | None:
        """
        id: TXA.6 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.6
        """
        return self._c_data[5][0]

    @origination_date_or_time.setter  # set TXA.6
    def origination_date_or_time(self, ts: TS | None):
        """
        id: TXA.6 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.6
        """
        self._c_data[5] = (ts,)

    @property  # get TXA.7
    def transcription_date_or_time(self) -> TS | None:
        """
        id: TXA.7 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.7
        """
        return self._c_data[6][0]

    @transcription_date_or_time.setter  # set TXA.7
    def transcription_date_or_time(self, ts: TS | None):
        """
        id: TXA.7 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.7
        """
        self._c_data[6] = (ts,)

    @property
    def edit_date_or_time(self) -> tuple[TS, ...] | tuple[None]:
        """
        id: TXA.8 | len: 26 | use: O | rpt: *
        ---
        return_type: tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.8
        """
        return self._c_data[7]

    @edit_date_or_time.setter  # set TXA.8
    def edit_date_or_time(self, ts: TS | tuple[TS] | None):
        """
        id: TXA.8 | len: 26 | use: O | rpt: *
        ---
        param_type: TS | tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.8
        """
        if isinstance(ts, tuple):
            self._c_data[7] = ts
        else:
            self._c_data[7] = (ts,)

    @property
    def originator_code_or_name(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: TXA.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.9
        """
        return self._c_data[8]

    @originator_code_or_name.setter  # set TXA.9
    def originator_code_or_name(self, xcn: XCN | tuple[XCN] | None):
        """
        id: TXA.9 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.9
        """
        if isinstance(xcn, tuple):
            self._c_data[8] = xcn
        else:
            self._c_data[8] = (xcn,)

    @property
    def assigned_document_authenticator(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: TXA.10 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.10
        """
        return self._c_data[9]

    @assigned_document_authenticator.setter  # set TXA.10
    def assigned_document_authenticator(self, xcn: XCN | tuple[XCN] | None):
        """
        id: TXA.10 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.10
        """
        if isinstance(xcn, tuple):
            self._c_data[9] = xcn
        else:
            self._c_data[9] = (xcn,)

    @property
    def transcriptionist_code_or_name(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: TXA.11 | len: 250 | use: C | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.11
        """
        return self._c_data[10]

    @transcriptionist_code_or_name.setter  # set TXA.11
    def transcriptionist_code_or_name(self, xcn: XCN | tuple[XCN] | None):
        """
        id: TXA.11 | len: 250 | use: C | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.11
        """
        if isinstance(xcn, tuple):
            self._c_data[10] = xcn
        else:
            self._c_data[10] = (xcn,)

    @property  # get TXA.12
    def unique_document_number(self) -> EI:
        """
        id: TXA.12 | len: 30 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.12
        """
        return self._c_data[11][0]

    @unique_document_number.setter  # set TXA.12
    def unique_document_number(self, ei: EI):
        """
        id: TXA.12 | len: 30 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.12
        """
        self._c_data[11] = (ei,)

    @property  # get TXA.13
    def parent_document_number(self) -> EI | None:
        """
        id: TXA.13 | len: 30 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.13
        """
        return self._c_data[12][0]

    @parent_document_number.setter  # set TXA.13
    def parent_document_number(self, ei: EI | None):
        """
        id: TXA.13 | len: 30 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.13
        """
        self._c_data[12] = (ei,)

    @property
    def placer_order_number(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: TXA.14 | len: 22 | use: O | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.14
        """
        return self._c_data[13]

    @placer_order_number.setter  # set TXA.14
    def placer_order_number(self, ei: EI | tuple[EI] | None):
        """
        id: TXA.14 | len: 22 | use: O | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.14
        """
        if isinstance(ei, tuple):
            self._c_data[13] = ei
        else:
            self._c_data[13] = (ei,)

    @property  # get TXA.15
    def filler_order_number(self) -> EI | None:
        """
        id: TXA.15 | len: 22 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.15
        """
        return self._c_data[14][0]

    @filler_order_number.setter  # set TXA.15
    def filler_order_number(self, ei: EI | None):
        """
        id: TXA.15 | len: 22 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.15
        """
        self._c_data[14] = (ei,)

    @property  # get TXA.16
    def unique_document_file_name(self) -> ST | None:
        """
        id: TXA.16 | len: 30 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.16
        """
        return self._c_data[15][0]

    @unique_document_file_name.setter  # set TXA.16
    def unique_document_file_name(self, st: ST | None):
        """
        id: TXA.16 | len: 30 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.16
        """
        self._c_data[15] = (st,)

    @property  # get TXA.17
    def document_completion_status(self) -> DocumentCompletionStatus:
        """
        id: TXA.17 | len: 2 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.17
        """
        return self._c_data[16][0]

    @document_completion_status.setter  # set TXA.17
    def document_completion_status(
        self, document_completion_status: DocumentCompletionStatus
    ):
        """
        id: TXA.17 | len: 2 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.17
        """
        self._c_data[16] = (document_completion_status,)

    @property  # get TXA.18
    def document_confidentiality_status(self) -> DocumentConfidentialityStatus | None:
        """
        id: TXA.18 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.18
        """
        return self._c_data[17][0]

    @document_confidentiality_status.setter  # set TXA.18
    def document_confidentiality_status(
        self, document_confidentiality_status: DocumentConfidentialityStatus | None
    ):
        """
        id: TXA.18 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.18
        """
        self._c_data[17] = (document_confidentiality_status,)

    @property  # get TXA.19
    def document_availability_status(self) -> DocumentAvailabilityStatus | None:
        """
        id: TXA.19 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.19
        """
        return self._c_data[18][0]

    @document_availability_status.setter  # set TXA.19
    def document_availability_status(
        self, document_availability_status: DocumentAvailabilityStatus | None
    ):
        """
        id: TXA.19 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.19
        """
        self._c_data[18] = (document_availability_status,)

    @property  # get TXA.20
    def document_storage_status(self) -> DocumentStorageStatus | None:
        """
        id: TXA.20 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.20
        """
        return self._c_data[19][0]

    @document_storage_status.setter  # set TXA.20
    def document_storage_status(
        self, document_storage_status: DocumentStorageStatus | None
    ):
        """
        id: TXA.20 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.20
        """
        self._c_data[19] = (document_storage_status,)

    @property  # get TXA.21
    def document_change_reason(self) -> ST | None:
        """
        id: TXA.21 | len: 30 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.21
        """
        return self._c_data[20][0]

    @document_change_reason.setter  # set TXA.21
    def document_change_reason(self, st: ST | None):
        """
        id: TXA.21 | len: 30 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.21
        """
        self._c_data[20] = (st,)

    @property
    def authentication_person_time_stamp(self) -> tuple[PPN, ...] | tuple[None]:
        """
        id: TXA.22 | len: 250 | use: C | rpt: *
        ---
        return_type: tuple[PPN, ...]: (Performing Person Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.22
        """
        return self._c_data[21]

    @authentication_person_time_stamp.setter  # set TXA.22
    def authentication_person_time_stamp(self, ppn: PPN | tuple[PPN] | None):
        """
        id: TXA.22 | len: 250 | use: C | rpt: *
        ---
        param_type: PPN | tuple[PPN, ...]: (Performing Person Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.22
        """
        if isinstance(ppn, tuple):
            self._c_data[21] = ppn
        else:
            self._c_data[21] = (ppn,)

    @property
    def distributed_copies(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: TXA.23 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.23
        """
        return self._c_data[22]

    @distributed_copies.setter  # set TXA.23
    def distributed_copies(self, xcn: XCN | tuple[XCN] | None):
        """
        id: TXA.23 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TXA.23
        """
        if isinstance(xcn, tuple):
            self._c_data[22] = xcn
        else:
            self._c_data[22] = (xcn,)
