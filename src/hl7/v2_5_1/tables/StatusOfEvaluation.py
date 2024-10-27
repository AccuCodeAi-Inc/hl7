from ...base import HL7Table

"""
HL7 Version: 2.5.1
Status of Evaluation - 0247
Table Type: HL7
"""


class StatusOfEvaluation(HL7Table):
    """
    Status of Evaluation - 0247 // HL7 table type
    - EVALUATION_ANTICIPATED_BUT_NOT_YET_BEGUN
    - PRODUCT_RECEIVED_IN_CONDITION_WHICH_MADE_ANALYSIS_IMPOSSIBLE
    - PRODUCT_DISCARDED_UNABLE_TO_FOLLOW_UP
    - PRODUCT_REMAINS_IMPLANTED_UNABLE_TO_FOLLOW_UP
    - PROBLEM_ALREADY_KNOWN_NO_EVALUATION_NECESSARY
    - OTHER
    - EVALUATION_IN_PROGRESS
    - PRODUCT_UNDER_QUARANTINE_UNABLE_TO_FOLLOW_UP
    - PRODUCT_UNDER_RECALL_OR_CORRECTIVE_ACTION
    - PRODUCT_UNAVAILABLE_FOR_FOLLOW_UP_INVESTIGATION
    - PRODUCT_NOT_MADE_BY_COMPANY
    - EVALUATION_COMPLETED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0247
    """

    EVALUATION_ANTICIPATED_BUT_NOT_YET_BEGUN = "A"
    """Evaluation anticipated, but not yet begun"""
    PRODUCT_RECEIVED_IN_CONDITION_WHICH_MADE_ANALYSIS_IMPOSSIBLE = "C"
    """Product received in condition which made analysis impossible"""
    PRODUCT_DISCARDED_UNABLE_TO_FOLLOW_UP = "D"
    """Product discarded -- unable to follow up"""
    PRODUCT_REMAINS_IMPLANTED_UNABLE_TO_FOLLOW_UP = "I"
    """Product remains implanted -- unable to follow up"""
    PROBLEM_ALREADY_KNOWN_NO_EVALUATION_NECESSARY = "K"
    """Problem already known, no evaluation necessary"""
    OTHER = "O"
    """Other"""
    EVALUATION_IN_PROGRESS = "P"
    """Evaluation in progress"""
    PRODUCT_UNDER_QUARANTINE_UNABLE_TO_FOLLOW_UP = "Q"
    """Product under quarantine -- unable to follow up"""
    PRODUCT_UNDER_RECALL_OR_CORRECTIVE_ACTION = "R"
    """Product under recall/corrective action"""
    PRODUCT_UNAVAILABLE_FOR_FOLLOW_UP_INVESTIGATION = "U"
    """Product unavailable for follow up investigation"""
    PRODUCT_NOT_MADE_BY_COMPANY = "X"
    """Product not made by company"""
    EVALUATION_COMPLETED = "Y"
    """Evaluation completed"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    StatusOfEvaluation.EVALUATION_ANTICIPATED_BUT_NOT_YET_BEGUN: "Evaluation anticipated, but not yet begun",
    StatusOfEvaluation.PRODUCT_RECEIVED_IN_CONDITION_WHICH_MADE_ANALYSIS_IMPOSSIBLE: "Product received in condition which made analysis impossible",
    StatusOfEvaluation.PRODUCT_DISCARDED_UNABLE_TO_FOLLOW_UP: "Product discarded -- unable to follow up",
    StatusOfEvaluation.PRODUCT_REMAINS_IMPLANTED_UNABLE_TO_FOLLOW_UP: "Product remains implanted -- unable to follow up",
    StatusOfEvaluation.PROBLEM_ALREADY_KNOWN_NO_EVALUATION_NECESSARY: "Problem already known, no evaluation necessary",
    StatusOfEvaluation.OTHER: "Other",
    StatusOfEvaluation.EVALUATION_IN_PROGRESS: "Evaluation in progress",
    StatusOfEvaluation.PRODUCT_UNDER_QUARANTINE_UNABLE_TO_FOLLOW_UP: "Product under quarantine -- unable to follow up",
    StatusOfEvaluation.PRODUCT_UNDER_RECALL_OR_CORRECTIVE_ACTION: "Product under recall/corrective action",
    StatusOfEvaluation.PRODUCT_UNAVAILABLE_FOR_FOLLOW_UP_INVESTIGATION: "Product unavailable for follow up investigation",
    StatusOfEvaluation.PRODUCT_NOT_MADE_BY_COMPANY: "Product not made by company",
    StatusOfEvaluation.EVALUATION_COMPLETED: "Evaluation completed",
}
