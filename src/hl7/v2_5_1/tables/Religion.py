from ...base import HL7Table

"""
HL7 Version: 2.5.1
Religion - Religion
Table Type: PreLoaded
"""


class Religion(HL7Table):
    """
    Religion - Religion // PreLoaded table type
    - AFRICAN
    - ANIMIST
    - BAHAI
    - BUDDHISM
    - CAO
    - CHINESE
    - CHRISTIANITY
    - HINDUISM
    - IRRELIGIOUS_OR_AGNOSTIC_OR_ATHEISM
    - ISLAM
    - JAINISM
    - JUCHE
    - JUDAISM
    - MORMONISM
    - NEO_PAGANISM
    - RASTAFARI
    - SHINTO
    - SIKHISM
    - SPIRITISM
    - TENRIKYO
    - UNITARIAN
    - ZOROASTRIANISM
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/Religion
    """

    AFRICAN = "African"
    """"""
    ANIMIST = "Animist"
    """"""
    BAHAI = "Baha'i"
    """"""
    BUDDHISM = "Buddhism"
    """"""
    CAO = "Cao"
    """"""
    CHINESE = "Chinese"
    """"""
    CHRISTIANITY = "Christianity"
    """"""
    HINDUISM = "Hinduism"
    """"""
    IRRELIGIOUS_OR_AGNOSTIC_OR_ATHEISM = "Irreligious/agnostic/atheism"
    """"""
    ISLAM = "Islam"
    """"""
    JAINISM = "Jainism"
    """"""
    JUCHE = "Juche"
    """"""
    JUDAISM = "Judaism"
    """"""
    MORMONISM = "Mormonism"
    """"""
    NEO_PAGANISM = "Neo-Paganism"
    """"""
    RASTAFARI = "Rastafari"
    """"""
    SHINTO = "Shinto"
    """"""
    SIKHISM = "Sikhism"
    """"""
    SPIRITISM = "Spiritism"
    """"""
    TENRIKYO = "Tenrikyo"
    """"""
    UNITARIAN = "Unitarian"
    """"""
    ZOROASTRIANISM = "Zoroastrianism"
    """"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Religion.AFRICAN: "",
    Religion.ANIMIST: "",
    Religion.BAHAI: "",
    Religion.BUDDHISM: "",
    Religion.CAO: "",
    Religion.CHINESE: "",
    Religion.CHRISTIANITY: "",
    Religion.HINDUISM: "",
    Religion.IRRELIGIOUS_OR_AGNOSTIC_OR_ATHEISM: "",
    Religion.ISLAM: "",
    Religion.JAINISM: "",
    Religion.JUCHE: "",
    Religion.JUDAISM: "",
    Religion.MORMONISM: "",
    Religion.NEO_PAGANISM: "",
    Religion.RASTAFARI: "",
    Religion.SHINTO: "",
    Religion.SIKHISM: "",
    Religion.SPIRITISM: "",
    Religion.TENRIKYO: "",
    Religion.UNITARIAN: "",
    Religion.ZOROASTRIANISM: "",
}
