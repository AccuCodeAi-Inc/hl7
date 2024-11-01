from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ST import ST
from ..data_types.NM import NM


"""
Observation Batteries (Sets) - OM5
HL7 Version: 2.5.1

-----BEGIN SEGMENT::OM5 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OM5,
    CE, ST, NM
)

om5 = OM5(  #  - This segment contains the information about batteries and supersets (a nature code of F, P or S, as described in OM1-18 - Nature of Service/Test/Observation)
    sequence_number_test_or_observation_master_file=None,  # NM(...) 
    test_or_observations_included_within_an_ordered_test_battery=None,  # CE(...) 
    observation_id_suffixes=None,  # ST(...) 
)

-----END SEGMENT::OM5 TEMPLATE-----
"""


class OM5(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """OM5"""
    _hl7_name = """Observation Batteries (Sets)"""
    _hl7_description = """This segment contains the information about batteries and supersets (a nature code of F, P or S, as described in OM1-18 - Nature of Service/Test/Observation)"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM5"
    _c_length = (4, 250, 250,)
    _c_rpt = (1, 65535, 1,)
    _c_usage = ("O", "O", "O",)
    _c_components = (NM, CE, ST,)
    _c_aliases = ("OM5.1", "OM5.2", "OM5.3",)
    _c_names = ("Sequence Number - Test/Observation Master File", "Test/Observations Included within an Ordered Test Battery", "Observation ID Suffixes",)
    _c_attrs = ("sequence_number_test_or_observation_master_file", "test_or_observations_included_within_an_ordered_test_battery", "observation_id_suffixes",)
    # fmt: on

    def __init__(
        self,
        sequence_number_test_or_observation_master_file: NM | None = None,  # OM5.1
        test_or_observations_included_within_an_ordered_test_battery: CE
        | None = None,  # OM5.2
        observation_id_suffixes: ST | None = None,  # OM5.3
    ):
        """
        Observation Batteries (Sets) - `OM5 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM5>`_
        This segment contains the information about batteries and supersets (a nature code of F, P or S, as described in OM1-18 - Nature of Service/Test/Observation).

        :param sequence_number_test_or_observation_master_file: Numeric (id: OM5.1 | len: 4 | use: O | rpt: 1)
        :param test_or_observations_included_within_an_ordered_test_battery: Coded Element (id: OM5.2 | len: 250 | use: O | rpt: *)
        :param observation_id_suffixes: String Data (id: OM5.3 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.sequence_number_test_or_observation_master_file = (
            sequence_number_test_or_observation_master_file
        )
        self.test_or_observations_included_within_an_ordered_test_battery = (
            test_or_observations_included_within_an_ordered_test_battery
        )
        self.observation_id_suffixes = observation_id_suffixes

    @property  # get OM5.1
    def sequence_number_test_or_observation_master_file(self) -> NM | None:
        """
        id: OM5.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM5.1
        """
        return self._c_data[0][0]

    @sequence_number_test_or_observation_master_file.setter  # set OM5.1
    def sequence_number_test_or_observation_master_file(self, nm: NM | None):
        """
        id: OM5.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM5.1
        """
        self._c_data[0] = (nm,)

    @property
    def test_or_observations_included_within_an_ordered_test_battery(
        self,
    ) -> tuple[CE, ...] | tuple[None]:
        """
        id: OM5.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM5.2
        """
        return self._c_data[1]

    @test_or_observations_included_within_an_ordered_test_battery.setter  # set OM5.2
    def test_or_observations_included_within_an_ordered_test_battery(
        self, ce: CE | tuple[CE] | None
    ):
        """
        id: OM5.2 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM5.2
        """
        if isinstance(ce, tuple):
            self._c_data[1] = ce
        else:
            self._c_data[1] = (ce,)

    @property  # get OM5.3
    def observation_id_suffixes(self) -> ST | None:
        """
        id: OM5.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM5.3
        """
        return self._c_data[2][0]

    @observation_id_suffixes.setter  # set OM5.3
    def observation_id_suffixes(self, st: ST | None):
        """
        id: OM5.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM5.3
        """
        self._c_data[2] = (st,)
