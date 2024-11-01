from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.CNE import CNE
from ..data_types.TS import TS
from ..data_types.IS import IS
from ..data_types.CWE import CWE
from ..data_types.ST import ST
from ..data_types.XPN import XPN
from ..data_types.ID import ID
from ..data_types.EI import EI
from ..data_types.FT import FT
from ..tables.ConsentDisclosureLevel import ConsentDisclosureLevel
from ..tables.PrimaryLanguage import PrimaryLanguage
from ..tables.NonSubjectConsenterReason import NonSubjectConsenterReason
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.ConsentBypassReason import ConsentBypassReason
from ..tables.ConsentMode import ConsentMode
from ..tables.ConsentNonDisclosureReason import ConsentNonDisclosureReason
from ..tables.ConsentType import ConsentType
from ..tables.ConsentStatus import ConsentStatus
from ..tables.SignatorySRelationshipToSubject import SignatorySRelationshipToSubject


"""
Consent - CON
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CON TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CON,
    SI, CNE, TS, IS, CWE, ST, XPN, ID, EI, FT
)

con = CON(  #  - The consent segment provides details about a specific consent by a patient or staff member
    set_id_con=si,  # SI(...)  # Required.
    consent_type=None,  # CWE(...) 
    consent_form_id=None,  # ST(...) 
    consent_form_number=None,  # EI(...) 
    consent_text=None,  # FT(...) 
    subject_specific_consent_text=None,  # FT(...) 
    consent_background=None,  # FT(...) 
    subject_specific_consent_background=None,  # FT(...) 
    consenter_imposed_limitations=None,  # FT(...) 
    consent_mode=None,  # CNE(...) 
    consent_status=cne,  # CNE(...)  # Required.
    consent_discussion_date_or_time=None,  # TS(...) 
    consent_decision_date_or_time=None,  # TS(...) 
    consent_effective_date_or_time=None,  # TS(...) 
    consent_end_date_or_time=None,  # TS(...) 
    subject_competence_indicator=None,  # ID(...) 
    translator_assistance_indicator=None,  # ID(...) 
    language_translated_to=None,  # ID(...) 
    informational_material_supplied_indicator=None,  # ID(...) 
    consent_bypass_reason=None,  # CWE(...) 
    consent_disclosure_level=None,  # ID(...) 
    consent_non_disclosure_reason=None,  # CWE(...) 
    non_subject_consenter_reason=None,  # CWE(...) 
    consenter_id=xpn,  # XPN(...)  # Required.
    relationship_to_subject_table=_is,  # IS(...)  # Required.
)

-----END SEGMENT::CON TEMPLATE-----
"""


class CON(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CON"""
    _hl7_name = """Consent"""
    _hl7_description = """The consent segment provides details about a specific consent by a patient or staff member"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CON"
    _c_length = (4, 250, 40, 180, 65536, 65536, 65536, 65536, 65536, 2, 2, 26, 26, 26, 26, 1, 1, 1, 1, 250, 1, 250, 250, 250, 100,)
    _c_rpt = (1, 1, 1, 1, 65535, 65535, 65535, 65535, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 65535,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "R", "R",)
    _c_components = (SI, CWE, ST, EI, FT, FT, FT, FT, FT, CNE, CNE, TS, TS, TS, TS, ID, ID, ID, ID, CWE, ID, CWE, CWE, XPN, IS,)
    _c_aliases = ("CON.1", "CON.2", "CON.3", "CON.4", "CON.5", "CON.6", "CON.7", "CON.8", "CON.9", "CON.10", "CON.11", "CON.12", "CON.13", "CON.14", "CON.15", "CON.16", "CON.17", "CON.18", "CON.19", "CON.20", "CON.21", "CON.22", "CON.23", "CON.24", "CON.25",)
    _c_names = ("Set ID - CON", "Consent Type", "Consent Form ID", "Consent Form Number", "Consent Text", "Subject-specific Consent Text", "Consent Background", "Subject-specific Consent Background", "Consenter-imposed limitations", "Consent Mode", "Consent Status", "Consent Discussion Date/Time", "Consent Decision Date/Time", "Consent Effective Date/Time", "Consent End Date/Time", "Subject Competence Indicator", "Translator Assistance Indicator", "Language Translated To", "Informational Material Supplied Indicator", "Consent Bypass Reason", "Consent Disclosure Level", "Consent Non-disclosure Reason", "Non-subject Consenter Reason", "Consenter ID", "Relationship to Subject Table",)
    _c_attrs = ("set_id_con", "consent_type", "consent_form_id", "consent_form_number", "consent_text", "subject_specific_consent_text", "consent_background", "subject_specific_consent_background", "consenter_imposed_limitations", "consent_mode", "consent_status", "consent_discussion_date_or_time", "consent_decision_date_or_time", "consent_effective_date_or_time", "consent_end_date_or_time", "subject_competence_indicator", "translator_assistance_indicator", "language_translated_to", "informational_material_supplied_indicator", "consent_bypass_reason", "consent_disclosure_level", "consent_non_disclosure_reason", "non_subject_consenter_reason", "consenter_id", "relationship_to_subject_table",)
    # fmt: on

    def __init__(
        self,
        set_id_con: SI | tuple[SI, ...],  # CON.1
        consent_status: ConsentStatus | CNE | tuple[ConsentStatus | CNE, ...],  # CON.11
        consenter_id: XPN | tuple[XPN, ...],  # CON.24
        relationship_to_subject_table: SignatorySRelationshipToSubject
        | IS
        | tuple[SignatorySRelationshipToSubject | IS, ...],  # CON.25
        consent_type: ConsentType
        | CWE
        | tuple[ConsentType | CWE, ...]
        | None = None,  # CON.2
        consent_form_id: ST | tuple[ST, ...] | None = None,  # CON.3
        consent_form_number: EI | tuple[EI, ...] | None = None,  # CON.4
        consent_text: FT | tuple[FT, ...] | None = None,  # CON.5
        subject_specific_consent_text: FT | tuple[FT, ...] | None = None,  # CON.6
        consent_background: FT | tuple[FT, ...] | None = None,  # CON.7
        subject_specific_consent_background: FT | tuple[FT, ...] | None = None,  # CON.8
        consenter_imposed_limitations: FT | tuple[FT, ...] | None = None,  # CON.9
        consent_mode: ConsentMode
        | CNE
        | tuple[ConsentMode | CNE, ...]
        | None = None,  # CON.10
        consent_discussion_date_or_time: TS | tuple[TS, ...] | None = None,  # CON.12
        consent_decision_date_or_time: TS | tuple[TS, ...] | None = None,  # CON.13
        consent_effective_date_or_time: TS | tuple[TS, ...] | None = None,  # CON.14
        consent_end_date_or_time: TS | tuple[TS, ...] | None = None,  # CON.15
        subject_competence_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # CON.16
        translator_assistance_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # CON.17
        language_translated_to: PrimaryLanguage
        | ID
        | tuple[PrimaryLanguage | ID, ...]
        | None = None,  # CON.18
        informational_material_supplied_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # CON.19
        consent_bypass_reason: ConsentBypassReason
        | CWE
        | tuple[ConsentBypassReason | CWE, ...]
        | None = None,  # CON.20
        consent_disclosure_level: ConsentDisclosureLevel
        | ID
        | tuple[ConsentDisclosureLevel | ID, ...]
        | None = None,  # CON.21
        consent_non_disclosure_reason: ConsentNonDisclosureReason
        | CWE
        | tuple[ConsentNonDisclosureReason | CWE, ...]
        | None = None,  # CON.22
        non_subject_consenter_reason: NonSubjectConsenterReason
        | CWE
        | tuple[NonSubjectConsenterReason | CWE, ...]
        | None = None,  # CON.23
    ):
        """
        Consent - `CON <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CON>`_
        The consent segment provides details about a specific consent by a patient or staff member

        :param set_id_con: Sequence ID (id: CON.1 | len: 4 | use: R | rpt: 1)
        :param consent_type: Coded with Exceptions (id: CON.2 | len: 250 | use: O | rpt: 1)
        :param consent_form_id: String Data (id: CON.3 | len: 40 | use: O | rpt: 1)
        :param consent_form_number: Entity Identifier (id: CON.4 | len: 180 | use: O | rpt: 1)
        :param consent_text: Formatted Text Data (id: CON.5 | len: 65536 | use: O | rpt: *)
        :param subject_specific_consent_text: Formatted Text Data (id: CON.6 | len: 65536 | use: O | rpt: *)
        :param consent_background: Formatted Text Data (id: CON.7 | len: 65536 | use: O | rpt: *)
        :param subject_specific_consent_background: Formatted Text Data (id: CON.8 | len: 65536 | use: O | rpt: *)
        :param consenter_imposed_limitations: Formatted Text Data (id: CON.9 | len: 65536 | use: O | rpt: *)
        :param consent_mode: Coded with No Exceptions (id: CON.10 | len: 2 | use: O | rpt: 1)
        :param consent_status: Coded with No Exceptions (id: CON.11 | len: 2 | use: R | rpt: 1)
        :param consent_discussion_date_or_time: Time Stamp (id: CON.12 | len: 26 | use: O | rpt: 1)
        :param consent_decision_date_or_time: Time Stamp (id: CON.13 | len: 26 | use: O | rpt: 1)
        :param consent_effective_date_or_time: Time Stamp (id: CON.14 | len: 26 | use: O | rpt: 1)
        :param consent_end_date_or_time: Time Stamp (id: CON.15 | len: 26 | use: O | rpt: 1)
        :param subject_competence_indicator: Coded values for HL7 tables (id: CON.16 | len: 1 | use: O | rpt: 1)
        :param translator_assistance_indicator: Coded values for HL7 tables (id: CON.17 | len: 1 | use: O | rpt: 1)
        :param language_translated_to: Coded values for HL7 tables (id: CON.18 | len: 1 | use: O | rpt: 1)
        :param informational_material_supplied_indicator: Coded values for HL7 tables (id: CON.19 | len: 1 | use: O | rpt: 1)
        :param consent_bypass_reason: Coded with Exceptions (id: CON.20 | len: 250 | use: O | rpt: 1)
        :param consent_disclosure_level: Coded values for HL7 tables (id: CON.21 | len: 1 | use: O | rpt: 1)
        :param consent_non_disclosure_reason: Coded with Exceptions (id: CON.22 | len: 250 | use: O | rpt: 1)
        :param non_subject_consenter_reason: Coded with Exceptions (id: CON.23 | len: 250 | use: O | rpt: 1)
        :param consenter_id: Extended Person Name (id: CON.24 | len: 250 | use: R | rpt: *)
        :param relationship_to_subject_table: Coded value for user-defined tables (id: CON.25 | len: 100 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 25
        self.set_id_con = set_id_con
        self.consent_type = consent_type
        self.consent_form_id = consent_form_id
        self.consent_form_number = consent_form_number
        self.consent_text = consent_text
        self.subject_specific_consent_text = subject_specific_consent_text
        self.consent_background = consent_background
        self.subject_specific_consent_background = subject_specific_consent_background
        self.consenter_imposed_limitations = consenter_imposed_limitations
        self.consent_mode = consent_mode
        self.consent_status = consent_status
        self.consent_discussion_date_or_time = consent_discussion_date_or_time
        self.consent_decision_date_or_time = consent_decision_date_or_time
        self.consent_effective_date_or_time = consent_effective_date_or_time
        self.consent_end_date_or_time = consent_end_date_or_time
        self.subject_competence_indicator = subject_competence_indicator
        self.translator_assistance_indicator = translator_assistance_indicator
        self.language_translated_to = language_translated_to
        self.informational_material_supplied_indicator = (
            informational_material_supplied_indicator
        )
        self.consent_bypass_reason = consent_bypass_reason
        self.consent_disclosure_level = consent_disclosure_level
        self.consent_non_disclosure_reason = consent_non_disclosure_reason
        self.non_subject_consenter_reason = non_subject_consenter_reason
        self.consenter_id = consenter_id
        self.relationship_to_subject_table = relationship_to_subject_table

    @property  # get CON.1
    def set_id_con(self) -> SI:
        """
        id: CON.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.1
        """
        return self._c_data[0][0]

    @set_id_con.setter  # set CON.1
    def set_id_con(self, si: SI):
        """
        id: CON.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.1
        """
        self._c_data[0] = (si,)

    @property  # get CON.2
    def consent_type(self) -> ConsentType | None:
        """
        id: CON.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.2
        """
        return self._c_data[1][0]

    @consent_type.setter  # set CON.2
    def consent_type(self, consent_type: ConsentType | None):
        """
        id: CON.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.2
        """
        self._c_data[1] = (consent_type,)

    @property  # get CON.3
    def consent_form_id(self) -> ST | None:
        """
        id: CON.3 | len: 40 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.3
        """
        return self._c_data[2][0]

    @consent_form_id.setter  # set CON.3
    def consent_form_id(self, st: ST | None):
        """
        id: CON.3 | len: 40 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.3
        """
        self._c_data[2] = (st,)

    @property  # get CON.4
    def consent_form_number(self) -> EI | None:
        """
        id: CON.4 | len: 180 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.4
        """
        return self._c_data[3][0]

    @consent_form_number.setter  # set CON.4
    def consent_form_number(self, ei: EI | None):
        """
        id: CON.4 | len: 180 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.4
        """
        self._c_data[3] = (ei,)

    @property
    def consent_text(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: CON.5 | len: 65536 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.5
        """
        return self._c_data[4]

    @consent_text.setter  # set CON.5
    def consent_text(self, ft: FT | tuple[FT] | None):
        """
        id: CON.5 | len: 65536 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.5
        """
        if isinstance(ft, tuple):
            self._c_data[4] = ft
        else:
            self._c_data[4] = (ft,)

    @property
    def subject_specific_consent_text(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: CON.6 | len: 65536 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.6
        """
        return self._c_data[5]

    @subject_specific_consent_text.setter  # set CON.6
    def subject_specific_consent_text(self, ft: FT | tuple[FT] | None):
        """
        id: CON.6 | len: 65536 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.6
        """
        if isinstance(ft, tuple):
            self._c_data[5] = ft
        else:
            self._c_data[5] = (ft,)

    @property
    def consent_background(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: CON.7 | len: 65536 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.7
        """
        return self._c_data[6]

    @consent_background.setter  # set CON.7
    def consent_background(self, ft: FT | tuple[FT] | None):
        """
        id: CON.7 | len: 65536 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.7
        """
        if isinstance(ft, tuple):
            self._c_data[6] = ft
        else:
            self._c_data[6] = (ft,)

    @property
    def subject_specific_consent_background(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: CON.8 | len: 65536 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.8
        """
        return self._c_data[7]

    @subject_specific_consent_background.setter  # set CON.8
    def subject_specific_consent_background(self, ft: FT | tuple[FT] | None):
        """
        id: CON.8 | len: 65536 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.8
        """
        if isinstance(ft, tuple):
            self._c_data[7] = ft
        else:
            self._c_data[7] = (ft,)

    @property
    def consenter_imposed_limitations(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: CON.9 | len: 65536 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.9
        """
        return self._c_data[8]

    @consenter_imposed_limitations.setter  # set CON.9
    def consenter_imposed_limitations(self, ft: FT | tuple[FT] | None):
        """
        id: CON.9 | len: 65536 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.9
        """
        if isinstance(ft, tuple):
            self._c_data[8] = ft
        else:
            self._c_data[8] = (ft,)

    @property  # get CON.10
    def consent_mode(self) -> ConsentMode | None:
        """
        id: CON.10 | len: 2 | use: O | rpt: 1
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.10
        """
        return self._c_data[9][0]

    @consent_mode.setter  # set CON.10
    def consent_mode(self, consent_mode: ConsentMode | None):
        """
        id: CON.10 | len: 2 | use: O | rpt: 1
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.10
        """
        self._c_data[9] = (consent_mode,)

    @property  # get CON.11
    def consent_status(self) -> ConsentStatus:
        """
        id: CON.11 | len: 2 | use: R | rpt: 1
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.11
        """
        return self._c_data[10][0]

    @consent_status.setter  # set CON.11
    def consent_status(self, consent_status: ConsentStatus):
        """
        id: CON.11 | len: 2 | use: R | rpt: 1
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.11
        """
        self._c_data[10] = (consent_status,)

    @property  # get CON.12
    def consent_discussion_date_or_time(self) -> TS | None:
        """
        id: CON.12 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.12
        """
        return self._c_data[11][0]

    @consent_discussion_date_or_time.setter  # set CON.12
    def consent_discussion_date_or_time(self, ts: TS | None):
        """
        id: CON.12 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.12
        """
        self._c_data[11] = (ts,)

    @property  # get CON.13
    def consent_decision_date_or_time(self) -> TS | None:
        """
        id: CON.13 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.13
        """
        return self._c_data[12][0]

    @consent_decision_date_or_time.setter  # set CON.13
    def consent_decision_date_or_time(self, ts: TS | None):
        """
        id: CON.13 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.13
        """
        self._c_data[12] = (ts,)

    @property  # get CON.14
    def consent_effective_date_or_time(self) -> TS | None:
        """
        id: CON.14 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.14
        """
        return self._c_data[13][0]

    @consent_effective_date_or_time.setter  # set CON.14
    def consent_effective_date_or_time(self, ts: TS | None):
        """
        id: CON.14 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.14
        """
        self._c_data[13] = (ts,)

    @property  # get CON.15
    def consent_end_date_or_time(self) -> TS | None:
        """
        id: CON.15 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.15
        """
        return self._c_data[14][0]

    @consent_end_date_or_time.setter  # set CON.15
    def consent_end_date_or_time(self, ts: TS | None):
        """
        id: CON.15 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.15
        """
        self._c_data[14] = (ts,)

    @property  # get CON.16
    def subject_competence_indicator(self) -> YesOrNoIndicator | None:
        """
        id: CON.16 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.16
        """
        return self._c_data[15][0]

    @subject_competence_indicator.setter  # set CON.16
    def subject_competence_indicator(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: CON.16 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.16
        """
        self._c_data[15] = (yes_or_no_indicator,)

    @property  # get CON.17
    def translator_assistance_indicator(self) -> YesOrNoIndicator | None:
        """
        id: CON.17 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.17
        """
        return self._c_data[16][0]

    @translator_assistance_indicator.setter  # set CON.17
    def translator_assistance_indicator(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: CON.17 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.17
        """
        self._c_data[16] = (yes_or_no_indicator,)

    @property  # get CON.18
    def language_translated_to(self) -> PrimaryLanguage | None:
        """
        id: CON.18 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.18
        """
        return self._c_data[17][0]

    @language_translated_to.setter  # set CON.18
    def language_translated_to(self, primary_language: PrimaryLanguage | None):
        """
        id: CON.18 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.18
        """
        self._c_data[17] = (primary_language,)

    @property  # get CON.19
    def informational_material_supplied_indicator(self) -> YesOrNoIndicator | None:
        """
        id: CON.19 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.19
        """
        return self._c_data[18][0]

    @informational_material_supplied_indicator.setter  # set CON.19
    def informational_material_supplied_indicator(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: CON.19 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.19
        """
        self._c_data[18] = (yes_or_no_indicator,)

    @property  # get CON.20
    def consent_bypass_reason(self) -> ConsentBypassReason | None:
        """
        id: CON.20 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.20
        """
        return self._c_data[19][0]

    @consent_bypass_reason.setter  # set CON.20
    def consent_bypass_reason(self, consent_bypass_reason: ConsentBypassReason | None):
        """
        id: CON.20 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.20
        """
        self._c_data[19] = (consent_bypass_reason,)

    @property  # get CON.21
    def consent_disclosure_level(self) -> ConsentDisclosureLevel | None:
        """
        id: CON.21 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.21
        """
        return self._c_data[20][0]

    @consent_disclosure_level.setter  # set CON.21
    def consent_disclosure_level(
        self, consent_disclosure_level: ConsentDisclosureLevel | None
    ):
        """
        id: CON.21 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.21
        """
        self._c_data[20] = (consent_disclosure_level,)

    @property  # get CON.22
    def consent_non_disclosure_reason(self) -> ConsentNonDisclosureReason | None:
        """
        id: CON.22 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.22
        """
        return self._c_data[21][0]

    @consent_non_disclosure_reason.setter  # set CON.22
    def consent_non_disclosure_reason(
        self, consent_nondisclosure_reason: ConsentNonDisclosureReason | None
    ):
        """
        id: CON.22 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.22
        """
        self._c_data[21] = (consent_nondisclosure_reason,)

    @property  # get CON.23
    def non_subject_consenter_reason(self) -> NonSubjectConsenterReason | None:
        """
        id: CON.23 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.23
        """
        return self._c_data[22][0]

    @non_subject_consenter_reason.setter  # set CON.23
    def non_subject_consenter_reason(
        self, nonsubject_consenter_reason: NonSubjectConsenterReason | None
    ):
        """
        id: CON.23 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.23
        """
        self._c_data[22] = (nonsubject_consenter_reason,)

    @property
    def consenter_id(self) -> tuple[XPN, ...]:
        """
        id: CON.24 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.24
        """
        return self._c_data[23]

    @consenter_id.setter  # set CON.24
    def consenter_id(self, xpn: XPN | tuple[XPN]):
        """
        id: CON.24 | len: 250 | use: R | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.24
        """
        if isinstance(xpn, tuple):
            self._c_data[23] = xpn
        else:
            self._c_data[23] = (xpn,)

    @property
    def relationship_to_subject_table(
        self,
    ) -> tuple[SignatorySRelationshipToSubject, ...]:
        """
        id: CON.25 | len: 100 | use: R | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.25
        """
        return self._c_data[24]

    @relationship_to_subject_table.setter  # set CON.25
    def relationship_to_subject_table(
        self,
        signatorys_relationship_to_subject: SignatorySRelationshipToSubject
        | tuple[SignatorySRelationshipToSubject],
    ):
        """
        id: CON.25 | len: 100 | use: R | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CON.25
        """
        if isinstance(signatorys_relationship_to_subject, tuple):
            self._c_data[24] = signatorys_relationship_to_subject
        else:
            self._c_data[24] = (signatorys_relationship_to_subject,)
