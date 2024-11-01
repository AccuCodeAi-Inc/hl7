from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ST import ST
from ..data_types.ID import ID
from ..tables.DietCodeSpecificationType import DietCodeSpecificationType


"""
Dietary Orders, Supplements, and Preferences - ODS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ODS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ODS,
    CE, ST, ID
)

ods = ODS(  #  - The ORC sequence items of interest to ODS are ORC-1-order control, ORC-2-placer order number, ORC-3-filler order number, ORC-7-quantity/timing, ORC-9-date/time of transaction, ORC-10-entered by, and ORC-11-verified by
    type=id,  # ID(...)  # Required.
    service_period=None,  # CE(...) 
    diet_supplement_or_preference_code=ce,  # CE(...)  # Required.
    text_instruction=None,  # ST(...) 
)

-----END SEGMENT::ODS TEMPLATE-----
"""


class ODS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ODS"""
    _hl7_name = """Dietary Orders, Supplements, and Preferences"""
    _hl7_description = """The ORC sequence items of interest to ODS are ORC-1-order control, ORC-2-placer order number, ORC-3-filler order number, ORC-7-quantity/timing, ORC-9-date/time of transaction, ORC-10-entered by, and ORC-11-verified by"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODS"
    _c_length = (1, 250, 250, 80,)
    _c_rpt = (1, 10, 20, 2,)
    _c_usage = ("R", "O", "R", "O",)
    _c_components = (ID, CE, CE, ST,)
    _c_aliases = ("ODS.1", "ODS.2", "ODS.3", "ODS.4",)
    _c_names = ("Type", "Service Period", "Diet, Supplement, or Preference Code", "Text Instruction",)
    _c_attrs = ("type", "service_period", "diet_supplement_or_preference_code", "text_instruction",)
    # fmt: on

    def __init__(
        self,
        type: DietCodeSpecificationType | ID,  # ODS.1
        diet_supplement_or_preference_code: CE,  # ODS.3
        service_period: CE | None = None,  # ODS.2
        text_instruction: ST | None = None,  # ODS.4
    ):
        """
        Dietary Orders, Supplements, and Preferences - `ODS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODS>`_
        The ORC sequence items of interest to ODS are ORC-1-order control, ORC-2-placer order number, ORC-3-filler order number, ORC-7-quantity/timing, ORC-9-date/time of transaction, ORC-10-entered by, and ORC-11-verified by. For ORC-1-order control, the values may be New (NW), Cancel (CA), Discontinue Order Request (DC), Change (XO), Hold Order Request (HD), and Release Previous Hold (RL). The HD and RL codes could stop service for a specified length of time. ORC-7-quantity/timing should be used to specify whether an order is continuous or for one service period only. It is also useful for supplements which are part of a diet but only delivered, say, every day at night.

        :param type: Coded values for HL7 tables (id: ODS.1 | len: 1 | use: R | rpt: 1)
        :param service_period: Coded Element (id: ODS.2 | len: 250 | use: O | rpt: 10)
        :param diet_supplement_or_preference_code: Coded Element (id: ODS.3 | len: 250 | use: R | rpt: 20)
        :param text_instruction: String Data (id: ODS.4 | len: 80 | use: O | rpt: 2)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.type = type
        self.service_period = service_period
        self.diet_supplement_or_preference_code = diet_supplement_or_preference_code
        self.text_instruction = text_instruction

    @property  # get ODS.1
    def type(self) -> DietCodeSpecificationType:
        """
        id: ODS.1 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODS.1
        """
        return self._c_data[0][0]

    @type.setter  # set ODS.1
    def type(self, diet_code_specification_type: DietCodeSpecificationType):
        """
        id: ODS.1 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODS.1
        """
        self._c_data[0] = (diet_code_specification_type,)

    @property
    def service_period(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: ODS.2 | len: 250 | use: O | rpt: 10
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODS.2
        """
        return self._c_data[1]

    @service_period.setter  # set ODS.2
    def service_period(self, ce: CE | tuple[CE] | None):
        """
        id: ODS.2 | len: 250 | use: O | rpt: 10
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODS.2
        """
        if isinstance(ce, tuple):
            self._c_data[1] = ce
        else:
            self._c_data[1] = (ce,)

    @property
    def diet_supplement_or_preference_code(self) -> tuple[CE, ...]:
        """
        id: ODS.3 | len: 250 | use: R | rpt: 20
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODS.3
        """
        return self._c_data[2]

    @diet_supplement_or_preference_code.setter  # set ODS.3
    def diet_supplement_or_preference_code(self, ce: CE | tuple[CE]):
        """
        id: ODS.3 | len: 250 | use: R | rpt: 20
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODS.3
        """
        if isinstance(ce, tuple):
            self._c_data[2] = ce
        else:
            self._c_data[2] = (ce,)

    @property
    def text_instruction(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: ODS.4 | len: 80 | use: O | rpt: 2
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODS.4
        """
        return self._c_data[3]

    @text_instruction.setter  # set ODS.4
    def text_instruction(self, st: ST | tuple[ST] | None):
        """
        id: ODS.4 | len: 80 | use: O | rpt: 2
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODS.4
        """
        if isinstance(st, tuple):
            self._c_data[3] = st
        else:
            self._c_data[3] = (st,)
