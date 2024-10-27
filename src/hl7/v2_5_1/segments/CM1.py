from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.ST import ST
from ..data_types.CE import CE


"""
Clinical Study Phase Master - CM1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CM1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CM1,
    SI, ST, CE
)

cm1 = CM1(  #  - Each Clinical Study Phase Master (CM1) segment contains the information about one phase of a study identified in the preceding CM0
    set_id_cm1=si,  # SI(...)  # Required.
    study_phase_identifier=ce,  # CE(...)  # Required.
    description_of_study_phase=st,  # ST(...)  # Required.
)

-----END SEGMENT::CM1 TEMPLATE-----
"""


class CM1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CM1"""
    _hl7_name = """Clinical Study Phase Master"""
    _hl7_description = """Each Clinical Study Phase Master (CM1) segment contains the information about one phase of a study identified in the preceding CM0"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM1"
    _c_length = (4, 250, 300,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("R", "R", "R",)
    _c_components = (SI, CE, ST,)
    _c_aliases = ("CM1.1", "CM1.2", "CM1.3",)
    _c_names = ("Set ID - CM1", "Study Phase Identifier", "Description of Study Phase",)
    _c_attrs = ("set_id_cm1", "study_phase_identifier", "description_of_study_phase",)
    # fmt: on

    def __init__(
        self,
        set_id_cm1: SI,  # CM1.1
        study_phase_identifier: CE,  # CM1.2
        description_of_study_phase: ST,  # CM1.3
    ):
        """
        Clinical Study Phase Master - `CM1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM1>`_
        Each Clinical Study Phase Master (CM1) segment contains the information about one phase of a study identified in the preceding CM0.  This is an optional structure to be used if the study has more than one treatment or evaluation phase within it.  The identification of study phases that the patient enters are sent in the CSP segment: sequence 2.  The CM1 segment describes the phase in general for the receiving system.

        :param set_id_cm1: Sequence ID (id: CM1.1 | len: 4 | use: R | rpt: 1)
        :param study_phase_identifier: Coded Element (id: CM1.2 | len: 250 | use: R | rpt: 1)
        :param description_of_study_phase: String Data (id: CM1.3 | len: 300 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.set_id_cm1 = set_id_cm1
        self.study_phase_identifier = study_phase_identifier
        self.description_of_study_phase = description_of_study_phase

    @property  # get CM1.1
    def set_id_cm1(self) -> SI:
        """
        id: CM1.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM1.1
        """
        return self._c_data[0][0]

    @set_id_cm1.setter  # set CM1.1
    def set_id_cm1(self, si: SI):
        """
        id: CM1.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM1.1
        """
        self._c_data[0] = (si,)

    @property  # get CM1.2
    def study_phase_identifier(self) -> CE:
        """
        id: CM1.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM1.2
        """
        return self._c_data[1][0]

    @study_phase_identifier.setter  # set CM1.2
    def study_phase_identifier(self, ce: CE):
        """
        id: CM1.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM1.2
        """
        self._c_data[1] = (ce,)

    @property  # get CM1.3
    def description_of_study_phase(self) -> ST:
        """
        id: CM1.3 | len: 300 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM1.3
        """
        return self._c_data[2][0]

    @description_of_study_phase.setter  # set CM1.3
    def description_of_study_phase(self, st: ST):
        """
        id: CM1.3 | len: 300 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM1.3
        """
        self._c_data[2] = (st,)
