from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TS import TS
from ..tables.IncidentTypeCode import IncidentTypeCode
from ..tables.RiskManagementIncidentCode import RiskManagementIncidentCode


"""
Risk Management Incident - RMI
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RMI TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RMI,
    CE, TS
)

rmi = RMI(  #  - The RMI segment is used to report an occurrence of an incident event pertaining or attaching to a patient encounter
    risk_management_incident_code=None,  # CE(...) 
    date_or_time_incident=None,  # TS(...) 
    incident_type_code=None,  # CE(...) 
)

-----END SEGMENT::RMI TEMPLATE-----
"""


class RMI(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RMI"""
    _hl7_name = """Risk Management Incident"""
    _hl7_description = """The RMI segment is used to report an occurrence of an incident event pertaining or attaching to a patient encounter"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RMI"
    _c_length = (250, 26, 250,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("O", "O", "O",)
    _c_components = (CE, TS, CE,)
    _c_aliases = ("RMI.1", "RMI.2", "RMI.3",)
    _c_names = ("Risk Management Incident Code", "Date/Time Incident", "Incident Type Code",)
    _c_attrs = ("risk_management_incident_code", "date_or_time_incident", "incident_type_code",)
    # fmt: on

    def __init__(
        self,
        risk_management_incident_code: RiskManagementIncidentCode
        | CE
        | None = None,  # RMI.1
        date_or_time_incident: TS | None = None,  # RMI.2
        incident_type_code: IncidentTypeCode | CE | None = None,  # RMI.3
    ):
        """
        Risk Management Incident - `RMI <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RMI>`_
        The RMI segment is used to report an occurrence of an incident event pertaining or attaching to a patient encounter.

        :param risk_management_incident_code: Coded Element (id: RMI.1 | len: 250 | use: O | rpt: 1)
        :param date_or_time_incident: Time Stamp (id: RMI.2 | len: 26 | use: O | rpt: 1)
        :param incident_type_code: Coded Element (id: RMI.3 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.risk_management_incident_code = risk_management_incident_code
        self.date_or_time_incident = date_or_time_incident
        self.incident_type_code = incident_type_code

    @property  # get RMI.1
    def risk_management_incident_code(self) -> RiskManagementIncidentCode | None:
        """
        id: RMI.1 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMI.1
        """
        return self._c_data[0][0]

    @risk_management_incident_code.setter  # set RMI.1
    def risk_management_incident_code(
        self, risk_management_incident_code: RiskManagementIncidentCode | None
    ):
        """
        id: RMI.1 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMI.1
        """
        self._c_data[0] = (risk_management_incident_code,)

    @property  # get RMI.2
    def date_or_time_incident(self) -> TS | None:
        """
        id: RMI.2 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMI.2
        """
        return self._c_data[1][0]

    @date_or_time_incident.setter  # set RMI.2
    def date_or_time_incident(self, ts: TS | None):
        """
        id: RMI.2 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMI.2
        """
        self._c_data[1] = (ts,)

    @property  # get RMI.3
    def incident_type_code(self) -> IncidentTypeCode | None:
        """
        id: RMI.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMI.3
        """
        return self._c_data[2][0]

    @incident_type_code.setter  # set RMI.3
    def incident_type_code(self, incident_type_code: IncidentTypeCode | None):
        """
        id: RMI.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMI.3
        """
        self._c_data[2] = (incident_type_code,)
