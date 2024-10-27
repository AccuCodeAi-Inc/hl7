from ...base import HL7Table

"""
HL7 Version: 2.5.1
State - State
Table Type: PreLoaded
"""


class State(HL7Table):
    """
    State - State // PreLoaded table type
    - ALABAMA
    - ALASKA
    - ARIZONA
    - ARKANSAS
    - CALIFORNIA
    - COLORADO
    - CONNECTICUT
    - DELAWARE
    - FLORIDA
    - GEORGIA
    - HAWAII
    - IDAHO
    - ILLINOIS
    - INDIANA
    - IOWA
    - KANSAS
    - KENTUCKY
    - LOUISIANA
    - MAINE
    - MARYLAND
    - MASSACHUSETTS
    - MICHIGAN
    - MINNESOTA
    - MISSISSIPPI
    - MISSOURI
    - MONTANA
    - NEBRASKA
    - NEVADA
    - NEW_HAMPSHIRE
    - NEW_JERSEY
    - NEW_MEXICO
    - NEW_YORK
    - NORTH_CAROLINA
    - NORTH_DAKOTA
    - OHIO
    - OKLAHOMA
    - OREGON
    - PENNSYLVANIA
    - RHODE_ISLAND
    - SOUTH_CAROLINA
    - SOUTH_DAKOTA
    - TENNESSEE
    - TEXAS
    - UTAH
    - VERMONT
    - VIRGINIA
    - WASHINGTON
    - WEST_VIRGINIA
    - WISCONSIN
    - WYOMING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/State
    """

    ALABAMA = "Alabama"
    """"""
    ALASKA = "Alaska"
    """"""
    ARIZONA = "Arizona"
    """"""
    ARKANSAS = "Arkansas"
    """"""
    CALIFORNIA = "California"
    """"""
    COLORADO = "Colorado"
    """"""
    CONNECTICUT = "Connecticut"
    """"""
    DELAWARE = "Delaware"
    """"""
    FLORIDA = "Florida"
    """"""
    GEORGIA = "Georgia"
    """"""
    HAWAII = "Hawaii"
    """"""
    IDAHO = "Idaho"
    """"""
    ILLINOIS = "Illinois"
    """"""
    INDIANA = "Indiana"
    """"""
    IOWA = "Iowa"
    """"""
    KANSAS = "Kansas"
    """"""
    KENTUCKY = "Kentucky"
    """"""
    LOUISIANA = "Louisiana"
    """"""
    MAINE = "Maine"
    """"""
    MARYLAND = "Maryland"
    """"""
    MASSACHUSETTS = "Massachusetts"
    """"""
    MICHIGAN = "Michigan"
    """"""
    MINNESOTA = "Minnesota"
    """"""
    MISSISSIPPI = "Mississippi"
    """"""
    MISSOURI = "Missouri"
    """"""
    MONTANA = "Montana"
    """"""
    NEBRASKA = "Nebraska"
    """"""
    NEVADA = "Nevada"
    """"""
    NEW_HAMPSHIRE = "New Hampshire"
    """"""
    NEW_JERSEY = "New Jersey"
    """"""
    NEW_MEXICO = "New Mexico"
    """"""
    NEW_YORK = "New York  "
    """"""
    NORTH_CAROLINA = "North Carolina"
    """"""
    NORTH_DAKOTA = "North Dakota"
    """"""
    OHIO = "Ohio"
    """"""
    OKLAHOMA = "Oklahoma"
    """"""
    OREGON = "Oregon"
    """"""
    PENNSYLVANIA = "Pennsylvania"
    """"""
    RHODE_ISLAND = "Rhode Island"
    """"""
    SOUTH_CAROLINA = "South Carolina"
    """"""
    SOUTH_DAKOTA = "South Dakota"
    """"""
    TENNESSEE = "Tennessee"
    """"""
    TEXAS = "Texas"
    """"""
    UTAH = "Utah"
    """"""
    VERMONT = "Vermont"
    """"""
    VIRGINIA = "Virginia"
    """"""
    WASHINGTON = "Washington"
    """"""
    WEST_VIRGINIA = "West Virginia"
    """"""
    WISCONSIN = "Wisconsin"
    """"""
    WYOMING = "Wyoming"
    """"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    State.ALABAMA: "",
    State.ALASKA: "",
    State.ARIZONA: "",
    State.ARKANSAS: "",
    State.CALIFORNIA: "",
    State.COLORADO: "",
    State.CONNECTICUT: "",
    State.DELAWARE: "",
    State.FLORIDA: "",
    State.GEORGIA: "",
    State.HAWAII: "",
    State.IDAHO: "",
    State.ILLINOIS: "",
    State.INDIANA: "",
    State.IOWA: "",
    State.KANSAS: "",
    State.KENTUCKY: "",
    State.LOUISIANA: "",
    State.MAINE: "",
    State.MARYLAND: "",
    State.MASSACHUSETTS: "",
    State.MICHIGAN: "",
    State.MINNESOTA: "",
    State.MISSISSIPPI: "",
    State.MISSOURI: "",
    State.MONTANA: "",
    State.NEBRASKA: "",
    State.NEVADA: "",
    State.NEW_HAMPSHIRE: "",
    State.NEW_JERSEY: "",
    State.NEW_MEXICO: "",
    State.NEW_YORK: "",
    State.NORTH_CAROLINA: "",
    State.NORTH_DAKOTA: "",
    State.OHIO: "",
    State.OKLAHOMA: "",
    State.OREGON: "",
    State.PENNSYLVANIA: "",
    State.RHODE_ISLAND: "",
    State.SOUTH_CAROLINA: "",
    State.SOUTH_DAKOTA: "",
    State.TENNESSEE: "",
    State.TEXAS: "",
    State.UTAH: "",
    State.VERMONT: "",
    State.VIRGINIA: "",
    State.WASHINGTON: "",
    State.WEST_VIRGINIA: "",
    State.WISCONSIN: "",
    State.WYOMING: "",
}
