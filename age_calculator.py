from datetime import datetime

# Function to calculate days remaining until next birthday
def days_until_next_birthday(birth_month, birth_day, today):
    # Create a date for this year's birthday
    this_year_birthday = datetime(today.year, birth_month, birth_day)

    # Check if birthday already happened
    if this_year_birthday < today:
        # If yes, next birthday is next year
        next_birthday = datetime(today.year + 1, birth_month, birth_day)
    else:
        # If no, next birthday is this year
        next_birthday = this_year_birthday

    # Calculate and return the difference in days
    return (next_birthday - today).days

def main():
    today = datetime.now()

    print("=== AGE CALCULATOR ===")

    current_year = today.year
    current_month = today.month
    current_day = today.day
    
    # Keep asking for input until we get valid data
    while True:
        try:
            birth_year = int(input("What year were you born? "))
            birth_month = int(input("What month were you born (1-12): "))
            birth_day = int(input("What day were you born? (1-31)"))
            
            # Try to create the date
            test_date = datetime(birth_year, birth_month, birth_day)

            # Make sure the birth date isn't in the future
            if test_date > datetime.now():
                print("Birth date can't be in ther future!")
                continue  # Ask again

            break  # All inputs are valid, exit the loop

        except ValueError:
            # Catches both invalid numbers and invalid dates
            print("That's not a valid number! Please try again.")

    # Calculate basic age
    age = current_year - birth_year

    # Check if today is the birthday
    is_birthday_today = (birth_month, birth_day) == (current_month, current_day)
    # Check if birthday already happened this year
    birthday_has_happened = (birth_month, birth_day) < (current_month, current_day)

    # If birthday hasn't happened yet this year, subtract 1 from age
    if not is_birthday_today and not birthday_has_happened:
        age -= 1

    # Calculate days until next birthday
    days_left = days_until_next_birthday(birth_month, birth_day, today)

    print(f"You're currently {age} years old.")

    # Display different messages based on birthday status
    if is_birthday_today:
        print("🎉 Happy Birthday! 🎉")
    elif birthday_has_happened:
        print("You've already had your birthday this year 🎉")
    else:
        print(f"Your birthday is in {days_left} days 🎂")

if __name__ == "__main__":
    main()