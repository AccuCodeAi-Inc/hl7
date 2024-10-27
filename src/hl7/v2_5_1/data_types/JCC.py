from __future__ import annotations
from ...base import DataType
from .TX import TX
from .IS import IS
from ..tables.JobCode import JobCode
from ..tables.EmployeeClassification import EmployeeClassification


"""
DataType - JCC
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::JCC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    JCC,
    TX, IS
)

jcc = JCC(  # Job Code/Class - Example 1: Codified job (where 1 represents the code for Administrator and F represents full time) |1^F^Administrator| 
Example 2: Uncodified job (where job codes are not codified and PT represents part time) |^PT^Analyst|
    job_code=None,  # IS(...) 
    job_class=None,  # IS(...) 
    job_description_text=None,  # TX(...) 
)

-----END COMPOSITE_DATA_TYPE::JCC TEMPLATE-----
"""


class JCC(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 292
    _hl7_id = """JCC"""
    _hl7_name = """Job Code/Class"""
    _hl7_description = """Example 1: Codified job (where 1 represents the code for Administrator and F represents full time) |1^F^Administrator| 
Example 2: Uncodified job (where job codes are not codified and PT represents part time) |^PT^Analyst|"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/JCC"
    _c_length = (20, 20, 250,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("O", "O", "O",)
    _c_aliases = ("JCC.1", "JCC.2", "JCC.3",)
    _c_components = (IS, IS, TX,)
    _c_names = ("Job Code", "Job Class", "Job Description Text",)
    _c_attrs = ("job_code", "job_class", "job_description_text",)
    # fmt: on

    def __init__(
        self,
        job_code: JobCode | IS | None = None,  # JCC.1
        job_class: EmployeeClassification | IS | None = None,  # JCC.2
        job_description_text: TX | None = None,  # JCC.3
    ):
        """
                Job Code/Class - `JCC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/JCC>`_
                Example 1: Codified job (where 1 represents the code for Administrator and F represents full time) |1^F^Administrator|
        Example 2: Uncodified job (where job codes are not codified and PT represents part time) |^PT^Analyst|.

                :param job_code: This component contains the persons job code (id: JCC.1 | len: 20 | use: O | rpt: 1)
                :param job_class: This component contains the persons employee classification (id: JCC.2 | len: 20 | use: O | rpt: 1)
                :param job_description_text: This component contains the text of the job description (id: JCC.3 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.job_code = job_code
        self.job_class = job_class
        self.job_description_text = job_description_text

    @property  # get JCC.1
    def job_code(self) -> JobCode | None:
        """
        id: JCC.1 | len: 20 | use: O | rpt: 1
        ---
        This component contains the persons job code. User-defined Table 0327 - Job code is used as the HL7 identifier for the user-defined table of values for this component.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/JCC.1
        """
        return self._c_data[0][0]

    @job_code.setter  # set JCC.1
    def job_code(self, job_code: JobCode | None):
        """
        id: JCC.1 | len: 20 | use: O | rpt: 1
        ---
        This component contains the persons job code. User-defined Table 0327 - Job code is used as the HL7 identifier for the user-defined table of values for this component.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/JCC.1
        """
        self._c_data[0] = (job_code,)

    @property  # get JCC.2
    def job_class(self) -> EmployeeClassification | None:
        """
        id: JCC.2 | len: 20 | use: O | rpt: 1
        ---
        This component contains the persons employee classification. Refer to User-defined Table 0328 - Employee classification for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/JCC.2
        """
        return self._c_data[1][0]

    @job_class.setter  # set JCC.2
    def job_class(self, employee_classification: EmployeeClassification | None):
        """
        id: JCC.2 | len: 20 | use: O | rpt: 1
        ---
        This component contains the persons employee classification. Refer to User-defined Table 0328 - Employee classification for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/JCC.2
        """
        self._c_data[1] = (employee_classification,)

    @property  # get JCC.3
    def job_description_text(self) -> TX | None:
        """
        id: JCC.3 | len: 250 | use: O | rpt: 1
        ---
        This component contains the text of the job description. This will accommodate systems where job descriptions are not codified.
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/JCC.3
        """
        return self._c_data[2][0]

    @job_description_text.setter  # set JCC.3
    def job_description_text(self, tx: TX | None):
        """
        id: JCC.3 | len: 250 | use: O | rpt: 1
        ---
        This component contains the text of the job description. This will accommodate systems where job descriptions are not codified.
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/JCC.3
        """
        self._c_data[2] = (tx,)
