from __future__ import annotations
from ...base import DataType
from .IS import IS
from .ST import ST
from .ID import ID
from ..tables.DegreeOrLicenseOrCertificate import DegreeOrLicenseOrCertificate
from ..tables.UniversalIdType import UniversalIdType
from ..tables.CnIdSource import CnIdSource
from ..tables.AssigningAuthority import AssigningAuthority


"""
DataType - CNN
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CNN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CNN,
    IS, ST, ID
)

cnn = CNN(  # Composite ID Number and Name Simplified - Specifies a person using both an identifier and the persons name
    id_number=None,  # ST(...) 
    family_name=None,  # ST(...) 
    given_name=None,  # ST(...) 
    second_and_further_given_names_or_initials_thereof=None,  # ST(...) 
    suffix=None,  # ST(...) 
    prefix=None,  # ST(...) 
    degree=None,  # IS(...) 
    source_table=None,  # IS(...) 
    assigning_authority_namespace_id=None,  # IS(...) 
    assigning_authority_universal_id=None,  # ST(...) 
    assigning_authority_universal_id_type=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::CNN TEMPLATE-----
"""


class CNN(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 406
    _hl7_id = """CNN"""
    _hl7_name = """Composite ID Number and Name Simplified"""
    _hl7_description = """Specifies a person using both an identifier and the persons name"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN"
    _c_length = (15, 50, 30, 30, 20, 20, 5, 4, 20, 199, 6,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "C", "C", "C", "C",)
    _c_aliases = ("CNN.1", "CNN.2", "CNN.3", "CNN.4", "CNN.5", "CNN.6", "CNN.7", "CNN.8", "CNN.9", "CNN.10", "CNN.11",)
    _c_components = (ST, ST, ST, ST, ST, ST, IS, IS, IS, ST, ID,)
    _c_names = ("Id Number", "Family Name", "Given Name", "Second And Further Given Names Or Initials Thereof", "Suffix", "Prefix", "Degree", "Source Table", "Assigning Authority - Namespace Id", "Assigning Authority- Universal Id", "Assigning Authority - Universal Id Type",)
    _c_attrs = ("id_number", "family_name", "given_name", "second_and_further_given_names_or_initials_thereof", "suffix", "prefix", "degree", "source_table", "assigning_authority_namespace_id", "assigning_authority_universal_id", "assigning_authority_universal_id_type",)
    # fmt: on

    def __init__(
        self,
        id_number: ST | None = None,  # CNN.1
        family_name: ST | None = None,  # CNN.2
        given_name: ST | None = None,  # CNN.3
        second_and_further_given_names_or_initials_thereof: ST | None = None,  # CNN.4
        suffix: ST | None = None,  # CNN.5
        prefix: ST | None = None,  # CNN.6
        degree: DegreeOrLicenseOrCertificate | IS | None = None,  # CNN.7
        source_table: CnIdSource | IS | None = None,  # CNN.8
        assigning_authority_namespace_id: AssigningAuthority
        | IS
        | None = None,  # CNN.9
        assigning_authority_universal_id: ST | None = None,  # CNN.10
        assigning_authority_universal_id_type: UniversalIdType
        | ID
        | None = None,  # CNN.11
    ):
        """
        Composite ID Number and Name Simplified - `CNN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CNN>`_
        Specifies a person using both an identifier and the persons name

        :param id_number: Coded ID according to a user-defined table (id: CNN.1 | len: 15 | use: O | rpt: 1)
        :param family_name: This component contains the person's family name in a string format (id: CNN.2 | len: 50 | use: O | rpt: 1)
        :param given_name: Used to specify a first name (id: CNN.3 | len: 30 | use: O | rpt: 1)
        :param second_and_further_given_names_or_initials_thereof:  (id: CNN.4 | len: 30 | use: O | rpt: 1)
        :param suffix: Used to specify a name suffix (e (id: CNN.5 | len: 20 | use: O | rpt: 1)
        :param prefix: Used to specify a name prefix (e (id: CNN.6 | len: 20 | use: O | rpt: 1)
        :param degree: Used to specify an educational degree (e (id: CNN.7 | len: 5 | use: O | rpt: 1)
        :param source_table: Refer to User-defined Table 0297 - CN ID source for suggested values (id: CNN.8 | len: 4 | use: C | rpt: 1)
        :param assigning_authority_namespace_id:  Assigning Authority is normally expressed as an HD data type, but has been flattened to 3 components here (CNS (id: CNN.9 | len: 20 | use: C | rpt: 1)
        :param assigning_authority_universal_id: If CNN (id: CNN.10 | len: 199 | use: C | rpt: 1)
        :param assigning_authority_universal_id_type: If this component is a known UID refer to HL7 Table 0301 - Universal ID type for valid values (id: CNN.11 | len: 6 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 11
        self.id_number = id_number
        self.family_name = family_name
        self.given_name = given_name
        self.second_and_further_given_names_or_initials_thereof = (
            second_and_further_given_names_or_initials_thereof
        )
        self.suffix = suffix
        self.prefix = prefix
        self.degree = degree
        self.source_table = source_table
        self.assigning_authority_namespace_id = assigning_authority_namespace_id
        self.assigning_authority_universal_id = assigning_authority_universal_id
        self.assigning_authority_universal_id_type = (
            assigning_authority_universal_id_type
        )

    @property  # get CNN.1
    def id_number(self) -> ST | None:
        """
        id: CNN.1 | len: 15 | use: O | rpt: 1
        ---
        Coded ID according to a user-defined table. If the first component is present, either component 8 or 9, or both 10 and 11, must be valued.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.1
        """
        return self._c_data[0][0]

    @id_number.setter  # set CNN.1
    def id_number(self, st: ST | None):
        """
        id: CNN.1 | len: 15 | use: O | rpt: 1
        ---
        Coded ID according to a user-defined table. If the first component is present, either component 8 or 9, or both 10 and 11, must be valued.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.1
        """
        self._c_data[0] = (st,)

    @property  # get CNN.2
    def family_name(self) -> ST | None:
        """
        id: CNN.2 | len: 50 | use: O | rpt: 1
        ---
        This component contains the person's family name in a string format.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.2
        """
        return self._c_data[1][0]

    @family_name.setter  # set CNN.2
    def family_name(self, st: ST | None):
        """
        id: CNN.2 | len: 50 | use: O | rpt: 1
        ---
        This component contains the person's family name in a string format.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.2
        """
        self._c_data[1] = (st,)

    @property  # get CNN.3
    def given_name(self) -> ST | None:
        """
        id: CNN.3 | len: 30 | use: O | rpt: 1
        ---
        Used to specify a first name.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.3
        """
        return self._c_data[2][0]

    @given_name.setter  # set CNN.3
    def given_name(self, st: ST | None):
        """
        id: CNN.3 | len: 30 | use: O | rpt: 1
        ---
        Used to specify a first name.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.3
        """
        self._c_data[2] = (st,)

    @property  # get CNN.4
    def second_and_further_given_names_or_initials_thereof(self) -> ST | None:
        """
        id: CNN.4 | len: 30 | use: O | rpt: 1
        ---
        None
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.4
        """
        return self._c_data[3][0]

    @second_and_further_given_names_or_initials_thereof.setter  # set CNN.4
    def second_and_further_given_names_or_initials_thereof(self, st: ST | None):
        """
        id: CNN.4 | len: 30 | use: O | rpt: 1
        ---
        None
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.4
        """
        self._c_data[3] = (st,)

    @property  # get CNN.5
    def suffix(self) -> ST | None:
        """
        id: CNN.5 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name suffix (e.g., Jr. or III).
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.5
        """
        return self._c_data[4][0]

    @suffix.setter  # set CNN.5
    def suffix(self, st: ST | None):
        """
        id: CNN.5 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name suffix (e.g., Jr. or III).
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.5
        """
        self._c_data[4] = (st,)

    @property  # get CNN.6
    def prefix(self) -> ST | None:
        """
        id: CNN.6 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name prefix (e.g., Dr.).
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.6
        """
        return self._c_data[5][0]

    @prefix.setter  # set CNN.6
    def prefix(self, st: ST | None):
        """
        id: CNN.6 | len: 20 | use: O | rpt: 1
        ---
        Used to specify a name prefix (e.g., Dr.).
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.6
        """
        self._c_data[5] = (st,)

    @property  # get CNN.7
    def degree(self) -> DegreeOrLicenseOrCertificate | None:
        """
        id: CNN.7 | len: 5 | use: O | rpt: 1
        ---
        Used to specify an educational degree (e.g., MD). Refer to User-defined Table 0360 - Degree for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.7
        """
        return self._c_data[6][0]

    @degree.setter  # set CNN.7
    def degree(
        self, degree_or_license_or_certificate: DegreeOrLicenseOrCertificate | None
    ):
        """
        id: CNN.7 | len: 5 | use: O | rpt: 1
        ---
        Used to specify an educational degree (e.g., MD). Refer to User-defined Table 0360 - Degree for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.7
        """
        self._c_data[6] = (degree_or_license_or_certificate,)

    @property  # get CNN.8
    def source_table(self) -> CnIdSource | None:
        """
        id: CNN.8 | len: 4 | use: C | rpt: 1
        ---
        Refer to User-defined Table 0297 - CN ID source for suggested values. Used to delineate the first component. If component 1 is valued, either component 8, or 9, or both 10 and 11, must be valued.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.8
        """
        return self._c_data[7][0]

    @source_table.setter  # set CNN.8
    def source_table(self, cn_id_source: CnIdSource | None):
        """
        id: CNN.8 | len: 4 | use: C | rpt: 1
        ---
        Refer to User-defined Table 0297 - CN ID source for suggested values. Used to delineate the first component. If component 1 is valued, either component 8, or 9, or both 10 and 11, must be valued.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.8
        """
        self._c_data[7] = (cn_id_source,)

    @property  # get CNN.9
    def assigning_authority_namespace_id(self) -> AssigningAuthority | None:
        """
                id: CNN.9 | len: 20 | use: C | rpt: 1
                ---
                 Assigning Authority is normally expressed as an HD data type, but has been flattened to 3 components here (CNS.9, CNS.10 and CNS.11) in this data type so that it may be fully expressed. Also note that if additional components are added to the HD data type in the future, adjustment will need to be made accordingly to this data type.

        If component 1 is valued, either component 8, or 9, or both 10 and 11, must be valued.
                ---
                return_type: IS: Coded value for user-defined tables
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.9
        """
        return self._c_data[8][0]

    @assigning_authority_namespace_id.setter  # set CNN.9
    def assigning_authority_namespace_id(
        self, assigning_authority: AssigningAuthority | None
    ):
        """
                id: CNN.9 | len: 20 | use: C | rpt: 1
                ---
                 Assigning Authority is normally expressed as an HD data type, but has been flattened to 3 components here (CNS.9, CNS.10 and CNS.11) in this data type so that it may be fully expressed. Also note that if additional components are added to the HD data type in the future, adjustment will need to be made accordingly to this data type.

        If component 1 is valued, either component 8, or 9, or both 10 and 11, must be valued.
                ---
                param_type: IS: Coded value for user-defined tables
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.9
        """
        self._c_data[8] = (assigning_authority,)

    @property  # get CNN.10
    def assigning_authority_universal_id(self) -> ST | None:
        """
        id: CNN.10 | len: 199 | use: C | rpt: 1
        ---
        If CNN.11 is valued, this component must be valued. If component 1 is valued, either component 8, or 9, or both 10 and 11, must be valued.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.10
        """
        return self._c_data[9][0]

    @assigning_authority_universal_id.setter  # set CNN.10
    def assigning_authority_universal_id(self, st: ST | None):
        """
        id: CNN.10 | len: 199 | use: C | rpt: 1
        ---
        If CNN.11 is valued, this component must be valued. If component 1 is valued, either component 8, or 9, or both 10 and 11, must be valued.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.10
        """
        self._c_data[9] = (st,)

    @property  # get CNN.11
    def assigning_authority_universal_id_type(self) -> UniversalIdType | None:
        """
                id: CNN.11 | len: 6 | use: C | rpt: 1
                ---
                If this component is a known UID refer to HL7 Table 0301 - Universal ID type for valid values.

        If CNN.10 is valued, this component must be valued. If component 1 is valued, either component 8, or 9, or both 10 and 11, must be valued.
                ---
                return_type: ID: Coded values for HL7 tables
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.11
        """
        return self._c_data[10][0]

    @assigning_authority_universal_id_type.setter  # set CNN.11
    def assigning_authority_universal_id_type(
        self, universal_id_type: UniversalIdType | None
    ):
        """
                id: CNN.11 | len: 6 | use: C | rpt: 1
                ---
                If this component is a known UID refer to HL7 Table 0301 - Universal ID type for valid values.

        If CNN.10 is valued, this component must be valued. If component 1 is valued, either component 8, or 9, or both 10 and 11, must be valued.
                ---
                param_type: ID: Coded values for HL7 tables
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CNN.11
        """
        self._c_data[10] = (universal_id_type,)
