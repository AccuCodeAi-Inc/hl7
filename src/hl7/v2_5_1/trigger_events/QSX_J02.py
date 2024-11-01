from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.QID import QID
from ..segments.SFT import SFT
from ..segments.MSH import MSH


"""
Cancel Subscription - QSX_J02
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::QSX_J02 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import QSX_J02
from utils.hl7.v2_5_1.segments import (
    QID, SFT, MSH
)

qsx_j02 = QSX_J02(  #  - 
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    query_identification=qid,  # QID(...)  # Required.
)

-----END TRIGGER_EVENT::QSX_J02 TEMPLATE-----
"""


class QSX_J02(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """QSX_J02"""
    _hl7_name = """Cancel Subscription"""
    _hl7_description = """"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/QSX_J02"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 1)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("1", "2", "3")
    _c_components = (MSH, SFT, QID)
    _c_name = ("MSH", "SFT", "QID")
    _c_is_group = (False, False, False)
    _c_attrs = ("message_header", "software_segment", "query_identification",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        query_identification: QID,  #  Required. QID.3
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `QSX_J02 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/QSX_J02>`_


        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param query_identification: Query Identification (id: QID | seq: 3 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.message_header = message_header
        self.software_segment = software_segment
        self.query_identification = query_identification

    @property  # get MSH.1
    def message_header(self) -> MSH:
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        return_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        return self._c_data[0][0]

    @message_header.setter  # set MSH.1
    def message_header(self, msh: MSH):
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        param_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        self._c_data[0] = (msh,)

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[1]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        param_type: SFT.2 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[1] = sft
        else:
            self._c_data[1] = (sft,)

    @property  # get QID.3
    def query_identification(self) -> QID:
        """
        id: QID | use: R | rpt: 1 | seq: 3
        ---
        return_type: QID.3: Query Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QID
        """
        return self._c_data[2][0]

    @query_identification.setter  # set QID.3
    def query_identification(self, qid: QID):
        """
        id: QID | use: R | rpt: 1 | seq: 3
        ---
        param_type: QID.3: Query Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QID
        """
        self._c_data[2] = (qid,)
