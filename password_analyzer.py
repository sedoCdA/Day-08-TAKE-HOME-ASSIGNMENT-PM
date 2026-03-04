"""
Password Strength Analyzer & Generator.

Analyzes password strength using scoring criteria and generates
secure random passwords using Python's string and random modules.
"""

import random
import string


# --- Constants ---
SPECIAL_CHARS = "!@#$%^&*"
STRENGTH_RATINGS = {
    (0, 2): "Weak",
    (3, 4): "Medium",
    (5, 6): "Strong",
    (7, 99): "Very Strong",
}


def get_strength_rating(score):
    """Return a strength label based on the score."""
    for (low, high), rating in STRENGTH_RATINGS.items():
        if low <= score <= high:
            return rating
    return "Unknown"


def analyze_password(password):
    """
    Analyze a password and return a score and list of missing criteria.

    Scoring:
        +1 if length >= 8
        +2 if length >= 12
        +3 if length >= 16
        +1 if contains uppercase letter
        +1 if contains lowercase letter
        +1 if contains digit
        +1 if contains special character
        +1 if no character repeats more than 2 times in a row

    Args:
        password (str): The password string to analyze.

    Returns:
        tuple: (score, missing_list)
    """
    score = 0
    missing = []

    # --- Length scoring using for loop logic ---
    length = len(password)
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        missing.append("too short (need 8+ characters)")

    # --- Character type checks using a for loop ---
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in SPECIAL_CHARS:
            has_special = True

    if has_upper:
        score += 1
    else:
        missing.append("uppercase letter")

    if has_lower:
        score += 1
    else:
        missing.append("lowercase letter")

    if has_digit:
        score += 1
    else:
        missing.append("digit")

    if has_special:
        score += 1
    else:
        missing.append(f"special character ({SPECIAL_CHARS})")

    # --- Check for repeated characters (more than 2 in a row) ---
    has_no_repeats = True
    for i in range(2, len(password)):
        if password[i] == password[i - 1] == password[i - 2]:
            has_no_repeats = False
            break

    if has_no_repeats:
        score += 1
    else:
        missing.append("3+ repeated characters in a row")

    return score, missing


def print_analysis(password, score, missing):
    """Print a formatted password strength analysis."""
    max_score = 7
    rating = get_strength_rating(score)

    print(f"\n  Password : {password}")
    print(f"  Strength : {score}/{max_score} ({rating})")

    if missing:
        print(f"  Missing  : {', '.join(missing)}")
    else:
        print("  Missing  : None — excellent password!")

    return rating


def password_input_loop():
    """
    Use a while loop to keep asking for a password until strength >= 5.

    Demonstrates: while loop, break, continue.
    """
    print("\n" + "=" * 50)
    print("     PASSWORD STRENGTH ANALYZER")
    print("=" * 50)

    attempts = 0

    # While loop — keeps running until strength is acceptable
    while True:
        attempts += 1
        password = input(f"\n[Attempt {attempts}] Enter password: ").strip()

        if not password:
            print("  Password cannot be empty. Try again.")
            continue  # Skip rest of loop, go back to top

        score, missing = analyze_password(password)
        rating = print_analysis(password, score, missing)

        if score >= 5:
            print(f"\n  Password accepted after {attempts} attempt(s)!")
            break  # Exit the while loop
        else:
            print(f"\n  Too weak. Need score ≥ 5. Try again...\n")

    return password


def generate_password(length):
    """
    Generate a random password of the specified length.

    Uses a for loop to build the password character by character.

    Args:
        length (int): Desired password length.

    Returns:
        str: The generated password.
    """
    # Character pool
    pool = string.ascii_letters + string.digits + string.punctuation

    # for loop to build the password
    password = ""
    for _ in range(length):
        password += random.choice(pool)

    return password


def generator_menu():
    """Interactive password generator with strength display."""
    print("\n" + "=" * 50)
    print("     PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        try:
            length = int(input("\nEnter desired password length (8-64): "))
            if 8 <= length <= 64:
                break
            print(" Length must be between 8 and 64.")
        except ValueError:
            print(" Please enter a valid number.")

    password = generate_password(length)
    score, missing = analyze_password(password)

    print(f"\n  Generated : {password}")
    print_analysis(password, score, missing)


def main():
    """Entry point — run analyzer then generator."""
    password_input_loop()
    print("\n" + "-" * 50)
    another = input("\nWould you like to generate a secure password? (yes/no): ").strip().lower()
    if another == "yes":
        generator_menu()
    print("\n  Goodbye! Stay secure. \n")


if __name__ == "__main__":
    main()
