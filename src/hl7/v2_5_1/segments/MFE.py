from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.VARIES import VARIES
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..tables.PrimaryKeyValueType import PrimaryKeyValueType
from ..tables.RecordLevelEventCode import RecordLevelEventCode


"""
Master File Entry - MFE
HL7 Version: 2.5.1

-----BEGIN SEGMENT::MFE TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MFE,
    ST, VARIES, ID, TS
)

mfe = MFE(  #  - The Technical Steward for the MFE segment is CQ
    record_level_event_code=id,  # ID(...)  # Required.
    mfn_control_id=None,  # ST(...) 
    effective_date_or_time=None,  # TS(...) 
    primary_key_value_mfe=varies,  # VARIES(...)  # Required.
    primary_key_value_type=id,  # ID(...)  # Required.
)

-----END SEGMENT::MFE TEMPLATE-----
"""


class MFE(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """MFE"""
    _hl7_name = """Master File Entry"""
    _hl7_description = """The Technical Steward for the MFE segment is CQ"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE"
    _c_length = (3, 20, 26, 200, 3,)
    _c_rpt = (1, 1, 1, 65535, 65535,)
    _c_usage = ("R", "C", "O", "R", "R",)
    _c_components = (ID, ST, TS, VARIES, ID,)
    _c_aliases = ("MFE.1", "MFE.2", "MFE.3", "MFE.4", "MFE.5",)
    _c_names = ("Record-Level Event Code", "MFN Control ID", "Effective Date/Time", "Primary Key Value - MFE", "Primary Key Value Type",)
    _c_attrs = ("record_level_event_code", "mfn_control_id", "effective_date_or_time", "primary_key_value_mfe", "primary_key_value_type",)
    # fmt: on

    def __init__(
        self,
        record_level_event_code: RecordLevelEventCode
        | ID
        | tuple[RecordLevelEventCode | ID, ...],  # MFE.1
        primary_key_value_mfe: VARIES | tuple[VARIES, ...],  # MFE.4
        primary_key_value_type: PrimaryKeyValueType
        | ID
        | tuple[PrimaryKeyValueType | ID, ...],  # MFE.5
        mfn_control_id: ST | tuple[ST, ...] | None = None,  # MFE.2
        effective_date_or_time: TS | tuple[TS, ...] | None = None,  # MFE.3
    ):
        """
        Master File Entry - `MFE <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE>`_
        The Technical Steward for the MFE segment is CQ.

        :param record_level_event_code: Coded values for HL7 tables (id: MFE.1 | len: 3 | use: R | rpt: 1)
        :param mfn_control_id: String Data (id: MFE.2 | len: 20 | use: C | rpt: 1)
        :param effective_date_or_time: Time Stamp (id: MFE.3 | len: 26 | use: O | rpt: 1)
        :param primary_key_value_mfe: Variable Datatype (id: MFE.4 | len: 200 | use: R | rpt: *)
        :param primary_key_value_type: Coded values for HL7 tables (id: MFE.5 | len: 3 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.record_level_event_code = record_level_event_code
        self.mfn_control_id = mfn_control_id
        self.effective_date_or_time = effective_date_or_time
        self.primary_key_value_mfe = primary_key_value_mfe
        self.primary_key_value_type = primary_key_value_type

    @property  # get MFE.1
    def record_level_event_code(self) -> RecordLevelEventCode:
        """
        id: MFE.1 | len: 3 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFE.1
        """
        return self._c_data[0][0]

    @record_level_event_code.setter  # set MFE.1
    def record_level_event_code(self, recordlevel_event_code: RecordLevelEventCode):
        """
        id: MFE.1 | len: 3 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFE.1
        """
        self._c_data[0] = (recordlevel_event_code,)

    @property  # get MFE.2
    def mfn_control_id(self) -> ST | None:
        """
        id: MFE.2 | len: 20 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFE.2
        """
        return self._c_data[1][0]

    @mfn_control_id.setter  # set MFE.2
    def mfn_control_id(self, st: ST | None):
        """
        id: MFE.2 | len: 20 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFE.2
        """
        self._c_data[1] = (st,)

    @property  # get MFE.3
    def effective_date_or_time(self) -> TS | None:
        """
        id: MFE.3 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFE.3
        """
        return self._c_data[2][0]

    @effective_date_or_time.setter  # set MFE.3
    def effective_date_or_time(self, ts: TS | None):
        """
        id: MFE.3 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFE.3
        """
        self._c_data[2] = (ts,)

    @property
    def primary_key_value_mfe(self) -> tuple[VARIES, ...]:
        """
        id: MFE.4 | len: 200 | use: R | rpt: *
        ---
        return_type: tuple[VARIES, ...]: (Variable Datatype, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFE.4
        """
        return self._c_data[3]

    @primary_key_value_mfe.setter  # set MFE.4
    def primary_key_value_mfe(self, varies: VARIES | tuple[VARIES]):
        """
        id: MFE.4 | len: 200 | use: R | rpt: *
        ---
        param_type: VARIES | tuple[VARIES, ...]: (Variable Datatype, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFE.4
        """
        if isinstance(varies, tuple):
            self._c_data[3] = varies
        else:
            self._c_data[3] = (varies,)

    @property
    def primary_key_value_type(self) -> tuple[PrimaryKeyValueType, ...]:
        """
        id: MFE.5 | len: 3 | use: R | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFE.5
        """
        return self._c_data[4]

    @primary_key_value_type.setter  # set MFE.5
    def primary_key_value_type(
        self, primary_key_value_type: PrimaryKeyValueType | tuple[PrimaryKeyValueType]
    ):
        """
        id: MFE.5 | len: 3 | use: R | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MFE.5
        """
        if isinstance(primary_key_value_type, tuple):
            self._c_data[4] = primary_key_value_type
        else:
            self._c_data[4] = (primary_key_value_type,)
