from __future__ import annotations
from ...base import DataType
from .CWE import CWE
from .TX import TX
from ..tables.BodySiteModifier import BodySiteModifier
from ..tables.BodySite import BodySite
from ..tables.SpecimenRole import SpecimenRole
from ..tables.AdditiveOrPreservative import AdditiveOrPreservative


"""
DataType - SPS
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::SPS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SPS,
    CWE, TX
)

sps = SPS(  # Specimen Source - This data type identifies the site where the specimen should be obtained or where the service should be performed
    specimen_source_name_or_code=None,  # CWE(...) 
    additives=None,  # CWE(...) 
    specimen_collection_method=None,  # TX(...) 
    body_site=None,  # CWE(...) 
    site_modifier=None,  # CWE(...) 
    collection_method_modifier_code=None,  # CWE(...) 
    specimen_role=None,  # CWE(...) 
)

-----END COMPOSITE_DATA_TYPE::SPS TEMPLATE-----
"""


class SPS(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 4436
    _hl7_id = """SPS"""
    _hl7_name = """Specimen Source"""
    _hl7_description = """This data type identifies the site where the specimen should be obtained or where the service should be performed"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS"
    _c_length = (705, 705, 200, 705, 705, 705, 705,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("SPS.1", "SPS.2", "SPS.3", "SPS.4", "SPS.5", "SPS.6", "SPS.7",)
    _c_components = (CWE, CWE, TX, CWE, CWE, CWE, CWE,)
    _c_names = ("Specimen Source Name Or Code", "Additives", "Specimen Collection Method", "Body Site", "Site Modifier", "Collection Method Modifier Code", "Specimen Role",)
    _c_attrs = ("specimen_source_name_or_code", "additives", "specimen_collection_method", "body_site", "site_modifier", "collection_method_modifier_code", "specimen_role",)
    # fmt: on

    def __init__(
        self,
        specimen_source_name_or_code: CWE | None = None,  # SPS.1
        additives: AdditiveOrPreservative | CWE | None = None,  # SPS.2
        specimen_collection_method: TX | None = None,  # SPS.3
        body_site: BodySite | CWE | None = None,  # SPS.4
        site_modifier: BodySiteModifier | CWE | None = None,  # SPS.5
        collection_method_modifier_code: CWE | None = None,  # SPS.6
        specimen_role: SpecimenRole | CWE | None = None,  # SPS.7
    ):
        """
        Specimen Source - `SPS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPS>`_
        This data type identifies the site where the specimen should be obtained or where the service should be performed.

        :param specimen_source_name_or_code: contains the specimen source name or code (as a CWE data type component) (id: SPS.1 | len: 705 | use: O | rpt: 1)
        :param additives: identifies an additive introduced to the specimen before or at the time of collection (id: SPS.2 | len: 705 | use: O | rpt: 1)
        :param specimen_collection_method: describes the method of collection when that information is a part of the order (id: SPS.3 | len: 200 | use: O | rpt: 1)
        :param body_site: This component specifies the body site from which the specimen was obtained (id: SPS.4 | len: 705 | use: O | rpt: 1)
        :param site_modifier: modifies body site (id: SPS.5 | len: 705 | use: O | rpt: 1)
        :param collection_method_modifier_code: I ndicates whether the specimen is frozen as part of the collection method (id: SPS.6 | len: 705 | use: O | rpt: 1)
        :param specimen_role: indicates the role of the sample (id: SPS.7 | len: 705 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.specimen_source_name_or_code = specimen_source_name_or_code
        self.additives = additives
        self.specimen_collection_method = specimen_collection_method
        self.body_site = body_site
        self.site_modifier = site_modifier
        self.collection_method_modifier_code = collection_method_modifier_code
        self.specimen_role = specimen_role

    @property  # get SPS.1
    def specimen_source_name_or_code(self) -> CWE | None:
        """
        id: SPS.1 | len: 705 | use: O | rpt: 1
        ---
        contains the specimen source name or code (as a CWE data type component). (Even in the case of observations whose name implies the source, a source may be required, e.g., blood culture-heart blood.)
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.1
        """
        return self._c_data[0][0]

    @specimen_source_name_or_code.setter  # set SPS.1
    def specimen_source_name_or_code(self, cwe: CWE | None):
        """
        id: SPS.1 | len: 705 | use: O | rpt: 1
        ---
        contains the specimen source name or code (as a CWE data type component). (Even in the case of observations whose name implies the source, a source may be required, e.g., blood culture-heart blood.)
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.1
        """
        self._c_data[0] = (cwe,)

    @property  # get SPS.2
    def additives(self) -> CWE | None:
        """
        id: SPS.2 | len: 705 | use: O | rpt: 1
        ---
        identifies an additive introduced to the specimen before or at the time of collection. Refer to HL7 Table0371 - Additive in chapter 7 for valid values. The tables values are taken from NCCLS AUTO4. The value set can be extended with user specific values.
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.2
        """
        return self._c_data[1][0]

    @additives.setter  # set SPS.2
    def additives(self, cwe: CWE | None):
        """
        id: SPS.2 | len: 705 | use: O | rpt: 1
        ---
        identifies an additive introduced to the specimen before or at the time of collection. Refer to HL7 Table0371 - Additive in chapter 7 for valid values. The tables values are taken from NCCLS AUTO4. The value set can be extended with user specific values.
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.2
        """
        self._c_data[1] = (cwe,)

    @property  # get SPS.3
    def specimen_collection_method(self) -> TX | None:
        """
        id: SPS.3 | len: 200 | use: O | rpt: 1
        ---
        describes the method of collection when that information is a part of the order. When the method of collection is logically an observation result, it should be included as a result segment (i.e., OBX segment).
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.3
        """
        return self._c_data[2][0]

    @specimen_collection_method.setter  # set SPS.3
    def specimen_collection_method(self, tx: TX | None):
        """
        id: SPS.3 | len: 200 | use: O | rpt: 1
        ---
        describes the method of collection when that information is a part of the order. When the method of collection is logically an observation result, it should be included as a result segment (i.e., OBX segment).
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.3
        """
        self._c_data[2] = (tx,)

    @property  # get SPS.4
    def body_site(self) -> CWE | None:
        """
        id: SPS.4 | len: 705 | use: O | rpt: 1
        ---
        This component specifies the body site from which the specimen was obtained. A nationally recognized coding system is to be used for this field. Valid coding sources for this field include:
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.4
        """
        return self._c_data[3][0]

    @body_site.setter  # set SPS.4
    def body_site(self, cwe: CWE | None):
        """
        id: SPS.4 | len: 705 | use: O | rpt: 1
        ---
        This component specifies the body site from which the specimen was obtained. A nationally recognized coding system is to be used for this field. Valid coding sources for this field include:
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.4
        """
        self._c_data[3] = (cwe,)

    @property  # get SPS.5
    def site_modifier(self) -> CWE | None:
        """
        id: SPS.5 | len: 705 | use: O | rpt: 1
        ---
        modifies body site. For example, the site could be antecubital fossa, and the site modifier right. Refer to HL7 Table 0495 Body Site Modifier for allowed values.
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.5
        """
        return self._c_data[4][0]

    @site_modifier.setter  # set SPS.5
    def site_modifier(self, cwe: CWE | None):
        """
        id: SPS.5 | len: 705 | use: O | rpt: 1
        ---
        modifies body site. For example, the site could be antecubital fossa, and the site modifier right. Refer to HL7 Table 0495 Body Site Modifier for allowed values.
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.5
        """
        self._c_data[4] = (cwe,)

    @property  # get SPS.6
    def collection_method_modifier_code(self) -> CWE | None:
        """
        id: SPS.6 | len: 705 | use: O | rpt: 1
        ---
        I ndicates whether the specimen is frozen as part of the collection method. Suggested values are F (Frozen); R (Refrigerated). If the component is blank, the specimen is assumed to be at room temperature.
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.6
        """
        return self._c_data[5][0]

    @collection_method_modifier_code.setter  # set SPS.6
    def collection_method_modifier_code(self, cwe: CWE | None):
        """
        id: SPS.6 | len: 705 | use: O | rpt: 1
        ---
        I ndicates whether the specimen is frozen as part of the collection method. Suggested values are F (Frozen); R (Refrigerated). If the component is blank, the specimen is assumed to be at room temperature.
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.6
        """
        self._c_data[5] = (cwe,)

    @property  # get SPS.7
    def specimen_role(self) -> CWE | None:
        """
        id: SPS.7 | len: 705 | use: O | rpt: 1
        ---
        indicates the role of the sample. Refer to User-defined Table 0369 - Specimen role for suggested values. Each of these values is normally identifiable by the systems and its components and can influence processing and data management related to the specimen.
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.7
        """
        return self._c_data[6][0]

    @specimen_role.setter  # set SPS.7
    def specimen_role(self, cwe: CWE | None):
        """
        id: SPS.7 | len: 705 | use: O | rpt: 1
        ---
        indicates the role of the sample. Refer to User-defined Table 0369 - Specimen role for suggested values. Each of these values is normally identifiable by the systems and its components and can influence processing and data management related to the specimen.
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPS.7
        """
        self._c_data[6] = (cwe,)
