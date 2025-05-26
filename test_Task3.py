import unittest
from Task3 import normalize_phone

class TestNormalizePhone(unittest.TestCase):
    def test_valid_ukrainian_formats(self):
        """Test normalization of various valid Ukrainian phone number formats."""
        self.assertEqual(normalize_phone("067\t123 4567"), "+380671234567")
        self.assertEqual(normalize_phone("(095) 234-5678\n"), "+380952345678")
        self.assertEqual(normalize_phone("+380 44 123 4567"), "+380441234567")
        self.assertEqual(normalize_phone("380501234567"), "+380501234567")
        self.assertEqual(normalize_phone("    +38(050)123-32-34"), "+380501233234")
        self.assertEqual(normalize_phone("     0503451234"), "+380503451234")
        self.assertEqual(normalize_phone("(050)8889900"), "+380508889900")
        self.assertEqual(normalize_phone("38050-111-22-22"), "+380501112222")
        self.assertEqual(normalize_phone("38050 111 22 11   "), "+380501112211")

    def test_plus_not_at_start(self):
        """Test numbers where plus sign is not at the start."""
        self.assertEqual(normalize_phone("38+0501234567"), "+380501234567")
        self.assertEqual(normalize_phone("050+3451234"), "+380503451234")
        self.assertEqual(normalize_phone("(0+50)8889900"), "+380508889900")

    def test_too_short(self):
        """Test numbers that are too short to be valid."""
        self.assertEqual(normalize_phone("12345"), "")
        self.assertEqual(normalize_phone("+38012"), "")

    def test_too_long(self):
        """Test numbers that are too long to be valid."""
        self.assertEqual(normalize_phone("+380501234567890"), "")
        self.assertEqual(normalize_phone("380501234567890"), "")

    def test_with_letters(self):
        """Test numbers containing letters mixed with digits."""
        self.assertEqual(normalize_phone("050abc3451234"), "+380503451234")
        self.assertEqual(normalize_phone("abc+380501234567"), "+380501234567")

    def test_only_plus_or_empty(self):
        """Test input that is only a plus sign or empty string."""
        self.assertEqual(normalize_phone("+"), "")
        self.assertEqual(normalize_phone(""), "")

    def test_edge_cases(self):
        """Test edge cases: exactly 9, 10, 12, 13 digits and mixed symbols."""
        self.assertEqual(normalize_phone("501234567"), "+380501234567")  # 9 digits
        self.assertEqual(normalize_phone("0501234567"), "+380501234567")  # 10 digits
        self.assertEqual(normalize_phone("380501234567"), "+380501234567")  # 12 digits
        self.assertEqual(normalize_phone("+380501234567"), "+380501234567")  # 13 with plus
        self.assertEqual(normalize_phone("+38(050)123-32-34"), "+380501233234")
        self.assertEqual(normalize_phone("  (+33) 32234234"), "+3332234234")  # non-Ukrainian, but plus at start

    def test_example_from_task(self):
        """Test the example list of numbers from the task description."""
        raw_numbers = [
            "067\t123 4567",
            "(095) 234-5678\n",
            "+380 44 123 4567",
            "380501234567",
            "    +38(050)123-32-34",
            "     0503451234",
            "(050)8889900",
            "38050-111-22-22",
            "38050 111 22 11   ",
        ]
        expected = [
            '+380671234567',
            '+380952345678',
            '+380441234567',
            '+380501234567',
            '+380501233234',
            '+380503451234',
            '+380508889900',
            '+380501112222',
            '+380501112211',
        ]
        result = [normalize_phone(num) for num in raw_numbers]
        self.assertEqual(result, expected)

    def test_additional_cases(self):
        """Test additional international and edge cases, including 00 prefix, double plus, and numbers with spaces."""
        # International number with plus (should not change)
        self.assertEqual(normalize_phone("+441234567890"), "+441234567890")
        self.assertEqual(normalize_phone("+1234567890"), "+1234567890")
        # 10 digits, does not start with 0 (should add +38)
        self.assertEqual(normalize_phone("1234567890"), "+381234567890")
        # Russian number with plus and extra symbols (should not change)
        self.assertEqual(normalize_phone("  +7 (495) 123-45-67"), "+74951234567")
        # 9 digits, does not start with 0 (should add +38)
        self.assertEqual(normalize_phone("501234567"), "+380501234567")
        # International code with 00 (should convert to +)
        self.assertEqual(normalize_phone("00380501234567"), "+380501234567")
        # Double plus (should become +380501234567)
        self.assertEqual(normalize_phone("++380501234567"), "+380501234567")
        # Digits separated by spaces, starts with 0 (should become +380501234567)
        self.assertEqual(normalize_phone("0 5 0 1 2 3 4 5 6 7"), "+380501234567")

if __name__ == "__main__":
    unittest.main() 