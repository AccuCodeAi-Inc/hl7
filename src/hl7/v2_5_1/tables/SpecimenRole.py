from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen Role - 0369
Table Type: User
"""


class SpecimenRole(HL7Table):
    """
    Specimen Role - 0369 // User table type
    - BLIND_SAMPLE
    - CALIBRATOR
    - ELECTRONIC_QC_USED_WITH_MANUFACTURED_REFERENCE_PROVIDING_SIGNALS_THAT_SIMULATE_QC_RESULTS
    - SPECIMEN_USED_FOR_TESTING_PROFICIENCY_OF_THE_ORGANIZATION_PERFORMING_THE_TESTING
    - GROUP
    - POOL
    - SPECIMEN_USED_FOR_TESTING_OPERATOR_PROFICIENCY
    - PATIENT
    - CONTROL_SPECIMEN
    - REPLICATE
    - VERIFYING_CALIBRATOR_USED_FOR_PERIODIC_CALIBRATION_CHECKS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0369
    """

    BLIND_SAMPLE = "B"
    """Blind Sample"""
    CALIBRATOR = "C"
    """Calibrator"""
    ELECTRONIC_QC_USED_WITH_MANUFACTURED_REFERENCE_PROVIDING_SIGNALS_THAT_SIMULATE_QC_RESULTS = "E"
    """Electronic QC, used with manufactured reference providing signals that simulate QC results"""
    SPECIMEN_USED_FOR_TESTING_PROFICIENCY_OF_THE_ORGANIZATION_PERFORMING_THE_TESTING = (
        "F"
    )
    """Specimen used for testing proficiency of the organization performing the testing (Filler)"""
    GROUP = "G"
    """Group (where a specimen consists of multiple individual elements that are not individually identified)"""
    POOL = "L"
    """Pool (aliquots of individual specimens combined to form a single specimen representing all of the components.)"""
    SPECIMEN_USED_FOR_TESTING_OPERATOR_PROFICIENCY = "O"
    """Specimen used for testing Operator Proficiency"""
    PATIENT = "P"
    """Patient (default if blank component value)"""
    CONTROL_SPECIMEN = "Q"
    """Control specimen"""
    REPLICATE = "R"
    """Replicate (of patient sample as a control)"""
    VERIFYING_CALIBRATOR_USED_FOR_PERIODIC_CALIBRATION_CHECKS = "V"
    """Verifying Calibrator, used for periodic calibration checks"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenRole.BLIND_SAMPLE: "Blind Sample",
    SpecimenRole.CALIBRATOR: "Calibrator",
    SpecimenRole.ELECTRONIC_QC_USED_WITH_MANUFACTURED_REFERENCE_PROVIDING_SIGNALS_THAT_SIMULATE_QC_RESULTS: "Electronic QC, used with manufactured reference providing signals that simulate QC results",
    SpecimenRole.SPECIMEN_USED_FOR_TESTING_PROFICIENCY_OF_THE_ORGANIZATION_PERFORMING_THE_TESTING: "Specimen used for testing proficiency of the organization performing the testing (Filler)",
    SpecimenRole.GROUP: "Group (where a specimen consists of multiple individual elements that are not individually identified)",
    SpecimenRole.POOL: "Pool (aliquots of individual specimens combined to form a single specimen representing all of the components.)",
    SpecimenRole.SPECIMEN_USED_FOR_TESTING_OPERATOR_PROFICIENCY: "Specimen used for testing Operator Proficiency",
    SpecimenRole.PATIENT: "Patient (default if blank component value)",
    SpecimenRole.CONTROL_SPECIMEN: "Control specimen",
    SpecimenRole.REPLICATE: "Replicate (of patient sample as a control)",
    SpecimenRole.VERIFYING_CALIBRATOR_USED_FOR_PERIODIC_CALIBRATION_CHECKS: "Verifying Calibrator, used for periodic calibration checks",
}
