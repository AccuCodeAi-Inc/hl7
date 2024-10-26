from pathlib import Path
from jinja2 import Template, Environment, FileSystemLoader
from src.codegen.session import session
from src.codegen.clean import to_valid_variable_name


def extract_segment_imports(segments, hl7_id) -> set[str]:
    _set = set()
    for segment in segments:
        if segment["isGroup"]:
            sname = to_valid_variable_name(segment["name"]).upper()
            _set.add(
                "from ..segment_groups.{0} import {0}".format(f"{hl7_id}_{sname}_GROUP")
            )
        else:
            sname = to_valid_variable_name(segment["id"]).upper()
            _set.add("from ..segments.{0} import {0}".format(sname))
    return _set


def extract_segment_imports_examples(segments, hl7_id) -> tuple[set[str], set[str]]:
    _set = set()
    _set_group = set()
    for segment in segments:
        if segment["isGroup"]:
            sname = to_valid_variable_name(segment["name"]).upper()
            _set_group.add(f"{hl7_id}_{sname}_GROUP")
        else:
            sname = to_valid_variable_name(segment["id"]).upper()
            _set.add(sname)
    return _set, _set_group


def render_trigger_event(
    hl7_id: str, version: str, seg_template: Template, path: Path, defs=None
) -> list[str]:  # returns segment_group_imports
    hl7_id = hl7_id.replace(" ", "_")
    parent_class = "HL7TriggerEvent" if not defs else "HL7SegmentGroup"
    subtype = "TRIGGER_EVENT" if not defs else "TRIGGER_EVENT_SEGMENT_GROUP"
    if not defs:
        r = session.get(
            f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/TriggerEvents/{hl7_id}"
        )
        defs = r.json()
    segment_imports = "\n".join(extract_segment_imports(defs["segments"], hl7_id))
    ex, group_ex = extract_segment_imports_examples(defs["segments"], hl7_id)
    segment_imports_examples = ", ".join(ex)
    segment_group_imports_examples = ", ".join(group_ex)

    init_params = []
    dupes = set()
    segment_group_imports = []
    for i, f in enumerate(defs["segments"]):
        try:
            fn_name = to_valid_variable_name(f["longName"]).lower()
        except:
            fn_name = to_valid_variable_name(f["name"]).lower()

        if fn_name in dupes:
            fn_name = f"{fn_name}_{f["sequence"]}"
        # param_type = f["tableName"].replace("/", " or ").title().replace(" ", "").replace("’", "").replace("-", "").replace("'", "") if f["tableName"] and f["dataType"] in ["IS", "ST", "ID"] else f["dataType"]
        suffix = "" if f["usage"] == "R" else " | None = None"
        required = " Required." if f["usage"] == "R" else ""
        if f["isGroup"]:
            segnames = (x["name"] for x in f["segments"])
            segsuffix = map(
                lambda x: "" if x["usage"] == "R" else "|None", f["segments"]
            )
            segs = ", ".join(sn + ss for sn, ss in zip(segnames, segsuffix))
            defs["segments"][i]["segs"] = segs
            seqs = ", ".join(
                x["name"] + "." + x["sequence"] for x in f["segments"] if x["sequence"]
            )
            group_suffix = ", ..." if f["rpt"] != "1" else ""
            sname = to_valid_variable_name(f["name"])
            pname = f"{defs['id']}_{sname}_GROUP".strip().replace(" ", "_")
            # param_type = f"tuple[{segs}{group_suffix}]"
            # group_aliases.append(f"{pname} = {param_type}")
            # group_aliases.append('"""')
            # for ff in f["segments"]:
            #     group_aliases.append(f"{ff['name']} - {ff['longName']} (use: {ff['usage']} | rpt: {ff['rpt']})")
            # group_aliases.append('"""')
            defs["segments"][i]["param_type"] = pname
            if f["rpt"] != "1":
                init_params.append(
                    f"        {fn_name}: {pname} | tuple[{pname}{group_suffix}]{suffix},  # {required} ({seqs}, ...)"
                )
            else:
                init_params.append(
                    f"        {fn_name}: {pname}{suffix},  # {required} {seqs}"
                )

            rdefs = f
            rdefs.update(
                {
                    "id": pname,
                    "eventDesc": f["name"],
                    "description": f"Segment group for {defs['id']} - {defs['eventDesc']} consisting of {segs}",
                }
            )
            new_path = path / ".." / "segment_groups"
            render_trigger_event(pname, version, seg_template, new_path, defs=rdefs)
            segment_group_imports.append(f"from .{pname} import {pname}")

        else:
            param_type = f["name"].replace(" ", "_")
            defs["segments"][i]["param_type"] = param_type
            if f["rpt"] != "1":
                init_params.append(
                    f"        {fn_name}: {param_type} | tuple[{param_type}, ...]{suffix},  # {required} {f["id"]}.{f["sequence"]}"
                )
            else:
                init_params.append(
                    f"        {fn_name}: {param_type}{suffix},  # {required} {f["id"]}.{f["sequence"]}"
                )
        defs["segments"][i]["fn_name"] = fn_name
        # group_types = "\n".join(group_aliases)
        dupes.add(fn_name)

    default_params = [ip for ip in init_params if " | None = None" in ip]
    non_default_params = [ip for ip in init_params if " | None = None" not in ip]
    init_params = "\n".join(non_default_params + default_params)

    rendered = seg_template.render(
        x=defs,
        version=version,
        segment_imports_examples=segment_imports_examples,
        init_params=init_params,
        segment_imports=segment_imports,
        segment_group_imports_examples=segment_group_imports_examples,
        parent_class=parent_class,
        subtype=subtype,
    )

    path.mkdir(parents=True, exist_ok=True)
    with open(path / f"{hl7_id}.py", "w") as f:
        f.write(rendered)

    return segment_group_imports


def get_all_trigger_event_ids(version: str) -> list[str]:
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/TriggerEvents"
    )
    return [x["id"] for x in r.json()]


def render_trigger_events(version: str, target_path: Path):
    env = Environment(
        loader=FileSystemLoader("trigger_events"), trim_blocks=True, lstrip_blocks=True
    )
    trig_template = env.get_template("trigger_events.py.jinja2")
    out_dir = target_path / Path("v" + version.replace(".", "_")) / "trigger_events"

    imports = []
    segment_group_imports = []
    for hl7_id in get_all_trigger_event_ids(version):
        imports.append(f"from .{hl7_id} import {hl7_id}")
        print(f"Rendering {hl7_id}")
        r = render_trigger_event(hl7_id, version, trig_template, out_dir)
        segment_group_imports.extend(r)
    with open(out_dir / "__init__.py", "w") as f:
        f.write("\n".join(imports))
    with open(out_dir / ".." / "segment_groups" / "__init__.py", "w") as f:
        f.write("\n".join(segment_group_imports))
