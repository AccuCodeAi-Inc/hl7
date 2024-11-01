from __future__ import annotations
from ...base import DataType
from .CE import CE
from .ID import ID
from ..tables.VersionId import VersionId
from ..tables.CountryCode import CountryCode


"""
DataType - VID
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::VID TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    VID,
    CE, ID
)

vid = VID(  # Version Identifier - 
    version_id=None,  # ID(...) 
    internationalization_code=None,  # CE(...) 
    international_version_id=None,  # CE(...) 
)

-----END COMPOSITE_DATA_TYPE::VID TEMPLATE-----
"""


class VID(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 973
    _hl7_id = """VID"""
    _hl7_name = """Version Identifier"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VID"
    _c_length = (5, 483, 483,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("O", "O", "O",)
    _c_aliases = ("VID.1", "VID.2", "VID.3",)
    _c_components = (ID, CE, CE,)
    _c_names = ("Version Id", "Internationalization Code", "International Version Id",)
    _c_attrs = ("version_id", "internationalization_code", "international_version_id",)
    # fmt: on

    def __init__(
        self,
        version_id: VersionId | ID | tuple[VersionId | ID, ...] | None = None,  # VID.1
        internationalization_code: CountryCode
        | CE
        | tuple[CountryCode | CE, ...]
        | None = None,  # VID.2
        international_version_id: CE | tuple[CE, ...] | None = None,  # VID.3
    ):
        """
        Version Identifier - `VID <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VID>`_


        :param version_id: Used to identify the HL7 version (id: VID.1 | len: 5 | use: O | rpt: 1)
        :param internationalization_code: Used to identify the international affiliate country code (id: VID.2 | len: 483 | use: O | rpt: 1)
        :param international_version_id: This field component identifies international affiliates version; it is especially important when the international affiliate has more than a single local version associated with a single US version (id: VID.3 | len: 483 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.version_id = version_id
        self.internationalization_code = internationalization_code
        self.international_version_id = international_version_id

    @property  # get VID.1
    def version_id(self) -> VersionId | None:
        """
        id: VID.1 | len: 5 | use: O | rpt: 1
        ---
        Used to identify the HL7 version. Refer to HL7 Table 0104 - Version ID in section 2.15.9.12 for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VID.1
        """
        return self._c_data[0][0]

    @version_id.setter  # set VID.1
    def version_id(self, version_id: VersionId | None):
        """
        id: VID.1 | len: 5 | use: O | rpt: 1
        ---
        Used to identify the HL7 version. Refer to HL7 Table 0104 - Version ID in section 2.15.9.12 for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VID.1
        """
        self._c_data[0] = (version_id,)

    @property  # get VID.2
    def internationalization_code(self) -> CE | None:
        """
        id: VID.2 | len: 483 | use: O | rpt: 1
        ---
        Used to identify the international affiliate country code. The values to be used are those of ISO 3166 -1:1977. The ISO 3166 table has three separate forms of the country code: HL7 specifies that the 3-character (alphabetic) form be used for the country code.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VID.2
        """
        return self._c_data[1][0]

    @internationalization_code.setter  # set VID.2
    def internationalization_code(self, ce: CE | None):
        """
        id: VID.2 | len: 483 | use: O | rpt: 1
        ---
        Used to identify the international affiliate country code. The values to be used are those of ISO 3166 -1:1977. The ISO 3166 table has three separate forms of the country code: HL7 specifies that the 3-character (alphabetic) form be used for the country code.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VID.2
        """
        self._c_data[1] = (ce,)

    @property  # get VID.3
    def international_version_id(self) -> CE | None:
        """
        id: VID.3 | len: 483 | use: O | rpt: 1
        ---
        This field component identifies international affiliates version; it is especially important when the international affiliate has more than a single local version associated with a single US version.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VID.3
        """
        return self._c_data[2][0]

    @international_version_id.setter  # set VID.3
    def international_version_id(self, ce: CE | None):
        """
        id: VID.3 | len: 483 | use: O | rpt: 1
        ---
        This field component identifies international affiliates version; it is especially important when the international affiliate has more than a single local version associated with a single US version.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VID.3
        """
        self._c_data[2] = (ce,)
