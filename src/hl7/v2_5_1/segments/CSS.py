from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TS import TS


"""
Clinical Study Data Schedule Segment - CSS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CSS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CSS,
    CE, TS
)

css = CSS(  #  - The Clinical Study Data Schedule (CSS) segment is optional depending on whether messaging of study data needs to be linked to the scheduled data time points for the study
    study_scheduled_time_point=ce,  # CE(...)  # Required.
    study_scheduled_patient_time_point=None,  # TS(...) 
    study_quality_control_codes=None,  # CE(...) 
)

-----END SEGMENT::CSS TEMPLATE-----
"""


class CSS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CSS"""
    _hl7_name = """Clinical Study Data Schedule Segment"""
    _hl7_description = """The Clinical Study Data Schedule (CSS) segment is optional depending on whether messaging of study data needs to be linked to the scheduled data time points for the study"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSS"
    _c_length = (250, 26, 250,)
    _c_rpt = (1, 1, 3,)
    _c_usage = ("R", "O", "O",)
    _c_components = (CE, TS, CE,)
    _c_aliases = ("CSS.1", "CSS.2", "CSS.3",)
    _c_names = ("Study Scheduled Time Point", "Study Scheduled Patient Time Point", "Study Quality Control Codes",)
    _c_attrs = ("study_scheduled_time_point", "study_scheduled_patient_time_point", "study_quality_control_codes",)
    # fmt: on

    def __init__(
        self,
        study_scheduled_time_point: CE,  # CSS.1
        study_scheduled_patient_time_point: TS | None = None,  # CSS.2
        study_quality_control_codes: CE | None = None,  # CSS.3
    ):
        """
        Clinical Study Data Schedule Segment - `CSS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSS>`_
        The Clinical Study Data Schedule (CSS) segment is optional depending on whether messaging of study data needs to be linked to the scheduled data time points for the study. (See Section 7.6.1.3, data schedule.) The CSS segment enables communication of data schedules and adherence that ranges from the basic to the elaborate. Use of the segment must be planned for each implementation. Each CSS segment will subsume observation and drug administration segments that follow, indicating that they satisfy this scheduled time point.

        :param study_scheduled_time_point: Coded Element (id: CSS.1 | len: 250 | use: R | rpt: 1)
        :param study_scheduled_patient_time_point: Time Stamp (id: CSS.2 | len: 26 | use: O | rpt: 1)
        :param study_quality_control_codes: Coded Element (id: CSS.3 | len: 250 | use: O | rpt: 3)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.study_scheduled_time_point = study_scheduled_time_point
        self.study_scheduled_patient_time_point = study_scheduled_patient_time_point
        self.study_quality_control_codes = study_quality_control_codes

    @property  # get CSS.1
    def study_scheduled_time_point(self) -> CE:
        """
        id: CSS.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSS.1
        """
        return self._c_data[0][0]

    @study_scheduled_time_point.setter  # set CSS.1
    def study_scheduled_time_point(self, ce: CE):
        """
        id: CSS.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSS.1
        """
        self._c_data[0] = (ce,)

    @property  # get CSS.2
    def study_scheduled_patient_time_point(self) -> TS | None:
        """
        id: CSS.2 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSS.2
        """
        return self._c_data[1][0]

    @study_scheduled_patient_time_point.setter  # set CSS.2
    def study_scheduled_patient_time_point(self, ts: TS | None):
        """
        id: CSS.2 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSS.2
        """
        self._c_data[1] = (ts,)

    @property
    def study_quality_control_codes(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: CSS.3 | len: 250 | use: O | rpt: 3
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSS.3
        """
        return self._c_data[2]

    @study_quality_control_codes.setter  # set CSS.3
    def study_quality_control_codes(self, ce: CE | tuple[CE] | None):
        """
        id: CSS.3 | len: 250 | use: O | rpt: 3
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSS.3
        """
        if isinstance(ce, tuple):
            self._c_data[2] = ce
        else:
            self._c_data[2] = (ce,)
