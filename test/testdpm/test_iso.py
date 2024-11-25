import unittest
from datetime import UTC, datetime

import pytz

from src.dpm.models.user import User


class TestGetIsoMethod(unittest.TestCase):
    def test_naive_datetime(self):
        """Check that naive datetime is correctly converted to ISO string in UTC"""
        naive_dt = datetime(2024, 11, 25, 12, 0, 0)
        expected_result = "2024-11-25T12:00:00"
        result = User.get_iso(naive_dt)
        self.assertEqual(result, expected_result)

    def test_aware_datetime(self):
        """Check that aware datetime is correctly converted to ISO string in UTC"""
        # UTC
        aware_dt = datetime(2024, 11, 25, 12, 0, 0, tzinfo=UTC)
        expected_result = "2024-11-25T12:00:00"
        result = User.get_iso(aware_dt)
        self.assertEqual(result, expected_result)
        # IST
        tz = pytz.timezone("America/New_York")
        aware_dt = tz.localize(datetime(2024, 11, 25, 12, 0, 0))
        result = User.get_iso(aware_dt)
        expected_result = "2024-11-25T17:00:00"
        self.assertEqual(result, expected_result)
