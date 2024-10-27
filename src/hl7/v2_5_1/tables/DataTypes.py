from ...base import HL7Table

"""
HL7 Version: 2.5.1
Data types - 0440
Table Type: HL7
"""


class DataTypes(HL7Table):
    """
    Data types - 0440 // HL7 table type
    - ADDRESS
    - AUTHORIZATION_INFORMATION
    - CHARGE_CODE_AND_DATE
    - CHANNEL_CALIBRATION_PARAMETERS
    - CHANNEL_DEFINITION
    - CODED_ELEMENT
    - CODED_ELEMENT_WITH_FORMATTED_VALUES
    - COMPOSITE_ID_WITH_CHECK_DIGIT
    - COMPOSITE
    - COMPOSITE_ID_NUMBER_AND_NAME
    - CODED_WITH_NO_EXCEPTIONS
    - COMPOSITE_ID_NUMBER_AND_NAME_SIMPLIFIED
    - COMPOSITE_PRICE
    - COMPOSITE_QUANTITY_WITH_UNITS
    - CHANNEL_SENSITIVITY
    - CODED_WITH_EXCEPTIONS
    - EXTENDED_COMPOSITE_ID_WITH_CHECK_DIGIT
    - DAILY_DEDUCTIBLE_INFORMATION
    - DATE_AND_INSTITUTION_NAME
    - DISCHARGE_TO_LOCATION_AND_DATE
    - DRIVERS_LICENSE_NUMBER
    - DELTA
    - DATE_OR_TIME_RANGE
    - DATE
    - DATE_OR_TIME
    - DAY_TYPE_AND_NUMBER
    - ENCAPSULATED_DATA
    - ENTITY_IDENTIFIER
    - ENTITY_IDENTIFIER_PAIR
    - ERROR_LOCATION
    - FINANCIAL_CLASS
    - FAMILY_NAME
    - FORMATTED_TEXT
    - GENERAL_TIMING_SPECIFICATION
    - HIERARCHIC_DESIGNATOR
    - INSURANCE_CERTIFICATION_DEFINITION
    - CODED_VALUES_FOR_HL7_TABLES
    - CODED_VALUE_FOR_USER_DEFINED_TABLES
    - JOB_CODE_OR_CLASS
    - LOCATION_WITH_ADDRESS_VARIATION_1
    - LOCATION_WITH_ADDRESS_VARIATION_2
    - ERROR_LOCATION_AND_DESCRIPTION
    - MULTIPLEXED_ARRAY
    - MONEY
    - MONEY_AND_CHARGE_CODE
    - MONEY_OR_PERCENTAGE
    - MESSAGE_TYPE
    - NUMERIC_ARRAY
    - NAME_WITH_LOCATION_AND_DATE
    - NUMERIC
    - NUMERIC_RANGE
    - OCCURRENCE_CODE_AND_DATE
    - ORDER_SEQUENCE_DEFINITION
    - OCCURRENCE_SPAN_CODE_AND_DATE
    - PRACTITIONER_INSTITUTIONAL_PRIVILEGES
    - PERSON_LOCATION
    - PRACTITIONER_LICENSE_OR_OTHER_ID_NUMBER
    - PERSON_NAME
    - PERFORMING_PERSON_TIME_STAMP
    - PARENT_RESULT_LINK
    - PROCESSING_TYPE
    - POLICY_TYPE_AND_AMOUNT
    - QUERY_INPUT_PARAMETER_LIST
    - QUERY_SELECTION_CRITERIA
    - ROW_COLUMN_DEFINITION
    - REFERENCE_RANGE
    - REPEAT_INTERVAL
    - ROOM_COVERAGE
    - REFERENCE_POINTER
    - REPEAT_PATTERN
    - STREET_ADDRESS
    - SCHEDULING_CLASS_VALUE_PAIR
    - SEQUENCE_ID
    - STRUCTURED_NUMERIC
    - SPECIALTY_DESCRIPTION
    - SPECIMEN_SOURCE
    - SORT_ORDER
    - STRING
    - TIME
    - TELEPHONE_NUMBER
    - TIMING_OR_QUANTITY
    - TIME_STAMP
    - TEXT_DATA
    - UB_VALUE_CODE_AND_AMOUNT
    - VISITING_HOURS
    - VERSION_IDENTIFIER
    - VALUE_RANGE
    - CHANNEL_IDENTIFIER
    - WAVEFORM_SOURCE
    - EXTENDED_ADDRESS
    - EXTENDED_COMPOSITE_ID_NUMBER_AND_NAME
    - EXTENDED_COMPOSITE_NAME_AND_ID_NUMBER_FOR_ORGANIZATIONS
    - EXTENDED_PERSON_NAME
    - EXTENDED_TELECOMMUNICATIONS_NUMBER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0440
    """

    ADDRESS = "AD"  # 415
    """Address"""
    AUTHORIZATION_INFORMATION = "AUI"  # 239
    """Authorization information"""
    CHARGE_CODE_AND_DATE = "CCD"  # 28
    """Charge code and date"""
    CHANNEL_CALIBRATION_PARAMETERS = "CCP"  # 20
    """Channel calibration parameters"""
    CHANNEL_DEFINITION = "CD"  # 581
    """Channel definition"""
    CODED_ELEMENT = "CE"  # 483
    """Coded element"""
    CODED_ELEMENT_WITH_FORMATTED_VALUES = "CF"  # 65536
    """Coded element with formatted values"""
    COMPOSITE_ID_WITH_CHECK_DIGIT = "CK"
    """Composite ID with check digit"""
    COMPOSITE = "CM"
    """Composite"""
    COMPOSITE_ID_NUMBER_AND_NAME = "CN"
    """Composite ID number and name"""
    CODED_WITH_NO_EXCEPTIONS = "CNE"  # 705
    """Coded with no exceptions"""
    COMPOSITE_ID_NUMBER_AND_NAME_SIMPLIFIED = "CNS"  # 406
    """Composite ID number and name simplified"""
    COMPOSITE_PRICE = "CP"  # 543
    """Composite price"""
    COMPOSITE_QUANTITY_WITH_UNITS = "CQ"  # 500
    """Composite quantity with units"""
    CHANNEL_SENSITIVITY = "CSU"  # 490
    """Channel sensitivity"""
    CODED_WITH_EXCEPTIONS = "CWE"  # 705
    """Coded with exceptions"""
    EXTENDED_COMPOSITE_ID_WITH_CHECK_DIGIT = "CX"  # 1913
    """Extended composite ID with check digit"""
    DAILY_DEDUCTIBLE_INFORMATION = "DDI"  # 25
    """Daily deductible information"""
    DATE_AND_INSTITUTION_NAME = "DIN"  # 510
    """Date and institution name"""
    DISCHARGE_TO_LOCATION_AND_DATE = "DLD"  # 47
    """Discharge to location and date"""
    DRIVERS_LICENSE_NUMBER = "DLN"  # 66
    """Drivers license number"""
    DELTA = "DLT"  # 45
    """Delta"""
    DATE_OR_TIME_RANGE = "DR"  # 53
    """Date/time range"""
    DATE = "DT"  # 8
    """Date"""
    DATE_OR_TIME = "DTM"  # 24
    """Date/time"""
    DAY_TYPE_AND_NUMBER = "DTN"  # 6
    """Day type and number"""
    ENCAPSULATED_DATA = "ED"  # 65536
    """Encapsulated data"""
    ENTITY_IDENTIFIER = "EI"  # 427
    """Entity identifier"""
    ENTITY_IDENTIFIER_PAIR = "EIP"  # 855
    """Entity identifier pair"""
    ERROR_LOCATION = "ERL"  # 18
    """Error location"""
    FINANCIAL_CLASS = "FC"  # 47
    """Financial class"""
    FAMILY_NAME = "FN"  # 194
    """Family name"""
    FORMATTED_TEXT = "FT"  # 65536
    """Formatted text"""
    GENERAL_TIMING_SPECIFICATION = "GTS"  # 199
    """General timing specification"""
    HIERARCHIC_DESIGNATOR = "HD"  # 227
    """Hierarchic designator"""
    INSURANCE_CERTIFICATION_DEFINITION = "ICD"  # 40
    """Insurance certification definition"""
    CODED_VALUES_FOR_HL7_TABLES = "ID"  # Variable
    """Coded values for HL7 tables"""
    CODED_VALUE_FOR_USER_DEFINED_TABLES = "IS"  # 20
    """Coded value for user-defined tables"""
    JOB_CODE_OR_CLASS = "JCC"  # 292
    """Job code/class"""
    LOCATION_WITH_ADDRESS_VARIATION_1 = "LA1"  # 415
    """Location with address variation 1"""
    LOCATION_WITH_ADDRESS_VARIATION_2 = "LA2"  # 790
    """Location with address variation 2"""
    ERROR_LOCATION_AND_DESCRIPTION = "LD"  # 493
    """Error location and description"""
    MULTIPLEXED_ARRAY = "MA"  # 65536
    """Multiplexed array"""
    MONEY = "MO"  # 20
    """Money"""
    MONEY_AND_CHARGE_CODE = "MOC"  # 504
    """Money and charge code"""
    MONEY_OR_PERCENTAGE = "MOP"  # 23
    """Money or percentage"""
    MESSAGE_TYPE = "MSG"  # 15
    """Message type"""
    NUMERIC_ARRAY = "NA"  # 65536
    """Numeric array"""
    NAME_WITH_LOCATION_AND_DATE = "NDL"  # 835
    """Name with location and date"""
    NUMERIC = "NM"  # 16
    """Numeric"""
    NUMERIC_RANGE = "NR"  # 33
    """Numeric range"""
    OCCURRENCE_CODE_AND_DATE = "OCD"  # 714
    """Occurrence code and date"""
    ORDER_SEQUENCE_DEFINITION = "OSD"  # 110
    """Order sequence definition"""
    OCCURRENCE_SPAN_CODE_AND_DATE = "OSP"  # 723
    """Occurrence span code and date"""
    PRACTITIONER_INSTITUTIONAL_PRIVILEGES = "PIP"  # 1413
    """Practitioner institutional privileges"""
    PERSON_LOCATION = "PL"  # 1230
    """Person location"""
    PRACTITIONER_LICENSE_OR_OTHER_ID_NUMBER = "PLN"  # 101
    """Practitioner license or other ID number"""
    PERSON_NAME = "PN"
    """Person name"""
    PERFORMING_PERSON_TIME_STAMP = "PPN"  # 2993
    """Performing person time stamp"""
    PARENT_RESULT_LINK = "PRL"  # 755
    """Parent result link"""
    PROCESSING_TYPE = "PT"  # 3
    """Processing type"""
    POLICY_TYPE_AND_AMOUNT = "PTA"  # 56
    """Policy type and amount"""
    QUERY_INPUT_PARAMETER_LIST = "QIP"  # 212
    """Query input parameter list"""
    QUERY_SELECTION_CRITERIA = "QSC"  # 219
    """Query selection criteria"""
    ROW_COLUMN_DEFINITION = "RCD"  # 19
    """Row column definition"""
    REFERENCE_RANGE = "RFR"  # 352
    """Reference range"""
    REPEAT_INTERVAL = "RI"  # 206
    """Repeat interval"""
    ROOM_COVERAGE = "RMC"  # 82
    """Room coverage"""
    REFERENCE_POINTER = "RP"  # 273
    """Reference pointer"""
    REPEAT_PATTERN = "RPT"  # 984
    """Repeat pattern"""
    STREET_ADDRESS = "SAD"  # 184
    """Street Address"""
    SCHEDULING_CLASS_VALUE_PAIR = "SCV"  # 41
    """Scheduling class value pair"""
    SEQUENCE_ID = "SI"  # 4
    """Sequence ID"""
    STRUCTURED_NUMERIC = "SN"  # 36
    """Structured numeric"""
    SPECIALTY_DESCRIPTION = "SPD"  # 112
    """Specialty description"""
    SPECIMEN_SOURCE = "SPS"  # 4436
    """Specimen source"""
    SORT_ORDER = "SRT"  # 15
    """Sort order"""
    STRING = "ST"  # 199
    """String"""
    TIME = "TM"  # 16
    """Time"""
    TELEPHONE_NUMBER = "TN"  # 199
    """Telephone number"""
    TIMING_OR_QUANTITY = "TQ"  # 1209
    """Timing/quantity"""
    TIME_STAMP = "TS"  # 26
    """Time stamp"""
    TEXT_DATA = "TX"  # 65536
    """Text data"""
    UB_VALUE_CODE_AND_AMOUNT = "UVC"  # 41
    """UB value code and amount"""
    VISITING_HOURS = "VH"  # 41
    """Visiting hours"""
    VERSION_IDENTIFIER = "VID"  # 973
    """Version identifier"""
    VALUE_RANGE = "VR"  # 13
    """Value range"""
    CHANNEL_IDENTIFIER = "WVI"  # 22
    """Channel Identifier"""
    WAVEFORM_SOURCE = "WVS"  # 17
    """Waveform source"""
    EXTENDED_ADDRESS = "XAD"  # 631
    """Extended address"""
    EXTENDED_COMPOSITE_ID_NUMBER_AND_NAME = "XCN"  # 3002
    """Extended composite ID number and name"""
    EXTENDED_COMPOSITE_NAME_AND_ID_NUMBER_FOR_ORGANIZATIONS = "XON"  # 567
    """Extended composite name and ID number for organizations"""
    EXTENDED_PERSON_NAME = "XPN"  # 1103
    """Extended person name"""
    EXTENDED_TELECOMMUNICATIONS_NUMBER = "XTN"  # 850
    """Extended telecommunications number"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DataTypes.ADDRESS: "Address",
    DataTypes.AUTHORIZATION_INFORMATION: "Authorization information",
    DataTypes.CHARGE_CODE_AND_DATE: "Charge code and date",
    DataTypes.CHANNEL_CALIBRATION_PARAMETERS: "Channel calibration parameters",
    DataTypes.CHANNEL_DEFINITION: "Channel definition",
    DataTypes.CODED_ELEMENT: "Coded element",
    DataTypes.CODED_ELEMENT_WITH_FORMATTED_VALUES: "Coded element with formatted values",
    DataTypes.COMPOSITE_ID_WITH_CHECK_DIGIT: "Composite ID with check digit",
    DataTypes.COMPOSITE: "Composite",
    DataTypes.COMPOSITE_ID_NUMBER_AND_NAME: "Composite ID number and name",
    DataTypes.CODED_WITH_NO_EXCEPTIONS: "Coded with no exceptions",
    DataTypes.COMPOSITE_ID_NUMBER_AND_NAME_SIMPLIFIED: "Composite ID number and name simplified",
    DataTypes.COMPOSITE_PRICE: "Composite price",
    DataTypes.COMPOSITE_QUANTITY_WITH_UNITS: "Composite quantity with units",
    DataTypes.CHANNEL_SENSITIVITY: "Channel sensitivity",
    DataTypes.CODED_WITH_EXCEPTIONS: "Coded with exceptions",
    DataTypes.EXTENDED_COMPOSITE_ID_WITH_CHECK_DIGIT: "Extended composite ID with check digit",
    DataTypes.DAILY_DEDUCTIBLE_INFORMATION: "Daily deductible information",
    DataTypes.DATE_AND_INSTITUTION_NAME: "Date and institution name",
    DataTypes.DISCHARGE_TO_LOCATION_AND_DATE: "Discharge to location and date",
    DataTypes.DRIVERS_LICENSE_NUMBER: "Drivers license number",
    DataTypes.DELTA: "Delta",
    DataTypes.DATE_OR_TIME_RANGE: "Date/time range",
    DataTypes.DATE: "Date",
    DataTypes.DATE_OR_TIME: "Date/time",
    DataTypes.DAY_TYPE_AND_NUMBER: "Day type and number",
    DataTypes.ENCAPSULATED_DATA: "Encapsulated data",
    DataTypes.ENTITY_IDENTIFIER: "Entity identifier",
    DataTypes.ENTITY_IDENTIFIER_PAIR: "Entity identifier pair",
    DataTypes.ERROR_LOCATION: "Error location",
    DataTypes.FINANCIAL_CLASS: "Financial class",
    DataTypes.FAMILY_NAME: "Family name",
    DataTypes.FORMATTED_TEXT: "Formatted text",
    DataTypes.GENERAL_TIMING_SPECIFICATION: "General timing specification",
    DataTypes.HIERARCHIC_DESIGNATOR: "Hierarchic designator",
    DataTypes.INSURANCE_CERTIFICATION_DEFINITION: "Insurance certification definition",
    DataTypes.CODED_VALUES_FOR_HL7_TABLES: "Coded values for HL7 tables",
    DataTypes.CODED_VALUE_FOR_USER_DEFINED_TABLES: "Coded value for user-defined tables",
    DataTypes.JOB_CODE_OR_CLASS: "Job code/class",
    DataTypes.LOCATION_WITH_ADDRESS_VARIATION_1: "Location with address variation 1",
    DataTypes.LOCATION_WITH_ADDRESS_VARIATION_2: "Location with address variation 2",
    DataTypes.ERROR_LOCATION_AND_DESCRIPTION: "Error location and description",
    DataTypes.MULTIPLEXED_ARRAY: "Multiplexed array",
    DataTypes.MONEY: "Money",
    DataTypes.MONEY_AND_CHARGE_CODE: "Money and charge code",
    DataTypes.MONEY_OR_PERCENTAGE: "Money or percentage",
    DataTypes.MESSAGE_TYPE: "Message type",
    DataTypes.NUMERIC_ARRAY: "Numeric array",
    DataTypes.NAME_WITH_LOCATION_AND_DATE: "Name with location and date",
    DataTypes.NUMERIC: "Numeric",
    DataTypes.NUMERIC_RANGE: "Numeric range",
    DataTypes.OCCURRENCE_CODE_AND_DATE: "Occurrence code and date",
    DataTypes.ORDER_SEQUENCE_DEFINITION: "Order sequence definition",
    DataTypes.OCCURRENCE_SPAN_CODE_AND_DATE: "Occurrence span code and date",
    DataTypes.PRACTITIONER_INSTITUTIONAL_PRIVILEGES: "Practitioner institutional privileges",
    DataTypes.PERSON_LOCATION: "Person location",
    DataTypes.PRACTITIONER_LICENSE_OR_OTHER_ID_NUMBER: "Practitioner license or other ID number",
    DataTypes.PERSON_NAME: "Person name",
    DataTypes.PERFORMING_PERSON_TIME_STAMP: "Performing person time stamp",
    DataTypes.PARENT_RESULT_LINK: "Parent result link",
    DataTypes.PROCESSING_TYPE: "Processing type",
    DataTypes.POLICY_TYPE_AND_AMOUNT: "Policy type and amount",
    DataTypes.QUERY_INPUT_PARAMETER_LIST: "Query input parameter list",
    DataTypes.QUERY_SELECTION_CRITERIA: "Query selection criteria",
    DataTypes.ROW_COLUMN_DEFINITION: "Row column definition",
    DataTypes.REFERENCE_RANGE: "Reference range",
    DataTypes.REPEAT_INTERVAL: "Repeat interval",
    DataTypes.ROOM_COVERAGE: "Room coverage",
    DataTypes.REFERENCE_POINTER: "Reference pointer",
    DataTypes.REPEAT_PATTERN: "Repeat pattern",
    DataTypes.STREET_ADDRESS: "Street Address",
    DataTypes.SCHEDULING_CLASS_VALUE_PAIR: "Scheduling class value pair",
    DataTypes.SEQUENCE_ID: "Sequence ID",
    DataTypes.STRUCTURED_NUMERIC: "Structured numeric",
    DataTypes.SPECIALTY_DESCRIPTION: "Specialty description",
    DataTypes.SPECIMEN_SOURCE: "Specimen source",
    DataTypes.SORT_ORDER: "Sort order",
    DataTypes.STRING: "String",
    DataTypes.TIME: "Time",
    DataTypes.TELEPHONE_NUMBER: "Telephone number",
    DataTypes.TIMING_OR_QUANTITY: "Timing/quantity",
    DataTypes.TIME_STAMP: "Time stamp",
    DataTypes.TEXT_DATA: "Text data",
    DataTypes.UB_VALUE_CODE_AND_AMOUNT: "UB value code and amount",
    DataTypes.VISITING_HOURS: "Visiting hours",
    DataTypes.VERSION_IDENTIFIER: "Version identifier",
    DataTypes.VALUE_RANGE: "Value range",
    DataTypes.CHANNEL_IDENTIFIER: "Channel Identifier",
    DataTypes.WAVEFORM_SOURCE: "Waveform source",
    DataTypes.EXTENDED_ADDRESS: "Extended address",
    DataTypes.EXTENDED_COMPOSITE_ID_NUMBER_AND_NAME: "Extended composite ID number and name",
    DataTypes.EXTENDED_COMPOSITE_NAME_AND_ID_NUMBER_FOR_ORGANIZATIONS: "Extended composite name and ID number for organizations",
    DataTypes.EXTENDED_PERSON_NAME: "Extended person name",
    DataTypes.EXTENDED_TELECOMMUNICATIONS_NUMBER: "Extended telecommunications number",
}
