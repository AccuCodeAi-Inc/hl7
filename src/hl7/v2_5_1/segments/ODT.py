from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..tables.TrayType import TrayType


"""
Diet Tray Instructions - ODT
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ODT TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ODT,
    ST, CE
)

odt = ODT(  #  - This segment addresses tray instructions
    tray_type=ce,  # CE(...)  # Required.
    service_period=None,  # CE(...) 
    text_instruction=None,  # ST(...) 
)

-----END SEGMENT::ODT TEMPLATE-----
"""


class ODT(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ODT"""
    _hl7_name = """Diet Tray Instructions"""
    _hl7_description = """This segment addresses tray instructions"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODT"
    _c_length = (250, 250, 80,)
    _c_rpt = (1, 10, 1,)
    _c_usage = ("R", "O", "O",)
    _c_components = (CE, CE, ST,)
    _c_aliases = ("ODT.1", "ODT.2", "ODT.3",)
    _c_names = ("Tray Type", "Service Period", "Text Instruction",)
    _c_attrs = ("tray_type", "service_period", "text_instruction",)
    # fmt: on

    def __init__(
        self,
        tray_type: TrayType | CE | tuple[TrayType | CE],  # ODT.1
        service_period: CE | tuple[CE] | None = None,  # ODT.2
        text_instruction: ST | tuple[ST] | None = None,  # ODT.3
    ):
        """
        Diet Tray Instructions - `ODT <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODT>`_
        This segment addresses tray instructions. These are independent of diet codes, supplements, and preferences and therefore get separate order numbers.

        :param tray_type: Coded Element (id: ODT.1 | len: 250 | use: R | rpt: 1)
        :param service_period: Coded Element (id: ODT.2 | len: 250 | use: O | rpt: 10)
        :param text_instruction: String Data (id: ODT.3 | len: 80 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.tray_type = tray_type
        self.service_period = service_period
        self.text_instruction = text_instruction

    @property  # get ODT.1
    def tray_type(self) -> TrayType:
        """
        id: ODT.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODT.1
        """
        return self._c_data[0][0]

    @tray_type.setter  # set ODT.1
    def tray_type(self, tray_type: TrayType):
        """
        id: ODT.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODT.1
        """
        self._c_data[0] = (tray_type,)

    @property
    def service_period(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: ODT.2 | len: 250 | use: O | rpt: 10
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODT.2
        """
        return self._c_data[1]

    @service_period.setter  # set ODT.2
    def service_period(self, ce: CE | tuple[CE] | None):
        """
        id: ODT.2 | len: 250 | use: O | rpt: 10
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODT.2
        """
        if isinstance(ce, tuple):
            self._c_data[1] = ce
        else:
            self._c_data[1] = (ce,)

    @property  # get ODT.3
    def text_instruction(self) -> ST | None:
        """
        id: ODT.3 | len: 80 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODT.3
        """
        return self._c_data[2][0]

    @text_instruction.setter  # set ODT.3
    def text_instruction(self, st: ST | None):
        """
        id: ODT.3 | len: 80 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ODT.3
        """
        self._c_data[2] = (st,)
