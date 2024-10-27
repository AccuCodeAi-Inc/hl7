from ...base import HL7Table

"""
HL7 Version: 2.5.1
BP Observation Status Codes Interpretation - 0511
Table Type: HL7
"""


class BpObservationStatusCodesInterpretation(HL7Table):
    """
    BP Observation Status Codes Interpretation - 0511 // HL7 table type
    - RECORD_COMING_OVER_IS_A_CORRECTION_AND_THUS_REPLACES_A_FINAL_STATUS
    - DELETES_THE_BPX_RECORD
    - FINAL_STATUS_CAN_ONLY_BE_CHANGED_WITH_A_CORRECTED_STATUS
    - ORDER_DETAIL_DESCRIPTION_ONLY
    - PRELIMINARY_STATUS
    - POST_ORIGINAL_AS_WRONG_E_G_TRANSMITTED_FOR_WRONG_PATIENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0511
    """

    RECORD_COMING_OVER_IS_A_CORRECTION_AND_THUS_REPLACES_A_FINAL_STATUS = "C"
    """Record coming over is a correction and thus replaces a final status"""
    DELETES_THE_BPX_RECORD = "D"
    """Deletes the BPX record"""
    FINAL_STATUS_CAN_ONLY_BE_CHANGED_WITH_A_CORRECTED_STATUS = "F"
    """Final status; Can only be changed with a corrected status"""
    ORDER_DETAIL_DESCRIPTION_ONLY = "O"
    """Order detail description only (no status)"""
    PRELIMINARY_STATUS = "P"
    """Preliminary status"""
    POST_ORIGINAL_AS_WRONG_E_G_TRANSMITTED_FOR_WRONG_PATIENT = "W"
    """Post original as wrong, e.g., transmitted for wrong patient"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    BpObservationStatusCodesInterpretation.RECORD_COMING_OVER_IS_A_CORRECTION_AND_THUS_REPLACES_A_FINAL_STATUS: "Record coming over is a correction and thus replaces a final status",
    BpObservationStatusCodesInterpretation.DELETES_THE_BPX_RECORD: "Deletes the BPX record",
    BpObservationStatusCodesInterpretation.FINAL_STATUS_CAN_ONLY_BE_CHANGED_WITH_A_CORRECTED_STATUS: "Final status; Can only be changed with a corrected status",
    BpObservationStatusCodesInterpretation.ORDER_DETAIL_DESCRIPTION_ONLY: "Order detail description only (no status)",
    BpObservationStatusCodesInterpretation.PRELIMINARY_STATUS: "Preliminary status",
    BpObservationStatusCodesInterpretation.POST_ORIGINAL_AS_WRONG_E_G_TRANSMITTED_FOR_WRONG_PATIENT: "Post original as wrong, e.g., transmitted for wrong patient",
}
