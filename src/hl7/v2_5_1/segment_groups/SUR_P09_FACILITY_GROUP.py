from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.FAC import FAC
from ..segment_groups.SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP import (
    SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP,
)
from ..segment_groups.SUR_P09_FACILITY_GROUP_PRODUCT_GROUP import (
    SUR_P09_FACILITY_GROUP_PRODUCT_GROUP,
)
from ..segments.PSH import PSH


"""
FACILITY - SUR_P09_FACILITY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SUR_P09_FACILITY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SUR_P09_FACILITY_GROUP
from utils.hl7.v2_5_1.segments import (
    PSH, FAC
)
from utils.hl7.v2_5_1.segment_groups import (
    SUR_P09_FACILITY_GROUP_PRODUCT_GROUP, SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP
)

sur_p09_facility_group = SUR_P09_FACILITY_GROUP(  # FACILITY - Segment group for SUR_P09 - Summary product experience report consisting of FAC, PRODUCT, PSH, FACILITY DETAIL
    facility=fac,  # FAC(...)  # Required.
    product=sur_p09_facility_group_product_group,  # SUR_P09_FACILITY_GROUP_PRODUCT_GROUP(...)  # Required.
    product_summary_header=psh,  # PSH(...)  # Required.
    facility_detail=sur_p09_facility_group_facility_detail_group,  # SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SUR_P09_FACILITY_GROUP TEMPLATE-----
"""


class SUR_P09_FACILITY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SUR_P09_FACILITY_GROUP"""
    _hl7_name = """FACILITY"""
    _hl7_description = """Segment group for SUR_P09 - Summary product experience report consisting of FAC, PRODUCT, PSH, FACILITY DETAIL"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SUR_P09_FACILITY_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "R", "R", "R")
    _c_aliases = ("2", "None", "5", "None")
    _c_components = (FAC, SUR_P09_FACILITY_GROUP_PRODUCT_GROUP, PSH, SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP)
    _c_name = ("FAC", "PRODUCT", "PSH", "FACILITY DETAIL")
    _c_is_group = (False, True, False, True)
    _c_attrs = ("facility", "product", "product_summary_header", "facility_detail",)
    # fmt: on

    def __init__(
        self,
        facility: FAC,  #  Required. FAC.2
        product: SUR_P09_FACILITY_GROUP_PRODUCT_GROUP
        | tuple[
            SUR_P09_FACILITY_GROUP_PRODUCT_GROUP, ...
        ],  #  Required. (PSH.3, PDC.4, ...)
        product_summary_header: PSH,  #  Required. PSH.5
        facility_detail: SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP
        | tuple[
            SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP, ...
        ],  #  Required. (FAC.6, PDC.7, NTE.8, ...)
    ):
        """
        None - `SUR_P09_FACILITY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SUR_P09_FACILITY_GROUP>`_
        Segment group for SUR_P09 - Summary product experience report consisting of FAC, PRODUCT, PSH, FACILITY DETAIL

        :param facility: Facility (id: FAC | seq: 2 | use: R | rpt: 1)
        :param product: Product segment group: [PSH, PDC] (id: PRODUCT | seq: 3, 4 | use: R | rpt: *)
        :param product_summary_header: Product Summary Header (id: PSH | seq: 5 | use: R | rpt: 1)
        :param facility_detail: Facility Detail segment group: [FAC, PDC, NTE] (id: FACILITY DETAIL | seq: 6, 7, 8 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.facility = facility
        self.product = product
        self.product_summary_header = product_summary_header
        self.facility_detail = facility_detail

    @property  # get FAC.2
    def facility(self) -> FAC:
        """
        id: FAC | use: R | rpt: 1 | seq: 2
        ---
        return_type: FAC.2: Facility
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FAC
        """
        return self._c_data[0][0]

    @facility.setter  # set FAC.2
    def facility(self, fac: FAC):
        """
        id: FAC | use: R | rpt: 1 | seq: 2
        ---
        param_type: FAC.2: Facility
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FAC
        """
        self._c_data[0] = (fac,)

    @property  # get PRODUCT
    def product(self) -> tuple[SUR_P09_FACILITY_GROUP_PRODUCT_GROUP, ...]:
        """
        id: SUR_P09_FACILITY_GROUP_PRODUCT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[SUR_P09_FACILITY_GROUP_PRODUCT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SUR_P09_FACILITY_GROUP_PRODUCT_GROUP
        """
        return self._c_data[1]

    @product.setter  # set PRODUCT
    def product(
        self,
        product: SUR_P09_FACILITY_GROUP_PRODUCT_GROUP
        | tuple[SUR_P09_FACILITY_GROUP_PRODUCT_GROUP, ...],
    ):
        """
        id: PRODUCT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: SUR_P09_FACILITY_GROUP_PRODUCT_GROUP.None | tuple[SUR_P09_FACILITY_GROUP_PRODUCT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SUR_P09_FACILITY_GROUP_PRODUCT_GROUP
        """
        if isinstance(product, tuple):
            self._c_data[1] = product
        else:
            self._c_data[1] = (product,)

    @property  # get PSH.5
    def product_summary_header(self) -> PSH:
        """
        id: PSH | use: R | rpt: 1 | seq: 5
        ---
        return_type: PSH.5: Product Summary Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PSH
        """
        return self._c_data[2][0]

    @product_summary_header.setter  # set PSH.5
    def product_summary_header(self, psh: PSH):
        """
        id: PSH | use: R | rpt: 1 | seq: 5
        ---
        param_type: PSH.5: Product Summary Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PSH
        """
        self._c_data[2] = (psh,)

    @property  # get FACILITY DETAIL
    def facility_detail(
        self,
    ) -> tuple[SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP, ...]:
        """
        id: SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP
        """
        return self._c_data[3]

    @facility_detail.setter  # set FACILITY DETAIL
    def facility_detail(
        self,
        facility_detail: SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP
        | tuple[SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP, ...],
    ):
        """
        id: FACILITY DETAIL SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP.None | tuple[SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP
        """
        if isinstance(facility_detail, tuple):
            self._c_data[3] = facility_detail
        else:
            self._c_data[3] = (facility_detail,)
