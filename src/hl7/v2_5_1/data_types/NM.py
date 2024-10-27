from __future__ import annotations
from ...base import HL7Primitive, HL7PrimitiveParseException


"""
HL7 Version: 2.5.1
DataType - NM
"""


class NM(str, HL7Primitive):
    """
        NM - Numeric (len: 16)
        ---
        A number represented as a series of ASCII numeric characters consisting of an optional leading sign (+ or -), the digits and an optional decimal point. In the absence of a sign, the number is assumed to be positive. If there is no decimal point the number is assumed to be an integer.

    Examples:
    |999|
    |-123.792|
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NM
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 16
    _hl7_id = """NM"""
    _hl7_name = """Numeric"""
    _hl7_description = """A number represented as a series of ASCII numeric characters consisting of an optional leading sign (+ or -), the digits and an optional decimal point"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NM"

    def __new__(cls, nm: str | int | float):
        content = str(nm)
        if len(content) > 16:
            raise HL7PrimitiveParseException(
                "NM content exceeds maximum length of 16 characters"
            )
        # Validate format (optional sign, digits, optional decimal point)
        if not content.replace(".", "").replace("-", "").replace("+", "").isdigit():
            raise HL7PrimitiveParseException("Invalid numeric format")
        return super().__new__(cls, content)

    def __add__(self, other):
        """Add two NM values or NM and a number."""
        return NM(float(self) + float(other))

    def __sub__(self, other):
        """Subtract two NM values or NM and a number."""
        return NM(float(self) - float(other))

    def __mul__(self, other):
        """Multiply two NM values or NM and a number."""
        return NM(float(self) * float(other))

    def __truediv__(self, other):
        """Divide two NM values or NM and a number."""
        return NM(float(self) / float(other))

    @classmethod
    def from_int(cls, value: int) -> NM:
        """Create NM from integer."""
        return cls(str(value))

    @classmethod
    def from_float(cls, value: float, precision: int = None) -> NM:
        """Create NM from float with optional precision."""
        if precision is not None:
            return cls(f"{value:.{precision}f}")
        return cls(str(value))

    def to_int(self) -> int:
        """Convert to integer (truncates decimal part)."""
        return int(float(self))

    def to_float(self) -> float:
        """Convert to float."""
        return float(self)

    @property
    def is_integer(self) -> bool:
        """Check if the number is an integer (no decimal part)."""
        return float(self).is_integer()

    @property
    def is_positive(self) -> bool:
        """Check if the number is positive."""
        return float(self) > 0

    @property
    def is_negative(self) -> bool:
        """Check if the number is negative."""
        return float(self) < 0
        # Convert input to string if it's a number
