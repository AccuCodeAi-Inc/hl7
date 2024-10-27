from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.GT1 import GT1
from ..segment_groups.PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP import (
    PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP,
)


"""
GUARANTOR INSURANCE - PIN_I07_GUARANTOR_INSURANCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PIN_I07_GUARANTOR_INSURANCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PIN_I07_GUARANTOR_INSURANCE_GROUP
from utils.hl7.v2_5_1.segments import (
    GT1
)
from utils.hl7.v2_5_1.segment_groups import (
    PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP
)

pin_i07_guarantor_insurance_group = PIN_I07_GUARANTOR_INSURANCE_GROUP(  # GUARANTOR INSURANCE - Segment group for PIN_I07 - Unsolicited insurance information consisting of GT1|None, INSURANCE
    guarantor=None,  # GT1(...) 
    insurance=pin_i07_guarantor_insurance_group_insurance_group,  # PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PIN_I07_GUARANTOR_INSURANCE_GROUP TEMPLATE-----
"""


class PIN_I07_GUARANTOR_INSURANCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PIN_I07_GUARANTOR_INSURANCE_GROUP"""
    _hl7_name = """GUARANTOR INSURANCE"""
    _hl7_description = """Segment group for PIN_I07 - Unsolicited insurance information consisting of GT1|None, INSURANCE"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PIN_I07_GUARANTOR_INSURANCE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (65535, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("7", "None")
    _c_components = (GT1, PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP)
    _c_name = ("GT1", "INSURANCE")
    _c_is_group = (False, True)
    _c_attrs = ("guarantor", "insurance",)
    # fmt: on

    def __init__(
        self,
        insurance: PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP
        | tuple[
            PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP, ...
        ],  #  Required. (IN1.8, IN2.9, IN3.10, ...)
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.7
    ):
        """
        None - `PIN_I07_GUARANTOR_INSURANCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PIN_I07_GUARANTOR_INSURANCE_GROUP>`_
        Segment group for PIN_I07 - Unsolicited insurance information consisting of GT1|None, INSURANCE

        :param guarantor: Guarantor (id: GT1 | seq: 7 | use: O | rpt: *)
        :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None] (id: INSURANCE | seq: 8, 9, 10 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.guarantor = guarantor
        self.insurance = insurance

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[0]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: GT1.7 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[0] = gt1
        else:
            self._c_data[0] = (gt1,)

    @property  # get INSURANCE
    def insurance(
        self,
    ) -> tuple[PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP, ...]:
        """
        id: PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP
        """
        return self._c_data[1]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP
        | tuple[PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP, ...],
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP.None | tuple[PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PIN_I07_GUARANTOR_INSURANCE_GROUP_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[1] = insurance
        else:
            self._c_data[1] = (insurance,)
