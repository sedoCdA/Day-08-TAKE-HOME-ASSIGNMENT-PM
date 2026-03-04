"""
Diamond Pattern Printer — Part C AI-Augmented Task.

Prints a diamond of asterisks using nested loops only.
No string multiplication tricks used.
"""


def print_diamond(rows):
    """
    Print a diamond pattern of asterisks using nested loops only.

    The diamond has (rows) lines in the upper half including the middle,
    and (rows - 1) lines in the lower half.

    Args:
        rows (int): Number of rows for the upper half (including middle row).
    """
    if rows <= 0:
        print(" Rows must be a positive integer.")
        return

    if rows == 1:
        print("*")
        return

    # --- Upper half (including middle row) ---
    # Row 1: 1 star, (rows-1) spaces before it
    # Row 2: 3 stars, (rows-2) spaces before it
    # Row n: (2n-1) stars, (rows-n) spaces before it
    for i in range(1, rows + 1):
        # Print leading spaces using a for loop (no string multiplication)
        for _ in range(rows - i):
            print(" ", end="")

        # Print asterisks using a for loop
        for _ in range(2 * i - 1):
            print("*", end="")

        print()  # Move to next line

    # --- Lower half (mirror of upper, excluding middle row) ---
    # Start from (rows-1) and go down to 1
    for i in range(rows - 1, 0, -1):
        # Print leading spaces
        for _ in range(rows - i):
            print(" ", end="")

        # Print asterisks
        for _ in range(2 * i - 1):
            print("*", end="")

        print()  # Move to next line


def main():
    """Entry point for diamond pattern printer."""
    print("\n=== Diamond Pattern Generator ===\n")

    while True:
        try:
            rows = int(input("Enter number of rows for upper half: "))
            if rows >= 0:
                break
            print(" Please enter a non-negative integer.")
        except ValueError:
            print(" Please enter a valid integer.")

    print()
    print_diamond(rows)


if __name__ == "__main__":
    main()
