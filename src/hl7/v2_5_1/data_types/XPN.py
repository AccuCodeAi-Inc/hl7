from __future__ import annotations
from ...base import DataType
from .TS import TS
from .ID import ID
from .IS import IS
from .DR import DR
from .ST import ST
from .CE import CE
from .FN import FN
from ..tables.NameContext import NameContext
from ..tables.NameType import NameType
from ..tables.DegreeOrLicenseOrCertificate import DegreeOrLicenseOrCertificate
from ..tables.FirstName import FirstName
from ..tables.NameOrAddressRepresentation import NameOrAddressRepresentation
from ..tables.NameAssemblyOrder import NameAssemblyOrder


"""
DataType - XPN
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::XPN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    XPN,
    TS, ID, IS, DR, ST, CE, FN
)

xpn = XPN(  # Extended Person Name - 
    family_name=None,  # FN(...) 
    given_name=None,  # ST(...) 
    second_and_further_given_names_or_initials_thereof=None,  # ST(...) 
    suffix=None,  # ST(...) 
    prefix=None,  # ST(...) 
    degree=None,  # IS(...) 
    name_type_code=None,  # ID(...) 
    name_representation_code=None,  # ID(...) 
    name_context=None,  # CE(...) 
    name_validity_range=None,  # DR(...) 
    name_assembly_order=None,  # ID(...) 
    effective_date=None,  # TS(...) 
    expiration_date=None,  # TS(...) 
    professional_suffix=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::XPN TEMPLATE-----
"""


class XPN(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 1103
    _hl7_id = """XPN"""
    _hl7_name = """Extended Person Name"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN"
    _c_length = (194, 30, 30, 20, 20, 6, 1, 1, 483, 53, 1, 26, 26, 199,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "B", "O", "O", "O", "B", "O", "O", "O", "O",)
    _c_aliases = ("XPN.1", "XPN.2", "XPN.3", "XPN.4", "XPN.5", "XPN.6", "XPN.7", "XPN.8", "XPN.9", "XPN.10", "XPN.11", "XPN.12", "XPN.13", "XPN.14",)
    _c_components = (FN, ST, ST, ST, ST, IS, ID, ID, CE, DR, ID, TS, TS, ST,)
    _c_names = ("Family Name", "Given Name", "Second And Further Given Names Or Initials Thereof", "Suffix (e.g., Jr Or Iii)", "Prefix (e.g., Dr)", "Degree (e.g., Md)", "Name Type Code", "Name Representation Code", "Name Context", "Name Validity Range", "Name Assembly Order", "Effective Date", "Expiration Date", "Professional Suffix",)
    _c_attrs = ("family_name", "given_name", "second_and_further_given_names_or_initials_thereof", "suffix", "prefix", "degree", "name_type_code", "name_representation_code", "name_context", "name_validity_range", "name_assembly_order", "effective_date", "expiration_date", "professional_suffix",)
    # fmt: on

    def __init__(
        self,
        family_name: FN | tuple[FN] | None = None,  # XPN.1
        given_name: FirstName | ST | tuple[FirstName | ST] | None = None,  # XPN.2
        second_and_further_given_names_or_initials_thereof: ST
        | tuple[ST]
        | None = None,  # XPN.3
        suffix: ST | tuple[ST] | None = None,  # XPN.4
        prefix: ST | tuple[ST] | None = None,  # XPN.5
        degree: DegreeOrLicenseOrCertificate
        | IS
        | tuple[DegreeOrLicenseOrCertificate | IS]
        | None = None,  # XPN.6
        name_type_code: NameType | ID | tuple[NameType | ID] | None = None,  # XPN.7
        name_representation_code: NameOrAddressRepresentation
        | ID
        | tuple[NameOrAddressRepresentation | ID]
        | None = None,  # XPN.8
        name_context: NameContext | CE | tuple[NameContext | CE] | None = None,  # XPN.9
        name_validity_range: DR | tuple[DR] | None = None,  # XPN.10
        name_assembly_order: NameAssemblyOrder
        | ID
        | tuple[NameAssemblyOrder | ID]
        | None = None,  # XPN.11
        effective_date: TS | tuple[TS] | None = None,  # XPN.12
        expiration_date: TS | tuple[TS] | None = None,  # XPN.13
        professional_suffix: ST | tuple[ST] | None = None,  # XPN.14
    ):
        """
        Extended Person Name - `XPN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/XPN>`_


        :param family_name: This component allows full specification of the surname of a person (id: XPN.1 | len: 194 | use: O | rpt: 1)
        :param given_name: First name (id: XPN.2 | len: 30 | use: O | rpt: 1)
        :param second_and_further_given_names_or_initials_thereof: Multiple middle names may be included by separating them with spaces (id: XPN.3 | len: 30 | use: O | rpt: 1)
        :param suffix: Used to specify a name suffix (e (id: XPN.4 | len: 20 | use: O | rpt: 1)
        :param prefix: Used to specify a name prefix (e (id: XPN.5 | len: 20 | use: O | rpt: 1)
        :param degree: Retained for backward compatibility only as of v 2 (id: XPN.6 | len: 6 | use: B | rpt: 1)
        :param name_type_code: A code that represents the type of name (id: XPN.7 | len: 1 | use: O | rpt: 1)
        :param name_representation_code: Different <name/address types> and representations of the same <name/address> should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component (id: XPN.8 | len: 1 | use: O | rpt: 1)
        :param name_context: This component is used to designate the context in which a name is used (id: XPN.9 | len: 483 | use: O | rpt: 1)
        :param name_validity_range: This component cannot be fully expressed (id: XPN.10 | len: 53 | use: B | rpt: 1)
        :param name_assembly_order: A code that represents the preferred display order of the components of this person name (id: XPN.11 | len: 1 | use: O | rpt: 1)
        :param effective_date: The first date, if known, on which the person name is valid and active (id: XPN.12 | len: 26 | use: O | rpt: 1)
        :param expiration_date: The last date, if known, on which the person name is valid and active (id: XPN.13 | len: 26 | use: O | rpt: 1)
        :param professional_suffix: Used to specify an abbreviation, or a string of abbreviations denoting qualifications that support the persons profession, (e (id: XPN.14 | len: 199 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 14
        self.family_name = family_name
        self.given_name = given_name
        self.second_and_further_given_names_or_initials_thereof = (
            second_and_further_given_names_or_initials_thereof
        )
        self.suffix = suffix
        self.prefix = prefix
        self.degree = degree
        self.name_type_code = name_type_code
        self.name_representation_code = name_representation_code
        self.name_context = name_context
        self.name_validity_range = name_validity_range
        self.name_assembly_order = name_assembly_order
        self.effective_date = effective_date
        self.expiration_date = expiration_date
        self.professional_suffix = professional_suffix

    @property  # get XPN.1
    def family_name(self) -> FN | None:
        """
        id: XPN.1 | len: 194 | use: O | rpt: 1
        ---
        This component allows full specification of the surname of a person. Where appropriate, it differentiates the person's own surname from that of the person's partner or spouse, in cases where the person's name may contain elements from either name. It also permits messages to distinguish the surname prefix (such as "van" or "de") from the surname root. See section 2.A.30, "FN - family name".
        ---
        return_type: FN: Family Name
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.1
        """
        return self._c_data[0][0]

    @family_name.setter  # set XPN.1
    def family_name(self, fn: FN | None):
        """
        id: XPN.1 | len: 194 | use: O | rpt: 1
        ---
        This component allows full specification of the surname of a person. Where appropriate, it differentiates the person's own surname from that of the person's partner or spouse, in cases where the person's name may contain elements from either name. It also permits messages to distinguish the surname prefix (such as "van" or "de") from the surname root. See section 2.A.30, "FN - family name".
        ---
        param_type: FN: Family Name
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.1
        """
        self._c_data[0] = (fn,)

    @property  # get XPN.2
    def given_name(self) -> FirstName | None:
        """
        id: XPN.2 | len: 30 | use: O | rpt: 1
        ---
        First name.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.2
        """
        return self._c_data[1][0]

    @given_name.setter  # set XPN.2
    def given_name(self, first_name: FirstName | None):
        """
        id: XPN.2 | len: 30 | use: O | rpt: 1
        ---
        First name.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.2
        """
        self._c_data[1] = (first_name,)

    @property  # get XPN.3
    def second_and_further_given_names_or_initials_thereof(self) -> ST | None:
        """
        id: XPN.3 | len: 30 | use: O | rpt: 1
        ---
        Multiple middle names may be included by separating them with spaces.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.3
        """
        return self._c_data[2][0]

    @second_and_further_given_names_or_initials_thereof.setter  # set XPN.3
    def second_and_further_given_names_or_initials_thereof(self, st: ST | None):
        """
        id: XPN.3 | len: 30 | use: O | rpt: 1
        ---
        Multiple middle names may be included by separating them with spaces.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.3
        """
        self._c_data[2] = (st,)

    @property  # get XPN.4
    def suffix(self) -> ST | None:
        """
        id: XPN.4 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name suffix (e.g., Jr. or III).
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.4
        """
        return self._c_data[3][0]

    @suffix.setter  # set XPN.4
    def suffix(self, st: ST | None):
        """
        id: XPN.4 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name suffix (e.g., Jr. or III).
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.4
        """
        self._c_data[3] = (st,)

    @property  # get XPN.5
    def prefix(self) -> ST | None:
        """
        id: XPN.5 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name prefix (e.g., Dr.).
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.5
        """
        return self._c_data[4][0]

    @prefix.setter  # set XPN.5
    def prefix(self, st: ST | None):
        """
        id: XPN.5 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name prefix (e.g., Dr.).
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.5
        """
        self._c_data[4] = (st,)

    @property  # get XPN.6
    def degree(self) -> DegreeOrLicenseOrCertificate | None:
        """
        id: XPN.6 | len: 6 | use: B | rpt: 1
        ---
        Retained for backward compatibility only as of v 2.5. See Professional Suffix component.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.6
        """
        return self._c_data[5][0]

    @degree.setter  # set XPN.6
    def degree(
        self, degree_or_license_or_certificate: DegreeOrLicenseOrCertificate | None
    ):
        """
        id: XPN.6 | len: 6 | use: B | rpt: 1
        ---
        Retained for backward compatibility only as of v 2.5. See Professional Suffix component.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.6
        """
        self._c_data[5] = (degree_or_license_or_certificate,)

    @property  # get XPN.7
    def name_type_code(self) -> NameType | None:
        """
        id: XPN.7 | len: 1 | use: O | rpt: 1
        ---
        A code that represents the type of name. Refer to HL7 Table 0200 - Name type for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.7
        """
        return self._c_data[6][0]

    @name_type_code.setter  # set XPN.7
    def name_type_code(self, name_type: NameType | None):
        """
        id: XPN.7 | len: 1 | use: O | rpt: 1
        ---
        A code that represents the type of name. Refer to HL7 Table 0200 - Name type for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.7
        """
        self._c_data[6] = (name_type,)

    @property  # get XPN.8
    def name_representation_code(self) -> NameOrAddressRepresentation | None:
        """
        id: XPN.8 | len: 1 | use: O | rpt: 1
        ---
        Different <name/address types> and representations of the same <name/address> should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.8
        """
        return self._c_data[7][0]

    @name_representation_code.setter  # set XPN.8
    def name_representation_code(
        self, name_or_address_representation: NameOrAddressRepresentation | None
    ):
        """
        id: XPN.8 | len: 1 | use: O | rpt: 1
        ---
        Different <name/address types> and representations of the same <name/address> should be described by repeating of this field, with different values of the <name/address type> and/or <name/address representation> component.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.8
        """
        self._c_data[7] = (name_or_address_representation,)

    @property  # get XPN.9
    def name_context(self) -> CE | None:
        """
        id: XPN.9 | len: 483 | use: O | rpt: 1
        ---
        This component is used to designate the context in which a name is used. The main use case is in Australian healthcare for indigenous patients who prefer to use different names when attending different healthcare institutions. Another use case occurs in the US where health practitioners can be licensed under slightly different names and the reporting of the correct name is vital for administrative purposes. Refer to User-defined Table 0448 - Name context for suggested values.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.9
        """
        return self._c_data[8][0]

    @name_context.setter  # set XPN.9
    def name_context(self, ce: CE | None):
        """
        id: XPN.9 | len: 483 | use: O | rpt: 1
        ---
        This component is used to designate the context in which a name is used. The main use case is in Australian healthcare for indigenous patients who prefer to use different names when attending different healthcare institutions. Another use case occurs in the US where health practitioners can be licensed under slightly different names and the reporting of the correct name is vital for administrative purposes. Refer to User-defined Table 0448 - Name context for suggested values.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.9
        """
        self._c_data[8] = (ce,)

    @property  # get XPN.10
    def name_validity_range(self) -> DR | None:
        """
                id: XPN.10 | len: 53 | use: B | rpt: 1
                ---
                This component cannot be fully expressed. Identified as v 2.4 erratum. Retained for backward compatibility only as of v 2.5. Refer to Effective Date and Expiration Date components.

        This component contains the start and end date/times, which define the period during which this name was valid. See section 2.A.20, "DR - date/time range" for description of subcomponents.
                ---
                return_type: DR: Date/Time Range
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.10
        """
        return self._c_data[9][0]

    @name_validity_range.setter  # set XPN.10
    def name_validity_range(self, dr: DR | None):
        """
                id: XPN.10 | len: 53 | use: B | rpt: 1
                ---
                This component cannot be fully expressed. Identified as v 2.4 erratum. Retained for backward compatibility only as of v 2.5. Refer to Effective Date and Expiration Date components.

        This component contains the start and end date/times, which define the period during which this name was valid. See section 2.A.20, "DR - date/time range" for description of subcomponents.
                ---
                param_type: DR: Date/Time Range
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.10
        """
        self._c_data[9] = (dr,)

    @property  # get XPN.11
    def name_assembly_order(self) -> NameAssemblyOrder | None:
        """
        id: XPN.11 | len: 1 | use: O | rpt: 1
        ---
        A code that represents the preferred display order of the components of this person name. Refer to HL7 0444 - Name assembly order for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.11
        """
        return self._c_data[10][0]

    @name_assembly_order.setter  # set XPN.11
    def name_assembly_order(self, name_assembly_order: NameAssemblyOrder | None):
        """
        id: XPN.11 | len: 1 | use: O | rpt: 1
        ---
        A code that represents the preferred display order of the components of this person name. Refer to HL7 0444 - Name assembly order for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.11
        """
        self._c_data[10] = (name_assembly_order,)

    @property  # get XPN.12
    def effective_date(self) -> TS | None:
        """
        id: XPN.12 | len: 26 | use: O | rpt: 1
        ---
        The first date, if known, on which the person name is valid and active.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.12
        """
        return self._c_data[11][0]

    @effective_date.setter  # set XPN.12
    def effective_date(self, ts: TS | None):
        """
        id: XPN.12 | len: 26 | use: O | rpt: 1
        ---
        The first date, if known, on which the person name is valid and active.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.12
        """
        self._c_data[11] = (ts,)

    @property  # get XPN.13
    def expiration_date(self) -> TS | None:
        """
        id: XPN.13 | len: 26 | use: O | rpt: 1
        ---
        The last date, if known, on which the person name is valid and active.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.13
        """
        return self._c_data[12][0]

    @expiration_date.setter  # set XPN.13
    def expiration_date(self, ts: TS | None):
        """
        id: XPN.13 | len: 26 | use: O | rpt: 1
        ---
        The last date, if known, on which the person name is valid and active.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.13
        """
        self._c_data[12] = (ts,)

    @property  # get XPN.14
    def professional_suffix(self) -> ST | None:
        """
        id: XPN.14 | len: 199 | use: O | rpt: 1
        ---
        Used to specify an abbreviation, or a string of abbreviations denoting qualifications that support the persons profession, (e.g., licenses, certificates, degrees, affiliations with professional societies, etc.). The Professional Suffix normally follows the Family Name when the Person Name is used for display purposes. Please note that this component is an unformatted string and is used for display purposes only. Detailed information regarding the contents of Professional Suffix is obtained using appropriate segments in Chapter 15, Personnel Management.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.14
        """
        return self._c_data[13][0]

    @professional_suffix.setter  # set XPN.14
    def professional_suffix(self, st: ST | None):
        """
        id: XPN.14 | len: 199 | use: O | rpt: 1
        ---
        Used to specify an abbreviation, or a string of abbreviations denoting qualifications that support the persons profession, (e.g., licenses, certificates, degrees, affiliations with professional societies, etc.). The Professional Suffix normally follows the Family Name when the Person Name is used for display purposes. Please note that this component is an unformatted string and is used for display purposes only. Detailed information regarding the contents of Professional Suffix is obtained using appropriate segments in Chapter 15, Personnel Management.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/XPN.14
        """
        self._c_data[13] = (st,)
