from datetime import datetime

# This function calculates the number of days between the given date and today
# The input date should be in the format 'YYYY-MM-DD'
def get_days_from_today(date:str) -> int | str:
    """
    Calculate the number of days between the given date and today.

    Args:
        date (str): Date string in the format 'YYYY-MM-DD'.

    Returns:
        int: Number of days from the given date to today.
             Negative if the date is in the future.
        str: "Invalid date format" if the input is not a valid date string.

    Examples:
        >>> get_days_from_today("2021-10-09")
        -157  # if today is 2021-05-05

        >>> get_days_from_today("not-a-date")
        'Invalid date format'
    """
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.now().date()
        return (today - date).days
    except  (ValueError, TypeError):
        # Return an error message if the date format is invalid
        return "Invalid date format"
