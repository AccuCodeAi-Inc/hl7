from ...base import HL7Table

"""
HL7 Version: 2.5.1
TQ conjunction ID - 0472
Table Type: HL7
"""


class TqConjunctionId(HL7Table):
    """
    TQ conjunction ID - 0472 // HL7 table type
    - ASYNCHRONOUS
    - ACTUATION_TIME
    - SYNCHRONOUS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0472
    """

    ASYNCHRONOUS = "A"  # Do the next specification in parallel with this one (unless otherwise constrained by the following components: ORC-7^4-start date/time and ORC-7^5-end date/time). The conjunction of “A” specifies two parallel instructions, as are sometimes used in medication, e.g., prednisone given at 1 tab on Monday, Wednesday, Friday, and at 1/2 tab on Tuesday, Thursday, Saturday, Sunday.
    """Asynchronous"""
    ACTUATION_TIME = "C"  # It will be followed by a completion time for the service. This code allows one to distinguish between the time and priority at which a service should be actuated (e.g., blood should be drawn) and the time and priority at which a service should be completed (e.g., results should be reported). For continuous or periodic services, the point at which the service is actually stopped is determined by the components ORC-7^5-end date/time and ORC-7^3-duration, whichever indicates an earlier stopping time. Ordinarily, only one of these components would be present, but if one requested an EKG with the specification  ^1^QAM^X3^D10 then the EKG would be done for only three days since the number of repeats (3) defined the earlier stopping time.
    """Actuation Time"""
    SYNCHRONOUS = "S"  # Do the next specification after this one (unless otherwise constrained by the following components: ORC-7^4-start date/time and ORC-7^5-end date/time). An “S” specification implies that the second timing sequence follows the first, e.g., when an order is written to measure blood pressure Q15 minutes for the 1st hour, then every 2 hours for the next day.
    """Synchronous"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TqConjunctionId.ASYNCHRONOUS: "Asynchronous",
    TqConjunctionId.ACTUATION_TIME: "Actuation Time",
    TqConjunctionId.SYNCHRONOUS: "Synchronous",
}
