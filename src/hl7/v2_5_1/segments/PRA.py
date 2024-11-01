from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SPD import SPD
from ..data_types.PLN import PLN
from ..data_types.ID import ID
from ..data_types.PIP import PIP
from ..data_types.IS import IS
from ..data_types.DT import DT
from ..data_types.CE import CE
from ..data_types.SI import SI
from ..tables.GovernmentReimbursementProgram import GovernmentReimbursementProgram
from ..tables.PractitionerCategory import PractitionerCategory
from ..tables.PractitionerGroup import PractitionerGroup
from ..tables.Institution import Institution
from ..tables.ProviderBilling import ProviderBilling


"""
Practitioner Detail - PRA
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PRA TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PRA,
    SPD, PLN, ID, PIP, IS, DT, CE, SI
)

pra = PRA(  #  - The PRA segment adds detailed medical practitioner information to the personnel identified by the STF segment
    primary_key_value_pra=None,  # CE(...) 
    practitioner_group=None,  # CE(...) 
    practitioner_category=None,  # IS(...) 
    provider_billing=None,  # ID(...) 
    specialty=None,  # SPD(...) 
    practitioner_id_numbers=None,  # PLN(...) 
    privileges=None,  # PIP(...) 
    date_entered_practice=None,  # DT(...) 
    institution=None,  # CE(...) 
    date_left_practice=None,  # DT(...) 
    government_reimbursement_billing_eligibility=None,  # CE(...) 
    set_id_pra=None,  # SI(...) 
)

-----END SEGMENT::PRA TEMPLATE-----
"""


class PRA(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PRA"""
    _hl7_name = """Practitioner Detail"""
    _hl7_description = """The PRA segment adds detailed medical practitioner information to the personnel identified by the STF segment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRA"
    _c_length = (250, 250, 3, 1, 112, 99, 770, 8, 250, 8, 250, 60,)
    _c_rpt = (1, 65535, 65535, 1, 65535, 65535, 65535, 1, 1, 1, 65535, 1,)
    _c_usage = ("C", "O", "O", "O", "O", "B", "O", "O", "O", "O", "O", "C",)
    _c_components = (CE, CE, IS, ID, SPD, PLN, PIP, DT, CE, DT, CE, SI,)
    _c_aliases = ("PRA.1", "PRA.2", "PRA.3", "PRA.4", "PRA.5", "PRA.6", "PRA.7", "PRA.8", "PRA.9", "PRA.10", "PRA.11", "PRA.12",)
    _c_names = ("Primary Key Value - PRA", "Practitioner Group", "Practitioner Category", "Provider Billing", "Specialty", "Practitioner ID Numbers", "Privileges", "Date Entered Practice", "Institution", "Date Left Practice", "Government Reimbursement Billing Eligibility", "Set ID - PRA",)
    _c_attrs = ("primary_key_value_pra", "practitioner_group", "practitioner_category", "provider_billing", "specialty", "practitioner_id_numbers", "privileges", "date_entered_practice", "institution", "date_left_practice", "government_reimbursement_billing_eligibility", "set_id_pra",)
    # fmt: on

    def __init__(
        self,
        primary_key_value_pra: CE | tuple[CE] | None = None,  # PRA.1
        practitioner_group: PractitionerGroup
        | CE
        | tuple[PractitionerGroup | CE]
        | None = None,  # PRA.2
        practitioner_category: PractitionerCategory
        | IS
        | tuple[PractitionerCategory | IS]
        | None = None,  # PRA.3
        provider_billing: ProviderBilling
        | ID
        | tuple[ProviderBilling | ID]
        | None = None,  # PRA.4
        specialty: SPD | tuple[SPD] | None = None,  # PRA.5
        practitioner_id_numbers: PLN | tuple[PLN] | None = None,  # PRA.6
        privileges: PIP | tuple[PIP] | None = None,  # PRA.7
        date_entered_practice: DT | tuple[DT] | None = None,  # PRA.8
        institution: Institution | CE | tuple[Institution | CE] | None = None,  # PRA.9
        date_left_practice: DT | tuple[DT] | None = None,  # PRA.10
        government_reimbursement_billing_eligibility: GovernmentReimbursementProgram
        | CE
        | tuple[GovernmentReimbursementProgram | CE]
        | None = None,  # PRA.11
        set_id_pra: SI | tuple[SI] | None = None,  # PRA.12
    ):
        """
        Practitioner Detail - `PRA <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRA>`_
        The PRA segment adds detailed medical practitioner information to the personnel identified by the STF segment.  A PRA segment may optionally follow an STF segment.  A PRA segment must always have been preceded by a corresponding STF segment.  The PRA segment may also be used for staff who work in healthcare who are not practitioners, but need to be certified, e.g., “medical records staff.”

        :param primary_key_value_pra: Coded Element (id: PRA.1 | len: 250 | use: C | rpt: 1)
        :param practitioner_group: Coded Element (id: PRA.2 | len: 250 | use: O | rpt: *)
        :param practitioner_category: Coded value for user-defined tables (id: PRA.3 | len: 3 | use: O | rpt: *)
        :param provider_billing: Coded values for HL7 tables (id: PRA.4 | len: 1 | use: O | rpt: 1)
        :param specialty: Specialty Description (id: PRA.5 | len: 112 | use: O | rpt: *)
        :param practitioner_id_numbers: Practitioner License or Other ID Number (id: PRA.6 | len: 99 | use: B | rpt: *)
        :param privileges: Practitioner Institutional Privileges (id: PRA.7 | len: 770 | use: O | rpt: *)
        :param date_entered_practice: Date (id: PRA.8 | len: 8 | use: O | rpt: 1)
        :param institution: Coded Element (id: PRA.9 | len: 250 | use: O | rpt: 1)
        :param date_left_practice: Date (id: PRA.10 | len: 8 | use: O | rpt: 1)
        :param government_reimbursement_billing_eligibility: Coded Element (id: PRA.11 | len: 250 | use: O | rpt: *)
        :param set_id_pra: Sequence ID (id: PRA.12 | len: 60 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.primary_key_value_pra = primary_key_value_pra
        self.practitioner_group = practitioner_group
        self.practitioner_category = practitioner_category
        self.provider_billing = provider_billing
        self.specialty = specialty
        self.practitioner_id_numbers = practitioner_id_numbers
        self.privileges = privileges
        self.date_entered_practice = date_entered_practice
        self.institution = institution
        self.date_left_practice = date_left_practice
        self.government_reimbursement_billing_eligibility = (
            government_reimbursement_billing_eligibility
        )
        self.set_id_pra = set_id_pra

    @property  # get PRA.1
    def primary_key_value_pra(self) -> CE | None:
        """
        id: PRA.1 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.1
        """
        return self._c_data[0][0]

    @primary_key_value_pra.setter  # set PRA.1
    def primary_key_value_pra(self, ce: CE | None):
        """
        id: PRA.1 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.1
        """
        self._c_data[0] = (ce,)

    @property
    def practitioner_group(self) -> tuple[PractitionerGroup, ...] | tuple[None]:
        """
        id: PRA.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.2
        """
        return self._c_data[1]

    @practitioner_group.setter  # set PRA.2
    def practitioner_group(
        self, practitioner_group: PractitionerGroup | tuple[PractitionerGroup] | None
    ):
        """
        id: PRA.2 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.2
        """
        if isinstance(practitioner_group, tuple):
            self._c_data[1] = practitioner_group
        else:
            self._c_data[1] = (practitioner_group,)

    @property
    def practitioner_category(self) -> tuple[PractitionerCategory, ...] | tuple[None]:
        """
        id: PRA.3 | len: 3 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.3
        """
        return self._c_data[2]

    @practitioner_category.setter  # set PRA.3
    def practitioner_category(
        self,
        practitioner_category: PractitionerCategory
        | tuple[PractitionerCategory]
        | None,
    ):
        """
        id: PRA.3 | len: 3 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.3
        """
        if isinstance(practitioner_category, tuple):
            self._c_data[2] = practitioner_category
        else:
            self._c_data[2] = (practitioner_category,)

    @property  # get PRA.4
    def provider_billing(self) -> ProviderBilling | None:
        """
        id: PRA.4 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.4
        """
        return self._c_data[3][0]

    @provider_billing.setter  # set PRA.4
    def provider_billing(self, provider_billing: ProviderBilling | None):
        """
        id: PRA.4 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.4
        """
        self._c_data[3] = (provider_billing,)

    @property
    def specialty(self) -> tuple[SPD, ...] | tuple[None]:
        """
        id: PRA.5 | len: 112 | use: O | rpt: *
        ---
        return_type: tuple[SPD, ...]: (Specialty Description, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.5
        """
        return self._c_data[4]

    @specialty.setter  # set PRA.5
    def specialty(self, spd: SPD | tuple[SPD] | None):
        """
        id: PRA.5 | len: 112 | use: O | rpt: *
        ---
        param_type: SPD | tuple[SPD, ...]: (Specialty Description, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.5
        """
        if isinstance(spd, tuple):
            self._c_data[4] = spd
        else:
            self._c_data[4] = (spd,)

    @property
    def practitioner_id_numbers(self) -> tuple[PLN, ...] | tuple[None]:
        """
        id: PRA.6 | len: 99 | use: B | rpt: *
        ---
        return_type: tuple[PLN, ...]: (Practitioner License or Other ID Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.6
        """
        return self._c_data[5]

    @practitioner_id_numbers.setter  # set PRA.6
    def practitioner_id_numbers(self, pln: PLN | tuple[PLN] | None):
        """
        id: PRA.6 | len: 99 | use: B | rpt: *
        ---
        param_type: PLN | tuple[PLN, ...]: (Practitioner License or Other ID Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.6
        """
        if isinstance(pln, tuple):
            self._c_data[5] = pln
        else:
            self._c_data[5] = (pln,)

    @property
    def privileges(self) -> tuple[PIP, ...] | tuple[None]:
        """
        id: PRA.7 | len: 770 | use: O | rpt: *
        ---
        return_type: tuple[PIP, ...]: (Practitioner Institutional Privileges, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.7
        """
        return self._c_data[6]

    @privileges.setter  # set PRA.7
    def privileges(self, pip: PIP | tuple[PIP] | None):
        """
        id: PRA.7 | len: 770 | use: O | rpt: *
        ---
        param_type: PIP | tuple[PIP, ...]: (Practitioner Institutional Privileges, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.7
        """
        if isinstance(pip, tuple):
            self._c_data[6] = pip
        else:
            self._c_data[6] = (pip,)

    @property  # get PRA.8
    def date_entered_practice(self) -> DT | None:
        """
        id: PRA.8 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.8
        """
        return self._c_data[7][0]

    @date_entered_practice.setter  # set PRA.8
    def date_entered_practice(self, dt: DT | None):
        """
        id: PRA.8 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.8
        """
        self._c_data[7] = (dt,)

    @property  # get PRA.9
    def institution(self) -> Institution | None:
        """
        id: PRA.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.9
        """
        return self._c_data[8][0]

    @institution.setter  # set PRA.9
    def institution(self, institution: Institution | None):
        """
        id: PRA.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.9
        """
        self._c_data[8] = (institution,)

    @property  # get PRA.10
    def date_left_practice(self) -> DT | None:
        """
        id: PRA.10 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.10
        """
        return self._c_data[9][0]

    @date_left_practice.setter  # set PRA.10
    def date_left_practice(self, dt: DT | None):
        """
        id: PRA.10 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.10
        """
        self._c_data[9] = (dt,)

    @property
    def government_reimbursement_billing_eligibility(
        self,
    ) -> tuple[GovernmentReimbursementProgram, ...] | tuple[None]:
        """
        id: PRA.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.11
        """
        return self._c_data[10]

    @government_reimbursement_billing_eligibility.setter  # set PRA.11
    def government_reimbursement_billing_eligibility(
        self,
        government_reimbursement_program: GovernmentReimbursementProgram
        | tuple[GovernmentReimbursementProgram]
        | None,
    ):
        """
        id: PRA.11 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.11
        """
        if isinstance(government_reimbursement_program, tuple):
            self._c_data[10] = government_reimbursement_program
        else:
            self._c_data[10] = (government_reimbursement_program,)

    @property  # get PRA.12
    def set_id_pra(self) -> SI | None:
        """
        id: PRA.12 | len: 60 | use: C | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.12
        """
        return self._c_data[11][0]

    @set_id_pra.setter  # set PRA.12
    def set_id_pra(self, si: SI | None):
        """
        id: PRA.12 | len: 60 | use: C | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRA.12
        """
        self._c_data[11] = (si,)
