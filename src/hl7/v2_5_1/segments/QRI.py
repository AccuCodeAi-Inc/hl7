from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..data_types.IS import IS
from ..tables.MatchAlgorithms import MatchAlgorithms
from ..tables.MatchReason import MatchReason


"""
Query Response Instance - QRI
HL7 Version: 2.5.1

-----BEGIN SEGMENT::QRI TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    QRI,
    CE, NM, IS
)

qri = QRI(  #  - The QRI segment is used to indicate the weight match for a returned record (where the responding system employs a numeric algorithm) and/or the match reason code (where the responding system uses rules or other match options)
    candidate_confidence=None,  # NM(...) 
    match_reason_code=None,  # IS(...) 
    algorithm_descriptor=None,  # CE(...) 
)

-----END SEGMENT::QRI TEMPLATE-----
"""


class QRI(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """QRI"""
    _hl7_name = """Query Response Instance"""
    _hl7_description = """The QRI segment is used to indicate the weight match for a returned record (where the responding system employs a numeric algorithm) and/or the match reason code (where the responding system uses rules or other match options)"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRI"
    _c_length = (10, 2, 250,)
    _c_rpt = (1, 65535, 1,)
    _c_usage = ("O", "O", "O",)
    _c_components = (NM, IS, CE,)
    _c_aliases = ("QRI.1", "QRI.2", "QRI.3",)
    _c_names = ("Candidate Confidence", "Match Reason Code", "Algorithm Descriptor",)
    _c_attrs = ("candidate_confidence", "match_reason_code", "algorithm_descriptor",)
    # fmt: on

    def __init__(
        self,
        candidate_confidence: NM | None = None,  # QRI.1
        match_reason_code: MatchReason | IS | None = None,  # QRI.2
        algorithm_descriptor: MatchAlgorithms | CE | None = None,  # QRI.3
    ):
        """
        Query Response Instance - `QRI <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRI>`_
        The QRI segment is used to indicate the weight match for a returned record (where the responding system employs a numeric algorithm) and/or the match reason code (where the responding system uses rules or other match options).

        :param candidate_confidence: Numeric (id: QRI.1 | len: 10 | use: O | rpt: 1)
        :param match_reason_code: Coded value for user-defined tables (id: QRI.2 | len: 2 | use: O | rpt: *)
        :param algorithm_descriptor: Coded Element (id: QRI.3 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.candidate_confidence = candidate_confidence
        self.match_reason_code = match_reason_code
        self.algorithm_descriptor = algorithm_descriptor

    @property  # get QRI.1
    def candidate_confidence(self) -> NM | None:
        """
        id: QRI.1 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRI.1
        """
        return self._c_data[0][0]

    @candidate_confidence.setter  # set QRI.1
    def candidate_confidence(self, nm: NM | None):
        """
        id: QRI.1 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRI.1
        """
        self._c_data[0] = (nm,)

    @property
    def match_reason_code(self) -> tuple[MatchReason, ...] | tuple[None]:
        """
        id: QRI.2 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRI.2
        """
        return self._c_data[1]

    @match_reason_code.setter  # set QRI.2
    def match_reason_code(self, match_reason: MatchReason | tuple[MatchReason] | None):
        """
        id: QRI.2 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRI.2
        """
        if isinstance(match_reason, tuple):
            self._c_data[1] = match_reason
        else:
            self._c_data[1] = (match_reason,)

    @property  # get QRI.3
    def algorithm_descriptor(self) -> MatchAlgorithms | None:
        """
        id: QRI.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRI.3
        """
        return self._c_data[2][0]

    @algorithm_descriptor.setter  # set QRI.3
    def algorithm_descriptor(self, match_algorithms: MatchAlgorithms | None):
        """
        id: QRI.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRI.3
        """
        self._c_data[2] = (match_algorithms,)
