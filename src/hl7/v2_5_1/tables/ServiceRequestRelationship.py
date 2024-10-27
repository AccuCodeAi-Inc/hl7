from ...base import HL7Table

"""
HL7 Version: 2.5.1
Service Request Relationship - 0506
Table Type: HL7
"""


class ServiceRequestRelationship(HL7Table):
    """
    Service Request Relationship - 0506 // HL7 table type
    - COMPOUND
    - EXCLUSIVE
    - NURSE_PREROGATIVE
    - SIMULTANEOUS
    - TAPERING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0506
    """

    COMPOUND = "C"  # A compound is an extempo order which may be made up of multiple drugs.  For example, many hospitals have a standard item called Magic Mouthwash.  The item is ordered that way by the physician. The extempo items will contain multiple products, such as Maalox, Benadryl, Xylocaine, etc.  They will all be mixed together and will be dispensed in a single container.
    """Compound"""
    EXCLUSIVE = "E"  # An exclusive order is an order where only one of the multiple items should be administered at any one dosage time.  The nurse may chose between the alternatives, but should only give ONE of them.  An example would be: Phenergan 25 mg PO, IM or R q6h prn (orally, intramuscularly, or rectally every 6 hours as needed).
    """Exclusive"""
    NURSE_PREROGATIVE = "N"  # Where a set of two or more orders exist and the Nurse, or other caregiver, has the prerogative to choose which order will be administered at a particular point in time.  For example, Milk of Magnesia PO 30 ml qhs (at bedtime)                 Dulcolax Supp R @ hs prn Colace 100 mg capsule PO bid The nurse would be administering MOM, but may add the Colace and may also give the Dulcolax Supp as needed to promote and maintain regularity.
    """Nurse prerogative"""
    SIMULTANEOUS = "S"  # A simultaneous order is 2 or more drugs which are ordered to be given at the same time.  A common example of this would be Demerol and Phenergan (Phenergan is given with the Demerol to control the nausea that Demerol can cause).  The order could be: Demerol 50 mg IM with Phenergan 25 mg IM q4h prn (every 4 hours as needed).
    """Simultaneous"""
    TAPERING = "T"  # A tapering order is one in which the same drug is used, but it has a declining dosage over a number of days. For example, Decadron 0.5 mg is often ordered this way.  The order would look like this: Decadron 0.5 mg qid (four times a day) for 2 days, then Decadron 0.5 mg tid (three times a day) for 2 days, then Decadron 0.5 mg bid (twice a day) for 2 days, then Decadron 0.5 mg qd (daily) for 2 days, then stop.
    """Tapering"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ServiceRequestRelationship.COMPOUND: "Compound",
    ServiceRequestRelationship.EXCLUSIVE: "Exclusive",
    ServiceRequestRelationship.NURSE_PREROGATIVE: "Nurse prerogative",
    ServiceRequestRelationship.SIMULTANEOUS: "Simultaneous",
    ServiceRequestRelationship.TAPERING: "Tapering",
}
