from pathlib import Path

from jinja2 import Template, Environment, FileSystemLoader

from src.codegen.session import session
from src.codegen.clean import to_valid_variable_name


def render_data_type(
    hl7_id: str,
    version: str,
    comp_template: Template,
    prim_template: Template,
    path: Path,
):
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/DataTypes/{hl7_id}"
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
        map("from .{0} import {0}".format, data_type_imports_list)
    )
    data_type_example_imports = ", ".join(data_type_imports_list)

    init_params = []
    for i, f in enumerate(defs["fields"]):
        fn_name = to_valid_variable_name(f["name"]).lower()
        param_type = (
            f["tableName"]
            .replace("/", " or ")
            .title()
            .replace(" ", "")
            .replace("’", "")
            .replace("-", "")
            .replace("'", "")
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

    if defs["fields"]:  # complex type
        rendered = comp_template.render(
            x=defs,
            version=version,
            table_imports=table_imports,
            data_type_imports=data_type_imports,
            table_imports_examples=table_imports_examples,
            data_type_example_imports=data_type_example_imports,
            init_params=init_params,
        )
    else:  # primitive
        rendered = prim_template.render(x=defs, version=version)

    path.mkdir(parents=True, exist_ok=True)
    with open(path / f"{hl7_id}.py", "w") as f:
        f.write(rendered)


def get_all_data_type_ids(version: str) -> list[str]:
    r = session.get(
        f"https://hl7-definition.caristix.com/v2-api/1/HL7v{version}/DataTypes"
    )
    return [x["id"] for x in r.json()]


def render_data_types(version: str, target_path: Path):
    env = Environment(
        loader=FileSystemLoader("data_types"), trim_blocks=True, lstrip_blocks=True
    )
    component_template = env.get_template("composites.py.jinja2")
    primitive_template = env.get_template("primitives.py.jinja2")
    out_dir = target_path / Path("v" + version.replace(".", "_")) / "data_types"

    imports = []
    for hl7_id in get_all_data_type_ids(version):
        imports.append(f"from .{hl7_id} import {hl7_id}")
        print(f"Rendering {hl7_id}")
        render_data_type(
            hl7_id, version, component_template, primitive_template, out_dir
        )
    with open(out_dir / "__init__.py", "w") as f:
        f.write("\n".join(imports))
