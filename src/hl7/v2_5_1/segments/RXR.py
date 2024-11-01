from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.CWE import CWE
from ..tables.AdministrationMethod import AdministrationMethod
from ..tables.RouteOfAdministration import RouteOfAdministration
from ..tables.BodySiteModifier import BodySiteModifier
from ..tables.AdministrationDevice import AdministrationDevice
from ..tables.BodySite import BodySite


"""
Pharmacy/Treatment Route - RXR
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RXR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RXR,
    CE, CWE
)

rxr = RXR(  #  - The Pharmacy/Treatment Route segment contains the alternative combination of route, site, administration device, and administration method that are prescribed as they apply to a particular order
    route=ce,  # CE(...)  # Required.
    administration_site=None,  # CWE(...) 
    administration_device=None,  # CE(...) 
    administration_method=None,  # CWE(...) 
    routing_instruction=None,  # CE(...) 
    administration_site_modifier=None,  # CWE(...) 
)

-----END SEGMENT::RXR TEMPLATE-----
"""


class RXR(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RXR"""
    _hl7_name = """Pharmacy/Treatment Route"""
    _hl7_description = """The Pharmacy/Treatment Route segment contains the alternative combination of route, site, administration device, and administration method that are prescribed as they apply to a particular order"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR"
    _c_length = (250, 250, 250, 250, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O",)
    _c_components = (CE, CWE, CE, CWE, CE, CWE,)
    _c_aliases = ("RXR.1", "RXR.2", "RXR.3", "RXR.4", "RXR.5", "RXR.6",)
    _c_names = ("Route", "Administration Site", "Administration Device", "Administration Method", "Routing Instruction", "Administration Site Modifier",)
    _c_attrs = ("route", "administration_site", "administration_device", "administration_method", "routing_instruction", "administration_site_modifier",)
    # fmt: on

    def __init__(
        self,
        route: RouteOfAdministration | CE,  # RXR.1
        administration_site: BodySite | CWE | None = None,  # RXR.2
        administration_device: AdministrationDevice | CE | None = None,  # RXR.3
        administration_method: AdministrationMethod | CWE | None = None,  # RXR.4
        routing_instruction: CE | None = None,  # RXR.5
        administration_site_modifier: BodySiteModifier | CWE | None = None,  # RXR.6
    ):
        """
        Pharmacy/Treatment Route - `RXR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR>`_
        The Pharmacy/Treatment Route segment contains the alternative combination of route, site, administration device, and administration method that are prescribed as they apply to a particular order. The pharmacy, treatment staff and/or nursing staff has a choice between the routes based on either their professional judgment or administration instructions provided by the physician.

        :param route: Coded Element (id: RXR.1 | len: 250 | use: R | rpt: 1)
        :param administration_site: Coded with Exceptions (id: RXR.2 | len: 250 | use: O | rpt: 1)
        :param administration_device: Coded Element (id: RXR.3 | len: 250 | use: O | rpt: 1)
        :param administration_method: Coded with Exceptions (id: RXR.4 | len: 250 | use: O | rpt: 1)
        :param routing_instruction: Coded Element (id: RXR.5 | len: 250 | use: O | rpt: 1)
        :param administration_site_modifier: Coded with Exceptions (id: RXR.6 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.route = route
        self.administration_site = administration_site
        self.administration_device = administration_device
        self.administration_method = administration_method
        self.routing_instruction = routing_instruction
        self.administration_site_modifier = administration_site_modifier

    @property  # get RXR.1
    def route(self) -> RouteOfAdministration:
        """
        id: RXR.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.1
        """
        return self._c_data[0][0]

    @route.setter  # set RXR.1
    def route(self, route_of_administration: RouteOfAdministration):
        """
        id: RXR.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.1
        """
        self._c_data[0] = (route_of_administration,)

    @property  # get RXR.2
    def administration_site(self) -> BodySite | None:
        """
        id: RXR.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.2
        """
        return self._c_data[1][0]

    @administration_site.setter  # set RXR.2
    def administration_site(self, body_site: BodySite | None):
        """
        id: RXR.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.2
        """
        self._c_data[1] = (body_site,)

    @property  # get RXR.3
    def administration_device(self) -> AdministrationDevice | None:
        """
        id: RXR.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.3
        """
        return self._c_data[2][0]

    @administration_device.setter  # set RXR.3
    def administration_device(self, administration_device: AdministrationDevice | None):
        """
        id: RXR.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.3
        """
        self._c_data[2] = (administration_device,)

    @property  # get RXR.4
    def administration_method(self) -> AdministrationMethod | None:
        """
        id: RXR.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.4
        """
        return self._c_data[3][0]

    @administration_method.setter  # set RXR.4
    def administration_method(self, administration_method: AdministrationMethod | None):
        """
        id: RXR.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.4
        """
        self._c_data[3] = (administration_method,)

    @property  # get RXR.5
    def routing_instruction(self) -> CE | None:
        """
        id: RXR.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.5
        """
        return self._c_data[4][0]

    @routing_instruction.setter  # set RXR.5
    def routing_instruction(self, ce: CE | None):
        """
        id: RXR.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.5
        """
        self._c_data[4] = (ce,)

    @property  # get RXR.6
    def administration_site_modifier(self) -> BodySiteModifier | None:
        """
        id: RXR.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.6
        """
        return self._c_data[5][0]

    @administration_site_modifier.setter  # set RXR.6
    def administration_site_modifier(self, body_site_modifier: BodySiteModifier | None):
        """
        id: RXR.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXR.6
        """
        self._c_data[5] = (body_site_modifier,)
