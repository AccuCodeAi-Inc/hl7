from __future__ import annotations
from ...base import HL7Segment
from ..data_types.XAD import XAD
from ..data_types.PLN import PLN
from ..data_types.CE import CE
from ..data_types.XPN import XPN
from ..data_types.XTN import XTN
from ..data_types.PL import PL
from ..tables.PreferredMethodOfContact import PreferredMethodOfContact
from ..tables.ContactRole import ContactRole


"""
Contact Data - CTD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CTD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CTD,
    XAD, PLN, CE, XPN, XTN, PL
)

ctd = CTD(  #  - The CTD segment may identify any contact personnel associated with a patient referral message and its related transactions
    contact_role=ce,  # CE(...)  # Required.
    contact_name=None,  # XPN(...) 
    contact_address=None,  # XAD(...) 
    contact_location=None,  # PL(...) 
    contact_communication_information=None,  # XTN(...) 
    preferred_method_of_contact=None,  # CE(...) 
    contact_identifiers=None,  # PLN(...) 
)

-----END SEGMENT::CTD TEMPLATE-----
"""


class CTD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CTD"""
    _hl7_name = """Contact Data"""
    _hl7_description = """The CTD segment may identify any contact personnel associated with a patient referral message and its related transactions"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD"
    _c_length = (250, 250, 250, 60, 250, 250, 100,)
    _c_rpt = (65535, 65535, 65535, 1, 65535, 1, 65535,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, XPN, XAD, PL, XTN, CE, PLN,)
    _c_aliases = ("CTD.1", "CTD.2", "CTD.3", "CTD.4", "CTD.5", "CTD.6", "CTD.7",)
    _c_names = ("Contact Role", "Contact Name", "Contact Address", "Contact Location", "Contact Communication Information", "Preferred Method of Contact", "Contact Identifiers",)
    _c_attrs = ("contact_role", "contact_name", "contact_address", "contact_location", "contact_communication_information", "preferred_method_of_contact", "contact_identifiers",)
    # fmt: on

    def __init__(
        self,
        contact_role: ContactRole | CE,  # CTD.1
        contact_name: XPN | None = None,  # CTD.2
        contact_address: XAD | None = None,  # CTD.3
        contact_location: PL | None = None,  # CTD.4
        contact_communication_information: XTN | None = None,  # CTD.5
        preferred_method_of_contact: PreferredMethodOfContact
        | CE
        | None = None,  # CTD.6
        contact_identifiers: PLN | None = None,  # CTD.7
    ):
        """
        Contact Data - `CTD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD>`_
        The CTD segment may identify any contact personnel associated with a patient referral message and its related transactions. The CTD segment will be paired with a PRD segment. The PRD segment contains data specifically focused on provider information in a referral. While it is important in an inter-enterprise transaction to transmit specific information regarding the providers involved (referring and referred-to), it may also be important to identify the contact personnel associated with the given provider. For example, a provider receiving a referral may need to know the office manager or the billing person at the institution of the provider who sent the referral. This segment allows for multiple contact personnel to be associated with a single provider.

        :param contact_role: Coded Element (id: CTD.1 | len: 250 | use: R | rpt: *)
        :param contact_name: Extended Person Name (id: CTD.2 | len: 250 | use: O | rpt: *)
        :param contact_address: Extended Address (id: CTD.3 | len: 250 | use: O | rpt: *)
        :param contact_location: Person Location (id: CTD.4 | len: 60 | use: O | rpt: 1)
        :param contact_communication_information: Extended Telecommunication Number (id: CTD.5 | len: 250 | use: O | rpt: *)
        :param preferred_method_of_contact: Coded Element (id: CTD.6 | len: 250 | use: O | rpt: 1)
        :param contact_identifiers: Practitioner License or Other ID Number (id: CTD.7 | len: 100 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.contact_role = contact_role
        self.contact_name = contact_name
        self.contact_address = contact_address
        self.contact_location = contact_location
        self.contact_communication_information = contact_communication_information
        self.preferred_method_of_contact = preferred_method_of_contact
        self.contact_identifiers = contact_identifiers

    @property
    def contact_role(self) -> tuple[ContactRole, ...]:
        """
        id: CTD.1 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.1
        """
        return self._c_data[0]

    @contact_role.setter  # set CTD.1
    def contact_role(self, contact_role: ContactRole | tuple[ContactRole]):
        """
        id: CTD.1 | len: 250 | use: R | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.1
        """
        if isinstance(contact_role, tuple):
            self._c_data[0] = contact_role
        else:
            self._c_data[0] = (contact_role,)

    @property
    def contact_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: CTD.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.2
        """
        return self._c_data[1]

    @contact_name.setter  # set CTD.2
    def contact_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: CTD.2 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.2
        """
        if isinstance(xpn, tuple):
            self._c_data[1] = xpn
        else:
            self._c_data[1] = (xpn,)

    @property
    def contact_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: CTD.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.3
        """
        return self._c_data[2]

    @contact_address.setter  # set CTD.3
    def contact_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: CTD.3 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.3
        """
        if isinstance(xad, tuple):
            self._c_data[2] = xad
        else:
            self._c_data[2] = (xad,)

    @property  # get CTD.4
    def contact_location(self) -> PL | None:
        """
        id: CTD.4 | len: 60 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.4
        """
        return self._c_data[3][0]

    @contact_location.setter  # set CTD.4
    def contact_location(self, pl: PL | None):
        """
        id: CTD.4 | len: 60 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.4
        """
        self._c_data[3] = (pl,)

    @property
    def contact_communication_information(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: CTD.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.5
        """
        return self._c_data[4]

    @contact_communication_information.setter  # set CTD.5
    def contact_communication_information(self, xtn: XTN | tuple[XTN] | None):
        """
        id: CTD.5 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.5
        """
        if isinstance(xtn, tuple):
            self._c_data[4] = xtn
        else:
            self._c_data[4] = (xtn,)

    @property  # get CTD.6
    def preferred_method_of_contact(self) -> PreferredMethodOfContact | None:
        """
        id: CTD.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.6
        """
        return self._c_data[5][0]

    @preferred_method_of_contact.setter  # set CTD.6
    def preferred_method_of_contact(
        self, preferred_method_of_contact: PreferredMethodOfContact | None
    ):
        """
        id: CTD.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.6
        """
        self._c_data[5] = (preferred_method_of_contact,)

    @property
    def contact_identifiers(self) -> tuple[PLN, ...] | tuple[None]:
        """
        id: CTD.7 | len: 100 | use: O | rpt: *
        ---
        return_type: tuple[PLN, ...]: (Practitioner License or Other ID Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.7
        """
        return self._c_data[6]

    @contact_identifiers.setter  # set CTD.7
    def contact_identifiers(self, pln: PLN | tuple[PLN] | None):
        """
        id: CTD.7 | len: 100 | use: O | rpt: *
        ---
        param_type: PLN | tuple[PLN, ...]: (Practitioner License or Other ID Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CTD.7
        """
        if isinstance(pln, tuple):
            self._c_data[6] = pln
        else:
            self._c_data[6] = (pln,)
