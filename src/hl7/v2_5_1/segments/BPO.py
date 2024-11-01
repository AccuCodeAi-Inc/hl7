from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.PL import PL
from ..data_types.CWE import CWE
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.XAD import XAD
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.IndicationForUse import IndicationForUse
from ..tables.BloodProductProcessingRequirements import (
    BloodProductProcessingRequirements,
)


"""
Blood product order - BPO
HL7 Version: 2.5.1

-----BEGIN SEGMENT::BPO TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    BPO,
    TS, ID, NM, PL, CWE, SI, CE, XAD
)

bpo = BPO(  #  - Blood product order messages require additional information that is not available in other standard HL7 order messages
    set_id_bpo=si,  # SI(...)  # Required.
    bp_universal_service_id=cwe,  # CWE(...)  # Required.
    bp_processing_requirements=None,  # CWE(...) 
    bp_quantity=nm,  # NM(...)  # Required.
    bp_amount=None,  # NM(...) 
    bp_units=None,  # CE(...) 
    bp_intended_use_date_or_time=None,  # TS(...) 
    bp_intended_dispense_from_location=None,  # PL(...) 
    bp_intended_dispense_from_address=None,  # XAD(...) 
    bp_requested_dispense_date_or_time=None,  # TS(...) 
    bp_requested_dispense_to_location=None,  # PL(...) 
    bp_requested_dispense_to_address=None,  # XAD(...) 
    bp_indication_for_use=None,  # CWE(...) 
    bp_informed_consent_indicator=None,  # ID(...) 
)

-----END SEGMENT::BPO TEMPLATE-----
"""


class BPO(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """BPO"""
    _hl7_name = """Blood product order"""
    _hl7_description = """Blood product order messages require additional information that is not available in other standard HL7 order messages"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPO"
    _c_length = (4, 250, 250, 5, 5, 250, 26, 80, 250, 26, 80, 250, 250, 1,)
    _c_rpt = (1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1,)
    _c_usage = ("R", "R", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, CWE, CWE, NM, NM, CE, TS, PL, XAD, TS, PL, XAD, CWE, ID,)
    _c_aliases = ("BPO.1", "BPO.2", "BPO.3", "BPO.4", "BPO.5", "BPO.6", "BPO.7", "BPO.8", "BPO.9", "BPO.10", "BPO.11", "BPO.12", "BPO.13", "BPO.14",)
    _c_names = ("Set ID - BPO", "BP Universal Service ID", "BP  Processing Requirements", "BP Quantity", "BP Amount", "BP Units", "BP Intended Use Date/Time", "BP Intended Dispense From Location", "BP Intended Dispense From Address", "BP Requested Dispense Date/Time", "BP Requested Dispense To Location", "BP Requested Dispense To Address", "BP Indication for Use", "BP Informed Consent Indicator",)
    _c_attrs = ("set_id_bpo", "bp_universal_service_id", "bp_processing_requirements", "bp_quantity", "bp_amount", "bp_units", "bp_intended_use_date_or_time", "bp_intended_dispense_from_location", "bp_intended_dispense_from_address", "bp_requested_dispense_date_or_time", "bp_requested_dispense_to_location", "bp_requested_dispense_to_address", "bp_indication_for_use", "bp_informed_consent_indicator",)
    # fmt: on

    def __init__(
        self,
        set_id_bpo: SI | tuple[SI],  # BPO.1
        bp_universal_service_id: CWE | tuple[CWE],  # BPO.2
        bp_quantity: NM | tuple[NM],  # BPO.4
        bp_processing_requirements: BloodProductProcessingRequirements
        | CWE
        | tuple[BloodProductProcessingRequirements | CWE]
        | None = None,  # BPO.3
        bp_amount: NM | tuple[NM] | None = None,  # BPO.5
        bp_units: CE | tuple[CE] | None = None,  # BPO.6
        bp_intended_use_date_or_time: TS | tuple[TS] | None = None,  # BPO.7
        bp_intended_dispense_from_location: PL | tuple[PL] | None = None,  # BPO.8
        bp_intended_dispense_from_address: XAD | tuple[XAD] | None = None,  # BPO.9
        bp_requested_dispense_date_or_time: TS | tuple[TS] | None = None,  # BPO.10
        bp_requested_dispense_to_location: PL | tuple[PL] | None = None,  # BPO.11
        bp_requested_dispense_to_address: XAD | tuple[XAD] | None = None,  # BPO.12
        bp_indication_for_use: IndicationForUse
        | CWE
        | tuple[IndicationForUse | CWE]
        | None = None,  # BPO.13
        bp_informed_consent_indicator: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID]
        | None = None,  # BPO.14
    ):
        """
        Blood product order - `BPO <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPO>`_
        Blood product order messages require additional information that is not available in other standard HL7 order messages.  Blood product order messages need to contain accompanying details regarding the blood product component, such as special processing requirements (e.g. irradiation and leukoreduction) and the amount of the blood product to be administered.

        :param set_id_bpo: Sequence ID (id: BPO.1 | len: 4 | use: R | rpt: 1)
        :param bp_universal_service_id: Coded with Exceptions (id: BPO.2 | len: 250 | use: R | rpt: 1)
        :param bp_processing_requirements: Coded with Exceptions (id: BPO.3 | len: 250 | use: O | rpt: *)
        :param bp_quantity: Numeric (id: BPO.4 | len: 5 | use: R | rpt: 1)
        :param bp_amount: Numeric (id: BPO.5 | len: 5 | use: O | rpt: 1)
        :param bp_units: Coded Element (id: BPO.6 | len: 250 | use: O | rpt: 1)
        :param bp_intended_use_date_or_time: Time Stamp (id: BPO.7 | len: 26 | use: O | rpt: 1)
        :param bp_intended_dispense_from_location: Person Location (id: BPO.8 | len: 80 | use: O | rpt: 1)
        :param bp_intended_dispense_from_address: Extended Address (id: BPO.9 | len: 250 | use: O | rpt: 1)
        :param bp_requested_dispense_date_or_time: Time Stamp (id: BPO.10 | len: 26 | use: O | rpt: 1)
        :param bp_requested_dispense_to_location: Person Location (id: BPO.11 | len: 80 | use: O | rpt: 1)
        :param bp_requested_dispense_to_address: Extended Address (id: BPO.12 | len: 250 | use: O | rpt: 1)
        :param bp_indication_for_use: Coded with Exceptions (id: BPO.13 | len: 250 | use: O | rpt: *)
        :param bp_informed_consent_indicator: Coded values for HL7 tables (id: BPO.14 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 14
        self.set_id_bpo = set_id_bpo
        self.bp_universal_service_id = bp_universal_service_id
        self.bp_processing_requirements = bp_processing_requirements
        self.bp_quantity = bp_quantity
        self.bp_amount = bp_amount
        self.bp_units = bp_units
        self.bp_intended_use_date_or_time = bp_intended_use_date_or_time
        self.bp_intended_dispense_from_location = bp_intended_dispense_from_location
        self.bp_intended_dispense_from_address = bp_intended_dispense_from_address
        self.bp_requested_dispense_date_or_time = bp_requested_dispense_date_or_time
        self.bp_requested_dispense_to_location = bp_requested_dispense_to_location
        self.bp_requested_dispense_to_address = bp_requested_dispense_to_address
        self.bp_indication_for_use = bp_indication_for_use
        self.bp_informed_consent_indicator = bp_informed_consent_indicator

    @property  # get BPO.1
    def set_id_bpo(self) -> SI:
        """
        id: BPO.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.1
        """
        return self._c_data[0][0]

    @set_id_bpo.setter  # set BPO.1
    def set_id_bpo(self, si: SI):
        """
        id: BPO.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.1
        """
        self._c_data[0] = (si,)

    @property  # get BPO.2
    def bp_universal_service_id(self) -> CWE:
        """
        id: BPO.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.2
        """
        return self._c_data[1][0]

    @bp_universal_service_id.setter  # set BPO.2
    def bp_universal_service_id(self, cwe: CWE):
        """
        id: BPO.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.2
        """
        self._c_data[1] = (cwe,)

    @property
    def bp_processing_requirements(
        self,
    ) -> tuple[BloodProductProcessingRequirements, ...] | tuple[None]:
        """
        id: BPO.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.3
        """
        return self._c_data[2]

    @bp_processing_requirements.setter  # set BPO.3
    def bp_processing_requirements(
        self,
        blood_product_processing_requirements: BloodProductProcessingRequirements
        | tuple[BloodProductProcessingRequirements]
        | None,
    ):
        """
        id: BPO.3 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.3
        """
        if isinstance(blood_product_processing_requirements, tuple):
            self._c_data[2] = blood_product_processing_requirements
        else:
            self._c_data[2] = (blood_product_processing_requirements,)

    @property  # get BPO.4
    def bp_quantity(self) -> NM:
        """
        id: BPO.4 | len: 5 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.4
        """
        return self._c_data[3][0]

    @bp_quantity.setter  # set BPO.4
    def bp_quantity(self, nm: NM):
        """
        id: BPO.4 | len: 5 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.4
        """
        self._c_data[3] = (nm,)

    @property  # get BPO.5
    def bp_amount(self) -> NM | None:
        """
        id: BPO.5 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.5
        """
        return self._c_data[4][0]

    @bp_amount.setter  # set BPO.5
    def bp_amount(self, nm: NM | None):
        """
        id: BPO.5 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.5
        """
        self._c_data[4] = (nm,)

    @property  # get BPO.6
    def bp_units(self) -> CE | None:
        """
        id: BPO.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.6
        """
        return self._c_data[5][0]

    @bp_units.setter  # set BPO.6
    def bp_units(self, ce: CE | None):
        """
        id: BPO.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.6
        """
        self._c_data[5] = (ce,)

    @property  # get BPO.7
    def bp_intended_use_date_or_time(self) -> TS | None:
        """
        id: BPO.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.7
        """
        return self._c_data[6][0]

    @bp_intended_use_date_or_time.setter  # set BPO.7
    def bp_intended_use_date_or_time(self, ts: TS | None):
        """
        id: BPO.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.7
        """
        self._c_data[6] = (ts,)

    @property  # get BPO.8
    def bp_intended_dispense_from_location(self) -> PL | None:
        """
        id: BPO.8 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.8
        """
        return self._c_data[7][0]

    @bp_intended_dispense_from_location.setter  # set BPO.8
    def bp_intended_dispense_from_location(self, pl: PL | None):
        """
        id: BPO.8 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.8
        """
        self._c_data[7] = (pl,)

    @property  # get BPO.9
    def bp_intended_dispense_from_address(self) -> XAD | None:
        """
        id: BPO.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.9
        """
        return self._c_data[8][0]

    @bp_intended_dispense_from_address.setter  # set BPO.9
    def bp_intended_dispense_from_address(self, xad: XAD | None):
        """
        id: BPO.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.9
        """
        self._c_data[8] = (xad,)

    @property  # get BPO.10
    def bp_requested_dispense_date_or_time(self) -> TS | None:
        """
        id: BPO.10 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.10
        """
        return self._c_data[9][0]

    @bp_requested_dispense_date_or_time.setter  # set BPO.10
    def bp_requested_dispense_date_or_time(self, ts: TS | None):
        """
        id: BPO.10 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.10
        """
        self._c_data[9] = (ts,)

    @property  # get BPO.11
    def bp_requested_dispense_to_location(self) -> PL | None:
        """
        id: BPO.11 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.11
        """
        return self._c_data[10][0]

    @bp_requested_dispense_to_location.setter  # set BPO.11
    def bp_requested_dispense_to_location(self, pl: PL | None):
        """
        id: BPO.11 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.11
        """
        self._c_data[10] = (pl,)

    @property  # get BPO.12
    def bp_requested_dispense_to_address(self) -> XAD | None:
        """
        id: BPO.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.12
        """
        return self._c_data[11][0]

    @bp_requested_dispense_to_address.setter  # set BPO.12
    def bp_requested_dispense_to_address(self, xad: XAD | None):
        """
        id: BPO.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.12
        """
        self._c_data[11] = (xad,)

    @property
    def bp_indication_for_use(self) -> tuple[IndicationForUse, ...] | tuple[None]:
        """
        id: BPO.13 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.13
        """
        return self._c_data[12]

    @bp_indication_for_use.setter  # set BPO.13
    def bp_indication_for_use(
        self, indication_for_use: IndicationForUse | tuple[IndicationForUse] | None
    ):
        """
        id: BPO.13 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.13
        """
        if isinstance(indication_for_use, tuple):
            self._c_data[12] = indication_for_use
        else:
            self._c_data[12] = (indication_for_use,)

    @property  # get BPO.14
    def bp_informed_consent_indicator(self) -> YesOrNoIndicator | None:
        """
        id: BPO.14 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.14
        """
        return self._c_data[13][0]

    @bp_informed_consent_indicator.setter  # set BPO.14
    def bp_informed_consent_indicator(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: BPO.14 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPO.14
        """
        self._c_data[13] = (yes_or_no_indicator,)
