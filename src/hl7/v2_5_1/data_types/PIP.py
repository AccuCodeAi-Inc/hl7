from __future__ import annotations
from ...base import DataType
from .CE import CE
from .EI import EI
from .DT import DT
from ..tables.PrivilegeClass import PrivilegeClass
from ..tables.Privilege import Privilege


"""
DataType - PIP
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::PIP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PIP,
    CE, EI, DT
)

pip = PIP(  # Practitioner Institutional Privileges - This data type specifies the institutional privileges with associated detail granted to a provider
    privilege=ce,  # CE(...)  # Required.
    privilege_class=None,  # CE(...) 
    expiration_date=None,  # DT(...) 
    activation_date=None,  # DT(...) 
    facility=None,  # EI(...) 
)

-----END COMPOSITE_DATA_TYPE::PIP TEMPLATE-----
"""


class PIP(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 1413
    _hl7_id = """PIP"""
    _hl7_name = """Practitioner Institutional Privileges"""
    _hl7_description = """This data type specifies the institutional privileges with associated detail granted to a provider"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP"
    _c_length = (483, 483, 8, 8, 427,)
    _c_rpt = (1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O",)
    _c_aliases = ("PIP.1", "PIP.2", "PIP.3", "PIP.4", "PIP.5",)
    _c_components = (CE, CE, DT, DT, EI,)
    _c_names = ("Privilege", "Privilege Class", "Expiration Date", "Activation Date", "Facility",)
    _c_attrs = ("privilege", "privilege_class", "expiration_date", "activation_date", "facility",)
    # fmt: on

    def __init__(
        self,
        privilege: Privilege | CE,  # PIP.1
        privilege_class: PrivilegeClass | CE | None = None,  # PIP.2
        expiration_date: DT | None = None,  # PIP.3
        activation_date: DT | None = None,  # PIP.4
        facility: EI | None = None,  # PIP.5
    ):
        """
        Practitioner Institutional Privileges - `PIP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PIP>`_
        This data type specifies the institutional privileges with associated detail granted to a provider.

        :param privilege: Specifies the institutional privilege itself (id: PIP.1 | len: 483 | use: R | rpt: 1)
        :param privilege_class: Specifies the class category of institutional privilege (id: PIP.2 | len: 483 | use: O | rpt: 1)
        :param expiration_date: Specifies the date the institutional privilege is/was no longer valid (id: PIP.3 | len: 8 | use: O | rpt: 1)
        :param activation_date: Specifies the date the institutional privilege became/becomes valid (id: PIP.4 | len: 8 | use: O | rpt: 1)
        :param facility: Specifies the facility in which the institutional privilege is/was valid (id: PIP.5 | len: 427 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.privilege = privilege
        self.privilege_class = privilege_class
        self.expiration_date = expiration_date
        self.activation_date = activation_date
        self.facility = facility

    @property  # get PIP.1
    def privilege(self) -> CE:
        """
        id: PIP.1 | len: 483 | use: R | rpt: 1
        ---
        Specifies the institutional privilege itself. Refer to user-defined table 0525 - Privilege for suggested values.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP.1
        """
        return self._c_data[0][0]

    @privilege.setter  # set PIP.1
    def privilege(self, ce: CE):
        """
        id: PIP.1 | len: 483 | use: R | rpt: 1
        ---
        Specifies the institutional privilege itself. Refer to user-defined table 0525 - Privilege for suggested values.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP.1
        """
        self._c_data[0] = (ce,)

    @property  # get PIP.2
    def privilege_class(self) -> CE | None:
        """
        id: PIP.2 | len: 483 | use: O | rpt: 1
        ---
        Specifies the class category of institutional privilege. Refer to User-Defined Table 0526 - Privilege Class for suggested values.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP.2
        """
        return self._c_data[1][0]

    @privilege_class.setter  # set PIP.2
    def privilege_class(self, ce: CE | None):
        """
        id: PIP.2 | len: 483 | use: O | rpt: 1
        ---
        Specifies the class category of institutional privilege. Refer to User-Defined Table 0526 - Privilege Class for suggested values.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP.2
        """
        self._c_data[1] = (ce,)

    @property  # get PIP.3
    def expiration_date(self) -> DT | None:
        """
        id: PIP.3 | len: 8 | use: O | rpt: 1
        ---
        Specifies the date the institutional privilege is/was no longer valid.
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP.3
        """
        return self._c_data[2][0]

    @expiration_date.setter  # set PIP.3
    def expiration_date(self, dt: DT | None):
        """
        id: PIP.3 | len: 8 | use: O | rpt: 1
        ---
        Specifies the date the institutional privilege is/was no longer valid.
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP.3
        """
        self._c_data[2] = (dt,)

    @property  # get PIP.4
    def activation_date(self) -> DT | None:
        """
        id: PIP.4 | len: 8 | use: O | rpt: 1
        ---
        Specifies the date the institutional privilege became/becomes valid.
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP.4
        """
        return self._c_data[3][0]

    @activation_date.setter  # set PIP.4
    def activation_date(self, dt: DT | None):
        """
        id: PIP.4 | len: 8 | use: O | rpt: 1
        ---
        Specifies the date the institutional privilege became/becomes valid.
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP.4
        """
        self._c_data[3] = (dt,)

    @property  # get PIP.5
    def facility(self) -> EI | None:
        """
        id: PIP.5 | len: 427 | use: O | rpt: 1
        ---
        Specifies the facility in which the institutional privilege is/was valid.
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP.5
        """
        return self._c_data[4][0]

    @facility.setter  # set PIP.5
    def facility(self, ei: EI | None):
        """
        id: PIP.5 | len: 427 | use: O | rpt: 1
        ---
        Specifies the facility in which the institutional privilege is/was valid.
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PIP.5
        """
        self._c_data[4] = (ei,)
