from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PDC import PDC
from ..segments.PSH import PSH


"""
PRODUCT - SUR_P09_FACILITY_GROUP_PRODUCT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SUR_P09_FACILITY_GROUP_PRODUCT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SUR_P09_FACILITY_GROUP_PRODUCT_GROUP
from utils.hl7.v2_5_1.segments import (
    PDC, PSH
)

sur_p09_facility_group_product_group = SUR_P09_FACILITY_GROUP_PRODUCT_GROUP(  # PRODUCT - Segment group for SUR_P09_FACILITY_GROUP - FACILITY consisting of PSH, PDC
    product_summary_header=psh,  # PSH(...)  # Required.
    product_detail_country=pdc,  # PDC(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SUR_P09_FACILITY_GROUP_PRODUCT_GROUP TEMPLATE-----
"""


class SUR_P09_FACILITY_GROUP_PRODUCT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SUR_P09_FACILITY_GROUP_PRODUCT_GROUP"""
    _hl7_name = """PRODUCT"""
    _hl7_description = """Segment group for SUR_P09_FACILITY_GROUP - FACILITY consisting of PSH, PDC"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SUR_P09_FACILITY_GROUP_PRODUCT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "R")
    _c_aliases = ("3", "4")
    _c_components = (PSH, PDC)
    _c_name = ("PSH", "PDC")
    _c_is_group = (False, False)
    _c_attrs = ("product_summary_header", "product_detail_country",)
    # fmt: on

    def __init__(
        self,
        product_summary_header: PSH,  #  Required. PSH.3
        product_detail_country: PDC,  #  Required. PDC.4
    ):
        """
        None - `SUR_P09_FACILITY_GROUP_PRODUCT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SUR_P09_FACILITY_GROUP_PRODUCT_GROUP>`_
        Segment group for SUR_P09_FACILITY_GROUP - FACILITY consisting of PSH, PDC

        :param product_summary_header: Product Summary Header (id: PSH | seq: 3 | use: R | rpt: 1)
        :param product_detail_country: Product Detail Country (id: PDC | seq: 4 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.product_summary_header = product_summary_header
        self.product_detail_country = product_detail_country

    @property  # get PSH.3
    def product_summary_header(self) -> PSH:
        """
        id: PSH | use: R | rpt: 1 | seq: 3
        ---
        return_type: PSH.3: Product Summary Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PSH
        """
        return self._c_data[0][0]

    @product_summary_header.setter  # set PSH.3
    def product_summary_header(self, psh: PSH):
        """
        id: PSH | use: R | rpt: 1 | seq: 3
        ---
        param_type: PSH.3: Product Summary Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PSH
        """
        self._c_data[0] = (psh,)

    @property  # get PDC.4
    def product_detail_country(self) -> PDC:
        """
        id: PDC | use: R | rpt: 1 | seq: 4
        ---
        return_type: PDC.4: Product Detail Country
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PDC
        """
        return self._c_data[1][0]

    @product_detail_country.setter  # set PDC.4
    def product_detail_country(self, pdc: PDC):
        """
        id: PDC | use: R | rpt: 1 | seq: 4
        ---
        param_type: PDC.4: Product Detail Country
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PDC
        """
        self._c_data[1] = (pdc,)
