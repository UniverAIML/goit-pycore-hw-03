import unittest
from datetime import datetime
from unittest.mock import patch
from Task4 import get_upcoming_birthdays

class TestGetUpcomingBirthdays(unittest.TestCase):
    """
    Test suite for the get_upcoming_birthdays function.
    
    This test suite verifies the functionality of birthday congratulation date calculation.
    It uses a fixed test date (2024-01-22, Monday) to ensure consistent test results.
    
    Key test scenarios include:
    - Regular weekday birthdays
    - Weekend birthdays (moving to Monday)
    - Edge cases (today, 7 days ahead)
    - Out of range cases (past dates, future dates beyond 7 days)
    """

    @patch('Task4.datetime')
    def setUp(self, mock_datetime):
        """
        Test setup method that runs before each test.
        Sets up a fixed date (2024-01-22, Monday) and test user data.
        
        The test data includes various scenarios:
        - Birthdays on different weekdays
        - Weekend birthdays
        - Past and future birthdays
        - Edge cases
        """
        self.test_date = datetime(2024, 1, 22)  # Monday
        mock_datetime.today.return_value = self.test_date
        mock_datetime.strptime = datetime.strptime
        self.users = [
            {"name": "John Doe", "birthday": "1985.01.23"},      # Tuesday
            {"name": "Jane Smith", "birthday": "1990.01.27"},    # Saturday -> Monday
            {"name": "Bob Wilson", "birthday": "1988.01.28"},    # Sunday -> Monday
            {"name": "Alice Brown", "birthday": "1992.01.29"},   # Monday next week
            {"name": "Charlie Davis", "birthday": "1987.01.30"}, # Out of 7 days
            {"name": "Eve Johnson", "birthday": "1995.01.21"},   # Yesterday (past)
            {"name": "Frank Miller", "birthday": "1991.01.22"},  # Today
        ]

    @patch('Task4.datetime')
    def test_upcoming_birthdays_regular(self, mock_datetime):
        """
        Tests the main functionality with multiple users having different birthday scenarios.
        
        Verifies that:
        1. Today's birthday is included
        2. Next day's birthday is included
        3. Weekend birthdays are moved to Monday
        4. Multiple birthdays can be scheduled for the same day
        5. The order of results doesn't matter (sorted before comparison)
        """
        mock_datetime.today.return_value = self.test_date
        mock_datetime.strptime = datetime.strptime
        result = get_upcoming_birthdays(self.users)
        expected = [
            {"name": "Frank Miller", "congratulation_date": "2024.01.22"},
            {"name": "John Doe", "congratulation_date": "2024.01.23"},
            {"name": "Jane Smith", "congratulation_date": "2024.01.29"},
            {"name": "Bob Wilson", "congratulation_date": "2024.01.29"},
            {"name": "Alice Brown", "congratulation_date": "2024.01.29"},
        ]
        # Sort both lists by name to ensure consistent order
        result.sort(key=lambda x: x["name"])
        expected.sort(key=lambda x: x["name"])
        self.assertEqual(result, expected)

    @patch('Task4.datetime')
    def test_birthday_on_today(self, mock_datetime):
        """
        Tests the edge case when birthday is today.
        
        Verifies that:
        1. Today's birthday is included in the results
        2. The congratulation date matches today's date
        3. The function correctly handles the case where days_diff = 0
        """
        mock_datetime.today.return_value = self.test_date
        mock_datetime.strptime = datetime.strptime
        users = [{"name": "Today User", "birthday": "2000.01.22"}]
        result = get_upcoming_birthdays(users)
        self.assertEqual(result, [{"name": "Today User", "congratulation_date": "2024.01.22"}])

    @patch('Task4.datetime')
    def test_birthday_on_seventh_day(self, mock_datetime):
        """
        Tests the edge case when birthday is exactly 7 days ahead.
        
        Verifies that:
        1. A birthday 7 days ahead is included
        2. The date calculation is inclusive of the 7th day
        3. The congratulation date is correctly formatted
        """
        mock_datetime.today.return_value = self.test_date
        mock_datetime.strptime = datetime.strptime
        users = [{"name": "Seventh Day", "birthday": "1990.01.29"}]
        result = get_upcoming_birthdays(users)
        self.assertEqual(result, [{"name": "Seventh Day", "congratulation_date": "2024.01.29"}])

    @patch('Task4.datetime')
    def test_birthday_out_of_range(self, mock_datetime):
        """
        Tests that birthdays more than 7 days ahead are not included.
        
        Verifies that:
        1. Birthdays beyond the 7-day window are excluded
        2. The function returns an empty list for out-of-range dates
        3. The boundary condition is correctly handled
        """
        mock_datetime.today.return_value = self.test_date
        mock_datetime.strptime = datetime.strptime
        users = [{"name": "Out of Range", "birthday": "1980.01.30"}]
        result = get_upcoming_birthdays(users)
        self.assertEqual(result, [])

    @patch('Task4.datetime')
    def test_birthday_in_past(self, mock_datetime):
        """
        Tests that past birthdays are not included in the current year.
        
        Verifies that:
        1. Yesterday's birthday is not included
        2. The function correctly handles past dates
        3. The function returns an empty list for past dates
        """
        mock_datetime.today.return_value = self.test_date
        mock_datetime.strptime = datetime.strptime
        users = [{"name": "Past User", "birthday": "1995.01.21"}]
        result = get_upcoming_birthdays(users)
        self.assertEqual(result, [])

    @patch('Task4.datetime')
    def test_birthday_on_weekend(self, mock_datetime):
        """
        Tests the weekend birthday handling logic.
        
        Verifies that:
        1. Saturday birthdays are moved to next Monday
        2. Sunday birthdays are moved to next Monday
        3. Multiple weekend birthdays can be moved to the same Monday
        4. The congratulation dates are correctly adjusted
        """
        mock_datetime.today.return_value = self.test_date
        mock_datetime.strptime = datetime.strptime
        users = [
            {"name": "Saturday User", "birthday": "1990.01.27"}, # Saturday
            {"name": "Sunday User", "birthday": "1990.01.28"},   # Sunday
        ]
        result = get_upcoming_birthdays(users)
        expected = [
            {"name": "Saturday User", "congratulation_date": "2024.01.29"},
            {"name": "Sunday User", "congratulation_date": "2024.01.29"},
        ]
        self.assertEqual(result, expected)

    @patch('Task4.datetime')
    def test_leap_year_birthday(self, mock_datetime):
        """
        Tests birthday handling for February 29th (leap year).
        
        Verifies that:
        1. In a leap year, February 29th birthday is celebrated on February 29th
        2. In a non-leap year, February 29th birthday is celebrated on February 28th
        3. Correctly handles the transition between leap and non-leap years
        """
        # Test in leap year (2024)
        test_date_leap = datetime(2024, 2, 25)  # Few days before Feb 29
        mock_datetime.today.return_value = test_date_leap
        mock_datetime.strptime = datetime.strptime
        
        users = [{"name": "Leap Day User", "birthday": "1996.02.29"}]
        result = get_upcoming_birthdays(users)
        self.assertEqual(result, [{"name": "Leap Day User", "congratulation_date": "2024.02.29"}])

        # Test in non-leap year (2023)
        test_date_non_leap = datetime(2023, 2, 25)
        mock_datetime.today.return_value = test_date_non_leap
        result = get_upcoming_birthdays(users)
        self.assertEqual(result, [{"name": "Leap Day User", "congratulation_date": "2023.02.28"}])

    @patch('Task4.datetime')
    def test_leap_year_birthday_on_weekend(self, mock_datetime):
        """
        Tests leap year birthday (February 29th) when it falls on a weekend.
        
        Verifies that:
        1. When Feb 29th falls on a weekend in a leap year, it's moved to Monday
        2. When Feb 28th falls on a weekend in a non-leap year, it's moved to Monday
        """
        # 2032 - leap year where Feb 29 falls on Sunday
        test_date_leap = datetime(2032, 2, 25)
        mock_datetime.today.return_value = test_date_leap
        mock_datetime.strptime = datetime.strptime
        
        users = [{"name": "Leap Weekend User", "birthday": "1996.02.29"}]
        result = get_upcoming_birthdays(users)
        self.assertEqual(result, [{"name": "Leap Weekend User", "congratulation_date": "2032.03.01"}])

        # 2026 - non-leap year where Feb 28 falls on Saturday
        test_date_non_leap = datetime(2026, 2, 25)
        mock_datetime.today.return_value = test_date_non_leap
        result = get_upcoming_birthdays(users)
        self.assertEqual(result, [{"name": "Leap Weekend User", "congratulation_date": "2026.03.01"}])

    @patch('Task4.datetime')
    def test_future_birth_date(self, mock_datetime):
        """
        Tests that users with future birth dates are skipped.
        
        Verifies that:
        1. Users with birth dates in the future are not included
        2. The function handles this gracefully without errors
        3. Only valid (past) birth dates are processed
        """
        mock_datetime.today.return_value = self.test_date
        mock_datetime.strptime = datetime.strptime
        
        users = [
            {"name": "Future User", "birthday": "2025.01.23"},    # Future date
            {"name": "Valid User", "birthday": "1990.01.23"},    # Valid past date
            {"name": "Another Future", "birthday": "2030.12.25"} # Another future date
        ]
        result = get_upcoming_birthdays(users)
        # Only the valid user should be included
        self.assertEqual(result, [{"name": "Valid User", "congratulation_date": "2024.01.23"}])

if __name__ == "__main__":
    unittest.main() 