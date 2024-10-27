from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..tables.SegmentActionCode import SegmentActionCode


"""
Resource Group - RGS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RGS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RGS,
    ID, SI, CE
)

rgs = RGS(  #  - The RGS segment is used to identify relationships between resources identified for a scheduled event
    set_id_rgs=si,  # SI(...)  # Required.
    segment_action_code=None,  # ID(...) 
    resource_group_id=None,  # CE(...) 
)

-----END SEGMENT::RGS TEMPLATE-----
"""


class RGS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RGS"""
    _hl7_name = """Resource Group"""
    _hl7_description = """The RGS segment is used to identify relationships between resources identified for a scheduled event"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGS"
    _c_length = (4, 3, 250,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("R", "C", "O",)
    _c_components = (SI, ID, CE,)
    _c_aliases = ("RGS.1", "RGS.2", "RGS.3",)
    _c_names = ("Set ID - RGS", "Segment Action Code", "Resource Group ID",)
    _c_attrs = ("set_id_rgs", "segment_action_code", "resource_group_id",)
    # fmt: on

    def __init__(
        self,
        set_id_rgs: SI,  # RGS.1
        segment_action_code: SegmentActionCode | ID | None = None,  # RGS.2
        resource_group_id: CE | None = None,  # RGS.3
    ):
        """
                Resource Group - `RGS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGS>`_
                The RGS segment is used to identify relationships between resources identified for a scheduled event. This segment can be used, on a site specified basis, to identify groups of resources that are used together within a scheduled event, or to describe some other relationship between resources. To specify related groups of resources within a message, begin each group with an RGS segment, and then follow that RGS with one or more of the Appointment Information segments (AIG, AIL, AIS, or AIP).

        If a message does not require any grouping of resources, then specify a single RGS in the message, and follow it with all of the Appointment Information segments for the scheduled event.   (At least one RGS segment is required in each message – even if no grouping of resources is required – to allow parsers to properly understand the message.)

                :param set_id_rgs: Sequence ID (id: RGS.1 | len: 4 | use: R | rpt: 1)
                :param segment_action_code: Coded values for HL7 tables (id: RGS.2 | len: 3 | use: C | rpt: 1)
                :param resource_group_id: Coded Element (id: RGS.3 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.set_id_rgs = set_id_rgs
        self.segment_action_code = segment_action_code
        self.resource_group_id = resource_group_id

    @property  # get RGS.1
    def set_id_rgs(self) -> SI:
        """
        id: RGS.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RGS.1
        """
        return self._c_data[0][0]

    @set_id_rgs.setter  # set RGS.1
    def set_id_rgs(self, si: SI):
        """
        id: RGS.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RGS.1
        """
        self._c_data[0] = (si,)

    @property  # get RGS.2
    def segment_action_code(self) -> SegmentActionCode | None:
        """
        id: RGS.2 | len: 3 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RGS.2
        """
        return self._c_data[1][0]

    @segment_action_code.setter  # set RGS.2
    def segment_action_code(self, segment_action_code: SegmentActionCode | None):
        """
        id: RGS.2 | len: 3 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RGS.2
        """
        self._c_data[1] = (segment_action_code,)

    @property  # get RGS.3
    def resource_group_id(self) -> CE | None:
        """
        id: RGS.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RGS.3
        """
        return self._c_data[2][0]

    @resource_group_id.setter  # set RGS.3
    def resource_group_id(self, ce: CE | None):
        """
        id: RGS.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RGS.3
        """
        self._c_data[2] = (ce,)
