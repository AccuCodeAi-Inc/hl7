from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.IN2 import IN2
from ..segments.IN3 import IN3
from ..segments.IN1 import IN1


"""
INSURANCE - RPA_I10_INSURANCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RPA_I10_INSURANCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RPA_I10_INSURANCE_GROUP
from utils.hl7.v2_5_1.segments import (
    IN2, IN3, IN1
)

rpa_i10_insurance_group = RPA_I10_INSURANCE_GROUP(  # INSURANCE - Segment group for RPA_I10 - Request for resubmission of an authorization acknowledgement consisting of IN1, IN2|None, IN3|None
    insurance=in1,  # IN1(...)  # Required.
    insurance_additional_information=None,  # IN2(...) 
    insurance_additional_information_certification=None,  # IN3(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RPA_I10_INSURANCE_GROUP TEMPLATE-----
"""


class RPA_I10_INSURANCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RPA_I10_INSURANCE_GROUP"""
    _hl7_name = """INSURANCE"""
    _hl7_description = """Segment group for RPA_I10 - Request for resubmission of an authorization acknowledgement consisting of IN1, IN2|None, IN3|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPA_I10_INSURANCE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 1)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("12", "13", "14")
    _c_components = (IN1, IN2, IN3)
    _c_name = ("IN1", "IN2", "IN3")
    _c_is_group = (False, False, False)
    _c_attrs = ("insurance", "insurance_additional_information", "insurance_additional_information_certification",)
    # fmt: on

    def __init__(
        self,
        insurance: IN1,  #  Required. IN1.12
        insurance_additional_information: IN2 | None = None,  #  IN2.13
        insurance_additional_information_certification: IN3 | None = None,  #  IN3.14
    ):
        """
        None - `RPA_I10_INSURANCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPA_I10_INSURANCE_GROUP>`_
        Segment group for RPA_I10 - Request for resubmission of an authorization acknowledgement consisting of IN1, IN2|None, IN3|None

        :param insurance: Insurance (id: IN1 | seq: 12 | use: R | rpt: 1)
        :param insurance_additional_information: Insurance Additional Information (id: IN2 | seq: 13 | use: O | rpt: 1)
        :param insurance_additional_information_certification: Insurance Additional Information, Certification (id: IN3 | seq: 14 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.insurance = insurance
        self.insurance_additional_information = insurance_additional_information
        self.insurance_additional_information_certification = (
            insurance_additional_information_certification
        )

    @property  # get IN1.12
    def insurance(self) -> IN1:
        """
        id: IN1 | use: R | rpt: 1 | seq: 12
        ---
        return_type: IN1.12: Insurance
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN1
        """
        return self._c_data[0][0]

    @insurance.setter  # set IN1.12
    def insurance(self, in1: IN1):
        """
        id: IN1 | use: R | rpt: 1 | seq: 12
        ---
        param_type: IN1.12: Insurance
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN1
        """
        self._c_data[0] = (in1,)

    @property  # get IN2.13
    def insurance_additional_information(self) -> IN2 | None:
        """
        id: IN2 | use: O | rpt: 1 | seq: 13
        ---
        return_type: IN2.13: Insurance Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN2
        """
        return self._c_data[1][0]

    @insurance_additional_information.setter  # set IN2.13
    def insurance_additional_information(self, in2: IN2 | None):
        """
        id: IN2 | use: O | rpt: 1 | seq: 13
        ---
        param_type: IN2.13: Insurance Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN2
        """
        self._c_data[1] = (in2,)

    @property  # get IN3.14
    def insurance_additional_information_certification(self) -> IN3 | None:
        """
        id: IN3 | use: O | rpt: 1 | seq: 14
        ---
        return_type: IN3.14: Insurance Additional Information, Certification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN3
        """
        return self._c_data[2][0]

    @insurance_additional_information_certification.setter  # set IN3.14
    def insurance_additional_information_certification(self, in3: IN3 | None):
        """
        id: IN3 | use: O | rpt: 1 | seq: 14
        ---
        param_type: IN3.14: Insurance Additional Information, Certification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN3
        """
        self._c_data[2] = (in3,)
