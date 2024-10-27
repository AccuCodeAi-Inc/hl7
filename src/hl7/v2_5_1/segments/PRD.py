from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.XAD import XAD
from ..data_types.PLN import PLN
from ..data_types.CE import CE
from ..data_types.XPN import XPN
from ..data_types.XTN import XTN
from ..data_types.PL import PL
from ..tables.PreferredMethodOfContact import PreferredMethodOfContact
from ..tables.ProviderRole import ProviderRole


"""
Provider Data - PRD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PRD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PRD,
    TS, XAD, PLN, CE, XPN, XTN, PL
)

prd = PRD(  #  - This segment will be employed as part of a patient referral message and its related transactions
    provider_role=ce,  # CE(...)  # Required.
    provider_name=None,  # XPN(...) 
    provider_address=None,  # XAD(...) 
    provider_location=None,  # PL(...) 
    provider_communication_information=None,  # XTN(...) 
    preferred_method_of_contact=None,  # CE(...) 
    provider_identifiers=None,  # PLN(...) 
    effective_start_date_of_provider_role=None,  # TS(...) 
    effective_end_date_of_provider_role=None,  # TS(...) 
)

-----END SEGMENT::PRD TEMPLATE-----
"""


class PRD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PRD"""
    _hl7_name = """Provider Data"""
    _hl7_description = """This segment will be employed as part of a patient referral message and its related transactions"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRD"
    _c_length = (250, 250, 250, 60, 250, 250, 100, 26, 26,)
    _c_rpt = (65535, 65535, 65535, 1, 65535, 1, 65535, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, XPN, XAD, PL, XTN, CE, PLN, TS, TS,)
    _c_aliases = ("PRD.1", "PRD.2", "PRD.3", "PRD.4", "PRD.5", "PRD.6", "PRD.7", "PRD.8", "PRD.9",)
    _c_names = ("Provider Role", "Provider Name", "Provider Address", "Provider Location", "Provider Communication Information", "Preferred Method of Contact", "Provider Identifiers", "Effective Start Date of Provider Role", "Effective End Date of Provider Role",)
    _c_attrs = ("provider_role", "provider_name", "provider_address", "provider_location", "provider_communication_information", "preferred_method_of_contact", "provider_identifiers", "effective_start_date_of_provider_role", "effective_end_date_of_provider_role",)
    # fmt: on

    def __init__(
        self,
        provider_role: ProviderRole | CE,  # PRD.1
        provider_name: XPN | None = None,  # PRD.2
        provider_address: XAD | None = None,  # PRD.3
        provider_location: PL | None = None,  # PRD.4
        provider_communication_information: XTN | None = None,  # PRD.5
        preferred_method_of_contact: PreferredMethodOfContact
        | CE
        | None = None,  # PRD.6
        provider_identifiers: PLN | None = None,  # PRD.7
        effective_start_date_of_provider_role: TS | None = None,  # PRD.8
        effective_end_date_of_provider_role: TS | None = None,  # PRD.9
    ):
        """
        Provider Data - `PRD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRD>`_
        This segment will be employed as part of a patient referral message and its related transactions. The PRD segment contains data specifically focused on a referral, and it is inter-enterprise in nature. The justification for this new segment comes from the fact that we are dealing with referrals that are external to the facilities that received them. Therefore, using a segment such as the current PV1 would be inadequate for all the return information that may be required by the receiving facility or application. In addition, the PV1 does not always provide information sufficient to enable the external facility to make a complete identification of the referring entity. The information contained in the PRD segment will include the referring provider, the referred-to provider, the referred-to location or service, and the referring provider clinic address.

        :param provider_role: Coded Element (id: PRD.1 | len: 250 | use: R | rpt: *)
        :param provider_name: Extended Person Name (id: PRD.2 | len: 250 | use: O | rpt: *)
        :param provider_address: Extended Address (id: PRD.3 | len: 250 | use: O | rpt: *)
        :param provider_location: Person Location (id: PRD.4 | len: 60 | use: O | rpt: 1)
        :param provider_communication_information: Extended Telecommunication Number (id: PRD.5 | len: 250 | use: O | rpt: *)
        :param preferred_method_of_contact: Coded Element (id: PRD.6 | len: 250 | use: O | rpt: 1)
        :param provider_identifiers: Practitioner License or Other ID Number (id: PRD.7 | len: 100 | use: O | rpt: *)
        :param effective_start_date_of_provider_role: Time Stamp (id: PRD.8 | len: 26 | use: O | rpt: 1)
        :param effective_end_date_of_provider_role: Time Stamp (id: PRD.9 | len: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.provider_role = provider_role
        self.provider_name = provider_name
        self.provider_address = provider_address
        self.provider_location = provider_location
        self.provider_communication_information = provider_communication_information
        self.preferred_method_of_contact = preferred_method_of_contact
        self.provider_identifiers = provider_identifiers
        self.effective_start_date_of_provider_role = (
            effective_start_date_of_provider_role
        )
        self.effective_end_date_of_provider_role = effective_end_date_of_provider_role

    @property
    def provider_role(self) -> tuple[ProviderRole, ...]:
        """
        id: PRD.1 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.1
        """
        return self._c_data[0]

    @provider_role.setter  # set PRD.1
    def provider_role(self, provider_role: ProviderRole | tuple[ProviderRole]):
        """
        id: PRD.1 | len: 250 | use: R | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.1
        """
        if isinstance(provider_role, tuple):
            self._c_data[0] = provider_role
        else:
            self._c_data[0] = (provider_role,)

    @property
    def provider_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: PRD.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.2
        """
        return self._c_data[1]

    @provider_name.setter  # set PRD.2
    def provider_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: PRD.2 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.2
        """
        if isinstance(xpn, tuple):
            self._c_data[1] = xpn
        else:
            self._c_data[1] = (xpn,)

    @property
    def provider_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: PRD.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.3
        """
        return self._c_data[2]

    @provider_address.setter  # set PRD.3
    def provider_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: PRD.3 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.3
        """
        if isinstance(xad, tuple):
            self._c_data[2] = xad
        else:
            self._c_data[2] = (xad,)

    @property  # get PRD.4
    def provider_location(self) -> PL | None:
        """
        id: PRD.4 | len: 60 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.4
        """
        return self._c_data[3][0]

    @provider_location.setter  # set PRD.4
    def provider_location(self, pl: PL | None):
        """
        id: PRD.4 | len: 60 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.4
        """
        self._c_data[3] = (pl,)

    @property
    def provider_communication_information(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: PRD.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.5
        """
        return self._c_data[4]

    @provider_communication_information.setter  # set PRD.5
    def provider_communication_information(self, xtn: XTN | tuple[XTN] | None):
        """
        id: PRD.5 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.5
        """
        if isinstance(xtn, tuple):
            self._c_data[4] = xtn
        else:
            self._c_data[4] = (xtn,)

    @property  # get PRD.6
    def preferred_method_of_contact(self) -> PreferredMethodOfContact | None:
        """
        id: PRD.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.6
        """
        return self._c_data[5][0]

    @preferred_method_of_contact.setter  # set PRD.6
    def preferred_method_of_contact(
        self, preferred_method_of_contact: PreferredMethodOfContact | None
    ):
        """
        id: PRD.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.6
        """
        self._c_data[5] = (preferred_method_of_contact,)

    @property
    def provider_identifiers(self) -> tuple[PLN, ...] | tuple[None]:
        """
        id: PRD.7 | len: 100 | use: O | rpt: *
        ---
        return_type: tuple[PLN, ...]: (Practitioner License or Other ID Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.7
        """
        return self._c_data[6]

    @provider_identifiers.setter  # set PRD.7
    def provider_identifiers(self, pln: PLN | tuple[PLN] | None):
        """
        id: PRD.7 | len: 100 | use: O | rpt: *
        ---
        param_type: PLN | tuple[PLN, ...]: (Practitioner License or Other ID Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.7
        """
        if isinstance(pln, tuple):
            self._c_data[6] = pln
        else:
            self._c_data[6] = (pln,)

    @property  # get PRD.8
    def effective_start_date_of_provider_role(self) -> TS | None:
        """
        id: PRD.8 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.8
        """
        return self._c_data[7][0]

    @effective_start_date_of_provider_role.setter  # set PRD.8
    def effective_start_date_of_provider_role(self, ts: TS | None):
        """
        id: PRD.8 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.8
        """
        self._c_data[7] = (ts,)

    @property  # get PRD.9
    def effective_end_date_of_provider_role(self) -> TS | None:
        """
        id: PRD.9 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.9
        """
        return self._c_data[8][0]

    @effective_end_date_of_provider_role.setter  # set PRD.9
    def effective_end_date_of_provider_role(self, ts: TS | None):
        """
        id: PRD.9 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRD.9
        """
        self._c_data[8] = (ts,)
