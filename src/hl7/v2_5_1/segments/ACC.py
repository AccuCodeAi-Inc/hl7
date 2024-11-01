from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..data_types.ST import ST
from ..data_types.XCN import XCN
from ..data_types.XAD import XAD
from ..data_types.TS import TS
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.StateOrProvince import StateOrProvince
from ..tables.AccidentCode import AccidentCode


"""
Accident - ACC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ACC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ACC,
    CE, ID, ST, XCN, XAD, TS
)

acc = ACC(  #  - The ACC segment contains patient information relative to an accident in which the patient has been involved
    accident_date_or_time=None,  # TS(...) 
    accident_code=None,  # CE(...) 
    accident_location=None,  # ST(...) 
    auto_accident_state=None,  # CE(...) 
    accident_job_related_indicator=None,  # ID(...) 
    accident_death_indicator=None,  # ID(...) 
    entered_by=None,  # XCN(...) 
    accident_description=None,  # ST(...) 
    brought_in_by=None,  # ST(...) 
    police_notified_indicator=None,  # ID(...) 
    accident_address=None,  # XAD(...) 
)

-----END SEGMENT::ACC TEMPLATE-----
"""


class ACC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ACC"""
    _hl7_name = """Accident"""
    _hl7_description = """The ACC segment contains patient information relative to an accident in which the patient has been involved"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC"
    _c_length = (26, 250, 25, 250, 1, 12, 250, 25, 80, 1, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "B", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (TS, CE, ST, CE, ID, ID, XCN, ST, ST, ID, XAD,)
    _c_aliases = ("ACC.1", "ACC.2", "ACC.3", "ACC.4", "ACC.5", "ACC.6", "ACC.7", "ACC.8", "ACC.9", "ACC.10", "ACC.11",)
    _c_names = ("Accident Date/Time", "Accident Code", "Accident Location", "Auto Accident State", "Accident Job Related Indicator", "Accident Death Indicator", "Entered By", "Accident Description", "Brought In By", "Police Notified Indicator", "Accident Address",)
    _c_attrs = ("accident_date_or_time", "accident_code", "accident_location", "auto_accident_state", "accident_job_related_indicator", "accident_death_indicator", "entered_by", "accident_description", "brought_in_by", "police_notified_indicator", "accident_address",)
    # fmt: on

    def __init__(
        self,
        accident_date_or_time: TS | None = None,  # ACC.1
        accident_code: AccidentCode | CE | None = None,  # ACC.2
        accident_location: ST | None = None,  # ACC.3
        auto_accident_state: StateOrProvince | CE | None = None,  # ACC.4
        accident_job_related_indicator: YesOrNoIndicator | ID | None = None,  # ACC.5
        accident_death_indicator: YesOrNoIndicator | ID | None = None,  # ACC.6
        entered_by: XCN | None = None,  # ACC.7
        accident_description: ST | None = None,  # ACC.8
        brought_in_by: ST | None = None,  # ACC.9
        police_notified_indicator: YesOrNoIndicator | ID | None = None,  # ACC.10
        accident_address: XAD | None = None,  # ACC.11
    ):
        """
        Accident - `ACC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC>`_
        The ACC segment contains patient information relative to an accident in which the patient has been involved.

        :param accident_date_or_time: Time Stamp (id: ACC.1 | len: 26 | use: O | rpt: 1)
        :param accident_code: Coded Element (id: ACC.2 | len: 250 | use: O | rpt: 1)
        :param accident_location: String Data (id: ACC.3 | len: 25 | use: O | rpt: 1)
        :param auto_accident_state: Coded Element (id: ACC.4 | len: 250 | use: B | rpt: 1)
        :param accident_job_related_indicator: Coded values for HL7 tables (id: ACC.5 | len: 1 | use: O | rpt: 1)
        :param accident_death_indicator: Coded values for HL7 tables (id: ACC.6 | len: 12 | use: O | rpt: 1)
        :param entered_by: Extended Composite ID Number and Name for Persons (id: ACC.7 | len: 250 | use: O | rpt: 1)
        :param accident_description: String Data (id: ACC.8 | len: 25 | use: O | rpt: 1)
        :param brought_in_by: String Data (id: ACC.9 | len: 80 | use: O | rpt: 1)
        :param police_notified_indicator: Coded values for HL7 tables (id: ACC.10 | len: 1 | use: O | rpt: 1)
        :param accident_address: Extended Address (id: ACC.11 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 11
        self.accident_date_or_time = accident_date_or_time
        self.accident_code = accident_code
        self.accident_location = accident_location
        self.auto_accident_state = auto_accident_state
        self.accident_job_related_indicator = accident_job_related_indicator
        self.accident_death_indicator = accident_death_indicator
        self.entered_by = entered_by
        self.accident_description = accident_description
        self.brought_in_by = brought_in_by
        self.police_notified_indicator = police_notified_indicator
        self.accident_address = accident_address

    @property  # get ACC.1
    def accident_date_or_time(self) -> TS | None:
        """
        id: ACC.1 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.1
        """
        return self._c_data[0][0]

    @accident_date_or_time.setter  # set ACC.1
    def accident_date_or_time(self, ts: TS | None):
        """
        id: ACC.1 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.1
        """
        self._c_data[0] = (ts,)

    @property  # get ACC.2
    def accident_code(self) -> AccidentCode | None:
        """
        id: ACC.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.2
        """
        return self._c_data[1][0]

    @accident_code.setter  # set ACC.2
    def accident_code(self, accident_code: AccidentCode | None):
        """
        id: ACC.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.2
        """
        self._c_data[1] = (accident_code,)

    @property  # get ACC.3
    def accident_location(self) -> ST | None:
        """
        id: ACC.3 | len: 25 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.3
        """
        return self._c_data[2][0]

    @accident_location.setter  # set ACC.3
    def accident_location(self, st: ST | None):
        """
        id: ACC.3 | len: 25 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.3
        """
        self._c_data[2] = (st,)

    @property  # get ACC.4
    def auto_accident_state(self) -> StateOrProvince | None:
        """
        id: ACC.4 | len: 250 | use: B | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.4
        """
        return self._c_data[3][0]

    @auto_accident_state.setter  # set ACC.4
    def auto_accident_state(self, state_or_province: StateOrProvince | None):
        """
        id: ACC.4 | len: 250 | use: B | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.4
        """
        self._c_data[3] = (state_or_province,)

    @property  # get ACC.5
    def accident_job_related_indicator(self) -> YesOrNoIndicator | None:
        """
        id: ACC.5 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.5
        """
        return self._c_data[4][0]

    @accident_job_related_indicator.setter  # set ACC.5
    def accident_job_related_indicator(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: ACC.5 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.5
        """
        self._c_data[4] = (yes_or_no_indicator,)

    @property  # get ACC.6
    def accident_death_indicator(self) -> YesOrNoIndicator | None:
        """
        id: ACC.6 | len: 12 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.6
        """
        return self._c_data[5][0]

    @accident_death_indicator.setter  # set ACC.6
    def accident_death_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: ACC.6 | len: 12 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.6
        """
        self._c_data[5] = (yes_or_no_indicator,)

    @property  # get ACC.7
    def entered_by(self) -> XCN | None:
        """
        id: ACC.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.7
        """
        return self._c_data[6][0]

    @entered_by.setter  # set ACC.7
    def entered_by(self, xcn: XCN | None):
        """
        id: ACC.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.7
        """
        self._c_data[6] = (xcn,)

    @property  # get ACC.8
    def accident_description(self) -> ST | None:
        """
        id: ACC.8 | len: 25 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.8
        """
        return self._c_data[7][0]

    @accident_description.setter  # set ACC.8
    def accident_description(self, st: ST | None):
        """
        id: ACC.8 | len: 25 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.8
        """
        self._c_data[7] = (st,)

    @property  # get ACC.9
    def brought_in_by(self) -> ST | None:
        """
        id: ACC.9 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.9
        """
        return self._c_data[8][0]

    @brought_in_by.setter  # set ACC.9
    def brought_in_by(self, st: ST | None):
        """
        id: ACC.9 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.9
        """
        self._c_data[8] = (st,)

    @property  # get ACC.10
    def police_notified_indicator(self) -> YesOrNoIndicator | None:
        """
        id: ACC.10 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.10
        """
        return self._c_data[9][0]

    @police_notified_indicator.setter  # set ACC.10
    def police_notified_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: ACC.10 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.10
        """
        self._c_data[9] = (yes_or_no_indicator,)

    @property  # get ACC.11
    def accident_address(self) -> XAD | None:
        """
        id: ACC.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.11
        """
        return self._c_data[10][0]

    @accident_address.setter  # set ACC.11
    def accident_address(self, xad: XAD | None):
        """
        id: ACC.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ACC.11
        """
        self._c_data[10] = (xad,)
