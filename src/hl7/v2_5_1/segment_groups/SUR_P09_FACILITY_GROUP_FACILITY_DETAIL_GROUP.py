from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.FAC import FAC
from ..segments.PDC import PDC


"""
FACILITY DETAIL - SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    PDC, NTE, FAC
)

sur_p09_facility_group_facility_detail_group = SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP(  # FACILITY DETAIL - Segment group for SUR_P09_FACILITY_GROUP - FACILITY consisting of FAC, PDC, NTE
    facility=fac,  # FAC(...)  # Required.
    product_detail_country=pdc,  # PDC(...)  # Required.
    notes_and_comments=nte,  # NTE(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP TEMPLATE-----
"""


class SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP"""
    _hl7_name = """FACILITY DETAIL"""
    _hl7_description = """Segment group for SUR_P09_FACILITY_GROUP - FACILITY consisting of FAC, PDC, NTE"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 1)
    _c_usage = ("R", "R", "R")
    _c_aliases = ("6", "7", "8")
    _c_components = (FAC, PDC, NTE)
    _c_name = ("FAC", "PDC", "NTE")
    _c_is_group = (False, False, False)
    _c_attrs = ("facility", "product_detail_country", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        facility: FAC,  #  Required. FAC.6
        product_detail_country: PDC,  #  Required. PDC.7
        notes_and_comments: NTE,  #  Required. NTE.8
    ):
        """
        None - `SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SUR_P09_FACILITY_GROUP_FACILITY_DETAIL_GROUP>`_
        Segment group for SUR_P09_FACILITY_GROUP - FACILITY consisting of FAC, PDC, NTE

        :param facility: Facility (id: FAC | seq: 6 | use: R | rpt: 1)
        :param product_detail_country: Product Detail Country (id: PDC | seq: 7 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 8 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.facility = facility
        self.product_detail_country = product_detail_country
        self.notes_and_comments = notes_and_comments

    @property  # get FAC.6
    def facility(self) -> FAC:
        """
        id: FAC | use: R | rpt: 1 | seq: 6
        ---
        return_type: FAC.6: Facility
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FAC
        """
        return self._c_data[0][0]

    @facility.setter  # set FAC.6
    def facility(self, fac: FAC):
        """
        id: FAC | use: R | rpt: 1 | seq: 6
        ---
        param_type: FAC.6: Facility
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FAC
        """
        self._c_data[0] = (fac,)

    @property  # get PDC.7
    def product_detail_country(self) -> PDC:
        """
        id: PDC | use: R | rpt: 1 | seq: 7
        ---
        return_type: PDC.7: Product Detail Country
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PDC
        """
        return self._c_data[1][0]

    @product_detail_country.setter  # set PDC.7
    def product_detail_country(self, pdc: PDC):
        """
        id: PDC | use: R | rpt: 1 | seq: 7
        ---
        param_type: PDC.7: Product Detail Country
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PDC
        """
        self._c_data[1] = (pdc,)

    @property  # get NTE.8
    def notes_and_comments(self) -> NTE:
        """
        id: NTE | use: R | rpt: 1 | seq: 8
        ---
        return_type: NTE.8: Notes and Comments
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2][0]

    @notes_and_comments.setter  # set NTE.8
    def notes_and_comments(self, nte: NTE):
        """
        id: NTE | use: R | rpt: 1 | seq: 8
        ---
        param_type: NTE.8: Notes and Comments
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        self._c_data[2] = (nte,)
