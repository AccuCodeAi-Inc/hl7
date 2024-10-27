from ...base import HL7Table

"""
HL7 Version: 2.5.1
What subject filter - 0048
Table Type: HL7
"""


class WhatSubjectFilter(HL7Table):
    """
    What subject filter - 0048 // HL7 table type
    - ADVICE_OR_DIAGNOSIS
    - NURSING_UNIT_LOOKUP
    - ACCOUNT_NUMBER_QUERY_RETURN_MATCHING_VISIT
    - MEDICAL_RECORD_NUMBER_QUERY_RETURNS_VISITS_FOR_A_MEDICAL_RECORD_NUMBER
    - PATIENT_NAME_LOOKUP
    - PHYSICIAN_LOOKUP
    - ARN
    - CANCEL_USED_TO_CANCEL_A_QUERY
    - DEMOGRAPHICS
    - FINANCIAL
    - GENERATE_NEW_IDENTIFIER
    - GOALS
    - MOST_RECENT_INPATIENT
    - MOST_RECENT_OUTPATIENT
    - NETWORK_CLOCK
    - NETWORK_STATUS_CHANGE
    - NETWORK_STATISTIC
    - ORDER
    - OTHER
    - PROBLEMS
    - PROCEDURE
    - PHARMACY_ADMINISTRATION_INFORMATION
    - PHARMACY_DISPENSE_INFORMATION
    - PHARMACY_ENCODED_ORDER_INFORMATION
    - RESULT
    - PHARMACY_GIVE_INFORMATION
    - PHARMACY_PRESCRIPTION_INFORMATION
    - ALL_SCHEDULE_RELATED_INFORMATION_INCLUDING_OPEN_SLOTS_BOOKED_SLOTS_BLOCKED_SLOTS
    - BOOKED_SLOTS_ON_THE_IDENTIFIED_SCHEDULE
    - BLOCKED_SLOTS_ON_THE_IDENTIFIED_SCHEDULE
    - FIRST_OPEN_SLOT_ON_THE_IDENTIFIED_SCHEDULE_AFTER_THE_START_DATE_OR_TIEM
    - OPEN_SLOTS_ON_THE_IDENTIFIED_SCHEDULE_BETWEEN_THE_BEGIN_AND_END_OF_THE_START_DATE_OR_TIME_RANGE
    - TIME_SLOTS_AVAILABLE_FOR_A_SINGLE_APPOINTMENT
    - TIME_SLOTS_AVAILABLE_FOR_A_RECURRING_APPOINTMENT
    - STATUS
    - VACCINE_INFORMATION
    - GET_CROSS_REFERENCED_IDENTIFIERS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0048
    """

    ADVICE_OR_DIAGNOSIS = "ADV"
    """Advice/diagnosis"""
    NURSING_UNIT_LOOKUP = "ANU"
    """Nursing unit lookup (returns patients in beds, excluding empty beds)"""
    ACCOUNT_NUMBER_QUERY_RETURN_MATCHING_VISIT = "APA"
    """Account number query, return matching visit"""
    MEDICAL_RECORD_NUMBER_QUERY_RETURNS_VISITS_FOR_A_MEDICAL_RECORD_NUMBER = "APM"
    """Medical record number query, returns visits for a medical record number"""
    PATIENT_NAME_LOOKUP = "APN"
    """Patient name lookup"""
    PHYSICIAN_LOOKUP = "APP"
    """Physician lookup"""
    ARN = "ARN"
    """Nursing unit lookup (returns patients in beds, including empty beds)"""
    CANCEL_USED_TO_CANCEL_A_QUERY = "CAN"
    """Cancel. Used to cancel a query"""
    DEMOGRAPHICS = "DEM"
    """Demographics"""
    FINANCIAL = "FIN"
    """Financial"""
    GENERATE_NEW_IDENTIFIER = "GID"
    """Generate new identifier"""
    GOALS = "GOL"
    """Goals"""
    MOST_RECENT_INPATIENT = "MRI"
    """Most recent inpatient"""
    MOST_RECENT_OUTPATIENT = "MRO"
    """Most recent outpatient"""
    NETWORK_CLOCK = "NCK"
    """Network clock"""
    NETWORK_STATUS_CHANGE = "NSC"
    """Network status change"""
    NETWORK_STATISTIC = "NST"
    """Network statistic"""
    ORDER = "ORD"
    """Order"""
    OTHER = "OTH"
    """Other"""
    PROBLEMS = "PRB"
    """Problems"""
    PROCEDURE = "PRO"
    """Procedure"""
    PHARMACY_ADMINISTRATION_INFORMATION = "RAR"
    """Pharmacy administration information"""
    PHARMACY_DISPENSE_INFORMATION = "RDR"
    """Pharmacy dispense information"""
    PHARMACY_ENCODED_ORDER_INFORMATION = "RER"
    """Pharmacy encoded order information"""
    RESULT = "RES"
    """Result"""
    PHARMACY_GIVE_INFORMATION = "RGR"
    """Pharmacy give information"""
    PHARMACY_PRESCRIPTION_INFORMATION = "ROR"
    """Pharmacy prescription information"""
    ALL_SCHEDULE_RELATED_INFORMATION_INCLUDING_OPEN_SLOTS_BOOKED_SLOTS_BLOCKED_SLOTS = (
        "SAL"
    )
    """All schedule related information, including open slots, booked slots, blocked slots"""
    BOOKED_SLOTS_ON_THE_IDENTIFIED_SCHEDULE = "SBK"
    """Booked slots on the identified schedule"""
    BLOCKED_SLOTS_ON_THE_IDENTIFIED_SCHEDULE = "SBL"
    """Blocked slots on the identified schedule"""
    FIRST_OPEN_SLOT_ON_THE_IDENTIFIED_SCHEDULE_AFTER_THE_START_DATE_OR_TIEM = "SOF"
    """First open slot on the identified schedule after the start date/tiem"""
    OPEN_SLOTS_ON_THE_IDENTIFIED_SCHEDULE_BETWEEN_THE_BEGIN_AND_END_OF_THE_START_DATE_OR_TIME_RANGE = "SOP"
    """Open slots on the identified schedule between the begin and end of the start date/time range"""
    TIME_SLOTS_AVAILABLE_FOR_A_SINGLE_APPOINTMENT = "SSA"
    """Time slots available for a single appointment"""
    TIME_SLOTS_AVAILABLE_FOR_A_RECURRING_APPOINTMENT = "SSR"
    """Time slots available for a recurring appointment"""
    STATUS = "STA"
    """Status"""
    VACCINE_INFORMATION = "VXI"
    """Vaccine Information"""
    GET_CROSS_REFERENCED_IDENTIFIERS = "XID"
    """Get cross-referenced identifiers"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    WhatSubjectFilter.ADVICE_OR_DIAGNOSIS: "Advice/diagnosis",
    WhatSubjectFilter.NURSING_UNIT_LOOKUP: "Nursing unit lookup (returns patients in beds, excluding empty beds)",
    WhatSubjectFilter.ACCOUNT_NUMBER_QUERY_RETURN_MATCHING_VISIT: "Account number query, return matching visit",
    WhatSubjectFilter.MEDICAL_RECORD_NUMBER_QUERY_RETURNS_VISITS_FOR_A_MEDICAL_RECORD_NUMBER: "Medical record number query, returns visits for a medical record number",
    WhatSubjectFilter.PATIENT_NAME_LOOKUP: "Patient name lookup",
    WhatSubjectFilter.PHYSICIAN_LOOKUP: "Physician lookup",
    WhatSubjectFilter.ARN: "Nursing unit lookup (returns patients in beds, including empty beds)",
    WhatSubjectFilter.CANCEL_USED_TO_CANCEL_A_QUERY: "Cancel. Used to cancel a query",
    WhatSubjectFilter.DEMOGRAPHICS: "Demographics",
    WhatSubjectFilter.FINANCIAL: "Financial",
    WhatSubjectFilter.GENERATE_NEW_IDENTIFIER: "Generate new identifier",
    WhatSubjectFilter.GOALS: "Goals",
    WhatSubjectFilter.MOST_RECENT_INPATIENT: "Most recent inpatient",
    WhatSubjectFilter.MOST_RECENT_OUTPATIENT: "Most recent outpatient",
    WhatSubjectFilter.NETWORK_CLOCK: "Network clock",
    WhatSubjectFilter.NETWORK_STATUS_CHANGE: "Network status change",
    WhatSubjectFilter.NETWORK_STATISTIC: "Network statistic",
    WhatSubjectFilter.ORDER: "Order",
    WhatSubjectFilter.OTHER: "Other",
    WhatSubjectFilter.PROBLEMS: "Problems",
    WhatSubjectFilter.PROCEDURE: "Procedure",
    WhatSubjectFilter.PHARMACY_ADMINISTRATION_INFORMATION: "Pharmacy administration information",
    WhatSubjectFilter.PHARMACY_DISPENSE_INFORMATION: "Pharmacy dispense information",
    WhatSubjectFilter.PHARMACY_ENCODED_ORDER_INFORMATION: "Pharmacy encoded order information",
    WhatSubjectFilter.RESULT: "Result",
    WhatSubjectFilter.PHARMACY_GIVE_INFORMATION: "Pharmacy give information",
    WhatSubjectFilter.PHARMACY_PRESCRIPTION_INFORMATION: "Pharmacy prescription information",
    WhatSubjectFilter.ALL_SCHEDULE_RELATED_INFORMATION_INCLUDING_OPEN_SLOTS_BOOKED_SLOTS_BLOCKED_SLOTS: "All schedule related information, including open slots, booked slots, blocked slots",
    WhatSubjectFilter.BOOKED_SLOTS_ON_THE_IDENTIFIED_SCHEDULE: "Booked slots on the identified schedule",
    WhatSubjectFilter.BLOCKED_SLOTS_ON_THE_IDENTIFIED_SCHEDULE: "Blocked slots on the identified schedule",
    WhatSubjectFilter.FIRST_OPEN_SLOT_ON_THE_IDENTIFIED_SCHEDULE_AFTER_THE_START_DATE_OR_TIEM: "First open slot on the identified schedule after the start date/tiem",
    WhatSubjectFilter.OPEN_SLOTS_ON_THE_IDENTIFIED_SCHEDULE_BETWEEN_THE_BEGIN_AND_END_OF_THE_START_DATE_OR_TIME_RANGE: "Open slots on the identified schedule between the begin and end of the start date/time range",
    WhatSubjectFilter.TIME_SLOTS_AVAILABLE_FOR_A_SINGLE_APPOINTMENT: "Time slots available for a single appointment",
    WhatSubjectFilter.TIME_SLOTS_AVAILABLE_FOR_A_RECURRING_APPOINTMENT: "Time slots available for a recurring appointment",
    WhatSubjectFilter.STATUS: "Status",
    WhatSubjectFilter.VACCINE_INFORMATION: "Vaccine Information",
    WhatSubjectFilter.GET_CROSS_REFERENCED_IDENTIFIERS: "Get cross-referenced identifiers",
}
