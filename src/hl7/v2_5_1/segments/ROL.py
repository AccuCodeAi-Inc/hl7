from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TS import TS
from ..data_types.XCN import XCN
from ..data_types.XAD import XAD
from ..data_types.XTN import XTN
from ..data_types.ID import ID
from ..data_types.EI import EI
from ..tables.ProviderRole import ProviderRole
from ..tables.ProblemOrGoalActionCode import ProblemOrGoalActionCode
from ..tables.OrganizationUnitType import OrganizationUnitType


"""
Role - ROL
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ROL TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ROL,
    CE, TS, XCN, XAD, XTN, ID, EI
)

rol = ROL(  #  - The role segment contains the data necessary to add, update, correct, and delete from the record persons involved, as well as their functional involvement with the activity being transmitted
    role_instance_id=None,  # EI(...) 
    action_code=id,  # ID(...)  # Required.
    role_rol=ce,  # CE(...)  # Required.
    role_person=xcn,  # XCN(...)  # Required.
    role_begin_date_or_time=None,  # TS(...) 
    role_end_date_or_time=None,  # TS(...) 
    role_duration=None,  # CE(...) 
    role_action_reason=None,  # CE(...) 
    provider_type=None,  # CE(...) 
    organization_unit_type=None,  # CE(...) 
    office_or_home_address_or_birthplace=None,  # XAD(...) 
    phone=None,  # XTN(...) 
)

-----END SEGMENT::ROL TEMPLATE-----
"""


class ROL(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ROL"""
    _hl7_name = """Role"""
    _hl7_description = """The role segment contains the data necessary to add, update, correct, and delete from the record persons involved, as well as their functional involvement with the activity being transmitted"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL"
    _c_length = (60, 2, 250, 250, 26, 26, 250, 250, 250, 250, 250, 250,)
    _c_rpt = (1, 1, 1, 65535, 1, 1, 1, 1, 65535, 1, 65535, 65535,)
    _c_usage = ("C", "R", "R", "R", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (EI, ID, CE, XCN, TS, TS, CE, CE, CE, CE, XAD, XTN,)
    _c_aliases = ("ROL.1", "ROL.2", "ROL.3", "ROL.4", "ROL.5", "ROL.6", "ROL.7", "ROL.8", "ROL.9", "ROL.10", "ROL.11", "ROL.12",)
    _c_names = ("Role Instance ID", "Action Code", "Role-ROL", "Role Person", "Role Begin Date/Time", "Role End Date/Time", "Role Duration", "Role Action Reason", "Provider Type", "Organization Unit Type", "Office/Home Address/Birthplace", "Phone",)
    _c_attrs = ("role_instance_id", "action_code", "role_rol", "role_person", "role_begin_date_or_time", "role_end_date_or_time", "role_duration", "role_action_reason", "provider_type", "organization_unit_type", "office_or_home_address_or_birthplace", "phone",)
    # fmt: on

    def __init__(
        self,
        action_code: ProblemOrGoalActionCode
        | ID
        | tuple[ProblemOrGoalActionCode | ID, ...],  # ROL.2
        role_rol: ProviderRole | CE | tuple[ProviderRole | CE, ...],  # ROL.3
        role_person: XCN | tuple[XCN, ...],  # ROL.4
        role_instance_id: EI | tuple[EI, ...] | None = None,  # ROL.1
        role_begin_date_or_time: TS | tuple[TS, ...] | None = None,  # ROL.5
        role_end_date_or_time: TS | tuple[TS, ...] | None = None,  # ROL.6
        role_duration: CE | tuple[CE, ...] | None = None,  # ROL.7
        role_action_reason: CE | tuple[CE, ...] | None = None,  # ROL.8
        provider_type: CE | tuple[CE, ...] | None = None,  # ROL.9
        organization_unit_type: OrganizationUnitType
        | CE
        | tuple[OrganizationUnitType | CE, ...]
        | None = None,  # ROL.10
        office_or_home_address_or_birthplace: XAD
        | tuple[XAD, ...]
        | None = None,  # ROL.11
        phone: XTN | tuple[XTN, ...] | None = None,  # ROL.12
    ):
        """
        Role - `ROL <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL>`_
        The role segment contains the data necessary to add, update, correct, and delete from the record persons involved, as well as their functional involvement with the activity being transmitted.

        :param role_instance_id: Entity Identifier (id: ROL.1 | len: 60 | use: C | rpt: 1)
        :param action_code: Coded values for HL7 tables (id: ROL.2 | len: 2 | use: R | rpt: 1)
        :param role_rol: Coded Element (id: ROL.3 | len: 250 | use: R | rpt: 1)
        :param role_person: Extended Composite ID Number and Name for Persons (id: ROL.4 | len: 250 | use: R | rpt: *)
        :param role_begin_date_or_time: Time Stamp (id: ROL.5 | len: 26 | use: O | rpt: 1)
        :param role_end_date_or_time: Time Stamp (id: ROL.6 | len: 26 | use: O | rpt: 1)
        :param role_duration: Coded Element (id: ROL.7 | len: 250 | use: O | rpt: 1)
        :param role_action_reason: Coded Element (id: ROL.8 | len: 250 | use: O | rpt: 1)
        :param provider_type: Coded Element (id: ROL.9 | len: 250 | use: O | rpt: *)
        :param organization_unit_type: Coded Element (id: ROL.10 | len: 250 | use: O | rpt: 1)
        :param office_or_home_address_or_birthplace: Extended Address (id: ROL.11 | len: 250 | use: O | rpt: *)
        :param phone: Extended Telecommunication Number (id: ROL.12 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.role_instance_id = role_instance_id
        self.action_code = action_code
        self.role_rol = role_rol
        self.role_person = role_person
        self.role_begin_date_or_time = role_begin_date_or_time
        self.role_end_date_or_time = role_end_date_or_time
        self.role_duration = role_duration
        self.role_action_reason = role_action_reason
        self.provider_type = provider_type
        self.organization_unit_type = organization_unit_type
        self.office_or_home_address_or_birthplace = office_or_home_address_or_birthplace
        self.phone = phone

    @property  # get ROL.1
    def role_instance_id(self) -> EI | None:
        """
        id: ROL.1 | len: 60 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.1
        """
        return self._c_data[0][0]

    @role_instance_id.setter  # set ROL.1
    def role_instance_id(self, ei: EI | None):
        """
        id: ROL.1 | len: 60 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.1
        """
        self._c_data[0] = (ei,)

    @property  # get ROL.2
    def action_code(self) -> ProblemOrGoalActionCode:
        """
        id: ROL.2 | len: 2 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.2
        """
        return self._c_data[1][0]

    @action_code.setter  # set ROL.2
    def action_code(self, problem_or_goal_action_code: ProblemOrGoalActionCode):
        """
        id: ROL.2 | len: 2 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.2
        """
        self._c_data[1] = (problem_or_goal_action_code,)

    @property  # get ROL.3
    def role_rol(self) -> ProviderRole:
        """
        id: ROL.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.3
        """
        return self._c_data[2][0]

    @role_rol.setter  # set ROL.3
    def role_rol(self, provider_role: ProviderRole):
        """
        id: ROL.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.3
        """
        self._c_data[2] = (provider_role,)

    @property
    def role_person(self) -> tuple[XCN, ...]:
        """
        id: ROL.4 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.4
        """
        return self._c_data[3]

    @role_person.setter  # set ROL.4
    def role_person(self, xcn: XCN | tuple[XCN]):
        """
        id: ROL.4 | len: 250 | use: R | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.4
        """
        if isinstance(xcn, tuple):
            self._c_data[3] = xcn
        else:
            self._c_data[3] = (xcn,)

    @property  # get ROL.5
    def role_begin_date_or_time(self) -> TS | None:
        """
        id: ROL.5 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.5
        """
        return self._c_data[4][0]

    @role_begin_date_or_time.setter  # set ROL.5
    def role_begin_date_or_time(self, ts: TS | None):
        """
        id: ROL.5 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.5
        """
        self._c_data[4] = (ts,)

    @property  # get ROL.6
    def role_end_date_or_time(self) -> TS | None:
        """
        id: ROL.6 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.6
        """
        return self._c_data[5][0]

    @role_end_date_or_time.setter  # set ROL.6
    def role_end_date_or_time(self, ts: TS | None):
        """
        id: ROL.6 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.6
        """
        self._c_data[5] = (ts,)

    @property  # get ROL.7
    def role_duration(self) -> CE | None:
        """
        id: ROL.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.7
        """
        return self._c_data[6][0]

    @role_duration.setter  # set ROL.7
    def role_duration(self, ce: CE | None):
        """
        id: ROL.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.7
        """
        self._c_data[6] = (ce,)

    @property  # get ROL.8
    def role_action_reason(self) -> CE | None:
        """
        id: ROL.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.8
        """
        return self._c_data[7][0]

    @role_action_reason.setter  # set ROL.8
    def role_action_reason(self, ce: CE | None):
        """
        id: ROL.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.8
        """
        self._c_data[7] = (ce,)

    @property
    def provider_type(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: ROL.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.9
        """
        return self._c_data[8]

    @provider_type.setter  # set ROL.9
    def provider_type(self, ce: CE | tuple[CE] | None):
        """
        id: ROL.9 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.9
        """
        if isinstance(ce, tuple):
            self._c_data[8] = ce
        else:
            self._c_data[8] = (ce,)

    @property  # get ROL.10
    def organization_unit_type(self) -> OrganizationUnitType | None:
        """
        id: ROL.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.10
        """
        return self._c_data[9][0]

    @organization_unit_type.setter  # set ROL.10
    def organization_unit_type(
        self, organization_unit_type: OrganizationUnitType | None
    ):
        """
        id: ROL.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.10
        """
        self._c_data[9] = (organization_unit_type,)

    @property
    def office_or_home_address_or_birthplace(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: ROL.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.11
        """
        return self._c_data[10]

    @office_or_home_address_or_birthplace.setter  # set ROL.11
    def office_or_home_address_or_birthplace(self, xad: XAD | tuple[XAD] | None):
        """
        id: ROL.11 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.11
        """
        if isinstance(xad, tuple):
            self._c_data[10] = xad
        else:
            self._c_data[10] = (xad,)

    @property
    def phone(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: ROL.12 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.12
        """
        return self._c_data[11]

    @phone.setter  # set ROL.12
    def phone(self, xtn: XTN | tuple[XTN] | None):
        """
        id: ROL.12 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ROL.12
        """
        if isinstance(xtn, tuple):
            self._c_data[11] = xtn
        else:
            self._c_data[11] = (xtn,)
