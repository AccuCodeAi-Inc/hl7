from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..tables.CommandResponse import CommandResponse
from ..tables.RemoteControlCommand import RemoteControlCommand


"""
Interaction Status Detail - ISD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ISD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ISD,
    CE, NM
)

isd = ISD(  #  - The interaction detail segment contains information about the status of specific interaction (e
    reference_interaction_number=nm,  # NM(...)  # Required.
    interaction_type_identifier=None,  # CE(...) 
    interaction_active_state=ce,  # CE(...)  # Required.
)

-----END SEGMENT::ISD TEMPLATE-----
"""


class ISD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ISD"""
    _hl7_name = """Interaction Status Detail"""
    _hl7_description = """The interaction detail segment contains information about the status of specific interaction (e"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ISD"
    _c_length = (20, 250, 250,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("R", "O", "R",)
    _c_components = (NM, CE, CE,)
    _c_aliases = ("ISD.1", "ISD.2", "ISD.3",)
    _c_names = ("Reference Interaction Number (unique identifier)", "Interaction Type Identifier", "Interaction Active State",)
    _c_attrs = ("reference_interaction_number", "interaction_type_identifier", "interaction_active_state",)
    # fmt: on

    def __init__(
        self,
        reference_interaction_number: NM,  # ISD.1
        interaction_active_state: CommandResponse | CE,  # ISD.3
        interaction_type_identifier: RemoteControlCommand | CE | None = None,  # ISD.2
    ):
        """
        Interaction Status Detail - `ISD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ISD>`_
        The interaction detail segment contains information about the status of specific interaction (e.g., processing) on the specific equipment.

        :param reference_interaction_number: Numeric (id: ISD.1 | len: 20 | use: R | rpt: 1)
        :param interaction_type_identifier: Coded Element (id: ISD.2 | len: 250 | use: O | rpt: 1)
        :param interaction_active_state: Coded Element (id: ISD.3 | len: 250 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.reference_interaction_number = reference_interaction_number
        self.interaction_type_identifier = interaction_type_identifier
        self.interaction_active_state = interaction_active_state

    @property  # get ISD.1
    def reference_interaction_number(self) -> NM:
        """
        id: ISD.1 | len: 20 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ISD.1
        """
        return self._c_data[0][0]

    @reference_interaction_number.setter  # set ISD.1
    def reference_interaction_number(self, nm: NM):
        """
        id: ISD.1 | len: 20 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ISD.1
        """
        self._c_data[0] = (nm,)

    @property  # get ISD.2
    def interaction_type_identifier(self) -> RemoteControlCommand | None:
        """
        id: ISD.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ISD.2
        """
        return self._c_data[1][0]

    @interaction_type_identifier.setter  # set ISD.2
    def interaction_type_identifier(
        self, remote_control_command: RemoteControlCommand | None
    ):
        """
        id: ISD.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ISD.2
        """
        self._c_data[1] = (remote_control_command,)

    @property  # get ISD.3
    def interaction_active_state(self) -> CommandResponse:
        """
        id: ISD.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ISD.3
        """
        return self._c_data[2][0]

    @interaction_active_state.setter  # set ISD.3
    def interaction_active_state(self, command_response: CommandResponse):
        """
        id: ISD.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ISD.3
        """
        self._c_data[2] = (command_response,)
