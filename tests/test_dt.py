import pytest
from datetime import datetime, date
from src.hl7.v2_5_1.data_types.DT import DT
from src.hl7.base import HL7PrimitiveParseException


class TestDT:
    def test_create_basic(self):
        """Test basic DT creation with valid dates"""
        # Test full date
        dt = DT("20240101")
        assert str(dt) == "20240101"

        # Test year-month
        dt = DT("202401")
        assert str(dt) == "202401"

        # Test year only
        dt = DT("2024")
        assert str(dt) == "2024"

    def test_length_validation(self):
        """Test length validation"""
        # Test invalid length
        with pytest.raises(HL7PrimitiveParseException):
            DT("202401011")  # 9 characters

        # Test empty string
        with pytest.raises(HL7PrimitiveParseException):
            DT("")

    def test_from_datetime(self):
        """Test creation from datetime object"""
        dt_obj = datetime(2024, 1, 1)
        dt = DT.from_datetime(dt_obj)
        assert str(dt) == "20240101"

    def test_from_date(self):
        """Test creation from date object"""
        date_obj = date(2024, 1, 1)
        dt = DT.from_date(date_obj)
        assert str(dt) == "20240101"

    def test_from_ymd(self):
        """Test creation from year, month, day components"""
        # Test full date
        dt = DT.from_ymd(2024, 1, 1)
        assert str(dt) == "20240101"

        # Test year-month
        dt = DT.from_ymd(2024, 1)
        assert str(dt) == "202401"

        # Test year only
        dt = DT.from_ymd(2024)
        assert str(dt) == "2024"

        # Test invalid values
        with pytest.raises(HL7PrimitiveParseException):
            DT.from_ymd(0)  # Invalid year
        with pytest.raises(HL7PrimitiveParseException):
            DT.from_ymd(2024, 13)  # Invalid month
        with pytest.raises(HL7PrimitiveParseException):
            DT.from_ymd(2024, 1, 32)  # Invalid day
        with pytest.raises(HL7PrimitiveParseException):
            DT.from_ymd(2024, None, 1)  # Day without month

    def test_today(self):
        """Test today() method"""
        dt = DT.today()
        today = date.today()
        assert dt == today.strftime("%Y%m%d")

    def test_from_iso(self):
        """Test creation from ISO format"""
        # Test valid ISO format
        dt = DT.from_iso("2024-01-01")
        assert str(dt) == "20240101"

        # Test invalid ISO format
        with pytest.raises(HL7PrimitiveParseException):
            DT.from_iso("invalid")

    def test_to_datetime(self):
        """Test conversion to datetime"""
        # Test full date
        dt = DT("20240101")
        dt_obj = dt.to_datetime()
        assert isinstance(dt_obj, datetime)
        assert dt_obj == datetime(2024, 1, 1)

        # Test year-month
        dt = DT("202401")
        dt_obj = dt.to_datetime()
        assert dt_obj == datetime(2024, 1, 1)

        # Test year only
        dt = DT("2024")
        dt_obj = dt.to_datetime()
        assert dt_obj == datetime(2024, 1, 1)

        # Test invalid format
        with pytest.raises(HL7PrimitiveParseException):
            DT("2024010").to_datetime()  # Invalid length

    def test_to_date(self):
        """Test conversion to date"""
        dt = DT("20240101")
        d = dt.to_date()
        assert isinstance(d, date)
        assert d == date(2024, 1, 1)

    def test_to_iso(self):
        """Test conversion to ISO format"""
        # Test full date
        dt = DT("20240101")
        assert dt.to_iso() == "2024-01-01"

        # Test year-month
        dt = DT("202401")
        assert dt.to_iso() == "2024-01"

        # Test year only
        dt = DT("2024")
        assert dt.to_iso() == "2024"

        # Test invalid format
        with pytest.raises(HL7PrimitiveParseException):
            DT("2024010").to_iso()  # Invalid length

    def test_properties(self):
        """Test year, month, and day properties"""
        # Test full date
        dt = DT("20240101")
        assert dt.year == 2024
        assert dt.month == 1
        assert dt.day == 1

        # Test year-month
        dt = DT("202401")
        assert dt.year == 2024
        assert dt.month == 1
        assert dt.day is None

        # Test year only
        dt = DT("2024")
        assert dt.year == 2024
        assert dt.month is None
        assert dt.day is None

    def test_edge_cases(self):
        """Test edge cases and boundary values"""
        # Test minimum year
        dt = DT.from_ymd(1001)
        assert dt.year == 1001

        # Test maximum year
        dt = DT.from_ymd(2999)
        assert dt.year == 2999

        # Test leap year date
        dt = DT("20240229")  # 2024 is a leap year
        assert dt.day == 29

        # Test various invalid cases
        with pytest.raises(HL7PrimitiveParseException):
            DT.from_ymd(10000)  # Year too large
        with pytest.raises(HL7PrimitiveParseException):
            DT.from_ymd(2024, 0)  # Month too
