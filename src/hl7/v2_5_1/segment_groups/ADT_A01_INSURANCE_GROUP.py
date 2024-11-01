from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ROL import ROL
from ..segments.IN1 import IN1
from ..segments.IN3 import IN3
from ..segments.IN2 import IN2


"""
INSURANCE - ADT_A01_INSURANCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ADT_A01_INSURANCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A01_INSURANCE_GROUP
from utils.hl7.v2_5_1.segments import (
    IN1, ROL, IN2, IN3
)

adt_a01_insurance_group = ADT_A01_INSURANCE_GROUP(  # INSURANCE - Segment group for ADT_A01 - Admit/Visit Notification consisting of IN1, IN2|None, IN3|None, ROL|None
    insurance=in1,  # IN1(...)  # Required.
    insurance_additional_information=None,  # IN2(...) 
    insurance_additional_information_certification=None,  # IN3(...) 
    role=None,  # ROL(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ADT_A01_INSURANCE_GROUP TEMPLATE-----
"""


class ADT_A01_INSURANCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ADT_A01_INSURANCE_GROUP"""
    _hl7_name = """INSURANCE"""
    _hl7_description = """Segment group for ADT_A01 - Admit/Visit Notification consisting of IN1, IN2|None, IN3|None, ROL|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A01_INSURANCE_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("19", "20", "21", "22")
    _c_components = (IN1, IN2, IN3, ROL)
    _c_name = ("IN1", "IN2", "IN3", "ROL")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("insurance", "insurance_additional_information", "insurance_additional_information_certification", "role",)
    # fmt: on

    def __init__(
        self,
        insurance: IN1,  #  Required. IN1.19
        insurance_additional_information: IN2 | None = None,  #  IN2.20
        insurance_additional_information_certification: IN3
        | tuple[IN3, ...]
        | None = None,  #  IN3.21
        role: ROL | tuple[ROL, ...] | None = None,  #  ROL.22
    ):
        """
        None - `ADT_A01_INSURANCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A01_INSURANCE_GROUP>`_
        Segment group for ADT_A01 - Admit/Visit Notification consisting of IN1, IN2|None, IN3|None, ROL|None

        :param insurance: Insurance (id: IN1 | seq: 19 | use: R | rpt: 1)
        :param insurance_additional_information: Insurance Additional Information (id: IN2 | seq: 20 | use: O | rpt: 1)
        :param insurance_additional_information_certification: Insurance Additional Information, Certification (id: IN3 | seq: 21 | use: O | rpt: *)
        :param role: Role (id: ROL | seq: 22 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.insurance = insurance
        self.insurance_additional_information = insurance_additional_information
        self.insurance_additional_information_certification = (
            insurance_additional_information_certification
        )
        self.role = role

    @property  # get IN1.19
    def insurance(self) -> IN1:
        """
        id: IN1 | use: R | rpt: 1 | seq: 19
        ---
        return_type: IN1.19: Insurance
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN1
        """
        return self._c_data[0][0]

    @insurance.setter  # set IN1.19
    def insurance(self, in1: IN1):
        """
        id: IN1 | use: R | rpt: 1 | seq: 19
        ---
        param_type: IN1.19: Insurance
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN1
        """
        self._c_data[0] = (in1,)

    @property  # get IN2.20
    def insurance_additional_information(self) -> IN2 | None:
        """
        id: IN2 | use: O | rpt: 1 | seq: 20
        ---
        return_type: IN2.20: Insurance Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN2
        """
        return self._c_data[1][0]

    @insurance_additional_information.setter  # set IN2.20
    def insurance_additional_information(self, in2: IN2 | None):
        """
        id: IN2 | use: O | rpt: 1 | seq: 20
        ---
        param_type: IN2.20: Insurance Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN2
        """
        self._c_data[1] = (in2,)

    @property  # get IN3
    def insurance_additional_information_certification(
        self,
    ) -> tuple[IN3, ...] | tuple[None]:
        """
        id: IN3 SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        return_type: tuple[IN3, ...]: (Insurance Additional Information, Certification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN3
        """
        return self._c_data[2]

    @insurance_additional_information_certification.setter  # set IN3
    def insurance_additional_information_certification(
        self, in3: IN3 | tuple[IN3, ...] | None
    ):
        """
        id: IN3 SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        param_type: IN3.21 | tuple[IN3, ...]: (Insurance Additional Information, Certification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN3
        """
        if isinstance(in3, tuple):
            self._c_data[2] = in3
        else:
            self._c_data[2] = (in3,)

    @property  # get ROL
    def role(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[3]

    @role.setter  # set ROL
    def role(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        param_type: ROL.22 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[3] = rol
        else:
            self._c_data[3] = (rol,)
