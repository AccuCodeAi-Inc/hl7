from ...base import HL7Table

"""
HL7 Version: 2.5.1
OCE Edit Code - 0458
Table Type: User
"""


class OceEditCode(HL7Table):
    """
    OCE Edit Code - 0458 // User table type
    - DOT_DOT_DOT
    - INVALID_DIAGNOSIS_CODE
    - NON_COVERED_SERVICE_SUBMITTED_FOR_VERIFICATION_OF_DENIAL
    - NON_COVERED_SERVICE_SUBMITTED_FOR_FI_REVIEW
    - QUESTIONABLE_COVERED_SERVICE
    - ADDITIONAL_PAYMENT_FOR_SERVICE_NOT_PROVIDED_BY_MEDICARE
    - CODE_INDICATES_A_SITE_OF_SERVICE_NOT_INCLUDED_IN_OPPS
    - SERVICE_UNIT_OUT_OF_RANGE_FOR_PROCEDURE
    - MULTIPLE_BILATERAL_PROCEDURES_WITHOUT_MODIFIER_50
    - MULTIPLE_BILATERAL_PROCEDURES_WITH_MODIFIER_50
    - INPATIENT_PROCEDURE
    - MUTUALLY_EXCLUSIVE_PROCEDURE_THAT_IS_NOT_ALLOWED_EVEN_IF_APPROPRIATE_MODIFIER_PRESENT
    - DIAGNOSIS_AND_AGE_CONFLICT
    - COMPONENT_OF_A_COMPREHENSIVE_PROCEDURE_THAT_IS_NOT_ALLOWED_EVEN_IF_APPROPRIATE_MODIFIER_PRESENT
    - MEDICAL_VISIT_ON_SAME_DAY_AS_A_TYPE_T_OR_S_PROCEDURE_WITHOUT_MODIFIER_25
    - INVALID_MODIFIER
    - INVALID_DATE
    - DATE_OUT_OF_OCE_RANGE
    - INVALID_AGE
    - INVALID_SEX
    - ONLY_INCIDENTAL_SERVICES_REPORTED
    - CODE_NOT_RECOGNIZED_BY_MEDICARE_ALTERNATE_CODE_FOR_SAME_SERVICE_AVAILABLE
    - PARTIAL_HOSPITALIZATION_SERVICE_FOR_NON_MENTAL_HEALTH_DIAGNOSIS
    - DIAGNOSIS_AND_SEX_CONFLICT
    - INSUFFICIENT_SERVICES_ON_DAY_OF_PARTIAL_HOSPITALIZATION
    - PARTIAL_HOSPITALIZATION_ON_SAME_DAY_AS_ECT_OR_TYPE_T_PROCEDURE
    - PARTIAL_HOSPITALIZATION_CLAIM_SPANS_3_OR_LESS_DAYS_WITH_IN_SUFFICIENT_SERVICES_OR_ECT_OR_SIGNIFICANT_PROCEDURE_ON_AT_LEAST_ONE_OF_THE_DAYS
    - PARTIAL_HOSPITALIZATION_CLAIM_SPANS_MORE_THAN_3_DAYS_WITH_INSUFFICIENT_NUMBER_OF_DAYS_HAVING_MENTAL_HEALTH_SERVICES
    - PARTIAL_HOSPITALIZATION_CLAIM_SPANS_MORE_THAN_3_DAYS_WITH_INSUFFICIENT_NUMBER_OF_DAYS_MEETING_PARTIAL_HOSPITALIZATION_CRITERIA
    - ONLY_ACTIVITY_THERAPY_AND_OR_OR_OCCUPATIONAL_THERAPY_SERVICES_PROVIDED
    - EXTENSIVE_MENTAL_HEALTH_SERVICES_PROVIDED_ON_DAY_OF_ECT_OR_SIGNIFICANT_PROCEDURE
    - TERMINATED_BILATERAL_PROCEDURE_OR_TERMINATED_PROCEDURE_WITH_UNITS_GREATER_THAN_ONE
    - INCONSISTENCY_BETWEEN_IMPLANTED_DEVICE_AND_IMPLANTATION_PROCEDURE
    - MUTUALLY_EXCLUSIVE_PROCEDURE_THAT_WOULD_BE_ALLOWED_IF_APPROPRIATE_MODIFIER_WERE_PRESENT
    - MEDICARE_SECONDARY_PAYER_ALERT
    - COMPONENT_OF_A_COMPREHENSIVE_PROCEDURE_THAT_WOULD_BE_ALLOWED_IF_APPROPRIATE_MODIFIER_WERE_PRESENT
    - INVALID_REVENUE_CODE
    - MULTIPLE_MEDICAL_VISITS_ON_SAME_DAY_WITH_SAME_REVENUE_CODE_WITHOUT_CONDITION_CODE_G0
    - E_CODE_AS_REASON_FOR_VISIT
    - INVALID_PROCEDURE_CODE
    - PROCEDURE_AND_AGE_CONFLICT
    - PROCEDURE_AND_SEX_CONFLICT
    - NOV_COVERED_SERVICE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0458
    """

    DOT_DOT_DOT = "…"
    """"""
    INVALID_DIAGNOSIS_CODE = "1"
    """Invalid diagnosis code"""
    NON_COVERED_SERVICE_SUBMITTED_FOR_VERIFICATION_OF_DENIAL = "10"
    """Non-covered service submitted for verification of denial (condition code 21 from header information on claim)"""
    NON_COVERED_SERVICE_SUBMITTED_FOR_FI_REVIEW = "11"
    """Non-covered service submitted for FI review (condition code 20 from header information on claim)"""
    QUESTIONABLE_COVERED_SERVICE = "12"
    """Questionable covered service"""
    ADDITIONAL_PAYMENT_FOR_SERVICE_NOT_PROVIDED_BY_MEDICARE = "13"
    """Additional payment for service not provided by Medicare"""
    CODE_INDICATES_A_SITE_OF_SERVICE_NOT_INCLUDED_IN_OPPS = "14"
    """Code indicates a site of service not included in OPPS"""
    SERVICE_UNIT_OUT_OF_RANGE_FOR_PROCEDURE = "15"
    """Service unit out of range for procedure"""
    MULTIPLE_BILATERAL_PROCEDURES_WITHOUT_MODIFIER_50 = "16"
    """Multiple bilateral procedures without modifier 50 (see Appendix A)"""
    MULTIPLE_BILATERAL_PROCEDURES_WITH_MODIFIER_50 = "17"
    """Multiple bilateral procedures with modifier 50 (see Appendix A)"""
    INPATIENT_PROCEDURE = "18"
    """Inpatient procedure"""
    MUTUALLY_EXCLUSIVE_PROCEDURE_THAT_IS_NOT_ALLOWED_EVEN_IF_APPROPRIATE_MODIFIER_PRESENT = "19"
    """Mutually exclusive procedure that is not allowed even if appropriate modifier present"""
    DIAGNOSIS_AND_AGE_CONFLICT = "2"
    """Diagnosis and age conflict"""
    COMPONENT_OF_A_COMPREHENSIVE_PROCEDURE_THAT_IS_NOT_ALLOWED_EVEN_IF_APPROPRIATE_MODIFIER_PRESENT = "20"
    """Component of a comprehensive procedure that is not allowed even if appropriate modifier present"""
    MEDICAL_VISIT_ON_SAME_DAY_AS_A_TYPE_T_OR_S_PROCEDURE_WITHOUT_MODIFIER_25 = "21"
    """Medical visit on same day as a type T or S procedure without modifier 25 (see Appendix B)"""
    INVALID_MODIFIER = "22"
    """Invalid modifier"""
    INVALID_DATE = "23"
    """Invalid date"""
    DATE_OUT_OF_OCE_RANGE = "24"
    """Date out of OCE range"""
    INVALID_AGE = "25"
    """Invalid age"""
    INVALID_SEX = "26"
    """Invalid sex"""
    ONLY_INCIDENTAL_SERVICES_REPORTED = "27"
    """Only incidental services reported"""
    CODE_NOT_RECOGNIZED_BY_MEDICARE_ALTERNATE_CODE_FOR_SAME_SERVICE_AVAILABLE = "28"
    """Code not recognized by Medicare; alternate code for same service available"""
    PARTIAL_HOSPITALIZATION_SERVICE_FOR_NON_MENTAL_HEALTH_DIAGNOSIS = "29"
    """Partial hospitalization service for non-mental health diagnosis"""
    DIAGNOSIS_AND_SEX_CONFLICT = "3"
    """Diagnosis and sex conflict"""
    INSUFFICIENT_SERVICES_ON_DAY_OF_PARTIAL_HOSPITALIZATION = "30"
    """Insufficient services on day of partial hospitalization"""
    PARTIAL_HOSPITALIZATION_ON_SAME_DAY_AS_ECT_OR_TYPE_T_PROCEDURE = "31"
    """Partial hospitalization on same day as ECT or type T procedure"""
    PARTIAL_HOSPITALIZATION_CLAIM_SPANS_3_OR_LESS_DAYS_WITH_IN_SUFFICIENT_SERVICES_OR_ECT_OR_SIGNIFICANT_PROCEDURE_ON_AT_LEAST_ONE_OF_THE_DAYS = "32"
    """Partial hospitalization claim spans 3 or less days with in-sufficient services, or ECT or significant procedure on at least one of the days"""
    PARTIAL_HOSPITALIZATION_CLAIM_SPANS_MORE_THAN_3_DAYS_WITH_INSUFFICIENT_NUMBER_OF_DAYS_HAVING_MENTAL_HEALTH_SERVICES = "33"
    """Partial hospitalization claim spans more than 3 days with insufficient number of days having mental health services"""
    PARTIAL_HOSPITALIZATION_CLAIM_SPANS_MORE_THAN_3_DAYS_WITH_INSUFFICIENT_NUMBER_OF_DAYS_MEETING_PARTIAL_HOSPITALIZATION_CRITERIA = "34"
    """Partial hospitalization claim spans more than 3 days with insufficient number of days meeting partial hospitalization criteria"""
    ONLY_ACTIVITY_THERAPY_AND_OR_OR_OCCUPATIONAL_THERAPY_SERVICES_PROVIDED = "35."
    """Only activity therapy and/or occupational therapy services provided"""
    EXTENSIVE_MENTAL_HEALTH_SERVICES_PROVIDED_ON_DAY_OF_ECT_OR_SIGNIFICANT_PROCEDURE = (
        "36."
    )
    """Extensive mental health services provided on day of ECT or significant procedure"""
    TERMINATED_BILATERAL_PROCEDURE_OR_TERMINATED_PROCEDURE_WITH_UNITS_GREATER_THAN_ONE = "37"
    """Terminated bilateral procedure or terminated procedure with units greater than one"""
    INCONSISTENCY_BETWEEN_IMPLANTED_DEVICE_AND_IMPLANTATION_PROCEDURE = "38."
    """Inconsistency between implanted device and implantation procedure"""
    MUTUALLY_EXCLUSIVE_PROCEDURE_THAT_WOULD_BE_ALLOWED_IF_APPROPRIATE_MODIFIER_WERE_PRESENT = "39."
    """Mutually exclusive procedure that would be allowed if appropriate modifier were present"""
    MEDICARE_SECONDARY_PAYER_ALERT = "4"
    """Medicare secondary payer alert"""
    COMPONENT_OF_A_COMPREHENSIVE_PROCEDURE_THAT_WOULD_BE_ALLOWED_IF_APPROPRIATE_MODIFIER_WERE_PRESENT = "40."
    """Component of a comprehensive procedure that would be allowed if appropriate modifier were present"""
    INVALID_REVENUE_CODE = "41."
    """Invalid revenue code"""
    MULTIPLE_MEDICAL_VISITS_ON_SAME_DAY_WITH_SAME_REVENUE_CODE_WITHOUT_CONDITION_CODE_G0 = "42."
    """Multiple medical visits on same day with same revenue code without condition code G0 (see Appendix B)"""
    E_CODE_AS_REASON_FOR_VISIT = "5"
    """E-code as reason for visit"""
    INVALID_PROCEDURE_CODE = "6"
    """Invalid procedure code"""
    PROCEDURE_AND_AGE_CONFLICT = "7"
    """Procedure and age conflict"""
    PROCEDURE_AND_SEX_CONFLICT = "8"
    """Procedure and sex conflict"""
    NOV_COVERED_SERVICE = "9"
    """Nov-covered service"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OceEditCode.DOT_DOT_DOT: "",
    OceEditCode.INVALID_DIAGNOSIS_CODE: "Invalid diagnosis code",
    OceEditCode.NON_COVERED_SERVICE_SUBMITTED_FOR_VERIFICATION_OF_DENIAL: "Non-covered service submitted for verification of denial (condition code 21 from header information on claim)",
    OceEditCode.NON_COVERED_SERVICE_SUBMITTED_FOR_FI_REVIEW: "Non-covered service submitted for FI review (condition code 20 from header information on claim)",
    OceEditCode.QUESTIONABLE_COVERED_SERVICE: "Questionable covered service",
    OceEditCode.ADDITIONAL_PAYMENT_FOR_SERVICE_NOT_PROVIDED_BY_MEDICARE: "Additional payment for service not provided by Medicare",
    OceEditCode.CODE_INDICATES_A_SITE_OF_SERVICE_NOT_INCLUDED_IN_OPPS: "Code indicates a site of service not included in OPPS",
    OceEditCode.SERVICE_UNIT_OUT_OF_RANGE_FOR_PROCEDURE: "Service unit out of range for procedure",
    OceEditCode.MULTIPLE_BILATERAL_PROCEDURES_WITHOUT_MODIFIER_50: "Multiple bilateral procedures without modifier 50 (see Appendix A)",
    OceEditCode.MULTIPLE_BILATERAL_PROCEDURES_WITH_MODIFIER_50: "Multiple bilateral procedures with modifier 50 (see Appendix A)",
    OceEditCode.INPATIENT_PROCEDURE: "Inpatient procedure",
    OceEditCode.MUTUALLY_EXCLUSIVE_PROCEDURE_THAT_IS_NOT_ALLOWED_EVEN_IF_APPROPRIATE_MODIFIER_PRESENT: "Mutually exclusive procedure that is not allowed even if appropriate modifier present",
    OceEditCode.DIAGNOSIS_AND_AGE_CONFLICT: "Diagnosis and age conflict",
    OceEditCode.COMPONENT_OF_A_COMPREHENSIVE_PROCEDURE_THAT_IS_NOT_ALLOWED_EVEN_IF_APPROPRIATE_MODIFIER_PRESENT: "Component of a comprehensive procedure that is not allowed even if appropriate modifier present",
    OceEditCode.MEDICAL_VISIT_ON_SAME_DAY_AS_A_TYPE_T_OR_S_PROCEDURE_WITHOUT_MODIFIER_25: "Medical visit on same day as a type T or S procedure without modifier 25 (see Appendix B)",
    OceEditCode.INVALID_MODIFIER: "Invalid modifier",
    OceEditCode.INVALID_DATE: "Invalid date",
    OceEditCode.DATE_OUT_OF_OCE_RANGE: "Date out of OCE range",
    OceEditCode.INVALID_AGE: "Invalid age",
    OceEditCode.INVALID_SEX: "Invalid sex",
    OceEditCode.ONLY_INCIDENTAL_SERVICES_REPORTED: "Only incidental services reported",
    OceEditCode.CODE_NOT_RECOGNIZED_BY_MEDICARE_ALTERNATE_CODE_FOR_SAME_SERVICE_AVAILABLE: "Code not recognized by Medicare; alternate code for same service available",
    OceEditCode.PARTIAL_HOSPITALIZATION_SERVICE_FOR_NON_MENTAL_HEALTH_DIAGNOSIS: "Partial hospitalization service for non-mental health diagnosis",
    OceEditCode.DIAGNOSIS_AND_SEX_CONFLICT: "Diagnosis and sex conflict",
    OceEditCode.INSUFFICIENT_SERVICES_ON_DAY_OF_PARTIAL_HOSPITALIZATION: "Insufficient services on day of partial hospitalization",
    OceEditCode.PARTIAL_HOSPITALIZATION_ON_SAME_DAY_AS_ECT_OR_TYPE_T_PROCEDURE: "Partial hospitalization on same day as ECT or type T procedure",
    OceEditCode.PARTIAL_HOSPITALIZATION_CLAIM_SPANS_3_OR_LESS_DAYS_WITH_IN_SUFFICIENT_SERVICES_OR_ECT_OR_SIGNIFICANT_PROCEDURE_ON_AT_LEAST_ONE_OF_THE_DAYS: "Partial hospitalization claim spans 3 or less days with in-sufficient services, or ECT or significant procedure on at least one of the days",
    OceEditCode.PARTIAL_HOSPITALIZATION_CLAIM_SPANS_MORE_THAN_3_DAYS_WITH_INSUFFICIENT_NUMBER_OF_DAYS_HAVING_MENTAL_HEALTH_SERVICES: "Partial hospitalization claim spans more than 3 days with insufficient number of days having mental health services",
    OceEditCode.PARTIAL_HOSPITALIZATION_CLAIM_SPANS_MORE_THAN_3_DAYS_WITH_INSUFFICIENT_NUMBER_OF_DAYS_MEETING_PARTIAL_HOSPITALIZATION_CRITERIA: "Partial hospitalization claim spans more than 3 days with insufficient number of days meeting partial hospitalization criteria",
    OceEditCode.ONLY_ACTIVITY_THERAPY_AND_OR_OR_OCCUPATIONAL_THERAPY_SERVICES_PROVIDED: "Only activity therapy and/or occupational therapy services provided",
    OceEditCode.EXTENSIVE_MENTAL_HEALTH_SERVICES_PROVIDED_ON_DAY_OF_ECT_OR_SIGNIFICANT_PROCEDURE: "Extensive mental health services provided on day of ECT or significant procedure",
    OceEditCode.TERMINATED_BILATERAL_PROCEDURE_OR_TERMINATED_PROCEDURE_WITH_UNITS_GREATER_THAN_ONE: "Terminated bilateral procedure or terminated procedure with units greater than one",
    OceEditCode.INCONSISTENCY_BETWEEN_IMPLANTED_DEVICE_AND_IMPLANTATION_PROCEDURE: "Inconsistency between implanted device and implantation procedure",
    OceEditCode.MUTUALLY_EXCLUSIVE_PROCEDURE_THAT_WOULD_BE_ALLOWED_IF_APPROPRIATE_MODIFIER_WERE_PRESENT: "Mutually exclusive procedure that would be allowed if appropriate modifier were present",
    OceEditCode.MEDICARE_SECONDARY_PAYER_ALERT: "Medicare secondary payer alert",
    OceEditCode.COMPONENT_OF_A_COMPREHENSIVE_PROCEDURE_THAT_WOULD_BE_ALLOWED_IF_APPROPRIATE_MODIFIER_WERE_PRESENT: "Component of a comprehensive procedure that would be allowed if appropriate modifier were present",
    OceEditCode.INVALID_REVENUE_CODE: "Invalid revenue code",
    OceEditCode.MULTIPLE_MEDICAL_VISITS_ON_SAME_DAY_WITH_SAME_REVENUE_CODE_WITHOUT_CONDITION_CODE_G0: "Multiple medical visits on same day with same revenue code without condition code G0 (see Appendix B)",
    OceEditCode.E_CODE_AS_REASON_FOR_VISIT: "E-code as reason for visit",
    OceEditCode.INVALID_PROCEDURE_CODE: "Invalid procedure code",
    OceEditCode.PROCEDURE_AND_AGE_CONFLICT: "Procedure and age conflict",
    OceEditCode.PROCEDURE_AND_SEX_CONFLICT: "Procedure and sex conflict",
    OceEditCode.NOV_COVERED_SERVICE: "Nov-covered service",
}
