from ...base import HL7Table

"""
HL7 Version: 2.5.1
Version ID - 0104
Table Type: HL7
"""


class VersionId(HL7Table):
    """
    Version ID - 0104 // HL7 table type
    - RELEASE_2_0
    - DEMO_2_0
    - RELEASE_2_1
    - RELEASE_2_2
    - RELEASE_2_3
    - RELEASE_2_3_1
    - RELEASE_2_4
    - RELEASE_2_5
    - RELEASE_2_5_1
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0104
    """

    RELEASE_2_0 = "2.0"  # September 1988
    """Release 2.0"""
    DEMO_2_0 = "2.0D"  # October 1988
    """Demo 2.0"""
    RELEASE_2_1 = "2.1"  # March 1990
    """Release 2. 1"""
    RELEASE_2_2 = "2.2"  # December 1994
    """Release 2.2"""
    RELEASE_2_3 = "2.3"  # March 1997
    """Release 2.3"""
    RELEASE_2_3_1 = "2.3.1"  # May 1999
    """Release 2.3.1"""
    RELEASE_2_4 = "2.4"  # November 2000
    """Release 2.4"""
    RELEASE_2_5 = "2.5"  # May 2003
    """Release 2.5"""
    RELEASE_2_5_1 = "2.5.1"  # January 2007
    """Release 2.5.1"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    VersionId.RELEASE_2_0: "Release 2.0",
    VersionId.DEMO_2_0: "Demo 2.0",
    VersionId.RELEASE_2_1: "Release 2. 1",
    VersionId.RELEASE_2_2: "Release 2.2",
    VersionId.RELEASE_2_3: "Release 2.3",
    VersionId.RELEASE_2_3_1: "Release 2.3.1",
    VersionId.RELEASE_2_4: "Release 2.4",
    VersionId.RELEASE_2_5: "Release 2.5",
    VersionId.RELEASE_2_5_1: "Release 2.5.1",
}
