from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.AL1 import AL1
from ..segment_groups.OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP import (
    OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP,
)
from ..segment_groups.OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP import (
    OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP,
)
from ..segment_groups.OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP import (
    OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP,
)


"""
PRIOR RESULT - OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP
from utils.hl7.v2_5_1.segments import (
    AL1
)
from utils.hl7.v2_5_1.segment_groups import (
    OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP, OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP, OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
)

oml_o21_order_group_observation_request_group_prior_result_group = OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP(  # PRIOR RESULT - Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP - OBSERVATION REQUEST consisting of PATIENT PRIOR|None, PATIENT VISIT PRIOR|None, AL1|None, ORDER PRIOR
    patient_prior=None,  # OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP(...) 
    patient_visit_prior=None,  # OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP(...) 
    patient_allergy_information=None,  # AL1(...) 
    order_prior=oml_o21_order_group_observation_request_group_prior_result_group_order_prior_group,  # OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP TEMPLATE-----
"""


class OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP"""
    _hl7_name = """PRIOR RESULT"""
    _hl7_description = """Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP - OBSERVATION REQUEST consisting of PATIENT PRIOR|None, PATIENT VISIT PRIOR|None, AL1|None, ORDER PRIOR"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535)
    _c_usage = ("O", "O", "O", "R")
    _c_aliases = ("None", "None", "34", "None")
    _c_components = (OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP, OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP, AL1, OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP)
    _c_name = ("PATIENT PRIOR", "PATIENT VISIT PRIOR", "AL1", "ORDER PRIOR")
    _c_is_group = (True, True, False, True)
    _c_attrs = ("patient_prior", "patient_visit_prior", "patient_allergy_information", "order_prior",)
    # fmt: on

    def __init__(
        self,
        order_prior: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
        | tuple[
            OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP,
            ...,
        ],  #  Required. (ORC.35, OBR.36, NTE.37, ...)
        patient_prior: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
        | None = None,  #  PID.30, PD1.31
        patient_visit_prior: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP
        | None = None,  #  PV1.32, PV2.33
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.34
    ):
        """
        None - `OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP>`_
        Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP - OBSERVATION REQUEST consisting of PATIENT PRIOR|None, PATIENT VISIT PRIOR|None, AL1|None, ORDER PRIOR

        :param patient_prior: Patient Prior segment group: [PID, PD1|None] (id: PATIENT PRIOR | seq: 30, 31 | use: O | rpt: 1)
        :param patient_visit_prior: Patient Visit Prior segment group: [PV1, PV2|None] (id: PATIENT VISIT PRIOR | seq: 32, 33 | use: O | rpt: 1)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 34 | use: O | rpt: *)
        :param order_prior: Order Prior segment group: [ORC|None, OBR, NTE|None, TIMING PRIOR|None, OBSERVATION PRIOR] (id: ORDER PRIOR | seq: 35, 36, 37, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.patient_prior = patient_prior
        self.patient_visit_prior = patient_visit_prior
        self.patient_allergy_information = patient_allergy_information
        self.order_prior = order_prior

    @property  # get OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP.None
    def patient_prior(
        self,
    ) -> (
        OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
        | None
    ):
        """
        id: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
        """
        return self._c_data[0][0]

    @patient_prior.setter  # set OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP.None
    def patient_prior(
        self,
        patient_prior: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
        | None,
    ):
        """
        id: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
        """
        self._c_data[0] = (patient_prior,)

    @property  # get OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP.None
    def patient_visit_prior(
        self,
    ) -> (
        OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP
        | None
    ):
        """
        id: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP
        """
        return self._c_data[1][0]

    @patient_visit_prior.setter  # set OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP.None
    def patient_visit_prior(
        self,
        patient_v_isit_prior: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP
        | None,
    ):
        """
        id: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_VISIT_PRIOR_GROUP
        """
        self._c_data[1] = (patient_v_isit_prior,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 34
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[2]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 34
        ---
        param_type: AL1.34 | tuple[AL1, ...]: (Patient Allergy Information, ...)
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
    ) -> tuple[
        OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP,
        ...,
    ]:
        """
        id: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
        """
        return self._c_data[3]

    @order_prior.setter  # set ORDER PRIOR
    def order_prior(
        self,
        order_prior: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
        | tuple[
            OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP,
            ...,
        ],
    ):
        """
        id: ORDER PRIOR SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP.None | tuple[OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_ORDER_PRIOR_GROUP
        """
        if isinstance(order_prior, tuple):
            self._c_data[3] = order_prior
        else:
            self._c_data[3] = (order_prior,)
