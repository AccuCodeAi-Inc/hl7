from ...base import HL7Table

"""
HL7 Version: 2.5.1
Causality Observations - 0252
Table Type: HL7
"""


class CausalityObservations(HL7Table):
    """
    Causality Observations - 0252 // HL7 table type
    - ABATEMENT_OF_EVENT_AFTER_PRODUCT_WITHDRAWN
    - EVENT_RECURRED_AFTER_PRODUCT_REINTRODUCED
    - DOSE_RESPONSE_OBSERVED
    - ALTERNATIVE_EXPLANATIONS_FOR_THE_EVENT_AVAILABLE
    - EVENT_OCCURRED_AFTER_PRODUCT_INTRODUCED
    - LITERATURE_REPORTS_ASSOCIATION_OF_PRODUCT_WITH_EVENT
    - OCCURRENCE_OF_EVENT_WAS_CONFIRMED_BY_OBJECTIVE_EVIDENCE
    - OTHER
    - EFFECT_OBSERVED_WHEN_PATIENT_RECEIVES_PLACEBO
    - SIMILAR_EVENTS_IN_PAST_FOR_THIS_PATIENT
    - TOXIC_LEVELS_OF_PRODUCT_DOCUMENTED_IN_BLOOD_OR_BODY_FLUIDS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0252
    """

    ABATEMENT_OF_EVENT_AFTER_PRODUCT_WITHDRAWN = "AW"
    """Abatement of event after product withdrawn"""
    EVENT_RECURRED_AFTER_PRODUCT_REINTRODUCED = "BE"
    """Event recurred after product reintroduced"""
    DOSE_RESPONSE_OBSERVED = "DR"
    """Dose response observed"""
    ALTERNATIVE_EXPLANATIONS_FOR_THE_EVENT_AVAILABLE = "EX"
    """Alternative explanations for the event available"""
    EVENT_OCCURRED_AFTER_PRODUCT_INTRODUCED = "IN"
    """Event occurred after product introduced"""
    LITERATURE_REPORTS_ASSOCIATION_OF_PRODUCT_WITH_EVENT = "LI"
    """Literature reports association of product with event"""
    OCCURRENCE_OF_EVENT_WAS_CONFIRMED_BY_OBJECTIVE_EVIDENCE = "OE"
    """Occurrence of event was confirmed by objective evidence"""
    OTHER = "OT"
    """Other"""
    EFFECT_OBSERVED_WHEN_PATIENT_RECEIVES_PLACEBO = "PL"
    """Effect observed when patient receives placebo"""
    SIMILAR_EVENTS_IN_PAST_FOR_THIS_PATIENT = "SE"
    """Similar events in past for this patient"""
    TOXIC_LEVELS_OF_PRODUCT_DOCUMENTED_IN_BLOOD_OR_BODY_FLUIDS = "TC"
    """Toxic levels of product documented in blood or body fluids"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CausalityObservations.ABATEMENT_OF_EVENT_AFTER_PRODUCT_WITHDRAWN: "Abatement of event after product withdrawn",
    CausalityObservations.EVENT_RECURRED_AFTER_PRODUCT_REINTRODUCED: "Event recurred after product reintroduced",
    CausalityObservations.DOSE_RESPONSE_OBSERVED: "Dose response observed",
    CausalityObservations.ALTERNATIVE_EXPLANATIONS_FOR_THE_EVENT_AVAILABLE: "Alternative explanations for the event available",
    CausalityObservations.EVENT_OCCURRED_AFTER_PRODUCT_INTRODUCED: "Event occurred after product introduced",
    CausalityObservations.LITERATURE_REPORTS_ASSOCIATION_OF_PRODUCT_WITH_EVENT: "Literature reports association of product with event",
    CausalityObservations.OCCURRENCE_OF_EVENT_WAS_CONFIRMED_BY_OBJECTIVE_EVIDENCE: "Occurrence of event was confirmed by objective evidence",
    CausalityObservations.OTHER: "Other",
    CausalityObservations.EFFECT_OBSERVED_WHEN_PATIENT_RECEIVES_PLACEBO: "Effect observed when patient receives placebo",
    CausalityObservations.SIMILAR_EVENTS_IN_PAST_FOR_THIS_PATIENT: "Similar events in past for this patient",
    CausalityObservations.TOXIC_LEVELS_OF_PRODUCT_DOCUMENTED_IN_BLOOD_OR_BODY_FLUIDS: "Toxic levels of product documented in blood or body fluids",
}
