from ...base import HL7Table

"""
HL7 Version: 2.5.1
Derived specimen - 0170
Table Type: HL7
"""


class DerivedSpecimen(HL7Table):
    """
    Derived specimen - 0170 // HL7 table type
    - CHILD_OBSERVATION
    - NOT_APPLICABLE
    - PARENT_OBSERVATION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0170
    """

    CHILD_OBSERVATION = "C"
    """Child Observation"""
    NOT_APPLICABLE = "N"
    """Not Applicable"""
    PARENT_OBSERVATION = "P"
    """Parent Observation"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DerivedSpecimen.CHILD_OBSERVATION: "Child Observation",
    DerivedSpecimen.NOT_APPLICABLE: "Not Applicable",
    DerivedSpecimen.PARENT_OBSERVATION: "Parent Observation",
}
