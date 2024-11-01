from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.IN2 import IN2
from ..segments.IN3 import IN3
from ..segments.IN1 import IN1


"""
INSURANCE - REF_I14_INSURANCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::REF_I14_INSURANCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import REF_I14_INSURANCE_GROUP
from utils.hl7.v2_5_1.segments import (
    IN3, IN2, IN1
)

ref_i14_insurance_group = REF_I14_INSURANCE_GROUP(  # INSURANCE - Segment group for REF_I14 - Cancel patient referral consisting of IN1, IN2|None, IN3|None
    insurance=in1,  # IN1(...)  # Required.
    insurance_additional_information=None,  # IN2(...) 
    insurance_additional_information_certification=None,  # IN3(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::REF_I14_INSURANCE_GROUP TEMPLATE-----
"""


class REF_I14_INSURANCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """REF_I14_INSURANCE_GROUP"""
    _hl7_name = """INSURANCE"""
    _hl7_description = """Segment group for REF_I14 - Cancel patient referral consisting of IN1, IN2|None, IN3|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/REF_I14_INSURANCE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 1)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("11", "12", "13")
    _c_components = (IN1, IN2, IN3)
    _c_name = ("IN1", "IN2", "IN3")
    _c_is_group = (False, False, False)
    _c_attrs = ("insurance", "insurance_additional_information", "insurance_additional_information_certification",)
    # fmt: on

    def __init__(
        self,
        insurance: IN1,  #  Required. IN1.11
        insurance_additional_information: IN2 | None = None,  #  IN2.12
        insurance_additional_information_certification: IN3 | None = None,  #  IN3.13
    ):
        """
        None - `REF_I14_INSURANCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/REF_I14_INSURANCE_GROUP>`_
        Segment group for REF_I14 - Cancel patient referral consisting of IN1, IN2|None, IN3|None

        :param insurance: Insurance (id: IN1 | seq: 11 | use: R | rpt: 1)
        :param insurance_additional_information: Insurance Additional Information (id: IN2 | seq: 12 | use: O | rpt: 1)
        :param insurance_additional_information_certification: Insurance Additional Information, Certification (id: IN3 | seq: 13 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.insurance = insurance
        self.insurance_additional_information = insurance_additional_information
        self.insurance_additional_information_certification = (
            insurance_additional_information_certification
        )

    @property  # get IN1.11
    def insurance(self) -> IN1:
        """
        id: IN1 | use: R | rpt: 1 | seq: 11
        ---
        return_type: IN1.11: Insurance
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN1
        """
        return self._c_data[0][0]

    @insurance.setter  # set IN1.11
    def insurance(self, in1: IN1):
        """
        id: IN1 | use: R | rpt: 1 | seq: 11
        ---
        param_type: IN1.11: Insurance
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN1
        """
        self._c_data[0] = (in1,)

    @property  # get IN2.12
    def insurance_additional_information(self) -> IN2 | None:
        """
        id: IN2 | use: O | rpt: 1 | seq: 12
        ---
        return_type: IN2.12: Insurance Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN2
        """
        return self._c_data[1][0]

    @insurance_additional_information.setter  # set IN2.12
    def insurance_additional_information(self, in2: IN2 | None):
        """
        id: IN2 | use: O | rpt: 1 | seq: 12
        ---
        param_type: IN2.12: Insurance Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN2
        """
        self._c_data[1] = (in2,)

    @property  # get IN3.13
    def insurance_additional_information_certification(self) -> IN3 | None:
        """
        id: IN3 | use: O | rpt: 1 | seq: 13
        ---
        return_type: IN3.13: Insurance Additional Information, Certification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN3
        """
        return self._c_data[2][0]

    @insurance_additional_information_certification.setter  # set IN3.13
    def insurance_additional_information_certification(self, in3: IN3 | None):
        """
        id: IN3 | use: O | rpt: 1 | seq: 13
        ---
        param_type: IN3.13: Insurance Additional Information, Certification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN3
        """
        self._c_data[2] = (in3,)
