from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TS import TS
from ..data_types.VARIES import VARIES
from ..data_types.ST import ST
from ..data_types.ID import ID
from ..tables.PrimaryKeyValueType import PrimaryKeyValueType
from ..tables.MfnRecordLevelErrorReturn import MfnRecordLevelErrorReturn
from ..tables.RecordLevelEventCode import RecordLevelEventCode


"""
Master File Acknowledgment - MFA
HL7 Version: 2.5.1

-----BEGIN SEGMENT::MFA TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MFA,
    CE, TS, VARIES, ST, ID
)

mfa = MFA(  #  - The Technical Steward for the MFA segment is CQ
    record_level_event_code=id,  # ID(...)  # Required.
    mfn_control_id=None,  # ST(...) 
    event_completion_date_or_time=None,  # TS(...) 
    mfn_record_level_error_return=ce,  # CE(...)  # Required.
    primary_key_value_mfa=varies,  # VARIES(...)  # Required.
    primary_key_value_type_mfa=id,  # ID(...)  # Required.
)

-----END SEGMENT::MFA TEMPLATE-----
"""


class MFA(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """MFA"""
    _hl7_name = """Master File Acknowledgment"""
    _hl7_description = """The Technical Steward for the MFA segment is CQ"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFA"
    _c_length = (3, 20, 26, 250, 250, 3,)
    _c_rpt = (1, 1, 1, 1, 65535, 65535,)
    _c_usage = ("R", "C", "O", "R", "R", "R",)
    _c_components = (ID, ST, TS, CE, VARIES, ID,)
    _c_aliases = ("MFA.1", "MFA.2", "MFA.3", "MFA.4", "MFA.5", "MFA.6",)
    _c_names = ("Record-Level Event Code", "MFN Control ID", "Event Completion Date/Time", "MFN Record Level Error Return", "Primary Key Value - MFA", "Primary Key Value Type - MFA",)
    _c_attrs = ("record_level_event_code", "mfn_control_id", "event_completion_date_or_time", "mfn_record_level_error_return", "primary_key_value_mfa", "primary_key_value_type_mfa",)
    # fmt: on

    def __init__(
        self,
        record_level_event_code: RecordLevelEventCode
        | ID
        | tuple[RecordLevelEventCode | ID, ...],  # MFA.1
        mfn_record_level_error_return: MfnRecordLevelErrorReturn
        | CE
        | tuple[MfnRecordLevelErrorReturn | CE, ...],  # MFA.4
        primary_key_value_mfa: VARIES | tuple[VARIES, ...],  # MFA.5
        primary_key_value_type_mfa: PrimaryKeyValueType
        | ID
        | tuple[PrimaryKeyValueType | ID, ...],  # MFA.6
        mfn_control_id: ST | tuple[ST, ...] | None = None,  # MFA.2
        event_completion_date_or_time: TS | tuple[TS, ...] | None = None,  # MFA.3
    ):
        """
        Master File Acknowledgment - `MFA <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFA>`_
        The Technical Steward for the MFA segment is CQ.

        :param record_level_event_code: Coded values for HL7 tables (id: MFA.1 | len: 3 | use: R | rpt: 1)
        :param mfn_control_id: String Data (id: MFA.2 | len: 20 | use: C | rpt: 1)
        :param event_completion_date_or_time: Time Stamp (id: MFA.3 | len: 26 | use: O | rpt: 1)
        :param mfn_record_level_error_return: Coded Element (id: MFA.4 | len: 250 | use: R | rpt: 1)
        :param primary_key_value_mfa: Variable Datatype (id: MFA.5 | len: 250 | use: R | rpt: *)
        :param primary_key_value_type_mfa: Coded values for HL7 tables (id: MFA.6 | len: 3 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.record_level_event_code = record_level_event_code
        self.mfn_control_id = mfn_control_id
        self.event_completion_date_or_time = event_completion_date_or_time
        self.mfn_record_level_error_return = mfn_record_level_error_return
        self.primary_key_value_mfa = primary_key_value_mfa
        self.primary_key_value_type_mfa = primary_key_value_type_mfa

    @property  # get MFA.1
    def record_level_event_code(self) -> RecordLevelEventCode:
        """
        id: MFA.1 | len: 3 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.1
        """
        return self._c_data[0][0]

    @record_level_event_code.setter  # set MFA.1
    def record_level_event_code(self, recordlevel_event_code: RecordLevelEventCode):
        """
        id: MFA.1 | len: 3 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.1
        """
        self._c_data[0] = (recordlevel_event_code,)

    @property  # get MFA.2
    def mfn_control_id(self) -> ST | None:
        """
        id: MFA.2 | len: 20 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.2
        """
        return self._c_data[1][0]

    @mfn_control_id.setter  # set MFA.2
    def mfn_control_id(self, st: ST | None):
        """
        id: MFA.2 | len: 20 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.2
        """
        self._c_data[1] = (st,)

    @property  # get MFA.3
    def event_completion_date_or_time(self) -> TS | None:
        """
        id: MFA.3 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.3
        """
        return self._c_data[2][0]

    @event_completion_date_or_time.setter  # set MFA.3
    def event_completion_date_or_time(self, ts: TS | None):
        """
        id: MFA.3 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.3
        """
        self._c_data[2] = (ts,)

    @property  # get MFA.4
    def mfn_record_level_error_return(self) -> MfnRecordLevelErrorReturn:
        """
        id: MFA.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.4
        """
        return self._c_data[3][0]

    @mfn_record_level_error_return.setter  # set MFA.4
    def mfn_record_level_error_return(
        self, mfn_recordlevel_error_return: MfnRecordLevelErrorReturn
    ):
        """
        id: MFA.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.4
        """
        self._c_data[3] = (mfn_recordlevel_error_return,)

    @property
    def primary_key_value_mfa(self) -> tuple[VARIES, ...]:
        """
        id: MFA.5 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[VARIES, ...]: (Variable Datatype, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.5
        """
        return self._c_data[4]

    @primary_key_value_mfa.setter  # set MFA.5
    def primary_key_value_mfa(self, varies: VARIES | tuple[VARIES]):
        """
        id: MFA.5 | len: 250 | use: R | rpt: *
        ---
        param_type: VARIES | tuple[VARIES, ...]: (Variable Datatype, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.5
        """
        if isinstance(varies, tuple):
            self._c_data[4] = varies
        else:
            self._c_data[4] = (varies,)

    @property
    def primary_key_value_type_mfa(self) -> tuple[PrimaryKeyValueType, ...]:
        """
        id: MFA.6 | len: 3 | use: R | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.6
        """
        return self._c_data[5]

    @primary_key_value_type_mfa.setter  # set MFA.6
    def primary_key_value_type_mfa(
        self, primary_key_value_type: PrimaryKeyValueType | tuple[PrimaryKeyValueType]
    ):
        """
        id: MFA.6 | len: 3 | use: R | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFA.6
        """
        if isinstance(primary_key_value_type, tuple):
            self._c_data[5] = primary_key_value_type
        else:
            self._c_data[5] = (primary_key_value_type,)
