from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.XCN import XCN
from ..data_types.XTN import XTN
from ..data_types.XAD import XAD
from ..data_types.EI import EI
from ..data_types.ST import ST
from ..tables.FacilityType import FacilityType


"""
Facility - FAC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::FAC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    FAC,
    ID, XCN, XTN, XAD, EI, ST
)

fac = FAC(  #  - 
    facility_id_fac=ei,  # EI(...)  # Required.
    facility_type=None,  # ID(...) 
    facility_address=xad,  # XAD(...)  # Required.
    facility_telecommunication=xtn,  # XTN(...)  # Required.
    contact_person=None,  # XCN(...) 
    contact_title=None,  # ST(...) 
    contact_address=None,  # XAD(...) 
    contact_telecommunication=None,  # XTN(...) 
    signature_authority=xcn,  # XCN(...)  # Required.
    signature_authority_title=None,  # ST(...) 
    signature_authority_address=None,  # XAD(...) 
    signature_authority_telecommunication=None,  # XTN(...) 
)

-----END SEGMENT::FAC TEMPLATE-----
"""


class FAC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """FAC"""
    _hl7_name = """Facility"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FAC"
    _c_length = (20, 1, 250, 250, 250, 60, 250, 250, 250, 60, 250, 250,)
    _c_rpt = (1, 1, 65535, 1, 65535, 65535, 65535, 65535, 65535, 1, 65535, 1,)
    _c_usage = ("R", "O", "R", "R", "O", "O", "O", "O", "R", "O", "O", "O",)
    _c_components = (EI, ID, XAD, XTN, XCN, ST, XAD, XTN, XCN, ST, XAD, XTN,)
    _c_aliases = ("FAC.1", "FAC.2", "FAC.3", "FAC.4", "FAC.5", "FAC.6", "FAC.7", "FAC.8", "FAC.9", "FAC.10", "FAC.11", "FAC.12",)
    _c_names = ("Facility ID-FAC", "Facility Type", "Facility Address", "Facility Telecommunication", "Contact Person", "Contact Title", "Contact Address", "Contact Telecommunication", "Signature Authority", "Signature Authority Title", "Signature Authority Address", "Signature Authority Telecommunication",)
    _c_attrs = ("facility_id_fac", "facility_type", "facility_address", "facility_telecommunication", "contact_person", "contact_title", "contact_address", "contact_telecommunication", "signature_authority", "signature_authority_title", "signature_authority_address", "signature_authority_telecommunication",)
    # fmt: on

    def __init__(
        self,
        facility_id_fac: EI | tuple[EI],  # FAC.1
        facility_address: XAD | tuple[XAD],  # FAC.3
        facility_telecommunication: XTN | tuple[XTN],  # FAC.4
        signature_authority: XCN | tuple[XCN],  # FAC.9
        facility_type: FacilityType
        | ID
        | tuple[FacilityType | ID]
        | None = None,  # FAC.2
        contact_person: XCN | tuple[XCN] | None = None,  # FAC.5
        contact_title: ST | tuple[ST] | None = None,  # FAC.6
        contact_address: XAD | tuple[XAD] | None = None,  # FAC.7
        contact_telecommunication: XTN | tuple[XTN] | None = None,  # FAC.8
        signature_authority_title: ST | tuple[ST] | None = None,  # FAC.10
        signature_authority_address: XAD | tuple[XAD] | None = None,  # FAC.11
        signature_authority_telecommunication: XTN | tuple[XTN] | None = None,  # FAC.12
    ):
        """
        Facility - `FAC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FAC>`_


        :param facility_id_fac: Entity Identifier (id: FAC.1 | len: 20 | use: R | rpt: 1)
        :param facility_type: Coded values for HL7 tables (id: FAC.2 | len: 1 | use: O | rpt: 1)
        :param facility_address: Extended Address (id: FAC.3 | len: 250 | use: R | rpt: *)
        :param facility_telecommunication: Extended Telecommunication Number (id: FAC.4 | len: 250 | use: R | rpt: 1)
        :param contact_person: Extended Composite ID Number and Name for Persons (id: FAC.5 | len: 250 | use: O | rpt: *)
        :param contact_title: String Data (id: FAC.6 | len: 60 | use: O | rpt: *)
        :param contact_address: Extended Address (id: FAC.7 | len: 250 | use: O | rpt: *)
        :param contact_telecommunication: Extended Telecommunication Number (id: FAC.8 | len: 250 | use: O | rpt: *)
        :param signature_authority: Extended Composite ID Number and Name for Persons (id: FAC.9 | len: 250 | use: R | rpt: *)
        :param signature_authority_title: String Data (id: FAC.10 | len: 60 | use: O | rpt: 1)
        :param signature_authority_address: Extended Address (id: FAC.11 | len: 250 | use: O | rpt: *)
        :param signature_authority_telecommunication: Extended Telecommunication Number (id: FAC.12 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.facility_id_fac = facility_id_fac
        self.facility_type = facility_type
        self.facility_address = facility_address
        self.facility_telecommunication = facility_telecommunication
        self.contact_person = contact_person
        self.contact_title = contact_title
        self.contact_address = contact_address
        self.contact_telecommunication = contact_telecommunication
        self.signature_authority = signature_authority
        self.signature_authority_title = signature_authority_title
        self.signature_authority_address = signature_authority_address
        self.signature_authority_telecommunication = (
            signature_authority_telecommunication
        )

    @property  # get FAC.1
    def facility_id_fac(self) -> EI:
        """
        id: FAC.1 | len: 20 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.1
        """
        return self._c_data[0][0]

    @facility_id_fac.setter  # set FAC.1
    def facility_id_fac(self, ei: EI):
        """
        id: FAC.1 | len: 20 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.1
        """
        self._c_data[0] = (ei,)

    @property  # get FAC.2
    def facility_type(self) -> FacilityType | None:
        """
        id: FAC.2 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.2
        """
        return self._c_data[1][0]

    @facility_type.setter  # set FAC.2
    def facility_type(self, facility_type: FacilityType | None):
        """
        id: FAC.2 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.2
        """
        self._c_data[1] = (facility_type,)

    @property
    def facility_address(self) -> tuple[XAD, ...]:
        """
        id: FAC.3 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.3
        """
        return self._c_data[2]

    @facility_address.setter  # set FAC.3
    def facility_address(self, xad: XAD | tuple[XAD]):
        """
        id: FAC.3 | len: 250 | use: R | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.3
        """
        if isinstance(xad, tuple):
            self._c_data[2] = xad
        else:
            self._c_data[2] = (xad,)

    @property  # get FAC.4
    def facility_telecommunication(self) -> XTN:
        """
        id: FAC.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.4
        """
        return self._c_data[3][0]

    @facility_telecommunication.setter  # set FAC.4
    def facility_telecommunication(self, xtn: XTN):
        """
        id: FAC.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.4
        """
        self._c_data[3] = (xtn,)

    @property
    def contact_person(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: FAC.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.5
        """
        return self._c_data[4]

    @contact_person.setter  # set FAC.5
    def contact_person(self, xcn: XCN | tuple[XCN] | None):
        """
        id: FAC.5 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.5
        """
        if isinstance(xcn, tuple):
            self._c_data[4] = xcn
        else:
            self._c_data[4] = (xcn,)

    @property
    def contact_title(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: FAC.6 | len: 60 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.6
        """
        return self._c_data[5]

    @contact_title.setter  # set FAC.6
    def contact_title(self, st: ST | tuple[ST] | None):
        """
        id: FAC.6 | len: 60 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.6
        """
        if isinstance(st, tuple):
            self._c_data[5] = st
        else:
            self._c_data[5] = (st,)

    @property
    def contact_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: FAC.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.7
        """
        return self._c_data[6]

    @contact_address.setter  # set FAC.7
    def contact_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: FAC.7 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.7
        """
        if isinstance(xad, tuple):
            self._c_data[6] = xad
        else:
            self._c_data[6] = (xad,)

    @property
    def contact_telecommunication(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: FAC.8 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.8
        """
        return self._c_data[7]

    @contact_telecommunication.setter  # set FAC.8
    def contact_telecommunication(self, xtn: XTN | tuple[XTN] | None):
        """
        id: FAC.8 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.8
        """
        if isinstance(xtn, tuple):
            self._c_data[7] = xtn
        else:
            self._c_data[7] = (xtn,)

    @property
    def signature_authority(self) -> tuple[XCN, ...]:
        """
        id: FAC.9 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.9
        """
        return self._c_data[8]

    @signature_authority.setter  # set FAC.9
    def signature_authority(self, xcn: XCN | tuple[XCN]):
        """
        id: FAC.9 | len: 250 | use: R | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.9
        """
        if isinstance(xcn, tuple):
            self._c_data[8] = xcn
        else:
            self._c_data[8] = (xcn,)

    @property  # get FAC.10
    def signature_authority_title(self) -> ST | None:
        """
        id: FAC.10 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.10
        """
        return self._c_data[9][0]

    @signature_authority_title.setter  # set FAC.10
    def signature_authority_title(self, st: ST | None):
        """
        id: FAC.10 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.10
        """
        self._c_data[9] = (st,)

    @property
    def signature_authority_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: FAC.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.11
        """
        return self._c_data[10]

    @signature_authority_address.setter  # set FAC.11
    def signature_authority_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: FAC.11 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.11
        """
        if isinstance(xad, tuple):
            self._c_data[10] = xad
        else:
            self._c_data[10] = (xad,)

    @property  # get FAC.12
    def signature_authority_telecommunication(self) -> XTN | None:
        """
        id: FAC.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.12
        """
        return self._c_data[11][0]

    @signature_authority_telecommunication.setter  # set FAC.12
    def signature_authority_telecommunication(self, xtn: XTN | None):
        """
        id: FAC.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FAC.12
        """
        self._c_data[11] = (xtn,)
