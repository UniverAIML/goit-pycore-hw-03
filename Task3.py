import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalize a phone number to the standard international format for SMS sending.

    The function removes all characters except digits and the plus sign at the start.
    If the number does not contain a country code, '+38' (for Ukraine) is added automatically.
    Handles numbers with various symbols, spaces, and international prefixes (00 or +).

    Args:
        phone_number (str): The input phone number in any format.

    Returns:
        str: The normalized phone number in the format '+380XXXXXXXXX' or similar,
             or an empty string if the number is invalid (too short/long).
    """
    # Check if there is a valid plus sign (not part of a digit sequence)
    has_valid_plus = bool(re.search(r'(^|[^\d+])\+', phone_number))
    # Extract all digit sequences from the input
    nums = re.findall(r"\d+", phone_number)
    ints = ''.join(nums)

    # Handle international prefix '00' (replace with '+')
    if ints.startswith("00"):
        return "+" + ints[2:]

    # If the number is too short or too long, return empty string
    if len(ints) < 9:
        return ''
    elif len(ints) > 12:
        return ''

    # If there was a valid plus sign, return '+' and the digits
    if has_valid_plus:
        return '+' + ints

    code = '+380'
    return code[:(13 - len(ints))] + ints