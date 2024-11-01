from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.NM import NM
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.CP import CP
from ..data_types.EI import EI
from ..tables.InsurancePlanId import InsurancePlanId
from ..tables.InsuranceCompanyIdCodes import InsuranceCompanyIdCodes


"""
Authorization Information - AUT
HL7 Version: 2.5.1

-----BEGIN SEGMENT::AUT TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    AUT,
    TS, NM, ST, CE, CP, EI
)

aut = AUT(  #  - This segment represents an authorization or a pre-authorization for a referred procedure or requested service by the payor covering the patients health care
    authorizing_payor_plan_id=None,  # CE(...) 
    authorizing_payor_company_id=ce,  # CE(...)  # Required.
    authorizing_payor_company_name=None,  # ST(...) 
    authorization_effective_date=None,  # TS(...) 
    authorization_expiration_date=None,  # TS(...) 
    authorization_identifier=None,  # EI(...) 
    reimbursement_limit=None,  # CP(...) 
    requested_number_of_treatments=None,  # NM(...) 
    authorized_number_of_treatments=None,  # NM(...) 
    process_date=None,  # TS(...) 
)

-----END SEGMENT::AUT TEMPLATE-----
"""


class AUT(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """AUT"""
    _hl7_name = """Authorization Information"""
    _hl7_description = """This segment represents an authorization or a pre-authorization for a referred procedure or requested service by the payor covering the patients health care"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AUT"
    _c_length = (250, 250, 45, 26, 26, 30, 25, 2, 2, 26,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "R", "O", "O", "O", "C", "O", "O", "O", "O",)
    _c_components = (CE, CE, ST, TS, TS, EI, CP, NM, NM, TS,)
    _c_aliases = ("AUT.1", "AUT.2", "AUT.3", "AUT.4", "AUT.5", "AUT.6", "AUT.7", "AUT.8", "AUT.9", "AUT.10",)
    _c_names = ("Authorizing Payor, Plan ID", "Authorizing Payor, Company ID", "Authorizing Payor, Company Name", "Authorization Effective Date", "Authorization Expiration Date", "Authorization Identifier", "Reimbursement Limit", "Requested Number of Treatments", "Authorized Number of Treatments", "Process Date",)
    _c_attrs = ("authorizing_payor_plan_id", "authorizing_payor_company_id", "authorizing_payor_company_name", "authorization_effective_date", "authorization_expiration_date", "authorization_identifier", "reimbursement_limit", "requested_number_of_treatments", "authorized_number_of_treatments", "process_date",)
    # fmt: on

    def __init__(
        self,
        authorizing_payor_company_id: InsuranceCompanyIdCodes
        | CE
        | tuple[InsuranceCompanyIdCodes | CE],  # AUT.2
        authorizing_payor_plan_id: InsurancePlanId
        | CE
        | tuple[InsurancePlanId | CE]
        | None = None,  # AUT.1
        authorizing_payor_company_name: ST | tuple[ST] | None = None,  # AUT.3
        authorization_effective_date: TS | tuple[TS] | None = None,  # AUT.4
        authorization_expiration_date: TS | tuple[TS] | None = None,  # AUT.5
        authorization_identifier: EI | tuple[EI] | None = None,  # AUT.6
        reimbursement_limit: CP | tuple[CP] | None = None,  # AUT.7
        requested_number_of_treatments: NM | tuple[NM] | None = None,  # AUT.8
        authorized_number_of_treatments: NM | tuple[NM] | None = None,  # AUT.9
        process_date: TS | tuple[TS] | None = None,  # AUT.10
    ):
        """
        Authorization Information - `AUT <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AUT>`_
        This segment represents an authorization or a pre-authorization for a referred procedure or requested service by the payor covering the patients health care.

        :param authorizing_payor_plan_id: Coded Element (id: AUT.1 | len: 250 | use: O | rpt: 1)
        :param authorizing_payor_company_id: Coded Element (id: AUT.2 | len: 250 | use: R | rpt: 1)
        :param authorizing_payor_company_name: String Data (id: AUT.3 | len: 45 | use: O | rpt: 1)
        :param authorization_effective_date: Time Stamp (id: AUT.4 | len: 26 | use: O | rpt: 1)
        :param authorization_expiration_date: Time Stamp (id: AUT.5 | len: 26 | use: O | rpt: 1)
        :param authorization_identifier: Entity Identifier (id: AUT.6 | len: 30 | use: C | rpt: 1)
        :param reimbursement_limit: Composite Price (id: AUT.7 | len: 25 | use: O | rpt: 1)
        :param requested_number_of_treatments: Numeric (id: AUT.8 | len: 2 | use: O | rpt: 1)
        :param authorized_number_of_treatments: Numeric (id: AUT.9 | len: 2 | use: O | rpt: 1)
        :param process_date: Time Stamp (id: AUT.10 | len: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.authorizing_payor_plan_id = authorizing_payor_plan_id
        self.authorizing_payor_company_id = authorizing_payor_company_id
        self.authorizing_payor_company_name = authorizing_payor_company_name
        self.authorization_effective_date = authorization_effective_date
        self.authorization_expiration_date = authorization_expiration_date
        self.authorization_identifier = authorization_identifier
        self.reimbursement_limit = reimbursement_limit
        self.requested_number_of_treatments = requested_number_of_treatments
        self.authorized_number_of_treatments = authorized_number_of_treatments
        self.process_date = process_date

    @property  # get AUT.1
    def authorizing_payor_plan_id(self) -> InsurancePlanId | None:
        """
        id: AUT.1 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.1
        """
        return self._c_data[0][0]

    @authorizing_payor_plan_id.setter  # set AUT.1
    def authorizing_payor_plan_id(self, insurance_plan_id: InsurancePlanId | None):
        """
        id: AUT.1 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.1
        """
        self._c_data[0] = (insurance_plan_id,)

    @property  # get AUT.2
    def authorizing_payor_company_id(self) -> InsuranceCompanyIdCodes:
        """
        id: AUT.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.2
        """
        return self._c_data[1][0]

    @authorizing_payor_company_id.setter  # set AUT.2
    def authorizing_payor_company_id(
        self, insurance_company_id_codes: InsuranceCompanyIdCodes
    ):
        """
        id: AUT.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.2
        """
        self._c_data[1] = (insurance_company_id_codes,)

    @property  # get AUT.3
    def authorizing_payor_company_name(self) -> ST | None:
        """
        id: AUT.3 | len: 45 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.3
        """
        return self._c_data[2][0]

    @authorizing_payor_company_name.setter  # set AUT.3
    def authorizing_payor_company_name(self, st: ST | None):
        """
        id: AUT.3 | len: 45 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.3
        """
        self._c_data[2] = (st,)

    @property  # get AUT.4
    def authorization_effective_date(self) -> TS | None:
        """
        id: AUT.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.4
        """
        return self._c_data[3][0]

    @authorization_effective_date.setter  # set AUT.4
    def authorization_effective_date(self, ts: TS | None):
        """
        id: AUT.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.4
        """
        self._c_data[3] = (ts,)

    @property  # get AUT.5
    def authorization_expiration_date(self) -> TS | None:
        """
        id: AUT.5 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.5
        """
        return self._c_data[4][0]

    @authorization_expiration_date.setter  # set AUT.5
    def authorization_expiration_date(self, ts: TS | None):
        """
        id: AUT.5 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.5
        """
        self._c_data[4] = (ts,)

    @property  # get AUT.6
    def authorization_identifier(self) -> EI | None:
        """
        id: AUT.6 | len: 30 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.6
        """
        return self._c_data[5][0]

    @authorization_identifier.setter  # set AUT.6
    def authorization_identifier(self, ei: EI | None):
        """
        id: AUT.6 | len: 30 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.6
        """
        self._c_data[5] = (ei,)

    @property  # get AUT.7
    def reimbursement_limit(self) -> CP | None:
        """
        id: AUT.7 | len: 25 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.7
        """
        return self._c_data[6][0]

    @reimbursement_limit.setter  # set AUT.7
    def reimbursement_limit(self, cp: CP | None):
        """
        id: AUT.7 | len: 25 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.7
        """
        self._c_data[6] = (cp,)

    @property  # get AUT.8
    def requested_number_of_treatments(self) -> NM | None:
        """
        id: AUT.8 | len: 2 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.8
        """
        return self._c_data[7][0]

    @requested_number_of_treatments.setter  # set AUT.8
    def requested_number_of_treatments(self, nm: NM | None):
        """
        id: AUT.8 | len: 2 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.8
        """
        self._c_data[7] = (nm,)

    @property  # get AUT.9
    def authorized_number_of_treatments(self) -> NM | None:
        """
        id: AUT.9 | len: 2 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.9
        """
        return self._c_data[8][0]

    @authorized_number_of_treatments.setter  # set AUT.9
    def authorized_number_of_treatments(self, nm: NM | None):
        """
        id: AUT.9 | len: 2 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.9
        """
        self._c_data[8] = (nm,)

    @property  # get AUT.10
    def process_date(self) -> TS | None:
        """
        id: AUT.10 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.10
        """
        return self._c_data[9][0]

    @process_date.setter  # set AUT.10
    def process_date(self, ts: TS | None):
        """
        id: AUT.10 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AUT.10
        """
        self._c_data[9] = (ts,)
