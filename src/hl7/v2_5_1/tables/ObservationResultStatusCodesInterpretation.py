from ...base import HL7Table

"""
HL7 Version: 2.5.1
Observation result status codes interpretation - 0085
Table Type: HL7
"""


class ObservationResultStatusCodesInterpretation(HL7Table):
    """
    Observation result status codes interpretation - 0085 // HL7 table type
    - RECORD_COMING_OVER_IS_A_CORRECTION_AND_THUS_REPLACES_A_FINAL_RESULT
    - DELETES_THE_OBX_RECORD
    - FINAL_RESULTS_CAN_ONLY_BE_CHANGED_WITH_A_CORRECTED_RESULT
    - SPECIMEN_IN_LAB_RESULTS_PENDING
    - NOT_ASKED_USED_TO_AFFIRMATIVELY_DOCUMENT_THAT_THE_OBSERVATION_IDENTIFIED_IN_THE_OBX_WAS_NOT_SOUGHT_WHEN_THE_UNIVERSAL_SERVICE_ID_IN_OBR_4_IMPLIES_THAT_IT_WOULD_BE_SOUGHT
    - ORDER_DETAIL_DESCRIPTION_ONLY
    - PRELIMINARY_RESULTS
    - RESULTS_ENTERED_NOT_VERIFIED
    - PARTIAL_RESULTS
    - RESULTS_STATUS_CHANGE_TO_FINAL_WITHOUT_RETRANSMITTING_RESULTS_ALREADY_SENT_AS_PRELIMINARY_E_G_RADIOLOGY_CHANGES_STATUS_FROM_PRELIMINARY_TO_FINAL
    - POST_ORIGINAL_AS_WRONG_E_G_TRANSMITTED_FOR_WRONG_PATIENT
    - RESULTS_CANNOT_BE_OBTAINED_FOR_THIS_OBSERVATION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0085
    """

    RECORD_COMING_OVER_IS_A_CORRECTION_AND_THUS_REPLACES_A_FINAL_RESULT = "C"
    """Record coming over is a correction and thus replaces a final result"""
    DELETES_THE_OBX_RECORD = "D"
    """Deletes the OBX record"""
    FINAL_RESULTS_CAN_ONLY_BE_CHANGED_WITH_A_CORRECTED_RESULT = "F"
    """Final results; Can only be changed with a corrected result."""
    SPECIMEN_IN_LAB_RESULTS_PENDING = "I"
    """Specimen in lab; results pending"""
    NOT_ASKED_USED_TO_AFFIRMATIVELY_DOCUMENT_THAT_THE_OBSERVATION_IDENTIFIED_IN_THE_OBX_WAS_NOT_SOUGHT_WHEN_THE_UNIVERSAL_SERVICE_ID_IN_OBR_4_IMPLIES_THAT_IT_WOULD_BE_SOUGHT = "N"
    """Not asked; used to affirmatively document that the observation identified in the OBX was not sought when the universal service ID in OBR-4 implies that it would be sought."""
    ORDER_DETAIL_DESCRIPTION_ONLY = "O"
    """Order detail description only (no result)"""
    PRELIMINARY_RESULTS = "P"
    """Preliminary results"""
    RESULTS_ENTERED_NOT_VERIFIED = "R"
    """Results entered -- not verified"""
    PARTIAL_RESULTS = "S"
    """Partial results"""
    RESULTS_STATUS_CHANGE_TO_FINAL_WITHOUT_RETRANSMITTING_RESULTS_ALREADY_SENT_AS_PRELIMINARY_E_G_RADIOLOGY_CHANGES_STATUS_FROM_PRELIMINARY_TO_FINAL = "U"
    """Results status change to final without retransmitting results already sent as preliminary. E.g., radiology changes status from preliminary to final"""
    POST_ORIGINAL_AS_WRONG_E_G_TRANSMITTED_FOR_WRONG_PATIENT = "W"
    """Post original as wrong, e.g., transmitted for wrong patient"""
    RESULTS_CANNOT_BE_OBTAINED_FOR_THIS_OBSERVATION = "X"
    """Results cannot be obtained for this observation"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ObservationResultStatusCodesInterpretation.RECORD_COMING_OVER_IS_A_CORRECTION_AND_THUS_REPLACES_A_FINAL_RESULT: "Record coming over is a correction and thus replaces a final result",
    ObservationResultStatusCodesInterpretation.DELETES_THE_OBX_RECORD: "Deletes the OBX record",
    ObservationResultStatusCodesInterpretation.FINAL_RESULTS_CAN_ONLY_BE_CHANGED_WITH_A_CORRECTED_RESULT: "Final results; Can only be changed with a corrected result.",
    ObservationResultStatusCodesInterpretation.SPECIMEN_IN_LAB_RESULTS_PENDING: "Specimen in lab; results pending",
    ObservationResultStatusCodesInterpretation.NOT_ASKED_USED_TO_AFFIRMATIVELY_DOCUMENT_THAT_THE_OBSERVATION_IDENTIFIED_IN_THE_OBX_WAS_NOT_SOUGHT_WHEN_THE_UNIVERSAL_SERVICE_ID_IN_OBR_4_IMPLIES_THAT_IT_WOULD_BE_SOUGHT: "Not asked; used to affirmatively document that the observation identified in the OBX was not sought when the universal service ID in OBR-4 implies that it would be sought.",
    ObservationResultStatusCodesInterpretation.ORDER_DETAIL_DESCRIPTION_ONLY: "Order detail description only (no result)",
    ObservationResultStatusCodesInterpretation.PRELIMINARY_RESULTS: "Preliminary results",
    ObservationResultStatusCodesInterpretation.RESULTS_ENTERED_NOT_VERIFIED: "Results entered -- not verified",
    ObservationResultStatusCodesInterpretation.PARTIAL_RESULTS: "Partial results",
    ObservationResultStatusCodesInterpretation.RESULTS_STATUS_CHANGE_TO_FINAL_WITHOUT_RETRANSMITTING_RESULTS_ALREADY_SENT_AS_PRELIMINARY_E_G_RADIOLOGY_CHANGES_STATUS_FROM_PRELIMINARY_TO_FINAL: "Results status change to final without retransmitting results already sent as preliminary. E.g., radiology changes status from preliminary to final",
    ObservationResultStatusCodesInterpretation.POST_ORIGINAL_AS_WRONG_E_G_TRANSMITTED_FOR_WRONG_PATIENT: "Post original as wrong, e.g., transmitted for wrong patient",
    ObservationResultStatusCodesInterpretation.RESULTS_CANNOT_BE_OBTAINED_FOR_THIS_OBSERVATION: "Results cannot be obtained for this observation",
}
