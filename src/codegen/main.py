from pathlib import Path
from data_types.data_types import render_data_types
from segments.segments import render_segments
from tables.tables import render_tables
from trigger_events.trigger_events import render_trigger_events
from session import session

"""
This is a code generator for the HL7 lib which builds the entire library based on scraped data from carastix
- archive of the raw source data can be found here: https://github.com/AccuCodeAi-Inc/HL7Scrape
- talk to kevin if you want to make changes as there's a lot of sharp corners in this code generator
"""


def get_all_versions() -> list[str]:
    r = session.get("https://hl7-definition.caristix.com/v2-api/1/ConformanceProfiles")
    return [
        k["key"].replace("HL7v", "")
        for k in r.json()
        if k["group"] == "HL7 International"
    ]


if __name__ == "__main__":
    TARGET = Path("../hl7")

    for version in get_all_versions():
        if version != "2.5.1":
            continue
        render_trigger_events(version, TARGET)
        render_segments(version, TARGET)
        render_data_types(version, TARGET)
        render_tables(version, TARGET)
