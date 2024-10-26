from pathlib import Path

from jinja2 import Template, Environment, FileSystemLoader

from src.codegen.clean import (
    make_table_filename,
    sanitize_string,
    to_valid_variable_name,
)
from src.codegen.session import session


def get_all_table_ids(version: str) -> list[str]:
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/Tables"
    )
    return [x["id"] for x in r.json()]


def render_table(
    hl7_id: str, version: str, table_template: Template, path: Path
) -> str | None:
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/Tables/{hl7_id}"
    )
    defs = r.json()
    filename = make_table_filename(defs["name"])
    if filename in ["PhoneNumber", "Street"]:
        defs["entries"] = []

    delete_queue = []
    dupes = set()
    for i, e in enumerate(defs["entries"]):
        e["description"] = sanitize_string(e["description"])
        defs["entries"][i]["description"] = e["description"]
        try:
            long = to_valid_variable_name(e["description"])
            assert long not in dupes
            defs["entries"][i]["enum"] = long
            dupes.add(long)
        except Exception:
            try:
                long = to_valid_variable_name(e["value"])
                assert long not in dupes
                defs["entries"][i]["enum"] = long
                dupes.add(long)
            except Exception:
                try:
                    long = to_valid_variable_name(e["description"])
                    assert long
                    while long in dupes:
                        long += "_"
                    defs["entries"][i]["enum"] = long
                    dupes.add(long)
                except Exception:
                    delete_queue.append(i)

    ii = 0  # can't modify list in place
    for i in delete_queue:
        del defs["entries"][i - ii]
        ii += 1

    rendered = table_template.render(
        x=defs,
        version=version,
        filename=filename,
    )
    path.mkdir(parents=True, exist_ok=True)
    with open(path / f"{filename}.py", "w") as f:
        f.write(rendered)
    return filename


def render_tables(version: str, target_path: Path):
    env = Environment(
        loader=FileSystemLoader("tables"), trim_blocks=True, lstrip_blocks=True
    )
    table_template = env.get_template("tables.py.jinja2")
    out_dir = target_path / Path("v" + version.replace(".", "_")) / "tables"

    imports = []
    for hl7_id in get_all_table_ids(version):
        # if hl7_id != "0458":
        #     continue
        filename = render_table(hl7_id, version, table_template, out_dir)
        if not filename:
            continue
        print(f"Rendering {hl7_id} -> {filename}")
        imports.append(f"from .{filename} import {filename}")
    with open(out_dir / "__init__.py", "w") as f:
        f.write("\n".join(imports))
