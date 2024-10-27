from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..tables.PrimaryLanguage import PrimaryLanguage
from ..tables.LanguageProficiency import LanguageProficiency
from ..tables.LanguageAbility import LanguageAbility


"""
Language Detail - LAN
HL7 Version: 2.5.1

-----BEGIN SEGMENT::LAN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    LAN,
    SI, CE
)

lan = LAN(  #  - The LAN segment adds detailed language information to the staff member identified by the STF segment
    set_id_lan=si,  # SI(...)  # Required.
    language_code=ce,  # CE(...)  # Required.
    language_ability_code=None,  # CE(...) 
    language_proficiency_code=None,  # CE(...) 
)

-----END SEGMENT::LAN TEMPLATE-----
"""


class LAN(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """LAN"""
    _hl7_name = """Language Detail"""
    _hl7_description = """The LAN segment adds detailed language information to the staff member identified by the STF segment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LAN"
    _c_length = (60, 250, 250, 250,)
    _c_rpt = (1, 1, 65535, 1,)
    _c_usage = ("R", "R", "O", "O",)
    _c_components = (SI, CE, CE, CE,)
    _c_aliases = ("LAN.1", "LAN.2", "LAN.3", "LAN.4",)
    _c_names = ("Set ID - LAN", "Language Code", "Language Ability Code", "Language Proficiency Code",)
    _c_attrs = ("set_id_lan", "language_code", "language_ability_code", "language_proficiency_code",)
    # fmt: on

    def __init__(
        self,
        set_id_lan: SI,  # LAN.1
        language_code: PrimaryLanguage | CE,  # LAN.2
        language_ability_code: LanguageAbility | CE | None = None,  # LAN.3
        language_proficiency_code: LanguageProficiency | CE | None = None,  # LAN.4
    ):
        """
        Language Detail - `LAN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/LAN>`_
        The LAN segment adds detailed language information to the staff member identified by the STF segment. An LAN segment may optionally follow an STF segment. An LAN segment must always have been preceded by a corresponding STF segment.

        :param set_id_lan: Sequence ID (id: LAN.1 | len: 60 | use: R | rpt: 1)
        :param language_code: Coded Element (id: LAN.2 | len: 250 | use: R | rpt: 1)
        :param language_ability_code: Coded Element (id: LAN.3 | len: 250 | use: O | rpt: *)
        :param language_proficiency_code: Coded Element (id: LAN.4 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.set_id_lan = set_id_lan
        self.language_code = language_code
        self.language_ability_code = language_ability_code
        self.language_proficiency_code = language_proficiency_code

    @property  # get LAN.1
    def set_id_lan(self) -> SI:
        """
        id: LAN.1 | len: 60 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LAN.1
        """
        return self._c_data[0][0]

    @set_id_lan.setter  # set LAN.1
    def set_id_lan(self, si: SI):
        """
        id: LAN.1 | len: 60 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LAN.1
        """
        self._c_data[0] = (si,)

    @property  # get LAN.2
    def language_code(self) -> PrimaryLanguage:
        """
        id: LAN.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LAN.2
        """
        return self._c_data[1][0]

    @language_code.setter  # set LAN.2
    def language_code(self, primary_language: PrimaryLanguage):
        """
        id: LAN.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LAN.2
        """
        self._c_data[1] = (primary_language,)

    @property
    def language_ability_code(self) -> tuple[LanguageAbility, ...] | tuple[None]:
        """
        id: LAN.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LAN.3
        """
        return self._c_data[2]

    @language_ability_code.setter  # set LAN.3
    def language_ability_code(
        self, language_ability: LanguageAbility | tuple[LanguageAbility] | None
    ):
        """
        id: LAN.3 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LAN.3
        """
        if isinstance(language_ability, tuple):
            self._c_data[2] = language_ability
        else:
            self._c_data[2] = (language_ability,)

    @property  # get LAN.4
    def language_proficiency_code(self) -> LanguageProficiency | None:
        """
        id: LAN.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LAN.4
        """
        return self._c_data[3][0]

    @language_proficiency_code.setter  # set LAN.4
    def language_proficiency_code(
        self, language_proficiency: LanguageProficiency | None
    ):
        """
        id: LAN.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/LAN.4
        """
        self._c_data[3] = (language_proficiency,)
