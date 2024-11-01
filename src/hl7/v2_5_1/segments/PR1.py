from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.IS import IS
from ..data_types.EI import EI
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.ST import ST
from ..data_types.XCN import XCN
from ..data_types.SI import SI
from ..data_types.TS import TS
from ..tables.ProcedureFunctionalType import ProcedureFunctionalType
from ..tables.SegmentActionCode import SegmentActionCode
from ..tables.ProcedurePriority import ProcedurePriority
from ..tables.ConsentCode import ConsentCode
from ..tables.PhysicianId import PhysicianId
from ..tables.ProcedureCodeModifier import ProcedureCodeModifier
from ..tables.ProcedureCode import ProcedureCode
from ..tables.AnesthesiaCode import AnesthesiaCode
from ..tables.DiagnosisCode import DiagnosisCode
from ..tables.ProcedureDrgType import ProcedureDrgType
from ..tables.ProcedureCodingMethod import ProcedureCodingMethod
from ..tables.TissueTypeCode import TissueTypeCode


"""
Procedures - PR1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PR1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PR1,
    CE, IS, EI, ID, NM, ST, XCN, SI, TS
)

pr1 = PR1(  #  - The PR1 segment contains information relative to various types of procedures that can be performed on a patient
    set_id_pr1=si,  # SI(...)  # Required.
    procedure_coding_method=None,  # IS(...) 
    procedure_code=ce,  # CE(...)  # Required.
    procedure_description=None,  # ST(...) 
    procedure_date_or_time=ts,  # TS(...)  # Required.
    procedure_functional_type=None,  # IS(...) 
    procedure_minutes=None,  # NM(...) 
    anesthesiologist=None,  # XCN(...) 
    anesthesia_code=None,  # IS(...) 
    anesthesia_minutes=None,  # NM(...) 
    surgeon=None,  # XCN(...) 
    procedure_practitioner=None,  # XCN(...) 
    consent_code=None,  # CE(...) 
    procedure_priority=None,  # ID(...) 
    associated_diagnosis_code=None,  # CE(...) 
    procedure_code_modifier=None,  # CE(...) 
    procedure_drg_type=None,  # IS(...) 
    tissue_type_code=None,  # CE(...) 
    procedure_identifier=None,  # EI(...) 
    procedure_action_code=None,  # ID(...) 
)

-----END SEGMENT::PR1 TEMPLATE-----
"""


class PR1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PR1"""
    _hl7_name = """Procedures"""
    _hl7_description = """The PR1 segment contains information relative to various types of procedures that can be performed on a patient"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1"
    _c_length = (4, 3, 250, 40, 26, 2, 4, 250, 2, 4, 250, 250, 250, 2, 250, 250, 20, 250, 427, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 65535, 65535, 1, 1, 1, 65535, 1, 65535, 1, 1,)
    _c_usage = ("R", "B", "R", "B", "R", "O", "O", "B", "O", "O", "B", "B", "O", "O", "O", "O", "O", "O", "C", "C",)
    _c_components = (SI, IS, CE, ST, TS, IS, NM, XCN, IS, NM, XCN, XCN, CE, ID, CE, CE, IS, CE, EI, ID,)
    _c_aliases = ("PR1.1", "PR1.2", "PR1.3", "PR1.4", "PR1.5", "PR1.6", "PR1.7", "PR1.8", "PR1.9", "PR1.10", "PR1.11", "PR1.12", "PR1.13", "PR1.14", "PR1.15", "PR1.16", "PR1.17", "PR1.18", "PR1.19", "PR1.20",)
    _c_names = ("Set ID - PR1", "Procedure Coding Method", "Procedure Code", "Procedure Description", "Procedure Date/Time", "Procedure Functional Type", "Procedure Minutes", "Anesthesiologist", "Anesthesia Code", "Anesthesia Minutes", "Surgeon", "Procedure Practitioner", "Consent Code", "Procedure Priority", "Associated Diagnosis Code", "Procedure Code Modifier", "Procedure DRG Type", "Tissue Type Code", "Procedure Identifier", "Procedure Action Code",)
    _c_attrs = ("set_id_pr1", "procedure_coding_method", "procedure_code", "procedure_description", "procedure_date_or_time", "procedure_functional_type", "procedure_minutes", "anesthesiologist", "anesthesia_code", "anesthesia_minutes", "surgeon", "procedure_practitioner", "consent_code", "procedure_priority", "associated_diagnosis_code", "procedure_code_modifier", "procedure_drg_type", "tissue_type_code", "procedure_identifier", "procedure_action_code",)
    # fmt: on

    def __init__(
        self,
        set_id_pr1: SI,  # PR1.1
        procedure_code: ProcedureCode | CE,  # PR1.3
        procedure_date_or_time: TS,  # PR1.5
        procedure_coding_method: ProcedureCodingMethod | IS | None = None,  # PR1.2
        procedure_description: ST | None = None,  # PR1.4
        procedure_functional_type: ProcedureFunctionalType | IS | None = None,  # PR1.6
        procedure_minutes: NM | None = None,  # PR1.7
        anesthesiologist: PhysicianId | XCN | None = None,  # PR1.8
        anesthesia_code: AnesthesiaCode | IS | None = None,  # PR1.9
        anesthesia_minutes: NM | None = None,  # PR1.10
        surgeon: PhysicianId | XCN | None = None,  # PR1.11
        procedure_practitioner: PhysicianId | XCN | None = None,  # PR1.12
        consent_code: ConsentCode | CE | None = None,  # PR1.13
        procedure_priority: ProcedurePriority | ID | None = None,  # PR1.14
        associated_diagnosis_code: DiagnosisCode | CE | None = None,  # PR1.15
        procedure_code_modifier: ProcedureCodeModifier | CE | None = None,  # PR1.16
        procedure_drg_type: ProcedureDrgType | IS | None = None,  # PR1.17
        tissue_type_code: TissueTypeCode | CE | None = None,  # PR1.18
        procedure_identifier: EI | None = None,  # PR1.19
        procedure_action_code: SegmentActionCode | ID | None = None,  # PR1.20
    ):
        """
        Procedures - `PR1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PR1>`_
        The PR1 segment contains information relative to various types of procedures that can be performed on a patient. The PR1 segment can be used to send procedure information, for example: Surgical, Nuclear Medicine, X-ray with contrast, etc. The PR1 segment is used to send multiple procedures, for example, for medical records encoding or for billing systems.

        :param set_id_pr1: Sequence ID (id: PR1.1 | len: 4 | use: R | rpt: 1)
        :param procedure_coding_method: Coded value for user-defined tables (id: PR1.2 | len: 3 | use: B | rpt: 1)
        :param procedure_code: Coded Element (id: PR1.3 | len: 250 | use: R | rpt: 1)
        :param procedure_description: String Data (id: PR1.4 | len: 40 | use: B | rpt: 1)
        :param procedure_date_or_time: Time Stamp (id: PR1.5 | len: 26 | use: R | rpt: 1)
        :param procedure_functional_type: Coded value for user-defined tables (id: PR1.6 | len: 2 | use: O | rpt: 1)
        :param procedure_minutes: Numeric (id: PR1.7 | len: 4 | use: O | rpt: 1)
        :param anesthesiologist: Extended Composite ID Number and Name for Persons (id: PR1.8 | len: 250 | use: B | rpt: *)
        :param anesthesia_code: Coded value for user-defined tables (id: PR1.9 | len: 2 | use: O | rpt: 1)
        :param anesthesia_minutes: Numeric (id: PR1.10 | len: 4 | use: O | rpt: 1)
        :param surgeon: Extended Composite ID Number and Name for Persons (id: PR1.11 | len: 250 | use: B | rpt: *)
        :param procedure_practitioner: Extended Composite ID Number and Name for Persons (id: PR1.12 | len: 250 | use: B | rpt: *)
        :param consent_code: Coded Element (id: PR1.13 | len: 250 | use: O | rpt: 1)
        :param procedure_priority: Coded values for HL7 tables (id: PR1.14 | len: 2 | use: O | rpt: 1)
        :param associated_diagnosis_code: Coded Element (id: PR1.15 | len: 250 | use: O | rpt: 1)
        :param procedure_code_modifier: Coded Element (id: PR1.16 | len: 250 | use: O | rpt: *)
        :param procedure_drg_type: Coded value for user-defined tables (id: PR1.17 | len: 20 | use: O | rpt: 1)
        :param tissue_type_code: Coded Element (id: PR1.18 | len: 250 | use: O | rpt: *)
        :param procedure_identifier: Entity Identifier (id: PR1.19 | len: 427 | use: C | rpt: 1)
        :param procedure_action_code: Coded values for HL7 tables (id: PR1.20 | len: 1 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 20
        self.set_id_pr1 = set_id_pr1
        self.procedure_coding_method = procedure_coding_method
        self.procedure_code = procedure_code
        self.procedure_description = procedure_description
        self.procedure_date_or_time = procedure_date_or_time
        self.procedure_functional_type = procedure_functional_type
        self.procedure_minutes = procedure_minutes
        self.anesthesiologist = anesthesiologist
        self.anesthesia_code = anesthesia_code
        self.anesthesia_minutes = anesthesia_minutes
        self.surgeon = surgeon
        self.procedure_practitioner = procedure_practitioner
        self.consent_code = consent_code
        self.procedure_priority = procedure_priority
        self.associated_diagnosis_code = associated_diagnosis_code
        self.procedure_code_modifier = procedure_code_modifier
        self.procedure_drg_type = procedure_drg_type
        self.tissue_type_code = tissue_type_code
        self.procedure_identifier = procedure_identifier
        self.procedure_action_code = procedure_action_code

    @property  # get PR1.1
    def set_id_pr1(self) -> SI:
        """
        id: PR1.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.1
        """
        return self._c_data[0][0]

    @set_id_pr1.setter  # set PR1.1
    def set_id_pr1(self, si: SI):
        """
        id: PR1.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.1
        """
        self._c_data[0] = (si,)

    @property  # get PR1.2
    def procedure_coding_method(self) -> ProcedureCodingMethod | None:
        """
        id: PR1.2 | len: 3 | use: B | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.2
        """
        return self._c_data[1][0]

    @procedure_coding_method.setter  # set PR1.2
    def procedure_coding_method(
        self, procedure_coding_method: ProcedureCodingMethod | None
    ):
        """
        id: PR1.2 | len: 3 | use: B | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.2
        """
        self._c_data[1] = (procedure_coding_method,)

    @property  # get PR1.3
    def procedure_code(self) -> ProcedureCode:
        """
        id: PR1.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.3
        """
        return self._c_data[2][0]

    @procedure_code.setter  # set PR1.3
    def procedure_code(self, procedure_code: ProcedureCode):
        """
        id: PR1.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.3
        """
        self._c_data[2] = (procedure_code,)

    @property  # get PR1.4
    def procedure_description(self) -> ST | None:
        """
        id: PR1.4 | len: 40 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.4
        """
        return self._c_data[3][0]

    @procedure_description.setter  # set PR1.4
    def procedure_description(self, st: ST | None):
        """
        id: PR1.4 | len: 40 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.4
        """
        self._c_data[3] = (st,)

    @property  # get PR1.5
    def procedure_date_or_time(self) -> TS:
        """
        id: PR1.5 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.5
        """
        return self._c_data[4][0]

    @procedure_date_or_time.setter  # set PR1.5
    def procedure_date_or_time(self, ts: TS):
        """
        id: PR1.5 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.5
        """
        self._c_data[4] = (ts,)

    @property  # get PR1.6
    def procedure_functional_type(self) -> ProcedureFunctionalType | None:
        """
        id: PR1.6 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.6
        """
        return self._c_data[5][0]

    @procedure_functional_type.setter  # set PR1.6
    def procedure_functional_type(
        self, procedure_functional_type: ProcedureFunctionalType | None
    ):
        """
        id: PR1.6 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.6
        """
        self._c_data[5] = (procedure_functional_type,)

    @property  # get PR1.7
    def procedure_minutes(self) -> NM | None:
        """
        id: PR1.7 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.7
        """
        return self._c_data[6][0]

    @procedure_minutes.setter  # set PR1.7
    def procedure_minutes(self, nm: NM | None):
        """
        id: PR1.7 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.7
        """
        self._c_data[6] = (nm,)

    @property
    def anesthesiologist(self) -> tuple[PhysicianId, ...] | tuple[None]:
        """
        id: PR1.8 | len: 250 | use: B | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.8
        """
        return self._c_data[7]

    @anesthesiologist.setter  # set PR1.8
    def anesthesiologist(self, physician_id: PhysicianId | tuple[PhysicianId] | None):
        """
        id: PR1.8 | len: 250 | use: B | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.8
        """
        if isinstance(physician_id, tuple):
            self._c_data[7] = physician_id
        else:
            self._c_data[7] = (physician_id,)

    @property  # get PR1.9
    def anesthesia_code(self) -> AnesthesiaCode | None:
        """
        id: PR1.9 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.9
        """
        return self._c_data[8][0]

    @anesthesia_code.setter  # set PR1.9
    def anesthesia_code(self, anesthesia_code: AnesthesiaCode | None):
        """
        id: PR1.9 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.9
        """
        self._c_data[8] = (anesthesia_code,)

    @property  # get PR1.10
    def anesthesia_minutes(self) -> NM | None:
        """
        id: PR1.10 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.10
        """
        return self._c_data[9][0]

    @anesthesia_minutes.setter  # set PR1.10
    def anesthesia_minutes(self, nm: NM | None):
        """
        id: PR1.10 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.10
        """
        self._c_data[9] = (nm,)

    @property
    def surgeon(self) -> tuple[PhysicianId, ...] | tuple[None]:
        """
        id: PR1.11 | len: 250 | use: B | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.11
        """
        return self._c_data[10]

    @surgeon.setter  # set PR1.11
    def surgeon(self, physician_id: PhysicianId | tuple[PhysicianId] | None):
        """
        id: PR1.11 | len: 250 | use: B | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.11
        """
        if isinstance(physician_id, tuple):
            self._c_data[10] = physician_id
        else:
            self._c_data[10] = (physician_id,)

    @property
    def procedure_practitioner(self) -> tuple[PhysicianId, ...] | tuple[None]:
        """
        id: PR1.12 | len: 250 | use: B | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.12
        """
        return self._c_data[11]

    @procedure_practitioner.setter  # set PR1.12
    def procedure_practitioner(
        self, physician_id: PhysicianId | tuple[PhysicianId] | None
    ):
        """
        id: PR1.12 | len: 250 | use: B | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.12
        """
        if isinstance(physician_id, tuple):
            self._c_data[11] = physician_id
        else:
            self._c_data[11] = (physician_id,)

    @property  # get PR1.13
    def consent_code(self) -> ConsentCode | None:
        """
        id: PR1.13 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.13
        """
        return self._c_data[12][0]

    @consent_code.setter  # set PR1.13
    def consent_code(self, consent_code: ConsentCode | None):
        """
        id: PR1.13 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.13
        """
        self._c_data[12] = (consent_code,)

    @property  # get PR1.14
    def procedure_priority(self) -> ProcedurePriority | None:
        """
        id: PR1.14 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.14
        """
        return self._c_data[13][0]

    @procedure_priority.setter  # set PR1.14
    def procedure_priority(self, procedure_priority: ProcedurePriority | None):
        """
        id: PR1.14 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.14
        """
        self._c_data[13] = (procedure_priority,)

    @property  # get PR1.15
    def associated_diagnosis_code(self) -> DiagnosisCode | None:
        """
        id: PR1.15 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.15
        """
        return self._c_data[14][0]

    @associated_diagnosis_code.setter  # set PR1.15
    def associated_diagnosis_code(self, diagnosis_code: DiagnosisCode | None):
        """
        id: PR1.15 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.15
        """
        self._c_data[14] = (diagnosis_code,)

    @property
    def procedure_code_modifier(
        self,
    ) -> tuple[ProcedureCodeModifier, ...] | tuple[None]:
        """
        id: PR1.16 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.16
        """
        return self._c_data[15]

    @procedure_code_modifier.setter  # set PR1.16
    def procedure_code_modifier(
        self,
        procedure_code_modifier: ProcedureCodeModifier
        | tuple[ProcedureCodeModifier]
        | None,
    ):
        """
        id: PR1.16 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.16
        """
        if isinstance(procedure_code_modifier, tuple):
            self._c_data[15] = procedure_code_modifier
        else:
            self._c_data[15] = (procedure_code_modifier,)

    @property  # get PR1.17
    def procedure_drg_type(self) -> ProcedureDrgType | None:
        """
        id: PR1.17 | len: 20 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.17
        """
        return self._c_data[16][0]

    @procedure_drg_type.setter  # set PR1.17
    def procedure_drg_type(self, procedure_drg_type: ProcedureDrgType | None):
        """
        id: PR1.17 | len: 20 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.17
        """
        self._c_data[16] = (procedure_drg_type,)

    @property
    def tissue_type_code(self) -> tuple[TissueTypeCode, ...] | tuple[None]:
        """
        id: PR1.18 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.18
        """
        return self._c_data[17]

    @tissue_type_code.setter  # set PR1.18
    def tissue_type_code(
        self, tissue_type_code: TissueTypeCode | tuple[TissueTypeCode] | None
    ):
        """
        id: PR1.18 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.18
        """
        if isinstance(tissue_type_code, tuple):
            self._c_data[17] = tissue_type_code
        else:
            self._c_data[17] = (tissue_type_code,)

    @property  # get PR1.19
    def procedure_identifier(self) -> EI | None:
        """
        id: PR1.19 | len: 427 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.19
        """
        return self._c_data[18][0]

    @procedure_identifier.setter  # set PR1.19
    def procedure_identifier(self, ei: EI | None):
        """
        id: PR1.19 | len: 427 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.19
        """
        self._c_data[18] = (ei,)

    @property  # get PR1.20
    def procedure_action_code(self) -> SegmentActionCode | None:
        """
        id: PR1.20 | len: 1 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.20
        """
        return self._c_data[19][0]

    @procedure_action_code.setter  # set PR1.20
    def procedure_action_code(self, segment_action_code: SegmentActionCode | None):
        """
        id: PR1.20 | len: 1 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PR1.20
        """
        self._c_data[19] = (segment_action_code,)
