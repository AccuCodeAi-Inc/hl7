from __future__ import annotations
from ...base import HL7Segment
from ..data_types.XCN import XCN
from ..data_types.CWE import CWE
from ..data_types.TX import TX
from ..tables.OverrideCode import OverrideCode
from ..tables.OverrideType import OverrideType


"""
Override Segment - OVR
HL7 Version: 2.5.1

-----BEGIN SEGMENT::OVR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OVR,
    XCN, CWE, TX
)

ovr = OVR(  #  - Definition: This segment allows a sender to override specific receiving applications business rules to allow for processing of a message that would normally be rejected or ignored
    business_rule_override_type=None,  # CWE(...) 
    business_rule_override_code=None,  # CWE(...) 
    override_comments=None,  # TX(...) 
    override_entered_by=None,  # XCN(...) 
    override_authorized_by=None,  # XCN(...) 
)

-----END SEGMENT::OVR TEMPLATE-----
"""


class OVR(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """OVR"""
    _hl7_name = """Override Segment"""
    _hl7_description = """Definition: This segment allows a sender to override specific receiving applications business rules to allow for processing of a message that would normally be rejected or ignored"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OVR"
    _c_length = (705, 705, 200, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O",)
    _c_components = (CWE, CWE, TX, XCN, XCN,)
    _c_aliases = ("OVR.1", "OVR.2", "OVR.3", "OVR.4", "OVR.5",)
    _c_names = ("Business Rule Override Type", "Business Rule Override Code", "Override Comments", "Override Entered By", "Override Authorized By",)
    _c_attrs = ("business_rule_override_type", "business_rule_override_code", "override_comments", "override_entered_by", "override_authorized_by",)
    # fmt: on

    def __init__(
        self,
        business_rule_override_type: OverrideType | CWE | None = None,  # OVR.1
        business_rule_override_code: OverrideCode | CWE | None = None,  # OVR.2
        override_comments: TX | None = None,  # OVR.3
        override_entered_by: XCN | None = None,  # OVR.4
        override_authorized_by: XCN | None = None,  # OVR.5
    ):
        """
                Override Segment - `OVR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OVR>`_
                Definition: This segment allows a sender to override specific receiving applications business rules to allow for processing of a message that would normally be rejected or ignored.

        The following is an example of how the OVR segment might be used in a dispense message (RDS_O13): MSH PID PV1 {ORC RXE {RXR} RXD {RXR} <RXC> <NTE> <FT1> <OVR>}

                :param business_rule_override_type: Coded with Exceptions (id: OVR.1 | len: 705 | use: O | rpt: 1)
                :param business_rule_override_code: Coded with Exceptions (id: OVR.2 | len: 705 | use: O | rpt: 1)
                :param override_comments: Text Data (id: OVR.3 | len: 200 | use: O | rpt: 1)
                :param override_entered_by: Extended Composite ID Number and Name for Persons (id: OVR.4 | len: 250 | use: O | rpt: 1)
                :param override_authorized_by: Extended Composite ID Number and Name for Persons (id: OVR.5 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.business_rule_override_type = business_rule_override_type
        self.business_rule_override_code = business_rule_override_code
        self.override_comments = override_comments
        self.override_entered_by = override_entered_by
        self.override_authorized_by = override_authorized_by

    @property  # get OVR.1
    def business_rule_override_type(self) -> OverrideType | None:
        """
        id: OVR.1 | len: 705 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OVR.1
        """
        return self._c_data[0][0]

    @business_rule_override_type.setter  # set OVR.1
    def business_rule_override_type(self, override_type: OverrideType | None):
        """
        id: OVR.1 | len: 705 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OVR.1
        """
        self._c_data[0] = (override_type,)

    @property  # get OVR.2
    def business_rule_override_code(self) -> OverrideCode | None:
        """
        id: OVR.2 | len: 705 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OVR.2
        """
        return self._c_data[1][0]

    @business_rule_override_code.setter  # set OVR.2
    def business_rule_override_code(self, override_code: OverrideCode | None):
        """
        id: OVR.2 | len: 705 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OVR.2
        """
        self._c_data[1] = (override_code,)

    @property  # get OVR.3
    def override_comments(self) -> TX | None:
        """
        id: OVR.3 | len: 200 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OVR.3
        """
        return self._c_data[2][0]

    @override_comments.setter  # set OVR.3
    def override_comments(self, tx: TX | None):
        """
        id: OVR.3 | len: 200 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OVR.3
        """
        self._c_data[2] = (tx,)

    @property  # get OVR.4
    def override_entered_by(self) -> XCN | None:
        """
        id: OVR.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OVR.4
        """
        return self._c_data[3][0]

    @override_entered_by.setter  # set OVR.4
    def override_entered_by(self, xcn: XCN | None):
        """
        id: OVR.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OVR.4
        """
        self._c_data[3] = (xcn,)

    @property  # get OVR.5
    def override_authorized_by(self) -> XCN | None:
        """
        id: OVR.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OVR.5
        """
        return self._c_data[4][0]

    @override_authorized_by.setter  # set OVR.5
    def override_authorized_by(self, xcn: XCN | None):
        """
        id: OVR.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OVR.5
        """
        self._c_data[4] = (xcn,)
