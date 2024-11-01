from __future__ import annotations
from ...base import HL7Segment
from ..data_types.FT import FT
from ..data_types.ID import ID
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..tables.CommentType import CommentType
from ..tables.SourceOfComment import SourceOfComment


"""
Notes and Comments - NTE
HL7 Version: 2.5.1

-----BEGIN SEGMENT::NTE TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    NTE,
    FT, ID, SI, CE
)

nte = NTE(  #  - The NTE segment is defined here for inclusion in messages defined in other chapters
    set_id_nte=None,  # SI(...) 
    source_of_comment=None,  # ID(...) 
    comment=None,  # FT(...) 
    comment_type=None,  # CE(...) 
)

-----END SEGMENT::NTE TEMPLATE-----
"""


class NTE(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """NTE"""
    _hl7_name = """Notes and Comments"""
    _hl7_description = """The NTE segment is defined here for inclusion in messages defined in other chapters"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE"
    _c_length = (4, 8, 65536, 250,)
    _c_rpt = (1, 1, 65535, 1,)
    _c_usage = ("O", "O", "O", "O",)
    _c_components = (SI, ID, FT, CE,)
    _c_aliases = ("NTE.1", "NTE.2", "NTE.3", "NTE.4",)
    _c_names = ("Set ID - NTE", "Source of Comment", "Comment", "Comment Type",)
    _c_attrs = ("set_id_nte", "source_of_comment", "comment", "comment_type",)
    # fmt: on

    def __init__(
        self,
        set_id_nte: SI | tuple[SI] | None = None,  # NTE.1
        source_of_comment: SourceOfComment
        | ID
        | tuple[SourceOfComment | ID]
        | None = None,  # NTE.2
        comment: FT | tuple[FT] | None = None,  # NTE.3
        comment_type: CommentType | CE | tuple[CommentType | CE] | None = None,  # NTE.4
    ):
        """
        Notes and Comments - `NTE <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE>`_
        The NTE segment is defined here for inclusion in messages defined in other chapters. It is commonly used for sending notes and comments.

        :param set_id_nte: Sequence ID (id: NTE.1 | len: 4 | use: O | rpt: 1)
        :param source_of_comment: Coded values for HL7 tables (id: NTE.2 | len: 8 | use: O | rpt: 1)
        :param comment: Formatted Text Data (id: NTE.3 | len: 65536 | use: O | rpt: *)
        :param comment_type: Coded Element (id: NTE.4 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.set_id_nte = set_id_nte
        self.source_of_comment = source_of_comment
        self.comment = comment
        self.comment_type = comment_type

    @property  # get NTE.1
    def set_id_nte(self) -> SI | None:
        """
        id: NTE.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NTE.1
        """
        return self._c_data[0][0]

    @set_id_nte.setter  # set NTE.1
    def set_id_nte(self, si: SI | None):
        """
        id: NTE.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NTE.1
        """
        self._c_data[0] = (si,)

    @property  # get NTE.2
    def source_of_comment(self) -> SourceOfComment | None:
        """
        id: NTE.2 | len: 8 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NTE.2
        """
        return self._c_data[1][0]

    @source_of_comment.setter  # set NTE.2
    def source_of_comment(self, source_of_comment: SourceOfComment | None):
        """
        id: NTE.2 | len: 8 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NTE.2
        """
        self._c_data[1] = (source_of_comment,)

    @property
    def comment(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: NTE.3 | len: 65536 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NTE.3
        """
        return self._c_data[2]

    @comment.setter  # set NTE.3
    def comment(self, ft: FT | tuple[FT] | None):
        """
        id: NTE.3 | len: 65536 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NTE.3
        """
        if isinstance(ft, tuple):
            self._c_data[2] = ft
        else:
            self._c_data[2] = (ft,)

    @property  # get NTE.4
    def comment_type(self) -> CommentType | None:
        """
        id: NTE.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NTE.4
        """
        return self._c_data[3][0]

    @comment_type.setter  # set NTE.4
    def comment_type(self, comment_type: CommentType | None):
        """
        id: NTE.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NTE.4
        """
        self._c_data[3] = (comment_type,)
