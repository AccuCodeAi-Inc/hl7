from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TX import TX
from ..data_types.NM import NM


"""
Observations that are Calculated from Other Observations - OM6
HL7 Version: 2.5.1

-----BEGIN SEGMENT::OM6 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OM6,
    TX, NM
)

om6 = OM6(  #  - This segment contains the information about quantities that are derived from one or more other quantities or direct observations by mathematical or logical means
    sequence_number_test_or_observation_master_file=None,  # NM(...) 
    derivation_rule=None,  # TX(...) 
)

-----END SEGMENT::OM6 TEMPLATE-----
"""


class OM6(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """OM6"""
    _hl7_name = """Observations that are Calculated from Other Observations"""
    _hl7_description = """This segment contains the information about quantities that are derived from one or more other quantities or direct observations by mathematical or logical means"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM6"
    _c_length = (4, 10240,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_components = (NM, TX,)
    _c_aliases = ("OM6.1", "OM6.2",)
    _c_names = ("Sequence Number - Test/Observation Master File", "Derivation Rule",)
    _c_attrs = ("sequence_number_test_or_observation_master_file", "derivation_rule",)
    # fmt: on

    def __init__(
        self,
        sequence_number_test_or_observation_master_file: NM
        | tuple[NM]
        | None = None,  # OM6.1
        derivation_rule: TX | tuple[TX] | None = None,  # OM6.2
    ):
        """
        Observations that are Calculated from Other Observations - `OM6 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM6>`_
        This segment contains the information about quantities that are derived from one or more other quantities or direct observations by mathematical or logical means.

        :param sequence_number_test_or_observation_master_file: Numeric (id: OM6.1 | len: 4 | use: O | rpt: 1)
        :param derivation_rule: Text Data (id: OM6.2 | len: 10240 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.sequence_number_test_or_observation_master_file = (
            sequence_number_test_or_observation_master_file
        )
        self.derivation_rule = derivation_rule

    @property  # get OM6.1
    def sequence_number_test_or_observation_master_file(self) -> NM | None:
        """
        id: OM6.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM6.1
        """
        return self._c_data[0][0]

    @sequence_number_test_or_observation_master_file.setter  # set OM6.1
    def sequence_number_test_or_observation_master_file(self, nm: NM | None):
        """
        id: OM6.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM6.1
        """
        self._c_data[0] = (nm,)

    @property  # get OM6.2
    def derivation_rule(self) -> TX | None:
        """
        id: OM6.2 | len: 10240 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM6.2
        """
        return self._c_data[1][0]

    @derivation_rule.setter  # set OM6.2
    def derivation_rule(self, tx: TX | None):
        """
        id: OM6.2 | len: 10240 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM6.2
        """
        self._c_data[1] = (tx,)
