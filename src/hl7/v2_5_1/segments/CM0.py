from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.DT import DT
from ..data_types.XCN import XCN
from ..data_types.NM import NM
from ..data_types.XTN import XTN
from ..data_types.XAD import XAD
from ..data_types.ST import ST
from ..data_types.EI import EI


"""
Clinical Study Master - CM0
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CM0 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CM0,
    SI, DT, XCN, NM, XTN, XAD, ST, EI
)

cm0 = CM0(  #  - The Clinical Study Master (CM0) segment contains the information about the study itself
    set_id_cm0=None,  # SI(...) 
    sponsor_study_id=ei,  # EI(...)  # Required.
    alternate_study_id=None,  # EI(...) 
    title_of_study=st,  # ST(...)  # Required.
    chairman_of_study=None,  # XCN(...) 
    last_irb_approval_date=None,  # DT(...) 
    total_accrual_to_date=None,  # NM(...) 
    last_accrual_date=None,  # DT(...) 
    contact_for_study=None,  # XCN(...) 
    contacts_telephone_number=None,  # XTN(...) 
    contacts_address=None,  # XAD(...) 
)

-----END SEGMENT::CM0 TEMPLATE-----
"""


class CM0(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CM0"""
    _hl7_name = """Clinical Study Master"""
    _hl7_description = """The Clinical Study Master (CM0) segment contains the information about the study itself"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM0"
    _c_length = (4, 60, 60, 300, 250, 8, 8, 8, 250, 250, 250,)
    _c_rpt = (1, 1, 3, 1, 65535, 1, 1, 1, 65535, 1, 65535,)
    _c_usage = ("O", "R", "O", "R", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, EI, EI, ST, XCN, DT, NM, DT, XCN, XTN, XAD,)
    _c_aliases = ("CM0.1", "CM0.2", "CM0.3", "CM0.4", "CM0.5", "CM0.6", "CM0.7", "CM0.8", "CM0.9", "CM0.10", "CM0.11",)
    _c_names = ("Set ID - CM0", "Sponsor Study ID", "Alternate Study ID", "Title of Study", "Chairman of Study", "Last IRB Approval Date", "Total Accrual to Date", "Last Accrual Date", "Contact for Study", "Contact's Telephone Number", "Contact's Address",)
    _c_attrs = ("set_id_cm0", "sponsor_study_id", "alternate_study_id", "title_of_study", "chairman_of_study", "last_irb_approval_date", "total_accrual_to_date", "last_accrual_date", "contact_for_study", "contacts_telephone_number", "contacts_address",)
    # fmt: on

    def __init__(
        self,
        sponsor_study_id: EI | tuple[EI, ...],  # CM0.2
        title_of_study: ST | tuple[ST, ...],  # CM0.4
        set_id_cm0: SI | tuple[SI, ...] | None = None,  # CM0.1
        alternate_study_id: EI | tuple[EI, ...] | None = None,  # CM0.3
        chairman_of_study: XCN | tuple[XCN, ...] | None = None,  # CM0.5
        last_irb_approval_date: DT | tuple[DT, ...] | None = None,  # CM0.6
        total_accrual_to_date: NM | tuple[NM, ...] | None = None,  # CM0.7
        last_accrual_date: DT | tuple[DT, ...] | None = None,  # CM0.8
        contact_for_study: XCN | tuple[XCN, ...] | None = None,  # CM0.9
        contacts_telephone_number: XTN | tuple[XTN, ...] | None = None,  # CM0.10
        contacts_address: XAD | tuple[XAD, ...] | None = None,  # CM0.11
    ):
        """
        Clinical Study Master - `CM0 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM0>`_
        The Clinical Study Master (CM0) segment contains the information about the study itself.  The sending application study number for each patient is sent in the CSR segment.  The optional CM0 enables information about the study at the sending application that may be useful to the receiving systems.  All of the fields in the segment describe the study status at the sending facility unless otherwise agreed upon.

        :param set_id_cm0: Sequence ID (id: CM0.1 | len: 4 | use: O | rpt: 1)
        :param sponsor_study_id: Entity Identifier (id: CM0.2 | len: 60 | use: R | rpt: 1)
        :param alternate_study_id: Entity Identifier (id: CM0.3 | len: 60 | use: O | rpt: 3)
        :param title_of_study: String Data (id: CM0.4 | len: 300 | use: R | rpt: 1)
        :param chairman_of_study: Extended Composite ID Number and Name for Persons (id: CM0.5 | len: 250 | use: O | rpt: *)
        :param last_irb_approval_date: Date (id: CM0.6 | len: 8 | use: O | rpt: 1)
        :param total_accrual_to_date: Numeric (id: CM0.7 | len: 8 | use: O | rpt: 1)
        :param last_accrual_date: Date (id: CM0.8 | len: 8 | use: O | rpt: 1)
        :param contact_for_study: Extended Composite ID Number and Name for Persons (id: CM0.9 | len: 250 | use: O | rpt: *)
        :param contacts_telephone_number: Extended Telecommunication Number (id: CM0.10 | len: 250 | use: O | rpt: 1)
        :param contacts_address: Extended Address (id: CM0.11 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 11
        self.set_id_cm0 = set_id_cm0
        self.sponsor_study_id = sponsor_study_id
        self.alternate_study_id = alternate_study_id
        self.title_of_study = title_of_study
        self.chairman_of_study = chairman_of_study
        self.last_irb_approval_date = last_irb_approval_date
        self.total_accrual_to_date = total_accrual_to_date
        self.last_accrual_date = last_accrual_date
        self.contact_for_study = contact_for_study
        self.contacts_telephone_number = contacts_telephone_number
        self.contacts_address = contacts_address

    @property  # get CM0.1
    def set_id_cm0(self) -> SI | None:
        """
        id: CM0.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.1
        """
        return self._c_data[0][0]

    @set_id_cm0.setter  # set CM0.1
    def set_id_cm0(self, si: SI | None):
        """
        id: CM0.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.1
        """
        self._c_data[0] = (si,)

    @property  # get CM0.2
    def sponsor_study_id(self) -> EI:
        """
        id: CM0.2 | len: 60 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.2
        """
        return self._c_data[1][0]

    @sponsor_study_id.setter  # set CM0.2
    def sponsor_study_id(self, ei: EI):
        """
        id: CM0.2 | len: 60 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.2
        """
        self._c_data[1] = (ei,)

    @property
    def alternate_study_id(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: CM0.3 | len: 60 | use: O | rpt: 3
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.3
        """
        return self._c_data[2]

    @alternate_study_id.setter  # set CM0.3
    def alternate_study_id(self, ei: EI | tuple[EI] | None):
        """
        id: CM0.3 | len: 60 | use: O | rpt: 3
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.3
        """
        if isinstance(ei, tuple):
            self._c_data[2] = ei
        else:
            self._c_data[2] = (ei,)

    @property  # get CM0.4
    def title_of_study(self) -> ST:
        """
        id: CM0.4 | len: 300 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.4
        """
        return self._c_data[3][0]

    @title_of_study.setter  # set CM0.4
    def title_of_study(self, st: ST):
        """
        id: CM0.4 | len: 300 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.4
        """
        self._c_data[3] = (st,)

    @property
    def chairman_of_study(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: CM0.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.5
        """
        return self._c_data[4]

    @chairman_of_study.setter  # set CM0.5
    def chairman_of_study(self, xcn: XCN | tuple[XCN] | None):
        """
        id: CM0.5 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.5
        """
        if isinstance(xcn, tuple):
            self._c_data[4] = xcn
        else:
            self._c_data[4] = (xcn,)

    @property  # get CM0.6
    def last_irb_approval_date(self) -> DT | None:
        """
        id: CM0.6 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.6
        """
        return self._c_data[5][0]

    @last_irb_approval_date.setter  # set CM0.6
    def last_irb_approval_date(self, dt: DT | None):
        """
        id: CM0.6 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.6
        """
        self._c_data[5] = (dt,)

    @property  # get CM0.7
    def total_accrual_to_date(self) -> NM | None:
        """
        id: CM0.7 | len: 8 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.7
        """
        return self._c_data[6][0]

    @total_accrual_to_date.setter  # set CM0.7
    def total_accrual_to_date(self, nm: NM | None):
        """
        id: CM0.7 | len: 8 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.7
        """
        self._c_data[6] = (nm,)

    @property  # get CM0.8
    def last_accrual_date(self) -> DT | None:
        """
        id: CM0.8 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.8
        """
        return self._c_data[7][0]

    @last_accrual_date.setter  # set CM0.8
    def last_accrual_date(self, dt: DT | None):
        """
        id: CM0.8 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.8
        """
        self._c_data[7] = (dt,)

    @property
    def contact_for_study(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: CM0.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.9
        """
        return self._c_data[8]

    @contact_for_study.setter  # set CM0.9
    def contact_for_study(self, xcn: XCN | tuple[XCN] | None):
        """
        id: CM0.9 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.9
        """
        if isinstance(xcn, tuple):
            self._c_data[8] = xcn
        else:
            self._c_data[8] = (xcn,)

    @property  # get CM0.10
    def contacts_telephone_number(self) -> XTN | None:
        """
        id: CM0.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.10
        """
        return self._c_data[9][0]

    @contacts_telephone_number.setter  # set CM0.10
    def contacts_telephone_number(self, xtn: XTN | None):
        """
        id: CM0.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.10
        """
        self._c_data[9] = (xtn,)

    @property
    def contacts_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: CM0.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.11
        """
        return self._c_data[10]

    @contacts_address.setter  # set CM0.11
    def contacts_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: CM0.11 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM0.11
        """
        if isinstance(xad, tuple):
            self._c_data[10] = xad
        else:
            self._c_data[10] = (xad,)
