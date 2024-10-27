from ...base import HL7Table

"""
HL7 Version: 2.5.1
Master file identifier code - 0175
Table Type: HL7
"""


class MasterFileIdentifierCode(HL7Table):
    """
    Master file identifier code - 0175 // HL7 table type
    - CHARGE_DESCRIPTION_MASTER_FILE
    - CLINIC_MASTER_FILE
    - CLINICAL_STUDY_WITH_PHASES_AND_SCHEDULED_MASTER_FILE
    - CLINICAL_STUDY_WITHOUT_PHASES_BUT_WITH_SCHEDULED_MASTER_FILE
    - INVENTORY_MASTER_FILE
    - LOCATION_MASTER_FILE
    - NUMERICAL_OBSERVATION_MASTER_FILE
    - CATEGORICAL_OBSERVATION_MASTER_FILE
    - OBSERVATION_BATTERIES_MASTER_FILE
    - CALCULATED_OBSERVATIONS_MASTER_FILE
    - OTHER_OBSERVATION_OR_SERVICE_ITEM_MASTER_FILE
    - PRACTITIONER_MASTER_FILE
    - STAFF_MASTER_FILE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0175
    """

    CHARGE_DESCRIPTION_MASTER_FILE = "CDM"
    """Charge description master file"""
    CLINIC_MASTER_FILE = "CLN"
    """Clinic master file"""
    CLINICAL_STUDY_WITH_PHASES_AND_SCHEDULED_MASTER_FILE = "CMA"
    """Clinical study with phases and scheduled master file"""
    CLINICAL_STUDY_WITHOUT_PHASES_BUT_WITH_SCHEDULED_MASTER_FILE = "CMB"
    """Clinical study without phases but with scheduled master file"""
    INVENTORY_MASTER_FILE = "INV"
    """Inventory master file"""
    LOCATION_MASTER_FILE = "LOC"
    """Location master file"""
    NUMERICAL_OBSERVATION_MASTER_FILE = "OMA"
    """Numerical observation master file"""
    CATEGORICAL_OBSERVATION_MASTER_FILE = "OMB"
    """Categorical observation master file"""
    OBSERVATION_BATTERIES_MASTER_FILE = "OMC"
    """Observation batteries master file"""
    CALCULATED_OBSERVATIONS_MASTER_FILE = "OMD"
    """Calculated observations master file"""
    OTHER_OBSERVATION_OR_SERVICE_ITEM_MASTER_FILE = "OME"
    """Other Observation/Service Item master file"""
    PRACTITIONER_MASTER_FILE = "PRA"
    """Practitioner master file"""
    STAFF_MASTER_FILE = "STF"
    """Staff master file"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MasterFileIdentifierCode.CHARGE_DESCRIPTION_MASTER_FILE: "Charge description master file",
    MasterFileIdentifierCode.CLINIC_MASTER_FILE: "Clinic master file",
    MasterFileIdentifierCode.CLINICAL_STUDY_WITH_PHASES_AND_SCHEDULED_MASTER_FILE: "Clinical study with phases and scheduled master file",
    MasterFileIdentifierCode.CLINICAL_STUDY_WITHOUT_PHASES_BUT_WITH_SCHEDULED_MASTER_FILE: "Clinical study without phases but with scheduled master file",
    MasterFileIdentifierCode.INVENTORY_MASTER_FILE: "Inventory master file",
    MasterFileIdentifierCode.LOCATION_MASTER_FILE: "Location master file",
    MasterFileIdentifierCode.NUMERICAL_OBSERVATION_MASTER_FILE: "Numerical observation master file",
    MasterFileIdentifierCode.CATEGORICAL_OBSERVATION_MASTER_FILE: "Categorical observation master file",
    MasterFileIdentifierCode.OBSERVATION_BATTERIES_MASTER_FILE: "Observation batteries master file",
    MasterFileIdentifierCode.CALCULATED_OBSERVATIONS_MASTER_FILE: "Calculated observations master file",
    MasterFileIdentifierCode.OTHER_OBSERVATION_OR_SERVICE_ITEM_MASTER_FILE: "Other Observation/Service Item master file",
    MasterFileIdentifierCode.PRACTITIONER_MASTER_FILE: "Practitioner master file",
    MasterFileIdentifierCode.STAFF_MASTER_FILE: "Staff master file",
}
