from __future__ import annotations
from ...base import DataType
from .IS import IS
from .ID import ID
from .TS import TS
from ..tables.CertificationPatientType import CertificationPatientType
from ..tables.YesOrNoIndicator import YesOrNoIndicator


"""
DataType - ICD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::ICD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ICD,
    IS, ID, TS
)

icd = ICD(  # Insurance Certification Definition - This data type specifies whether insurance certification is required for particular patient types, and the time window for obtaining the certification
    certification_patient_type=None,  # IS(...) 
    certification_required=id,  # ID(...)  # Required.
    date_or_time_certification_required=None,  # TS(...) 
)

-----END COMPOSITE_DATA_TYPE::ICD TEMPLATE-----
"""


class ICD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 40
    _hl7_id = """ICD"""
    _hl7_name = """Insurance Certification Definition"""
    _hl7_description = """This data type specifies whether insurance certification is required for particular patient types, and the time window for obtaining the certification"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ICD"
    _c_length = (11, 1, 26,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("O", "R", "O",)
    _c_aliases = ("ICD.1", "ICD.2", "ICD.3",)
    _c_components = (IS, ID, TS,)
    _c_names = ("Certification Patient Type", "Certification Required", "Date/Time Certification Required",)
    _c_attrs = ("certification_patient_type", "certification_required", "date_or_time_certification_required",)
    # fmt: on

    def __init__(
        self,
        certification_required: YesOrNoIndicator | ID,  # ICD.2
        certification_patient_type: CertificationPatientType
        | IS
        | None = None,  # ICD.1
        date_or_time_certification_required: TS | None = None,  # ICD.3
    ):
        """
        Insurance Certification Definition - `ICD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ICD>`_
        This data type specifies whether insurance certification is required for particular patient types, and the time window for obtaining the certification.

        :param certification_patient_type: Specifies the category or type of patient for which this certification is requested (id: ICD.1 | len: 11 | use: O | rpt: 1)
        :param certification_required: Specifies whether or not a certification is required (id: ICD.2 | len: 1 | use: R | rpt: 1)
        :param date_or_time_certification_required: The date/time by which the certification must be obtained (id: ICD.3 | len: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.certification_patient_type = certification_patient_type
        self.certification_required = certification_required
        self.date_or_time_certification_required = date_or_time_certification_required

    @property  # get ICD.1
    def certification_patient_type(self) -> CertificationPatientType | None:
        """
        id: ICD.1 | len: 11 | use: O | rpt: 1
        ---
        Specifies the category or type of patient for which this certification is requested. Refer to User-defined Table 0150 - Certification patient type for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ICD.1
        """
        return self._c_data[0][0]

    @certification_patient_type.setter  # set ICD.1
    def certification_patient_type(
        self, certification_patient_type: CertificationPatientType | None
    ):
        """
        id: ICD.1 | len: 11 | use: O | rpt: 1
        ---
        Specifies the category or type of patient for which this certification is requested. Refer to User-defined Table 0150 - Certification patient type for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ICD.1
        """
        self._c_data[0] = (certification_patient_type,)

    @property  # get ICD.2
    def certification_required(self) -> YesOrNoIndicator:
        """
        id: ICD.2 | len: 1 | use: R | rpt: 1
        ---
        Specifies whether or not a certification is required. Refer to HL7 table 0136 - Yes/no indicator for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ICD.2
        """
        return self._c_data[1][0]

    @certification_required.setter  # set ICD.2
    def certification_required(self, yes_or_no_indicator: YesOrNoIndicator):
        """
        id: ICD.2 | len: 1 | use: R | rpt: 1
        ---
        Specifies whether or not a certification is required. Refer to HL7 table 0136 - Yes/no indicator for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ICD.2
        """
        self._c_data[1] = (yes_or_no_indicator,)

    @property  # get ICD.3
    def date_or_time_certification_required(self) -> TS | None:
        """
        id: ICD.3 | len: 26 | use: O | rpt: 1
        ---
        The date/time by which the certification must be obtained.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ICD.3
        """
        return self._c_data[2][0]

    @date_or_time_certification_required.setter  # set ICD.3
    def date_or_time_certification_required(self, ts: TS | None):
        """
        id: ICD.3 | len: 26 | use: O | rpt: 1
        ---
        The date/time by which the certification must be obtained.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ICD.3
        """
        self._c_data[2] = (ts,)
