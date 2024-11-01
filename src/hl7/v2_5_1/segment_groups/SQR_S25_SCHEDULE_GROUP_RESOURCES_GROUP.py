from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP import (
    SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP,
)
from ..segment_groups.SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP import (
    SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP,
)
from ..segment_groups.SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP import (
    SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP,
)
from ..segment_groups.SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP import (
    SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP,
)
from ..segments.RGS import RGS


"""
RESOURCES - SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP
from utils.hl7.v2_5_1.segments import (
    RGS
)
from utils.hl7.v2_5_1.segment_groups import (
    SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP, SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
)

sqr_s25_schedule_group_resources_group = SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP(  # RESOURCES - Segment group for SQR_S25_SCHEDULE_GROUP - SCHEDULE consisting of RGS, SERVICE|None, GENERAL RESOURCE|None, PERSONNEL RESOURCE|None, LOCATION RESOURCE|None
    resource_group=rgs,  # RGS(...)  # Required.
    service=None,  # SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP(...) 
    general_resource=None,  # SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP(...) 
    personnel_resource=None,  # SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP(...) 
    location_resource=None,  # SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP TEMPLATE-----
"""


class SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP"""
    _hl7_name = """RESOURCES"""
    _hl7_description = """Segment group for SQR_S25_SCHEDULE_GROUP - SCHEDULE consisting of RGS, SERVICE|None, GENERAL RESOURCE|None, PERSONNEL RESOURCE|None, LOCATION RESOURCE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("12", "None", "None", "None", "None")
    _c_components = (RGS, SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP, SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP)
    _c_name = ("RGS", "SERVICE", "GENERAL RESOURCE", "PERSONNEL RESOURCE", "LOCATION RESOURCE")
    _c_is_group = (False, True, True, True, True)
    _c_attrs = ("resource_group", "service", "general_resource", "personnel_resource", "location_resource",)
    # fmt: on

    def __init__(
        self,
        resource_group: RGS,  #  Required. RGS.12
        service: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP
        | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP, ...]
        | None = None,  #  (AIS.13, NTE.14, ...)
        general_resource: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
        | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, ...]
        | None = None,  #  (AIG.15, NTE.16, ...)
        personnel_resource: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
        | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, ...]
        | None = None,  #  (AIP.17, NTE.18, ...)
        location_resource: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
        | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, ...]
        | None = None,  #  (AIL.19, NTE.20, ...)
    ):
        """
        None - `SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP>`_
        Segment group for SQR_S25_SCHEDULE_GROUP - SCHEDULE consisting of RGS, SERVICE|None, GENERAL RESOURCE|None, PERSONNEL RESOURCE|None, LOCATION RESOURCE|None

        :param resource_group: Resource Group (id: RGS | seq: 12 | use: R | rpt: 1)
        :param service: Service segment group: [AIS, NTE|None] (id: SERVICE | seq: 13, 14 | use: O | rpt: *)
        :param general_resource: General Resource segment group: [AIG, NTE|None] (id: GENERAL RESOURCE | seq: 15, 16 | use: O | rpt: *)
        :param personnel_resource: Personnel Resource segment group: [AIP, NTE|None] (id: PERSONNEL RESOURCE | seq: 17, 18 | use: O | rpt: *)
        :param location_resource: Location Resource segment group: [AIL, NTE|None] (id: LOCATION RESOURCE | seq: 19, 20 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.resource_group = resource_group
        self.service = service
        self.general_resource = general_resource
        self.personnel_resource = personnel_resource
        self.location_resource = location_resource

    @property  # get RGS.12
    def resource_group(self) -> RGS:
        """
        id: RGS | use: R | rpt: 1 | seq: 12
        ---
        return_type: RGS.12: Resource Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGS
        """
        return self._c_data[0][0]

    @resource_group.setter  # set RGS.12
    def resource_group(self, rgs: RGS):
        """
        id: RGS | use: R | rpt: 1 | seq: 12
        ---
        param_type: RGS.12: Resource Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGS
        """
        self._c_data[0] = (rgs,)

    @property  # get SERVICE
    def service(
        self,
    ) -> tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP, ...] | tuple[None]:
        """
        id: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP
        """
        return self._c_data[1]

    @service.setter  # set SERVICE
    def service(
        self,
        service: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP
        | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP, ...]
        | None,
    ):
        """
        id: SERVICE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP.None | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_SERVICE_GROUP
        """
        if isinstance(service, tuple):
            self._c_data[1] = service
        else:
            self._c_data[1] = (service,)

    @property  # get GENERAL RESOURCE
    def general_resource(
        self,
    ) -> (
        tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, ...]
        | tuple[None]
    ):
        """
        id: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
        """
        return self._c_data[2]

    @general_resource.setter  # set GENERAL RESOURCE
    def general_resource(
        self,
        general_resource: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
        | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, ...]
        | None,
    ):
        """
        id: GENERAL RESOURCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP.None | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
        """
        if isinstance(general_resource, tuple):
            self._c_data[2] = general_resource
        else:
            self._c_data[2] = (general_resource,)

    @property  # get PERSONNEL RESOURCE
    def personnel_resource(
        self,
    ) -> (
        tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, ...]
        | tuple[None]
    ):
        """
        id: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
        """
        return self._c_data[3]

    @personnel_resource.setter  # set PERSONNEL RESOURCE
    def personnel_resource(
        self,
        personnel_resource: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
        | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, ...]
        | None,
    ):
        """
        id: PERSONNEL RESOURCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP.None | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
        """
        if isinstance(personnel_resource, tuple):
            self._c_data[3] = personnel_resource
        else:
            self._c_data[3] = (personnel_resource,)

    @property  # get LOCATION RESOURCE
    def location_resource(
        self,
    ) -> (
        tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, ...]
        | tuple[None]
    ):
        """
        id: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
        """
        return self._c_data[4]

    @location_resource.setter  # set LOCATION RESOURCE
    def location_resource(
        self,
        location_resource: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
        | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, ...]
        | None,
    ):
        """
        id: LOCATION RESOURCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP.None | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
        """
        if isinstance(location_resource, tuple):
            self._c_data[4] = location_resource
        else:
            self._c_data[4] = (location_resource,)
