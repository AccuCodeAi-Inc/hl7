from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen Action Code - 0065
Table Type: HL7
"""


class SpecimenActionCode(HL7Table):
    """
    Specimen Action Code - 0065 // HL7 table type
    - ADD_ORDERED_TESTS_TO_THE_EXISTING_SPECIMEN
    - GENERATED_ORDER_REFLEX_ORDER
    - LAB_TO_OBTAIN_SPECIMEN_FROM_PATIENT
    - SPECIMEN_OBTAINED_BY_SERVICE_OTHER_THAN_LAB
    - PENDING_SPECIMEN_ORDER_SENT_PRIOR_TO_DELIVERY
    - REVISED_ORDER
    - SCHEDULE_THE_TESTS_SPECIFIED_BELOW
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0065
    """

    ADD_ORDERED_TESTS_TO_THE_EXISTING_SPECIMEN = "A"
    """Add ordered tests to the existing specimen"""
    GENERATED_ORDER_REFLEX_ORDER = "G"
    """Generated order; reflex order"""
    LAB_TO_OBTAIN_SPECIMEN_FROM_PATIENT = "L"
    """Lab to obtain specimen from patient"""
    SPECIMEN_OBTAINED_BY_SERVICE_OTHER_THAN_LAB = "O"
    """Specimen obtained by service other than Lab"""
    PENDING_SPECIMEN_ORDER_SENT_PRIOR_TO_DELIVERY = "P"
    """Pending specimen; Order sent prior to delivery"""
    REVISED_ORDER = "R"
    """Revised order"""
    SCHEDULE_THE_TESTS_SPECIFIED_BELOW = "S"
    """Schedule the tests specified below"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenActionCode.ADD_ORDERED_TESTS_TO_THE_EXISTING_SPECIMEN: "Add ordered tests to the existing specimen",
    SpecimenActionCode.GENERATED_ORDER_REFLEX_ORDER: "Generated order; reflex order",
    SpecimenActionCode.LAB_TO_OBTAIN_SPECIMEN_FROM_PATIENT: "Lab to obtain specimen from patient",
    SpecimenActionCode.SPECIMEN_OBTAINED_BY_SERVICE_OTHER_THAN_LAB: "Specimen obtained by service other than Lab",
    SpecimenActionCode.PENDING_SPECIMEN_ORDER_SENT_PRIOR_TO_DELIVERY: "Pending specimen; Order sent prior to delivery",
    SpecimenActionCode.REVISED_ORDER: "Revised order",
    SpecimenActionCode.SCHEDULE_THE_TESTS_SPECIFIED_BELOW: "Schedule the tests specified below",
}
