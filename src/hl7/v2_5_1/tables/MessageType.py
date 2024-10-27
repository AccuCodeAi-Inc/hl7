from ...base import HL7Table

"""
HL7 Version: 2.5.1
Message type - 0076
Table Type: HL7
"""


class MessageType(HL7Table):
    """
    Message type - 0076 // HL7 table type
    - GENERAL_ACKNOWLEDGMENT_MESSAGE
    - ADT_RESPONSE
    - ADT_MESSAGE
    - ADD_OR_CHANGE_BILLING_ACCOUNT
    - BLOOD_PRODUCT_DISPENSE_STATUS_MESSAGE
    - BLOOD_PRODUCT_DISPENSE_STATUS_ACKNOWLEDGEMENT_MESSAGE
    - BLOOD_PRODUCT_TRANSFUSION_OR_DISPOSITION_ACKNOWLEDGEMENT_MESSAGE
    - BLOOD_PRODUCT_TRANSFUSION_OR_DISPOSITION_MESSAGE
    - CLINICAL_STUDY_REGISTRATION_MESSAGE
    - UNSOLICITED_STUDY_DATA_MESSAGE
    - DETAIL_FINANCIAL_TRANSACTIONS
    - DOCUMENT_RESPONSE
    - DISPLAY_RESPONSE
    - AUTOMATED_EQUIPMENT_COMMAND_MESSAGE
    - AUTOMATED_EQUIPMENT_NOTIFICATION_MESSAGE
    - AUTOMATED_EQUIPMENT_RESPONSE_MESSAGE
    - ENHANCED_DISPLAY_RESPONSE
    - EMBEDDED_QUERY_LANGUAGE_QUERY
    - EVENT_REPLAY_RESPONSE
    - AUTOMATED_EQUIPMENT_STATUS_UPDATE_ACKNOWLEDGMENT_MESSAGE
    - AUTOMATED_EQUIPMENT_STATUS_UPDATE_MESSAGE
    - AUTOMATED_EQUIPMENT_INVENTORY_REQUEST_MESSAGE
    - AUTOMATED_EQUIPMENT_INVENTORY_UPDATE_MESSAGE
    - AUTOMATED_EQUIPMENT_LOG_OR_SERVICE_REQUEST_MESSAGE
    - AUTOMATED_EQUIPMENT_LOG_OR_SERVICE_UPDATE_MESSAGE
    - DELAYED_ACKNOWLEDGMENT
    - MEDICAL_DOCUMENT_MANAGEMENT
    - MASTER_FILES_DELAYED_APPLICATION_ACKNOWLEDGMENT
    - MASTER_FILES_APPLICATION_ACKNOWLEDGMENT
    - MASTER_FILES_NOTIFICATION
    - MASTER_FILES_QUERY
    - MASTER_FILES_RESPONSE
    - APPLICATION_MANAGEMENT_DATA_MESSAGE
    - APPLICATION_MANAGEMENT_QUERY_MESSAGE
    - APPLICATION_MANAGEMENT_RESPONSE_MESSAGE
    - BLOOD_PRODUCT_ORDER_MESSAGE
    - DIETARY_ORDER
    - GENERAL_CLINICAL_ORDER_MESSAGE
    - IMAGING_ORDER
    - LABORATORY_ORDER_MESSAGE
    - NON_STOCK_REQUISITION_ORDER_MESSAGE
    - PHARMACY_OR_TREATMENT_ORDER_MESSAGE
    - STOCK_REQUISITION_ORDER_MESSAGE
    - BLOOD_PRODUCT_ORDER_ACKNOWLEDGEMENT_MESSAGE
    - DIETARY_ORDER_ACKNOWLEDGMENT_MESSAGE
    - QUERY_FOR_RESULTS_OF_OBSERVATION
    - GENERAL_CLINICAL_ORDER_ACKNOWLEDGMENT_MESSAGE
    - IMAGING_ORDER_ACKNOWLEDGEMENT_MESSAGE
    - LABORATORY_ACKNOWLEDGMENT_MESSAGE
    - ORM
    - NON_STOCK_REQUISITION_GENERAL_ORDER_ACKNOWLEDGMENT_MESSAGE
    - PHARMACY_OR_TREATMENT_ORDER_ACKNOWLEDGMENT_MESSAGE
    - GENERAL_ORDER_RESPONSE_MESSAGE_RESPONSE_TO_ANY_ORM
    - STOCK_REQUISITION_ORDER_ACKNOWLEDGMENT_MESSAGE
    - UNSOLICITED_TRANSMISSION_OF_AN_OBSERVATION_MESSAGE
    - QUERY_RESPONSE_FOR_ORDER_STATUS
    - OSR
    - UNSOLICITED_LABORATORY_OBSERVATION_MESSAGE
    - PRODUCT_EXPERIENCE_MESSAGE
    - PATIENT_GOAL_MESSAGE
    - PATIENT_INSURANCE_INFORMATION
    - ADD_PERSONNEL_RECORD
    - PATIENT_PATHWAY_MESSAGE
    - PPP
    - PATIENT_PROBLEM_MESSAGE
    - PATIENT_PATHWAY_GOAL_ORIENTED_RESPONSE
    - PATIENT_GOAL_RESPONSE
    - PATIENT_PROBLEM_RESPONSE
    - PATIENT_PATHWAY_PROBLEM_ORIENTED_RESPONSE
    - QUERY_BY_PARAMETER
    - DEFERRED_QUERY
    - CANCEL_QUERY
    - QUERY_ORIGINAL_MODE
    - CREATE_SUBSCRIPTION
    - CANCEL_SUBSCRIPTION_OR_ACKNOWLEDGE_MESSAGE
    - QUERY_FOR_PREVIOUS_EVENTS
    - PHARMACY_OR_TREATMENT_ADMINISTRATION_INFORMATION
    - PHARMACY_OR_TREATMENT_ADMINISTRATION_MESSAGE
    - RETURN_CLINICAL_INFORMATION
    - RETURN_CLINICAL_LIST
    - PHARMACY_OR_TREATMENT_ENCODED_ORDER_MESSAGE
    - PHARMACY_OR_TREATMENT_DISPENSE_INFORMATION
    - PHARMACY_OR_TREATMENT_DISPENSE_MESSAGE
    - DISPLAY_BASED_RESPONSE
    - PATIENT_REFERRAL
    - PHARMACY_OR_TREATMENT_ENCODED_ORDER_INFORMATION
    - PHARMACY_OR_TREATMENT_DOSE_INFORMATION
    - PHARMACY_OR_TREATMENT_GIVE_MESSAGE
    - PHARMACY_OR_TREATMENT_ORDER_RESPONSE
    - RETURN_PATIENT_AUTHORIZATION
    - RETURN_PATIENT_INFORMATION
    - RETURN_PATIENT_DISPLAY_LIST
    - RETURN_PATIENT_LIST
    - REQUEST_PATIENT_AUTHORIZATION
    - REQUEST_CLINICAL_INFORMATION
    - REQUEST_PATIENT_INFORMATION
    - REQUEST_PATIENT_DEMOGRAPHICS
    - EVENT_REPLAY_QUERY
    - PHARMACY_OR_TREATMENT_ADMINISTRATION_ACKNOWLEDGMENT_MESSAGE
    - PHARMACY_OR_TREATMENT_DISPENSE_ACKNOWLEDGMENT_MESSAGE
    - PHARMACY_OR_TREATMENT_ENCODED_ORDER_ACKNOWLEDGMENT_MESSAGE
    - PHARMACY_OR_TREATMENT_GIVE_ACKNOWLEDGMENT_MESSAGE
    - RETURN_REFERRAL_INFORMATION
    - SEGMENT_PATTERN_RESPONSE
    - TABULAR_RESPONSE
    - SCHEDULE_INFORMATION_UNSOLICITED
    - STORED_PROCEDURE_REQUEST
    - SCHEDULE_QUERY_MESSAGE
    - SCHEDULE_QUERY_RESPONSE
    - SCHEDULE_REQUEST_MESSAGE
    - SCHEDULED_REQUEST_RESPONSE
    - SPECIMEN_STATUS_REQUEST_MESSAGE
    - SPECIMEN_STATUS_UPDATE_MESSAGE
    - SUMMARY_PRODUCT_EXPERIENCE_REPORT
    - TABULAR_DATA_RESPONSE
    - AUTOMATED_EQUIPMENT_TEST_CODE_SETTINGS_REQUEST_MESSAGE
    - AUTOMATED_EQUIPMENT_TEST_CODE_SETTINGS_UPDATE_MESSAGE
    - UNSOLICITED_DISPLAY_UPDATE_MESSAGE
    - VIRTUAL_TABLE_QUERY
    - QUERY_FOR_VACCINATION_RECORD
    - VACCINATION_RECORD_RESPONSE
    - UNSOLICITED_VACCINATION_RECORD_UPDATE
    - RESPONSE_FOR_VACCINATION_QUERY_WITH_MULTIPLE_PID_MATCHES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0076
    """

    GENERAL_ACKNOWLEDGMENT_MESSAGE = "ACK"  # 2
    """General acknowledgment message"""
    ADT_RESPONSE = "ADR"  # 3
    """ADT response"""
    ADT_MESSAGE = "ADT"  # 3
    """ADT message"""
    ADD_OR_CHANGE_BILLING_ACCOUNT = "BAR"  # 6
    """Add/change billing account"""
    BLOOD_PRODUCT_DISPENSE_STATUS_MESSAGE = "BPS"  # 4
    """Blood product dispense status message"""
    BLOOD_PRODUCT_DISPENSE_STATUS_ACKNOWLEDGEMENT_MESSAGE = "BRP"  # 4
    """Blood product dispense status acknowledgement message"""
    BLOOD_PRODUCT_TRANSFUSION_OR_DISPOSITION_ACKNOWLEDGEMENT_MESSAGE = "BRT"  # 4
    """Blood product transfusion/disposition acknowledgement message"""
    BLOOD_PRODUCT_TRANSFUSION_OR_DISPOSITION_MESSAGE = "BTS"  # 4
    """Blood product transfusion/disposition message"""
    CLINICAL_STUDY_REGISTRATION_MESSAGE = "CRM"  # 7
    """Clinical study registration message"""
    UNSOLICITED_STUDY_DATA_MESSAGE = "CSU"  # 7
    """Unsolicited study data message"""
    DETAIL_FINANCIAL_TRANSACTIONS = "DFT"  # 6
    """Detail financial transactions"""
    DOCUMENT_RESPONSE = "DOC"  # 9
    """Document response"""
    DISPLAY_RESPONSE = "DSR"  # 5
    """Display response"""
    AUTOMATED_EQUIPMENT_COMMAND_MESSAGE = "EAC"  # 13
    """Automated equipment command message"""
    AUTOMATED_EQUIPMENT_NOTIFICATION_MESSAGE = "EAN"  # 13
    """Automated equipment notification message"""
    AUTOMATED_EQUIPMENT_RESPONSE_MESSAGE = "EAR"  # 13
    """Automated equipment response message"""
    ENHANCED_DISPLAY_RESPONSE = "EDR"  # 5
    """Enhanced display response"""
    EMBEDDED_QUERY_LANGUAGE_QUERY = "EQQ"  # 5
    """Embedded query language query"""
    EVENT_REPLAY_RESPONSE = "ERP"  # 5
    """Event replay response"""
    AUTOMATED_EQUIPMENT_STATUS_UPDATE_ACKNOWLEDGMENT_MESSAGE = "ESR"  # 13
    """Automated equipment status update acknowledgment message"""
    AUTOMATED_EQUIPMENT_STATUS_UPDATE_MESSAGE = "ESU"  # 13
    """Automated equipment status update message"""
    AUTOMATED_EQUIPMENT_INVENTORY_REQUEST_MESSAGE = "INR"  # 13
    """Automated equipment inventory request message"""
    AUTOMATED_EQUIPMENT_INVENTORY_UPDATE_MESSAGE = "INU"  # 13
    """Automated equipment inventory update message"""
    AUTOMATED_EQUIPMENT_LOG_OR_SERVICE_REQUEST_MESSAGE = "LSR"  # 13
    """Automated equipment log/service request message"""
    AUTOMATED_EQUIPMENT_LOG_OR_SERVICE_UPDATE_MESSAGE = "LSU"  # 13
    """Automated equipment log/service update message"""
    DELAYED_ACKNOWLEDGMENT = "MCF"  # 2
    """Delayed Acknowledgment (Retained for backward compatibility only)"""
    MEDICAL_DOCUMENT_MANAGEMENT = "MDM"  # 9
    """Medical document management"""
    MASTER_FILES_DELAYED_APPLICATION_ACKNOWLEDGMENT = "MFD"  # 8
    """Master files delayed application acknowledgment"""
    MASTER_FILES_APPLICATION_ACKNOWLEDGMENT = "MFK"  # 8
    """Master files application acknowledgment"""
    MASTER_FILES_NOTIFICATION = "MFN"  # 8
    """Master files notification"""
    MASTER_FILES_QUERY = "MFQ"  # 8
    """Master files query"""
    MASTER_FILES_RESPONSE = "MFR"  # 8
    """Master files response"""
    APPLICATION_MANAGEMENT_DATA_MESSAGE = "NMD"  # 14
    """Application management data message"""
    APPLICATION_MANAGEMENT_QUERY_MESSAGE = "NMQ"  # 14
    """Application management query message"""
    APPLICATION_MANAGEMENT_RESPONSE_MESSAGE = "NMR"  # 14
    """Application management response message"""
    BLOOD_PRODUCT_ORDER_MESSAGE = "OMB"  # 4
    """Blood product order message"""
    DIETARY_ORDER = "OMD"  # 4
    """Dietary order"""
    GENERAL_CLINICAL_ORDER_MESSAGE = "OMG"  # 4
    """General clinical order message"""
    IMAGING_ORDER = "OMI"  # 4
    """Imaging order"""
    LABORATORY_ORDER_MESSAGE = "OML"  # 4
    """Laboratory order message"""
    NON_STOCK_REQUISITION_ORDER_MESSAGE = "OMN"  # 4
    """Non-stock requisition order message"""
    PHARMACY_OR_TREATMENT_ORDER_MESSAGE = "OMP"  # 4
    """Pharmacy/treatment order message"""
    STOCK_REQUISITION_ORDER_MESSAGE = "OMS"  # 4
    """Stock requisition order message"""
    BLOOD_PRODUCT_ORDER_ACKNOWLEDGEMENT_MESSAGE = "ORB"  # 4
    """Blood product order acknowledgement message"""
    DIETARY_ORDER_ACKNOWLEDGMENT_MESSAGE = "ORD"  # 4
    """Dietary order acknowledgment message"""
    QUERY_FOR_RESULTS_OF_OBSERVATION = "ORF"  # 7
    """Query for results of observation"""
    GENERAL_CLINICAL_ORDER_ACKNOWLEDGMENT_MESSAGE = "ORG"  # 4
    """General clinical order acknowledgment message"""
    IMAGING_ORDER_ACKNOWLEDGEMENT_MESSAGE = "ORI"  # 4
    """Imaging order acknowledgement message"""
    LABORATORY_ACKNOWLEDGMENT_MESSAGE = "ORL"  # 7
    """Laboratory acknowledgment message (unsolicited)"""
    ORM = "ORM"  # 4
    """Pharmacy/treatment order message"""
    NON_STOCK_REQUISITION_GENERAL_ORDER_ACKNOWLEDGMENT_MESSAGE = "ORN"  # 4
    """Non-stock requisition - General order acknowledgment message"""
    PHARMACY_OR_TREATMENT_ORDER_ACKNOWLEDGMENT_MESSAGE = "ORP"  # 4
    """Pharmacy/treatment order acknowledgment message"""
    GENERAL_ORDER_RESPONSE_MESSAGE_RESPONSE_TO_ANY_ORM = "ORR"  # 4
    """General order response message response to any ORM"""
    STOCK_REQUISITION_ORDER_ACKNOWLEDGMENT_MESSAGE = "ORS"  # 4
    """Stock requisition - Order acknowledgment message"""
    UNSOLICITED_TRANSMISSION_OF_AN_OBSERVATION_MESSAGE = "ORU"  # 7
    """Unsolicited transmission of an observation message"""
    QUERY_RESPONSE_FOR_ORDER_STATUS = "OSQ"  # 4
    """Query response for order status"""
    OSR = "OSR"  # 4
    """Query response for order status"""
    UNSOLICITED_LABORATORY_OBSERVATION_MESSAGE = "OUL"  # 7
    """Unsolicited laboratory observation message"""
    PRODUCT_EXPERIENCE_MESSAGE = "PEX"  # 7
    """Product experience message"""
    PATIENT_GOAL_MESSAGE = "PGL"  # 12
    """Patient goal message"""
    PATIENT_INSURANCE_INFORMATION = "PIN"  # 11
    """Patient insurance information"""
    ADD_PERSONNEL_RECORD = "PMU"  # 15
    """Add personnel record"""
    PATIENT_PATHWAY_MESSAGE = "PPG"  # 12
    """Patient pathway message (goal-oriented)"""
    PPP = "PPP"  # 12
    """Patient pathway message (problem-oriented)"""
    PATIENT_PROBLEM_MESSAGE = "PPR"  # 12
    """Patient problem message"""
    PATIENT_PATHWAY_GOAL_ORIENTED_RESPONSE = "PPT"  # 12
    """Patient pathway goal-oriented response"""
    PATIENT_GOAL_RESPONSE = "PPV"  # 12
    """Patient goal response"""
    PATIENT_PROBLEM_RESPONSE = "PRR"  # 12
    """Patient problem response"""
    PATIENT_PATHWAY_PROBLEM_ORIENTED_RESPONSE = "PTR"  # 12
    """Patient pathway problem-oriented response"""
    QUERY_BY_PARAMETER = "QBP"  # 5
    """Query by parameter"""
    DEFERRED_QUERY = "QCK"  # 5
    """Deferred query"""
    CANCEL_QUERY = "QCN"  # 5
    """Cancel query"""
    QUERY_ORIGINAL_MODE = "QRY"  # 3
    """Query, original mode"""
    CREATE_SUBSCRIPTION = "QSB"  # 5
    """Create subscription"""
    CANCEL_SUBSCRIPTION_OR_ACKNOWLEDGE_MESSAGE = "QSX"  # 5
    """Cancel subscription/acknowledge message"""
    QUERY_FOR_PREVIOUS_EVENTS = "QVR"  # 5
    """Query for previous events"""
    PHARMACY_OR_TREATMENT_ADMINISTRATION_INFORMATION = "RAR"  # 4
    """Pharmacy/treatment administration information"""
    PHARMACY_OR_TREATMENT_ADMINISTRATION_MESSAGE = "RAS"  # 4
    """Pharmacy/treatment administration message"""
    RETURN_CLINICAL_INFORMATION = "RCI"  # 11
    """Return clinical information"""
    RETURN_CLINICAL_LIST = "RCL"  # 11
    """Return clinical list"""
    PHARMACY_OR_TREATMENT_ENCODED_ORDER_MESSAGE = "RDE"  # 4
    """Pharmacy/treatment encoded order message"""
    PHARMACY_OR_TREATMENT_DISPENSE_INFORMATION = "RDR"  # 4
    """Pharmacy/treatment dispense information"""
    PHARMACY_OR_TREATMENT_DISPENSE_MESSAGE = "RDS"  # 4
    """Pharmacy/treatment dispense message"""
    DISPLAY_BASED_RESPONSE = "RDY"  # 5
    """Display based response"""
    PATIENT_REFERRAL = "REF"  # 11
    """Patient referral"""
    PHARMACY_OR_TREATMENT_ENCODED_ORDER_INFORMATION = "RER"  # 4
    """Pharmacy/treatment encoded order information"""
    PHARMACY_OR_TREATMENT_DOSE_INFORMATION = "RGR"  # 4
    """Pharmacy/treatment dose information"""
    PHARMACY_OR_TREATMENT_GIVE_MESSAGE = "RGV"  # 4
    """Pharmacy/treatment give message"""
    PHARMACY_OR_TREATMENT_ORDER_RESPONSE = "ROR"  # 4
    """Pharmacy/treatment order response"""
    RETURN_PATIENT_AUTHORIZATION = "RPA"  # 11
    """Return patient authorization"""
    RETURN_PATIENT_INFORMATION = "RPI"  # 11
    """Return patient information"""
    RETURN_PATIENT_DISPLAY_LIST = "RPL"  # 11
    """Return patient display list"""
    RETURN_PATIENT_LIST = "RPR"  # 11
    """Return patient list"""
    REQUEST_PATIENT_AUTHORIZATION = "RQA"  # 11
    """Request patient authorization"""
    REQUEST_CLINICAL_INFORMATION = "RQC"  # 11
    """Request clinical information"""
    REQUEST_PATIENT_INFORMATION = "RQI"  # 11
    """Request patient information"""
    REQUEST_PATIENT_DEMOGRAPHICS = "RQP"  # 11
    """Request patient demographics"""
    EVENT_REPLAY_QUERY = "RQQ"  # 5
    """Event replay query"""
    PHARMACY_OR_TREATMENT_ADMINISTRATION_ACKNOWLEDGMENT_MESSAGE = "RRA"  # 4
    """Pharmacy/treatment administration acknowledgment message"""
    PHARMACY_OR_TREATMENT_DISPENSE_ACKNOWLEDGMENT_MESSAGE = "RRD"  # 4
    """Pharmacy/treatment dispense acknowledgment message"""
    PHARMACY_OR_TREATMENT_ENCODED_ORDER_ACKNOWLEDGMENT_MESSAGE = "RRE"  # 4
    """Pharmacy/treatment encoded order acknowledgment message"""
    PHARMACY_OR_TREATMENT_GIVE_ACKNOWLEDGMENT_MESSAGE = "RRG"  # 4
    """Pharmacy/treatment give acknowledgment message"""
    RETURN_REFERRAL_INFORMATION = "RRI"  # 11
    """Return referral information"""
    SEGMENT_PATTERN_RESPONSE = "RSP"  # 5
    """Segment pattern response"""
    TABULAR_RESPONSE = "RTB"  # 5
    """Tabular response"""
    SCHEDULE_INFORMATION_UNSOLICITED = "SIU"  # 10
    """Schedule information unsolicited"""
    STORED_PROCEDURE_REQUEST = "SPQ"  # 5
    """Stored procedure request"""
    SCHEDULE_QUERY_MESSAGE = "SQM"  # 10
    """Schedule query message"""
    SCHEDULE_QUERY_RESPONSE = "SQR"  # 10
    """Schedule query response"""
    SCHEDULE_REQUEST_MESSAGE = "SRM"  # 10
    """Schedule request message"""
    SCHEDULED_REQUEST_RESPONSE = "SRR"  # 10
    """Scheduled request response"""
    SPECIMEN_STATUS_REQUEST_MESSAGE = "SSR"  # 13
    """Specimen status request message"""
    SPECIMEN_STATUS_UPDATE_MESSAGE = "SSU"  # 13
    """Specimen status update message"""
    SUMMARY_PRODUCT_EXPERIENCE_REPORT = "SUR"  # 7
    """Summary product experience report"""
    TABULAR_DATA_RESPONSE = "TBR"  # 5
    """Tabular data response"""
    AUTOMATED_EQUIPMENT_TEST_CODE_SETTINGS_REQUEST_MESSAGE = "TCR"  # 13
    """Automated equipment test code settings request message"""
    AUTOMATED_EQUIPMENT_TEST_CODE_SETTINGS_UPDATE_MESSAGE = "TCU"  # 13
    """Automated equipment test code settings update message"""
    UNSOLICITED_DISPLAY_UPDATE_MESSAGE = "UDM"  # 5
    """Unsolicited display update message"""
    VIRTUAL_TABLE_QUERY = "VQQ"  # 5
    """Virtual table query"""
    QUERY_FOR_VACCINATION_RECORD = "VXQ"  # 4
    """Query for vaccination record"""
    VACCINATION_RECORD_RESPONSE = "VXR"  # 4
    """Vaccination record response"""
    UNSOLICITED_VACCINATION_RECORD_UPDATE = "VXU"  # 4
    """Unsolicited vaccination record update"""
    RESPONSE_FOR_VACCINATION_QUERY_WITH_MULTIPLE_PID_MATCHES = "VXX"  # 4
    """Response for vaccination query with multiple PID matches"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MessageType.GENERAL_ACKNOWLEDGMENT_MESSAGE: "General acknowledgment message",
    MessageType.ADT_RESPONSE: "ADT response",
    MessageType.ADT_MESSAGE: "ADT message",
    MessageType.ADD_OR_CHANGE_BILLING_ACCOUNT: "Add/change billing account",
    MessageType.BLOOD_PRODUCT_DISPENSE_STATUS_MESSAGE: "Blood product dispense status message",
    MessageType.BLOOD_PRODUCT_DISPENSE_STATUS_ACKNOWLEDGEMENT_MESSAGE: "Blood product dispense status acknowledgement message",
    MessageType.BLOOD_PRODUCT_TRANSFUSION_OR_DISPOSITION_ACKNOWLEDGEMENT_MESSAGE: "Blood product transfusion/disposition acknowledgement message",
    MessageType.BLOOD_PRODUCT_TRANSFUSION_OR_DISPOSITION_MESSAGE: "Blood product transfusion/disposition message",
    MessageType.CLINICAL_STUDY_REGISTRATION_MESSAGE: "Clinical study registration message",
    MessageType.UNSOLICITED_STUDY_DATA_MESSAGE: "Unsolicited study data message",
    MessageType.DETAIL_FINANCIAL_TRANSACTIONS: "Detail financial transactions",
    MessageType.DOCUMENT_RESPONSE: "Document response",
    MessageType.DISPLAY_RESPONSE: "Display response",
    MessageType.AUTOMATED_EQUIPMENT_COMMAND_MESSAGE: "Automated equipment command message",
    MessageType.AUTOMATED_EQUIPMENT_NOTIFICATION_MESSAGE: "Automated equipment notification message",
    MessageType.AUTOMATED_EQUIPMENT_RESPONSE_MESSAGE: "Automated equipment response message",
    MessageType.ENHANCED_DISPLAY_RESPONSE: "Enhanced display response",
    MessageType.EMBEDDED_QUERY_LANGUAGE_QUERY: "Embedded query language query",
    MessageType.EVENT_REPLAY_RESPONSE: "Event replay response",
    MessageType.AUTOMATED_EQUIPMENT_STATUS_UPDATE_ACKNOWLEDGMENT_MESSAGE: "Automated equipment status update acknowledgment message",
    MessageType.AUTOMATED_EQUIPMENT_STATUS_UPDATE_MESSAGE: "Automated equipment status update message",
    MessageType.AUTOMATED_EQUIPMENT_INVENTORY_REQUEST_MESSAGE: "Automated equipment inventory request message",
    MessageType.AUTOMATED_EQUIPMENT_INVENTORY_UPDATE_MESSAGE: "Automated equipment inventory update message",
    MessageType.AUTOMATED_EQUIPMENT_LOG_OR_SERVICE_REQUEST_MESSAGE: "Automated equipment log/service request message",
    MessageType.AUTOMATED_EQUIPMENT_LOG_OR_SERVICE_UPDATE_MESSAGE: "Automated equipment log/service update message",
    MessageType.DELAYED_ACKNOWLEDGMENT: "Delayed Acknowledgment (Retained for backward compatibility only)",
    MessageType.MEDICAL_DOCUMENT_MANAGEMENT: "Medical document management",
    MessageType.MASTER_FILES_DELAYED_APPLICATION_ACKNOWLEDGMENT: "Master files delayed application acknowledgment",
    MessageType.MASTER_FILES_APPLICATION_ACKNOWLEDGMENT: "Master files application acknowledgment",
    MessageType.MASTER_FILES_NOTIFICATION: "Master files notification",
    MessageType.MASTER_FILES_QUERY: "Master files query",
    MessageType.MASTER_FILES_RESPONSE: "Master files response",
    MessageType.APPLICATION_MANAGEMENT_DATA_MESSAGE: "Application management data message",
    MessageType.APPLICATION_MANAGEMENT_QUERY_MESSAGE: "Application management query message",
    MessageType.APPLICATION_MANAGEMENT_RESPONSE_MESSAGE: "Application management response message",
    MessageType.BLOOD_PRODUCT_ORDER_MESSAGE: "Blood product order message",
    MessageType.DIETARY_ORDER: "Dietary order",
    MessageType.GENERAL_CLINICAL_ORDER_MESSAGE: "General clinical order message",
    MessageType.IMAGING_ORDER: "Imaging order",
    MessageType.LABORATORY_ORDER_MESSAGE: "Laboratory order message",
    MessageType.NON_STOCK_REQUISITION_ORDER_MESSAGE: "Non-stock requisition order message",
    MessageType.PHARMACY_OR_TREATMENT_ORDER_MESSAGE: "Pharmacy/treatment order message",
    MessageType.STOCK_REQUISITION_ORDER_MESSAGE: "Stock requisition order message",
    MessageType.BLOOD_PRODUCT_ORDER_ACKNOWLEDGEMENT_MESSAGE: "Blood product order acknowledgement message",
    MessageType.DIETARY_ORDER_ACKNOWLEDGMENT_MESSAGE: "Dietary order acknowledgment message",
    MessageType.QUERY_FOR_RESULTS_OF_OBSERVATION: "Query for results of observation",
    MessageType.GENERAL_CLINICAL_ORDER_ACKNOWLEDGMENT_MESSAGE: "General clinical order acknowledgment message",
    MessageType.IMAGING_ORDER_ACKNOWLEDGEMENT_MESSAGE: "Imaging order acknowledgement message",
    MessageType.LABORATORY_ACKNOWLEDGMENT_MESSAGE: "Laboratory acknowledgment message (unsolicited)",
    MessageType.ORM: "Pharmacy/treatment order message",
    MessageType.NON_STOCK_REQUISITION_GENERAL_ORDER_ACKNOWLEDGMENT_MESSAGE: "Non-stock requisition - General order acknowledgment message",
    MessageType.PHARMACY_OR_TREATMENT_ORDER_ACKNOWLEDGMENT_MESSAGE: "Pharmacy/treatment order acknowledgment message",
    MessageType.GENERAL_ORDER_RESPONSE_MESSAGE_RESPONSE_TO_ANY_ORM: "General order response message response to any ORM",
    MessageType.STOCK_REQUISITION_ORDER_ACKNOWLEDGMENT_MESSAGE: "Stock requisition - Order acknowledgment message",
    MessageType.UNSOLICITED_TRANSMISSION_OF_AN_OBSERVATION_MESSAGE: "Unsolicited transmission of an observation message",
    MessageType.QUERY_RESPONSE_FOR_ORDER_STATUS: "Query response for order status",
    MessageType.OSR: "Query response for order status",
    MessageType.UNSOLICITED_LABORATORY_OBSERVATION_MESSAGE: "Unsolicited laboratory observation message",
    MessageType.PRODUCT_EXPERIENCE_MESSAGE: "Product experience message",
    MessageType.PATIENT_GOAL_MESSAGE: "Patient goal message",
    MessageType.PATIENT_INSURANCE_INFORMATION: "Patient insurance information",
    MessageType.ADD_PERSONNEL_RECORD: "Add personnel record",
    MessageType.PATIENT_PATHWAY_MESSAGE: "Patient pathway message (goal-oriented)",
    MessageType.PPP: "Patient pathway message (problem-oriented)",
    MessageType.PATIENT_PROBLEM_MESSAGE: "Patient problem message",
    MessageType.PATIENT_PATHWAY_GOAL_ORIENTED_RESPONSE: "Patient pathway goal-oriented response",
    MessageType.PATIENT_GOAL_RESPONSE: "Patient goal response",
    MessageType.PATIENT_PROBLEM_RESPONSE: "Patient problem response",
    MessageType.PATIENT_PATHWAY_PROBLEM_ORIENTED_RESPONSE: "Patient pathway problem-oriented response",
    MessageType.QUERY_BY_PARAMETER: "Query by parameter",
    MessageType.DEFERRED_QUERY: "Deferred query",
    MessageType.CANCEL_QUERY: "Cancel query",
    MessageType.QUERY_ORIGINAL_MODE: "Query, original mode",
    MessageType.CREATE_SUBSCRIPTION: "Create subscription",
    MessageType.CANCEL_SUBSCRIPTION_OR_ACKNOWLEDGE_MESSAGE: "Cancel subscription/acknowledge message",
    MessageType.QUERY_FOR_PREVIOUS_EVENTS: "Query for previous events",
    MessageType.PHARMACY_OR_TREATMENT_ADMINISTRATION_INFORMATION: "Pharmacy/treatment administration information",
    MessageType.PHARMACY_OR_TREATMENT_ADMINISTRATION_MESSAGE: "Pharmacy/treatment administration message",
    MessageType.RETURN_CLINICAL_INFORMATION: "Return clinical information",
    MessageType.RETURN_CLINICAL_LIST: "Return clinical list",
    MessageType.PHARMACY_OR_TREATMENT_ENCODED_ORDER_MESSAGE: "Pharmacy/treatment encoded order message",
    MessageType.PHARMACY_OR_TREATMENT_DISPENSE_INFORMATION: "Pharmacy/treatment dispense information",
    MessageType.PHARMACY_OR_TREATMENT_DISPENSE_MESSAGE: "Pharmacy/treatment dispense message",
    MessageType.DISPLAY_BASED_RESPONSE: "Display based response",
    MessageType.PATIENT_REFERRAL: "Patient referral",
    MessageType.PHARMACY_OR_TREATMENT_ENCODED_ORDER_INFORMATION: "Pharmacy/treatment encoded order information",
    MessageType.PHARMACY_OR_TREATMENT_DOSE_INFORMATION: "Pharmacy/treatment dose information",
    MessageType.PHARMACY_OR_TREATMENT_GIVE_MESSAGE: "Pharmacy/treatment give message",
    MessageType.PHARMACY_OR_TREATMENT_ORDER_RESPONSE: "Pharmacy/treatment order response",
    MessageType.RETURN_PATIENT_AUTHORIZATION: "Return patient authorization",
    MessageType.RETURN_PATIENT_INFORMATION: "Return patient information",
    MessageType.RETURN_PATIENT_DISPLAY_LIST: "Return patient display list",
    MessageType.RETURN_PATIENT_LIST: "Return patient list",
    MessageType.REQUEST_PATIENT_AUTHORIZATION: "Request patient authorization",
    MessageType.REQUEST_CLINICAL_INFORMATION: "Request clinical information",
    MessageType.REQUEST_PATIENT_INFORMATION: "Request patient information",
    MessageType.REQUEST_PATIENT_DEMOGRAPHICS: "Request patient demographics",
    MessageType.EVENT_REPLAY_QUERY: "Event replay query",
    MessageType.PHARMACY_OR_TREATMENT_ADMINISTRATION_ACKNOWLEDGMENT_MESSAGE: "Pharmacy/treatment administration acknowledgment message",
    MessageType.PHARMACY_OR_TREATMENT_DISPENSE_ACKNOWLEDGMENT_MESSAGE: "Pharmacy/treatment dispense acknowledgment message",
    MessageType.PHARMACY_OR_TREATMENT_ENCODED_ORDER_ACKNOWLEDGMENT_MESSAGE: "Pharmacy/treatment encoded order acknowledgment message",
    MessageType.PHARMACY_OR_TREATMENT_GIVE_ACKNOWLEDGMENT_MESSAGE: "Pharmacy/treatment give acknowledgment message",
    MessageType.RETURN_REFERRAL_INFORMATION: "Return referral information",
    MessageType.SEGMENT_PATTERN_RESPONSE: "Segment pattern response",
    MessageType.TABULAR_RESPONSE: "Tabular response",
    MessageType.SCHEDULE_INFORMATION_UNSOLICITED: "Schedule information unsolicited",
    MessageType.STORED_PROCEDURE_REQUEST: "Stored procedure request",
    MessageType.SCHEDULE_QUERY_MESSAGE: "Schedule query message",
    MessageType.SCHEDULE_QUERY_RESPONSE: "Schedule query response",
    MessageType.SCHEDULE_REQUEST_MESSAGE: "Schedule request message",
    MessageType.SCHEDULED_REQUEST_RESPONSE: "Scheduled request response",
    MessageType.SPECIMEN_STATUS_REQUEST_MESSAGE: "Specimen status request message",
    MessageType.SPECIMEN_STATUS_UPDATE_MESSAGE: "Specimen status update message",
    MessageType.SUMMARY_PRODUCT_EXPERIENCE_REPORT: "Summary product experience report",
    MessageType.TABULAR_DATA_RESPONSE: "Tabular data response",
    MessageType.AUTOMATED_EQUIPMENT_TEST_CODE_SETTINGS_REQUEST_MESSAGE: "Automated equipment test code settings request message",
    MessageType.AUTOMATED_EQUIPMENT_TEST_CODE_SETTINGS_UPDATE_MESSAGE: "Automated equipment test code settings update message",
    MessageType.UNSOLICITED_DISPLAY_UPDATE_MESSAGE: "Unsolicited display update message",
    MessageType.VIRTUAL_TABLE_QUERY: "Virtual table query",
    MessageType.QUERY_FOR_VACCINATION_RECORD: "Query for vaccination record",
    MessageType.VACCINATION_RECORD_RESPONSE: "Vaccination record response",
    MessageType.UNSOLICITED_VACCINATION_RECORD_UPDATE: "Unsolicited vaccination record update",
    MessageType.RESPONSE_FOR_VACCINATION_QUERY_WITH_MULTIPLE_PID_MATCHES: "Response for vaccination query with multiple PID matches",
}
