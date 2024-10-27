from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TS import TS


"""
Clinical Study Phase - CSP
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CSP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CSP,
    CE, TS
)

csp = CSP(  #  - The CSP segment contains information on a patients status for a particular phase of the study
    study_phase_identifier=ce,  # CE(...)  # Required.
    date_or_time_study_phase_began=ts,  # TS(...)  # Required.
    date_or_time_study_phase_ended=None,  # TS(...) 
    study_phase_evaluability=None,  # CE(...) 
)

-----END SEGMENT::CSP TEMPLATE-----
"""


class CSP(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CSP"""
    _hl7_name = """Clinical Study Phase"""
    _hl7_description = """The CSP segment contains information on a patients status for a particular phase of the study"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSP"
    _c_length = (250, 26, 26, 250,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("R", "R", "O", "C",)
    _c_components = (CE, TS, TS, CE,)
    _c_aliases = ("CSP.1", "CSP.2", "CSP.3", "CSP.4",)
    _c_names = ("Study Phase Identifier", "Date/time Study Phase Began", "Date/time Study Phase Ended", "Study Phase Evaluability",)
    _c_attrs = ("study_phase_identifier", "date_or_time_study_phase_began", "date_or_time_study_phase_ended", "study_phase_evaluability",)
    # fmt: on

    def __init__(
        self,
        study_phase_identifier: CE,  # CSP.1
        date_or_time_study_phase_began: TS,  # CSP.2
        date_or_time_study_phase_ended: TS | None = None,  # CSP.3
        study_phase_evaluability: CE | None = None,  # CSP.4
    ):
        """
        Clinical Study Phase - `CSP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSP>`_
        The CSP segment contains information on a patients status for a particular phase of the study. This segment is optional and is useful when a study has different evaluation intervals within it. (See Section 0, HL7 Attribute Table - CSR - Clinical Study RegistrationPhase of a Clinical Trial. The CSP segment is implemented on a study-specific basis for messaging purposes. The fact that the patient has entered a phase of the study that represents a certain treatment approach may need to be messaged to other systems, like pharmacy, nursing, or order entry. It is also important to sponsors and data management centers for tracking patient progress through the study and monitoring the data schedule defined for each phase. It may subsume OBR and OBX segments that follow it to indicate that these data describe the phase.

        :param study_phase_identifier: Coded Element (id: CSP.1 | len: 250 | use: R | rpt: 1)
        :param date_or_time_study_phase_began: Time Stamp (id: CSP.2 | len: 26 | use: R | rpt: 1)
        :param date_or_time_study_phase_ended: Time Stamp (id: CSP.3 | len: 26 | use: O | rpt: 1)
        :param study_phase_evaluability: Coded Element (id: CSP.4 | len: 250 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.study_phase_identifier = study_phase_identifier
        self.date_or_time_study_phase_began = date_or_time_study_phase_began
        self.date_or_time_study_phase_ended = date_or_time_study_phase_ended
        self.study_phase_evaluability = study_phase_evaluability

    @property  # get CSP.1
    def study_phase_identifier(self) -> CE:
        """
        id: CSP.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSP.1
        """
        return self._c_data[0][0]

    @study_phase_identifier.setter  # set CSP.1
    def study_phase_identifier(self, ce: CE):
        """
        id: CSP.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSP.1
        """
        self._c_data[0] = (ce,)

    @property  # get CSP.2
    def date_or_time_study_phase_began(self) -> TS:
        """
        id: CSP.2 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSP.2
        """
        return self._c_data[1][0]

    @date_or_time_study_phase_began.setter  # set CSP.2
    def date_or_time_study_phase_began(self, ts: TS):
        """
        id: CSP.2 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSP.2
        """
        self._c_data[1] = (ts,)

    @property  # get CSP.3
    def date_or_time_study_phase_ended(self) -> TS | None:
        """
        id: CSP.3 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSP.3
        """
        return self._c_data[2][0]

    @date_or_time_study_phase_ended.setter  # set CSP.3
    def date_or_time_study_phase_ended(self, ts: TS | None):
        """
        id: CSP.3 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSP.3
        """
        self._c_data[2] = (ts,)

    @property  # get CSP.4
    def study_phase_evaluability(self) -> CE | None:
        """
        id: CSP.4 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSP.4
        """
        return self._c_data[3][0]

    @study_phase_evaluability.setter  # set CSP.4
    def study_phase_evaluability(self, ce: CE | None):
        """
        id: CSP.4 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSP.4
        """
        self._c_data[3] = (ce,)
