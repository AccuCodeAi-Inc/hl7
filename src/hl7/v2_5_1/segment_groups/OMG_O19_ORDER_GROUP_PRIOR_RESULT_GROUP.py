from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP import (
    OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP,
)
from ..segment_groups.OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP import (
    OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP,
)
from ..segments.AL1 import AL1
from ..segment_groups.OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP import (
    OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP,
)


"""
PRIOR RESULT - OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP
from utils.hl7.v2_5_1.segments import (
    AL1
)
from utils.hl7.v2_5_1.segment_groups import (
    OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP, OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP, OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
)

omg_o19_order_group_prior_result_group = OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP(  # PRIOR RESULT - Segment group for OMG_O19_ORDER_GROUP - ORDER consisting of PATIENT PRIOR|None, PATIENT VISIT PRIOR|None, AL1|None, ORDER PRIOR
    patient_prior=None,  # OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP(...) 
    patient_visit_prior=None,  # OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP(...) 
    patient_allergy_information=None,  # AL1(...) 
    order_prior=omg_o19_order_group_prior_result_group_order_prior_group,  # OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP TEMPLATE-----
"""


class OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP"""
    _hl7_name = """PRIOR RESULT"""
    _hl7_description = """Segment group for OMG_O19_ORDER_GROUP - ORDER consisting of PATIENT PRIOR|None, PATIENT VISIT PRIOR|None, AL1|None, ORDER PRIOR"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535)
    _c_usage = ("O", "O", "O", "R")
    _c_aliases = ("None", "None", "32", "None")
    _c_components = (OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP, OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP, AL1, OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP)
    _c_name = ("PATIENT PRIOR", "PATIENT VISIT PRIOR", "AL1", "ORDER PRIOR")
    _c_is_group = (True, True, False, True)
    _c_attrs = ("patient_prior", "patient_visit_prior", "patient_allergy_information", "order_prior",)
    # fmt: on

    def __init__(
        self,
        order_prior: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
        | tuple[
            OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP, ...
        ],  #  Required. (ORC.33, OBR.34, NTE.37, CTD.38, ...)
        patient_prior: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
        | None = None,  #  PID.28, PD1.29
        patient_visit_prior: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP
        | None = None,  #  PV1.30, PV2.31
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.32
    ):
        """
        None - `OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP>`_
        Segment group for OMG_O19_ORDER_GROUP - ORDER consisting of PATIENT PRIOR|None, PATIENT VISIT PRIOR|None, AL1|None, ORDER PRIOR

        :param patient_prior: Patient Prior segment group: [PID, PD1|None] (id: PATIENT PRIOR | seq: 28, 29 | use: O | rpt: 1)
        :param patient_visit_prior: Patient Visit Prior segment group: [PV1, PV2|None] (id: PATIENT VISIT PRIOR | seq: 30, 31 | use: O | rpt: 1)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 32 | use: O | rpt: *)
        :param order_prior: Order Prior segment group: [ORC|None, OBR, TIMING PRIOR|None, NTE|None, CTD|None, OBSERVATION PRIOR] (id: ORDER PRIOR | seq: 33, 34, None, 37, 38, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.patient_prior = patient_prior
        self.patient_visit_prior = patient_visit_prior
        self.patient_allergy_information = patient_allergy_information
        self.order_prior = order_prior

    @property  # get OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP.None
    def patient_prior(
        self,
    ) -> OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP | None:
        """
        id: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
        """
        return self._c_data[0][0]

    @patient_prior.setter  # set OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP.None
    def patient_prior(
        self,
        patient_prior: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
        | None,
    ):
        """
        id: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
        """
        self._c_data[0] = (patient_prior,)

    @property  # get OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP.None
    def patient_visit_prior(
        self,
    ) -> OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP | None:
        """
        id: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP
        """
        return self._c_data[1][0]

    @patient_visit_prior.setter  # set OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP.None
    def patient_visit_prior(
        self,
        patient_v_isit_prior: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP
        | None,
    ):
        """
        id: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP
        """
        self._c_data[1] = (patient_v_isit_prior,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 32
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[2]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 32
        ---
        param_type: AL1.32 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[2] = al1
        else:
            self._c_data[2] = (al1,)

    @property  # get ORDER PRIOR
    def order_prior(
        self,
    ) -> tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP, ...]:
        """
        id: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
        """
        return self._c_data[3]

    @order_prior.setter  # set ORDER PRIOR
    def order_prior(
        self,
        order_prior: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
        | tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP, ...],
    ):
        """
        id: ORDER PRIOR SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP.None | tuple[OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
        """
        if isinstance(order_prior, tuple):
            self._c_data[3] = order_prior
        else:
            self._c_data[3] = (order_prior,)
