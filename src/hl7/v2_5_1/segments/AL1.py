from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.DT import DT
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..tables.AllergySeverity import AllergySeverity
from ..tables.AllergenType import AllergenType


"""
Patient Allergy Information - AL1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::AL1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    AL1,
    SI, DT, ST, CE
)

al1 = AL1(  #  - The AL1 segment contains patient allergy information of various types
    set_id_al1=si,  # SI(...)  # Required.
    allergen_type_code=None,  # CE(...) 
    allergen_code_or_mnemonic_or_description=ce,  # CE(...)  # Required.
    allergy_severity_code=None,  # CE(...) 
    allergy_reaction_code=None,  # ST(...) 
    identification_date=None,  # DT(...) 
)

-----END SEGMENT::AL1 TEMPLATE-----
"""


class AL1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """AL1"""
    _hl7_name = """Patient Allergy Information"""
    _hl7_description = """The AL1 segment contains patient allergy information of various types"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1"
    _c_length = (4, 250, 250, 250, 15, 8,)
    _c_rpt = (1, 1, 1, 1, 65535, 1,)
    _c_usage = ("R", "O", "R", "O", "O", "B",)
    _c_components = (SI, CE, CE, CE, ST, DT,)
    _c_aliases = ("AL1.1", "AL1.2", "AL1.3", "AL1.4", "AL1.5", "AL1.6",)
    _c_names = ("Set ID - AL1", "Allergen Type Code", "Allergen Code/Mnemonic/Description", "Allergy Severity Code", "Allergy Reaction Code", "Identification Date",)
    _c_attrs = ("set_id_al1", "allergen_type_code", "allergen_code_or_mnemonic_or_description", "allergy_severity_code", "allergy_reaction_code", "identification_date",)
    # fmt: on

    def __init__(
        self,
        set_id_al1: SI,  # AL1.1
        allergen_code_or_mnemonic_or_description: CE,  # AL1.3
        allergen_type_code: AllergenType | CE | None = None,  # AL1.2
        allergy_severity_code: AllergySeverity | CE | None = None,  # AL1.4
        allergy_reaction_code: ST | None = None,  # AL1.5
        identification_date: DT | None = None,  # AL1.6
    ):
        """
        Patient Allergy Information - `AL1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1>`_
        The AL1 segment contains patient allergy information of various types. Most of this information will be derived from user-defined tables. Each AL1 segment describes a single patient allergy.

        :param set_id_al1: Sequence ID (id: AL1.1 | len: 4 | use: R | rpt: 1)
        :param allergen_type_code: Coded Element (id: AL1.2 | len: 250 | use: O | rpt: 1)
        :param allergen_code_or_mnemonic_or_description: Coded Element (id: AL1.3 | len: 250 | use: R | rpt: 1)
        :param allergy_severity_code: Coded Element (id: AL1.4 | len: 250 | use: O | rpt: 1)
        :param allergy_reaction_code: String Data (id: AL1.5 | len: 15 | use: O | rpt: *)
        :param identification_date: Date (id: AL1.6 | len: 8 | use: B | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.set_id_al1 = set_id_al1
        self.allergen_type_code = allergen_type_code
        self.allergen_code_or_mnemonic_or_description = (
            allergen_code_or_mnemonic_or_description
        )
        self.allergy_severity_code = allergy_severity_code
        self.allergy_reaction_code = allergy_reaction_code
        self.identification_date = identification_date

    @property  # get AL1.1
    def set_id_al1(self) -> SI:
        """
        id: AL1.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.1
        """
        return self._c_data[0][0]

    @set_id_al1.setter  # set AL1.1
    def set_id_al1(self, si: SI):
        """
        id: AL1.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.1
        """
        self._c_data[0] = (si,)

    @property  # get AL1.2
    def allergen_type_code(self) -> AllergenType | None:
        """
        id: AL1.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.2
        """
        return self._c_data[1][0]

    @allergen_type_code.setter  # set AL1.2
    def allergen_type_code(self, allergen_type: AllergenType | None):
        """
        id: AL1.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.2
        """
        self._c_data[1] = (allergen_type,)

    @property  # get AL1.3
    def allergen_code_or_mnemonic_or_description(self) -> CE:
        """
        id: AL1.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.3
        """
        return self._c_data[2][0]

    @allergen_code_or_mnemonic_or_description.setter  # set AL1.3
    def allergen_code_or_mnemonic_or_description(self, ce: CE):
        """
        id: AL1.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.3
        """
        self._c_data[2] = (ce,)

    @property  # get AL1.4
    def allergy_severity_code(self) -> AllergySeverity | None:
        """
        id: AL1.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.4
        """
        return self._c_data[3][0]

    @allergy_severity_code.setter  # set AL1.4
    def allergy_severity_code(self, allergy_severity: AllergySeverity | None):
        """
        id: AL1.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.4
        """
        self._c_data[3] = (allergy_severity,)

    @property
    def allergy_reaction_code(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: AL1.5 | len: 15 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.5
        """
        return self._c_data[4]

    @allergy_reaction_code.setter  # set AL1.5
    def allergy_reaction_code(self, st: ST | tuple[ST] | None):
        """
        id: AL1.5 | len: 15 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.5
        """
        if isinstance(st, tuple):
            self._c_data[4] = st
        else:
            self._c_data[4] = (st,)

    @property  # get AL1.6
    def identification_date(self) -> DT | None:
        """
        id: AL1.6 | len: 8 | use: B | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.6
        """
        return self._c_data[5][0]

    @identification_date.setter  # set AL1.6
    def identification_date(self, dt: DT | None):
        """
        id: AL1.6 | len: 8 | use: B | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AL1.6
        """
        self._c_data[5] = (dt,)
