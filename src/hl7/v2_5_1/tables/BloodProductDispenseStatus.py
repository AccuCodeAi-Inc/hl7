from ...base import HL7Table

"""
HL7 Version: 2.5.1
Blood Product Dispense Status - 0510
Table Type: HL7
"""


class BloodProductDispenseStatus(HL7Table):
    """
    Blood Product Dispense Status - 0510 // HL7 table type
    - RELEASED_INTO_INVENTORY_FOR_GENERAL_AVAILABILITY
    - DISPENSED_TO_PATIENT_LOCATION
    - PRESUMED_TRANSFUSED
    - RETURNED_UNUSED_OR_NO_LONGER_NEEDED
    - RESERVED_AND_READY_TO_DISPENSE
    - RELEASED
    - RECEIVED_INTO_INVENTORY
    - RETURNED_UNUSED_OR_KEEP_LINKED_TO_PATIENT_FOR_POSSIBLE_USE_LATER
    - REQUEST_TO_DISPENSE_BLOOD_PRODUCT
    - RESERVED
    - WASTED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0510
    """

    RELEASED_INTO_INVENTORY_FOR_GENERAL_AVAILABILITY = (
        "CR"  # Status determined by Filler
    )
    """Released into inventory for general availability"""
    DISPENSED_TO_PATIENT_LOCATION = "DS"  # Status determined by Filler
    """Dispensed to patient location"""
    PRESUMED_TRANSFUSED = "PT"  # Status determined by Filler
    """Presumed transfused (dispensed and not returned)"""
    RETURNED_UNUSED_OR_NO_LONGER_NEEDED = "RA"  # Status determined by Filler
    """Returned unused/no longer needed"""
    RESERVED_AND_READY_TO_DISPENSE = "RD"  # Status determined by Filler
    """Reserved and ready to dispense"""
    RELEASED = "RE"  # Status determined by Placer or Filler
    """Released (no longer allocated for the patient)"""
    RECEIVED_INTO_INVENTORY = "RI"  # Status determined by Filler
    """Received into inventory (for specified patient)"""
    RETURNED_UNUSED_OR_KEEP_LINKED_TO_PATIENT_FOR_POSSIBLE_USE_LATER = (
        "RL"  # Status determined by Filler
    )
    """Returned unused/keep linked to patient for possible use later"""
    REQUEST_TO_DISPENSE_BLOOD_PRODUCT = "RQ"  # Status determined by Placer
    """Request to dispense blood product"""
    RESERVED = "RS"  # Status determined by Filler
    """Reserved (ordered and product allocated for the patient)"""
    WASTED = "WA"  # Status determined by Filler
    """Wasted (product no longer viable)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    BloodProductDispenseStatus.RELEASED_INTO_INVENTORY_FOR_GENERAL_AVAILABILITY: "Released into inventory for general availability",
    BloodProductDispenseStatus.DISPENSED_TO_PATIENT_LOCATION: "Dispensed to patient location",
    BloodProductDispenseStatus.PRESUMED_TRANSFUSED: "Presumed transfused (dispensed and not returned)",
    BloodProductDispenseStatus.RETURNED_UNUSED_OR_NO_LONGER_NEEDED: "Returned unused/no longer needed",
    BloodProductDispenseStatus.RESERVED_AND_READY_TO_DISPENSE: "Reserved and ready to dispense",
    BloodProductDispenseStatus.RELEASED: "Released (no longer allocated for the patient)",
    BloodProductDispenseStatus.RECEIVED_INTO_INVENTORY: "Received into inventory (for specified patient)",
    BloodProductDispenseStatus.RETURNED_UNUSED_OR_KEEP_LINKED_TO_PATIENT_FOR_POSSIBLE_USE_LATER: "Returned unused/keep linked to patient for possible use later",
    BloodProductDispenseStatus.REQUEST_TO_DISPENSE_BLOOD_PRODUCT: "Request to dispense blood product",
    BloodProductDispenseStatus.RESERVED: "Reserved (ordered and product allocated for the patient)",
    BloodProductDispenseStatus.WASTED: "Wasted (product no longer viable)",
}
