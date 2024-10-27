from ...base import HL7Table

"""
HL7 Version: 2.5.1
Observation Result Handling - 0507
Table Type: User
"""


class ObservationResultHandling(HL7Table):
    """
    Observation Result Handling - 0507 // User table type
    - FILM_WITH_PATIENT
    - NOTIFY_PROVIDER_WHEN_READY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0507
    """

    FILM_WITH_PATIENT = "F"
    """Film-with-patient"""
    NOTIFY_PROVIDER_WHEN_READY = "N"
    """Notify provider when ready"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ObservationResultHandling.FILM_WITH_PATIENT: "Film-with-patient",
    ObservationResultHandling.NOTIFY_PROVIDER_WHEN_READY: "Notify provider when ready",
}
