from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TQ import TQ
from ..data_types.TX import TX
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.CE import CE
from ..tables.RemoteControlCommand import RemoteControlCommand
from ..tables.YesOrNoIndicator import YesOrNoIndicator


"""
Equipment Command - ECD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ECD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ECD,
    TQ, TX, ID, NM, CE
)

ecd = ECD(  #  - The equipment command segment contains the information required to notify the receiving component what is to happen
    reference_command_number=nm,  # NM(...)  # Required.
    remote_control_command=ce,  # CE(...)  # Required.
    response_required=None,  # ID(...) 
    requested_completion_time=None,  # TQ(...) 
    parameters=None,  # TX(...) 
)

-----END SEGMENT::ECD TEMPLATE-----
"""


class ECD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ECD"""
    _hl7_name = """Equipment Command"""
    _hl7_description = """The equipment command segment contains the information required to notify the receiving component what is to happen"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ECD"
    _c_length = (20, 250, 80, 200, 65536,)
    _c_rpt = (1, 1, 1, 1, 65535,)
    _c_usage = ("R", "R", "O", "B", "O",)
    _c_components = (NM, CE, ID, TQ, TX,)
    _c_aliases = ("ECD.1", "ECD.2", "ECD.3", "ECD.4", "ECD.5",)
    _c_names = ("Reference Command Number", "Remote Control Command", "Response Required", "Requested Completion Time", "Parameters",)
    _c_attrs = ("reference_command_number", "remote_control_command", "response_required", "requested_completion_time", "parameters",)
    # fmt: on

    def __init__(
        self,
        reference_command_number: NM | tuple[NM],  # ECD.1
        remote_control_command: RemoteControlCommand
        | CE
        | tuple[RemoteControlCommand | CE],  # ECD.2
        response_required: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # ECD.3
        requested_completion_time: TQ | tuple[TQ] | None = None,  # ECD.4
        parameters: TX | tuple[TX] | None = None,  # ECD.5
    ):
        """
        Equipment Command - `ECD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ECD>`_
        The equipment command segment contains the information required to notify the receiving component what is to happen.

        :param reference_command_number: Numeric (id: ECD.1 | len: 20 | use: R | rpt: 1)
        :param remote_control_command: Coded Element (id: ECD.2 | len: 250 | use: R | rpt: 1)
        :param response_required: Coded values for HL7 tables (id: ECD.3 | len: 80 | use: O | rpt: 1)
        :param requested_completion_time: Timing Quantity (id: ECD.4 | len: 200 | use: B | rpt: 1)
        :param parameters: Text Data (id: ECD.5 | len: 65536 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.reference_command_number = reference_command_number
        self.remote_control_command = remote_control_command
        self.response_required = response_required
        self.requested_completion_time = requested_completion_time
        self.parameters = parameters

    @property  # get ECD.1
    def reference_command_number(self) -> NM:
        """
        id: ECD.1 | len: 20 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECD.1
        """
        return self._c_data[0][0]

    @reference_command_number.setter  # set ECD.1
    def reference_command_number(self, nm: NM):
        """
        id: ECD.1 | len: 20 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECD.1
        """
        self._c_data[0] = (nm,)

    @property  # get ECD.2
    def remote_control_command(self) -> RemoteControlCommand:
        """
        id: ECD.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECD.2
        """
        return self._c_data[1][0]

    @remote_control_command.setter  # set ECD.2
    def remote_control_command(self, remote_control_command: RemoteControlCommand):
        """
        id: ECD.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECD.2
        """
        self._c_data[1] = (remote_control_command,)

    @property  # get ECD.3
    def response_required(self) -> YesOrNoIndicator | None:
        """
        id: ECD.3 | len: 80 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECD.3
        """
        return self._c_data[2][0]

    @response_required.setter  # set ECD.3
    def response_required(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: ECD.3 | len: 80 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECD.3
        """
        self._c_data[2] = (yes_or_no_indicator,)

    @property  # get ECD.4
    def requested_completion_time(self) -> TQ | None:
        """
        id: ECD.4 | len: 200 | use: B | rpt: 1
        ---
        return_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECD.4
        """
        return self._c_data[3][0]

    @requested_completion_time.setter  # set ECD.4
    def requested_completion_time(self, tq: TQ | None):
        """
        id: ECD.4 | len: 200 | use: B | rpt: 1
        ---
        param_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECD.4
        """
        self._c_data[3] = (tq,)

    @property
    def parameters(self) -> tuple[TX, ...] | tuple[None]:
        """
        id: ECD.5 | len: 65536 | use: O | rpt: *
        ---
        return_type: tuple[TX, ...]: (Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECD.5
        """
        return self._c_data[4]

    @parameters.setter  # set ECD.5
    def parameters(self, tx: TX | tuple[TX] | None):
        """
        id: ECD.5 | len: 65536 | use: O | rpt: *
        ---
        param_type: TX | tuple[TX, ...]: (Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECD.5
        """
        if isinstance(tx, tuple):
            self._c_data[4] = tx
        else:
            self._c_data[4] = (tx,)
