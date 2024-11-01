from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ORC import ORC
from ..segment_groups.CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP import (
    CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP,
)


"""
STUDY PHARM - CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP
)

csu_c09_patient_group_study_phase_group_study_schedule_group_study_pharm_group = CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP(  # STUDY PHARM - Segment group for CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP - STUDY SCHEDULE consisting of ORC|None, RX ADMIN
    common_order=None,  # ORC(...) 
    rx_admin=csu_c09_patient_group_study_phase_group_study_schedule_group_study_pharm_group_rx_admin_group,  # CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP TEMPLATE-----
"""


class CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP"""
    _hl7_name = """STUDY PHARM"""
    _hl7_description = """Segment group for CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP - STUDY SCHEDULE consisting of ORC|None, RX ADMIN"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("16", "None")
    _c_components = (ORC, CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP)
    _c_name = ("ORC", "RX ADMIN")
    _c_is_group = (False, True)
    _c_attrs = ("common_order", "rx_admin",)
    # fmt: on

    def __init__(
        self,
        rx_admin: CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP
        | tuple[
            CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP,
            ...,
        ],  #  Required. (RXA.17, RXR.18, ...)
        common_order: ORC | None = None,  #  ORC.16
    ):
        """
        None - `CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP>`_
        Segment group for CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP - STUDY SCHEDULE consisting of ORC|None, RX ADMIN

        :param common_order: Common Order (id: ORC | seq: 16 | use: O | rpt: 1)
        :param rx_admin: Rx Admin segment group: [RXA, RXR] (id: RX ADMIN | seq: 17, 18 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.common_order = common_order
        self.rx_admin = rx_admin

    @property  # get ORC.16
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 16
        ---
        return_type: ORC.16: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.16
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 16
        ---
        param_type: ORC.16: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get RX ADMIN
    def rx_admin(
        self,
    ) -> tuple[
        CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP,
        ...,
    ]:
        """
        id: CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP
        """
        return self._c_data[1]

    @rx_admin.setter  # set RX ADMIN
    def rx_admin(
        self,
        rx_admin: CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP
        | tuple[
            CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP,
            ...,
        ],
    ):
        """
        id: RX ADMIN SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP.None | tuple[CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP
        """
        if isinstance(rx_admin, tuple):
            self._c_data[1] = rx_admin
        else:
            self._c_data[1] = (rx_admin,)
