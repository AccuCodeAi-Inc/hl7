from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SCV import SCV
from ..data_types.NM import NM
from ..tables.TimeSelectionCriteriaParameterClassCodes import (
    TimeSelectionCriteriaParameterClassCodes,
)


"""
Appointment Preferences - APR
HL7 Version: 2.5.1

-----BEGIN SEGMENT::APR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    APR,
    SCV, NM
)

apr = APR(  #  - The APR segment contains parameters and preference specifications used for requesting appointments in the SRM message
    time_selection_criteria=None,  # SCV(...) 
    resource_selection_criteria=None,  # SCV(...) 
    location_selection_criteria=None,  # SCV(...) 
    slot_spacing_criteria=None,  # NM(...) 
    filler_override_criteria=None,  # SCV(...) 
)

-----END SEGMENT::APR TEMPLATE-----
"""


class APR(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """APR"""
    _hl7_name = """Appointment Preferences"""
    _hl7_description = """The APR segment contains parameters and preference specifications used for requesting appointments in the SRM message"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR"
    _c_length = (80, 80, 80, 5, 80,)
    _c_rpt = (65535, 65535, 65535, 1, 65535,)
    _c_usage = ("O", "O", "O", "O", "O",)
    _c_components = (SCV, SCV, SCV, NM, SCV,)
    _c_aliases = ("APR.1", "APR.2", "APR.3", "APR.4", "APR.5",)
    _c_names = ("Time Selection Criteria", "Resource Selection Criteria", "Location Selection Criteria", "Slot Spacing Criteria", "Filler Override Criteria",)
    _c_attrs = ("time_selection_criteria", "resource_selection_criteria", "location_selection_criteria", "slot_spacing_criteria", "filler_override_criteria",)
    # fmt: on

    def __init__(
        self,
        time_selection_criteria: TimeSelectionCriteriaParameterClassCodes
        | SCV
        | tuple[TimeSelectionCriteriaParameterClassCodes | SCV, ...]
        | None = None,  # APR.1
        resource_selection_criteria: TimeSelectionCriteriaParameterClassCodes
        | SCV
        | tuple[TimeSelectionCriteriaParameterClassCodes | SCV, ...]
        | None = None,  # APR.2
        location_selection_criteria: TimeSelectionCriteriaParameterClassCodes
        | SCV
        | tuple[TimeSelectionCriteriaParameterClassCodes | SCV, ...]
        | None = None,  # APR.3
        slot_spacing_criteria: NM | tuple[NM, ...] | None = None,  # APR.4
        filler_override_criteria: SCV | tuple[SCV, ...] | None = None,  # APR.5
    ):
        """
        Appointment Preferences - `APR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR>`_
        The APR segment contains parameters and preference specifications used for requesting appointments in the SRM message. It allows placer applications to provide coded parameters and preference indicators to the filler application, to help determine when a requested appointment should be scheduled. An APR segment can be provided in conjunction with either the ARQ segment or any of the service and resource segments (AIG, AIS, AIP, and AIL). If an APR segment appears in conjunction with an ARQ segment, its parameters and preference indicators pertain to the schedule request as a whole. If the APR segment appears with any of the service and resource segments, then its parameters and preferences apply only to the immediately preceding service or resource.

        :param time_selection_criteria: Scheduling Class Value Pair (id: APR.1 | len: 80 | use: O | rpt: *)
        :param resource_selection_criteria: Scheduling Class Value Pair (id: APR.2 | len: 80 | use: O | rpt: *)
        :param location_selection_criteria: Scheduling Class Value Pair (id: APR.3 | len: 80 | use: O | rpt: *)
        :param slot_spacing_criteria: Numeric (id: APR.4 | len: 5 | use: O | rpt: 1)
        :param filler_override_criteria: Scheduling Class Value Pair (id: APR.5 | len: 80 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.time_selection_criteria = time_selection_criteria
        self.resource_selection_criteria = resource_selection_criteria
        self.location_selection_criteria = location_selection_criteria
        self.slot_spacing_criteria = slot_spacing_criteria
        self.filler_override_criteria = filler_override_criteria

    @property
    def time_selection_criteria(
        self,
    ) -> tuple[TimeSelectionCriteriaParameterClassCodes, ...] | tuple[None]:
        """
        id: APR.1 | len: 80 | use: O | rpt: *
        ---
        return_type: tuple[SCV, ...]: (Scheduling Class Value Pair, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/APR.1
        """
        return self._c_data[0]

    @time_selection_criteria.setter  # set APR.1
    def time_selection_criteria(
        self,
        time_selection_criteria_parameter_class_codes: TimeSelectionCriteriaParameterClassCodes
        | tuple[TimeSelectionCriteriaParameterClassCodes]
        | None,
    ):
        """
        id: APR.1 | len: 80 | use: O | rpt: *
        ---
        param_type: SCV | tuple[SCV, ...]: (Scheduling Class Value Pair, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/APR.1
        """
        if isinstance(time_selection_criteria_parameter_class_codes, tuple):
            self._c_data[0] = time_selection_criteria_parameter_class_codes
        else:
            self._c_data[0] = (time_selection_criteria_parameter_class_codes,)

    @property
    def resource_selection_criteria(
        self,
    ) -> tuple[TimeSelectionCriteriaParameterClassCodes, ...] | tuple[None]:
        """
        id: APR.2 | len: 80 | use: O | rpt: *
        ---
        return_type: tuple[SCV, ...]: (Scheduling Class Value Pair, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/APR.2
        """
        return self._c_data[1]

    @resource_selection_criteria.setter  # set APR.2
    def resource_selection_criteria(
        self,
        time_selection_criteria_parameter_class_codes: TimeSelectionCriteriaParameterClassCodes
        | tuple[TimeSelectionCriteriaParameterClassCodes]
        | None,
    ):
        """
        id: APR.2 | len: 80 | use: O | rpt: *
        ---
        param_type: SCV | tuple[SCV, ...]: (Scheduling Class Value Pair, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/APR.2
        """
        if isinstance(time_selection_criteria_parameter_class_codes, tuple):
            self._c_data[1] = time_selection_criteria_parameter_class_codes
        else:
            self._c_data[1] = (time_selection_criteria_parameter_class_codes,)

    @property
    def location_selection_criteria(
        self,
    ) -> tuple[TimeSelectionCriteriaParameterClassCodes, ...] | tuple[None]:
        """
        id: APR.3 | len: 80 | use: O | rpt: *
        ---
        return_type: tuple[SCV, ...]: (Scheduling Class Value Pair, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/APR.3
        """
        return self._c_data[2]

    @location_selection_criteria.setter  # set APR.3
    def location_selection_criteria(
        self,
        time_selection_criteria_parameter_class_codes: TimeSelectionCriteriaParameterClassCodes
        | tuple[TimeSelectionCriteriaParameterClassCodes]
        | None,
    ):
        """
        id: APR.3 | len: 80 | use: O | rpt: *
        ---
        param_type: SCV | tuple[SCV, ...]: (Scheduling Class Value Pair, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/APR.3
        """
        if isinstance(time_selection_criteria_parameter_class_codes, tuple):
            self._c_data[2] = time_selection_criteria_parameter_class_codes
        else:
            self._c_data[2] = (time_selection_criteria_parameter_class_codes,)

    @property  # get APR.4
    def slot_spacing_criteria(self) -> NM | None:
        """
        id: APR.4 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/APR.4
        """
        return self._c_data[3][0]

    @slot_spacing_criteria.setter  # set APR.4
    def slot_spacing_criteria(self, nm: NM | None):
        """
        id: APR.4 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/APR.4
        """
        self._c_data[3] = (nm,)

    @property
    def filler_override_criteria(self) -> tuple[SCV, ...] | tuple[None]:
        """
        id: APR.5 | len: 80 | use: O | rpt: *
        ---
        return_type: tuple[SCV, ...]: (Scheduling Class Value Pair, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/APR.5
        """
        return self._c_data[4]

    @filler_override_criteria.setter  # set APR.5
    def filler_override_criteria(self, scv: SCV | tuple[SCV] | None):
        """
        id: APR.5 | len: 80 | use: O | rpt: *
        ---
        param_type: SCV | tuple[SCV, ...]: (Scheduling Class Value Pair, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/APR.5
        """
        if isinstance(scv, tuple):
            self._c_data[4] = scv
        else:
            self._c_data[4] = (scv,)
