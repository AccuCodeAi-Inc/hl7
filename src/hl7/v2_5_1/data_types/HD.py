from __future__ import annotations
from ...base import DataType
from .ID import ID
from .ST import ST
from .IS import IS
from ..tables.NamespaceId import NamespaceId
from ..tables.UniversalIdType import UniversalIdType


"""
DataType - HD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::HD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    HD,
    ID, ST, IS
)

hd = HD(  # Hierarchic Designator - The basic definition of the HD is that it identifies an (administrative or system or application or other) entity that has responsibility for managing or assigning a defined set of instance identifiers (such as placer or filler number, patient identifiers, provider identifiers, etc
    namespace_id=None,  # IS(...) 
    universal_id=None,  # ST(...) 
    universal_id_type=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::HD TEMPLATE-----
"""


class HD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 227
    _hl7_id = """HD"""
    _hl7_name = """Hierarchic Designator"""
    _hl7_description = """The basic definition of the HD is that it identifies an (administrative or system or application or other) entity that has responsibility for managing or assigning a defined set of instance identifiers (such as placer or filler number, patient identifiers, provider identifiers, etc"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/HD"
    _c_length = (20, 199, 6,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("O", "C", "C",)
    _c_aliases = ("HD.1", "HD.2", "HD.3",)
    _c_components = (IS, ST, ID,)
    _c_names = ("Namespace Id", "Universal Id", "Universal Id Type",)
    _c_attrs = ("namespace_id", "universal_id", "universal_id_type",)
    # fmt: on

    def __init__(
        self,
        namespace_id: NamespaceId | IS | None = None,  # HD.1
        universal_id: ST | None = None,  # HD.2
        universal_id_type: UniversalIdType | ID | None = None,  # HD.3
    ):
        """
                Hierarchic Designator - `HD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/HD>`_
                The basic definition of the HD is that it identifies an (administrative or system or application or other) entity that has responsibility for managing or assigning a defined set of instance identifiers (such as placer or filler number, patient identifiers, provider identifiers, etc.). This entity could be a particular health care application such as a registration system that assigns patient identifiers, a governmental entity such as a licensing authority that assigns professional identifiers or drivers license numbers, or a facility where such identifiers are assigned.

        Note:  The HD is used in fields that in earlier versions of HL7 used the IS data type. Thus, a single component HD (only the first component valued) will look like a simple IS data type for older systems expecting a single component in the place of the HD data type.

        If the first component for the HD data type is present, the second and third components are optional. If the third component is present, then the second must also be present (although in this case the first is optional). The second and third components must either both be valued (both non-null), or both be not valued (both null).

        This means that if all three components of the HD are valued, the entity identified by the first component is the same as the entity identified by components two and three taken together. However, implementers may choose, by site agreement, to specify that if all three components of the HD are valued, the first component defines a member in the set defined by the second and third components.

                :param namespace_id: Namespace ID is used as the HL7 identifier for the user-defined table of values for this component (id: HD.1 | len: 20 | use: O | rpt: 1)
                :param universal_id: The HDs second component, <universal ID> (UID), is a string formatted according to the scheme defined by the third component, <universal ID type> (UID type) (id: HD.2 | len: 199 | use: C | rpt: 1)
                :param universal_id_type: The third component governs the interpretation of the second component of the HD (id: HD.3 | len: 6 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.namespace_id = namespace_id
        self.universal_id = universal_id
        self.universal_id_type = universal_id_type

    @property  # get HD.1
    def namespace_id(self) -> NamespaceId | None:
        """
                id: HD.1 | len: 20 | use: O | rpt: 1
                ---
                Namespace ID is used as the HL7 identifier for the user-defined table of values for this component.

        Note: When the HD is used in a given segment (either as a field or as a component of another data type) this table may be re-defined (given a different user-defined table number and name) by the technical committee responsible for that segment.
                ---
                return_type: IS: Coded value for user-defined tables
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/HD.1
        """
        return self._c_data[0][0]

    @namespace_id.setter  # set HD.1
    def namespace_id(self, namespace_id: NamespaceId | None):
        """
                id: HD.1 | len: 20 | use: O | rpt: 1
                ---
                Namespace ID is used as the HL7 identifier for the user-defined table of values for this component.

        Note: When the HD is used in a given segment (either as a field or as a component of another data type) this table may be re-defined (given a different user-defined table number and name) by the technical committee responsible for that segment.
                ---
                param_type: IS: Coded value for user-defined tables
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/HD.1
        """
        self._c_data[0] = (namespace_id,)

    @property  # get HD.2
    def universal_id(self) -> ST | None:
        """
        id: HD.2 | len: 199 | use: C | rpt: 1
        ---
        The HDs second component, <universal ID> (UID), is a string formatted according to the scheme defined by the third component, <universal ID type> (UID type). The UID is intended to be unique over time within the UID type. It is rigorously defined. Each UID must belong to one of the specifically enumerated schemes for constructing UIDs (defined by the UID type). The UID (second component) must follow the syntactic rules of the particular universal identifier scheme (defined by the third component). Note that these syntactic rules are not defined within HL7 but are defined by the rules of the particular universal identifier scheme (defined by the third component).
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/HD.2
        """
        return self._c_data[1][0]

    @universal_id.setter  # set HD.2
    def universal_id(self, st: ST | None):
        """
        id: HD.2 | len: 199 | use: C | rpt: 1
        ---
        The HDs second component, <universal ID> (UID), is a string formatted according to the scheme defined by the third component, <universal ID type> (UID type). The UID is intended to be unique over time within the UID type. It is rigorously defined. Each UID must belong to one of the specifically enumerated schemes for constructing UIDs (defined by the UID type). The UID (second component) must follow the syntactic rules of the particular universal identifier scheme (defined by the third component). Note that these syntactic rules are not defined within HL7 but are defined by the rules of the particular universal identifier scheme (defined by the third component).
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/HD.2
        """
        self._c_data[1] = (st,)

    @property  # get HD.3
    def universal_id_type(self) -> UniversalIdType | None:
        """
        id: HD.3 | len: 6 | use: C | rpt: 1
        ---
        The third component governs the interpretation of the second component of the HD. If the third component is a known UID refer to HL7 Table 0301 - Universal ID type for valid values, then the second component is a universal ID of that type.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/HD.3
        """
        return self._c_data[2][0]

    @universal_id_type.setter  # set HD.3
    def universal_id_type(self, universal_id_type: UniversalIdType | None):
        """
        id: HD.3 | len: 6 | use: C | rpt: 1
        ---
        The third component governs the interpretation of the second component of the HD. If the third component is a known UID refer to HL7 Table 0301 - Universal ID type for valid values, then the second component is a universal ID of that type.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/HD.3
        """
        self._c_data[2] = (universal_id_type,)
