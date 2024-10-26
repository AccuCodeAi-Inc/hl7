import os

from src.codegen.clean import make_table_filename, to_valid_variable_name
from src.codegen.session import session
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

PRIMITIVES = {"NM", "ST", "ID", "DT", "TM", "DTM", "SI", "IS", "TX", "VARIES"}


def is_empty_table(hl7_id: str, version: str):
    component = "Tables"
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/{component}/{hl7_id}"
    )
    defs = r.json()
    return not defs["entries"]


def generate_component_template(
    hl7_id: str, version: str, indent: int, usage: str, depth=0, component="Segments"
):
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/{component}/{hl7_id}"
    )
    defs = r.json()
    data_type_imports = set()
    table_imports = set()
    buf = defs["id"]
    banned_tables = ["Street", "PhoneNumber"]

    buf += "("
    # if defs["fields"]:
    # buf += f" # {usage}"
    fn_set = set()
    for i, f in enumerate(defs["fields"]):
        fn_name = to_valid_variable_name(f["name"]).lower()
        if fn_name in fn_set:
            fn_name = f"{fn_name}_{i}"
        fn_set.add(fn_name)
        buf += "\n"
        buf += " " * indent
        buf += fn_name
        buf += "="

        # if f["rpt"] != "1":
        #     buf += "("
        #     buf += f" # rpt:{f["rpt"]}"
        #     buf += "\n"
        #     buf += " " * (indent + 4)

        if (
            f["tableName"]
            and not is_empty_table(f["tableId"], version)
            and make_table_filename(f["tableName"]) not in banned_tables
        ):
            if is_empty_table(f["tableId"], version):
                t = f["dataType"]
            else:
                t = make_table_filename(f["tableName"])
            table_imports.add(t)
            buf += t
            # buf += ".parse(x, using=llm_parser),"
            buf += ".parse(\n"
            buf += " " * (indent + 4)
            buf += "x, using=llm_parser\n"
            buf += " " * indent
            buf += "),"

        else:
            type_ = "DataTypes"
            # offset = 8 if f["rpt"] != "1" else 8
            t, ti, dt = generate_component_template(
                f["dataType"], version, indent + 4, f["usage"], depth + 1, type_
            )
            buf += t
            data_type_imports.add(f["dataType"])
            data_type_imports |= dt
            table_imports |= ti
            # buf += "x"
            # buf += "),"

            if f["dataType"] in PRIMITIVES:
                buf += "x),"
            else:
                buf += "\n"
                buf += " " * indent
                buf += "),"

        # if f["rpt"] != "1":
        #     buf += "\n"
        #     buf += " " * indent
        #     buf += ")"

    if depth == 0:
        buf += "\n"
        buf += " " * (indent - 4)
        buf += ")"
    buf = buf.strip(",")
    return buf, table_imports, data_type_imports


def align_comments(x: str, maxwidth=100) -> str:
    res = []
    for line in x.split("\n"):
        if "#" not in line:
            res.append(line)
            continue
        code, comment = line.split("#", 1)
        indent = code.rstrip().count(" ")
        comment = "#" + comment
        comment = comment.strip()
        comment += " " * (24 - indent)
        code += comment.rjust(maxwidth - len(code))
        res.append(code)
    return "\n".join(res)


def generate_trigger_event_template(hl7_id: str, version: str, init_indent: 0):
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/TriggerEvents/{hl7_id}"
    )
    defs = r.json()
    buf = " " * init_indent
    buf += defs["msgStructId"].lower()
    buf += " = "
    buf += defs["msgStructId"]
    buf += "("
    indent = init_indent + 4

    data_type_imports = set()
    table_imports = set()
    segment_imports = set()
    segment_group_imports = set()
    component_ids = []
    component_use = []
    component_seq = []

    dupes = set()
    for seg in defs["segments"]:
        try:
            fn_name = to_valid_variable_name(seg["longName"]).lower()
        except:
            fn_name = to_valid_variable_name(seg["name"]).lower()
        if fn_name in dupes:
            fn_name = f"{fn_name}_{seg["sequence"]}"
        dupes.add(fn_name)

        if not seg["isGroup"]:
            buf += "\n"
            buf += " " * indent
            buf += fn_name
            buf += "="
            component_ids.append(seg["id"])
            component_use.append(seg["usage"])
            component_seq.append(seg["sequence"])
            segment_imports.add(seg["id"])
            # table_imports |= ti
            # data_type_imports |= di
            if seg["rpt"] != "1":
                buf += "("
                buf += f" # rpt:{seg["rpt"]}"
                buf += "\n"
                buf += " " * (indent + 4)
                buf += f"await build({seg["id"].lower()}_{seg["sequence"]}),"
                buf += "\n"
                buf += " " * (indent)
                buf += "),"
            else:
                buf += f"await build({seg["id"].lower()}_{seg["sequence"]}),"
        else:
            buf += "\n"
            buf += " " * indent
            buf += fn_name
            buf += "="
            if seg["rpt"] != "1":
                buf += "("
                buf += f" # rpt:{seg['rpt']}"
                buf += "\n"
                for i in range(2):
                    pname = f"{defs['id']}_{seg['name']}_GROUP".strip().replace(
                        " ", "_"
                    )
                    segment_group_imports.add(pname)
                    buf += " " * (indent + 4)
                    buf += pname
                    buf += "("
                    for s in seg["segments"]:
                        buf += "\n"
                        buf += " " * (indent + 8)
                        buf += to_valid_variable_name(s["longName"]).lower()
                        buf += "="
                        # table_imports |= ti
                        # data_type_imports |= di
                        segment_imports.add(s["id"])
                        buf += f"await build({s["id"].lower()}_{s["sequence"]}),"
                        if i == 0:
                            component_ids.append(s["id"])
                            component_use.append(s["usage"])
                            component_seq.append(s["sequence"])
                    buf += "\n"
                    buf += " " * (indent + 4)
                    buf += "),"
                    if i == 0:
                        buf += "\n"
            else:
                pname = f"{defs['id']}_{seg['name']}_GROUP".strip().replace(" ", "_")
                buf += pname
                buf += "("
                for s in seg["segments"]:
                    buf += "\n"
                    buf += " " * (indent + 4)
                    buf += to_valid_variable_name(s["longName"]).lower()
                    buf += "="
                    segment_imports.add(s["id"])
                    component_ids.append(s["id"])
                    component_use.append(s["usage"])
                    component_seq.append(s["sequence"])
                    # table_imports |= ti
                    # data_type_imports |= di
                    buf += f"await build({s["id"].lower()}_{s["sequence"]}),"
                # buf += t

            buf += "\n"
            buf += " " * indent
            buf += "),"

    buf += "\n"
    buf += " " * init_indent
    buf += ")"
    return (
        buf,
        {defs["msgStructId"]},
        segment_imports,
        segment_group_imports,
        table_imports,
        data_type_imports,
        defs["description"],
        component_ids,
        component_use,
        component_seq,
    )


def get_component_description(version, hl7_id, component="Segments"):
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/{component}/{hl7_id}"
    )
    defs = r.json()
    return defs["description"]


if __name__ == "__main__":
    version = "2.5.1"
    hl7_id = "ADT_A08"

    env = Environment(
        loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True
    )
    trig_template = env.get_template("temporal.py.jinja2")
    # out_dir = Path("v" + version.replace(".", "_")) / "trigger_events"
    # x, table_imports, data_type_imports = generate_component_template(hl7_id, version, 4, "O", 0, "Segments")
    # print(align_comments(x))
    # print(table_imports)
    # print(data_type_imports)
    (
        tmpl,
        tei,
        si,
        sgi,
        ti,
        di,
        description,
        component_ids,
        component_use,
        component_seq,
    ) = generate_trigger_event_template(hl7_id, version, init_indent=8)

    activities = []
    for cid, use, seq in zip(component_ids, component_use, component_seq):
        ctmpl, ti_, di_ = generate_component_template(
            cid, version, 8, usage=use, depth=0, component="Segments"
        )
        activities.append(
            {
                "tmpl": ctmpl,
                "component_id": cid,
                "description": get_component_description(version, cid),
                "sequence": seq,
            }
        )
        ti |= ti_
        di |= di_
    # print(align_comments(tmpl))
    # print(tei)
    # print(si)
    # print(ti)
    # print(di)

    x = trig_template.render(
        tmpl=align_comments(tmpl),
        activities=activities,
        description=description,
        version=version,
        hl7_id=hl7_id,
        trigger_event_imports=tei,
        segment_imports=si,
        segment_group_imports=sgi,
        data_type_imports=di,
        table_imports=ti,
    )

    TARGET = Path(__file__).parent.parent.parent.parent / "examples"
    os.makedirs(TARGET, exist_ok=True)
    with open(TARGET / f"{hl7_id}.py", "w") as f:
        f.write(x)
    print(x)
