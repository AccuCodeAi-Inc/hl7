from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.XAD import XAD
from ..data_types.XON import XON
from ..data_types.ST import ST
from ..data_types.DR import DR


"""
Professional Affiliation - AFF
HL7 Version: 2.5.1

-----BEGIN SEGMENT::AFF TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    AFF,
    SI, XAD, XON, ST, DR
)

aff = AFF(  #  - The AFF segment adds detailed information regarding professional affiliations with which the staff member identified by the STF segment is/was associated
    set_id_aff=si,  # SI(...)  # Required.
    professional_organization=xon,  # XON(...)  # Required.
    professional_organization_address=None,  # XAD(...) 
    professional_organization_affiliation_date_range=None,  # DR(...) 
    professional_affiliation_additional_information=None,  # ST(...) 
)

-----END SEGMENT::AFF TEMPLATE-----
"""


class AFF(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """AFF"""
    _hl7_name = """Professional Affiliation"""
    _hl7_description = """The AFF segment adds detailed information regarding professional affiliations with which the staff member identified by the STF segment is/was associated"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AFF"
    _c_length = (60, 250, 250, 52, 60,)
    _c_rpt = (1, 1, 1, 65535, 1,)
    _c_usage = ("R", "R", "O", "O", "O",)
    _c_components = (SI, XON, XAD, DR, ST,)
    _c_aliases = ("AFF.1", "AFF.2", "AFF.3", "AFF.4", "AFF.5",)
    _c_names = ("Set ID - AFF", "Professional Organization", "Professional Organization Address", "Professional Organization Affiliation Date Range", "Professional Affiliation Additional Information",)
    _c_attrs = ("set_id_aff", "professional_organization", "professional_organization_address", "professional_organization_affiliation_date_range", "professional_affiliation_additional_information",)
    # fmt: on

    def __init__(
        self,
        set_id_aff: SI | tuple[SI, ...],  # AFF.1
        professional_organization: XON | tuple[XON, ...],  # AFF.2
        professional_organization_address: XAD | tuple[XAD, ...] | None = None,  # AFF.3
        professional_organization_affiliation_date_range: DR
        | tuple[DR, ...]
        | None = None,  # AFF.4
        professional_affiliation_additional_information: ST
        | tuple[ST, ...]
        | None = None,  # AFF.5
    ):
        """
        Professional Affiliation - `AFF <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AFF>`_
        The AFF segment adds detailed information regarding professional affiliations with which the staff member identified by the STF segment is/was associated.

        :param set_id_aff: Sequence ID (id: AFF.1 | len: 60 | use: R | rpt: 1)
        :param professional_organization: Extended Composite Name and Identification Number for Organizations (id: AFF.2 | len: 250 | use: R | rpt: 1)
        :param professional_organization_address: Extended Address (id: AFF.3 | len: 250 | use: O | rpt: 1)
        :param professional_organization_affiliation_date_range: Date/Time Range (id: AFF.4 | len: 52 | use: O | rpt: *)
        :param professional_affiliation_additional_information: String Data (id: AFF.5 | len: 60 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.set_id_aff = set_id_aff
        self.professional_organization = professional_organization
        self.professional_organization_address = professional_organization_address
        self.professional_organization_affiliation_date_range = (
            professional_organization_affiliation_date_range
        )
        self.professional_affiliation_additional_information = (
            professional_affiliation_additional_information
        )

    @property  # get AFF.1
    def set_id_aff(self) -> SI:
        """
        id: AFF.1 | len: 60 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AFF.1
        """
        return self._c_data[0][0]

    @set_id_aff.setter  # set AFF.1
    def set_id_aff(self, si: SI):
        """
        id: AFF.1 | len: 60 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AFF.1
        """
        self._c_data[0] = (si,)

    @property  # get AFF.2
    def professional_organization(self) -> XON:
        """
        id: AFF.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AFF.2
        """
        return self._c_data[1][0]

    @professional_organization.setter  # set AFF.2
    def professional_organization(self, xon: XON):
        """
        id: AFF.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AFF.2
        """
        self._c_data[1] = (xon,)

    @property  # get AFF.3
    def professional_organization_address(self) -> XAD | None:
        """
        id: AFF.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AFF.3
        """
        return self._c_data[2][0]

    @professional_organization_address.setter  # set AFF.3
    def professional_organization_address(self, xad: XAD | None):
        """
        id: AFF.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AFF.3
        """
        self._c_data[2] = (xad,)

    @property
    def professional_organization_affiliation_date_range(
        self,
    ) -> tuple[DR, ...] | tuple[None]:
        """
        id: AFF.4 | len: 52 | use: O | rpt: *
        ---
        return_type: tuple[DR, ...]: (Date/Time Range, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AFF.4
        """
        return self._c_data[3]

    @professional_organization_affiliation_date_range.setter  # set AFF.4
    def professional_organization_affiliation_date_range(
        self, dr: DR | tuple[DR] | None
    ):
        """
        id: AFF.4 | len: 52 | use: O | rpt: *
        ---
        param_type: DR | tuple[DR, ...]: (Date/Time Range, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AFF.4
        """
        if isinstance(dr, tuple):
            self._c_data[3] = dr
        else:
            self._c_data[3] = (dr,)

    @property  # get AFF.5
    def professional_affiliation_additional_information(self) -> ST | None:
        """
        id: AFF.5 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AFF.5
        """
        return self._c_data[4][0]

    @professional_affiliation_additional_information.setter  # set AFF.5
    def professional_affiliation_additional_information(self, st: ST | None):
        """
        id: AFF.5 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/AFF.5
        """
        self._c_data[4] = (st,)
