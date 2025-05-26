from datetime import datetime, timedelta
from typing import List, Dict
from calendar import isleap

def parse_birthday(birthday_str: str) -> datetime.date:
    """Parse birthday string into date object."""
    return datetime.strptime(birthday_str, "%Y.%m.%d").date()

def get_birthday_this_year(birthday: datetime.date, today: datetime.date) -> datetime.date:
    """
    Get the birthday date for current year, handling February 29th in non-leap years.
    """
    if birthday.month == 2 and birthday.day == 29 and not isleap(today.year):
        # If it's not a leap year, celebrate on February 28th
        return birthday.replace(day=28, year=today.year)
    return birthday.replace(year=today.year)

def get_birthday_next_year(birthday: datetime.date, today: datetime.date) -> datetime.date:
    """
    Get the birthday date for next year, handling February 29th in non-leap years.
    """
    next_year = today.year + 1
    if birthday.month == 2 and birthday.day == 29:
        if isleap(next_year):
            return birthday.replace(year=next_year)
        return datetime(next_year, 2, 28).date()
    return birthday.replace(year=next_year)

def adjust_weekend_date(date: datetime.date) -> datetime.date:
    """
    Adjust the date if it falls on a weekend.
    Special handling for February 28th in non-leap years.
    """
    weekday = date.weekday()
    if weekday == 5:  # Saturday
        # Special case for February 28th
        if date.month == 2 and date.day == 28:
            return date + timedelta(days=1)  # Move to March 1st
        return date + timedelta(days=2)
    elif weekday == 6:  # Sunday
        return date + timedelta(days=1)
    return date

def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Returns a list of users whose birthdays are within the next 7 days (including today).
    If a birthday falls on a weekend, the congratulation date is moved to the next Monday.
    Each result contains the user's name and the congratulation date as a string in 'YYYY.MM.DD' format.
    
    Args:
        users: List of dictionaries with keys 'name' (str) and 'birthday' (str, format 'YYYY.MM.DD').
    Returns:
        List of dictionaries with keys 'name' and 'congratulation_date' (str).
    """
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        # Parse the user's birthday
        birthday = parse_birthday(user["birthday"])
        
        # Skip users with future birth dates (not yet born)
        if birthday > today:
            continue
        
        # Get birthday date this year
        birthday_this_year = get_birthday_this_year(birthday, today)
        
        # If the birthday has already passed this year, use next year
        if birthday_this_year < today:
            birthday_this_year = get_birthday_next_year(birthday, today)
        
        # Check if birthday is within next 7 days
        days_diff = (birthday_this_year - today).days
        if days_diff <= 7:
            # Adjust for weekends
            congratulation_date = adjust_weekend_date(birthday_this_year)
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays
