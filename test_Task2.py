import unittest
from Task2 import get_numbers_ticket

class TestGetNumbersTicket(unittest.TestCase):
    def test_normal_case(self):
        # Normal case: range 1-6, quantity 6
        result = get_numbers_ticket(1, 6, 6)
        self.assertEqual(len(result), 6)
        self.assertEqual(sorted(result), result)
        self.assertTrue(all(1 <= x <= 6 for x in result))
        self.assertEqual(len(set(result)), 6)

    def test_quantity_too_large(self):
        # quantity is greater than the number of values in the range — should return []
        self.assertEqual(get_numbers_ticket(1, 5, 10), [])

    def test_min_greater_than_max(self):
        # min is greater than max — should return []
        self.assertEqual(get_numbers_ticket(10, 5, 3), [])

    def test_quantity_less_than_1(self):
        # quantity is less than 1 — should return []
        self.assertEqual(get_numbers_ticket(1, 10, 0), [])

    def test_max_greater_than_1000(self):
        # max is greater than 1000 — should return []
        self.assertEqual(get_numbers_ticket(1, 1001, 5), [])

    def test_min_less_than_1(self):
        # min is less than 1 — should return []
        self.assertEqual(get_numbers_ticket(0, 10, 5), [])
        self.assertEqual(get_numbers_ticket(-5, 10, 3), [])

    def test_single_number(self):
        # min = max, quantity = 1 — should return a list with that number
        self.assertEqual(get_numbers_ticket(5, 5, 1), [5])

    def test_single_number_full_range(self):
        # quantity equals the size of the range — should return all numbers in the range
        self.assertEqual(get_numbers_ticket(1, 6, 6), [1, 2, 3, 4, 5, 6])

    def test_min_equals_max_quantity_more_than_one(self):
        # min = max, quantity > 1 — impossible to choose, should return []
        self.assertEqual(get_numbers_ticket(5, 5, 2), [])

    def test_min_equals_max_quantity_zero(self):
        # min = max, quantity = 0 — should return []
        self.assertEqual(get_numbers_ticket(5, 5, 0), [])

    def test_large_positive_range(self):
        # Large range of positive numbers
        result = get_numbers_ticket(900, 1000, 5)
        self.assertEqual(len(result), 5)
        self.assertTrue(all(900 <= x <= 1000 for x in result))
        self.assertEqual(len(set(result)), 5)

    def test_quantity_one(self):
        # quantity = 1, range has more than one number
        result = get_numbers_ticket(1, 10, 1)
        self.assertEqual(len(result), 1)
        self.assertTrue(1 <= result[0] <= 10)

    def test_zero_zero_one(self):
        # min = max = 0, quantity = 1 — should return [] (min < 1)
        self.assertEqual(get_numbers_ticket(0, 0, 1), [])

    def test_zero_zero_zero(self):
        # min = max = 0, quantity = 0 — should return [] (min < 1)
        self.assertEqual(get_numbers_ticket(0, 0, 0), [])

    def test_full_range_quantity(self):
        # quantity equals the size of the range (1-1000) — should return all numbers
        result = get_numbers_ticket(1, 1000, 1000)
        self.assertEqual(len(result), 1000)
        self.assertEqual(result, list(range(1, 1001)))

    def test_quantity_more_than_range(self):
        # quantity is greater than the number of values in the range (1-1000) — should return []
        self.assertEqual(get_numbers_ticket(1, 1000, 1001), [])

if __name__ == '__main__':
    unittest.main() 