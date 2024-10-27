from ...base import HL7Table

"""
HL7 Version: 2.5.1
Result Status - 0123
Table Type: HL7
"""


class ResultStatus(HL7Table):
    """
    Result Status - 0123 // HL7 table type
    - SOME_BUT_NOT_ALL_RESULTS_AVAILABLE
    - CORRECTION_TO_RESULTS
    - FINAL_RESULTS_RESULTS_STORED_AND_VERIFIED_CAN_ONLY_BE_CHANGED_WITH_A_CORRECTED_RESULT
    - NO_RESULTS_AVAILABLE_SPECIMEN_RECEIVED_PROCEDURE_INCOMPLETE
    - ORDER_RECEIVED_SPECIMEN_NOT_YET_RECEIVED
    - PRELIMINARY_A_VERIFIED_EARLY_RESULT_IS_AVAILABLE_FINAL_RESULTS_NOT_YET_OBTAINED
    - RESULTS_STORED_NOT_YET_VERIFIED
    - NO_RESULTS_AVAILABLE_PROCEDURE_SCHEDULED_BUT_NOT_DONE
    - NO_RESULTS_AVAILABLE_ORDER_CANCELED
    - NO_ORDER_ON_RECORD_FOR_THIS_TEST
    - NO_RECORD_OF_THIS_PATIENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0123
    """

    SOME_BUT_NOT_ALL_RESULTS_AVAILABLE = "A"
    """Some, but not all, results available"""
    CORRECTION_TO_RESULTS = "C"
    """Correction to results"""
    FINAL_RESULTS_RESULTS_STORED_AND_VERIFIED_CAN_ONLY_BE_CHANGED_WITH_A_CORRECTED_RESULT = "F"
    """Final results; results stored and verified. Can only be changed with a corrected result."""
    NO_RESULTS_AVAILABLE_SPECIMEN_RECEIVED_PROCEDURE_INCOMPLETE = "I"
    """No results available; specimen received, procedure incomplete"""
    ORDER_RECEIVED_SPECIMEN_NOT_YET_RECEIVED = "O"
    """Order received; specimen not yet received"""
    PRELIMINARY_A_VERIFIED_EARLY_RESULT_IS_AVAILABLE_FINAL_RESULTS_NOT_YET_OBTAINED = (
        "P"
    )
    """Preliminary: A verified early result is available, final results not yet obtained"""
    RESULTS_STORED_NOT_YET_VERIFIED = "R"
    """Results stored; not yet verified"""
    NO_RESULTS_AVAILABLE_PROCEDURE_SCHEDULED_BUT_NOT_DONE = "S"
    """No results available; procedure scheduled, but not done"""
    NO_RESULTS_AVAILABLE_ORDER_CANCELED = "X"
    """No results available; Order canceled."""
    NO_ORDER_ON_RECORD_FOR_THIS_TEST = "Y"
    """No order on record for this test. (Used only on queries)"""
    NO_RECORD_OF_THIS_PATIENT = "Z"
    """No record of this patient. (Used only on queries)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ResultStatus.SOME_BUT_NOT_ALL_RESULTS_AVAILABLE: "Some, but not all, results available",
    ResultStatus.CORRECTION_TO_RESULTS: "Correction to results",
    ResultStatus.FINAL_RESULTS_RESULTS_STORED_AND_VERIFIED_CAN_ONLY_BE_CHANGED_WITH_A_CORRECTED_RESULT: "Final results; results stored and verified. Can only be changed with a corrected result.",
    ResultStatus.NO_RESULTS_AVAILABLE_SPECIMEN_RECEIVED_PROCEDURE_INCOMPLETE: "No results available; specimen received, procedure incomplete",
    ResultStatus.ORDER_RECEIVED_SPECIMEN_NOT_YET_RECEIVED: "Order received; specimen not yet received",
    ResultStatus.PRELIMINARY_A_VERIFIED_EARLY_RESULT_IS_AVAILABLE_FINAL_RESULTS_NOT_YET_OBTAINED: "Preliminary: A verified early result is available, final results not yet obtained",
    ResultStatus.RESULTS_STORED_NOT_YET_VERIFIED: "Results stored; not yet verified",
    ResultStatus.NO_RESULTS_AVAILABLE_PROCEDURE_SCHEDULED_BUT_NOT_DONE: "No results available; procedure scheduled, but not done",
    ResultStatus.NO_RESULTS_AVAILABLE_ORDER_CANCELED: "No results available; Order canceled.",
    ResultStatus.NO_ORDER_ON_RECORD_FOR_THIS_TEST: "No order on record for this test. (Used only on queries)",
    ResultStatus.NO_RECORD_OF_THIS_PATIENT: "No record of this patient. (Used only on queries)",
}
