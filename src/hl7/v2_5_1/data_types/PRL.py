from __future__ import annotations
from ...base import DataType
from .ST import ST
from .CE import CE
from .TX import TX


"""
DataType - PRL
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::PRL TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PRL,
    ST, CE, TX
)

prl = PRL(  # Parent Result Link - Uniquely identifies the parent results OBX segment related to the current order, together with the information in OBR-29-parent
    parent_observation_identifier=ce,  # CE(...)  # Required.
    parent_observation_sub_identifier=None,  # ST(...) 
    parent_observation_value_descriptor=None,  # TX(...) 
)

-----END COMPOSITE_DATA_TYPE::PRL TEMPLATE-----
"""


class PRL(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 755
    _hl7_id = """PRL"""
    _hl7_name = """Parent Result Link"""
    _hl7_description = """Uniquely identifies the parent results OBX segment related to the current order, together with the information in OBR-29-parent"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRL"
    _c_length = (483, 20, 250,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("R", "O", "O",)
    _c_aliases = ("PRL.1", "PRL.2", "PRL.3",)
    _c_components = (CE, ST, TX,)
    _c_names = ("Parent Observation Identifier", "Parent Observation Sub-identifier", "Parent Observation Value Descriptor",)
    _c_attrs = ("parent_observation_identifier", "parent_observation_sub_identifier", "parent_observation_value_descriptor",)
    # fmt: on

    def __init__(
        self,
        parent_observation_identifier: CE | tuple[CE, ...],  # PRL.1
        parent_observation_sub_identifier: ST | tuple[ST, ...] | None = None,  # PRL.2
        parent_observation_value_descriptor: TX | tuple[TX, ...] | None = None,  # PRL.3
    ):
        """
        Parent Result Link - `PRL <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRL>`_
        Uniquely identifies the parent results OBX segment related to the current order, together with the information in OBR-29-parent.

        :param parent_observation_identifier: Contains the unique identifier of the parent observation as defined in the OBX-3 of the parent result (id: PRL.1 | len: 483 | use: R | rpt: 1)
        :param parent_observation_sub_identifier: Contains the sub-ID of the parent result as defined in the OBX-4 of the parent result (id: PRL.2 | len: 20 | use: O | rpt: 1)
        :param parent_observation_value_descriptor: Contains a descriptor of the parent observation value as specified in the OBX-5 of the parent result (id: PRL.3 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.parent_observation_identifier = parent_observation_identifier
        self.parent_observation_sub_identifier = parent_observation_sub_identifier
        self.parent_observation_value_descriptor = parent_observation_value_descriptor

    @property  # get PRL.1
    def parent_observation_identifier(self) -> CE:
        """
        id: PRL.1 | len: 483 | use: R | rpt: 1
        ---
        Contains the unique identifier of the parent observation as defined in the OBX-3 of the parent result. The value is the same as the OBX-3 of the parent.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRL.1
        """
        return self._c_data[0][0]

    @parent_observation_identifier.setter  # set PRL.1
    def parent_observation_identifier(self, ce: CE):
        """
        id: PRL.1 | len: 483 | use: R | rpt: 1
        ---
        Contains the unique identifier of the parent observation as defined in the OBX-3 of the parent result. The value is the same as the OBX-3 of the parent.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRL.1
        """
        self._c_data[0] = (ce,)

    @property  # get PRL.2
    def parent_observation_sub_identifier(self) -> ST | None:
        """
        id: PRL.2 | len: 20 | use: O | rpt: 1
        ---
        Contains the sub-ID of the parent result as defined in the OBX-4 of the parent result. The value is the same as the OBX-4 of the parent.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRL.2
        """
        return self._c_data[1][0]

    @parent_observation_sub_identifier.setter  # set PRL.2
    def parent_observation_sub_identifier(self, st: ST | None):
        """
        id: PRL.2 | len: 20 | use: O | rpt: 1
        ---
        Contains the sub-ID of the parent result as defined in the OBX-4 of the parent result. The value is the same as the OBX-4 of the parent.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRL.2
        """
        self._c_data[1] = (st,)

    @property  # get PRL.3
    def parent_observation_value_descriptor(self) -> TX | None:
        """
        id: PRL.3 | len: 250 | use: O | rpt: 1
        ---
        Contains a descriptor of the parent observation value as specified in the OBX-5 of the parent result.
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRL.3
        """
        return self._c_data[2][0]

    @parent_observation_value_descriptor.setter  # set PRL.3
    def parent_observation_value_descriptor(self, tx: TX | None):
        """
        id: PRL.3 | len: 250 | use: O | rpt: 1
        ---
        Contains a descriptor of the parent observation value as specified in the OBX-5 of the parent result.
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRL.3
        """
        self._c_data[2] = (tx,)
