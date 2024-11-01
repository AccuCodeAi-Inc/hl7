from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.CX import CX
from ..data_types.ID import ID
from ..data_types.DR import DR
from ..tables.EmploymentStatus import EmploymentStatus
from ..tables.OrganizationUnit import OrganizationUnit
from ..tables.HealthCareProviderClassification import HealthCareProviderClassification
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.HealthCareProviderAreaOfSpecialization import (
    HealthCareProviderAreaOfSpecialization,
)
from ..tables.OrganizationUnitType import OrganizationUnitType
from ..tables.HealthCareProviderTypeCode import HealthCareProviderTypeCode


"""
Practitioner Organization Unit - ORG
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ORG TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ORG,
    SI, CE, CX, ID, DR
)

org = ORG(  #  - The ORG segment relates a practitioner to an organization unit and adds detailed information regarding the practitioner's practicing specialty in that organization unit
    set_id_org=si,  # SI(...)  # Required.
    organization_unit_code=None,  # CE(...) 
    organization_unit_type_code=None,  # CE(...) 
    primary_org_unit_indicator=None,  # ID(...) 
    practitioner_org_unit_identifier=None,  # CX(...) 
    health_care_provider_type_code=None,  # CE(...) 
    health_care_provider_classification_code=None,  # CE(...) 
    health_care_provider_area_of_specialization_code=None,  # CE(...) 
    effective_date_range=None,  # DR(...) 
    employment_status_code=None,  # CE(...) 
    board_approval_indicator=None,  # ID(...) 
    primary_care_physician_indicator=None,  # ID(...) 
)

-----END SEGMENT::ORG TEMPLATE-----
"""


class ORG(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ORG"""
    _hl7_name = """Practitioner Organization Unit"""
    _hl7_description = """The ORG segment relates a practitioner to an organization unit and adds detailed information regarding the practitioner's practicing specialty in that organization unit"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG"
    _c_length = (60, 250, 250, 1, 60, 250, 250, 250, 52, 250, 1, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, CE, CE, ID, CX, CE, CE, CE, DR, CE, ID, ID,)
    _c_aliases = ("ORG.1", "ORG.2", "ORG.3", "ORG.4", "ORG.5", "ORG.6", "ORG.7", "ORG.8", "ORG.9", "ORG.10", "ORG.11", "ORG.12",)
    _c_names = ("Set ID - ORG", "Organization Unit Code", "Organization Unit Type Code", "Primary Org Unit Indicator", "Practitioner Org Unit Identifier", "Health Care Provider Type Code", "Health Care Provider Classification Code", "Health Care Provider Area of Specialization Code", "Effective Date Range", "Employment Status Code", "Board Approval Indicator", "Primary Care Physician Indicator",)
    _c_attrs = ("set_id_org", "organization_unit_code", "organization_unit_type_code", "primary_org_unit_indicator", "practitioner_org_unit_identifier", "health_care_provider_type_code", "health_care_provider_classification_code", "health_care_provider_area_of_specialization_code", "effective_date_range", "employment_status_code", "board_approval_indicator", "primary_care_physician_indicator",)
    # fmt: on

    def __init__(
        self,
        set_id_org: SI | tuple[SI, ...],  # ORG.1
        organization_unit_code: OrganizationUnit
        | CE
        | tuple[OrganizationUnit | CE, ...]
        | None = None,  # ORG.2
        organization_unit_type_code: OrganizationUnitType
        | CE
        | tuple[OrganizationUnitType | CE, ...]
        | None = None,  # ORG.3
        primary_org_unit_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # ORG.4
        practitioner_org_unit_identifier: CX | tuple[CX, ...] | None = None,  # ORG.5
        health_care_provider_type_code: HealthCareProviderTypeCode
        | CE
        | tuple[HealthCareProviderTypeCode | CE, ...]
        | None = None,  # ORG.6
        health_care_provider_classification_code: HealthCareProviderClassification
        | CE
        | tuple[HealthCareProviderClassification | CE, ...]
        | None = None,  # ORG.7
        health_care_provider_area_of_specialization_code: HealthCareProviderAreaOfSpecialization
        | CE
        | tuple[HealthCareProviderAreaOfSpecialization | CE, ...]
        | None = None,  # ORG.8
        effective_date_range: DR | tuple[DR, ...] | None = None,  # ORG.9
        employment_status_code: EmploymentStatus
        | CE
        | tuple[EmploymentStatus | CE, ...]
        | None = None,  # ORG.10
        board_approval_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # ORG.11
        primary_care_physician_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # ORG.12
    ):
        """
        Practitioner Organization Unit - `ORG <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORG>`_
        The ORG segment relates a practitioner to an organization unit and adds detailed information regarding the practitioner's practicing specialty in that organization unit. An ORG segment may optionally follow an STF segment. An ORG segment must always have been preceded by a corresponding STF segment. If no organization unit is specified, this segment is used to relate practitioners with their practicing specialties, including effective and end dates. When it is not necessary to record organization unit or dates associated with the practicing specialty, this data is recorded in PRA-3-Practitioner Category.

        :param set_id_org: Sequence ID (id: ORG.1 | len: 60 | use: R | rpt: 1)
        :param organization_unit_code: Coded Element (id: ORG.2 | len: 250 | use: O | rpt: 1)
        :param organization_unit_type_code: Coded Element (id: ORG.3 | len: 250 | use: O | rpt: 1)
        :param primary_org_unit_indicator: Coded values for HL7 tables (id: ORG.4 | len: 1 | use: O | rpt: 1)
        :param practitioner_org_unit_identifier: Extended Composite ID with Check Digit (id: ORG.5 | len: 60 | use: O | rpt: 1)
        :param health_care_provider_type_code: Coded Element (id: ORG.6 | len: 250 | use: O | rpt: 1)
        :param health_care_provider_classification_code: Coded Element (id: ORG.7 | len: 250 | use: O | rpt: 1)
        :param health_care_provider_area_of_specialization_code: Coded Element (id: ORG.8 | len: 250 | use: O | rpt: 1)
        :param effective_date_range: Date/Time Range (id: ORG.9 | len: 52 | use: O | rpt: 1)
        :param employment_status_code: Coded Element (id: ORG.10 | len: 250 | use: O | rpt: 1)
        :param board_approval_indicator: Coded values for HL7 tables (id: ORG.11 | len: 1 | use: O | rpt: 1)
        :param primary_care_physician_indicator: Coded values for HL7 tables (id: ORG.12 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.set_id_org = set_id_org
        self.organization_unit_code = organization_unit_code
        self.organization_unit_type_code = organization_unit_type_code
        self.primary_org_unit_indicator = primary_org_unit_indicator
        self.practitioner_org_unit_identifier = practitioner_org_unit_identifier
        self.health_care_provider_type_code = health_care_provider_type_code
        self.health_care_provider_classification_code = (
            health_care_provider_classification_code
        )
        self.health_care_provider_area_of_specialization_code = (
            health_care_provider_area_of_specialization_code
        )
        self.effective_date_range = effective_date_range
        self.employment_status_code = employment_status_code
        self.board_approval_indicator = board_approval_indicator
        self.primary_care_physician_indicator = primary_care_physician_indicator

    @property  # get ORG.1
    def set_id_org(self) -> SI:
        """
        id: ORG.1 | len: 60 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.1
        """
        return self._c_data[0][0]

    @set_id_org.setter  # set ORG.1
    def set_id_org(self, si: SI):
        """
        id: ORG.1 | len: 60 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.1
        """
        self._c_data[0] = (si,)

    @property  # get ORG.2
    def organization_unit_code(self) -> OrganizationUnit | None:
        """
        id: ORG.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.2
        """
        return self._c_data[1][0]

    @organization_unit_code.setter  # set ORG.2
    def organization_unit_code(self, organization_unit: OrganizationUnit | None):
        """
        id: ORG.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.2
        """
        self._c_data[1] = (organization_unit,)

    @property  # get ORG.3
    def organization_unit_type_code(self) -> OrganizationUnitType | None:
        """
        id: ORG.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.3
        """
        return self._c_data[2][0]

    @organization_unit_type_code.setter  # set ORG.3
    def organization_unit_type_code(
        self, organization_unit_type: OrganizationUnitType | None
    ):
        """
        id: ORG.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.3
        """
        self._c_data[2] = (organization_unit_type,)

    @property  # get ORG.4
    def primary_org_unit_indicator(self) -> YesOrNoIndicator | None:
        """
        id: ORG.4 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.4
        """
        return self._c_data[3][0]

    @primary_org_unit_indicator.setter  # set ORG.4
    def primary_org_unit_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: ORG.4 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.4
        """
        self._c_data[3] = (yes_or_no_indicator,)

    @property  # get ORG.5
    def practitioner_org_unit_identifier(self) -> CX | None:
        """
        id: ORG.5 | len: 60 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.5
        """
        return self._c_data[4][0]

    @practitioner_org_unit_identifier.setter  # set ORG.5
    def practitioner_org_unit_identifier(self, cx: CX | None):
        """
        id: ORG.5 | len: 60 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.5
        """
        self._c_data[4] = (cx,)

    @property  # get ORG.6
    def health_care_provider_type_code(self) -> HealthCareProviderTypeCode | None:
        """
        id: ORG.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.6
        """
        return self._c_data[5][0]

    @health_care_provider_type_code.setter  # set ORG.6
    def health_care_provider_type_code(
        self, health_care_provider_type_code: HealthCareProviderTypeCode | None
    ):
        """
        id: ORG.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.6
        """
        self._c_data[5] = (health_care_provider_type_code,)

    @property  # get ORG.7
    def health_care_provider_classification_code(
        self,
    ) -> HealthCareProviderClassification | None:
        """
        id: ORG.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.7
        """
        return self._c_data[6][0]

    @health_care_provider_classification_code.setter  # set ORG.7
    def health_care_provider_classification_code(
        self,
        health_care_provider_classification: HealthCareProviderClassification | None,
    ):
        """
        id: ORG.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.7
        """
        self._c_data[6] = (health_care_provider_classification,)

    @property  # get ORG.8
    def health_care_provider_area_of_specialization_code(
        self,
    ) -> HealthCareProviderAreaOfSpecialization | None:
        """
        id: ORG.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.8
        """
        return self._c_data[7][0]

    @health_care_provider_area_of_specialization_code.setter  # set ORG.8
    def health_care_provider_area_of_specialization_code(
        self,
        health_care_provider_area_of_specialization: HealthCareProviderAreaOfSpecialization
        | None,
    ):
        """
        id: ORG.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.8
        """
        self._c_data[7] = (health_care_provider_area_of_specialization,)

    @property  # get ORG.9
    def effective_date_range(self) -> DR | None:
        """
        id: ORG.9 | len: 52 | use: O | rpt: 1
        ---
        return_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.9
        """
        return self._c_data[8][0]

    @effective_date_range.setter  # set ORG.9
    def effective_date_range(self, dr: DR | None):
        """
        id: ORG.9 | len: 52 | use: O | rpt: 1
        ---
        param_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.9
        """
        self._c_data[8] = (dr,)

    @property  # get ORG.10
    def employment_status_code(self) -> EmploymentStatus | None:
        """
        id: ORG.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.10
        """
        return self._c_data[9][0]

    @employment_status_code.setter  # set ORG.10
    def employment_status_code(self, employment_status: EmploymentStatus | None):
        """
        id: ORG.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.10
        """
        self._c_data[9] = (employment_status,)

    @property  # get ORG.11
    def board_approval_indicator(self) -> YesOrNoIndicator | None:
        """
        id: ORG.11 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.11
        """
        return self._c_data[10][0]

    @board_approval_indicator.setter  # set ORG.11
    def board_approval_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: ORG.11 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.11
        """
        self._c_data[10] = (yes_or_no_indicator,)

    @property  # get ORG.12
    def primary_care_physician_indicator(self) -> YesOrNoIndicator | None:
        """
        id: ORG.12 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.12
        """
        return self._c_data[11][0]

    @primary_care_physician_indicator.setter  # set ORG.12
    def primary_care_physician_indicator(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: ORG.12 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORG.12
        """
        self._c_data[11] = (yes_or_no_indicator,)
