"""Movie-ticket helpers with defensive input validation."""

import re


def parse_seat(seat):
    """Return (row, number) for a seat such as ``H12``; invalid input returns None."""
    if not isinstance(seat, str):
        return None

    value = seat.strip().upper()
    if not re.fullmatch(r"[A-Z][1-9][0-9]*", value):
        return None

    return value[0], int(value[1:])


def total_price(prices_csv):
    """Return the total including 18% GST; invalid input returns 0.0."""
    if not isinstance(prices_csv, str) or not prices_csv.strip():
        return 0.0

    try:
        parts = [part.strip() for part in prices_csv.split(",")]
        if any(not part or not part.isdigit() for part in parts):
            return 0.0
        prices = [int(part) for part in parts]
    except (TypeError, ValueError, OverflowError):
        return 0.0

    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    """Return the average of space-separated ratings from 0 through 5.

    Invalid, empty, or non-string input returns 0.0 instead of raising.
    """
    if not isinstance(ratings, str) or not ratings.strip():
        return 0.0

    try:
        tokens = ratings.split()
        values = [int(token) for token in tokens]
    except (TypeError, ValueError, OverflowError):
        return 0.0

    if not values or any(value < 0 or value > 5 for value in values):
        return 0.0

    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)


if __name__ == "__main__":
    main()
