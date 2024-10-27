from __future__ import annotations
from ...base import HL7Primitive, HL7PrimitiveParseException
from datetime import datetime, date


"""
HL7 Version: 2.5.1
DataType - DT
"""


class DT(str, HL7Primitive):
    """
        DT - Date (len: 8)
        ---
        Specifies the century and year with optional precision to month and day.

    As of v 2.3, the number of digits populated specifies the precision using the format specification YYYY[MM[DD]].

    Prior to v 2.3, this data type was specified in the format YYYYMMDD. As of v 2.3 month and days are no longer required. By site-specific agreement, YYYYMMDD may be used where backward compatibility must be maintained.

    Examples:
    |19880704|
    |199503|
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DT
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 8
    _hl7_id = """DT"""
    _hl7_name = """Date"""
    _hl7_description = (
        """Specifies the century and year with optional precision to month and day"""
    )
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DT"

    def __new__(cls, yymmdd: str):
        if len(yymmdd) > 8:
            raise HL7PrimitiveParseException(
                "DT - Date content exceeds maximum length of 8 characters"
            )
        return super().__new__(cls, yymmdd)

    @classmethod
    def from_datetime(cls, dt: datetime) -> DT:
        """Create a DT instance from a datetime object."""
        return cls(dt.strftime("%Y%m%d"))

    @classmethod
    def from_date(cls, d: date) -> DT:
        """Create a DT instance from a date object."""
        return cls(d.strftime("%Y%m%d"))

    @classmethod
    def from_ymd(
        cls, year: int, month: int | None = None, day: int | None = None
    ) -> DT:
        """
        Create a DT instance from year, month, and day components.
        Month and day are optional per HL7 v2.3+ specification.
        """
        if not 1 <= year <= 9999:
            raise HL7PrimitiveParseException("Year must be between 1 and 9999")

        result = f"{year:04d}"

        if month is not None:
            if not 1 <= month <= 12:
                raise HL7PrimitiveParseException("Month must be between 1 and 12")
            result += f"{month:02d}"

            if day is not None:
                if (
                    not 1 <= day <= 31
                ):  # Simple validation, doesn't check month-specific day limits
                    raise HL7PrimitiveParseException("Day must be between 1 and 31")
                result += f"{day:02d}"
        elif day is not None:
            raise HL7PrimitiveParseException("Cannot specify day without month")

        return cls(result)

    @classmethod
    def today(cls) -> DT:
        """Create a DT instance for today's date."""
        return cls.from_date(date.today())

    @classmethod
    def from_iso(cls, iso_date: str) -> DT:
        """Create a DT instance from an ISO format date string (YYYY-MM-DD)."""
        try:
            return cls.from_date(date.fromisoformat(iso_date))
        except HL7PrimitiveParseException:
            raise HL7PrimitiveParseException(
                "Invalid ISO date format. Expected YYYY-MM-DD"
            )

    def to_datetime(self) -> datetime:
        """Convert to datetime object. Time components will be set to midnight."""
        length = len(self)
        if length == 4:
            return datetime(int(self), 1, 1)
        elif length == 6:
            return datetime(int(self[:4]), int(self[4:6]), 1)
        elif length == 8:
            return datetime(int(self[:4]), int(self[4:6]), int(self[6:8]))
        else:
            raise HL7PrimitiveParseException("Invalid DT format")

    def to_date(self) -> date:
        """Convert to date object."""
        return self.to_datetime().date()

    def to_iso(self) -> str:
        """Convert to ISO format (YYYY-MM-DD)."""
        length = len(self)
        if length == 4:
            return f"{self}"
        elif length == 6:
            return f"{self[:4]}-{self[4:6]}"
        elif length == 8:
            return f"{self[:4]}-{self[4:6]}-{self[6:8]}"
        else:
            raise HL7PrimitiveParseException("Invalid DT format")

    @property
    def year(self) -> int:
        """Get the year component."""
        return int(self[:4])

    @property
    def month(self) -> int | None:
        """Get the month component if available."""
        return int(self[4:6]) if len(self) >= 6 else None

    @property
    def day(self) -> int | None:
        """Get the day component if available."""
        return int(self[6:8]) if len(self) == 8 else None
