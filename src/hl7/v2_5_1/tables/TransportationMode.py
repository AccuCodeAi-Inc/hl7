from ...base import HL7Table

"""
HL7 Version: 2.5.1
Transportation Mode - 0124
Table Type: HL7
"""


class TransportationMode(HL7Table):
    """
    Transportation Mode - 0124 // HL7 table type
    - CART_PATIENT_TRAVELS_ON_CART_OR_GURNEY
    - THE_EXAMINING_DEVICE_GOES_TO_PATIENTS_LOCATION
    - PATIENT_WALKS_TO_DIAGNOSTIC_SERVICE
    - WHEELCHAIR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0124
    """

    CART_PATIENT_TRAVELS_ON_CART_OR_GURNEY = "CART"
    """Cart - patient travels on cart or gurney"""
    THE_EXAMINING_DEVICE_GOES_TO_PATIENTS_LOCATION = "PORT"
    """The examining device goes to patients location"""
    PATIENT_WALKS_TO_DIAGNOSTIC_SERVICE = "WALK"
    """Patient walks to diagnostic service"""
    WHEELCHAIR = "WHLC"
    """Wheelchair"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TransportationMode.CART_PATIENT_TRAVELS_ON_CART_OR_GURNEY: "Cart - patient travels on cart or gurney",
    TransportationMode.THE_EXAMINING_DEVICE_GOES_TO_PATIENTS_LOCATION: "The examining device goes to patients location",
    TransportationMode.PATIENT_WALKS_TO_DIAGNOSTIC_SERVICE: "Patient walks to diagnostic service",
    TransportationMode.WHEELCHAIR: "Wheelchair",
}
