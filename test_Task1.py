import unittest
from Task1 import get_days_from_today
from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

class TestGetDaysFromToday(unittest.TestCase):
    def test_future_date(self):
        self.assertTrue(get_days_from_today("2999-01-01") < 0)

    def test_today(self):
        today_str = datetime.now().strftime("%Y-%m-%d")
        self.assertEqual(get_days_from_today(today_str), 0)

    def test_past_date(self):
        self.assertTrue(get_days_from_today("2000-01-01") > 0)

    def test_invalid_format(self):
        self.assertEqual(get_days_from_today("01-01-2020"), "Invalid date format")

    def test_nonexistent_date(self):
        self.assertEqual(get_days_from_today("2023-02-30"), "Invalid date format")

    def test_plain_number(self):
        self.assertEqual(get_days_from_today(12345), "Invalid date format")

    def test_empty_string(self):
        self.assertEqual(get_days_from_today(""), "Invalid date format")

    def test_none(self):
        self.assertEqual(get_days_from_today(None), "Invalid date format")

    def test_very_old_date(self):
        self.assertTrue(get_days_from_today("1800-01-01") > 0)

    def test_string_with_spaces(self):
        self.assertEqual(get_days_from_today(" 2020-01-01 "), "Invalid date format")

    def test_wrong_separator(self):
        self.assertEqual(get_days_from_today("2020/01/01"), "Invalid date format")

class TestTask1(TestCase):
    def test_specific_date_difference(self):
        fixed_date = datetime(2021, 5, 5)
        with patch('Task1.datetime') as mock_datetime:
            mock_datetime.now.return_value = fixed_date
            mock_datetime.strptime.side_effect = lambda *args, **kwargs: datetime.strptime(*args, **kwargs)
            from Task1 import get_days_from_today
            self.assertEqual(get_days_from_today("2021-10-09"), -157)

if __name__ == '__main__':
    unittest.main() 