from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.PT import PT
from ..data_types.ST import ST
from ..data_types.VID import VID
from ..data_types.MSG import MSG
from ..data_types.EI import EI
from ..data_types.HD import HD
from ..data_types.TS import TS
from ..tables.CountryCode import CountryCode
from ..tables.AlternateCharacterSetHandlingScheme import (
    AlternateCharacterSetHandlingScheme,
)
from ..tables.AlternateCharacterSets import AlternateCharacterSets
from ..tables.Facility import Facility
from ..tables.Application import Application
from ..tables.AcceptOrApplicationAcknowledgmentConditions import (
    AcceptOrApplicationAcknowledgmentConditions,
)


"""
Message Header - MSH
HL7 Version: 2.5.1

-----BEGIN SEGMENT::MSH TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MSH,
    CE, ID, NM, PT, ST, VID, MSG, EI, HD, TS
)

msh = MSH(  #  - The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message
    field_separator=st,  # ST(...)  # Required.
    encoding_characters=st,  # ST(...)  # Required.
    sending_application=None,  # HD(...) 
    sending_facility=None,  # HD(...) 
    receiving_application=None,  # HD(...) 
    receiving_facility=None,  # HD(...) 
    date_or_time_of_message=ts,  # TS(...)  # Required.
    security=None,  # ST(...) 
    message_type=msg,  # MSG(...)  # Required.
    message_control_id=st,  # ST(...)  # Required.
    processing_id=pt,  # PT(...)  # Required.
    version_id=vid,  # VID(...)  # Required.
    sequence_number=None,  # NM(...) 
    continuation_pointer=None,  # ST(...) 
    accept_acknowledgment_type=None,  # ID(...) 
    application_acknowledgment_type=None,  # ID(...) 
    country_code=None,  # ID(...) 
    character_set=None,  # ID(...) 
    principal_language_of_message=None,  # CE(...) 
    alternate_character_set_handling_scheme=None,  # ID(...) 
    message_profile_identifier=None,  # EI(...) 
)

-----END SEGMENT::MSH TEMPLATE-----
"""


class MSH(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """MSH"""
    _hl7_name = """Message Header"""
    _hl7_description = """The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH"
    _c_length = (1, 4, 227, 227, 227, 227, 26, 40, 15, 20, 3, 60, 15, 180, 2, 2, 3, 16, 250, 20, 427,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 65535,)
    _c_usage = ("R", "R", "O", "O", "O", "O", "R", "O", "R", "R", "R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (ST, ST, HD, HD, HD, HD, TS, ST, MSG, ST, PT, VID, NM, ST, ID, ID, ID, ID, CE, ID, EI,)
    _c_aliases = ("MSH.1", "MSH.2", "MSH.3", "MSH.4", "MSH.5", "MSH.6", "MSH.7", "MSH.8", "MSH.9", "MSH.10", "MSH.11", "MSH.12", "MSH.13", "MSH.14", "MSH.15", "MSH.16", "MSH.17", "MSH.18", "MSH.19", "MSH.20", "MSH.21",)
    _c_names = ("Field Separator", "Encoding Characters", "Sending Application", "Sending Facility", "Receiving Application", "Receiving Facility", "Date/Time Of Message", "Security", "Message Type", "Message Control ID", "Processing ID", "Version ID", "Sequence Number", "Continuation Pointer", "Accept Acknowledgment Type", "Application Acknowledgment Type", "Country Code", "Character Set", "Principal Language Of Message", "Alternate Character Set Handling Scheme", "Message Profile Identifier",)
    _c_attrs = ("field_separator", "encoding_characters", "sending_application", "sending_facility", "receiving_application", "receiving_facility", "date_or_time_of_message", "security", "message_type", "message_control_id", "processing_id", "version_id", "sequence_number", "continuation_pointer", "accept_acknowledgment_type", "application_acknowledgment_type", "country_code", "character_set", "principal_language_of_message", "alternate_character_set_handling_scheme", "message_profile_identifier",)
    # fmt: on

    def __init__(
        self,
        date_or_time_of_message: TS,  # MSH.7
        message_type: MSG,  # MSH.9
        message_control_id: ST,  # MSH.10
        processing_id: PT,  # MSH.11
        version_id: VID,  # MSH.12
        field_separator: ST = ST("|"),  # MSH.1
        encoding_characters: ST = ST("^~\\&"),  # MSH.2
        sending_application: Application | HD | None = None,  # MSH.3
        sending_facility: Facility | HD | None = None,  # MSH.4
        receiving_application: Application | HD | None = None,  # MSH.5
        receiving_facility: Facility | HD | None = None,  # MSH.6
        security: ST | None = None,  # MSH.8
        sequence_number: NM | None = None,  # MSH.13
        continuation_pointer: ST | None = None,  # MSH.14
        accept_acknowledgment_type: AcceptOrApplicationAcknowledgmentConditions
        | ID
        | None = None,  # MSH.15
        application_acknowledgment_type: AcceptOrApplicationAcknowledgmentConditions
        | ID
        | None = None,  # MSH.16
        country_code: CountryCode | ID | None = None,  # MSH.17
        character_set: AlternateCharacterSets | ID | None = None,  # MSH.18
        principal_language_of_message: CE | None = None,  # MSH.19
        alternate_character_set_handling_scheme: AlternateCharacterSetHandlingScheme
        | ID
        | None = None,  # MSH.20
        message_profile_identifier: EI | None = None,  # MSH.21
    ):
        """
        Message Header - `MSH <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH>`_
        The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message.

        :param field_separator: String Data (id: MSH.1 | len: 1 | use: R | rpt: 1)
        :param encoding_characters: String Data (id: MSH.2 | len: 4 | use: R | rpt: 1)
        :param sending_application: Hierarchic Designator (id: MSH.3 | len: 227 | use: O | rpt: 1)
        :param sending_facility: Hierarchic Designator (id: MSH.4 | len: 227 | use: O | rpt: 1)
        :param receiving_application: Hierarchic Designator (id: MSH.5 | len: 227 | use: O | rpt: 1)
        :param receiving_facility: Hierarchic Designator (id: MSH.6 | len: 227 | use: O | rpt: 1)
        :param date_or_time_of_message: Time Stamp (id: MSH.7 | len: 26 | use: R | rpt: 1)
        :param security: String Data (id: MSH.8 | len: 40 | use: O | rpt: 1)
        :param message_type: Message Type (id: MSH.9 | len: 15 | use: R | rpt: 1)
        :param message_control_id: String Data (id: MSH.10 | len: 20 | use: R | rpt: 1)
        :param processing_id: Processing Type (id: MSH.11 | len: 3 | use: R | rpt: 1)
        :param version_id: Version Identifier (id: MSH.12 | len: 60 | use: R | rpt: 1)
        :param sequence_number: Numeric (id: MSH.13 | len: 15 | use: O | rpt: 1)
        :param continuation_pointer: String Data (id: MSH.14 | len: 180 | use: O | rpt: 1)
        :param accept_acknowledgment_type: Coded values for HL7 tables (id: MSH.15 | len: 2 | use: O | rpt: 1)
        :param application_acknowledgment_type: Coded values for HL7 tables (id: MSH.16 | len: 2 | use: O | rpt: 1)
        :param country_code: Coded values for HL7 tables (id: MSH.17 | len: 3 | use: O | rpt: 1)
        :param character_set: Coded values for HL7 tables (id: MSH.18 | len: 16 | use: O | rpt: *)
        :param principal_language_of_message: Coded Element (id: MSH.19 | len: 250 | use: O | rpt: 1)
        :param alternate_character_set_handling_scheme: Coded values for HL7 tables (id: MSH.20 | len: 20 | use: O | rpt: 1)
        :param message_profile_identifier: Entity Identifier (id: MSH.21 | len: 427 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 21
        self.field_separator = field_separator
        self.encoding_characters = encoding_characters
        self.sending_application = sending_application
        self.sending_facility = sending_facility
        self.receiving_application = receiving_application
        self.receiving_facility = receiving_facility
        self.date_or_time_of_message = date_or_time_of_message
        self.security = security
        self.message_type = message_type
        self.message_control_id = message_control_id
        self.processing_id = processing_id
        self.version_id = version_id
        self.sequence_number = sequence_number
        self.continuation_pointer = continuation_pointer
        self.accept_acknowledgment_type = accept_acknowledgment_type
        self.application_acknowledgment_type = application_acknowledgment_type
        self.country_code = country_code
        self.character_set = character_set
        self.principal_language_of_message = principal_language_of_message
        self.alternate_character_set_handling_scheme = (
            alternate_character_set_handling_scheme
        )
        self.message_profile_identifier = message_profile_identifier

    @property  # get MSH.1
    def field_separator(self) -> ST:
        """
        id: MSH.1 | len: 1 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.1
        """
        return self._c_data[0][0]

    @field_separator.setter  # set MSH.1
    def field_separator(self, st: ST):
        """
        id: MSH.1 | len: 1 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.1
        """
        self._c_data[0] = (st,)

    @property  # get MSH.2
    def encoding_characters(self) -> ST:
        """
        id: MSH.2 | len: 4 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.2
        """
        return self._c_data[1][0]

    @encoding_characters.setter  # set MSH.2
    def encoding_characters(self, st: ST):
        """
        id: MSH.2 | len: 4 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.2
        """
        self._c_data[1] = (st,)

    @property  # get MSH.3
    def sending_application(self) -> Application | None:
        """
        id: MSH.3 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.3
        """
        return self._c_data[2][0]

    @sending_application.setter  # set MSH.3
    def sending_application(self, application: Application | None):
        """
        id: MSH.3 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.3
        """
        self._c_data[2] = (application,)

    @property  # get MSH.4
    def sending_facility(self) -> Facility | None:
        """
        id: MSH.4 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.4
        """
        return self._c_data[3][0]

    @sending_facility.setter  # set MSH.4
    def sending_facility(self, facility: Facility | None):
        """
        id: MSH.4 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.4
        """
        self._c_data[3] = (facility,)

    @property  # get MSH.5
    def receiving_application(self) -> Application | None:
        """
        id: MSH.5 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.5
        """
        return self._c_data[4][0]

    @receiving_application.setter  # set MSH.5
    def receiving_application(self, application: Application | None):
        """
        id: MSH.5 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.5
        """
        self._c_data[4] = (application,)

    @property  # get MSH.6
    def receiving_facility(self) -> Facility | None:
        """
        id: MSH.6 | len: 227 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.6
        """
        return self._c_data[5][0]

    @receiving_facility.setter  # set MSH.6
    def receiving_facility(self, facility: Facility | None):
        """
        id: MSH.6 | len: 227 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.6
        """
        self._c_data[5] = (facility,)

    @property  # get MSH.7
    def date_or_time_of_message(self) -> TS:
        """
        id: MSH.7 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.7
        """
        return self._c_data[6][0]

    @date_or_time_of_message.setter  # set MSH.7
    def date_or_time_of_message(self, ts: TS):
        """
        id: MSH.7 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.7
        """
        self._c_data[6] = (ts,)

    @property  # get MSH.8
    def security(self) -> ST | None:
        """
        id: MSH.8 | len: 40 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.8
        """
        return self._c_data[7][0]

    @security.setter  # set MSH.8
    def security(self, st: ST | None):
        """
        id: MSH.8 | len: 40 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.8
        """
        self._c_data[7] = (st,)

    @property  # get MSH.9
    def message_type(self) -> MSG:
        """
        id: MSH.9 | len: 15 | use: R | rpt: 1
        ---
        return_type: MSG: Message Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.9
        """
        return self._c_data[8][0]

    @message_type.setter  # set MSH.9
    def message_type(self, msg: MSG):
        """
        id: MSH.9 | len: 15 | use: R | rpt: 1
        ---
        param_type: MSG: Message Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.9
        """
        self._c_data[8] = (msg,)

    @property  # get MSH.10
    def message_control_id(self) -> ST:
        """
        id: MSH.10 | len: 20 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.10
        """
        return self._c_data[9][0]

    @message_control_id.setter  # set MSH.10
    def message_control_id(self, st: ST):
        """
        id: MSH.10 | len: 20 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.10
        """
        self._c_data[9] = (st,)

    @property  # get MSH.11
    def processing_id(self) -> PT:
        """
        id: MSH.11 | len: 3 | use: R | rpt: 1
        ---
        return_type: PT: Processing Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.11
        """
        return self._c_data[10][0]

    @processing_id.setter  # set MSH.11
    def processing_id(self, pt: PT):
        """
        id: MSH.11 | len: 3 | use: R | rpt: 1
        ---
        param_type: PT: Processing Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.11
        """
        self._c_data[10] = (pt,)

    @property  # get MSH.12
    def version_id(self) -> VID:
        """
        id: MSH.12 | len: 60 | use: R | rpt: 1
        ---
        return_type: VID: Version Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.12
        """
        return self._c_data[11][0]

    @version_id.setter  # set MSH.12
    def version_id(self, vid: VID):
        """
        id: MSH.12 | len: 60 | use: R | rpt: 1
        ---
        param_type: VID: Version Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.12
        """
        self._c_data[11] = (vid,)

    @property  # get MSH.13
    def sequence_number(self) -> NM | None:
        """
        id: MSH.13 | len: 15 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.13
        """
        return self._c_data[12][0]

    @sequence_number.setter  # set MSH.13
    def sequence_number(self, nm: NM | None):
        """
        id: MSH.13 | len: 15 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.13
        """
        self._c_data[12] = (nm,)

    @property  # get MSH.14
    def continuation_pointer(self) -> ST | None:
        """
        id: MSH.14 | len: 180 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.14
        """
        return self._c_data[13][0]

    @continuation_pointer.setter  # set MSH.14
    def continuation_pointer(self, st: ST | None):
        """
        id: MSH.14 | len: 180 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.14
        """
        self._c_data[13] = (st,)

    @property  # get MSH.15
    def accept_acknowledgment_type(
        self,
    ) -> AcceptOrApplicationAcknowledgmentConditions | None:
        """
        id: MSH.15 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.15
        """
        return self._c_data[14][0]

    @accept_acknowledgment_type.setter  # set MSH.15
    def accept_acknowledgment_type(
        self,
        accept_or_application_acknowledgment_conditions: AcceptOrApplicationAcknowledgmentConditions
        | None,
    ):
        """
        id: MSH.15 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.15
        """
        self._c_data[14] = (accept_or_application_acknowledgment_conditions,)

    @property  # get MSH.16
    def application_acknowledgment_type(
        self,
    ) -> AcceptOrApplicationAcknowledgmentConditions | None:
        """
        id: MSH.16 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.16
        """
        return self._c_data[15][0]

    @application_acknowledgment_type.setter  # set MSH.16
    def application_acknowledgment_type(
        self,
        accept_or_application_acknowledgment_conditions: AcceptOrApplicationAcknowledgmentConditions
        | None,
    ):
        """
        id: MSH.16 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.16
        """
        self._c_data[15] = (accept_or_application_acknowledgment_conditions,)

    @property  # get MSH.17
    def country_code(self) -> CountryCode | None:
        """
        id: MSH.17 | len: 3 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.17
        """
        return self._c_data[16][0]

    @country_code.setter  # set MSH.17
    def country_code(self, country_code: CountryCode | None):
        """
        id: MSH.17 | len: 3 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.17
        """
        self._c_data[16] = (country_code,)

    @property
    def character_set(self) -> tuple[AlternateCharacterSets, ...] | tuple[None]:
        """
        id: MSH.18 | len: 16 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.18
        """
        return self._c_data[17]

    @character_set.setter  # set MSH.18
    def character_set(
        self,
        alternate_character_sets: AlternateCharacterSets
        | tuple[AlternateCharacterSets]
        | None,
    ):
        """
        id: MSH.18 | len: 16 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.18
        """
        if isinstance(alternate_character_sets, tuple):
            self._c_data[17] = alternate_character_sets
        else:
            self._c_data[17] = (alternate_character_sets,)

    @property  # get MSH.19
    def principal_language_of_message(self) -> CE | None:
        """
        id: MSH.19 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.19
        """
        return self._c_data[18][0]

    @principal_language_of_message.setter  # set MSH.19
    def principal_language_of_message(self, ce: CE | None):
        """
        id: MSH.19 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.19
        """
        self._c_data[18] = (ce,)

    @property  # get MSH.20
    def alternate_character_set_handling_scheme(
        self,
    ) -> AlternateCharacterSetHandlingScheme | None:
        """
        id: MSH.20 | len: 20 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.20
        """
        return self._c_data[19][0]

    @alternate_character_set_handling_scheme.setter  # set MSH.20
    def alternate_character_set_handling_scheme(
        self,
        alternate_character_set_handling_scheme: AlternateCharacterSetHandlingScheme
        | None,
    ):
        """
        id: MSH.20 | len: 20 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.20
        """
        self._c_data[19] = (alternate_character_set_handling_scheme,)

    @property
    def message_profile_identifier(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: MSH.21 | len: 427 | use: O | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.21
        """
        return self._c_data[20]

    @message_profile_identifier.setter  # set MSH.21
    def message_profile_identifier(self, ei: EI | tuple[EI] | None):
        """
        id: MSH.21 | len: 427 | use: O | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MSH.21
        """
        if isinstance(ei, tuple):
            self._c_data[20] = ei
        else:
            self._c_data[20] = (ei,)
