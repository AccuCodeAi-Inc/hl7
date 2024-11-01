from __future__ import annotations
from ...base import HL7Segment
from ..data_types.XPN import XPN
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.CE import CE
from ..data_types.XTN import XTN
from ..data_types.XAD import XAD
from ..data_types.FT import FT
from ..tables.EventConsequence import EventConsequence
from ..tables.PrimaryObserverSQualification import PrimaryObserverSQualification
from ..tables.EventExpected import EventExpected
from ..tables.PatientOutcome import PatientOutcome
from ..tables.EventQualification import EventQualification
from ..tables.IdentityMayBeDivulged import IdentityMayBeDivulged
from ..tables.EventSeriousness import EventSeriousness


"""
Product Experience Observation - PEO
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PEO TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PEO,
    XPN, TS, ID, CE, XTN, XAD, FT
)

peo = PEO(  #  - Details related to a particular clinical experience or event are embodied in the PEO segment
    event_identifiers_used=None,  # CE(...) 
    event_symptom_or_diagnosis_code=None,  # CE(...) 
    event_onset_date_or_time=ts,  # TS(...)  # Required.
    event_exacerbation_date_or_time=None,  # TS(...) 
    event_improved_date_or_time=None,  # TS(...) 
    event_ended_data_or_time=None,  # TS(...) 
    event_location_occurred_address=None,  # XAD(...) 
    event_qualification=None,  # ID(...) 
    event_serious=None,  # ID(...) 
    event_expected=None,  # ID(...) 
    event_outcome=None,  # ID(...) 
    patient_outcome=None,  # ID(...) 
    event_description_from_others=None,  # FT(...) 
    event_from_original_reporter=None,  # FT(...) 
    event_description_from_patient=None,  # FT(...) 
    event_description_from_practitioner=None,  # FT(...) 
    event_description_from_autopsy=None,  # FT(...) 
    cause_of_death=None,  # CE(...) 
    primary_observer_name=None,  # XPN(...) 
    primary_observer_address=None,  # XAD(...) 
    primary_observer_telephone=None,  # XTN(...) 
    primary_observers_qualification=None,  # ID(...) 
    confirmation_provided_by=None,  # ID(...) 
    primary_observer_aware_date_or_time=None,  # TS(...) 
    primary_observers_identity_may_be_divulged=None,  # ID(...) 
)

-----END SEGMENT::PEO TEMPLATE-----
"""


class PEO(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PEO"""
    _hl7_name = """Product Experience Observation"""
    _hl7_description = """Details related to a particular clinical experience or event are embodied in the PEO segment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEO"
    _c_length = (250, 250, 26, 26, 26, 26, 250, 1, 1, 1, 1, 1, 600, 600, 600, 600, 600, 250, 250, 250, 250, 1, 1, 26, 1,)
    _c_rpt = (65535, 65535, 1, 1, 1, 1, 65535, 65535, 1, 1, 65535, 1, 65535, 65535, 65535, 65535, 65535, 65535, 65535, 65535, 65535, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, CE, TS, TS, TS, TS, XAD, ID, ID, ID, ID, ID, FT, FT, FT, FT, FT, CE, XPN, XAD, XTN, ID, ID, TS, ID,)
    _c_aliases = ("PEO.1", "PEO.2", "PEO.3", "PEO.4", "PEO.5", "PEO.6", "PEO.7", "PEO.8", "PEO.9", "PEO.10", "PEO.11", "PEO.12", "PEO.13", "PEO.14", "PEO.15", "PEO.16", "PEO.17", "PEO.18", "PEO.19", "PEO.20", "PEO.21", "PEO.22", "PEO.23", "PEO.24", "PEO.25",)
    _c_names = ("Event Identifiers Used", "Event Symptom/Diagnosis Code", "Event Onset Date/Time", "Event Exacerbation Date/Time", "Event Improved Date/Time", "Event Ended Data/Time", "Event Location Occurred Address", "Event Qualification", "Event Serious", "Event Expected", "Event Outcome", "Patient Outcome", "Event Description From Others", "Event From Original Reporter", "Event Description From Patient", "Event Description From Practitioner", "Event Description From Autopsy", "Cause Of Death", "Primary Observer Name", "Primary Observer Address", "Primary Observer Telephone", "Primary Observer's Qualification", "Confirmation Provided By", "Primary Observer Aware Date/Time", "Primary Observer's identity May Be Divulged",)
    _c_attrs = ("event_identifiers_used", "event_symptom_or_diagnosis_code", "event_onset_date_or_time", "event_exacerbation_date_or_time", "event_improved_date_or_time", "event_ended_data_or_time", "event_location_occurred_address", "event_qualification", "event_serious", "event_expected", "event_outcome", "patient_outcome", "event_description_from_others", "event_from_original_reporter", "event_description_from_patient", "event_description_from_practitioner", "event_description_from_autopsy", "cause_of_death", "primary_observer_name", "primary_observer_address", "primary_observer_telephone", "primary_observers_qualification", "confirmation_provided_by", "primary_observer_aware_date_or_time", "primary_observers_identity_may_be_divulged",)
    # fmt: on

    def __init__(
        self,
        event_onset_date_or_time: TS | tuple[TS],  # PEO.3
        event_identifiers_used: CE | tuple[CE] | None = None,  # PEO.1
        event_symptom_or_diagnosis_code: CE | tuple[CE] | None = None,  # PEO.2
        event_exacerbation_date_or_time: TS | tuple[TS] | None = None,  # PEO.4
        event_improved_date_or_time: TS | tuple[TS] | None = None,  # PEO.5
        event_ended_data_or_time: TS | tuple[TS] | None = None,  # PEO.6
        event_location_occurred_address: XAD | tuple[XAD] | None = None,  # PEO.7
        event_qualification: EventQualification
        | ID
        | tuple[EventQualification | ID]
        | None = None,  # PEO.8
        event_serious: EventSeriousness
        | ID
        | tuple[EventSeriousness | ID]
        | None = None,  # PEO.9
        event_expected: EventExpected
        | ID
        | tuple[EventExpected | ID]
        | None = None,  # PEO.10
        event_outcome: EventConsequence
        | ID
        | tuple[EventConsequence | ID]
        | None = None,  # PEO.11
        patient_outcome: PatientOutcome
        | ID
        | tuple[PatientOutcome | ID]
        | None = None,  # PEO.12
        event_description_from_others: FT | tuple[FT] | None = None,  # PEO.13
        event_from_original_reporter: FT | tuple[FT] | None = None,  # PEO.14
        event_description_from_patient: FT | tuple[FT] | None = None,  # PEO.15
        event_description_from_practitioner: FT | tuple[FT] | None = None,  # PEO.16
        event_description_from_autopsy: FT | tuple[FT] | None = None,  # PEO.17
        cause_of_death: CE | tuple[CE] | None = None,  # PEO.18
        primary_observer_name: XPN | tuple[XPN] | None = None,  # PEO.19
        primary_observer_address: XAD | tuple[XAD] | None = None,  # PEO.20
        primary_observer_telephone: XTN | tuple[XTN] | None = None,  # PEO.21
        primary_observers_qualification: PrimaryObserverSQualification
        | ID
        | tuple[PrimaryObserverSQualification | ID]
        | None = None,  # PEO.22
        confirmation_provided_by: PrimaryObserverSQualification
        | ID
        | tuple[PrimaryObserverSQualification | ID]
        | None = None,  # PEO.23
        primary_observer_aware_date_or_time: TS | tuple[TS] | None = None,  # PEO.24
        primary_observers_identity_may_be_divulged: IdentityMayBeDivulged
        | ID
        | tuple[IdentityMayBeDivulged | ID]
        | None = None,  # PEO.25
    ):
        """
        Product Experience Observation - `PEO <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEO>`_
        Details related to a particular clinical experience or event are embodied in the PEO segment. This segment can be used to characterize an event which might be attributed to a product to which the patient was exposed. Products with a possible causal relationship to the observed experience are described in the following PCR (possible causal relationship) segments. The message format was designed to be robust and includes many optional elements which may not be required for a particular regulatory purpose but allow a complete representation of the drug experience if needed.

        :param event_identifiers_used: Coded Element (id: PEO.1 | len: 250 | use: O | rpt: *)
        :param event_symptom_or_diagnosis_code: Coded Element (id: PEO.2 | len: 250 | use: O | rpt: *)
        :param event_onset_date_or_time: Time Stamp (id: PEO.3 | len: 26 | use: R | rpt: 1)
        :param event_exacerbation_date_or_time: Time Stamp (id: PEO.4 | len: 26 | use: O | rpt: 1)
        :param event_improved_date_or_time: Time Stamp (id: PEO.5 | len: 26 | use: O | rpt: 1)
        :param event_ended_data_or_time: Time Stamp (id: PEO.6 | len: 26 | use: O | rpt: 1)
        :param event_location_occurred_address: Extended Address (id: PEO.7 | len: 250 | use: O | rpt: *)
        :param event_qualification: Coded values for HL7 tables (id: PEO.8 | len: 1 | use: O | rpt: *)
        :param event_serious: Coded values for HL7 tables (id: PEO.9 | len: 1 | use: O | rpt: 1)
        :param event_expected: Coded values for HL7 tables (id: PEO.10 | len: 1 | use: O | rpt: 1)
        :param event_outcome: Coded values for HL7 tables (id: PEO.11 | len: 1 | use: O | rpt: *)
        :param patient_outcome: Coded values for HL7 tables (id: PEO.12 | len: 1 | use: O | rpt: 1)
        :param event_description_from_others: Formatted Text Data (id: PEO.13 | len: 600 | use: O | rpt: *)
        :param event_from_original_reporter: Formatted Text Data (id: PEO.14 | len: 600 | use: O | rpt: *)
        :param event_description_from_patient: Formatted Text Data (id: PEO.15 | len: 600 | use: O | rpt: *)
        :param event_description_from_practitioner: Formatted Text Data (id: PEO.16 | len: 600 | use: O | rpt: *)
        :param event_description_from_autopsy: Formatted Text Data (id: PEO.17 | len: 600 | use: O | rpt: *)
        :param cause_of_death: Coded Element (id: PEO.18 | len: 250 | use: O | rpt: *)
        :param primary_observer_name: Extended Person Name (id: PEO.19 | len: 250 | use: O | rpt: *)
        :param primary_observer_address: Extended Address (id: PEO.20 | len: 250 | use: O | rpt: *)
        :param primary_observer_telephone: Extended Telecommunication Number (id: PEO.21 | len: 250 | use: O | rpt: *)
        :param primary_observers_qualification: Coded values for HL7 tables (id: PEO.22 | len: 1 | use: O | rpt: 1)
        :param confirmation_provided_by: Coded values for HL7 tables (id: PEO.23 | len: 1 | use: O | rpt: 1)
        :param primary_observer_aware_date_or_time: Time Stamp (id: PEO.24 | len: 26 | use: O | rpt: 1)
        :param primary_observers_identity_may_be_divulged: Coded values for HL7 tables (id: PEO.25 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 25
        self.event_identifiers_used = event_identifiers_used
        self.event_symptom_or_diagnosis_code = event_symptom_or_diagnosis_code
        self.event_onset_date_or_time = event_onset_date_or_time
        self.event_exacerbation_date_or_time = event_exacerbation_date_or_time
        self.event_improved_date_or_time = event_improved_date_or_time
        self.event_ended_data_or_time = event_ended_data_or_time
        self.event_location_occurred_address = event_location_occurred_address
        self.event_qualification = event_qualification
        self.event_serious = event_serious
        self.event_expected = event_expected
        self.event_outcome = event_outcome
        self.patient_outcome = patient_outcome
        self.event_description_from_others = event_description_from_others
        self.event_from_original_reporter = event_from_original_reporter
        self.event_description_from_patient = event_description_from_patient
        self.event_description_from_practitioner = event_description_from_practitioner
        self.event_description_from_autopsy = event_description_from_autopsy
        self.cause_of_death = cause_of_death
        self.primary_observer_name = primary_observer_name
        self.primary_observer_address = primary_observer_address
        self.primary_observer_telephone = primary_observer_telephone
        self.primary_observers_qualification = primary_observers_qualification
        self.confirmation_provided_by = confirmation_provided_by
        self.primary_observer_aware_date_or_time = primary_observer_aware_date_or_time
        self.primary_observers_identity_may_be_divulged = (
            primary_observers_identity_may_be_divulged
        )

    @property
    def event_identifiers_used(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: PEO.1 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.1
        """
        return self._c_data[0]

    @event_identifiers_used.setter  # set PEO.1
    def event_identifiers_used(self, ce: CE | tuple[CE] | None):
        """
        id: PEO.1 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.1
        """
        if isinstance(ce, tuple):
            self._c_data[0] = ce
        else:
            self._c_data[0] = (ce,)

    @property
    def event_symptom_or_diagnosis_code(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: PEO.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.2
        """
        return self._c_data[1]

    @event_symptom_or_diagnosis_code.setter  # set PEO.2
    def event_symptom_or_diagnosis_code(self, ce: CE | tuple[CE] | None):
        """
        id: PEO.2 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.2
        """
        if isinstance(ce, tuple):
            self._c_data[1] = ce
        else:
            self._c_data[1] = (ce,)

    @property  # get PEO.3
    def event_onset_date_or_time(self) -> TS:
        """
        id: PEO.3 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.3
        """
        return self._c_data[2][0]

    @event_onset_date_or_time.setter  # set PEO.3
    def event_onset_date_or_time(self, ts: TS):
        """
        id: PEO.3 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.3
        """
        self._c_data[2] = (ts,)

    @property  # get PEO.4
    def event_exacerbation_date_or_time(self) -> TS | None:
        """
        id: PEO.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.4
        """
        return self._c_data[3][0]

    @event_exacerbation_date_or_time.setter  # set PEO.4
    def event_exacerbation_date_or_time(self, ts: TS | None):
        """
        id: PEO.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.4
        """
        self._c_data[3] = (ts,)

    @property  # get PEO.5
    def event_improved_date_or_time(self) -> TS | None:
        """
        id: PEO.5 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.5
        """
        return self._c_data[4][0]

    @event_improved_date_or_time.setter  # set PEO.5
    def event_improved_date_or_time(self, ts: TS | None):
        """
        id: PEO.5 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.5
        """
        self._c_data[4] = (ts,)

    @property  # get PEO.6
    def event_ended_data_or_time(self) -> TS | None:
        """
        id: PEO.6 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.6
        """
        return self._c_data[5][0]

    @event_ended_data_or_time.setter  # set PEO.6
    def event_ended_data_or_time(self, ts: TS | None):
        """
        id: PEO.6 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.6
        """
        self._c_data[5] = (ts,)

    @property
    def event_location_occurred_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: PEO.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.7
        """
        return self._c_data[6]

    @event_location_occurred_address.setter  # set PEO.7
    def event_location_occurred_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: PEO.7 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.7
        """
        if isinstance(xad, tuple):
            self._c_data[6] = xad
        else:
            self._c_data[6] = (xad,)

    @property
    def event_qualification(self) -> tuple[EventQualification, ...] | tuple[None]:
        """
        id: PEO.8 | len: 1 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.8
        """
        return self._c_data[7]

    @event_qualification.setter  # set PEO.8
    def event_qualification(
        self, event_qualification: EventQualification | tuple[EventQualification] | None
    ):
        """
        id: PEO.8 | len: 1 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.8
        """
        if isinstance(event_qualification, tuple):
            self._c_data[7] = event_qualification
        else:
            self._c_data[7] = (event_qualification,)

    @property  # get PEO.9
    def event_serious(self) -> EventSeriousness | None:
        """
        id: PEO.9 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.9
        """
        return self._c_data[8][0]

    @event_serious.setter  # set PEO.9
    def event_serious(self, event_seriousness: EventSeriousness | None):
        """
        id: PEO.9 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.9
        """
        self._c_data[8] = (event_seriousness,)

    @property  # get PEO.10
    def event_expected(self) -> EventExpected | None:
        """
        id: PEO.10 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.10
        """
        return self._c_data[9][0]

    @event_expected.setter  # set PEO.10
    def event_expected(self, event_expected: EventExpected | None):
        """
        id: PEO.10 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.10
        """
        self._c_data[9] = (event_expected,)

    @property
    def event_outcome(self) -> tuple[EventConsequence, ...] | tuple[None]:
        """
        id: PEO.11 | len: 1 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.11
        """
        return self._c_data[10]

    @event_outcome.setter  # set PEO.11
    def event_outcome(
        self, event_consequence: EventConsequence | tuple[EventConsequence] | None
    ):
        """
        id: PEO.11 | len: 1 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.11
        """
        if isinstance(event_consequence, tuple):
            self._c_data[10] = event_consequence
        else:
            self._c_data[10] = (event_consequence,)

    @property  # get PEO.12
    def patient_outcome(self) -> PatientOutcome | None:
        """
        id: PEO.12 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.12
        """
        return self._c_data[11][0]

    @patient_outcome.setter  # set PEO.12
    def patient_outcome(self, patient_outcome: PatientOutcome | None):
        """
        id: PEO.12 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.12
        """
        self._c_data[11] = (patient_outcome,)

    @property
    def event_description_from_others(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: PEO.13 | len: 600 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.13
        """
        return self._c_data[12]

    @event_description_from_others.setter  # set PEO.13
    def event_description_from_others(self, ft: FT | tuple[FT] | None):
        """
        id: PEO.13 | len: 600 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.13
        """
        if isinstance(ft, tuple):
            self._c_data[12] = ft
        else:
            self._c_data[12] = (ft,)

    @property
    def event_from_original_reporter(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: PEO.14 | len: 600 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.14
        """
        return self._c_data[13]

    @event_from_original_reporter.setter  # set PEO.14
    def event_from_original_reporter(self, ft: FT | tuple[FT] | None):
        """
        id: PEO.14 | len: 600 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.14
        """
        if isinstance(ft, tuple):
            self._c_data[13] = ft
        else:
            self._c_data[13] = (ft,)

    @property
    def event_description_from_patient(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: PEO.15 | len: 600 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.15
        """
        return self._c_data[14]

    @event_description_from_patient.setter  # set PEO.15
    def event_description_from_patient(self, ft: FT | tuple[FT] | None):
        """
        id: PEO.15 | len: 600 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.15
        """
        if isinstance(ft, tuple):
            self._c_data[14] = ft
        else:
            self._c_data[14] = (ft,)

    @property
    def event_description_from_practitioner(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: PEO.16 | len: 600 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.16
        """
        return self._c_data[15]

    @event_description_from_practitioner.setter  # set PEO.16
    def event_description_from_practitioner(self, ft: FT | tuple[FT] | None):
        """
        id: PEO.16 | len: 600 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.16
        """
        if isinstance(ft, tuple):
            self._c_data[15] = ft
        else:
            self._c_data[15] = (ft,)

    @property
    def event_description_from_autopsy(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: PEO.17 | len: 600 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.17
        """
        return self._c_data[16]

    @event_description_from_autopsy.setter  # set PEO.17
    def event_description_from_autopsy(self, ft: FT | tuple[FT] | None):
        """
        id: PEO.17 | len: 600 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.17
        """
        if isinstance(ft, tuple):
            self._c_data[16] = ft
        else:
            self._c_data[16] = (ft,)

    @property
    def cause_of_death(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: PEO.18 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.18
        """
        return self._c_data[17]

    @cause_of_death.setter  # set PEO.18
    def cause_of_death(self, ce: CE | tuple[CE] | None):
        """
        id: PEO.18 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.18
        """
        if isinstance(ce, tuple):
            self._c_data[17] = ce
        else:
            self._c_data[17] = (ce,)

    @property
    def primary_observer_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: PEO.19 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.19
        """
        return self._c_data[18]

    @primary_observer_name.setter  # set PEO.19
    def primary_observer_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: PEO.19 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.19
        """
        if isinstance(xpn, tuple):
            self._c_data[18] = xpn
        else:
            self._c_data[18] = (xpn,)

    @property
    def primary_observer_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: PEO.20 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.20
        """
        return self._c_data[19]

    @primary_observer_address.setter  # set PEO.20
    def primary_observer_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: PEO.20 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.20
        """
        if isinstance(xad, tuple):
            self._c_data[19] = xad
        else:
            self._c_data[19] = (xad,)

    @property
    def primary_observer_telephone(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: PEO.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.21
        """
        return self._c_data[20]

    @primary_observer_telephone.setter  # set PEO.21
    def primary_observer_telephone(self, xtn: XTN | tuple[XTN] | None):
        """
        id: PEO.21 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.21
        """
        if isinstance(xtn, tuple):
            self._c_data[20] = xtn
        else:
            self._c_data[20] = (xtn,)

    @property  # get PEO.22
    def primary_observers_qualification(self) -> PrimaryObserverSQualification | None:
        """
        id: PEO.22 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.22
        """
        return self._c_data[21][0]

    @primary_observers_qualification.setter  # set PEO.22
    def primary_observers_qualification(
        self, primary_observers_qualification: PrimaryObserverSQualification | None
    ):
        """
        id: PEO.22 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.22
        """
        self._c_data[21] = (primary_observers_qualification,)

    @property  # get PEO.23
    def confirmation_provided_by(self) -> PrimaryObserverSQualification | None:
        """
        id: PEO.23 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.23
        """
        return self._c_data[22][0]

    @confirmation_provided_by.setter  # set PEO.23
    def confirmation_provided_by(
        self, primary_observers_qualification: PrimaryObserverSQualification | None
    ):
        """
        id: PEO.23 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.23
        """
        self._c_data[22] = (primary_observers_qualification,)

    @property  # get PEO.24
    def primary_observer_aware_date_or_time(self) -> TS | None:
        """
        id: PEO.24 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.24
        """
        return self._c_data[23][0]

    @primary_observer_aware_date_or_time.setter  # set PEO.24
    def primary_observer_aware_date_or_time(self, ts: TS | None):
        """
        id: PEO.24 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.24
        """
        self._c_data[23] = (ts,)

    @property  # get PEO.25
    def primary_observers_identity_may_be_divulged(
        self,
    ) -> IdentityMayBeDivulged | None:
        """
        id: PEO.25 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.25
        """
        return self._c_data[24][0]

    @primary_observers_identity_may_be_divulged.setter  # set PEO.25
    def primary_observers_identity_may_be_divulged(
        self, identity_may_be_divulged: IdentityMayBeDivulged | None
    ):
        """
        id: PEO.25 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PEO.25
        """
        self._c_data[24] = (identity_may_be_divulged,)
