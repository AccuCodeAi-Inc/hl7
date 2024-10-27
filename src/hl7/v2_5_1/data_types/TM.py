from __future__ import annotations
from ...base import HL7Primitive, HL7PrimitiveParseException

from datetime import datetime, time
from zoneinfo import ZoneInfo
import re


"""
HL7 Version: 2.5.1
DataType - TM
"""


class TM(str, HL7Primitive):
    """
        TM - Time (len: 16)
        ---
        Specifies the hour of the day with optional minutes, seconds, fraction of second using a 24-hour clock notation and time zone.

    Format: HH[MM[SS[.S[S[S[S]]]]]][+/-ZZZZ]
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TM
    """

    _hl7_version = """2.5.1"""
    _hl7_type = "PRIMITIVE_DATA_TYPE"
    _hl7_length = 16
    _hl7_id = """TM"""
    _hl7_name = """Time"""
    _hl7_description = """Specifies the hour of the day with optional minutes, seconds, fraction of second using a 24-hour clock notation and time zone"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TM"

    # Regex pattern for validating TM format
    __pattern = re.compile(
        r"^(?P<hour>[0-1][0-9]|2[0-3])"
        r"(?:(?P<minute>[0-5][0-9])"
        r"(?:(?P<second>[0-5][0-9])"
        r"(?:\.(?P<fraction>[0-9]{1,4}))?)?)?"
        r"(?P<timezone>[+-][0-2][0-9][0-5][0-9])?$"
    )

    def __new__(cls, tm: str):
        if len(tm) > 16:
            raise HL7PrimitiveParseException(
                "TM content exceeds maximum length of 16 characters"
            )
        if not cls.__pattern.match(tm):
            raise HL7PrimitiveParseException("Invalid TM format")
        return super().__new__(cls, tm)

    @classmethod
    def from_time(cls, t: time, include_timezone: bool = True) -> TM:
        """Create a TM instance from a time object."""
        basic = t.strftime("%H%M%S")
        if t.microsecond:
            # Convert microseconds to 4 decimal places
            fraction = f".{t.microsecond:06d}"[:5]
            basic += fraction

        if include_timezone and t.tzinfo:
            offset = t.tzinfo.utcoffset(None)
            if offset is not None:
                minutes = offset.total_seconds() / 60
                sign = "+" if minutes >= 0 else "-"
                hours, mins = divmod(abs(int(minutes)), 60)
                basic += f"{sign}{hours:02d}{mins:02d}"

        return cls(basic)

    @classmethod
    def from_datetime(cls, dt: datetime, include_timezone: bool = True) -> TM:
        """Create a TM instance from a datetime object."""
        return cls.from_time(dt.timetz(), include_timezone)

    @classmethod
    def now(cls, tz: str | ZoneInfo | None = None) -> TM:
        """Create a TM instance for current time."""
        if isinstance(tz, str):
            tz = ZoneInfo(tz)
        return cls.from_datetime(datetime.now(tz))

    @classmethod
    def from_hhmmss(
        cls,
        hour: int,
        minute: int | None = None,
        second: int | None = None,
        *,
        microsecond: int | None = None,
        timezone_offset: tuple[int, int] | None = None,
    ) -> TM:
        """
        Create a TM instance from time components.
        timezone_offset should be a tuple of (hours, minutes) representing UTC offset
        """
        if not 0 <= hour <= 23:
            raise HL7PrimitiveParseException("Hour must be between 0 and 23")

        result = f"{hour:02d}"

        if minute is not None:
            if not 0 <= minute <= 59:
                raise HL7PrimitiveParseException("Minute must be between 0 and 59")
            result += f"{minute:02d}"

            if second is not None:
                if not 0 <= second <= 59:
                    raise HL7PrimitiveParseException("Second must be between 0 and 59")
                result += f"{second:02d}"

                if microsecond is not None:
                    if not 0 <= microsecond <= 999999:
                        raise HL7PrimitiveParseException(
                            "Microsecond must be between 0 and 999999"
                        )
                    result += f".{microsecond:06d}"[:5]  # Truncate to 4 decimal places

        if timezone_offset is not None:
            tz_hour, tz_minute = timezone_offset
            if not -23 <= tz_hour <= 23 or not 0 <= tz_minute <= 59:
                raise HL7PrimitiveParseException("Invalid timezone offset")
            sign = "+" if tz_hour >= 0 else "-"
            result += f"{sign}{abs(tz_hour):02d}{tz_minute:02d}"

        return cls(result)

    @classmethod
    def from_iso(cls, iso_time: str) -> TM:
        """Create a TM instance from an ISO format time string (HH:MM:SS.mmm±HHMM)."""
        for fmt in ["%H:%M:%S.%f%z", "%H:%M:%S%z", "%H:%M:%S.%f", "%H:%M:%S"]:
            try:
                t = datetime.strptime(iso_time, "%H:%M:%S.%f%z").time()
                return cls.from_time(t)
            except ValueError:
                pass
        return HL7PrimitiveParseException("Invalid ISO format time")

    def to_time(self) -> time:
        """Convert to time object."""
        match = self._pattern.match(self)
        if not match:
            raise HL7PrimitiveParseException("Invalid TM format")

        parts = match.groupdict()
        hour = int(parts["hour"])
        minute = int(parts["minute"]) if parts["minute"] else 0
        second = int(parts["second"]) if parts["second"] else 0
        microsecond = int(parts["fraction"].ljust(6, "0")) if parts["fraction"] else 0

        timezone = None
        if parts["timezone"]:
            sign = 1 if parts["timezone"][0] == "+" else -1
            tz_hour = int(parts["timezone"][1:3])
            tz_minute = int(parts["timezone"][3:5])
            timezone = ZoneInfo(f"Etc/GMT{'-' if sign > 0 else '+'}{tz_hour}")

        return time(hour, minute, second, microsecond, timezone)

    def to_iso(self) -> str:
        """Convert to ISO format (HH:MM:SS.mmm±HHMM)."""
        return self.to_time().isoformat()

    @property
    def hour(self) -> int:
        """Get the hour component."""
        return int(self[:2])

    @property
    def minute(self) -> int | None:
        """Get the minute component if available."""
        return int(self[2:4]) if len(self) >= 4 else None

    @property
    def second(self) -> int | None:
        """Get the second component if available."""
        return int(self[4:6]) if len(self) >= 6 else None

    @property
    def fraction(self) -> str | None:
        """Get the fractional seconds if available."""
        match = self._pattern.match(self)
        return match.group("fraction") if match and match.group("fraction") else None

    @property
    def timezone(self) -> tuple[int, int] | None:
        """Get the timezone offset as (hour, minute) tuple if available."""
        match = self._pattern.match(self)
        if match and match.group("timezone"):
            tz = match.group("timezone")
            sign = 1 if tz[0] == "+" else -1
            return (sign * int(tz[1:3]), int(tz[3:5]))
        return None
