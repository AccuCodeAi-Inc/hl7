from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ELD import ELD
from ..data_types.TX import TX
from ..data_types.IS import IS
from ..data_types.ERL import ERL
from ..data_types.ID import ID
from ..data_types.XTN import XTN
from ..data_types.ST import ST
from ..data_types.CWE import CWE
from ..tables.ApplicationErrorCode import ApplicationErrorCode
from ..tables.OverrideType import OverrideType
from ..tables.ErrorSeverity import ErrorSeverity
from ..tables.InformPersonCode import InformPersonCode
from ..tables.OverrideReason import OverrideReason
from ..tables.MessageErrorConditionCodes import MessageErrorConditionCodes


"""
Error - ERR
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ERR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ERR,
    ELD, TX, IS, ERL, ID, XTN, ST, CWE
)

err = ERR(  #  - The ERR segment is used to add error comments to acknowledgment messages
    error_code_and_location=None,  # ELD(...) 
    error_location=None,  # ERL(...) 
    hl7_error_code=cwe,  # CWE(...)  # Required.
    severity=id,  # ID(...)  # Required.
    application_error_code=None,  # CWE(...) 
    application_error_parameter=None,  # ST(...) 
    diagnostic_information=None,  # TX(...) 
    user_message=None,  # TX(...) 
    inform_person_indicator=None,  # IS(...) 
    override_type=None,  # CWE(...) 
    override_reason_code=None,  # CWE(...) 
    help_desk_contact_point=None,  # XTN(...) 
)

-----END SEGMENT::ERR TEMPLATE-----
"""


class ERR(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ERR"""
    _hl7_name = """Error"""
    _hl7_description = """The ERR segment is used to add error comments to acknowledgment messages"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR"
    _c_length = (493, 18, 705, 2, 705, 80, 2048, 250, 20, 705, 705, 652,)
    _c_rpt = (65535, 65535, 1, 1, 1, 10, 1, 1, 65535, 1, 65535, 65535,)
    _c_usage = ("B", "O", "R", "R", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (ELD, ERL, CWE, ID, CWE, ST, TX, TX, IS, CWE, CWE, XTN,)
    _c_aliases = ("ERR.1", "ERR.2", "ERR.3", "ERR.4", "ERR.5", "ERR.6", "ERR.7", "ERR.8", "ERR.9", "ERR.10", "ERR.11", "ERR.12",)
    _c_names = ("Error Code and Location", "Error Location", "HL7 Error Code", "Severity", "Application Error Code", "Application Error Parameter", "Diagnostic Information", "User Message", "Inform Person Indicator", "Override Type", "Override Reason Code", "Help Desk Contact Point",)
    _c_attrs = ("error_code_and_location", "error_location", "hl7_error_code", "severity", "application_error_code", "application_error_parameter", "diagnostic_information", "user_message", "inform_person_indicator", "override_type", "override_reason_code", "help_desk_contact_point",)
    # fmt: on

    def __init__(
        self,
        hl7_error_code: MessageErrorConditionCodes | CWE,  # ERR.3
        severity: ErrorSeverity | ID,  # ERR.4
        error_code_and_location: ELD | None = None,  # ERR.1
        error_location: ERL | None = None,  # ERR.2
        application_error_code: ApplicationErrorCode | CWE | None = None,  # ERR.5
        application_error_parameter: ST | None = None,  # ERR.6
        diagnostic_information: TX | None = None,  # ERR.7
        user_message: TX | None = None,  # ERR.8
        inform_person_indicator: InformPersonCode | IS | None = None,  # ERR.9
        override_type: OverrideType | CWE | None = None,  # ERR.10
        override_reason_code: OverrideReason | CWE | None = None,  # ERR.11
        help_desk_contact_point: XTN | None = None,  # ERR.12
    ):
        """
        Error - `ERR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR>`_
        The ERR segment is used to add error comments to acknowledgment messages.

        :param error_code_and_location: Error Location and Description (id: ERR.1 | len: 493 | use: B | rpt: *)
        :param error_location: Error Location (id: ERR.2 | len: 18 | use: O | rpt: *)
        :param hl7_error_code: Coded with Exceptions (id: ERR.3 | len: 705 | use: R | rpt: 1)
        :param severity: Coded values for HL7 tables (id: ERR.4 | len: 2 | use: R | rpt: 1)
        :param application_error_code: Coded with Exceptions (id: ERR.5 | len: 705 | use: O | rpt: 1)
        :param application_error_parameter: String Data (id: ERR.6 | len: 80 | use: O | rpt: 10)
        :param diagnostic_information: Text Data (id: ERR.7 | len: 2048 | use: O | rpt: 1)
        :param user_message: Text Data (id: ERR.8 | len: 250 | use: O | rpt: 1)
        :param inform_person_indicator: Coded value for user-defined tables (id: ERR.9 | len: 20 | use: O | rpt: *)
        :param override_type: Coded with Exceptions (id: ERR.10 | len: 705 | use: O | rpt: 1)
        :param override_reason_code: Coded with Exceptions (id: ERR.11 | len: 705 | use: O | rpt: *)
        :param help_desk_contact_point: Extended Telecommunication Number (id: ERR.12 | len: 652 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.error_code_and_location = error_code_and_location
        self.error_location = error_location
        self.hl7_error_code = hl7_error_code
        self.severity = severity
        self.application_error_code = application_error_code
        self.application_error_parameter = application_error_parameter
        self.diagnostic_information = diagnostic_information
        self.user_message = user_message
        self.inform_person_indicator = inform_person_indicator
        self.override_type = override_type
        self.override_reason_code = override_reason_code
        self.help_desk_contact_point = help_desk_contact_point

    @property
    def error_code_and_location(self) -> tuple[ELD, ...] | tuple[None]:
        """
        id: ERR.1 | len: 493 | use: B | rpt: *
        ---
        return_type: tuple[ELD, ...]: (Error Location and Description, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.1
        """
        return self._c_data[0]

    @error_code_and_location.setter  # set ERR.1
    def error_code_and_location(self, eld: ELD | tuple[ELD] | None):
        """
        id: ERR.1 | len: 493 | use: B | rpt: *
        ---
        param_type: ELD | tuple[ELD, ...]: (Error Location and Description, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.1
        """
        if isinstance(eld, tuple):
            self._c_data[0] = eld
        else:
            self._c_data[0] = (eld,)

    @property
    def error_location(self) -> tuple[ERL, ...] | tuple[None]:
        """
        id: ERR.2 | len: 18 | use: O | rpt: *
        ---
        return_type: tuple[ERL, ...]: (Error Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.2
        """
        return self._c_data[1]

    @error_location.setter  # set ERR.2
    def error_location(self, erl: ERL | tuple[ERL] | None):
        """
        id: ERR.2 | len: 18 | use: O | rpt: *
        ---
        param_type: ERL | tuple[ERL, ...]: (Error Location, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.2
        """
        if isinstance(erl, tuple):
            self._c_data[1] = erl
        else:
            self._c_data[1] = (erl,)

    @property  # get ERR.3
    def hl7_error_code(self) -> MessageErrorConditionCodes:
        """
        id: ERR.3 | len: 705 | use: R | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.3
        """
        return self._c_data[2][0]

    @hl7_error_code.setter  # set ERR.3
    def hl7_error_code(self, message_error_condition_codes: MessageErrorConditionCodes):
        """
        id: ERR.3 | len: 705 | use: R | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.3
        """
        self._c_data[2] = (message_error_condition_codes,)

    @property  # get ERR.4
    def severity(self) -> ErrorSeverity:
        """
        id: ERR.4 | len: 2 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.4
        """
        return self._c_data[3][0]

    @severity.setter  # set ERR.4
    def severity(self, error_severity: ErrorSeverity):
        """
        id: ERR.4 | len: 2 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.4
        """
        self._c_data[3] = (error_severity,)

    @property  # get ERR.5
    def application_error_code(self) -> ApplicationErrorCode | None:
        """
        id: ERR.5 | len: 705 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.5
        """
        return self._c_data[4][0]

    @application_error_code.setter  # set ERR.5
    def application_error_code(
        self, application_error_code: ApplicationErrorCode | None
    ):
        """
        id: ERR.5 | len: 705 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.5
        """
        self._c_data[4] = (application_error_code,)

    @property
    def application_error_parameter(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: ERR.6 | len: 80 | use: O | rpt: 10
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.6
        """
        return self._c_data[5]

    @application_error_parameter.setter  # set ERR.6
    def application_error_parameter(self, st: ST | tuple[ST] | None):
        """
        id: ERR.6 | len: 80 | use: O | rpt: 10
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.6
        """
        if isinstance(st, tuple):
            self._c_data[5] = st
        else:
            self._c_data[5] = (st,)

    @property  # get ERR.7
    def diagnostic_information(self) -> TX | None:
        """
        id: ERR.7 | len: 2048 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.7
        """
        return self._c_data[6][0]

    @diagnostic_information.setter  # set ERR.7
    def diagnostic_information(self, tx: TX | None):
        """
        id: ERR.7 | len: 2048 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.7
        """
        self._c_data[6] = (tx,)

    @property  # get ERR.8
    def user_message(self) -> TX | None:
        """
        id: ERR.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.8
        """
        return self._c_data[7][0]

    @user_message.setter  # set ERR.8
    def user_message(self, tx: TX | None):
        """
        id: ERR.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.8
        """
        self._c_data[7] = (tx,)

    @property
    def inform_person_indicator(self) -> tuple[InformPersonCode, ...] | tuple[None]:
        """
        id: ERR.9 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.9
        """
        return self._c_data[8]

    @inform_person_indicator.setter  # set ERR.9
    def inform_person_indicator(
        self, inform_person_code: InformPersonCode | tuple[InformPersonCode] | None
    ):
        """
        id: ERR.9 | len: 20 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.9
        """
        if isinstance(inform_person_code, tuple):
            self._c_data[8] = inform_person_code
        else:
            self._c_data[8] = (inform_person_code,)

    @property  # get ERR.10
    def override_type(self) -> OverrideType | None:
        """
        id: ERR.10 | len: 705 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.10
        """
        return self._c_data[9][0]

    @override_type.setter  # set ERR.10
    def override_type(self, override_type: OverrideType | None):
        """
        id: ERR.10 | len: 705 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.10
        """
        self._c_data[9] = (override_type,)

    @property
    def override_reason_code(self) -> tuple[OverrideReason, ...] | tuple[None]:
        """
        id: ERR.11 | len: 705 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.11
        """
        return self._c_data[10]

    @override_reason_code.setter  # set ERR.11
    def override_reason_code(
        self, override_reason: OverrideReason | tuple[OverrideReason] | None
    ):
        """
        id: ERR.11 | len: 705 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.11
        """
        if isinstance(override_reason, tuple):
            self._c_data[10] = override_reason
        else:
            self._c_data[10] = (override_reason,)

    @property
    def help_desk_contact_point(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: ERR.12 | len: 652 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.12
        """
        return self._c_data[11]

    @help_desk_contact_point.setter  # set ERR.12
    def help_desk_contact_point(self, xtn: XTN | tuple[XTN] | None):
        """
        id: ERR.12 | len: 652 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERR.12
        """
        if isinstance(xtn, tuple):
            self._c_data[11] = xtn
        else:
            self._c_data[11] = (xtn,)
