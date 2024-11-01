from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.CX import CX
from ..data_types.XCN import XCN
from ..data_types.CE import CE
from ..data_types.EI import EI


"""
Clinical Study Registration - CSR
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CSR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CSR,
    TS, CX, XCN, CE, EI
)

csr = CSR(  #  - The CSR segment will contain fundamental administrative and regulatory information required to document a patients enrollment on a clinical trial
    sponsor_study_id=ei,  # EI(...)  # Required.
    alternate_study_id=None,  # EI(...) 
    institution_registering_the_patient=None,  # CE(...) 
    sponsor_patient_id=cx,  # CX(...)  # Required.
    alternate_patient_id_csr=None,  # CX(...) 
    date_or_time_of_patient_study_registration=ts,  # TS(...)  # Required.
    person_performing_study_registration=None,  # XCN(...) 
    study_authorizing_provider=xcn,  # XCN(...)  # Required.
    date_or_time_patient_study_consent_signed=None,  # TS(...) 
    patient_study_eligibility_status=None,  # CE(...) 
    study_randomization_date_or_time=None,  # TS(...) 
    randomized_study_arm=None,  # CE(...) 
    stratum_for_study_randomization=None,  # CE(...) 
    patient_evaluability_status=None,  # CE(...) 
    date_or_time_ended_study=None,  # TS(...) 
    reason_ended_study=None,  # CE(...) 
)

-----END SEGMENT::CSR TEMPLATE-----
"""


class CSR(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CSR"""
    _hl7_name = """Clinical Study Registration"""
    _hl7_description = """The CSR segment will contain fundamental administrative and regulatory information required to document a patients enrollment on a clinical trial"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSR"
    _c_length = (60, 60, 250, 30, 30, 26, 250, 250, 26, 250, 26, 250, 250, 250, 26, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 65535, 65535, 1, 1, 3, 3, 3, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "R", "O", "R", "O", "R", "C", "C", "O", "O", "O", "C", "C", "C",)
    _c_components = (EI, EI, CE, CX, CX, TS, XCN, XCN, TS, CE, TS, CE, CE, CE, TS, CE,)
    _c_aliases = ("CSR.1", "CSR.2", "CSR.3", "CSR.4", "CSR.5", "CSR.6", "CSR.7", "CSR.8", "CSR.9", "CSR.10", "CSR.11", "CSR.12", "CSR.13", "CSR.14", "CSR.15", "CSR.16",)
    _c_names = ("Sponsor Study ID", "Alternate Study ID", "Institution Registering the Patient", "Sponsor Patient ID", "Alternate Patient ID - CSR", "Date/Time Of Patient Study Registration", "Person Performing Study Registration", "Study Authorizing Provider", "Date/time Patient Study Consent Signed", "Patient Study Eligibility Status", "Study Randomization Date/time", "Randomized Study Arm", "Stratum for Study Randomization", "Patient Evaluability Status", "Date/time Ended Study", "Reason Ended Study",)
    _c_attrs = ("sponsor_study_id", "alternate_study_id", "institution_registering_the_patient", "sponsor_patient_id", "alternate_patient_id_csr", "date_or_time_of_patient_study_registration", "person_performing_study_registration", "study_authorizing_provider", "date_or_time_patient_study_consent_signed", "patient_study_eligibility_status", "study_randomization_date_or_time", "randomized_study_arm", "stratum_for_study_randomization", "patient_evaluability_status", "date_or_time_ended_study", "reason_ended_study",)
    # fmt: on

    def __init__(
        self,
        sponsor_study_id: EI | tuple[EI],  # CSR.1
        sponsor_patient_id: CX | tuple[CX],  # CSR.4
        date_or_time_of_patient_study_registration: TS | tuple[TS],  # CSR.6
        study_authorizing_provider: XCN | tuple[XCN],  # CSR.8
        alternate_study_id: EI | tuple[EI] | None = None,  # CSR.2
        institution_registering_the_patient: CE | tuple[CE] | None = None,  # CSR.3
        alternate_patient_id_csr: CX | tuple[CX] | None = None,  # CSR.5
        person_performing_study_registration: XCN | tuple[XCN] | None = None,  # CSR.7
        date_or_time_patient_study_consent_signed: TS
        | tuple[TS]
        | None = None,  # CSR.9
        patient_study_eligibility_status: CE | tuple[CE] | None = None,  # CSR.10
        study_randomization_date_or_time: TS | tuple[TS] | None = None,  # CSR.11
        randomized_study_arm: CE | tuple[CE] | None = None,  # CSR.12
        stratum_for_study_randomization: CE | tuple[CE] | None = None,  # CSR.13
        patient_evaluability_status: CE | tuple[CE] | None = None,  # CSR.14
        date_or_time_ended_study: TS | tuple[TS] | None = None,  # CSR.15
        reason_ended_study: CE | tuple[CE] | None = None,  # CSR.16
    ):
        """
        Clinical Study Registration - `CSR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSR>`_
        The CSR segment will contain fundamental administrative and regulatory information required to document a patients enrollment on a clinical trial. This segment is all that is required if one needs to message another system that an enrollment has taken place, i.e., from clinical trials to pharmacy, accounting, or order entry systems. The CSR segment may also be used to identify that OBR, OBX, RXA, and RXR segments that follow represent data applicable to the identified study.

        :param sponsor_study_id: Entity Identifier (id: CSR.1 | len: 60 | use: R | rpt: 1)
        :param alternate_study_id: Entity Identifier (id: CSR.2 | len: 60 | use: O | rpt: 1)
        :param institution_registering_the_patient: Coded Element (id: CSR.3 | len: 250 | use: O | rpt: 1)
        :param sponsor_patient_id: Extended Composite ID with Check Digit (id: CSR.4 | len: 30 | use: R | rpt: 1)
        :param alternate_patient_id_csr: Extended Composite ID with Check Digit (id: CSR.5 | len: 30 | use: O | rpt: 1)
        :param date_or_time_of_patient_study_registration: Time Stamp (id: CSR.6 | len: 26 | use: R | rpt: 1)
        :param person_performing_study_registration: Extended Composite ID Number and Name for Persons (id: CSR.7 | len: 250 | use: O | rpt: *)
        :param study_authorizing_provider: Extended Composite ID Number and Name for Persons (id: CSR.8 | len: 250 | use: R | rpt: *)
        :param date_or_time_patient_study_consent_signed: Time Stamp (id: CSR.9 | len: 26 | use: C | rpt: 1)
        :param patient_study_eligibility_status: Coded Element (id: CSR.10 | len: 250 | use: C | rpt: 1)
        :param study_randomization_date_or_time: Time Stamp (id: CSR.11 | len: 26 | use: O | rpt: 3)
        :param randomized_study_arm: Coded Element (id: CSR.12 | len: 250 | use: O | rpt: 3)
        :param stratum_for_study_randomization: Coded Element (id: CSR.13 | len: 250 | use: O | rpt: 3)
        :param patient_evaluability_status: Coded Element (id: CSR.14 | len: 250 | use: C | rpt: 1)
        :param date_or_time_ended_study: Time Stamp (id: CSR.15 | len: 26 | use: C | rpt: 1)
        :param reason_ended_study: Coded Element (id: CSR.16 | len: 250 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 16
        self.sponsor_study_id = sponsor_study_id
        self.alternate_study_id = alternate_study_id
        self.institution_registering_the_patient = institution_registering_the_patient
        self.sponsor_patient_id = sponsor_patient_id
        self.alternate_patient_id_csr = alternate_patient_id_csr
        self.date_or_time_of_patient_study_registration = (
            date_or_time_of_patient_study_registration
        )
        self.person_performing_study_registration = person_performing_study_registration
        self.study_authorizing_provider = study_authorizing_provider
        self.date_or_time_patient_study_consent_signed = (
            date_or_time_patient_study_consent_signed
        )
        self.patient_study_eligibility_status = patient_study_eligibility_status
        self.study_randomization_date_or_time = study_randomization_date_or_time
        self.randomized_study_arm = randomized_study_arm
        self.stratum_for_study_randomization = stratum_for_study_randomization
        self.patient_evaluability_status = patient_evaluability_status
        self.date_or_time_ended_study = date_or_time_ended_study
        self.reason_ended_study = reason_ended_study

    @property  # get CSR.1
    def sponsor_study_id(self) -> EI:
        """
        id: CSR.1 | len: 60 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.1
        """
        return self._c_data[0][0]

    @sponsor_study_id.setter  # set CSR.1
    def sponsor_study_id(self, ei: EI):
        """
        id: CSR.1 | len: 60 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.1
        """
        self._c_data[0] = (ei,)

    @property  # get CSR.2
    def alternate_study_id(self) -> EI | None:
        """
        id: CSR.2 | len: 60 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.2
        """
        return self._c_data[1][0]

    @alternate_study_id.setter  # set CSR.2
    def alternate_study_id(self, ei: EI | None):
        """
        id: CSR.2 | len: 60 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.2
        """
        self._c_data[1] = (ei,)

    @property  # get CSR.3
    def institution_registering_the_patient(self) -> CE | None:
        """
        id: CSR.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.3
        """
        return self._c_data[2][0]

    @institution_registering_the_patient.setter  # set CSR.3
    def institution_registering_the_patient(self, ce: CE | None):
        """
        id: CSR.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.3
        """
        self._c_data[2] = (ce,)

    @property  # get CSR.4
    def sponsor_patient_id(self) -> CX:
        """
        id: CSR.4 | len: 30 | use: R | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.4
        """
        return self._c_data[3][0]

    @sponsor_patient_id.setter  # set CSR.4
    def sponsor_patient_id(self, cx: CX):
        """
        id: CSR.4 | len: 30 | use: R | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.4
        """
        self._c_data[3] = (cx,)

    @property  # get CSR.5
    def alternate_patient_id_csr(self) -> CX | None:
        """
        id: CSR.5 | len: 30 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.5
        """
        return self._c_data[4][0]

    @alternate_patient_id_csr.setter  # set CSR.5
    def alternate_patient_id_csr(self, cx: CX | None):
        """
        id: CSR.5 | len: 30 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.5
        """
        self._c_data[4] = (cx,)

    @property  # get CSR.6
    def date_or_time_of_patient_study_registration(self) -> TS:
        """
        id: CSR.6 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.6
        """
        return self._c_data[5][0]

    @date_or_time_of_patient_study_registration.setter  # set CSR.6
    def date_or_time_of_patient_study_registration(self, ts: TS):
        """
        id: CSR.6 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.6
        """
        self._c_data[5] = (ts,)

    @property
    def person_performing_study_registration(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: CSR.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.7
        """
        return self._c_data[6]

    @person_performing_study_registration.setter  # set CSR.7
    def person_performing_study_registration(self, xcn: XCN | tuple[XCN] | None):
        """
        id: CSR.7 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.7
        """
        if isinstance(xcn, tuple):
            self._c_data[6] = xcn
        else:
            self._c_data[6] = (xcn,)

    @property
    def study_authorizing_provider(self) -> tuple[XCN, ...]:
        """
        id: CSR.8 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.8
        """
        return self._c_data[7]

    @study_authorizing_provider.setter  # set CSR.8
    def study_authorizing_provider(self, xcn: XCN | tuple[XCN]):
        """
        id: CSR.8 | len: 250 | use: R | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.8
        """
        if isinstance(xcn, tuple):
            self._c_data[7] = xcn
        else:
            self._c_data[7] = (xcn,)

    @property  # get CSR.9
    def date_or_time_patient_study_consent_signed(self) -> TS | None:
        """
        id: CSR.9 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.9
        """
        return self._c_data[8][0]

    @date_or_time_patient_study_consent_signed.setter  # set CSR.9
    def date_or_time_patient_study_consent_signed(self, ts: TS | None):
        """
        id: CSR.9 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.9
        """
        self._c_data[8] = (ts,)

    @property  # get CSR.10
    def patient_study_eligibility_status(self) -> CE | None:
        """
        id: CSR.10 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.10
        """
        return self._c_data[9][0]

    @patient_study_eligibility_status.setter  # set CSR.10
    def patient_study_eligibility_status(self, ce: CE | None):
        """
        id: CSR.10 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.10
        """
        self._c_data[9] = (ce,)

    @property
    def study_randomization_date_or_time(self) -> tuple[TS, ...] | tuple[None]:
        """
        id: CSR.11 | len: 26 | use: O | rpt: 3
        ---
        return_type: tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.11
        """
        return self._c_data[10]

    @study_randomization_date_or_time.setter  # set CSR.11
    def study_randomization_date_or_time(self, ts: TS | tuple[TS] | None):
        """
        id: CSR.11 | len: 26 | use: O | rpt: 3
        ---
        param_type: TS | tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.11
        """
        if isinstance(ts, tuple):
            self._c_data[10] = ts
        else:
            self._c_data[10] = (ts,)

    @property
    def randomized_study_arm(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: CSR.12 | len: 250 | use: O | rpt: 3
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.12
        """
        return self._c_data[11]

    @randomized_study_arm.setter  # set CSR.12
    def randomized_study_arm(self, ce: CE | tuple[CE] | None):
        """
        id: CSR.12 | len: 250 | use: O | rpt: 3
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.12
        """
        if isinstance(ce, tuple):
            self._c_data[11] = ce
        else:
            self._c_data[11] = (ce,)

    @property
    def stratum_for_study_randomization(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: CSR.13 | len: 250 | use: O | rpt: 3
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.13
        """
        return self._c_data[12]

    @stratum_for_study_randomization.setter  # set CSR.13
    def stratum_for_study_randomization(self, ce: CE | tuple[CE] | None):
        """
        id: CSR.13 | len: 250 | use: O | rpt: 3
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.13
        """
        if isinstance(ce, tuple):
            self._c_data[12] = ce
        else:
            self._c_data[12] = (ce,)

    @property  # get CSR.14
    def patient_evaluability_status(self) -> CE | None:
        """
        id: CSR.14 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.14
        """
        return self._c_data[13][0]

    @patient_evaluability_status.setter  # set CSR.14
    def patient_evaluability_status(self, ce: CE | None):
        """
        id: CSR.14 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.14
        """
        self._c_data[13] = (ce,)

    @property  # get CSR.15
    def date_or_time_ended_study(self) -> TS | None:
        """
        id: CSR.15 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.15
        """
        return self._c_data[14][0]

    @date_or_time_ended_study.setter  # set CSR.15
    def date_or_time_ended_study(self, ts: TS | None):
        """
        id: CSR.15 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.15
        """
        self._c_data[14] = (ts,)

    @property  # get CSR.16
    def reason_ended_study(self) -> CE | None:
        """
        id: CSR.16 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.16
        """
        return self._c_data[15][0]

    @reason_ended_study.setter  # set CSR.16
    def reason_ended_study(self, ce: CE | None):
        """
        id: CSR.16 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSR.16
        """
        self._c_data[15] = (ce,)
