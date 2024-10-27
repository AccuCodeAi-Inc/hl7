from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..data_types.CWE import CWE
from ..tables.RxComponentType import RxComponentType


"""
Pharmacy/Treatment Component Order - RXC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RXC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RXC,
    ID, CE, NM, CWE
)

rxc = RXC(  #  - If the drug or treatment ordered with the RXO segment is a compound drug OR an IV solution, AND there is not a coded value for OBR-4-universal service ID , which specifies the components (base and all additives), then the components (the base and additives) are specified by two or more RXC segments
    rx_component_type=id,  # ID(...)  # Required.
    component_code=ce,  # CE(...)  # Required.
    component_amount=nm,  # NM(...)  # Required.
    component_units=ce,  # CE(...)  # Required.
    component_strength=None,  # NM(...) 
    component_strength_units=None,  # CE(...) 
    supplementary_code=None,  # CE(...) 
    component_drug_strength_volume=None,  # NM(...) 
    component_drug_strength_volume_units=None,  # CWE(...) 
)

-----END SEGMENT::RXC TEMPLATE-----
"""


class RXC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RXC"""
    _hl7_name = """Pharmacy/Treatment Component Order"""
    _hl7_description = """If the drug or treatment ordered with the RXO segment is a compound drug OR an IV solution, AND there is not a coded value for OBR-4-universal service ID , which specifies the components (base and all additives), then the components (the base and additives) are specified by two or more RXC segments"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC"
    _c_length = (1, 250, 20, 250, 20, 250, 250, 5, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 65535, 1, 1,)
    _c_usage = ("R", "R", "R", "R", "O", "O", "O", "O", "O",)
    _c_components = (ID, CE, NM, CE, NM, CE, CE, NM, CWE,)
    _c_aliases = ("RXC.1", "RXC.2", "RXC.3", "RXC.4", "RXC.5", "RXC.6", "RXC.7", "RXC.8", "RXC.9",)
    _c_names = ("RX Component Type", "Component Code", "Component Amount", "Component Units", "Component Strength", "Component Strength Units", "Supplementary Code", "Component Drug Strength Volume", "Component Drug Strength Volume Units",)
    _c_attrs = ("rx_component_type", "component_code", "component_amount", "component_units", "component_strength", "component_strength_units", "supplementary_code", "component_drug_strength_volume", "component_drug_strength_volume_units",)
    # fmt: on

    def __init__(
        self,
        rx_component_type: RxComponentType | ID,  # RXC.1
        component_code: CE,  # RXC.2
        component_amount: NM,  # RXC.3
        component_units: CE,  # RXC.4
        component_strength: NM | None = None,  # RXC.5
        component_strength_units: CE | None = None,  # RXC.6
        supplementary_code: CE | None = None,  # RXC.7
        component_drug_strength_volume: NM | None = None,  # RXC.8
        component_drug_strength_volume_units: CWE | None = None,  # RXC.9
    ):
        """
        Pharmacy/Treatment Component Order - `RXC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC>`_
        If the drug or treatment ordered with the RXO segment is a compound drug OR an IV solution, AND there is not a coded value for OBR-4-universal service ID , which specifies the components (base and all additives), then the components (the base and additives) are specified by two or more RXC segments. The policy of the pharmacy or treatment application on substitutions at the RXC level is identical to that for the RXO level.

        :param rx_component_type: Coded values for HL7 tables (id: RXC.1 | len: 1 | use: R | rpt: 1)
        :param component_code: Coded Element (id: RXC.2 | len: 250 | use: R | rpt: 1)
        :param component_amount: Numeric (id: RXC.3 | len: 20 | use: R | rpt: 1)
        :param component_units: Coded Element (id: RXC.4 | len: 250 | use: R | rpt: 1)
        :param component_strength: Numeric (id: RXC.5 | len: 20 | use: O | rpt: 1)
        :param component_strength_units: Coded Element (id: RXC.6 | len: 250 | use: O | rpt: 1)
        :param supplementary_code: Coded Element (id: RXC.7 | len: 250 | use: O | rpt: *)
        :param component_drug_strength_volume: Numeric (id: RXC.8 | len: 5 | use: O | rpt: 1)
        :param component_drug_strength_volume_units: Coded with Exceptions (id: RXC.9 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.rx_component_type = rx_component_type
        self.component_code = component_code
        self.component_amount = component_amount
        self.component_units = component_units
        self.component_strength = component_strength
        self.component_strength_units = component_strength_units
        self.supplementary_code = supplementary_code
        self.component_drug_strength_volume = component_drug_strength_volume
        self.component_drug_strength_volume_units = component_drug_strength_volume_units

    @property  # get RXC.1
    def rx_component_type(self) -> RxComponentType:
        """
        id: RXC.1 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.1
        """
        return self._c_data[0][0]

    @rx_component_type.setter  # set RXC.1
    def rx_component_type(self, rx_component_type: RxComponentType):
        """
        id: RXC.1 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.1
        """
        self._c_data[0] = (rx_component_type,)

    @property  # get RXC.2
    def component_code(self) -> CE:
        """
        id: RXC.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.2
        """
        return self._c_data[1][0]

    @component_code.setter  # set RXC.2
    def component_code(self, ce: CE):
        """
        id: RXC.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.2
        """
        self._c_data[1] = (ce,)

    @property  # get RXC.3
    def component_amount(self) -> NM:
        """
        id: RXC.3 | len: 20 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.3
        """
        return self._c_data[2][0]

    @component_amount.setter  # set RXC.3
    def component_amount(self, nm: NM):
        """
        id: RXC.3 | len: 20 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.3
        """
        self._c_data[2] = (nm,)

    @property  # get RXC.4
    def component_units(self) -> CE:
        """
        id: RXC.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.4
        """
        return self._c_data[3][0]

    @component_units.setter  # set RXC.4
    def component_units(self, ce: CE):
        """
        id: RXC.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.4
        """
        self._c_data[3] = (ce,)

    @property  # get RXC.5
    def component_strength(self) -> NM | None:
        """
        id: RXC.5 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.5
        """
        return self._c_data[4][0]

    @component_strength.setter  # set RXC.5
    def component_strength(self, nm: NM | None):
        """
        id: RXC.5 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.5
        """
        self._c_data[4] = (nm,)

    @property  # get RXC.6
    def component_strength_units(self) -> CE | None:
        """
        id: RXC.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.6
        """
        return self._c_data[5][0]

    @component_strength_units.setter  # set RXC.6
    def component_strength_units(self, ce: CE | None):
        """
        id: RXC.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.6
        """
        self._c_data[5] = (ce,)

    @property
    def supplementary_code(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXC.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.7
        """
        return self._c_data[6]

    @supplementary_code.setter  # set RXC.7
    def supplementary_code(self, ce: CE | tuple[CE] | None):
        """
        id: RXC.7 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.7
        """
        if isinstance(ce, tuple):
            self._c_data[6] = ce
        else:
            self._c_data[6] = (ce,)

    @property  # get RXC.8
    def component_drug_strength_volume(self) -> NM | None:
        """
        id: RXC.8 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.8
        """
        return self._c_data[7][0]

    @component_drug_strength_volume.setter  # set RXC.8
    def component_drug_strength_volume(self, nm: NM | None):
        """
        id: RXC.8 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.8
        """
        self._c_data[7] = (nm,)

    @property  # get RXC.9
    def component_drug_strength_volume_units(self) -> CWE | None:
        """
        id: RXC.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.9
        """
        return self._c_data[8][0]

    @component_drug_strength_volume_units.setter  # set RXC.9
    def component_drug_strength_volume_units(self, cwe: CWE | None):
        """
        id: RXC.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXC.9
        """
        self._c_data[8] = (cwe,)
