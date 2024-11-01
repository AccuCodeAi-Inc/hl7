from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.EI import EI


"""
Imaging Procedure Control Segment - IPC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::IPC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    IPC,
    ST, CE, EI
)

ipc = IPC(  #  - The IPC segment contains information about tasks that need to be performed in order to fulfill the request for imaging service
    accession_identifier=ei,  # EI(...)  # Required.
    requested_procedure_id=ei,  # EI(...)  # Required.
    study_instance_uid=ei,  # EI(...)  # Required.
    scheduled_procedure_step_id=ei,  # EI(...)  # Required.
    modality=None,  # CE(...) 
    protocol_code=None,  # CE(...) 
    scheduled_station_name=None,  # EI(...) 
    scheduled_procedure_step_location=None,  # CE(...) 
    scheduled_ae_title=None,  # ST(...) 
)

-----END SEGMENT::IPC TEMPLATE-----
"""


class IPC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """IPC"""
    _hl7_name = """Imaging Procedure Control Segment"""
    _hl7_description = """The IPC segment contains information about tasks that need to be performed in order to fulfill the request for imaging service"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IPC"
    _c_length = (80, 22, 70, 22, 16, 250, 22, 250, 16,)
    _c_rpt = (1, 1, 1, 1, 1, 65535, 1, 65535, 1,)
    _c_usage = ("R", "R", "R", "R", "O", "O", "O", "O", "O",)
    _c_components = (EI, EI, EI, EI, CE, CE, EI, CE, ST,)
    _c_aliases = ("IPC.1", "IPC.2", "IPC.3", "IPC.4", "IPC.5", "IPC.6", "IPC.7", "IPC.8", "IPC.9",)
    _c_names = ("Accession Identifier", "Requested Procedure ID", "Study Instance UID", "Scheduled Procedure Step ID", "Modality", "Protocol Code", "Scheduled Station Name", "Scheduled Procedure Step Location", "Scheduled AE Title",)
    _c_attrs = ("accession_identifier", "requested_procedure_id", "study_instance_uid", "scheduled_procedure_step_id", "modality", "protocol_code", "scheduled_station_name", "scheduled_procedure_step_location", "scheduled_ae_title",)
    # fmt: on

    def __init__(
        self,
        accession_identifier: EI | tuple[EI, ...],  # IPC.1
        requested_procedure_id: EI | tuple[EI, ...],  # IPC.2
        study_instance_uid: EI | tuple[EI, ...],  # IPC.3
        scheduled_procedure_step_id: EI | tuple[EI, ...],  # IPC.4
        modality: CE | tuple[CE, ...] | None = None,  # IPC.5
        protocol_code: CE | tuple[CE, ...] | None = None,  # IPC.6
        scheduled_station_name: EI | tuple[EI, ...] | None = None,  # IPC.7
        scheduled_procedure_step_location: CE | tuple[CE, ...] | None = None,  # IPC.8
        scheduled_ae_title: ST | tuple[ST, ...] | None = None,  # IPC.9
    ):
        """
        Imaging Procedure Control Segment - `IPC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IPC>`_
        The IPC segment contains information about tasks that need to be performed in order to fulfill the request for imaging service. The information includes location, type and instance identification of equipment (acquisition modality) and stages (procedure steps).

        :param accession_identifier: Entity Identifier (id: IPC.1 | len: 80 | use: R | rpt: 1)
        :param requested_procedure_id: Entity Identifier (id: IPC.2 | len: 22 | use: R | rpt: 1)
        :param study_instance_uid: Entity Identifier (id: IPC.3 | len: 70 | use: R | rpt: 1)
        :param scheduled_procedure_step_id: Entity Identifier (id: IPC.4 | len: 22 | use: R | rpt: 1)
        :param modality: Coded Element (id: IPC.5 | len: 16 | use: O | rpt: 1)
        :param protocol_code: Coded Element (id: IPC.6 | len: 250 | use: O | rpt: *)
        :param scheduled_station_name: Entity Identifier (id: IPC.7 | len: 22 | use: O | rpt: 1)
        :param scheduled_procedure_step_location: Coded Element (id: IPC.8 | len: 250 | use: O | rpt: *)
        :param scheduled_ae_title: String Data (id: IPC.9 | len: 16 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.accession_identifier = accession_identifier
        self.requested_procedure_id = requested_procedure_id
        self.study_instance_uid = study_instance_uid
        self.scheduled_procedure_step_id = scheduled_procedure_step_id
        self.modality = modality
        self.protocol_code = protocol_code
        self.scheduled_station_name = scheduled_station_name
        self.scheduled_procedure_step_location = scheduled_procedure_step_location
        self.scheduled_ae_title = scheduled_ae_title

    @property  # get IPC.1
    def accession_identifier(self) -> EI:
        """
        id: IPC.1 | len: 80 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.1
        """
        return self._c_data[0][0]

    @accession_identifier.setter  # set IPC.1
    def accession_identifier(self, ei: EI):
        """
        id: IPC.1 | len: 80 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.1
        """
        self._c_data[0] = (ei,)

    @property  # get IPC.2
    def requested_procedure_id(self) -> EI:
        """
        id: IPC.2 | len: 22 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.2
        """
        return self._c_data[1][0]

    @requested_procedure_id.setter  # set IPC.2
    def requested_procedure_id(self, ei: EI):
        """
        id: IPC.2 | len: 22 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.2
        """
        self._c_data[1] = (ei,)

    @property  # get IPC.3
    def study_instance_uid(self) -> EI:
        """
        id: IPC.3 | len: 70 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.3
        """
        return self._c_data[2][0]

    @study_instance_uid.setter  # set IPC.3
    def study_instance_uid(self, ei: EI):
        """
        id: IPC.3 | len: 70 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.3
        """
        self._c_data[2] = (ei,)

    @property  # get IPC.4
    def scheduled_procedure_step_id(self) -> EI:
        """
        id: IPC.4 | len: 22 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.4
        """
        return self._c_data[3][0]

    @scheduled_procedure_step_id.setter  # set IPC.4
    def scheduled_procedure_step_id(self, ei: EI):
        """
        id: IPC.4 | len: 22 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.4
        """
        self._c_data[3] = (ei,)

    @property  # get IPC.5
    def modality(self) -> CE | None:
        """
        id: IPC.5 | len: 16 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.5
        """
        return self._c_data[4][0]

    @modality.setter  # set IPC.5
    def modality(self, ce: CE | None):
        """
        id: IPC.5 | len: 16 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.5
        """
        self._c_data[4] = (ce,)

    @property
    def protocol_code(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: IPC.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.6
        """
        return self._c_data[5]

    @protocol_code.setter  # set IPC.6
    def protocol_code(self, ce: CE | tuple[CE] | None):
        """
        id: IPC.6 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.6
        """
        if isinstance(ce, tuple):
            self._c_data[5] = ce
        else:
            self._c_data[5] = (ce,)

    @property  # get IPC.7
    def scheduled_station_name(self) -> EI | None:
        """
        id: IPC.7 | len: 22 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.7
        """
        return self._c_data[6][0]

    @scheduled_station_name.setter  # set IPC.7
    def scheduled_station_name(self, ei: EI | None):
        """
        id: IPC.7 | len: 22 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.7
        """
        self._c_data[6] = (ei,)

    @property
    def scheduled_procedure_step_location(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: IPC.8 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.8
        """
        return self._c_data[7]

    @scheduled_procedure_step_location.setter  # set IPC.8
    def scheduled_procedure_step_location(self, ce: CE | tuple[CE] | None):
        """
        id: IPC.8 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.8
        """
        if isinstance(ce, tuple):
            self._c_data[7] = ce
        else:
            self._c_data[7] = (ce,)

    @property  # get IPC.9
    def scheduled_ae_title(self) -> ST | None:
        """
        id: IPC.9 | len: 16 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.9
        """
        return self._c_data[8][0]

    @scheduled_ae_title.setter  # set IPC.9
    def scheduled_ae_title(self, st: ST | None):
        """
        id: IPC.9 | len: 16 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IPC.9
        """
        self._c_data[8] = (st,)
