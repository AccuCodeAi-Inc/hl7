from ...base import HL7Table

"""
HL7 Version: 2.5.1
Command response - 0387
Table Type: User
"""


class CommandResponse(HL7Table):
    """
    Command response - 0387 // User table type
    - COMMAND_CANNOT_BE_COMPLETED_BECAUSE_OF_ERROR_CONDITION
    - COMMAND_COMPLETED_SUCCESSFULLY
    - COMMAND_CANNOT_BE_COMPLETED_BECAUSE_OF_THE_STATUS_OF_THE_REQUESTED_EQUIPMENT
    - COMMAND_CANNOT_BE_COMPLETED_WITHIN_REQUESTED_COMPLETION_TIME
    - COMMAND_CANNOT_BE_COMPLETED_FOR_UNKNOWN_REASONS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0387
    """

    COMMAND_CANNOT_BE_COMPLETED_BECAUSE_OF_ERROR_CONDITION = (
        "ER"  # See response parameters.
    )
    """Command cannot be completed because of error condition"""
    COMMAND_COMPLETED_SUCCESSFULLY = "OK"
    """Command completed successfully"""
    COMMAND_CANNOT_BE_COMPLETED_BECAUSE_OF_THE_STATUS_OF_THE_REQUESTED_EQUIPMENT = "ST"
    """Command cannot be completed because of the status of the requested equipment"""
    COMMAND_CANNOT_BE_COMPLETED_WITHIN_REQUESTED_COMPLETION_TIME = "TI"
    """Command cannot be completed within requested completion time"""
    COMMAND_CANNOT_BE_COMPLETED_FOR_UNKNOWN_REASONS = "UN"
    """Command cannot be completed for unknown reasons"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CommandResponse.COMMAND_CANNOT_BE_COMPLETED_BECAUSE_OF_ERROR_CONDITION: "Command cannot be completed because of error condition",
    CommandResponse.COMMAND_COMPLETED_SUCCESSFULLY: "Command completed successfully",
    CommandResponse.COMMAND_CANNOT_BE_COMPLETED_BECAUSE_OF_THE_STATUS_OF_THE_REQUESTED_EQUIPMENT: "Command cannot be completed because of the status of the requested equipment",
    CommandResponse.COMMAND_CANNOT_BE_COMPLETED_WITHIN_REQUESTED_COMPLETION_TIME: "Command cannot be completed within requested completion time",
    CommandResponse.COMMAND_CANNOT_BE_COMPLETED_FOR_UNKNOWN_REASONS: "Command cannot be completed for unknown reasons",
}
