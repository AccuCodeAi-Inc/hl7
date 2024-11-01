import pytest
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from src.hl7.v2_5_1.data_types.DTM import DTM
from src.hl7.base import HL7PrimitiveParseException

class TestDTM:
    def test_valid_dtm_creation(self):
        """Test creation of DTM objects with valid formats."""
        valid_dtms = [
            "2024",  # Year only
            "202401",  # Year and month
            "20240101",  # Date only
            "2024010112",  # Date and hour
            "202401011234",  # Date and time without seconds
            "20240101123456",  # Full date/time
            "20240101123456.1",  # With fractional second
            "20240101123456.123",  # With milliseconds
            "20240101123456.1234",  # With four decimal places
            "20240101123456+0500",  # With timezone
            "20240101123456-0500",  # With negative timezone
            "20240101123456.1234+0500",  # Full format
        ]

        for dtm_str in valid_dtms:
            print(dtm_str)
            dtm = DTM(dtm_str)
            assert str(dtm) == dtm_str

    def test_invalid_dtm_creation(self):
        """Test that invalid DTM formats raise appropriate exceptions."""
        invalid_dtms = [
            "",  # Empty string
            "202",  # Incomplete year
            "20241301",  # Invalid month
            "20240132",  # Invalid day
            "20240101125960",  # Invalid seconds
            "20240101123456.12345",  # Too many decimal places
            "abcd",  # Non-numeric
            "2024/01/01",  # Wrong format
            "2024-01-01T12:34:56",  # ISO format (invalid for DTM)
            "20240101123456++0500",  # Invalid timezone format
            "20240101123456.A234",  # Invalid decimal
            "20240101123456+0500+0200",  # Multiple timezones
        ]

        for invalid_dtm in invalid_dtms:
            print(invalid_dtm)
            with pytest.raises(HL7PrimitiveParseException):
                DTM(invalid_dtm)

    def test_length_validation(self):
        """Test that DTM objects cannot exceed 24 characters."""
        with pytest.raises(HL7PrimitiveParseException):
            DTM("20240101123456.12345+0500")  # 25 characters

    def test_from_datetime(self):
        """Test creation of DTM objects from datetime objects."""
        # Test UTC datetime
        dt = datetime(2024, 1, 1, 12, 34, 56, 123000, tzinfo=timezone.utc)
        dtm = DTM.from_datetime(dt)
        assert str(dtm) == "20240101123456.123+0000"

        # Test datetime with positive timezone
        tz = timezone(timedelta(hours=5, minutes=30))
        dt = datetime(2024, 1, 1, 12, 34, 56, tzinfo=tz)
        dtm = DTM.from_datetime(dt)
        assert str(dtm) == "20240101123456.000+0530"

        # Test datetime with negative timezone
        tz = timezone(timedelta(hours=-8))
        dt = datetime(2024, 1, 1, 12, 34, 56, tzinfo=tz)
        dtm = DTM.from_datetime(dt)
        assert str(dtm) == "20240101123456.000-0800"

        # Test datetime without timezone
        dt = datetime(2024, 1, 1, 12, 34, 56)
        dtm = DTM.from_datetime(dt, include_timezone=False)
        assert str(dtm) == "20240101123456.000"

    def test_from_time(self):
        """Test creation of DTM objects from time timestamps."""
        # Create a specific timestamp
        dt = datetime(2024, 1, 1, 12, 34, 56, tzinfo=timezone.utc)
        timestamp = dt.timestamp()

        dtm = DTM.from_time(timestamp)
        # Note: exact string comparison might fail due to system timezone
        # Instead, verify the conversion back matches
        assert abs(dtm.to_time() - timestamp) < 1  # Within 1 second

    def test_now(self):
        """Test creation of DTM objects representing current time."""
        # Test with UTC
        dtm = DTM.now(ZoneInfo("UTC"))
        now = datetime.now(timezone.utc)
        dtm_time = datetime.fromisoformat(dtm.to_iso())
        assert abs((now - dtm_time).total_seconds()) < 2  # Within 2 seconds

        # Test with specific timezone
        tz = "America/New_York"
        dtm = DTM.now(tz)
        now = datetime.now(ZoneInfo(tz))
        dtm_time = datetime.fromisoformat(dtm.to_iso())
        assert abs((now - dtm_time).total_seconds()) < 2  # Within 2 seconds

    def test_from_ymdhms(self):
        """Test creation of DTM objects from individual components."""
        dtm = DTM.from_ymdhms(2024, 1, 1, 12, 34, 56)
        assert str(dtm) == "20240101123456.000"

    def test_from_iso(self):
        """Test creation of DTM objects from ISO format strings."""
        iso_times = [
            "2024-01-01T12:34:56",
            "2024-01-01T12:34:56+05:00",
            "2024-01-01T12:34:56-08:00",
            "2024-01-01T12:34:56.123+05:00",
        ]

        for iso_time in iso_times:
            dtm = DTM.from_iso(iso_time)
            # Convert back to ISO and compare normalized datetime objects
            assert (datetime.fromisoformat(iso_time) -
                    datetime.fromisoformat(dtm.to_iso())).total_seconds() == 0

    def test_to_iso(self):
        """Test conversion of DTM objects to ISO format."""
        test_cases = [
            ("20240101123456+0500", "2024-01-01T12:34:56+05:00"),
            ("20240101123456.123-0800", "2024-01-01T12:34:56.123000-08:00"),
            ("2024", "2024-01-01T00:00:00"),
            ("202401", "2024-01-01T00:00:00"),
            ("20240101", "2024-01-01T00:00:00"),
            ("2024010112", "2024-01-01T12:00:00"),
            ("202401011234", "2024-01-01T12:34:00"),
        ]

        for dtm_str, expected_iso in test_cases:
            dtm = DTM(dtm_str)
            assert dtm.to_iso() == expected_iso

    def test_component_properties(self):
        """Test the component properties (year, month, day, etc.)."""
        dtm = DTM("20240101123456.123+0500")

        assert dtm.year == 2024
        assert dtm.month == 1
        assert dtm.day == 1
        assert dtm.hour == 12
        assert dtm.minute == 34
        assert dtm.second == 56
        assert dtm.microsecond == 123000
        assert dtm.timezone == (5, 0)

        # Test partial DTM
        dtm = DTM("2024")
        assert dtm.year == 2024
        assert dtm.month is None  # Default
        assert dtm.day is None  # Default
        assert dtm.hour is None
        assert dtm.minute is None
        assert dtm.second is None
        assert dtm.microsecond is None
        assert dtm.timezone is None  # Default

    def test_timezone_property(self):
        """Test timezone property with various formats."""
        test_cases = [
            ("20240101123456+0500", (5, 0)),
            ("20240101123456-0800", (-8, 0)),
            ("20240101123456+0530", (5, 30)),
            ("20240101123456-0245", (-2, 45)),
            ("20240101123456", None),
            ("2024", None),
        ]

        for dtm_str, expected_tz in test_cases:
            dtm = DTM(dtm_str)
            assert dtm.timezone == expected_tz

    def test_to_time(self):
        """Test conversion to Unix timestamp."""
        # Test with timezone
        dtm = DTM("20240101123456+0000")
        expected_dt = datetime(2024, 1, 1, 12, 34, 56, tzinfo=timezone.utc)
        assert abs(dtm.to_time() - expected_dt.timestamp()) < 1

        # Test without timezone
        dtm = DTM("20240101123456")
        expected_dt = datetime(2024, 1, 1, 12, 34, 56)
        assert abs(dtm.to_time() - expected_dt.timestamp()) < 1