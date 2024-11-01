from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CCD import CCD
from ..data_types.CWE import CWE
from ..data_types.ID import ID
from ..data_types.CX import CX
from ..tables.ChargeType import ChargeType
from ..tables.ChargeTypeReason import ChargeTypeReason


"""
Billing - BLG
HL7 Version: 2.5.1

-----BEGIN SEGMENT::BLG TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    BLG,
    CCD, CWE, ID, CX
)

blg = BLG(  #  - The BLG segment is used to provide billing information, on the ordered service, to the filling application
    when_to_charge=None,  # CCD(...) 
    charge_type=None,  # ID(...) 
    account_id=None,  # CX(...) 
    charge_type_reason=None,  # CWE(...) 
)

-----END SEGMENT::BLG TEMPLATE-----
"""


class BLG(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """BLG"""
    _hl7_name = """Billing"""
    _hl7_description = """The BLG segment is used to provide billing information, on the ordered service, to the filling application"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG"
    _c_length = (40, 50, 100, 60,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O",)
    _c_components = (CCD, ID, CX, CWE,)
    _c_aliases = ("BLG.1", "BLG.2", "BLG.3", "BLG.4",)
    _c_names = ("When to Charge", "Charge Type", "Account ID", "Charge Type Reason",)
    _c_attrs = ("when_to_charge", "charge_type", "account_id", "charge_type_reason",)
    # fmt: on

    def __init__(
        self,
        when_to_charge: CCD | tuple[CCD] | None = None,  # BLG.1
        charge_type: ChargeType | ID | tuple[ChargeType | ID] | None = None,  # BLG.2
        account_id: CX | tuple[CX] | None = None,  # BLG.3
        charge_type_reason: ChargeTypeReason
        | CWE
        | tuple[ChargeTypeReason | CWE]
        | None = None,  # BLG.4
    ):
        """
        Billing - `BLG <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG>`_
        The BLG segment is used to provide billing information, on the ordered service, to the filling application.

        :param when_to_charge: Charge Code and Date (id: BLG.1 | len: 40 | use: O | rpt: 1)
        :param charge_type: Coded values for HL7 tables (id: BLG.2 | len: 50 | use: O | rpt: 1)
        :param account_id: Extended Composite ID with Check Digit (id: BLG.3 | len: 100 | use: O | rpt: 1)
        :param charge_type_reason: Coded with Exceptions (id: BLG.4 | len: 60 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.when_to_charge = when_to_charge
        self.charge_type = charge_type
        self.account_id = account_id
        self.charge_type_reason = charge_type_reason

    @property  # get BLG.1
    def when_to_charge(self) -> CCD | None:
        """
        id: BLG.1 | len: 40 | use: O | rpt: 1
        ---
        return_type: CCD: Charge Code and Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLG.1
        """
        return self._c_data[0][0]

    @when_to_charge.setter  # set BLG.1
    def when_to_charge(self, ccd: CCD | None):
        """
        id: BLG.1 | len: 40 | use: O | rpt: 1
        ---
        param_type: CCD: Charge Code and Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLG.1
        """
        self._c_data[0] = (ccd,)

    @property  # get BLG.2
    def charge_type(self) -> ChargeType | None:
        """
        id: BLG.2 | len: 50 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLG.2
        """
        return self._c_data[1][0]

    @charge_type.setter  # set BLG.2
    def charge_type(self, charge_type: ChargeType | None):
        """
        id: BLG.2 | len: 50 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLG.2
        """
        self._c_data[1] = (charge_type,)

    @property  # get BLG.3
    def account_id(self) -> CX | None:
        """
        id: BLG.3 | len: 100 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLG.3
        """
        return self._c_data[2][0]

    @account_id.setter  # set BLG.3
    def account_id(self, cx: CX | None):
        """
        id: BLG.3 | len: 100 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLG.3
        """
        self._c_data[2] = (cx,)

    @property  # get BLG.4
    def charge_type_reason(self) -> ChargeTypeReason | None:
        """
        id: BLG.4 | len: 60 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLG.4
        """
        return self._c_data[3][0]

    @charge_type_reason.setter  # set BLG.4
    def charge_type_reason(self, charge_type_reason: ChargeTypeReason | None):
        """
        id: BLG.4 | len: 60 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLG.4
        """
        self._c_data[3] = (charge_type_reason,)
