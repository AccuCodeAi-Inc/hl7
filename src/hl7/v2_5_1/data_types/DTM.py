from __future__ import annotations
from ...base import HL7Primitive, HL7PrimitiveParseException

from datetime import datetime, time
from zoneinfo import ZoneInfo
import re


"""
HL7 Version: 2.5.1
DataType - DTM
"""


class DTM(str, HL7Primitive):
    """
        DTM - Date/Time (len: 24)
        ---
        Specifies a point in time using a 24-hour clock notation.

    Format: YYYY[MM[DD[HH[MM[SS[.S[S[S[S]]]]]]]]][+/-ZZZZ].
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DTM
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 24
    _hl7_id = """DTM"""
    _hl7_name = """Date/Time"""
    _hl7_description = """Specifies a point in time using a 24-hour clock notation"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DTM"

    _DTM_PATTERN = re.compile(
        r"^(\d{4})"  # Year (required)      - 1 group
        r"(?:(\d{2})"  # Month (optional)     - 2 groups
        r"(?:(\d{2})"  # Day (optional)       - 3 groups
        r"(?:(\d{2})"  # Hour (optional)      - 4 groups
        r"(?:(\d{2})"  # Minute (optional)    - 5 groups
        r"(?:(\d{2})"  # Second (optional)    - 6 groups
        r"(?:\.(\d{1,4}))?)?)?)?)?)?"  # Fractional second   - 7 groups
        r"(?:([+-])(\d{2})(\d{2}))?$"  # Timezone (optional) - 10 groups total
    )

    def __new__(cls, dtm: str):
        if len(dtm) > 24:
            raise HL7PrimitiveParseException(
                "DTM - Date/Time content exceeds maximum length of 24 characters"
            )

        if not cls._DTM_PATTERN.match(dtm):
            raise HL7PrimitiveParseException("DTM - Invalid date/time format")

        dtm = super().__new__(cls, dtm)
        dtm._validate_or_raise()
        return dtm

    def _validate_or_raise(self):
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

        # Hour validation (0-23)
        if self.hour is not None and not (0 <= self.hour <= 23):
            raise HL7PrimitiveParseException(
                f"DTM - Invalid hour: {self.hour}. Must be between 0 and 23"
            )

        # Minute validation (0-59)
        if self.minute is not None and not (0 <= self.minute <= 59):
            raise HL7PrimitiveParseException(
                f"DTM - Invalid minute: {self.minute}. Must be between 0 and 59"
            )

        # Second validation (0-59)
        if self.second is not None and not (0 <= self.second <= 59):
            raise HL7PrimitiveParseException(
                f"DTM - Invalid second: {self.second}. Must be between 0 and 59"
            )

        # Component dependency validation
        self._validate_component_dependencies()

    def _is_leap_year(self):
        """Helper method to determine if the current year is a leap year"""
        if self.year is None:
            return False
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def _validate_component_dependencies(self):
        """Validate that time components are provided in the correct order"""
        if self.month is None and any([self.day, self.hour, self.minute, self.second]):
            raise HL7PrimitiveParseException(
                "DTM - Cannot specify day/time components without month"
            )

        if self.day is None and any([self.hour, self.minute, self.second]):
            raise HL7PrimitiveParseException(
                "DTM - Cannot specify time components without day"
            )

        if self.hour is None and any([self.minute, self.second]):
            raise HL7PrimitiveParseException(
                "DTM - Cannot specify minute/second without hour"
            )

        if self.minute is None and self.second is not None:
            raise HL7PrimitiveParseException(
                "DTM - Cannot specify second without minute"
            )

    @classmethod
    def from_time(cls, t: time, include_timezone: bool = True) -> DTM:
        """Convert a time object to DTM format."""
        dt = datetime.fromtimestamp(t)
        return cls.from_datetime(dt, include_timezone)

    @classmethod
    def from_datetime(cls, dt: datetime, include_timezone: bool = True) -> DTM:
        """Convert a datetime object to DTM format."""
        basic_fmt = dt.strftime("%Y%m%d%H%M%S.%f")[:18]  # Truncate to 4 decimal places

        if include_timezone and dt.tzinfo is not None:
            offset = dt.utcoffset()
            if offset is not None:
                minutes = offset.total_seconds() / 60
                hours = int(minutes / 60)
                mins = int(minutes % 60)
                tz_str = f"{'+' if hours >= 0 else '-'}{abs(hours):02d}{abs(mins):02d}"
                return cls(f"{basic_fmt}{tz_str}")

        return cls(basic_fmt)

    @classmethod
    def now(cls, tz: str | ZoneInfo | None = None) -> DTM:
        """Create a DTM object representing the current time."""
        if isinstance(tz, str):
            tz = ZoneInfo(tz)
        return cls.from_datetime(datetime.now(tz))

    @classmethod
    def from_ymdhms(
        cls,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int = 0,
        microsecond: int = 0,
        tz: ZoneInfo = ZoneInfo("UTC"),
    ) -> DTM:
        """Create a DTM object from individual components."""
        dt = datetime(year, month, day, hour, minute, second, microsecond, tz)
        return cls.from_datetime(dt, include_timezone=False)

    @classmethod
    def from_iso(cls, iso_time: str) -> DTM:
        """Convert an ISO format datetime string to DTM format."""
        dt = datetime.fromisoformat(iso_time)
        return cls.from_datetime(dt)

    def to_time(self) -> time:
        """Convert DTM to Unix timestamp."""
        return datetime.fromisoformat(self.to_iso()).timestamp()

    def to_iso(self) -> str:
        """Convert DTM to ISO format."""
        match = self._DTM_PATTERN.match(self)
        if not match:
            raise ValueError("Invalid DTM format")

        parts = list(match.groups())
        # Pad missing components with defaults
        year, month, day = parts[0], parts[1] or "01", parts[2] or "01"
        hour, minute, second = parts[3] or "00", parts[4] or "00", parts[5] or "00"

        iso_time = f"{year}-{month}-{day}T{hour}:{minute}:{second}"

        if parts[6]:  # Microseconds
            micro = parts[6].ljust(6, "0")[:6]
            iso_time += f".{micro}"

        if all(parts[7:10]):  # Timezone
            sign, tz_hour, tz_minute = parts[7:10]
            iso_time += f"{sign}{tz_hour}:{tz_minute}"

        return iso_time

    @property
    def year(self) -> int:
        """Get the year component."""
        return int(self[:4])

    @property
    def month(self) -> int | None:
        """Get the month component."""
        if len(self) >= 6:
            return int(self[4:6])
        return None

    @property
    def day(self) -> int | None:
        """Get the day component."""
        if len(self) >= 8:
            return int(self[6:8])
        return None

    @property
    def hour(self) -> int | None:
        """Get the hour component."""
        if len(self) >= 10:
            return int(self[8:10])
        return None

    @property
    def minute(self) -> int | None:
        """Get the minute component."""
        if len(self) >= 12:
            return int(self[10:12])
        return None

    @property
    def second(self) -> int | None:
        """Get the second component."""
        if len(self) >= 14:
            return int(self[12:14])
        return None

    @property
    def microsecond(self) -> int | None:
        """Get the microsecond component."""
        match = self._DTM_PATTERN.match(self)
        if match and match.group(7):
            return int(match.group(7).ljust(6, "0")[:6])
        return None

    @property
    def timezone(self) -> tuple[int, int] | None:
        """Get the timezone offset as (hour, minute) tuple if available."""
        match = self._DTM_PATTERN.match(self)
        if match and all(match.groups()[7:10]):
            sign = 1 if match.group(8) == "+" else -1
            return (sign * int(match.group(9)), int(match.group(10)))
        return None
