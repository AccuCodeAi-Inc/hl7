from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.ST import ST
from ..data_types.TX import TX


"""
Display Data - DSP
HL7 Version: 2.5.1

-----BEGIN SEGMENT::DSP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DSP,
    SI, ST, TX
)

dsp = DSP(  #  - The DSP segment is used to contain data that has been preformatted by the sender for display
    set_id_dsp=None,  # SI(...) 
    display_level=None,  # SI(...) 
    data_line=tx,  # TX(...)  # Required.
    logical_break_point=None,  # ST(...) 
    result_id=None,  # TX(...) 
)

-----END SEGMENT::DSP TEMPLATE-----
"""


class DSP(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """DSP"""
    _hl7_name = """Display Data"""
    _hl7_description = """The DSP segment is used to contain data that has been preformatted by the sender for display"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSP"
    _c_length = (4, 4, 300, 2, 20,)
    _c_rpt = (1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "R", "O", "O",)
    _c_components = (SI, SI, TX, ST, TX,)
    _c_aliases = ("DSP.1", "DSP.2", "DSP.3", "DSP.4", "DSP.5",)
    _c_names = ("Set ID - DSP", "Display Level", "Data Line", "Logical Break Point", "Result ID",)
    _c_attrs = ("set_id_dsp", "display_level", "data_line", "logical_break_point", "result_id",)
    # fmt: on

    def __init__(
        self,
        data_line: TX | tuple[TX, ...],  # DSP.3
        set_id_dsp: SI | tuple[SI, ...] | None = None,  # DSP.1
        display_level: SI | tuple[SI, ...] | None = None,  # DSP.2
        logical_break_point: ST | tuple[ST, ...] | None = None,  # DSP.4
        result_id: TX | tuple[TX, ...] | None = None,  # DSP.5
    ):
        """
        Display Data - `DSP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSP>`_
        The DSP segment is used to contain data that has been preformatted by the sender for display. The semantic content of the data is lost; the data is simply treated as lines of text.

        :param set_id_dsp: Sequence ID (id: DSP.1 | len: 4 | use: O | rpt: 1)
        :param display_level: Sequence ID (id: DSP.2 | len: 4 | use: O | rpt: 1)
        :param data_line: Text Data (id: DSP.3 | len: 300 | use: R | rpt: 1)
        :param logical_break_point: String Data (id: DSP.4 | len: 2 | use: O | rpt: 1)
        :param result_id: Text Data (id: DSP.5 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.set_id_dsp = set_id_dsp
        self.display_level = display_level
        self.data_line = data_line
        self.logical_break_point = logical_break_point
        self.result_id = result_id

    @property  # get DSP.1
    def set_id_dsp(self) -> SI | None:
        """
        id: DSP.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSP.1
        """
        return self._c_data[0][0]

    @set_id_dsp.setter  # set DSP.1
    def set_id_dsp(self, si: SI | None):
        """
        id: DSP.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSP.1
        """
        self._c_data[0] = (si,)

    @property  # get DSP.2
    def display_level(self) -> SI | None:
        """
        id: DSP.2 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSP.2
        """
        return self._c_data[1][0]

    @display_level.setter  # set DSP.2
    def display_level(self, si: SI | None):
        """
        id: DSP.2 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSP.2
        """
        self._c_data[1] = (si,)

    @property  # get DSP.3
    def data_line(self) -> TX:
        """
        id: DSP.3 | len: 300 | use: R | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSP.3
        """
        return self._c_data[2][0]

    @data_line.setter  # set DSP.3
    def data_line(self, tx: TX):
        """
        id: DSP.3 | len: 300 | use: R | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSP.3
        """
        self._c_data[2] = (tx,)

    @property  # get DSP.4
    def logical_break_point(self) -> ST | None:
        """
        id: DSP.4 | len: 2 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSP.4
        """
        return self._c_data[3][0]

    @logical_break_point.setter  # set DSP.4
    def logical_break_point(self, st: ST | None):
        """
        id: DSP.4 | len: 2 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSP.4
        """
        self._c_data[3] = (st,)

    @property  # get DSP.5
    def result_id(self) -> TX | None:
        """
        id: DSP.5 | len: 20 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSP.5
        """
        return self._c_data[4][0]

    @result_id.setter  # set DSP.5
    def result_id(self, tx: TX | None):
        """
        id: DSP.5 | len: 20 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSP.5
        """
        self._c_data[4] = (tx,)
