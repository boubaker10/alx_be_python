from datetime import datetime, timedelta


def display_current_datetime():
    # get current date & time
    current_date = datetime.now()
    # formatted output
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date(days):
    # current date
    current = datetime.now()
    # future date calculation
    future_date = current + timedelta(days=days)
    # formatted output
    print("Future date:", future_date.strftime("%Y-%m-%d"))


def main():
    display_current_datetime()

    try:
        days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return
    
    calculate_future_date(days)


if __name__ == "__main__":
    main()
