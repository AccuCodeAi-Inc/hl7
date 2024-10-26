from pathlib import Path

from jinja2 import Template, Environment, FileSystemLoader

from src.codegen.session import session
from src.codegen.clean import to_valid_variable_name


def render_segment(hl7_id: str, version: str, seg_template: Template, path: Path):
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/Segments/{hl7_id}"
    )
    defs = r.json()

    def fmt_table(x):
        return (
            x.replace("/", " or ")
            .title()
            .replace(" ", "")
            .replace("’", "")
            .replace("-", "")
            .replace("'", "")
            .replace("*", "_")
            .replace(")", "")
            .replace("(", "")
            .replace(".", "_")
            .replace(",", "_")
        )

    table_imports_list = set(
        fmt_table(f["tableName"]) for f in defs["fields"] if f["tableName"]
    )
    table_imports = "\n".join(
        map("from ..tables.{0} import {0}".format, table_imports_list)
    )
    table_imports_examples = ", ".join(table_imports_list)

    data_type_imports_list = set(f["dataType"] for f in defs["fields"])
    data_type_imports = "\n".join(
        map("from ..data_types.{0} import {0}".format, data_type_imports_list)
    )
    data_type_example_imports = ", ".join(data_type_imports_list)

    init_params = []
    fn_set = set()
    for i, f in enumerate(defs["fields"]):
        fn_name = to_valid_variable_name(f["name"]).lower()
        if fn_name in fn_set:
            fn_name = f"{fn_name}_{i}"
        fn_set.add(fn_name)
        param_type = (
            f["tableName"]
            .replace("*", "_")
            .replace("/", " or ")
            .title()
            .replace(" ", "")
            .replace("’", "")
            .replace("-", "")
            .replace("'", "")
            .replace(")", "")
            .replace("(", "")
            .replace(".", "_")
            .replace(",", "_")
            + " | "
            + f["dataType"]
            if f["tableName"]
            else f["dataType"]
        )
        defs["fields"][i]["param_type"] = param_type
        defs["fields"][i]["fn_name"] = fn_name
        suffix = "" if f["usage"] == "R" else " | None = None"
        init_params.append(
            f"        {fn_name}: {param_type}{suffix},  # {f["position"]}"
        )

    default_params = [ip for ip in init_params if " | None = None" in ip]
    non_default_params = [ip for ip in init_params if " | None = None" not in ip]
    init_params = "\n".join(non_default_params + default_params)

    rendered = seg_template.render(
        x=defs,
        version=version,
        table_imports=table_imports,
        data_type_imports=data_type_imports,
        data_type_example_imports=data_type_example_imports,
        table_imports_examples=table_imports_examples,
        init_params=init_params,
    )

    path.mkdir(parents=True, exist_ok=True)
    with open(path / f"{hl7_id}.py", "w") as f:
        f.write(rendered)


def get_all_segment_ids(version: str) -> list[str]:
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/Segments"
    )
    return [x["id"] for x in r.json()]


def render_segments(version: str, target_path: Path):
    env = Environment(
        loader=FileSystemLoader("./segments"), trim_blocks=True, lstrip_blocks=True
    )
    seg_template = env.get_template("segments.py.jinja2")
    out_dir = target_path / Path("v" + version.replace(".", "_")) / "segments"

    imports = []
    for hl7_id in get_all_segment_ids(version):
        imports.append(f"from .{hl7_id} import {hl7_id}")
        print(f"Rendering {hl7_id}")
        render_segment(hl7_id, version, seg_template, out_dir)
    with open(out_dir / "__init__.py", "w") as f:
        f.write("\n".join(imports))
