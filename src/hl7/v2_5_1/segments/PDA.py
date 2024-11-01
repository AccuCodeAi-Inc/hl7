from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.PL import PL
from ..data_types.DR import DR
from ..data_types.XCN import XCN
from ..data_types.CE import CE
from ..tables.YesOrNoIndicator import YesOrNoIndicator


"""
Patient Death and Autopsy - PDA
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PDA TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PDA,
    TS, ID, PL, DR, XCN, CE
)

pda = PDA(  #  - This segment carries information on a patients death and possible autopsy
    death_cause_code=None,  # CE(...) 
    death_location=None,  # PL(...) 
    death_certified_indicator=None,  # ID(...) 
    death_certificate_signed_date_or_time=None,  # TS(...) 
    death_certified_by=None,  # XCN(...) 
    autopsy_indicator=None,  # ID(...) 
    autopsy_start_and_end_date_or_time=None,  # DR(...) 
    autopsy_performed_by=None,  # XCN(...) 
    coroner_indicator=None,  # ID(...) 
)

-----END SEGMENT::PDA TEMPLATE-----
"""


class PDA(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PDA"""
    _hl7_name = """Patient Death and Autopsy"""
    _hl7_description = """This segment carries information on a patients death and possible autopsy"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PDA"
    _c_length = (250, 80, 1, 26, 250, 1, 53, 250, 1,)
    _c_rpt = (65535, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, PL, ID, TS, XCN, ID, DR, XCN, ID,)
    _c_aliases = ("PDA.1", "PDA.2", "PDA.3", "PDA.4", "PDA.5", "PDA.6", "PDA.7", "PDA.8", "PDA.9",)
    _c_names = ("Death Cause Code", "Death Location", "Death Certified Indicator", "Death Certificate Signed Date/Time", "Death Certified By", "Autopsy Indicator", "Autopsy Start and End Date/Time", "Autopsy Performed By", "Coroner Indicator",)
    _c_attrs = ("death_cause_code", "death_location", "death_certified_indicator", "death_certificate_signed_date_or_time", "death_certified_by", "autopsy_indicator", "autopsy_start_and_end_date_or_time", "autopsy_performed_by", "coroner_indicator",)
    # fmt: on

    def __init__(
        self,
        death_cause_code: CE | tuple[CE] | None = None,  # PDA.1
        death_location: PL | tuple[PL] | None = None,  # PDA.2
        death_certified_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # PDA.3
        death_certificate_signed_date_or_time: TS | tuple[TS] | None = None,  # PDA.4
        death_certified_by: XCN | tuple[XCN] | None = None,  # PDA.5
        autopsy_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # PDA.6
        autopsy_start_and_end_date_or_time: DR | tuple[DR] | None = None,  # PDA.7
        autopsy_performed_by: XCN | tuple[XCN] | None = None,  # PDA.8
        coroner_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # PDA.9
    ):
        """
        Patient Death and Autopsy - `PDA <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PDA>`_
        This segment carries information on a patients death and possible autopsy.

        :param death_cause_code: Coded Element (id: PDA.1 | len: 250 | use: O | rpt: *)
        :param death_location: Person Location (id: PDA.2 | len: 80 | use: O | rpt: 1)
        :param death_certified_indicator: Coded values for HL7 tables (id: PDA.3 | len: 1 | use: O | rpt: 1)
        :param death_certificate_signed_date_or_time: Time Stamp (id: PDA.4 | len: 26 | use: O | rpt: 1)
        :param death_certified_by: Extended Composite ID Number and Name for Persons (id: PDA.5 | len: 250 | use: O | rpt: 1)
        :param autopsy_indicator: Coded values for HL7 tables (id: PDA.6 | len: 1 | use: O | rpt: 1)
        :param autopsy_start_and_end_date_or_time: Date/Time Range (id: PDA.7 | len: 53 | use: O | rpt: 1)
        :param autopsy_performed_by: Extended Composite ID Number and Name for Persons (id: PDA.8 | len: 250 | use: O | rpt: 1)
        :param coroner_indicator: Coded values for HL7 tables (id: PDA.9 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.death_cause_code = death_cause_code
        self.death_location = death_location
        self.death_certified_indicator = death_certified_indicator
        self.death_certificate_signed_date_or_time = (
            death_certificate_signed_date_or_time
        )
        self.death_certified_by = death_certified_by
        self.autopsy_indicator = autopsy_indicator
        self.autopsy_start_and_end_date_or_time = autopsy_start_and_end_date_or_time
        self.autopsy_performed_by = autopsy_performed_by
        self.coroner_indicator = coroner_indicator

    @property
    def death_cause_code(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: PDA.1 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.1
        """
        return self._c_data[0]

    @death_cause_code.setter  # set PDA.1
    def death_cause_code(self, ce: CE | tuple[CE] | None):
        """
        id: PDA.1 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.1
        """
        if isinstance(ce, tuple):
            self._c_data[0] = ce
        else:
            self._c_data[0] = (ce,)

    @property  # get PDA.2
    def death_location(self) -> PL | None:
        """
        id: PDA.2 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.2
        """
        return self._c_data[1][0]

    @death_location.setter  # set PDA.2
    def death_location(self, pl: PL | None):
        """
        id: PDA.2 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.2
        """
        self._c_data[1] = (pl,)

    @property  # get PDA.3
    def death_certified_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PDA.3 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.3
        """
        return self._c_data[2][0]

    @death_certified_indicator.setter  # set PDA.3
    def death_certified_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PDA.3 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.3
        """
        self._c_data[2] = (yes_or_no_indicator,)

    @property  # get PDA.4
    def death_certificate_signed_date_or_time(self) -> TS | None:
        """
        id: PDA.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.4
        """
        return self._c_data[3][0]

    @death_certificate_signed_date_or_time.setter  # set PDA.4
    def death_certificate_signed_date_or_time(self, ts: TS | None):
        """
        id: PDA.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.4
        """
        self._c_data[3] = (ts,)

    @property  # get PDA.5
    def death_certified_by(self) -> XCN | None:
        """
        id: PDA.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.5
        """
        return self._c_data[4][0]

    @death_certified_by.setter  # set PDA.5
    def death_certified_by(self, xcn: XCN | None):
        """
        id: PDA.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.5
        """
        self._c_data[4] = (xcn,)

    @property  # get PDA.6
    def autopsy_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PDA.6 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.6
        """
        return self._c_data[5][0]

    @autopsy_indicator.setter  # set PDA.6
    def autopsy_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PDA.6 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.6
        """
        self._c_data[5] = (yes_or_no_indicator,)

    @property  # get PDA.7
    def autopsy_start_and_end_date_or_time(self) -> DR | None:
        """
        id: PDA.7 | len: 53 | use: O | rpt: 1
        ---
        return_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.7
        """
        return self._c_data[6][0]

    @autopsy_start_and_end_date_or_time.setter  # set PDA.7
    def autopsy_start_and_end_date_or_time(self, dr: DR | None):
        """
        id: PDA.7 | len: 53 | use: O | rpt: 1
        ---
        param_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.7
        """
        self._c_data[6] = (dr,)

    @property  # get PDA.8
    def autopsy_performed_by(self) -> XCN | None:
        """
        id: PDA.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.8
        """
        return self._c_data[7][0]

    @autopsy_performed_by.setter  # set PDA.8
    def autopsy_performed_by(self, xcn: XCN | None):
        """
        id: PDA.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.8
        """
        self._c_data[7] = (xcn,)

    @property  # get PDA.9
    def coroner_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PDA.9 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.9
        """
        return self._c_data[8][0]

    @coroner_indicator.setter  # set PDA.9
    def coroner_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PDA.9 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDA.9
        """
        self._c_data[8] = (yes_or_no_indicator,)
