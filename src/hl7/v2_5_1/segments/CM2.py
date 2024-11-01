from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.SI import SI
from ..data_types.CE import CE


"""
Clinical Study Schedule Master - CM2
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CM2 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CM2,
    ST, SI, CE
)

cm2 = CM2(  #  - The Clinical Study Schedule Master (CM2) contains the information about the scheduled time points for study or phase-related treatment or evaluation events
    set_id_cm2=None,  # SI(...) 
    scheduled_time_point=ce,  # CE(...)  # Required.
    description_of_time_point=None,  # ST(...) 
    events_scheduled_this_time_point=ce,  # CE(...)  # Required.
)

-----END SEGMENT::CM2 TEMPLATE-----
"""


class CM2(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CM2"""
    _hl7_name = """Clinical Study Schedule Master"""
    _hl7_description = """The Clinical Study Schedule Master (CM2) contains the information about the scheduled time points for study or phase-related treatment or evaluation events"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM2"
    _c_length = (4, 250, 300, 250,)
    _c_rpt = (1, 1, 1, 200,)
    _c_usage = ("O", "R", "O", "R",)
    _c_components = (SI, CE, ST, CE,)
    _c_aliases = ("CM2.1", "CM2.2", "CM2.3", "CM2.4",)
    _c_names = ("Set ID - CM2", "Scheduled Time Point", "Description of Time Point", "Events Scheduled This Time Point",)
    _c_attrs = ("set_id_cm2", "scheduled_time_point", "description_of_time_point", "events_scheduled_this_time_point",)
    # fmt: on

    def __init__(
        self,
        scheduled_time_point: CE | tuple[CE],  # CM2.2
        events_scheduled_this_time_point: CE | tuple[CE],  # CM2.4
        set_id_cm2: SI | tuple[SI] | None = None,  # CM2.1
        description_of_time_point: ST | tuple[ST] | None = None,  # CM2.3
    ):
        """
        Clinical Study Schedule Master - `CM2 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM2>`_
        The Clinical Study Schedule Master (CM2) contains the information about the scheduled time points for study or phase-related treatment or evaluation events.  The fact that a patient has data satisfying a scheduled time point is sent in the CSS segment, sequence 2.  The CM2 segment describes the scheduled time points in general.

        :param set_id_cm2: Sequence ID (id: CM2.1 | len: 4 | use: O | rpt: 1)
        :param scheduled_time_point: Coded Element (id: CM2.2 | len: 250 | use: R | rpt: 1)
        :param description_of_time_point: String Data (id: CM2.3 | len: 300 | use: O | rpt: 1)
        :param events_scheduled_this_time_point: Coded Element (id: CM2.4 | len: 250 | use: R | rpt: 200)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.set_id_cm2 = set_id_cm2
        self.scheduled_time_point = scheduled_time_point
        self.description_of_time_point = description_of_time_point
        self.events_scheduled_this_time_point = events_scheduled_this_time_point

    @property  # get CM2.1
    def set_id_cm2(self) -> SI | None:
        """
        id: CM2.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM2.1
        """
        return self._c_data[0][0]

    @set_id_cm2.setter  # set CM2.1
    def set_id_cm2(self, si: SI | None):
        """
        id: CM2.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM2.1
        """
        self._c_data[0] = (si,)

    @property  # get CM2.2
    def scheduled_time_point(self) -> CE:
        """
        id: CM2.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM2.2
        """
        return self._c_data[1][0]

    @scheduled_time_point.setter  # set CM2.2
    def scheduled_time_point(self, ce: CE):
        """
        id: CM2.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM2.2
        """
        self._c_data[1] = (ce,)

    @property  # get CM2.3
    def description_of_time_point(self) -> ST | None:
        """
        id: CM2.3 | len: 300 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM2.3
        """
        return self._c_data[2][0]

    @description_of_time_point.setter  # set CM2.3
    def description_of_time_point(self, st: ST | None):
        """
        id: CM2.3 | len: 300 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM2.3
        """
        self._c_data[2] = (st,)

    @property
    def events_scheduled_this_time_point(self) -> tuple[CE, ...]:
        """
        id: CM2.4 | len: 250 | use: R | rpt: 200
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM2.4
        """
        return self._c_data[3]

    @events_scheduled_this_time_point.setter  # set CM2.4
    def events_scheduled_this_time_point(self, ce: CE | tuple[CE]):
        """
        id: CM2.4 | len: 250 | use: R | rpt: 200
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CM2.4
        """
        if isinstance(ce, tuple):
            self._c_data[3] = ce
        else:
            self._c_data[3] = (ce,)
