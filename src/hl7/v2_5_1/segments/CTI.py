from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.EI import EI


"""
Clinical Trial Identification - CTI
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CTI TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CTI,
    CE, EI
)

cti = CTI(  #  - The CTI segment is an optional segment that contains information to identify the clinical trial, phase and time point with which an order or result is associated
    sponsor_study_id=ei,  # EI(...)  # Required.
    study_phase_identifier=None,  # CE(...) 
    study_scheduled_time_point=None,  # CE(...) 
)

-----END SEGMENT::CTI TEMPLATE-----
"""


class CTI(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CTI"""
    _hl7_name = """Clinical Trial Identification"""
    _hl7_description = """The CTI segment is an optional segment that contains information to identify the clinical trial, phase and time point with which an order or result is associated"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI"
    _c_length = (60, 250, 250,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("R", "C", "O",)
    _c_components = (EI, CE, CE,)
    _c_aliases = ("CTI.1", "CTI.2", "CTI.3",)
    _c_names = ("Sponsor Study ID", "Study Phase Identifier", "Study Scheduled Time Point",)
    _c_attrs = ("sponsor_study_id", "study_phase_identifier", "study_scheduled_time_point",)
    # fmt: on

    def __init__(
        self,
        sponsor_study_id: EI | tuple[EI, ...],  # CTI.1
        study_phase_identifier: CE | tuple[CE, ...] | None = None,  # CTI.2
        study_scheduled_time_point: CE | tuple[CE, ...] | None = None,  # CTI.3
    ):
        """
        Clinical Trial Identification - `CTI <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI>`_
        The CTI segment is an optional segment that contains information to identify the clinical trial, phase and time point with which an order or result is associated.

        :param sponsor_study_id: Entity Identifier (id: CTI.1 | len: 60 | use: R | rpt: 1)
        :param study_phase_identifier: Coded Element (id: CTI.2 | len: 250 | use: C | rpt: 1)
        :param study_scheduled_time_point: Coded Element (id: CTI.3 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.sponsor_study_id = sponsor_study_id
        self.study_phase_identifier = study_phase_identifier
        self.study_scheduled_time_point = study_scheduled_time_point

    @property  # get CTI.1
    def sponsor_study_id(self) -> EI:
        """
        id: CTI.1 | len: 60 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTI.1
        """
        return self._c_data[0][0]

    @sponsor_study_id.setter  # set CTI.1
    def sponsor_study_id(self, ei: EI):
        """
        id: CTI.1 | len: 60 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTI.1
        """
        self._c_data[0] = (ei,)

    @property  # get CTI.2
    def study_phase_identifier(self) -> CE | None:
        """
        id: CTI.2 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTI.2
        """
        return self._c_data[1][0]

    @study_phase_identifier.setter  # set CTI.2
    def study_phase_identifier(self, ce: CE | None):
        """
        id: CTI.2 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTI.2
        """
        self._c_data[1] = (ce,)

    @property  # get CTI.3
    def study_scheduled_time_point(self) -> CE | None:
        """
        id: CTI.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTI.3
        """
        return self._c_data[2][0]

    @study_scheduled_time_point.setter  # set CTI.3
    def study_scheduled_time_point(self, ce: CE | None):
        """
        id: CTI.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTI.3
        """
        self._c_data[2] = (ce,)
