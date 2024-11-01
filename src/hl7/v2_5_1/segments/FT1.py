from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.CNE import CNE
from ..data_types.NM import NM
from ..data_types.CP import CP
from ..data_types.PL import PL
from ..data_types.IS import IS
from ..data_types.DR import DR
from ..data_types.CX import CX
from ..data_types.EI import EI
from ..data_types.CWE import CWE
from ..data_types.ST import ST
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.XCN import XCN
from ..tables.AdvancedBeneficiaryNoticeCode import AdvancedBeneficiaryNoticeCode
from ..tables.MedicallyNecessaryDuplicateProcedureReason import (
    MedicallyNecessaryDuplicateProcedureReason,
)
from ..tables.InsurancePlanId import InsurancePlanId
from ..tables.PerformedBy import PerformedBy
from ..tables.ProcedureCode import ProcedureCode
from ..tables.TransactionType import TransactionType
from ..tables.DiagnosisCode import DiagnosisCode
from ..tables.NdcCodes import NdcCodes
from ..tables.DepartmentCode import DepartmentCode
from ..tables.ProcedureCodeModifier import ProcedureCodeModifier
from ..tables.TransactionCode import TransactionCode
from ..tables.PatientType import PatientType
from ..tables.FeeSchedule import FeeSchedule


"""
Financial Transaction - FT1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::FT1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    FT1,
    TS, CNE, NM, CP, PL, IS, DR, CX, EI, CWE, ST, SI, CE, XCN
)

ft1 = FT1(  #  - The FT1 segment contains the detail data necessary to post charges, payments, adjustments, etc
    set_id_ft1=None,  # SI(...) 
    transaction_id=None,  # ST(...) 
    transaction_batch_id=None,  # ST(...) 
    transaction_date=dr,  # DR(...)  # Required.
    transaction_posting_date=None,  # TS(...) 
    transaction_type=_is,  # IS(...)  # Required.
    transaction_code=ce,  # CE(...)  # Required.
    transaction_description=None,  # ST(...) 
    transaction_description_alt=None,  # ST(...) 
    transaction_quantity=None,  # NM(...) 
    transaction_amount_extended=None,  # CP(...) 
    transaction_amount_unit=None,  # CP(...) 
    department_code=None,  # CE(...) 
    insurance_plan_id=None,  # CE(...) 
    insurance_amount=None,  # CP(...) 
    assigned_patient_location=None,  # PL(...) 
    fee_schedule=None,  # IS(...) 
    patient_type=None,  # IS(...) 
    diagnosis_code_ft1=None,  # CE(...) 
    performed_by_code=None,  # XCN(...) 
    ordered_by_code=None,  # XCN(...) 
    unit_cost=None,  # CP(...) 
    filler_order_number=None,  # EI(...) 
    entered_by_code=None,  # XCN(...) 
    procedure_code=None,  # CE(...) 
    procedure_code_modifier=None,  # CE(...) 
    advanced_beneficiary_notice_code=None,  # CE(...) 
    medically_necessary_duplicate_procedure_reason=None,  # CWE(...) 
    ndc_code=None,  # CNE(...) 
    payment_reference_id=None,  # CX(...) 
    transaction_reference_key=None,  # SI(...) 
)

-----END SEGMENT::FT1 TEMPLATE-----
"""


class FT1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """FT1"""
    _hl7_name = """Financial Transaction"""
    _hl7_description = """The FT1 segment contains the detail data necessary to post charges, payments, adjustments, etc"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1"
    _c_length = (4, 12, 10, 53, 26, 8, 250, 40, 40, 6, 12, 12, 250, 250, 12, 80, 1, 2, 250, 250, 250, 12, 427, 250, 250, 250, 250, 250, 250, 250, 4,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 65535, 65535, 1, 1, 65535, 1, 65535, 1, 1, 1, 1, 65535,)
    _c_usage = ("O", "O", "O", "R", "O", "R", "R", "B", "B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, ST, ST, DR, TS, IS, CE, ST, ST, NM, CP, CP, CE, CE, CP, PL, IS, IS, CE, XCN, XCN, CP, EI, XCN, CE, CE, CE, CWE, CNE, CX, SI,)
    _c_aliases = ("FT1.1", "FT1.2", "FT1.3", "FT1.4", "FT1.5", "FT1.6", "FT1.7", "FT1.8", "FT1.9", "FT1.10", "FT1.11", "FT1.12", "FT1.13", "FT1.14", "FT1.15", "FT1.16", "FT1.17", "FT1.18", "FT1.19", "FT1.20", "FT1.21", "FT1.22", "FT1.23", "FT1.24", "FT1.25", "FT1.26", "FT1.27", "FT1.28", "FT1.29", "FT1.30", "FT1.31",)
    _c_names = ("Set ID - FT1", "Transaction ID", "Transaction Batch ID", "Transaction Date", "Transaction Posting Date", "Transaction Type", "Transaction Code", "Transaction Description", "Transaction Description - Alt", "Transaction Quantity", "Transaction Amount - Extended", "Transaction Amount - Unit", "Department Code", "Insurance Plan ID", "Insurance Amount", "Assigned Patient Location", "Fee Schedule", "Patient Type", "Diagnosis Code - FT1", "Performed By Code", "Ordered By Code", "Unit Cost", "Filler Order Number", "Entered By Code", "Procedure Code", "Procedure Code Modifier", "Advanced Beneficiary Notice Code", "Medically Necessary Duplicate Procedure Reason.", "NDC Code", "Payment Reference ID", "Transaction Reference Key",)
    _c_attrs = ("set_id_ft1", "transaction_id", "transaction_batch_id", "transaction_date", "transaction_posting_date", "transaction_type", "transaction_code", "transaction_description", "transaction_description_alt", "transaction_quantity", "transaction_amount_extended", "transaction_amount_unit", "department_code", "insurance_plan_id", "insurance_amount", "assigned_patient_location", "fee_schedule", "patient_type", "diagnosis_code_ft1", "performed_by_code", "ordered_by_code", "unit_cost", "filler_order_number", "entered_by_code", "procedure_code", "procedure_code_modifier", "advanced_beneficiary_notice_code", "medically_necessary_duplicate_procedure_reason", "ndc_code", "payment_reference_id", "transaction_reference_key",)
    # fmt: on

    def __init__(
        self,
        transaction_date: DR | tuple[DR],  # FT1.4
        transaction_type: TransactionType | IS | tuple[TransactionType | IS],  # FT1.6
        transaction_code: TransactionCode | CE | tuple[TransactionCode | CE],  # FT1.7
        set_id_ft1: SI | tuple[SI] | None = None,  # FT1.1
        transaction_id: ST | tuple[ST] | None = None,  # FT1.2
        transaction_batch_id: ST | tuple[ST] | None = None,  # FT1.3
        transaction_posting_date: TS | tuple[TS] | None = None,  # FT1.5
        transaction_description: ST | tuple[ST] | None = None,  # FT1.8
        transaction_description_alt: ST | tuple[ST] | None = None,  # FT1.9
        transaction_quantity: NM | tuple[NM] | None = None,  # FT1.10
        transaction_amount_extended: CP | tuple[CP] | None = None,  # FT1.11
        transaction_amount_unit: CP | tuple[CP] | None = None,  # FT1.12
        department_code: DepartmentCode
        | CE
        | tuple[DepartmentCode | CE]
        | None = None,  # FT1.13
        insurance_plan_id: InsurancePlanId
        | CE
        | tuple[InsurancePlanId | CE]
        | None = None,  # FT1.14
        insurance_amount: CP | tuple[CP] | None = None,  # FT1.15
        assigned_patient_location: PL | tuple[PL] | None = None,  # FT1.16
        fee_schedule: FeeSchedule
        | IS
        | tuple[FeeSchedule | IS]
        | None = None,  # FT1.17
        patient_type: PatientType
        | IS
        | tuple[PatientType | IS]
        | None = None,  # FT1.18
        diagnosis_code_ft1: DiagnosisCode
        | CE
        | tuple[DiagnosisCode | CE]
        | None = None,  # FT1.19
        performed_by_code: PerformedBy
        | XCN
        | tuple[PerformedBy | XCN]
        | None = None,  # FT1.20
        ordered_by_code: XCN | tuple[XCN] | None = None,  # FT1.21
        unit_cost: CP | tuple[CP] | None = None,  # FT1.22
        filler_order_number: EI | tuple[EI] | None = None,  # FT1.23
        entered_by_code: XCN | tuple[XCN] | None = None,  # FT1.24
        procedure_code: ProcedureCode
        | CE
        | tuple[ProcedureCode | CE]
        | None = None,  # FT1.25
        procedure_code_modifier: ProcedureCodeModifier
        | CE
        | tuple[ProcedureCodeModifier | CE]
        | None = None,  # FT1.26
        advanced_beneficiary_notice_code: AdvancedBeneficiaryNoticeCode
        | CE
        | tuple[AdvancedBeneficiaryNoticeCode | CE]
        | None = None,  # FT1.27
        medically_necessary_duplicate_procedure_reason: MedicallyNecessaryDuplicateProcedureReason
        | CWE
        | tuple[MedicallyNecessaryDuplicateProcedureReason | CWE]
        | None = None,  # FT1.28
        ndc_code: NdcCodes | CNE | tuple[NdcCodes | CNE] | None = None,  # FT1.29
        payment_reference_id: CX | tuple[CX] | None = None,  # FT1.30
        transaction_reference_key: SI | tuple[SI] | None = None,  # FT1.31
    ):
        """
        Financial Transaction - `FT1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1>`_
        The FT1 segment contains the detail data necessary to post charges, payments, adjustments, etc. to patient accounting records.

        :param set_id_ft1: Sequence ID (id: FT1.1 | len: 4 | use: O | rpt: 1)
        :param transaction_id: String Data (id: FT1.2 | len: 12 | use: O | rpt: 1)
        :param transaction_batch_id: String Data (id: FT1.3 | len: 10 | use: O | rpt: 1)
        :param transaction_date: Date/Time Range (id: FT1.4 | len: 53 | use: R | rpt: 1)
        :param transaction_posting_date: Time Stamp (id: FT1.5 | len: 26 | use: O | rpt: 1)
        :param transaction_type: Coded value for user-defined tables (id: FT1.6 | len: 8 | use: R | rpt: 1)
        :param transaction_code: Coded Element (id: FT1.7 | len: 250 | use: R | rpt: 1)
        :param transaction_description: String Data (id: FT1.8 | len: 40 | use: B | rpt: 1)
        :param transaction_description_alt: String Data (id: FT1.9 | len: 40 | use: B | rpt: 1)
        :param transaction_quantity: Numeric (id: FT1.10 | len: 6 | use: O | rpt: 1)
        :param transaction_amount_extended: Composite Price (id: FT1.11 | len: 12 | use: O | rpt: 1)
        :param transaction_amount_unit: Composite Price (id: FT1.12 | len: 12 | use: O | rpt: 1)
        :param department_code: Coded Element (id: FT1.13 | len: 250 | use: O | rpt: 1)
        :param insurance_plan_id: Coded Element (id: FT1.14 | len: 250 | use: O | rpt: 1)
        :param insurance_amount: Composite Price (id: FT1.15 | len: 12 | use: O | rpt: 1)
        :param assigned_patient_location: Person Location (id: FT1.16 | len: 80 | use: O | rpt: 1)
        :param fee_schedule: Coded value for user-defined tables (id: FT1.17 | len: 1 | use: O | rpt: 1)
        :param patient_type: Coded value for user-defined tables (id: FT1.18 | len: 2 | use: O | rpt: 1)
        :param diagnosis_code_ft1: Coded Element (id: FT1.19 | len: 250 | use: O | rpt: *)
        :param performed_by_code: Extended Composite ID Number and Name for Persons (id: FT1.20 | len: 250 | use: O | rpt: *)
        :param ordered_by_code: Extended Composite ID Number and Name for Persons (id: FT1.21 | len: 250 | use: O | rpt: *)
        :param unit_cost: Composite Price (id: FT1.22 | len: 12 | use: O | rpt: 1)
        :param filler_order_number: Entity Identifier (id: FT1.23 | len: 427 | use: O | rpt: 1)
        :param entered_by_code: Extended Composite ID Number and Name for Persons (id: FT1.24 | len: 250 | use: O | rpt: *)
        :param procedure_code: Coded Element (id: FT1.25 | len: 250 | use: O | rpt: 1)
        :param procedure_code_modifier: Coded Element (id: FT1.26 | len: 250 | use: O | rpt: *)
        :param advanced_beneficiary_notice_code: Coded Element (id: FT1.27 | len: 250 | use: O | rpt: 1)
        :param medically_necessary_duplicate_procedure_reason: Coded with Exceptions (id: FT1.28 | len: 250 | use: O | rpt: 1)
        :param ndc_code: Coded with No Exceptions (id: FT1.29 | len: 250 | use: O | rpt: 1)
        :param payment_reference_id: Extended Composite ID with Check Digit (id: FT1.30 | len: 250 | use: O | rpt: 1)
        :param transaction_reference_key: Sequence ID (id: FT1.31 | len: 4 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 31
        self.set_id_ft1 = set_id_ft1
        self.transaction_id = transaction_id
        self.transaction_batch_id = transaction_batch_id
        self.transaction_date = transaction_date
        self.transaction_posting_date = transaction_posting_date
        self.transaction_type = transaction_type
        self.transaction_code = transaction_code
        self.transaction_description = transaction_description
        self.transaction_description_alt = transaction_description_alt
        self.transaction_quantity = transaction_quantity
        self.transaction_amount_extended = transaction_amount_extended
        self.transaction_amount_unit = transaction_amount_unit
        self.department_code = department_code
        self.insurance_plan_id = insurance_plan_id
        self.insurance_amount = insurance_amount
        self.assigned_patient_location = assigned_patient_location
        self.fee_schedule = fee_schedule
        self.patient_type = patient_type
        self.diagnosis_code_ft1 = diagnosis_code_ft1
        self.performed_by_code = performed_by_code
        self.ordered_by_code = ordered_by_code
        self.unit_cost = unit_cost
        self.filler_order_number = filler_order_number
        self.entered_by_code = entered_by_code
        self.procedure_code = procedure_code
        self.procedure_code_modifier = procedure_code_modifier
        self.advanced_beneficiary_notice_code = advanced_beneficiary_notice_code
        self.medically_necessary_duplicate_procedure_reason = (
            medically_necessary_duplicate_procedure_reason
        )
        self.ndc_code = ndc_code
        self.payment_reference_id = payment_reference_id
        self.transaction_reference_key = transaction_reference_key

    @property  # get FT1.1
    def set_id_ft1(self) -> SI | None:
        """
        id: FT1.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.1
        """
        return self._c_data[0][0]

    @set_id_ft1.setter  # set FT1.1
    def set_id_ft1(self, si: SI | None):
        """
        id: FT1.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.1
        """
        self._c_data[0] = (si,)

    @property  # get FT1.2
    def transaction_id(self) -> ST | None:
        """
        id: FT1.2 | len: 12 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.2
        """
        return self._c_data[1][0]

    @transaction_id.setter  # set FT1.2
    def transaction_id(self, st: ST | None):
        """
        id: FT1.2 | len: 12 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.2
        """
        self._c_data[1] = (st,)

    @property  # get FT1.3
    def transaction_batch_id(self) -> ST | None:
        """
        id: FT1.3 | len: 10 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.3
        """
        return self._c_data[2][0]

    @transaction_batch_id.setter  # set FT1.3
    def transaction_batch_id(self, st: ST | None):
        """
        id: FT1.3 | len: 10 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.3
        """
        self._c_data[2] = (st,)

    @property  # get FT1.4
    def transaction_date(self) -> DR:
        """
        id: FT1.4 | len: 53 | use: R | rpt: 1
        ---
        return_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.4
        """
        return self._c_data[3][0]

    @transaction_date.setter  # set FT1.4
    def transaction_date(self, dr: DR):
        """
        id: FT1.4 | len: 53 | use: R | rpt: 1
        ---
        param_type: DR: Date/Time Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.4
        """
        self._c_data[3] = (dr,)

    @property  # get FT1.5
    def transaction_posting_date(self) -> TS | None:
        """
        id: FT1.5 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.5
        """
        return self._c_data[4][0]

    @transaction_posting_date.setter  # set FT1.5
    def transaction_posting_date(self, ts: TS | None):
        """
        id: FT1.5 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.5
        """
        self._c_data[4] = (ts,)

    @property  # get FT1.6
    def transaction_type(self) -> TransactionType:
        """
        id: FT1.6 | len: 8 | use: R | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.6
        """
        return self._c_data[5][0]

    @transaction_type.setter  # set FT1.6
    def transaction_type(self, transaction_type: TransactionType):
        """
        id: FT1.6 | len: 8 | use: R | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.6
        """
        self._c_data[5] = (transaction_type,)

    @property  # get FT1.7
    def transaction_code(self) -> TransactionCode:
        """
        id: FT1.7 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.7
        """
        return self._c_data[6][0]

    @transaction_code.setter  # set FT1.7
    def transaction_code(self, transaction_code: TransactionCode):
        """
        id: FT1.7 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.7
        """
        self._c_data[6] = (transaction_code,)

    @property  # get FT1.8
    def transaction_description(self) -> ST | None:
        """
        id: FT1.8 | len: 40 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.8
        """
        return self._c_data[7][0]

    @transaction_description.setter  # set FT1.8
    def transaction_description(self, st: ST | None):
        """
        id: FT1.8 | len: 40 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.8
        """
        self._c_data[7] = (st,)

    @property  # get FT1.9
    def transaction_description_alt(self) -> ST | None:
        """
        id: FT1.9 | len: 40 | use: B | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.9
        """
        return self._c_data[8][0]

    @transaction_description_alt.setter  # set FT1.9
    def transaction_description_alt(self, st: ST | None):
        """
        id: FT1.9 | len: 40 | use: B | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.9
        """
        self._c_data[8] = (st,)

    @property  # get FT1.10
    def transaction_quantity(self) -> NM | None:
        """
        id: FT1.10 | len: 6 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.10
        """
        return self._c_data[9][0]

    @transaction_quantity.setter  # set FT1.10
    def transaction_quantity(self, nm: NM | None):
        """
        id: FT1.10 | len: 6 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.10
        """
        self._c_data[9] = (nm,)

    @property  # get FT1.11
    def transaction_amount_extended(self) -> CP | None:
        """
        id: FT1.11 | len: 12 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.11
        """
        return self._c_data[10][0]

    @transaction_amount_extended.setter  # set FT1.11
    def transaction_amount_extended(self, cp: CP | None):
        """
        id: FT1.11 | len: 12 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.11
        """
        self._c_data[10] = (cp,)

    @property  # get FT1.12
    def transaction_amount_unit(self) -> CP | None:
        """
        id: FT1.12 | len: 12 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.12
        """
        return self._c_data[11][0]

    @transaction_amount_unit.setter  # set FT1.12
    def transaction_amount_unit(self, cp: CP | None):
        """
        id: FT1.12 | len: 12 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.12
        """
        self._c_data[11] = (cp,)

    @property  # get FT1.13
    def department_code(self) -> DepartmentCode | None:
        """
        id: FT1.13 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.13
        """
        return self._c_data[12][0]

    @department_code.setter  # set FT1.13
    def department_code(self, department_code: DepartmentCode | None):
        """
        id: FT1.13 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.13
        """
        self._c_data[12] = (department_code,)

    @property  # get FT1.14
    def insurance_plan_id(self) -> InsurancePlanId | None:
        """
        id: FT1.14 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.14
        """
        return self._c_data[13][0]

    @insurance_plan_id.setter  # set FT1.14
    def insurance_plan_id(self, insurance_plan_id: InsurancePlanId | None):
        """
        id: FT1.14 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.14
        """
        self._c_data[13] = (insurance_plan_id,)

    @property  # get FT1.15
    def insurance_amount(self) -> CP | None:
        """
        id: FT1.15 | len: 12 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.15
        """
        return self._c_data[14][0]

    @insurance_amount.setter  # set FT1.15
    def insurance_amount(self, cp: CP | None):
        """
        id: FT1.15 | len: 12 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.15
        """
        self._c_data[14] = (cp,)

    @property  # get FT1.16
    def assigned_patient_location(self) -> PL | None:
        """
        id: FT1.16 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.16
        """
        return self._c_data[15][0]

    @assigned_patient_location.setter  # set FT1.16
    def assigned_patient_location(self, pl: PL | None):
        """
        id: FT1.16 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.16
        """
        self._c_data[15] = (pl,)

    @property  # get FT1.17
    def fee_schedule(self) -> FeeSchedule | None:
        """
        id: FT1.17 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.17
        """
        return self._c_data[16][0]

    @fee_schedule.setter  # set FT1.17
    def fee_schedule(self, fee_schedule: FeeSchedule | None):
        """
        id: FT1.17 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.17
        """
        self._c_data[16] = (fee_schedule,)

    @property  # get FT1.18
    def patient_type(self) -> PatientType | None:
        """
        id: FT1.18 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.18
        """
        return self._c_data[17][0]

    @patient_type.setter  # set FT1.18
    def patient_type(self, patient_type: PatientType | None):
        """
        id: FT1.18 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.18
        """
        self._c_data[17] = (patient_type,)

    @property
    def diagnosis_code_ft1(self) -> tuple[DiagnosisCode, ...] | tuple[None]:
        """
        id: FT1.19 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.19
        """
        return self._c_data[18]

    @diagnosis_code_ft1.setter  # set FT1.19
    def diagnosis_code_ft1(
        self, diagnosis_code: DiagnosisCode | tuple[DiagnosisCode] | None
    ):
        """
        id: FT1.19 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.19
        """
        if isinstance(diagnosis_code, tuple):
            self._c_data[18] = diagnosis_code
        else:
            self._c_data[18] = (diagnosis_code,)

    @property
    def performed_by_code(self) -> tuple[PerformedBy, ...] | tuple[None]:
        """
        id: FT1.20 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.20
        """
        return self._c_data[19]

    @performed_by_code.setter  # set FT1.20
    def performed_by_code(self, performed_by: PerformedBy | tuple[PerformedBy] | None):
        """
        id: FT1.20 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.20
        """
        if isinstance(performed_by, tuple):
            self._c_data[19] = performed_by
        else:
            self._c_data[19] = (performed_by,)

    @property
    def ordered_by_code(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: FT1.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.21
        """
        return self._c_data[20]

    @ordered_by_code.setter  # set FT1.21
    def ordered_by_code(self, xcn: XCN | tuple[XCN] | None):
        """
        id: FT1.21 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.21
        """
        if isinstance(xcn, tuple):
            self._c_data[20] = xcn
        else:
            self._c_data[20] = (xcn,)

    @property  # get FT1.22
    def unit_cost(self) -> CP | None:
        """
        id: FT1.22 | len: 12 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.22
        """
        return self._c_data[21][0]

    @unit_cost.setter  # set FT1.22
    def unit_cost(self, cp: CP | None):
        """
        id: FT1.22 | len: 12 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.22
        """
        self._c_data[21] = (cp,)

    @property  # get FT1.23
    def filler_order_number(self) -> EI | None:
        """
        id: FT1.23 | len: 427 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.23
        """
        return self._c_data[22][0]

    @filler_order_number.setter  # set FT1.23
    def filler_order_number(self, ei: EI | None):
        """
        id: FT1.23 | len: 427 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.23
        """
        self._c_data[22] = (ei,)

    @property
    def entered_by_code(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: FT1.24 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.24
        """
        return self._c_data[23]

    @entered_by_code.setter  # set FT1.24
    def entered_by_code(self, xcn: XCN | tuple[XCN] | None):
        """
        id: FT1.24 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.24
        """
        if isinstance(xcn, tuple):
            self._c_data[23] = xcn
        else:
            self._c_data[23] = (xcn,)

    @property  # get FT1.25
    def procedure_code(self) -> ProcedureCode | None:
        """
        id: FT1.25 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.25
        """
        return self._c_data[24][0]

    @procedure_code.setter  # set FT1.25
    def procedure_code(self, procedure_code: ProcedureCode | None):
        """
        id: FT1.25 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.25
        """
        self._c_data[24] = (procedure_code,)

    @property
    def procedure_code_modifier(
        self,
    ) -> tuple[ProcedureCodeModifier, ...] | tuple[None]:
        """
        id: FT1.26 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.26
        """
        return self._c_data[25]

    @procedure_code_modifier.setter  # set FT1.26
    def procedure_code_modifier(
        self,
        procedure_code_modifier: ProcedureCodeModifier
        | tuple[ProcedureCodeModifier]
        | None,
    ):
        """
        id: FT1.26 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.26
        """
        if isinstance(procedure_code_modifier, tuple):
            self._c_data[25] = procedure_code_modifier
        else:
            self._c_data[25] = (procedure_code_modifier,)

    @property  # get FT1.27
    def advanced_beneficiary_notice_code(self) -> AdvancedBeneficiaryNoticeCode | None:
        """
        id: FT1.27 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.27
        """
        return self._c_data[26][0]

    @advanced_beneficiary_notice_code.setter  # set FT1.27
    def advanced_beneficiary_notice_code(
        self, advanced_beneficiary_notice_code: AdvancedBeneficiaryNoticeCode | None
    ):
        """
        id: FT1.27 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.27
        """
        self._c_data[26] = (advanced_beneficiary_notice_code,)

    @property  # get FT1.28
    def medically_necessary_duplicate_procedure_reason(
        self,
    ) -> MedicallyNecessaryDuplicateProcedureReason | None:
        """
        id: FT1.28 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.28
        """
        return self._c_data[27][0]

    @medically_necessary_duplicate_procedure_reason.setter  # set FT1.28
    def medically_necessary_duplicate_procedure_reason(
        self,
        medically_necessary_duplicate_procedure_reason: MedicallyNecessaryDuplicateProcedureReason
        | None,
    ):
        """
        id: FT1.28 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.28
        """
        self._c_data[27] = (medically_necessary_duplicate_procedure_reason,)

    @property  # get FT1.29
    def ndc_code(self) -> NdcCodes | None:
        """
        id: FT1.29 | len: 250 | use: O | rpt: 1
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.29
        """
        return self._c_data[28][0]

    @ndc_code.setter  # set FT1.29
    def ndc_code(self, ndc_codes: NdcCodes | None):
        """
        id: FT1.29 | len: 250 | use: O | rpt: 1
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.29
        """
        self._c_data[28] = (ndc_codes,)

    @property  # get FT1.30
    def payment_reference_id(self) -> CX | None:
        """
        id: FT1.30 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.30
        """
        return self._c_data[29][0]

    @payment_reference_id.setter  # set FT1.30
    def payment_reference_id(self, cx: CX | None):
        """
        id: FT1.30 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.30
        """
        self._c_data[29] = (cx,)

    @property
    def transaction_reference_key(self) -> tuple[SI, ...] | tuple[None]:
        """
        id: FT1.31 | len: 4 | use: O | rpt: *
        ---
        return_type: tuple[SI, ...]: (Sequence ID, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.31
        """
        return self._c_data[30]

    @transaction_reference_key.setter  # set FT1.31
    def transaction_reference_key(self, si: SI | tuple[SI] | None):
        """
        id: FT1.31 | len: 4 | use: O | rpt: *
        ---
        param_type: SI | tuple[SI, ...]: (Sequence ID, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/FT1.31
        """
        if isinstance(si, tuple):
            self._c_data[30] = si
        else:
            self._c_data[30] = (si,)
