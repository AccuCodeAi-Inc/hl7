from __future__ import annotations
from ...base import HL7Segment
from ..data_types.EIP import EIP
from ..data_types.CQ import CQ
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.DR import DR
from ..data_types.ST import ST
from ..data_types.CWE import CWE
from ..data_types.SI import SI
from ..data_types.TS import TS
from ..tables.SpecimenCollectionSite import SpecimenCollectionSite
from ..tables.ContainerCondition import ContainerCondition
from ..tables.SpecimenRole import SpecimenRole
from ..tables.SpecimenQuality import SpecimenQuality
from ..tables.SpecimenCollectionMethod import SpecimenCollectionMethod
from ..tables.SpecialHandlingCode import SpecialHandlingCode
from ..tables.RiskCodes import RiskCodes
from ..tables.SpecimenTypeModifier import SpecimenTypeModifier
from ..tables.SpecimenSourceTypeModifier import SpecimenSourceTypeModifier
from ..tables.AdditiveOrPreservative import AdditiveOrPreservative
from ..tables.SpecimenType import SpecimenType
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.SpecimenCondition import SpecimenCondition
from ..tables.SpecimenAppropriateness import SpecimenAppropriateness
from ..tables.SpecimenChildRole import SpecimenChildRole
from ..tables.SpecimenRejectReason import SpecimenRejectReason


"""
Specimen - SPM
HL7 Version: 2.5.1

-----BEGIN SEGMENT::SPM TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SPM,
    EIP, CQ, ID, NM, DR, ST, CWE, SI, TS
)

spm = SPM(  #  - The intent of this segment is to describe the characteristics of a specimen
    set_id_spm=None,  # SI(...) 
    specimen_id=None,  # EIP(...) 
    specimen_parent_ids=None,  # EIP(...) 
    specimen_type=cwe,  # CWE(...)  # Required.
    specimen_type_modifier=None,  # CWE(...) 
    specimen_additives=None,  # CWE(...) 
    specimen_collection_method=None,  # CWE(...) 
    specimen_source_site=None,  # CWE(...) 
    specimen_source_site_modifier=None,  # CWE(...) 
    specimen_collection_site=None,  # CWE(...) 
    specimen_role=None,  # CWE(...) 
    specimen_collection_amount=None,  # CQ(...) 
    grouped_specimen_count=None,  # NM(...) 
    specimen_description=None,  # ST(...) 
    specimen_handling_code=None,  # CWE(...) 
    specimen_risk_code=None,  # CWE(...) 
    specimen_collection_date_or_time=None,  # DR(...) 
    specimen_received_date_or_time=None,  # TS(...) 
    specimen_expiration_date_or_time=None,  # TS(...) 
    specimen_availability=None,  # ID(...) 
    specimen_reject_reason=None,  # CWE(...) 
    specimen_quality=None,  # CWE(...) 
    specimen_appropriateness=None,  # CWE(...) 
    specimen_condition=None,  # CWE(...) 
    specimen_current_quantity=None,  # CQ(...) 
    number_of_specimen_containers=None,  # NM(...) 
    container_type=None,  # CWE(...) 
    container_condition=None,  # CWE(...) 
    specimen_child_role=None,  # CWE(...) 
)

-----END SEGMENT::SPM TEMPLATE-----
"""


class SPM(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """SPM"""
    _hl7_name = """Specimen"""
    _hl7_description = """The intent of this segment is to describe the characteristics of a specimen"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM"
    _c_length = (4, 80, 80, 250, 250, 250, 250, 250, 250, 250, 250, 20, 6, 250, 250, 250, 26, 26, 26, 1, 250, 250, 250, 250, 20, 4, 250, 250, 250,)
    _c_rpt = (1, 1, 65535, 1, 65535, 65535, 1, 1, 65535, 1, 65535, 1, 1, 65535, 65535, 65535, 1, 1, 1, 1, 65535, 1, 1, 65535, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, EIP, EIP, CWE, CWE, CWE, CWE, CWE, CWE, CWE, CWE, CQ, NM, ST, CWE, CWE, DR, TS, TS, ID, CWE, CWE, CWE, CWE, CQ, NM, CWE, CWE, CWE,)
    _c_aliases = ("SPM.1", "SPM.2", "SPM.3", "SPM.4", "SPM.5", "SPM.6", "SPM.7", "SPM.8", "SPM.9", "SPM.10", "SPM.11", "SPM.12", "SPM.13", "SPM.14", "SPM.15", "SPM.16", "SPM.17", "SPM.18", "SPM.19", "SPM.20", "SPM.21", "SPM.22", "SPM.23", "SPM.24", "SPM.25", "SPM.26", "SPM.27", "SPM.28", "SPM.29",)
    _c_names = ("Set ID - SPM", "Specimen ID", "Specimen Parent IDs", "Specimen Type", "Specimen Type Modifier", "Specimen Additives", "Specimen Collection Method", "Specimen Source Site", "Specimen Source Site Modifier", "Specimen Collection Site", "Specimen Role", "Specimen Collection Amount", "Grouped Specimen Count", "Specimen Description", "Specimen Handling Code", "Specimen Risk Code", "Specimen Collection Date/Time", "Specimen Received Date/Time", "Specimen Expiration Date/Time", "Specimen Availability", "Specimen Reject Reason", "Specimen Quality", "Specimen Appropriateness", "Specimen Condition", "Specimen Current Quantity", "Number of Specimen Containers", "Container Type", "Container Condition", "Specimen Child Role",)
    _c_attrs = ("set_id_spm", "specimen_id", "specimen_parent_ids", "specimen_type", "specimen_type_modifier", "specimen_additives", "specimen_collection_method", "specimen_source_site", "specimen_source_site_modifier", "specimen_collection_site", "specimen_role", "specimen_collection_amount", "grouped_specimen_count", "specimen_description", "specimen_handling_code", "specimen_risk_code", "specimen_collection_date_or_time", "specimen_received_date_or_time", "specimen_expiration_date_or_time", "specimen_availability", "specimen_reject_reason", "specimen_quality", "specimen_appropriateness", "specimen_condition", "specimen_current_quantity", "number_of_specimen_containers", "container_type", "container_condition", "specimen_child_role",)
    # fmt: on

    def __init__(
        self,
        specimen_type: SpecimenType | CWE,  # SPM.4
        set_id_spm: SI | None = None,  # SPM.1
        specimen_id: EIP | None = None,  # SPM.2
        specimen_parent_ids: EIP | None = None,  # SPM.3
        specimen_type_modifier: SpecimenTypeModifier | CWE | None = None,  # SPM.5
        specimen_additives: AdditiveOrPreservative | CWE | None = None,  # SPM.6
        specimen_collection_method: SpecimenCollectionMethod
        | CWE
        | None = None,  # SPM.7
        specimen_source_site: CWE | None = None,  # SPM.8
        specimen_source_site_modifier: SpecimenSourceTypeModifier
        | CWE
        | None = None,  # SPM.9
        specimen_collection_site: SpecimenCollectionSite | CWE | None = None,  # SPM.10
        specimen_role: SpecimenRole | CWE | None = None,  # SPM.11
        specimen_collection_amount: CQ | None = None,  # SPM.12
        grouped_specimen_count: NM | None = None,  # SPM.13
        specimen_description: ST | None = None,  # SPM.14
        specimen_handling_code: SpecialHandlingCode | CWE | None = None,  # SPM.15
        specimen_risk_code: RiskCodes | CWE | None = None,  # SPM.16
        specimen_collection_date_or_time: DR | None = None,  # SPM.17
        specimen_received_date_or_time: TS | None = None,  # SPM.18
        specimen_expiration_date_or_time: TS | None = None,  # SPM.19
        specimen_availability: YesOrNoIndicator | ID | None = None,  # SPM.20
        specimen_reject_reason: SpecimenRejectReason | CWE | None = None,  # SPM.21
        specimen_quality: SpecimenQuality | CWE | None = None,  # SPM.22
        specimen_appropriateness: SpecimenAppropriateness | CWE | None = None,  # SPM.23
        specimen_condition: SpecimenCondition | CWE | None = None,  # SPM.24
        specimen_current_quantity: CQ | None = None,  # SPM.25
        number_of_specimen_containers: NM | None = None,  # SPM.26
        container_type: CWE | None = None,  # SPM.27
        container_condition: ContainerCondition | CWE | None = None,  # SPM.28
        specimen_child_role: SpecimenChildRole | CWE | None = None,  # SPM.29
    ):
        """
        Specimen - `SPM <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM>`_
        The intent of this segment is to describe the characteristics of a specimen. It differs from the intent of the OBR in that the OBR addresses order-specific information. It differs from the SAC segment in that the SAC addresses specimen container attributes. An advantage afforded by a separate specimen segment is that it generalizes the multiple relationships among order(s), results, specimen(s) and specimen container(s).

        :param set_id_spm: Sequence ID (id: SPM.1 | len: 4 | use: O | rpt: 1)
        :param specimen_id: Entity Identifier Pair (id: SPM.2 | len: 80 | use: O | rpt: 1)
        :param specimen_parent_ids: Entity Identifier Pair (id: SPM.3 | len: 80 | use: O | rpt: *)
        :param specimen_type: Coded with Exceptions (id: SPM.4 | len: 250 | use: R | rpt: 1)
        :param specimen_type_modifier: Coded with Exceptions (id: SPM.5 | len: 250 | use: O | rpt: *)
        :param specimen_additives: Coded with Exceptions (id: SPM.6 | len: 250 | use: O | rpt: *)
        :param specimen_collection_method: Coded with Exceptions (id: SPM.7 | len: 250 | use: O | rpt: 1)
        :param specimen_source_site: Coded with Exceptions (id: SPM.8 | len: 250 | use: O | rpt: 1)
        :param specimen_source_site_modifier: Coded with Exceptions (id: SPM.9 | len: 250 | use: O | rpt: *)
        :param specimen_collection_site: Coded with Exceptions (id: SPM.10 | len: 250 | use: O | rpt: 1)
        :param specimen_role: Coded with Exceptions (id: SPM.11 | len: 250 | use: O | rpt: *)
        :param specimen_collection_amount: Composite Quantity with Units (id: SPM.12 | len: 20 | use: O | rpt: 1)
        :param grouped_specimen_count: Numeric (id: SPM.13 | len: 6 | use: C | rpt: 1)
        :param specimen_description: String Data (id: SPM.14 | len: 250 | use: O | rpt: *)
        :param specimen_handling_code: Coded with Exceptions (id: SPM.15 | len: 250 | use: O | rpt: *)
        :param specimen_risk_code: Coded with Exceptions (id: SPM.16 | len: 250 | use: O | rpt: *)
        :param specimen_collection_date_or_time: Date/Time Range (id: SPM.17 | len: 26 | use: O | rpt: 1)
        :param specimen_received_date_or_time: Time Stamp (id: SPM.18 | len: 26 | use: O | rpt: 1)
        :param specimen_expiration_date_or_time: Time Stamp (id: SPM.19 | len: 26 | use: O | rpt: 1)
        :param specimen_availability: Coded values for HL7 tables (id: SPM.20 | len: 1 | use: O | rpt: 1)
        :param specimen_reject_reason: Coded with Exceptions (id: SPM.21 | len: 250 | use: O | rpt: *)
        :param specimen_quality: Coded with Exceptions (id: SPM.22 | len: 250 | use: O | rpt: 1)
        :param specimen_appropriateness: Coded with Exceptions (id: SPM.23 | len: 250 | use: O | rpt: 1)
        :param specimen_condition: Coded with Exceptions (id: SPM.24 | len: 250 | use: O | rpt: *)
        :param specimen_current_quantity: Composite Quantity with Units (id: SPM.25 | len: 20 | use: O | rpt: 1)
        :param number_of_specimen_containers: Numeric (id: SPM.26 | len: 4 | use: O | rpt: 1)
        :param container_type: Coded with Exceptions (id: SPM.27 | len: 250 | use: O | rpt: 1)
        :param container_condition: Coded with Exceptions (id: SPM.28 | len: 250 | use: O | rpt: 1)
        :param specimen_child_role: Coded with Exceptions (id: SPM.29 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 29
        self.set_id_spm = set_id_spm
        self.specimen_id = specimen_id
        self.specimen_parent_ids = specimen_parent_ids
        self.specimen_type = specimen_type
        self.specimen_type_modifier = specimen_type_modifier
        self.specimen_additives = specimen_additives
        self.specimen_collection_method = specimen_collection_method
        self.specimen_source_site = specimen_source_site
        self.specimen_source_site_modifier = specimen_source_site_modifier
        self.specimen_collection_site = specimen_collection_site
        self.specimen_role = specimen_role
        self.specimen_collection_amount = specimen_collection_amount
        self.grouped_specimen_count = grouped_specimen_count
        self.specimen_description = specimen_description
        self.specimen_handling_code = specimen_handling_code
        self.specimen_risk_code = specimen_risk_code
        self.specimen_collection_date_or_time = specimen_collection_date_or_time
        self.specimen_received_date_or_time = specimen_received_date_or_time
        self.specimen_expiration_date_or_time = specimen_expiration_date_or_time
        self.specimen_availability = specimen_availability
        self.specimen_reject_reason = specimen_reject_reason
        self.specimen_quality = specimen_quality
        self.specimen_appropriateness = specimen_appropriateness
        self.specimen_condition = specimen_condition
        self.specimen_current_quantity = specimen_current_quantity
        self.number_of_specimen_containers = number_of_specimen_containers
        self.container_type = container_type
        self.container_condition = container_condition
        self.specimen_child_role = specimen_child_role

    @property  # get SPM.1
    def set_id_spm(self) -> SI | None:
        """
        id: SPM.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.1
        """
        return self._c_data[0][0]

    @set_id_spm.setter  # set SPM.1
    def set_id_spm(self, si: SI | None):
        """
        id: SPM.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.1
        """
        self._c_data[0] = (si,)

    @property  # get SPM.2
    def specimen_id(self) -> EIP | None:
        """
        id: SPM.2 | len: 80 | use: O | rpt: 1
        ---
        return_type: EIP: Entity Identifier Pair
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.2
        """
        return self._c_data[1][0]

    @specimen_id.setter  # set SPM.2
    def specimen_id(self, eip: EIP | None):
        """
        id: SPM.2 | len: 80 | use: O | rpt: 1
        ---
        param_type: EIP: Entity Identifier Pair
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.2
        """
        self._c_data[1] = (eip,)

    @property
    def specimen_parent_ids(self) -> tuple[EIP, ...] | tuple[None]:
        """
        id: SPM.3 | len: 80 | use: O | rpt: *
        ---
        return_type: tuple[EIP, ...]: (Entity Identifier Pair, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.3
        """
        return self._c_data[2]

    @specimen_parent_ids.setter  # set SPM.3
    def specimen_parent_ids(self, eip: EIP | tuple[EIP] | None):
        """
        id: SPM.3 | len: 80 | use: O | rpt: *
        ---
        param_type: EIP | tuple[EIP, ...]: (Entity Identifier Pair, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.3
        """
        if isinstance(eip, tuple):
            self._c_data[2] = eip
        else:
            self._c_data[2] = (eip,)

    @property  # get SPM.4
    def specimen_type(self) -> SpecimenType:
        """
        id: SPM.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.4
        """
        return self._c_data[3][0]

    @specimen_type.setter  # set SPM.4
    def specimen_type(self, specimen_type: SpecimenType):
        """
        id: SPM.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.4
        """
        self._c_data[3] = (specimen_type,)

    @property
    def specimen_type_modifier(self) -> tuple[SpecimenTypeModifier, ...] | tuple[None]:
        """
        id: SPM.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.5
        """
        return self._c_data[4]

    @specimen_type_modifier.setter  # set SPM.5
    def specimen_type_modifier(
        self,
        specimen_type_modifier: SpecimenTypeModifier
        | tuple[SpecimenTypeModifier]
        | None,
    ):
        """
        id: SPM.5 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.5
        """
        if isinstance(specimen_type_modifier, tuple):
            self._c_data[4] = specimen_type_modifier
        else:
            self._c_data[4] = (specimen_type_modifier,)

    @property
    def specimen_additives(self) -> tuple[AdditiveOrPreservative, ...] | tuple[None]:
        """
        id: SPM.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.6
        """
        return self._c_data[5]

    @specimen_additives.setter  # set SPM.6
    def specimen_additives(
        self,
        additive_or_preservative: AdditiveOrPreservative
        | tuple[AdditiveOrPreservative]
        | None,
    ):
        """
        id: SPM.6 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.6
        """
        if isinstance(additive_or_preservative, tuple):
            self._c_data[5] = additive_or_preservative
        else:
            self._c_data[5] = (additive_or_preservative,)

    @property  # get SPM.7
    def specimen_collection_method(self) -> SpecimenCollectionMethod | None:
        """
        id: SPM.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.7
        """
        return self._c_data[6][0]

    @specimen_collection_method.setter  # set SPM.7
    def specimen_collection_method(
        self, specimen_collection_method: SpecimenCollectionMethod | None
    ):
        """
        id: SPM.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.7
        """
        self._c_data[6] = (specimen_collection_method,)

    @property  # get SPM.8
    def specimen_source_site(self) -> CWE | None:
        """
        id: SPM.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.8
        """
        return self._c_data[7][0]

    @specimen_source_site.setter  # set SPM.8
    def specimen_source_site(self, cwe: CWE | None):
        """
        id: SPM.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.8
        """
        self._c_data[7] = (cwe,)

    @property
    def specimen_source_site_modifier(
        self,
    ) -> tuple[SpecimenSourceTypeModifier, ...] | tuple[None]:
        """
        id: SPM.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.9
        """
        return self._c_data[8]

    @specimen_source_site_modifier.setter  # set SPM.9
    def specimen_source_site_modifier(
        self,
        specimen_source_type_modifier: SpecimenSourceTypeModifier
        | tuple[SpecimenSourceTypeModifier]
        | None,
    ):
        """
        id: SPM.9 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.9
        """
        if isinstance(specimen_source_type_modifier, tuple):
            self._c_data[8] = specimen_source_type_modifier
        else:
            self._c_data[8] = (specimen_source_type_modifier,)

    @property  # get SPM.10
    def specimen_collection_site(self) -> SpecimenCollectionSite | None:
        """
        id: SPM.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.10
        """
        return self._c_data[9][0]

    @specimen_collection_site.setter  # set SPM.10
    def specimen_collection_site(
        self, specimen_collection_site: SpecimenCollectionSite | None
    ):
        """
        id: SPM.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.10
        """
        self._c_data[9] = (specimen_collection_site,)

    @property
    def specimen_role(self) -> tuple[SpecimenRole, ...] | tuple[None]:
        """
        id: SPM.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.11
        """
        return self._c_data[10]

    @specimen_role.setter  # set SPM.11
    def specimen_role(self, specimen_role: SpecimenRole | tuple[SpecimenRole] | None):
        """
        id: SPM.11 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.11
        """
        if isinstance(specimen_role, tuple):
            self._c_data[10] = specimen_role
        else:
            self._c_data[10] = (specimen_role,)

    @property  # get SPM.12
    def specimen_collection_amount(self) -> CQ | None:
        """
        id: SPM.12 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.12
        """
        return self._c_data[11][0]

    @specimen_collection_amount.setter  # set SPM.12
    def specimen_collection_amount(self, cq: CQ | None):
        """
        id: SPM.12 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.12
        """
        self._c_data[11] = (cq,)

    @property  # get SPM.13
    def grouped_specimen_count(self) -> NM | None:
        """
        id: SPM.13 | len: 6 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.13
        """
        return self._c_data[12][0]

    @grouped_specimen_count.setter  # set SPM.13
    def grouped_specimen_count(self, nm: NM | None):
        """
        id: SPM.13 | len: 6 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.13
        """
        self._c_data[12] = (nm,)

    @property
    def specimen_description(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: SPM.14 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.14
        """
        return self._c_data[13]

    @specimen_description.setter  # set SPM.14
    def specimen_description(self, st: ST | tuple[ST] | None):
        """
        id: SPM.14 | len: 250 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.14
        """
        if isinstance(st, tuple):
            self._c_data[13] = st
        else:
            self._c_data[13] = (st,)

    @property
    def specimen_handling_code(self) -> tuple[SpecialHandlingCode, ...] | tuple[None]:
        """
        id: SPM.15 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.15
        """
        return self._c_data[14]

    @specimen_handling_code.setter  # set SPM.15
    def specimen_handling_code(
        self,
        special_handling_code: SpecialHandlingCode | tuple[SpecialHandlingCode] | None,
    ):
        """
        id: SPM.15 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.15
        """
        if isinstance(special_handling_code, tuple):
            self._c_data[14] = special_handling_code
        else:
            self._c_data[14] = (special_handling_code,)

    @property
    def specimen_risk_code(self) -> tuple[RiskCodes, ...] | tuple[None]:
        """
        id: SPM.16 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.16
        """
        return self._c_data[15]

    @specimen_risk_code.setter  # set SPM.16
    def specimen_risk_code(self, risk_codes: RiskCodes | tuple[RiskCodes] | None):
        """
        id: SPM.16 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.16
        """
        if isinstance(risk_codes, tuple):
            self._c_data[15] = risk_codes
        else:
            self._c_data[15] = (risk_codes,)

    @property  # get SPM.17
    def specimen_collection_date_or_time(self) -> DR | None:
        """
        id: SPM.17 | len: 26 | use: O | rpt: 1
        ---
        return_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.17
        """
        return self._c_data[16][0]

    @specimen_collection_date_or_time.setter  # set SPM.17
    def specimen_collection_date_or_time(self, dr: DR | None):
        """
        id: SPM.17 | len: 26 | use: O | rpt: 1
        ---
        param_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.17
        """
        self._c_data[16] = (dr,)

    @property  # get SPM.18
    def specimen_received_date_or_time(self) -> TS | None:
        """
        id: SPM.18 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.18
        """
        return self._c_data[17][0]

    @specimen_received_date_or_time.setter  # set SPM.18
    def specimen_received_date_or_time(self, ts: TS | None):
        """
        id: SPM.18 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.18
        """
        self._c_data[17] = (ts,)

    @property  # get SPM.19
    def specimen_expiration_date_or_time(self) -> TS | None:
        """
        id: SPM.19 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.19
        """
        return self._c_data[18][0]

    @specimen_expiration_date_or_time.setter  # set SPM.19
    def specimen_expiration_date_or_time(self, ts: TS | None):
        """
        id: SPM.19 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.19
        """
        self._c_data[18] = (ts,)

    @property  # get SPM.20
    def specimen_availability(self) -> YesOrNoIndicator | None:
        """
        id: SPM.20 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.20
        """
        return self._c_data[19][0]

    @specimen_availability.setter  # set SPM.20
    def specimen_availability(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: SPM.20 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.20
        """
        self._c_data[19] = (yes_or_no_indicator,)

    @property
    def specimen_reject_reason(self) -> tuple[SpecimenRejectReason, ...] | tuple[None]:
        """
        id: SPM.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.21
        """
        return self._c_data[20]

    @specimen_reject_reason.setter  # set SPM.21
    def specimen_reject_reason(
        self,
        specimen_reject_reason: SpecimenRejectReason
        | tuple[SpecimenRejectReason]
        | None,
    ):
        """
        id: SPM.21 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.21
        """
        if isinstance(specimen_reject_reason, tuple):
            self._c_data[20] = specimen_reject_reason
        else:
            self._c_data[20] = (specimen_reject_reason,)

    @property  # get SPM.22
    def specimen_quality(self) -> SpecimenQuality | None:
        """
        id: SPM.22 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.22
        """
        return self._c_data[21][0]

    @specimen_quality.setter  # set SPM.22
    def specimen_quality(self, specimen_quality: SpecimenQuality | None):
        """
        id: SPM.22 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.22
        """
        self._c_data[21] = (specimen_quality,)

    @property  # get SPM.23
    def specimen_appropriateness(self) -> SpecimenAppropriateness | None:
        """
        id: SPM.23 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.23
        """
        return self._c_data[22][0]

    @specimen_appropriateness.setter  # set SPM.23
    def specimen_appropriateness(
        self, specimen_appropriateness: SpecimenAppropriateness | None
    ):
        """
        id: SPM.23 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.23
        """
        self._c_data[22] = (specimen_appropriateness,)

    @property
    def specimen_condition(self) -> tuple[SpecimenCondition, ...] | tuple[None]:
        """
        id: SPM.24 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.24
        """
        return self._c_data[23]

    @specimen_condition.setter  # set SPM.24
    def specimen_condition(
        self, specimen_condition: SpecimenCondition | tuple[SpecimenCondition] | None
    ):
        """
        id: SPM.24 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.24
        """
        if isinstance(specimen_condition, tuple):
            self._c_data[23] = specimen_condition
        else:
            self._c_data[23] = (specimen_condition,)

    @property  # get SPM.25
    def specimen_current_quantity(self) -> CQ | None:
        """
        id: SPM.25 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.25
        """
        return self._c_data[24][0]

    @specimen_current_quantity.setter  # set SPM.25
    def specimen_current_quantity(self, cq: CQ | None):
        """
        id: SPM.25 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.25
        """
        self._c_data[24] = (cq,)

    @property  # get SPM.26
    def number_of_specimen_containers(self) -> NM | None:
        """
        id: SPM.26 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.26
        """
        return self._c_data[25][0]

    @number_of_specimen_containers.setter  # set SPM.26
    def number_of_specimen_containers(self, nm: NM | None):
        """
        id: SPM.26 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.26
        """
        self._c_data[25] = (nm,)

    @property  # get SPM.27
    def container_type(self) -> CWE | None:
        """
        id: SPM.27 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.27
        """
        return self._c_data[26][0]

    @container_type.setter  # set SPM.27
    def container_type(self, cwe: CWE | None):
        """
        id: SPM.27 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.27
        """
        self._c_data[26] = (cwe,)

    @property  # get SPM.28
    def container_condition(self) -> ContainerCondition | None:
        """
        id: SPM.28 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.28
        """
        return self._c_data[27][0]

    @container_condition.setter  # set SPM.28
    def container_condition(self, container_condition: ContainerCondition | None):
        """
        id: SPM.28 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.28
        """
        self._c_data[27] = (container_condition,)

    @property  # get SPM.29
    def specimen_child_role(self) -> SpecimenChildRole | None:
        """
        id: SPM.29 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.29
        """
        return self._c_data[28][0]

    @specimen_child_role.setter  # set SPM.29
    def specimen_child_role(self, specimen_child_role: SpecimenChildRole | None):
        """
        id: SPM.29 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPM.29
        """
        self._c_data[28] = (specimen_child_role,)
