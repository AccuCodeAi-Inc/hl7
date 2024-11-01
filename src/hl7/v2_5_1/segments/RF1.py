from __future__ import annotations
from ...base import HL7Segment
from ..data_types.EI import EI
from ..data_types.CE import CE
from ..data_types.TS import TS
from ..tables.ReferralPriority import ReferralPriority
from ..tables.ReferralStatus import ReferralStatus
from ..tables.ReferralType import ReferralType
from ..tables.ReferralDisposition import ReferralDisposition
from ..tables.ReferralReason import ReferralReason
from ..tables.ReferralCategory import ReferralCategory


"""
Referral Information - RF1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RF1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RF1,
    EI, CE, TS
)

rf1 = RF1(  #  - This segment represents information that may be useful when sending referrals from the referring provider to the referred-to provider
    referral_status=None,  # CE(...) 
    referral_priority=None,  # CE(...) 
    referral_type=None,  # CE(...) 
    referral_disposition=None,  # CE(...) 
    referral_category=None,  # CE(...) 
    originating_referral_identifier=ei,  # EI(...)  # Required.
    effective_date=None,  # TS(...) 
    expiration_date=None,  # TS(...) 
    process_date=None,  # TS(...) 
    referral_reason=None,  # CE(...) 
    external_referral_identifier=None,  # EI(...) 
)

-----END SEGMENT::RF1 TEMPLATE-----
"""


class RF1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RF1"""
    _hl7_name = """Referral Information"""
    _hl7_description = """This segment represents information that may be useful when sending referrals from the referring provider to the referred-to provider"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RF1"
    _c_length = (250, 250, 250, 250, 250, 30, 26, 26, 26, 250, 30,)
    _c_rpt = (1, 1, 1, 65535, 1, 1, 1, 1, 1, 65535, 65535,)
    _c_usage = ("O", "O", "O", "O", "O", "R", "O", "O", "O", "O", "O",)
    _c_components = (CE, CE, CE, CE, CE, EI, TS, TS, TS, CE, EI,)
    _c_aliases = ("RF1.1", "RF1.2", "RF1.3", "RF1.4", "RF1.5", "RF1.6", "RF1.7", "RF1.8", "RF1.9", "RF1.10", "RF1.11",)
    _c_names = ("Referral Status", "Referral Priority", "Referral Type", "Referral Disposition", "Referral Category", "Originating Referral Identifier", "Effective Date", "Expiration Date", "Process Date", "Referral Reason", "External Referral Identifier",)
    _c_attrs = ("referral_status", "referral_priority", "referral_type", "referral_disposition", "referral_category", "originating_referral_identifier", "effective_date", "expiration_date", "process_date", "referral_reason", "external_referral_identifier",)
    # fmt: on

    def __init__(
        self,
        originating_referral_identifier: EI | tuple[EI],  # RF1.6
        referral_status: ReferralStatus
        | CE
        | tuple[ReferralStatus | CE]
        | None = None,  # RF1.1
        referral_priority: ReferralPriority
        | CE
        | tuple[ReferralPriority | CE]
        | None = None,  # RF1.2
        referral_type: ReferralType
        | CE
        | tuple[ReferralType | CE]
        | None = None,  # RF1.3
        referral_disposition: ReferralDisposition
        | CE
        | tuple[ReferralDisposition | CE]
        | None = None,  # RF1.4
        referral_category: ReferralCategory
        | CE
        | tuple[ReferralCategory | CE]
        | None = None,  # RF1.5
        effective_date: TS | tuple[TS] | None = None,  # RF1.7
        expiration_date: TS | tuple[TS] | None = None,  # RF1.8
        process_date: TS | tuple[TS] | None = None,  # RF1.9
        referral_reason: ReferralReason
        | CE
        | tuple[ReferralReason | CE]
        | None = None,  # RF1.10
        external_referral_identifier: EI | tuple[EI] | None = None,  # RF1.11
    ):
        """
        Referral Information - `RF1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RF1>`_
        This segment represents information that may be useful when sending referrals from the referring provider to the referred-to provider.

        :param referral_status: Coded Element (id: RF1.1 | len: 250 | use: O | rpt: 1)
        :param referral_priority: Coded Element (id: RF1.2 | len: 250 | use: O | rpt: 1)
        :param referral_type: Coded Element (id: RF1.3 | len: 250 | use: O | rpt: 1)
        :param referral_disposition: Coded Element (id: RF1.4 | len: 250 | use: O | rpt: *)
        :param referral_category: Coded Element (id: RF1.5 | len: 250 | use: O | rpt: 1)
        :param originating_referral_identifier: Entity Identifier (id: RF1.6 | len: 30 | use: R | rpt: 1)
        :param effective_date: Time Stamp (id: RF1.7 | len: 26 | use: O | rpt: 1)
        :param expiration_date: Time Stamp (id: RF1.8 | len: 26 | use: O | rpt: 1)
        :param process_date: Time Stamp (id: RF1.9 | len: 26 | use: O | rpt: 1)
        :param referral_reason: Coded Element (id: RF1.10 | len: 250 | use: O | rpt: *)
        :param external_referral_identifier: Entity Identifier (id: RF1.11 | len: 30 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 11
        self.referral_status = referral_status
        self.referral_priority = referral_priority
        self.referral_type = referral_type
        self.referral_disposition = referral_disposition
        self.referral_category = referral_category
        self.originating_referral_identifier = originating_referral_identifier
        self.effective_date = effective_date
        self.expiration_date = expiration_date
        self.process_date = process_date
        self.referral_reason = referral_reason
        self.external_referral_identifier = external_referral_identifier

    @property  # get RF1.1
    def referral_status(self) -> ReferralStatus | None:
        """
        id: RF1.1 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.1
        """
        return self._c_data[0][0]

    @referral_status.setter  # set RF1.1
    def referral_status(self, referral_status: ReferralStatus | None):
        """
        id: RF1.1 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.1
        """
        self._c_data[0] = (referral_status,)

    @property  # get RF1.2
    def referral_priority(self) -> ReferralPriority | None:
        """
        id: RF1.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.2
        """
        return self._c_data[1][0]

    @referral_priority.setter  # set RF1.2
    def referral_priority(self, referral_priority: ReferralPriority | None):
        """
        id: RF1.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.2
        """
        self._c_data[1] = (referral_priority,)

    @property  # get RF1.3
    def referral_type(self) -> ReferralType | None:
        """
        id: RF1.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.3
        """
        return self._c_data[2][0]

    @referral_type.setter  # set RF1.3
    def referral_type(self, referral_type: ReferralType | None):
        """
        id: RF1.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.3
        """
        self._c_data[2] = (referral_type,)

    @property
    def referral_disposition(self) -> tuple[ReferralDisposition, ...] | tuple[None]:
        """
        id: RF1.4 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.4
        """
        return self._c_data[3]

    @referral_disposition.setter  # set RF1.4
    def referral_disposition(
        self,
        referral_disposition: ReferralDisposition | tuple[ReferralDisposition] | None,
    ):
        """
        id: RF1.4 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.4
        """
        if isinstance(referral_disposition, tuple):
            self._c_data[3] = referral_disposition
        else:
            self._c_data[3] = (referral_disposition,)

    @property  # get RF1.5
    def referral_category(self) -> ReferralCategory | None:
        """
        id: RF1.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.5
        """
        return self._c_data[4][0]

    @referral_category.setter  # set RF1.5
    def referral_category(self, referral_category: ReferralCategory | None):
        """
        id: RF1.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.5
        """
        self._c_data[4] = (referral_category,)

    @property  # get RF1.6
    def originating_referral_identifier(self) -> EI:
        """
        id: RF1.6 | len: 30 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.6
        """
        return self._c_data[5][0]

    @originating_referral_identifier.setter  # set RF1.6
    def originating_referral_identifier(self, ei: EI):
        """
        id: RF1.6 | len: 30 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.6
        """
        self._c_data[5] = (ei,)

    @property  # get RF1.7
    def effective_date(self) -> TS | None:
        """
        id: RF1.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.7
        """
        return self._c_data[6][0]

    @effective_date.setter  # set RF1.7
    def effective_date(self, ts: TS | None):
        """
        id: RF1.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.7
        """
        self._c_data[6] = (ts,)

    @property  # get RF1.8
    def expiration_date(self) -> TS | None:
        """
        id: RF1.8 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.8
        """
        return self._c_data[7][0]

    @expiration_date.setter  # set RF1.8
    def expiration_date(self, ts: TS | None):
        """
        id: RF1.8 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.8
        """
        self._c_data[7] = (ts,)

    @property  # get RF1.9
    def process_date(self) -> TS | None:
        """
        id: RF1.9 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.9
        """
        return self._c_data[8][0]

    @process_date.setter  # set RF1.9
    def process_date(self, ts: TS | None):
        """
        id: RF1.9 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.9
        """
        self._c_data[8] = (ts,)

    @property
    def referral_reason(self) -> tuple[ReferralReason, ...] | tuple[None]:
        """
        id: RF1.10 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.10
        """
        return self._c_data[9]

    @referral_reason.setter  # set RF1.10
    def referral_reason(
        self, referral_reason: ReferralReason | tuple[ReferralReason] | None
    ):
        """
        id: RF1.10 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.10
        """
        if isinstance(referral_reason, tuple):
            self._c_data[9] = referral_reason
        else:
            self._c_data[9] = (referral_reason,)

    @property
    def external_referral_identifier(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: RF1.11 | len: 30 | use: O | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.11
        """
        return self._c_data[10]

    @external_referral_identifier.setter  # set RF1.11
    def external_referral_identifier(self, ei: EI | tuple[EI] | None):
        """
        id: RF1.11 | len: 30 | use: O | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RF1.11
        """
        if isinstance(ei, tuple):
            self._c_data[10] = ei
        else:
            self._c_data[10] = (ei,)
