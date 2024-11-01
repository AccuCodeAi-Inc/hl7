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
        dt = super().__new__(cls, yymmdd)
        dt._validate_or_raise()
        return dt

    def _validate_or_raise(self):
        if len(self) == 0:
            raise HL7PrimitiveParseException("DT - Date content is empty")

        if len(self) > 8:
            raise HL7PrimitiveParseException(
                "DT - Date content exceeds maximum length of 8 characters"
            )
        # Year validation (1000-3000)
        if not (1000 <= self.year <= 3000):
            raise HL7PrimitiveParseException(
                f"DTM - Invalid year: {self.year}. Must be between 1000 and 3000"
            )

        # Month validation (1-12)
        if self.month is not None and not (1 <= self.month <= 12):
            raise HL7PrimitiveParseException(
                f"DTM - Invalid month: {self.month}. Must be between 1 and 12"
            )

        # Day validation (1-31, considering month)
        if self.day is not None:
            days_in_month = {
                1: 31,
                2: 29 if self._is_leap_year() else 28,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31,
            }
            max_days = days_in_month.get(self.month, 31)
            if not (1 <= self.day <= max_days):
                raise HL7PrimitiveParseException(
                    f"DTM - Invalid day: {self.day} for month {self.month}. Must be between 1 and {max_days}"
                )

    def _is_leap_year(self):
        """Helper method to determine if the current year is a leap year"""
        if self.year is None:
            return False
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

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
            iso_date = iso_date.replace("/", "").replace("-", "")
            return cls.from_date(date.fromisoformat(iso_date))
        except Exception as e:
            raise HL7PrimitiveParseException(
                "Invalid ISO date format. Expected YYYY-MM-DD"
            ) from e

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
