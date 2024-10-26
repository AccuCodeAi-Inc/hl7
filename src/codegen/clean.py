import re


def to_valid_variable_name(s):
    old = s
    if s == "...":
        s = "ANY"
    tr = str.maketrans(
        {
            "…": "_ANY_",
            "<": "_BELOW_",
            ">": "_ABOVE_",
            "!": "_IMPORTANT_",
            "@": "_AT_",
            "#": "_POUND_",
            "$": "_DOLLAR_",
            "%": "_PERCENT",
            "^": "_CARET_",
            "&": "_AND_",
            "+": "_PLUS_",
            "/": "_OR_",
            "=": "_EQUALS_",
            "~": "_",
            "*": "_STAR_",
            "`": "_",
            "|": "_",
            "\\": "_",
            "(": "_",
            ")": "_",
            "[": "_",
            "]": "_",
            "-": "_",
            ":": "_",
            ";": "_",
            ".": "_",
            ",": "_",
            "'": "",
            '"': "",
            "\n": "_",
            "\r": "_",
            "\t": "",
            " ": "_",
            "’": "_",
        }
    )
    if not s:
        raise ValueError("empty")
    s = "".join(char for char in s if ord(char) < 128)
    if not s:
        s = "DOT_DOT_DOT"
    s = s.split("(")[0]
    s = s.translate(tr)
    s = s.upper()
    while "__" in s:
        s = s.replace("__", "_")
    s = s.strip()
    s = s.strip("_")
    if re.match(r"^\d", s):
        s = "_" + s
    s = s[:256]
    try:
        compile(f"{s} = 1", "<testing_enum_suitability>", "exec")
    except SyntaxError as e:
        print("FAILED:")
        print(old)
        raise ValueError(str(e) + old)
    return s


def make_table_filename(name: str) -> str:
    return (
        name.replace("/", " or ")
        .title()
        .replace(" ", "")
        .replace("’", "")
        .replace("-", "")
        .replace("'", "")
        .replace("*", "")
        .replace(",", "")
        .split("(")[0]
    )


def sanitize_string(s: str) -> str:
    if not s:
        return ""
    escape_chars = {
        "\n": " ",  # newline
        "\r": " ",  # carriage return
        "\t": " ",  # tab
        "\b": "",  # backspace
        "\f": "",  # form feed
        "\v": "",  # vertical tab
        "\0": "",  # null character
        "\\": "",  # backslash
        "'": "",  # single quote
        '"': "",  # double quote
    }
    for escape_char, replacement in escape_chars.items():
        s = s.replace(escape_char, replacement)
    s = s.encode("ascii", errors="ignore").decode("ascii")
    s = " ".join(s.split())
    return s.strip()
