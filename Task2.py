import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Generate a sorted list of unique random numbers within a given range for a lottery ticket.

    Args:
        min (int): The minimum value in the range (inclusive). Must be >= 1.
        max (int): The maximum value in the range (inclusive). Must be <= 1000 and >= min.
        quantity (int): The number of unique random numbers to generate. Must be >= 1 and <= (max - min + 1).

    Returns:
        list[int]: A sorted list of unique random numbers in the range [min, max].
                   Returns an empty list if any of the following conditions are met:
                       - quantity > (max - min + 1)
                       - min > max
                       - min < 1
                       - quantity < 1
                       - max > 1000
    """
    if quantity > max - min + 1:
        return []
    elif min > max:
        return []
    elif min < 1:
        return []
    elif max > 1000:
        return []
    
    nums = random.sample(range(min, max + 1), quantity)
    return sorted(nums)

print(get_numbers_ticket(1, 6, 6))
