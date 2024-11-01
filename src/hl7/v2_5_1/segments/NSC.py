from __future__ import annotations
from ...base import HL7Segment
from ..data_types.IS import IS
from ..data_types.HD import HD
from ..data_types.ST import ST
from ..tables.ApplicationChangeType import ApplicationChangeType


"""
Application Status Change - NSC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::NSC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    NSC,
    IS, HD, ST
)

nsc = NSC(  #  - The NSC segment is used to inform (NMR query response) or announce (NMD unsolicited update) the start-up, shut-down, and/or migration (to a different cpu or file-server/file-system) of a particular application
    application_change_type=_is,  # IS(...)  # Required.
    current_cpu=None,  # ST(...) 
    current_fileserver=None,  # ST(...) 
    current_application=None,  # HD(...) 
    current_facility=None,  # HD(...) 
    new_cpu=None,  # ST(...) 
    new_fileserver=None,  # ST(...) 
    new_application=None,  # HD(...) 
    new_facility=None,  # HD(...) 
)

-----END SEGMENT::NSC TEMPLATE-----
"""


class NSC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """NSC"""
    _hl7_name = """Application Status Change"""
    _hl7_description = """The NSC segment is used to inform (NMR query response) or announce (NMD unsolicited update) the start-up, shut-down, and/or migration (to a different cpu or file-server/file-system) of a particular application"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NSC"
    _c_length = (4, 30, 30, 30, 30, 30, 30, 30, 30,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (IS, ST, ST, HD, HD, ST, ST, HD, HD,)
    _c_aliases = ("NSC.1", "NSC.2", "NSC.3", "NSC.4", "NSC.5", "NSC.6", "NSC.7", "NSC.8", "NSC.9",)
    _c_names = ("Application Change Type", "Current CPU", "Current Fileserver", "Current Application", "Current Facility", "New CPU", "New Fileserver", "New Application", "New Facility",)
    _c_attrs = ("application_change_type", "current_cpu", "current_fileserver", "current_application", "current_facility", "new_cpu", "new_fileserver", "new_application", "new_facility",)
    # fmt: on

    def __init__(
        self,
        application_change_type: ApplicationChangeType
        | IS
        | tuple[ApplicationChangeType | IS],  # NSC.1
        current_cpu: ST | tuple[ST] | None = None,  # NSC.2
        current_fileserver: ST | tuple[ST] | None = None,  # NSC.3
        current_application: HD | tuple[HD] | None = None,  # NSC.4
        current_facility: HD | tuple[HD] | None = None,  # NSC.5
        new_cpu: ST | tuple[ST] | None = None,  # NSC.6
        new_fileserver: ST | tuple[ST] | None = None,  # NSC.7
        new_application: HD | tuple[HD] | None = None,  # NSC.8
        new_facility: HD | tuple[HD] | None = None,  # NSC.9
    ):
        """
                Application Status Change - `NSC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NSC>`_
                The NSC segment is used to inform (NMR query response) or announce (NMD unsolicited update) the start-up, shut-down, and/or migration (to a different cpu or file-server/file-system) of a particular application.

        Usage Notes: Fields 2-9.  These are not applicable (“n/a”) when the type of change being requested or reported is start-up or shut-down.  If the change is of type "M", at least one of fields 2-5 must be different from its corresponding field in range 6-9.

        Fields 4-5, 8-9.  See definitions for the MSH, message header segment, for fields 3-4, for system and facility.  "Application" is available for interfacing with lower level protocols.  "Facility" is entirely site-defined.

        Fields 2-3, 6-7. Entirely site-defined.

                :param application_change_type: Coded value for user-defined tables (id: NSC.1 | len: 4 | use: R | rpt: 1)
                :param current_cpu: String Data (id: NSC.2 | len: 30 | use: O | rpt: 1)
                :param current_fileserver: String Data (id: NSC.3 | len: 30 | use: O | rpt: 1)
                :param current_application: Hierarchic Designator (id: NSC.4 | len: 30 | use: O | rpt: 1)
                :param current_facility: Hierarchic Designator (id: NSC.5 | len: 30 | use: O | rpt: 1)
                :param new_cpu: String Data (id: NSC.6 | len: 30 | use: O | rpt: 1)
                :param new_fileserver: String Data (id: NSC.7 | len: 30 | use: O | rpt: 1)
                :param new_application: Hierarchic Designator (id: NSC.8 | len: 30 | use: O | rpt: 1)
                :param new_facility: Hierarchic Designator (id: NSC.9 | len: 30 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.application_change_type = application_change_type
        self.current_cpu = current_cpu
        self.current_fileserver = current_fileserver
        self.current_application = current_application
        self.current_facility = current_facility
        self.new_cpu = new_cpu
        self.new_fileserver = new_fileserver
        self.new_application = new_application
        self.new_facility = new_facility

    @property  # get NSC.1
    def application_change_type(self) -> ApplicationChangeType:
        """
        id: NSC.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.1
        """
        return self._c_data[0][0]

    @application_change_type.setter  # set NSC.1
    def application_change_type(self, application_change_type: ApplicationChangeType):
        """
        id: NSC.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.1
        """
        self._c_data[0] = (application_change_type,)

    @property  # get NSC.2
    def current_cpu(self) -> ST | None:
        """
        id: NSC.2 | len: 30 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.2
        """
        return self._c_data[1][0]

    @current_cpu.setter  # set NSC.2
    def current_cpu(self, st: ST | None):
        """
        id: NSC.2 | len: 30 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.2
        """
        self._c_data[1] = (st,)

    @property  # get NSC.3
    def current_fileserver(self) -> ST | None:
        """
        id: NSC.3 | len: 30 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.3
        """
        return self._c_data[2][0]

    @current_fileserver.setter  # set NSC.3
    def current_fileserver(self, st: ST | None):
        """
        id: NSC.3 | len: 30 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.3
        """
        self._c_data[2] = (st,)

    @property  # get NSC.4
    def current_application(self) -> HD | None:
        """
        id: NSC.4 | len: 30 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.4
        """
        return self._c_data[3][0]

    @current_application.setter  # set NSC.4
    def current_application(self, hd: HD | None):
        """
        id: NSC.4 | len: 30 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.4
        """
        self._c_data[3] = (hd,)

    @property  # get NSC.5
    def current_facility(self) -> HD | None:
        """
        id: NSC.5 | len: 30 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.5
        """
        return self._c_data[4][0]

    @current_facility.setter  # set NSC.5
    def current_facility(self, hd: HD | None):
        """
        id: NSC.5 | len: 30 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.5
        """
        self._c_data[4] = (hd,)

    @property  # get NSC.6
    def new_cpu(self) -> ST | None:
        """
        id: NSC.6 | len: 30 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.6
        """
        return self._c_data[5][0]

    @new_cpu.setter  # set NSC.6
    def new_cpu(self, st: ST | None):
        """
        id: NSC.6 | len: 30 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.6
        """
        self._c_data[5] = (st,)

    @property  # get NSC.7
    def new_fileserver(self) -> ST | None:
        """
        id: NSC.7 | len: 30 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.7
        """
        return self._c_data[6][0]

    @new_fileserver.setter  # set NSC.7
    def new_fileserver(self, st: ST | None):
        """
        id: NSC.7 | len: 30 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.7
        """
        self._c_data[6] = (st,)

    @property  # get NSC.8
    def new_application(self) -> HD | None:
        """
        id: NSC.8 | len: 30 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.8
        """
        return self._c_data[7][0]

    @new_application.setter  # set NSC.8
    def new_application(self, hd: HD | None):
        """
        id: NSC.8 | len: 30 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.8
        """
        self._c_data[7] = (hd,)

    @property  # get NSC.9
    def new_facility(self) -> HD | None:
        """
        id: NSC.9 | len: 30 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.9
        """
        return self._c_data[8][0]

    @new_facility.setter  # set NSC.9
    def new_facility(self, hd: HD | None):
        """
        id: NSC.9 | len: 30 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NSC.9
        """
        self._c_data[8] = (hd,)
