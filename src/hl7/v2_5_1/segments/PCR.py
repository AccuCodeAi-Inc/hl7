from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.IS import IS
from ..data_types.CQ import CQ
from ..data_types.ID import ID
from ..data_types.ST import ST
from ..data_types.TS import TS
from ..tables.CausalityObservations import CausalityObservations
from ..tables.ActionTakenInResponseToTheEvent import ActionTakenInResponseToTheEvent
from ..tables.GenericProduct import GenericProduct
from ..tables.PrimaryObserverSQualification import PrimaryObserverSQualification
from ..tables.ProductProblem import ProductProblem
from ..tables.SingleUseDevice import SingleUseDevice
from ..tables.StatusOfEvaluation import StatusOfEvaluation
from ..tables.ProductSource import ProductSource
from ..tables.IndirectExposureMechanism import IndirectExposureMechanism
from ..tables.RelatednessAssessment import RelatednessAssessment
from ..tables.ProductAvailableForInspection import ProductAvailableForInspection


"""
Possible Causal Relationship - PCR
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PCR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PCR,
    CE, IS, CQ, ID, ST, TS
)

pcr = PCR(  #  - The PCR segment is used to communicate a potential or suspected relationship between a product (drug or device) or test and an event with detrimental effect on a patient
    implicated_product=ce,  # CE(...)  # Required.
    generic_product=None,  # IS(...) 
    product_class=None,  # CE(...) 
    total_duration_of_therapy=None,  # CQ(...) 
    product_manufacture_date=None,  # TS(...) 
    product_expiration_date=None,  # TS(...) 
    product_implantation_date=None,  # TS(...) 
    product_explantation_date=None,  # TS(...) 
    single_use_device=None,  # IS(...) 
    indication_for_product_use=None,  # CE(...) 
    product_problem=None,  # IS(...) 
    product_serial_or_lot_number=None,  # ST(...) 
    product_available_for_inspection=None,  # IS(...) 
    product_evaluation_performed=None,  # CE(...) 
    product_evaluation_status=None,  # CE(...) 
    product_evaluation_results=None,  # CE(...) 
    evaluated_product_source=None,  # ID(...) 
    date_product_returned_to_manufacturer=None,  # TS(...) 
    device_operator_qualifications=None,  # ID(...) 
    relatedness_assessment=None,  # ID(...) 
    action_taken_in_response_to_the_event=None,  # ID(...) 
    event_causality_observations=None,  # ID(...) 
    indirect_exposure_mechanism=None,  # ID(...) 
)

-----END SEGMENT::PCR TEMPLATE-----
"""


class PCR(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PCR"""
    _hl7_name = """Possible Causal Relationship"""
    _hl7_description = """The PCR segment is used to communicate a potential or suspected relationship between a product (drug or device) or test and an event with detrimental effect on a patient"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PCR"
    _c_length = (250, 1, 250, 8, 26, 26, 26, 26, 8, 250, 8, 30, 1, 250, 250, 250, 8, 26, 1, 1, 2, 2, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 3,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, IS, CE, CQ, TS, TS, TS, TS, IS, CE, IS, ST, IS, CE, CE, CE, ID, TS, ID, ID, ID, ID, ID,)
    _c_aliases = ("PCR.1", "PCR.2", "PCR.3", "PCR.4", "PCR.5", "PCR.6", "PCR.7", "PCR.8", "PCR.9", "PCR.10", "PCR.11", "PCR.12", "PCR.13", "PCR.14", "PCR.15", "PCR.16", "PCR.17", "PCR.18", "PCR.19", "PCR.20", "PCR.21", "PCR.22", "PCR.23",)
    _c_names = ("Implicated Product", "Generic Product", "Product Class", "Total Duration Of Therapy", "Product Manufacture Date", "Product Expiration Date", "Product Implantation Date", "Product Explantation Date", "Single Use Device", "Indication For Product Use", "Product Problem", "Product Serial/Lot Number", "Product Available For Inspection", "Product Evaluation Performed", "Product Evaluation Status", "Product Evaluation Results", "Evaluated Product Source", "Date Product Returned To Manufacturer", "Device Operator Qualifications", "Relatedness Assessment", "Action Taken In Response To The Event", "Event Causality Observations", "Indirect Exposure Mechanism",)
    _c_attrs = ("implicated_product", "generic_product", "product_class", "total_duration_of_therapy", "product_manufacture_date", "product_expiration_date", "product_implantation_date", "product_explantation_date", "single_use_device", "indication_for_product_use", "product_problem", "product_serial_or_lot_number", "product_available_for_inspection", "product_evaluation_performed", "product_evaluation_status", "product_evaluation_results", "evaluated_product_source", "date_product_returned_to_manufacturer", "device_operator_qualifications", "relatedness_assessment", "action_taken_in_response_to_the_event", "event_causality_observations", "indirect_exposure_mechanism",)
    # fmt: on

    def __init__(
        self,
        implicated_product: CE,  # PCR.1
        generic_product: GenericProduct | IS | None = None,  # PCR.2
        product_class: CE | None = None,  # PCR.3
        total_duration_of_therapy: CQ | None = None,  # PCR.4
        product_manufacture_date: TS | None = None,  # PCR.5
        product_expiration_date: TS | None = None,  # PCR.6
        product_implantation_date: TS | None = None,  # PCR.7
        product_explantation_date: TS | None = None,  # PCR.8
        single_use_device: SingleUseDevice | IS | None = None,  # PCR.9
        indication_for_product_use: CE | None = None,  # PCR.10
        product_problem: ProductProblem | IS | None = None,  # PCR.11
        product_serial_or_lot_number: ST | None = None,  # PCR.12
        product_available_for_inspection: ProductAvailableForInspection
        | IS
        | None = None,  # PCR.13
        product_evaluation_performed: CE | None = None,  # PCR.14
        product_evaluation_status: StatusOfEvaluation | CE | None = None,  # PCR.15
        product_evaluation_results: CE | None = None,  # PCR.16
        evaluated_product_source: ProductSource | ID | None = None,  # PCR.17
        date_product_returned_to_manufacturer: TS | None = None,  # PCR.18
        device_operator_qualifications: PrimaryObserverSQualification
        | ID
        | None = None,  # PCR.19
        relatedness_assessment: RelatednessAssessment | ID | None = None,  # PCR.20
        action_taken_in_response_to_the_event: ActionTakenInResponseToTheEvent
        | ID
        | None = None,  # PCR.21
        event_causality_observations: CausalityObservations
        | ID
        | None = None,  # PCR.22
        indirect_exposure_mechanism: IndirectExposureMechanism
        | ID
        | None = None,  # PCR.23
    ):
        """
        Possible Causal Relationship - `PCR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PCR>`_
        The PCR segment is used to communicate a potential or suspected relationship between a product (drug or device) or test and an event with detrimental effect on a patient. This segment identifies a potential causal relationship between the product identified in this segment and the event identified in the PEO segment.

        :param implicated_product: Coded Element (id: PCR.1 | len: 250 | use: R | rpt: 1)
        :param generic_product: Coded value for user-defined tables (id: PCR.2 | len: 1 | use: O | rpt: 1)
        :param product_class: Coded Element (id: PCR.3 | len: 250 | use: O | rpt: 1)
        :param total_duration_of_therapy: Composite Quantity with Units (id: PCR.4 | len: 8 | use: O | rpt: 1)
        :param product_manufacture_date: Time Stamp (id: PCR.5 | len: 26 | use: O | rpt: 1)
        :param product_expiration_date: Time Stamp (id: PCR.6 | len: 26 | use: O | rpt: 1)
        :param product_implantation_date: Time Stamp (id: PCR.7 | len: 26 | use: O | rpt: 1)
        :param product_explantation_date: Time Stamp (id: PCR.8 | len: 26 | use: O | rpt: 1)
        :param single_use_device: Coded value for user-defined tables (id: PCR.9 | len: 8 | use: O | rpt: 1)
        :param indication_for_product_use: Coded Element (id: PCR.10 | len: 250 | use: O | rpt: 1)
        :param product_problem: Coded value for user-defined tables (id: PCR.11 | len: 8 | use: O | rpt: 1)
        :param product_serial_or_lot_number: String Data (id: PCR.12 | len: 30 | use: O | rpt: 3)
        :param product_available_for_inspection: Coded value for user-defined tables (id: PCR.13 | len: 1 | use: O | rpt: 1)
        :param product_evaluation_performed: Coded Element (id: PCR.14 | len: 250 | use: O | rpt: 1)
        :param product_evaluation_status: Coded Element (id: PCR.15 | len: 250 | use: O | rpt: 1)
        :param product_evaluation_results: Coded Element (id: PCR.16 | len: 250 | use: O | rpt: 1)
        :param evaluated_product_source: Coded values for HL7 tables (id: PCR.17 | len: 8 | use: O | rpt: 1)
        :param date_product_returned_to_manufacturer: Time Stamp (id: PCR.18 | len: 26 | use: O | rpt: 1)
        :param device_operator_qualifications: Coded values for HL7 tables (id: PCR.19 | len: 1 | use: O | rpt: 1)
        :param relatedness_assessment: Coded values for HL7 tables (id: PCR.20 | len: 1 | use: O | rpt: 1)
        :param action_taken_in_response_to_the_event: Coded values for HL7 tables (id: PCR.21 | len: 2 | use: O | rpt: 6)
        :param event_causality_observations: Coded values for HL7 tables (id: PCR.22 | len: 2 | use: O | rpt: 6)
        :param indirect_exposure_mechanism: Coded values for HL7 tables (id: PCR.23 | len: 1 | use: O | rpt: 3)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 23
        self.implicated_product = implicated_product
        self.generic_product = generic_product
        self.product_class = product_class
        self.total_duration_of_therapy = total_duration_of_therapy
        self.product_manufacture_date = product_manufacture_date
        self.product_expiration_date = product_expiration_date
        self.product_implantation_date = product_implantation_date
        self.product_explantation_date = product_explantation_date
        self.single_use_device = single_use_device
        self.indication_for_product_use = indication_for_product_use
        self.product_problem = product_problem
        self.product_serial_or_lot_number = product_serial_or_lot_number
        self.product_available_for_inspection = product_available_for_inspection
        self.product_evaluation_performed = product_evaluation_performed
        self.product_evaluation_status = product_evaluation_status
        self.product_evaluation_results = product_evaluation_results
        self.evaluated_product_source = evaluated_product_source
        self.date_product_returned_to_manufacturer = (
            date_product_returned_to_manufacturer
        )
        self.device_operator_qualifications = device_operator_qualifications
        self.relatedness_assessment = relatedness_assessment
        self.action_taken_in_response_to_the_event = (
            action_taken_in_response_to_the_event
        )
        self.event_causality_observations = event_causality_observations
        self.indirect_exposure_mechanism = indirect_exposure_mechanism

    @property  # get PCR.1
    def implicated_product(self) -> CE:
        """
        id: PCR.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.1
        """
        return self._c_data[0][0]

    @implicated_product.setter  # set PCR.1
    def implicated_product(self, ce: CE):
        """
        id: PCR.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.1
        """
        self._c_data[0] = (ce,)

    @property  # get PCR.2
    def generic_product(self) -> GenericProduct | None:
        """
        id: PCR.2 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.2
        """
        return self._c_data[1][0]

    @generic_product.setter  # set PCR.2
    def generic_product(self, generic_product: GenericProduct | None):
        """
        id: PCR.2 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.2
        """
        self._c_data[1] = (generic_product,)

    @property  # get PCR.3
    def product_class(self) -> CE | None:
        """
        id: PCR.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.3
        """
        return self._c_data[2][0]

    @product_class.setter  # set PCR.3
    def product_class(self, ce: CE | None):
        """
        id: PCR.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.3
        """
        self._c_data[2] = (ce,)

    @property  # get PCR.4
    def total_duration_of_therapy(self) -> CQ | None:
        """
        id: PCR.4 | len: 8 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.4
        """
        return self._c_data[3][0]

    @total_duration_of_therapy.setter  # set PCR.4
    def total_duration_of_therapy(self, cq: CQ | None):
        """
        id: PCR.4 | len: 8 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.4
        """
        self._c_data[3] = (cq,)

    @property  # get PCR.5
    def product_manufacture_date(self) -> TS | None:
        """
        id: PCR.5 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.5
        """
        return self._c_data[4][0]

    @product_manufacture_date.setter  # set PCR.5
    def product_manufacture_date(self, ts: TS | None):
        """
        id: PCR.5 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.5
        """
        self._c_data[4] = (ts,)

    @property  # get PCR.6
    def product_expiration_date(self) -> TS | None:
        """
        id: PCR.6 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.6
        """
        return self._c_data[5][0]

    @product_expiration_date.setter  # set PCR.6
    def product_expiration_date(self, ts: TS | None):
        """
        id: PCR.6 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.6
        """
        self._c_data[5] = (ts,)

    @property  # get PCR.7
    def product_implantation_date(self) -> TS | None:
        """
        id: PCR.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.7
        """
        return self._c_data[6][0]

    @product_implantation_date.setter  # set PCR.7
    def product_implantation_date(self, ts: TS | None):
        """
        id: PCR.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.7
        """
        self._c_data[6] = (ts,)

    @property  # get PCR.8
    def product_explantation_date(self) -> TS | None:
        """
        id: PCR.8 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.8
        """
        return self._c_data[7][0]

    @product_explantation_date.setter  # set PCR.8
    def product_explantation_date(self, ts: TS | None):
        """
        id: PCR.8 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.8
        """
        self._c_data[7] = (ts,)

    @property  # get PCR.9
    def single_use_device(self) -> SingleUseDevice | None:
        """
        id: PCR.9 | len: 8 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.9
        """
        return self._c_data[8][0]

    @single_use_device.setter  # set PCR.9
    def single_use_device(self, single_use_device: SingleUseDevice | None):
        """
        id: PCR.9 | len: 8 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.9
        """
        self._c_data[8] = (single_use_device,)

    @property  # get PCR.10
    def indication_for_product_use(self) -> CE | None:
        """
        id: PCR.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.10
        """
        return self._c_data[9][0]

    @indication_for_product_use.setter  # set PCR.10
    def indication_for_product_use(self, ce: CE | None):
        """
        id: PCR.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.10
        """
        self._c_data[9] = (ce,)

    @property  # get PCR.11
    def product_problem(self) -> ProductProblem | None:
        """
        id: PCR.11 | len: 8 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.11
        """
        return self._c_data[10][0]

    @product_problem.setter  # set PCR.11
    def product_problem(self, product_problem: ProductProblem | None):
        """
        id: PCR.11 | len: 8 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.11
        """
        self._c_data[10] = (product_problem,)

    @property
    def product_serial_or_lot_number(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: PCR.12 | len: 30 | use: O | rpt: 3
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.12
        """
        return self._c_data[11]

    @product_serial_or_lot_number.setter  # set PCR.12
    def product_serial_or_lot_number(self, st: ST | tuple[ST] | None):
        """
        id: PCR.12 | len: 30 | use: O | rpt: 3
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.12
        """
        if isinstance(st, tuple):
            self._c_data[11] = st
        else:
            self._c_data[11] = (st,)

    @property  # get PCR.13
    def product_available_for_inspection(self) -> ProductAvailableForInspection | None:
        """
        id: PCR.13 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.13
        """
        return self._c_data[12][0]

    @product_available_for_inspection.setter  # set PCR.13
    def product_available_for_inspection(
        self, product_available_for_inspection: ProductAvailableForInspection | None
    ):
        """
        id: PCR.13 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.13
        """
        self._c_data[12] = (product_available_for_inspection,)

    @property  # get PCR.14
    def product_evaluation_performed(self) -> CE | None:
        """
        id: PCR.14 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.14
        """
        return self._c_data[13][0]

    @product_evaluation_performed.setter  # set PCR.14
    def product_evaluation_performed(self, ce: CE | None):
        """
        id: PCR.14 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.14
        """
        self._c_data[13] = (ce,)

    @property  # get PCR.15
    def product_evaluation_status(self) -> StatusOfEvaluation | None:
        """
        id: PCR.15 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.15
        """
        return self._c_data[14][0]

    @product_evaluation_status.setter  # set PCR.15
    def product_evaluation_status(
        self, status_of_evaluation: StatusOfEvaluation | None
    ):
        """
        id: PCR.15 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.15
        """
        self._c_data[14] = (status_of_evaluation,)

    @property  # get PCR.16
    def product_evaluation_results(self) -> CE | None:
        """
        id: PCR.16 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.16
        """
        return self._c_data[15][0]

    @product_evaluation_results.setter  # set PCR.16
    def product_evaluation_results(self, ce: CE | None):
        """
        id: PCR.16 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.16
        """
        self._c_data[15] = (ce,)

    @property  # get PCR.17
    def evaluated_product_source(self) -> ProductSource | None:
        """
        id: PCR.17 | len: 8 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.17
        """
        return self._c_data[16][0]

    @evaluated_product_source.setter  # set PCR.17
    def evaluated_product_source(self, product_source: ProductSource | None):
        """
        id: PCR.17 | len: 8 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.17
        """
        self._c_data[16] = (product_source,)

    @property  # get PCR.18
    def date_product_returned_to_manufacturer(self) -> TS | None:
        """
        id: PCR.18 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.18
        """
        return self._c_data[17][0]

    @date_product_returned_to_manufacturer.setter  # set PCR.18
    def date_product_returned_to_manufacturer(self, ts: TS | None):
        """
        id: PCR.18 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.18
        """
        self._c_data[17] = (ts,)

    @property  # get PCR.19
    def device_operator_qualifications(self) -> PrimaryObserverSQualification | None:
        """
        id: PCR.19 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.19
        """
        return self._c_data[18][0]

    @device_operator_qualifications.setter  # set PCR.19
    def device_operator_qualifications(
        self, primary_observers_qualification: PrimaryObserverSQualification | None
    ):
        """
        id: PCR.19 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.19
        """
        self._c_data[18] = (primary_observers_qualification,)

    @property  # get PCR.20
    def relatedness_assessment(self) -> RelatednessAssessment | None:
        """
        id: PCR.20 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.20
        """
        return self._c_data[19][0]

    @relatedness_assessment.setter  # set PCR.20
    def relatedness_assessment(
        self, relatedness_assessment: RelatednessAssessment | None
    ):
        """
        id: PCR.20 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.20
        """
        self._c_data[19] = (relatedness_assessment,)

    @property
    def action_taken_in_response_to_the_event(
        self,
    ) -> tuple[ActionTakenInResponseToTheEvent, ...] | tuple[None]:
        """
        id: PCR.21 | len: 2 | use: O | rpt: 6
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.21
        """
        return self._c_data[20]

    @action_taken_in_response_to_the_event.setter  # set PCR.21
    def action_taken_in_response_to_the_event(
        self,
        action_taken_in_response_to_the_event: ActionTakenInResponseToTheEvent
        | tuple[ActionTakenInResponseToTheEvent]
        | None,
    ):
        """
        id: PCR.21 | len: 2 | use: O | rpt: 6
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.21
        """
        if isinstance(action_taken_in_response_to_the_event, tuple):
            self._c_data[20] = action_taken_in_response_to_the_event
        else:
            self._c_data[20] = (action_taken_in_response_to_the_event,)

    @property
    def event_causality_observations(
        self,
    ) -> tuple[CausalityObservations, ...] | tuple[None]:
        """
        id: PCR.22 | len: 2 | use: O | rpt: 6
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.22
        """
        return self._c_data[21]

    @event_causality_observations.setter  # set PCR.22
    def event_causality_observations(
        self,
        causality_observations: CausalityObservations
        | tuple[CausalityObservations]
        | None,
    ):
        """
        id: PCR.22 | len: 2 | use: O | rpt: 6
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.22
        """
        if isinstance(causality_observations, tuple):
            self._c_data[21] = causality_observations
        else:
            self._c_data[21] = (causality_observations,)

    @property
    def indirect_exposure_mechanism(
        self,
    ) -> tuple[IndirectExposureMechanism, ...] | tuple[None]:
        """
        id: PCR.23 | len: 1 | use: O | rpt: 3
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.23
        """
        return self._c_data[22]

    @indirect_exposure_mechanism.setter  # set PCR.23
    def indirect_exposure_mechanism(
        self,
        indirect_exposure_mechanism: IndirectExposureMechanism
        | tuple[IndirectExposureMechanism]
        | None,
    ):
        """
        id: PCR.23 | len: 1 | use: O | rpt: 3
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PCR.23
        """
        if isinstance(indirect_exposure_mechanism, tuple):
            self._c_data[22] = indirect_exposure_mechanism
        else:
            self._c_data[22] = (indirect_exposure_mechanism,)
