from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TX import TX
from ..data_types.CE import CE
from ..data_types.TS import TS
from ..tables.CommandResponse import CommandResponse


"""
Equipment Command Response - ECR
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ECR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ECR,
    TX, CE, TS
)

ecr = ECR(  #  - The equipment command response segment contains the receiving component's response to the previously received command
    command_response=ce,  # CE(...)  # Required.
    date_or_time_completed=ts,  # TS(...)  # Required.
    command_response_parameters=None,  # TX(...) 
)

-----END SEGMENT::ECR TEMPLATE-----
"""


class ECR(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ECR"""
    _hl7_name = """Equipment Command Response"""
    _hl7_description = """The equipment command response segment contains the receiving component's response to the previously received command"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ECR"
    _c_length = (250, 26, 65536,)
    _c_rpt = (1, 1, 65535,)
    _c_usage = ("R", "R", "O",)
    _c_components = (CE, TS, TX,)
    _c_aliases = ("ECR.1", "ECR.2", "ECR.3",)
    _c_names = ("Command Response", "Date/Time Completed", "Command Response Parameters",)
    _c_attrs = ("command_response", "date_or_time_completed", "command_response_parameters",)
    # fmt: on

    def __init__(
        self,
        command_response: CommandResponse | CE | tuple[CommandResponse | CE],  # ECR.1
        date_or_time_completed: TS | tuple[TS],  # ECR.2
        command_response_parameters: TX | tuple[TX] | None = None,  # ECR.3
    ):
        """
        Equipment Command Response - `ECR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ECR>`_
        The equipment command response segment contains the receiving component's response to the previously received command.

        :param command_response: Coded Element (id: ECR.1 | len: 250 | use: R | rpt: 1)
        :param date_or_time_completed: Time Stamp (id: ECR.2 | len: 26 | use: R | rpt: 1)
        :param command_response_parameters: Text Data (id: ECR.3 | len: 65536 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.command_response = command_response
        self.date_or_time_completed = date_or_time_completed
        self.command_response_parameters = command_response_parameters

    @property  # get ECR.1
    def command_response(self) -> CommandResponse:
        """
        id: ECR.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECR.1
        """
        return self._c_data[0][0]

    @command_response.setter  # set ECR.1
    def command_response(self, command_response: CommandResponse):
        """
        id: ECR.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECR.1
        """
        self._c_data[0] = (command_response,)

    @property  # get ECR.2
    def date_or_time_completed(self) -> TS:
        """
        id: ECR.2 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECR.2
        """
        return self._c_data[1][0]

    @date_or_time_completed.setter  # set ECR.2
    def date_or_time_completed(self, ts: TS):
        """
        id: ECR.2 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECR.2
        """
        self._c_data[1] = (ts,)

    @property
    def command_response_parameters(self) -> tuple[TX, ...] | tuple[None]:
        """
        id: ECR.3 | len: 65536 | use: O | rpt: *
        ---
        return_type: tuple[TX, ...]: (Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECR.3
        """
        return self._c_data[2]

    @command_response_parameters.setter  # set ECR.3
    def command_response_parameters(self, tx: TX | tuple[TX] | None):
        """
        id: ECR.3 | len: 65536 | use: O | rpt: *
        ---
        param_type: TX | tuple[TX, ...]: (Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ECR.3
        """
        if isinstance(tx, tuple):
            self._c_data[2] = tx
        else:
            self._c_data[2] = (tx,)
