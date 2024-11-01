from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.XON import XON
from ..data_types.ED import ED
from ..data_types.ID import ID
from ..data_types.ST import ST
from ..data_types.XCN import XCN
from ..data_types.CWE import CWE
from ..data_types.SI import SI
from ..data_types.TS import TS
from ..tables.CountryCode import CountryCode
from ..tables.JurisdictionalBreadth import JurisdictionalBreadth
from ..tables.StateOrProvince import StateOrProvince
from ..tables.CountyOrParish import CountyOrParish
from ..tables.CertificateStatus import CertificateStatus
from ..tables.YesOrNoIndicator import YesOrNoIndicator


"""
Certificate Detail - CER
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CER TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CER,
    CE, XON, ED, ID, ST, XCN, CWE, SI, TS
)

cer = CER(  #  - The CER segment adds detailed information regarding the formal authorizations to provide a service (e
    set_id_cer=si,  # SI(...)  # Required.
    serial_number=None,  # ST(...) 
    version=None,  # ST(...) 
    granting_authority=None,  # XON(...) 
    issuing_authority=None,  # XCN(...) 
    signature_of_issuing_authority=None,  # ED(...) 
    granting_country=None,  # ID(...) 
    granting_state_or_province=None,  # CWE(...) 
    granting_county_or_parish=None,  # CWE(...) 
    certificate_type=None,  # CWE(...) 
    certificate_domain=None,  # CWE(...) 
    subject_id=None,  # ID(...) 
    subject_name=st,  # ST(...)  # Required.
    subject_directory_attribute_extension=None,  # CWE(...) 
    subject_public_key_info=None,  # CWE(...) 
    authority_key_identifier=None,  # CWE(...) 
    basic_constraint=None,  # ID(...) 
    crl_distribution_point=None,  # CWE(...) 
    jurisdiction_country=None,  # ID(...) 
    jurisdiction_state_or_province=None,  # CWE(...) 
    jurisdiction_county_or_parish=None,  # CWE(...) 
    jurisdiction_breadth=None,  # CWE(...) 
    granting_date=None,  # TS(...) 
    issuing_date=None,  # TS(...) 
    activation_date=None,  # TS(...) 
    inactivation_date=None,  # TS(...) 
    expiration_date=None,  # TS(...) 
    renewal_date=None,  # TS(...) 
    revocation_date=None,  # TS(...) 
    revocation_reason_code=None,  # CE(...) 
    certificate_status=None,  # CWE(...) 
)

-----END SEGMENT::CER TEMPLATE-----
"""


class CER(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CER"""
    _hl7_name = """Certificate Detail"""
    _hl7_description = """The CER segment adds detailed information regarding the formal authorizations to provide a service (e"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CER"
    _c_length = (4, 80, 80, 250, 250, 65536, 3, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 3, 250, 250, 250, 26, 26, 26, 26, 26, 26, 26, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 65535, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "C", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, ST, ST, XON, XCN, ED, ID, CWE, CWE, CWE, CWE, ID, ST, CWE, CWE, CWE, ID, CWE, ID, CWE, CWE, CWE, TS, TS, TS, TS, TS, TS, TS, CE, CWE,)
    _c_aliases = ("CER.1", "CER.2", "CER.3", "CER.4", "CER.5", "CER.6", "CER.7", "CER.8", "CER.9", "CER.10", "CER.11", "CER.12", "CER.13", "CER.14", "CER.15", "CER.16", "CER.17", "CER.18", "CER.19", "CER.20", "CER.21", "CER.22", "CER.23", "CER.24", "CER.25", "CER.26", "CER.27", "CER.28", "CER.29", "CER.30", "CER.31",)
    _c_names = ("Set ID - CER", "Serial Number", "Version", "Granting Authority", "Issuing Authority", "Signature of Issuing Authority", "Granting Country", "Granting State/Province", "Granting County/Parish", "Certificate Type", "Certificate Domain", "Subject ID", "Subject Name", "Subject Directory Attribute Extension (Health Professional Data)", "Subject Public Key Info", "Authority Key Identifier", "Basic Constraint", "CRL Distribution Point", "Jurisdiction Country", "Jurisdiction State/Province", "Jurisdiction County/Parish", "Jurisdiction Breadth", "Granting Date", "Issuing Date", "Activation Date", "Inactivation Date", "Expiration Date", "Renewal Date", "Revocation Date", "Revocation Reason Code", "Certificate Status",)
    _c_attrs = ("set_id_cer", "serial_number", "version", "granting_authority", "issuing_authority", "signature_of_issuing_authority", "granting_country", "granting_state_or_province", "granting_county_or_parish", "certificate_type", "certificate_domain", "subject_id", "subject_name", "subject_directory_attribute_extension", "subject_public_key_info", "authority_key_identifier", "basic_constraint", "crl_distribution_point", "jurisdiction_country", "jurisdiction_state_or_province", "jurisdiction_county_or_parish", "jurisdiction_breadth", "granting_date", "issuing_date", "activation_date", "inactivation_date", "expiration_date", "renewal_date", "revocation_date", "revocation_reason_code", "certificate_status",)
    # fmt: on

    def __init__(
        self,
        set_id_cer: SI,  # CER.1
        subject_name: ST,  # CER.13
        serial_number: ST | None = None,  # CER.2
        version: ST | None = None,  # CER.3
        granting_authority: XON | None = None,  # CER.4
        issuing_authority: XCN | None = None,  # CER.5
        signature_of_issuing_authority: ED | None = None,  # CER.6
        granting_country: CountryCode | ID | None = None,  # CER.7
        granting_state_or_province: StateOrProvince | CWE | None = None,  # CER.8
        granting_county_or_parish: CountyOrParish | CWE | None = None,  # CER.9
        certificate_type: CWE | None = None,  # CER.10
        certificate_domain: CWE | None = None,  # CER.11
        subject_id: ID | None = None,  # CER.12
        subject_directory_attribute_extension: CWE | None = None,  # CER.14
        subject_public_key_info: CWE | None = None,  # CER.15
        authority_key_identifier: CWE | None = None,  # CER.16
        basic_constraint: YesOrNoIndicator | ID | None = None,  # CER.17
        crl_distribution_point: CWE | None = None,  # CER.18
        jurisdiction_country: CountryCode | ID | None = None,  # CER.19
        jurisdiction_state_or_province: StateOrProvince | CWE | None = None,  # CER.20
        jurisdiction_county_or_parish: CountyOrParish | CWE | None = None,  # CER.21
        jurisdiction_breadth: JurisdictionalBreadth | CWE | None = None,  # CER.22
        granting_date: TS | None = None,  # CER.23
        issuing_date: TS | None = None,  # CER.24
        activation_date: TS | None = None,  # CER.25
        inactivation_date: TS | None = None,  # CER.26
        expiration_date: TS | None = None,  # CER.27
        renewal_date: TS | None = None,  # CER.28
        revocation_date: TS | None = None,  # CER.29
        revocation_reason_code: CE | None = None,  # CER.30
        certificate_status: CertificateStatus | CWE | None = None,  # CER.31
    ):
        """
        Certificate Detail - `CER <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CER>`_
        The CER segment adds detailed information regarding the formal authorizations to provide a service (e.g. licenses, certificates) held by the health professional identified by the STF segment.

        :param set_id_cer: Sequence ID (id: CER.1 | len: 4 | use: R | rpt: 1)
        :param serial_number: String Data (id: CER.2 | len: 80 | use: O | rpt: 1)
        :param version: String Data (id: CER.3 | len: 80 | use: O | rpt: 1)
        :param granting_authority: Extended Composite Name and Identification Number for Organizations (id: CER.4 | len: 250 | use: O | rpt: 1)
        :param issuing_authority: Extended Composite ID Number and Name for Persons (id: CER.5 | len: 250 | use: O | rpt: 1)
        :param signature_of_issuing_authority: Encapsulated Data (id: CER.6 | len: 65536 | use: O | rpt: 1)
        :param granting_country: Coded values for HL7 tables (id: CER.7 | len: 3 | use: O | rpt: 1)
        :param granting_state_or_province: Coded with Exceptions (id: CER.8 | len: 250 | use: O | rpt: 1)
        :param granting_county_or_parish: Coded with Exceptions (id: CER.9 | len: 250 | use: O | rpt: 1)
        :param certificate_type: Coded with Exceptions (id: CER.10 | len: 250 | use: O | rpt: 1)
        :param certificate_domain: Coded with Exceptions (id: CER.11 | len: 250 | use: O | rpt: 1)
        :param subject_id: Coded values for HL7 tables (id: CER.12 | len: 250 | use: C | rpt: 1)
        :param subject_name: String Data (id: CER.13 | len: 250 | use: R | rpt: 1)
        :param subject_directory_attribute_extension: Coded with Exceptions (id: CER.14 | len: 250 | use: O | rpt: *)
        :param subject_public_key_info: Coded with Exceptions (id: CER.15 | len: 250 | use: O | rpt: 1)
        :param authority_key_identifier: Coded with Exceptions (id: CER.16 | len: 250 | use: O | rpt: 1)
        :param basic_constraint: Coded values for HL7 tables (id: CER.17 | len: 250 | use: O | rpt: 1)
        :param crl_distribution_point: Coded with Exceptions (id: CER.18 | len: 250 | use: O | rpt: *)
        :param jurisdiction_country: Coded values for HL7 tables (id: CER.19 | len: 3 | use: O | rpt: 1)
        :param jurisdiction_state_or_province: Coded with Exceptions (id: CER.20 | len: 250 | use: O | rpt: 1)
        :param jurisdiction_county_or_parish: Coded with Exceptions (id: CER.21 | len: 250 | use: O | rpt: 1)
        :param jurisdiction_breadth: Coded with Exceptions (id: CER.22 | len: 250 | use: O | rpt: *)
        :param granting_date: Time Stamp (id: CER.23 | len: 26 | use: O | rpt: 1)
        :param issuing_date: Time Stamp (id: CER.24 | len: 26 | use: O | rpt: 1)
        :param activation_date: Time Stamp (id: CER.25 | len: 26 | use: O | rpt: 1)
        :param inactivation_date: Time Stamp (id: CER.26 | len: 26 | use: O | rpt: 1)
        :param expiration_date: Time Stamp (id: CER.27 | len: 26 | use: O | rpt: 1)
        :param renewal_date: Time Stamp (id: CER.28 | len: 26 | use: O | rpt: 1)
        :param revocation_date: Time Stamp (id: CER.29 | len: 26 | use: O | rpt: 1)
        :param revocation_reason_code: Coded Element (id: CER.30 | len: 250 | use: O | rpt: 1)
        :param certificate_status: Coded with Exceptions (id: CER.31 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 31
        self.set_id_cer = set_id_cer
        self.serial_number = serial_number
        self.version = version
        self.granting_authority = granting_authority
        self.issuing_authority = issuing_authority
        self.signature_of_issuing_authority = signature_of_issuing_authority
        self.granting_country = granting_country
        self.granting_state_or_province = granting_state_or_province
        self.granting_county_or_parish = granting_county_or_parish
        self.certificate_type = certificate_type
        self.certificate_domain = certificate_domain
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.subject_directory_attribute_extension = (
            subject_directory_attribute_extension
        )
        self.subject_public_key_info = subject_public_key_info
        self.authority_key_identifier = authority_key_identifier
        self.basic_constraint = basic_constraint
        self.crl_distribution_point = crl_distribution_point
        self.jurisdiction_country = jurisdiction_country
        self.jurisdiction_state_or_province = jurisdiction_state_or_province
        self.jurisdiction_county_or_parish = jurisdiction_county_or_parish
        self.jurisdiction_breadth = jurisdiction_breadth
        self.granting_date = granting_date
        self.issuing_date = issuing_date
        self.activation_date = activation_date
        self.inactivation_date = inactivation_date
        self.expiration_date = expiration_date
        self.renewal_date = renewal_date
        self.revocation_date = revocation_date
        self.revocation_reason_code = revocation_reason_code
        self.certificate_status = certificate_status

    @property  # get CER.1
    def set_id_cer(self) -> SI:
        """
        id: CER.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.1
        """
        return self._c_data[0][0]

    @set_id_cer.setter  # set CER.1
    def set_id_cer(self, si: SI):
        """
        id: CER.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.1
        """
        self._c_data[0] = (si,)

    @property  # get CER.2
    def serial_number(self) -> ST | None:
        """
        id: CER.2 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.2
        """
        return self._c_data[1][0]

    @serial_number.setter  # set CER.2
    def serial_number(self, st: ST | None):
        """
        id: CER.2 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.2
        """
        self._c_data[1] = (st,)

    @property  # get CER.3
    def version(self) -> ST | None:
        """
        id: CER.3 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.3
        """
        return self._c_data[2][0]

    @version.setter  # set CER.3
    def version(self, st: ST | None):
        """
        id: CER.3 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.3
        """
        self._c_data[2] = (st,)

    @property  # get CER.4
    def granting_authority(self) -> XON | None:
        """
        id: CER.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.4
        """
        return self._c_data[3][0]

    @granting_authority.setter  # set CER.4
    def granting_authority(self, xon: XON | None):
        """
        id: CER.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.4
        """
        self._c_data[3] = (xon,)

    @property  # get CER.5
    def issuing_authority(self) -> XCN | None:
        """
        id: CER.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.5
        """
        return self._c_data[4][0]

    @issuing_authority.setter  # set CER.5
    def issuing_authority(self, xcn: XCN | None):
        """
        id: CER.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.5
        """
        self._c_data[4] = (xcn,)

    @property  # get CER.6
    def signature_of_issuing_authority(self) -> ED | None:
        """
        id: CER.6 | len: 65536 | use: O | rpt: 1
        ---
        return_type: ED: Encapsulated Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.6
        """
        return self._c_data[5][0]

    @signature_of_issuing_authority.setter  # set CER.6
    def signature_of_issuing_authority(self, ed: ED | None):
        """
        id: CER.6 | len: 65536 | use: O | rpt: 1
        ---
        param_type: ED: Encapsulated Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.6
        """
        self._c_data[5] = (ed,)

    @property  # get CER.7
    def granting_country(self) -> CountryCode | None:
        """
        id: CER.7 | len: 3 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.7
        """
        return self._c_data[6][0]

    @granting_country.setter  # set CER.7
    def granting_country(self, country_code: CountryCode | None):
        """
        id: CER.7 | len: 3 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.7
        """
        self._c_data[6] = (country_code,)

    @property  # get CER.8
    def granting_state_or_province(self) -> StateOrProvince | None:
        """
        id: CER.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.8
        """
        return self._c_data[7][0]

    @granting_state_or_province.setter  # set CER.8
    def granting_state_or_province(self, state_or_province: StateOrProvince | None):
        """
        id: CER.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.8
        """
        self._c_data[7] = (state_or_province,)

    @property  # get CER.9
    def granting_county_or_parish(self) -> CountyOrParish | None:
        """
        id: CER.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.9
        """
        return self._c_data[8][0]

    @granting_county_or_parish.setter  # set CER.9
    def granting_county_or_parish(self, county_or_parish: CountyOrParish | None):
        """
        id: CER.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.9
        """
        self._c_data[8] = (county_or_parish,)

    @property  # get CER.10
    def certificate_type(self) -> CWE | None:
        """
        id: CER.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.10
        """
        return self._c_data[9][0]

    @certificate_type.setter  # set CER.10
    def certificate_type(self, cwe: CWE | None):
        """
        id: CER.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.10
        """
        self._c_data[9] = (cwe,)

    @property  # get CER.11
    def certificate_domain(self) -> CWE | None:
        """
        id: CER.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.11
        """
        return self._c_data[10][0]

    @certificate_domain.setter  # set CER.11
    def certificate_domain(self, cwe: CWE | None):
        """
        id: CER.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.11
        """
        self._c_data[10] = (cwe,)

    @property  # get CER.12
    def subject_id(self) -> ID | None:
        """
        id: CER.12 | len: 250 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.12
        """
        return self._c_data[11][0]

    @subject_id.setter  # set CER.12
    def subject_id(self, id: ID | None):
        """
        id: CER.12 | len: 250 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.12
        """
        self._c_data[11] = (id,)

    @property  # get CER.13
    def subject_name(self) -> ST:
        """
        id: CER.13 | len: 250 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.13
        """
        return self._c_data[12][0]

    @subject_name.setter  # set CER.13
    def subject_name(self, st: ST):
        """
        id: CER.13 | len: 250 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.13
        """
        self._c_data[12] = (st,)

    @property
    def subject_directory_attribute_extension(self) -> tuple[CWE, ...] | tuple[None]:
        """
        id: CER.14 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.14
        """
        return self._c_data[13]

    @subject_directory_attribute_extension.setter  # set CER.14
    def subject_directory_attribute_extension(self, cwe: CWE | tuple[CWE] | None):
        """
        id: CER.14 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.14
        """
        if isinstance(cwe, tuple):
            self._c_data[13] = cwe
        else:
            self._c_data[13] = (cwe,)

    @property  # get CER.15
    def subject_public_key_info(self) -> CWE | None:
        """
        id: CER.15 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.15
        """
        return self._c_data[14][0]

    @subject_public_key_info.setter  # set CER.15
    def subject_public_key_info(self, cwe: CWE | None):
        """
        id: CER.15 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.15
        """
        self._c_data[14] = (cwe,)

    @property  # get CER.16
    def authority_key_identifier(self) -> CWE | None:
        """
        id: CER.16 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.16
        """
        return self._c_data[15][0]

    @authority_key_identifier.setter  # set CER.16
    def authority_key_identifier(self, cwe: CWE | None):
        """
        id: CER.16 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.16
        """
        self._c_data[15] = (cwe,)

    @property  # get CER.17
    def basic_constraint(self) -> YesOrNoIndicator | None:
        """
        id: CER.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.17
        """
        return self._c_data[16][0]

    @basic_constraint.setter  # set CER.17
    def basic_constraint(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: CER.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.17
        """
        self._c_data[16] = (yes_or_no_indicator,)

    @property
    def crl_distribution_point(self) -> tuple[CWE, ...] | tuple[None]:
        """
        id: CER.18 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.18
        """
        return self._c_data[17]

    @crl_distribution_point.setter  # set CER.18
    def crl_distribution_point(self, cwe: CWE | tuple[CWE] | None):
        """
        id: CER.18 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.18
        """
        if isinstance(cwe, tuple):
            self._c_data[17] = cwe
        else:
            self._c_data[17] = (cwe,)

    @property  # get CER.19
    def jurisdiction_country(self) -> CountryCode | None:
        """
        id: CER.19 | len: 3 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.19
        """
        return self._c_data[18][0]

    @jurisdiction_country.setter  # set CER.19
    def jurisdiction_country(self, country_code: CountryCode | None):
        """
        id: CER.19 | len: 3 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.19
        """
        self._c_data[18] = (country_code,)

    @property  # get CER.20
    def jurisdiction_state_or_province(self) -> StateOrProvince | None:
        """
        id: CER.20 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.20
        """
        return self._c_data[19][0]

    @jurisdiction_state_or_province.setter  # set CER.20
    def jurisdiction_state_or_province(self, state_or_province: StateOrProvince | None):
        """
        id: CER.20 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.20
        """
        self._c_data[19] = (state_or_province,)

    @property  # get CER.21
    def jurisdiction_county_or_parish(self) -> CountyOrParish | None:
        """
        id: CER.21 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.21
        """
        return self._c_data[20][0]

    @jurisdiction_county_or_parish.setter  # set CER.21
    def jurisdiction_county_or_parish(self, county_or_parish: CountyOrParish | None):
        """
        id: CER.21 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.21
        """
        self._c_data[20] = (county_or_parish,)

    @property
    def jurisdiction_breadth(self) -> tuple[JurisdictionalBreadth, ...] | tuple[None]:
        """
        id: CER.22 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.22
        """
        return self._c_data[21]

    @jurisdiction_breadth.setter  # set CER.22
    def jurisdiction_breadth(
        self,
        jurisdictional_breadth: JurisdictionalBreadth
        | tuple[JurisdictionalBreadth]
        | None,
    ):
        """
        id: CER.22 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.22
        """
        if isinstance(jurisdictional_breadth, tuple):
            self._c_data[21] = jurisdictional_breadth
        else:
            self._c_data[21] = (jurisdictional_breadth,)

    @property  # get CER.23
    def granting_date(self) -> TS | None:
        """
        id: CER.23 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.23
        """
        return self._c_data[22][0]

    @granting_date.setter  # set CER.23
    def granting_date(self, ts: TS | None):
        """
        id: CER.23 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.23
        """
        self._c_data[22] = (ts,)

    @property  # get CER.24
    def issuing_date(self) -> TS | None:
        """
        id: CER.24 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.24
        """
        return self._c_data[23][0]

    @issuing_date.setter  # set CER.24
    def issuing_date(self, ts: TS | None):
        """
        id: CER.24 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.24
        """
        self._c_data[23] = (ts,)

    @property  # get CER.25
    def activation_date(self) -> TS | None:
        """
        id: CER.25 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.25
        """
        return self._c_data[24][0]

    @activation_date.setter  # set CER.25
    def activation_date(self, ts: TS | None):
        """
        id: CER.25 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.25
        """
        self._c_data[24] = (ts,)

    @property  # get CER.26
    def inactivation_date(self) -> TS | None:
        """
        id: CER.26 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.26
        """
        return self._c_data[25][0]

    @inactivation_date.setter  # set CER.26
    def inactivation_date(self, ts: TS | None):
        """
        id: CER.26 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.26
        """
        self._c_data[25] = (ts,)

    @property  # get CER.27
    def expiration_date(self) -> TS | None:
        """
        id: CER.27 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.27
        """
        return self._c_data[26][0]

    @expiration_date.setter  # set CER.27
    def expiration_date(self, ts: TS | None):
        """
        id: CER.27 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.27
        """
        self._c_data[26] = (ts,)

    @property  # get CER.28
    def renewal_date(self) -> TS | None:
        """
        id: CER.28 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.28
        """
        return self._c_data[27][0]

    @renewal_date.setter  # set CER.28
    def renewal_date(self, ts: TS | None):
        """
        id: CER.28 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.28
        """
        self._c_data[27] = (ts,)

    @property  # get CER.29
    def revocation_date(self) -> TS | None:
        """
        id: CER.29 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.29
        """
        return self._c_data[28][0]

    @revocation_date.setter  # set CER.29
    def revocation_date(self, ts: TS | None):
        """
        id: CER.29 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.29
        """
        self._c_data[28] = (ts,)

    @property  # get CER.30
    def revocation_reason_code(self) -> CE | None:
        """
        id: CER.30 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.30
        """
        return self._c_data[29][0]

    @revocation_reason_code.setter  # set CER.30
    def revocation_reason_code(self, ce: CE | None):
        """
        id: CER.30 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.30
        """
        self._c_data[29] = (ce,)

    @property  # get CER.31
    def certificate_status(self) -> CertificateStatus | None:
        """
        id: CER.31 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.31
        """
        return self._c_data[30][0]

    @certificate_status.setter  # set CER.31
    def certificate_status(self, certificate_status: CertificateStatus | None):
        """
        id: CER.31 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CER.31
        """
        self._c_data[30] = (certificate_status,)
