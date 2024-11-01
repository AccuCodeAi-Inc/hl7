from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CX import CX
from ..data_types.XPN import XPN


"""
Merge Patient Information - MRG
HL7 Version: 2.5.1

-----BEGIN SEGMENT::MRG TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MRG,
    CX, XPN
)

mrg = MRG(  #  - The MRG segment provides receiving applications with information necessary to initiate the merging of patient data as well as groups of records
    prior_patient_identifier_list=cx,  # CX(...)  # Required.
    prior_alternate_patient_id=None,  # CX(...) 
    prior_patient_account_number=None,  # CX(...) 
    prior_patient_id=None,  # CX(...) 
    prior_visit_number=None,  # CX(...) 
    prior_alternate_visit_id=None,  # CX(...) 
    prior_patient_name=None,  # XPN(...) 
)

-----END SEGMENT::MRG TEMPLATE-----
"""


class MRG(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """MRG"""
    _hl7_name = """Merge Patient Information"""
    _hl7_description = """The MRG segment provides receiving applications with information necessary to initiate the merging of patient data as well as groups of records"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MRG"
    _c_length = (250, 250, 250, 250, 250, 250, 250,)
    _c_rpt = (65535, 65535, 1, 1, 1, 1, 65535,)
    _c_usage = ("R", "B", "O", "B", "O", "O", "O",)
    _c_components = (CX, CX, CX, CX, CX, CX, XPN,)
    _c_aliases = ("MRG.1", "MRG.2", "MRG.3", "MRG.4", "MRG.5", "MRG.6", "MRG.7",)
    _c_names = ("Prior Patient Identifier List", "Prior Alternate Patient ID", "Prior Patient Account Number", "Prior Patient ID", "Prior Visit Number", "Prior Alternate Visit ID", "Prior Patient Name",)
    _c_attrs = ("prior_patient_identifier_list", "prior_alternate_patient_id", "prior_patient_account_number", "prior_patient_id", "prior_visit_number", "prior_alternate_visit_id", "prior_patient_name",)
    # fmt: on

    def __init__(
        self,
        prior_patient_identifier_list: CX | tuple[CX],  # MRG.1
        prior_alternate_patient_id: CX | tuple[CX] | None = None,  # MRG.2
        prior_patient_account_number: CX | tuple[CX] | None = None,  # MRG.3
        prior_patient_id: CX | tuple[CX] | None = None,  # MRG.4
        prior_visit_number: CX | tuple[CX] | None = None,  # MRG.5
        prior_alternate_visit_id: CX | tuple[CX] | None = None,  # MRG.6
        prior_patient_name: XPN | tuple[XPN] | None = None,  # MRG.7
    ):
        """
        Merge Patient Information - `MRG <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MRG>`_
        The MRG segment provides receiving applications with information necessary to initiate the merging of patient data as well as groups of records. It is intended that this segment be used throughout the Standard to allow the merging of registration, accounting, and clinical records within specific applications.

        :param prior_patient_identifier_list: Extended Composite ID with Check Digit (id: MRG.1 | len: 250 | use: R | rpt: *)
        :param prior_alternate_patient_id: Extended Composite ID with Check Digit (id: MRG.2 | len: 250 | use: B | rpt: *)
        :param prior_patient_account_number: Extended Composite ID with Check Digit (id: MRG.3 | len: 250 | use: O | rpt: 1)
        :param prior_patient_id: Extended Composite ID with Check Digit (id: MRG.4 | len: 250 | use: B | rpt: 1)
        :param prior_visit_number: Extended Composite ID with Check Digit (id: MRG.5 | len: 250 | use: O | rpt: 1)
        :param prior_alternate_visit_id: Extended Composite ID with Check Digit (id: MRG.6 | len: 250 | use: O | rpt: 1)
        :param prior_patient_name: Extended Person Name (id: MRG.7 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.prior_patient_identifier_list = prior_patient_identifier_list
        self.prior_alternate_patient_id = prior_alternate_patient_id
        self.prior_patient_account_number = prior_patient_account_number
        self.prior_patient_id = prior_patient_id
        self.prior_visit_number = prior_visit_number
        self.prior_alternate_visit_id = prior_alternate_visit_id
        self.prior_patient_name = prior_patient_name

    @property
    def prior_patient_identifier_list(self) -> tuple[CX, ...]:
        """
        id: MRG.1 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.1
        """
        return self._c_data[0]

    @prior_patient_identifier_list.setter  # set MRG.1
    def prior_patient_identifier_list(self, cx: CX | tuple[CX]):
        """
        id: MRG.1 | len: 250 | use: R | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.1
        """
        if isinstance(cx, tuple):
            self._c_data[0] = cx
        else:
            self._c_data[0] = (cx,)

    @property
    def prior_alternate_patient_id(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: MRG.2 | len: 250 | use: B | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.2
        """
        return self._c_data[1]

    @prior_alternate_patient_id.setter  # set MRG.2
    def prior_alternate_patient_id(self, cx: CX | tuple[CX] | None):
        """
        id: MRG.2 | len: 250 | use: B | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.2
        """
        if isinstance(cx, tuple):
            self._c_data[1] = cx
        else:
            self._c_data[1] = (cx,)

    @property  # get MRG.3
    def prior_patient_account_number(self) -> CX | None:
        """
        id: MRG.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.3
        """
        return self._c_data[2][0]

    @prior_patient_account_number.setter  # set MRG.3
    def prior_patient_account_number(self, cx: CX | None):
        """
        id: MRG.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.3
        """
        self._c_data[2] = (cx,)

    @property  # get MRG.4
    def prior_patient_id(self) -> CX | None:
        """
        id: MRG.4 | len: 250 | use: B | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.4
        """
        return self._c_data[3][0]

    @prior_patient_id.setter  # set MRG.4
    def prior_patient_id(self, cx: CX | None):
        """
        id: MRG.4 | len: 250 | use: B | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.4
        """
        self._c_data[3] = (cx,)

    @property  # get MRG.5
    def prior_visit_number(self) -> CX | None:
        """
        id: MRG.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.5
        """
        return self._c_data[4][0]

    @prior_visit_number.setter  # set MRG.5
    def prior_visit_number(self, cx: CX | None):
        """
        id: MRG.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.5
        """
        self._c_data[4] = (cx,)

    @property  # get MRG.6
    def prior_alternate_visit_id(self) -> CX | None:
        """
        id: MRG.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.6
        """
        return self._c_data[5][0]

    @prior_alternate_visit_id.setter  # set MRG.6
    def prior_alternate_visit_id(self, cx: CX | None):
        """
        id: MRG.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.6
        """
        self._c_data[5] = (cx,)

    @property
    def prior_patient_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: MRG.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.7
        """
        return self._c_data[6]

    @prior_patient_name.setter  # set MRG.7
    def prior_patient_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: MRG.7 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MRG.7
        """
        if isinstance(xpn, tuple):
            self._c_data[6] = xpn
        else:
            self._c_data[6] = (xpn,)
