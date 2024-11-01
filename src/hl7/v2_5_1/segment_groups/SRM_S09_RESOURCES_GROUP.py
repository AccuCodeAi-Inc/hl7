from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP import (
    SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP,
)
from ..segment_groups.SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP import (
    SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP,
)
from ..segment_groups.SRM_S09_RESOURCES_GROUP_SERVICE_GROUP import (
    SRM_S09_RESOURCES_GROUP_SERVICE_GROUP,
)
from ..segment_groups.SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP import (
    SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP,
)
from ..segments.RGS import RGS


"""
RESOURCES - SRM_S09_RESOURCES_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SRM_S09_RESOURCES_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SRM_S09_RESOURCES_GROUP
from utils.hl7.v2_5_1.segments import (
    RGS
)
from utils.hl7.v2_5_1.segment_groups import (
    SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, SRM_S09_RESOURCES_GROUP_SERVICE_GROUP, SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
)

srm_s09_resources_group = SRM_S09_RESOURCES_GROUP(  # RESOURCES - Segment group for SRM_S09 - Schedule request - Cancellation of service/resource on appointment consisting of RGS, SERVICE|None, GENERAL RESOURCE|None, LOCATION RESOURCE|None, PERSONNEL RESOURCE|None
    resource_group=rgs,  # RGS(...)  # Required.
    service=None,  # SRM_S09_RESOURCES_GROUP_SERVICE_GROUP(...) 
    general_resource=None,  # SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP(...) 
    location_resource=None,  # SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP(...) 
    personnel_resource=None,  # SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SRM_S09_RESOURCES_GROUP TEMPLATE-----
"""


class SRM_S09_RESOURCES_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SRM_S09_RESOURCES_GROUP"""
    _hl7_name = """RESOURCES"""
    _hl7_description = """Segment group for SRM_S09 - Schedule request - Cancellation of service/resource on appointment consisting of RGS, SERVICE|None, GENERAL RESOURCE|None, LOCATION RESOURCE|None, PERSONNEL RESOURCE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S09_RESOURCES_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("10", "None", "None", "None", "None")
    _c_components = (RGS, SRM_S09_RESOURCES_GROUP_SERVICE_GROUP, SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP)
    _c_name = ("RGS", "SERVICE", "GENERAL RESOURCE", "LOCATION RESOURCE", "PERSONNEL RESOURCE")
    _c_is_group = (False, True, True, True, True)
    _c_attrs = ("resource_group", "service", "general_resource", "location_resource", "personnel_resource",)
    # fmt: on

    def __init__(
        self,
        resource_group: RGS,  #  Required. RGS.10
        service: SRM_S09_RESOURCES_GROUP_SERVICE_GROUP
        | tuple[SRM_S09_RESOURCES_GROUP_SERVICE_GROUP, ...]
        | None = None,  #  (AIS.11, APR.12, NTE.13, ...)
        general_resource: SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
        | tuple[SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, ...]
        | None = None,  #  (AIG.14, APR.15, NTE.16, ...)
        location_resource: SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
        | tuple[SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, ...]
        | None = None,  #  (AIL.17, APR.18, NTE.19, ...)
        personnel_resource: SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
        | tuple[SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, ...]
        | None = None,  #  (AIP.20, APR.21, NTE.22, ...)
    ):
        """
        None - `SRM_S09_RESOURCES_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S09_RESOURCES_GROUP>`_
        Segment group for SRM_S09 - Schedule request - Cancellation of service/resource on appointment consisting of RGS, SERVICE|None, GENERAL RESOURCE|None, LOCATION RESOURCE|None, PERSONNEL RESOURCE|None

        :param resource_group: Resource Group (id: RGS | seq: 10 | use: R | rpt: 1)
        :param service: Service segment group: [AIS, APR|None, NTE|None] (id: SERVICE | seq: 11, 12, 13 | use: O | rpt: *)
        :param general_resource: General Resource segment group: [AIG, APR|None, NTE|None] (id: GENERAL RESOURCE | seq: 14, 15, 16 | use: O | rpt: *)
        :param location_resource: Location Resource segment group: [AIL, APR|None, NTE|None] (id: LOCATION RESOURCE | seq: 17, 18, 19 | use: O | rpt: *)
        :param personnel_resource: Personnel Resource segment group: [AIP, APR|None, NTE|None] (id: PERSONNEL RESOURCE | seq: 20, 21, 22 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.resource_group = resource_group
        self.service = service
        self.general_resource = general_resource
        self.location_resource = location_resource
        self.personnel_resource = personnel_resource

    @property  # get RGS.10
    def resource_group(self) -> RGS:
        """
        id: RGS | use: R | rpt: 1 | seq: 10
        ---
        return_type: RGS.10: Resource Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGS
        """
        return self._c_data[0][0]

    @resource_group.setter  # set RGS.10
    def resource_group(self, rgs: RGS):
        """
        id: RGS | use: R | rpt: 1 | seq: 10
        ---
        param_type: RGS.10: Resource Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGS
        """
        self._c_data[0] = (rgs,)

    @property  # get SERVICE
    def service(
        self,
    ) -> tuple[SRM_S09_RESOURCES_GROUP_SERVICE_GROUP, ...] | tuple[None]:
        """
        id: SRM_S09_RESOURCES_GROUP_SERVICE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SRM_S09_RESOURCES_GROUP_SERVICE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S09_RESOURCES_GROUP_SERVICE_GROUP
        """
        return self._c_data[1]

    @service.setter  # set SERVICE
    def service(
        self,
        service: SRM_S09_RESOURCES_GROUP_SERVICE_GROUP
        | tuple[SRM_S09_RESOURCES_GROUP_SERVICE_GROUP, ...]
        | None,
    ):
        """
        id: SERVICE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SRM_S09_RESOURCES_GROUP_SERVICE_GROUP.None | tuple[SRM_S09_RESOURCES_GROUP_SERVICE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S09_RESOURCES_GROUP_SERVICE_GROUP
        """
        if isinstance(service, tuple):
            self._c_data[1] = service
        else:
            self._c_data[1] = (service,)

    @property  # get GENERAL RESOURCE
    def general_resource(
        self,
    ) -> tuple[SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, ...] | tuple[None]:
        """
        id: SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
        """
        return self._c_data[2]

    @general_resource.setter  # set GENERAL RESOURCE
    def general_resource(
        self,
        general_resource: SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
        | tuple[SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, ...]
        | None,
    ):
        """
        id: GENERAL RESOURCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP.None | tuple[SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S09_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
        """
        if isinstance(general_resource, tuple):
            self._c_data[2] = general_resource
        else:
            self._c_data[2] = (general_resource,)

    @property  # get LOCATION RESOURCE
    def location_resource(
        self,
    ) -> tuple[SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, ...] | tuple[None]:
        """
        id: SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
        """
        return self._c_data[3]

    @location_resource.setter  # set LOCATION RESOURCE
    def location_resource(
        self,
        location_resource: SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
        | tuple[SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, ...]
        | None,
    ):
        """
        id: LOCATION RESOURCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP.None | tuple[SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S09_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
        """
        if isinstance(location_resource, tuple):
            self._c_data[3] = location_resource
        else:
            self._c_data[3] = (location_resource,)

    @property  # get PERSONNEL RESOURCE
    def personnel_resource(
        self,
    ) -> tuple[SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, ...] | tuple[None]:
        """
        id: SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
        """
        return self._c_data[4]

    @personnel_resource.setter  # set PERSONNEL RESOURCE
    def personnel_resource(
        self,
        personnel_resource: SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
        | tuple[SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, ...]
        | None,
    ):
        """
        id: PERSONNEL RESOURCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP.None | tuple[SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S09_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
        """
        if isinstance(personnel_resource, tuple):
            self._c_data[4] = personnel_resource
        else:
            self._c_data[4] = (personnel_resource,)
