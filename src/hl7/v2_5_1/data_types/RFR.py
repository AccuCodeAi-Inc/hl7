from __future__ import annotations
from ...base import DataType
from .IS import IS
from .TX import TX
from .ST import ST
from .NR import NR
from ..tables.AdministrativeSex import AdministrativeSex


"""
DataType - RFR
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::RFR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RFR,
    IS, TX, ST, NR
)

rfr = RFR(  # Reference Range - Describes a reference range and its supporting detail
    numeric_range=nr,  # NR(...)  # Required.
    administrative_sex=None,  # IS(...) 
    age_range=None,  # NR(...) 
    gestational_age_range=None,  # NR(...) 
    species=None,  # ST(...) 
    race_or_subspecies=None,  # ST(...) 
    conditions=None,  # TX(...) 
)

-----END COMPOSITE_DATA_TYPE::RFR TEMPLATE-----
"""


class RFR(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 352
    _hl7_id = """RFR"""
    _hl7_name = """Reference Range"""
    _hl7_description = """Describes a reference range and its supporting detail"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR"
    _c_length = (33, 8, 33, 33, 20, 20, 199,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("RFR.1", "RFR.2", "RFR.3", "RFR.4", "RFR.5", "RFR.6", "RFR.7",)
    _c_components = (NR, IS, NR, NR, ST, ST, TX,)
    _c_names = ("Numeric Range", "Administrative Sex", "Age Range", "Gestational Age Range", "Species", "Race/Subspecies", "Conditions",)
    _c_attrs = ("numeric_range", "administrative_sex", "age_range", "gestational_age_range", "species", "race_or_subspecies", "conditions",)
    # fmt: on

    def __init__(
        self,
        numeric_range: NR | tuple[NR],  # RFR.1
        administrative_sex: AdministrativeSex
        | IS
        | tuple[AdministrativeSex | IS]
        | None = None,  # RFR.2
        age_range: NR | tuple[NR] | None = None,  # RFR.3
        gestational_age_range: NR | tuple[NR] | None = None,  # RFR.4
        species: ST | tuple[ST] | None = None,  # RFR.5
        race_or_subspecies: ST | tuple[ST] | None = None,  # RFR.6
        conditions: TX | tuple[TX] | None = None,  # RFR.7
    ):
        """
        Reference Range - `RFR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RFR>`_
        Describes a reference range and its supporting detail.

        :param numeric_range: This component specifies the numeric interval of the reference data (id: RFR.1 | len: 33 | use: R | rpt: 1)
        :param administrative_sex: This component specifies which gender for which the reference range is valid (id: RFR.2 | len: 8 | use: O | rpt: 1)
        :param age_range: This component specifies the age range for which the reference range is valid (id: RFR.3 | len: 33 | use: O | rpt: 1)
        :param gestational_age_range: This component specifies the gestational age range for which the reference range is valid (id: RFR.4 | len: 33 | use: O | rpt: 1)
        :param species: This component specifies the species for which the reference range is valid (id: RFR.5 | len: 20 | use: O | rpt: 1)
        :param race_or_subspecies: This component specifies the race or subspecies for which the reference range is valid (id: RFR.6 | len: 20 | use: O | rpt: 1)
        :param conditions: This component specifies any arbitrary condition for which the reference range is valid (id: RFR.7 | len: 199 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.numeric_range = numeric_range
        self.administrative_sex = administrative_sex
        self.age_range = age_range
        self.gestational_age_range = gestational_age_range
        self.species = species
        self.race_or_subspecies = race_or_subspecies
        self.conditions = conditions

    @property  # get RFR.1
    def numeric_range(self) -> NR:
        """
        id: RFR.1 | len: 33 | use: R | rpt: 1
        ---
        This component specifies the numeric interval of the reference data. Range is taken to be inclusive (i.e., the range includes the end points). Units are context sensitive and are defined in the usage note for the field where this data type is used.
        ---
        return_type: NR: Numeric Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.1
        """
        return self._c_data[0][0]

    @numeric_range.setter  # set RFR.1
    def numeric_range(self, nr: NR):
        """
        id: RFR.1 | len: 33 | use: R | rpt: 1
        ---
        This component specifies the numeric interval of the reference data. Range is taken to be inclusive (i.e., the range includes the end points). Units are context sensitive and are defined in the usage note for the field where this data type is used.
        ---
        param_type: NR: Numeric Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.1
        """
        self._c_data[0] = (nr,)

    @property  # get RFR.2
    def administrative_sex(self) -> AdministrativeSex | None:
        """
        id: RFR.2 | len: 8 | use: O | rpt: 1
        ---
        This component specifies which gender for which the reference range is valid. Refer to User-defined Table 0001 - Administrative Sex for suggested values.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.2
        """
        return self._c_data[1][0]

    @administrative_sex.setter  # set RFR.2
    def administrative_sex(self, administrative_sex: AdministrativeSex | None):
        """
        id: RFR.2 | len: 8 | use: O | rpt: 1
        ---
        This component specifies which gender for which the reference range is valid. Refer to User-defined Table 0001 - Administrative Sex for suggested values.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.2
        """
        self._c_data[1] = (administrative_sex,)

    @property  # get RFR.3
    def age_range(self) -> NR | None:
        """
        id: RFR.3 | len: 33 | use: O | rpt: 1
        ---
        This component specifies the age range for which the reference range is valid. Ages of less than one year should be specified as a fraction (e.g., 1 month = 0.0830, 1 week = 0.01920, 1 day = 0.0027300). However, for most purposes involving infants, the gestational age (measured in weeks) is preferred. The lower end of the range is not indicated; the upper end is, assuring that series of ranges do not overlap.
        ---
        return_type: NR: Numeric Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.3
        """
        return self._c_data[2][0]

    @age_range.setter  # set RFR.3
    def age_range(self, nr: NR | None):
        """
        id: RFR.3 | len: 33 | use: O | rpt: 1
        ---
        This component specifies the age range for which the reference range is valid. Ages of less than one year should be specified as a fraction (e.g., 1 month = 0.0830, 1 week = 0.01920, 1 day = 0.0027300). However, for most purposes involving infants, the gestational age (measured in weeks) is preferred. The lower end of the range is not indicated; the upper end is, assuring that series of ranges do not overlap.
        ---
        param_type: NR: Numeric Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.3
        """
        self._c_data[2] = (nr,)

    @property  # get RFR.4
    def gestational_age_range(self) -> NR | None:
        """
        id: RFR.4 | len: 33 | use: O | rpt: 1
        ---
        This component specifies the gestational age range for which the reference range is valid. Gestational age is relevant only when the reference range is influenced by the stage of pregnancy. The gestational age is measured in weeks from conception. For example, |1&4| implies that the normals apply to gestational ages from 1 week to 4 weeks inclusive. The lower end of the range is not included; the upper end is, assuring that series of age ranges do not overlap.
        ---
        return_type: NR: Numeric Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.4
        """
        return self._c_data[3][0]

    @gestational_age_range.setter  # set RFR.4
    def gestational_age_range(self, nr: NR | None):
        """
        id: RFR.4 | len: 33 | use: O | rpt: 1
        ---
        This component specifies the gestational age range for which the reference range is valid. Gestational age is relevant only when the reference range is influenced by the stage of pregnancy. The gestational age is measured in weeks from conception. For example, |1&4| implies that the normals apply to gestational ages from 1 week to 4 weeks inclusive. The lower end of the range is not included; the upper end is, assuring that series of age ranges do not overlap.
        ---
        param_type: NR: Numeric Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.4
        """
        self._c_data[3] = (nr,)

    @property  # get RFR.5
    def species(self) -> ST | None:
        """
        id: RFR.5 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the species for which the reference range is valid. Species is assumed to be human unless otherwise stated. Example values are rabbit, mouse, and rat.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.5
        """
        return self._c_data[4][0]

    @species.setter  # set RFR.5
    def species(self, st: ST | None):
        """
        id: RFR.5 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the species for which the reference range is valid. Species is assumed to be human unless otherwise stated. Example values are rabbit, mouse, and rat.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.5
        """
        self._c_data[4] = (st,)

    @property  # get RFR.6
    def race_or_subspecies(self) -> ST | None:
        """
        id: RFR.6 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the race or subspecies for which the reference range is valid. In the case of humans (the default species), the race is specified when race influences the reference range. When normal ranges for animals are being described, this component can be used to describe subspecies or special breeds of animals.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.6
        """
        return self._c_data[5][0]

    @race_or_subspecies.setter  # set RFR.6
    def race_or_subspecies(self, st: ST | None):
        """
        id: RFR.6 | len: 20 | use: O | rpt: 1
        ---
        This component specifies the race or subspecies for which the reference range is valid. In the case of humans (the default species), the race is specified when race influences the reference range. When normal ranges for animals are being described, this component can be used to describe subspecies or special breeds of animals.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.6
        """
        self._c_data[5] = (st,)

    @property  # get RFR.7
    def conditions(self) -> TX | None:
        """
        id: RFR.7 | len: 199 | use: O | rpt: 1
        ---
        This component specifies any arbitrary condition for which the reference range is valid. This may include such conditions as phase of menstrual cycle or dose of a particular drug. It is provided as a way to communicate the normal ranges for special conditions. It does not allow automatic checking of these text conditions.
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.7
        """
        return self._c_data[6][0]

    @conditions.setter  # set RFR.7
    def conditions(self, tx: TX | None):
        """
        id: RFR.7 | len: 199 | use: O | rpt: 1
        ---
        This component specifies any arbitrary condition for which the reference range is valid. This may include such conditions as phase of menstrual cycle or dose of a particular drug. It is provided as a way to communicate the normal ranges for special conditions. It does not allow automatic checking of these text conditions.
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RFR.7
        """
        self._c_data[6] = (tx,)
