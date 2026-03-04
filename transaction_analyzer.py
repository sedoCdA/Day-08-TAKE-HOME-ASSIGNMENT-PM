"""
Daily Transaction Analyzer — Paytm Case Study (Part D Bonus).

Accepts transactions via while loop, tracks credits/debits,
flags high-value transactions, and prints a bar chart summary.
"""


def get_transaction():
    """
    Prompt the user for a transaction amount and type.

    Returns:
        tuple: (amount, txn_type, category) or None if user types 'done'.
    """
    raw = input("\nAmount (or 'done' to finish): ").strip().lower()
    if raw == "done":
        return None

    try:
        amount = float(raw)
        if amount <= 0:
            print(" Amount must be positive.")
            return "skip"
    except ValueError:
        print(" Invalid amount. Please enter a number or 'done'.")
        return "skip"

    txn_type = input("Type (credit/debit)          : ").strip().lower()
    if txn_type not in ["credit", "debit"]:
        print(" Type must be 'credit' or 'debit'.")
        return "skip"

    category = input("Category (food/travel/bills/other): ").strip().lower()
    if category not in ["food", "travel", "bills", "other"]:
        category = "other"

    return amount, txn_type, category


def print_bar_chart(transactions):
    """
    Print a bar chart of the last 10 transactions.

    Each * represents ₹1000.

    Args:
        transactions (list): List of (amount, type, category) tuples.
    """
    print("\n" + "=" * 55)
    print("  BAR CHART — Last 10 Transactions (★ = ₹1,000)")
    print("=" * 55)

    # Show last 10 only
    recent = transactions[-10:]

    # for loop to print each bar
    for i, (amount, txn_type, category) in enumerate(recent, 1):
        stars = int(amount / 1000)
        bar = "★" * stars if stars > 0 else "▏"
        tag = "⬆ CR" if txn_type == "credit" else "⬇ DR"
        flag = " HIGH" if amount > 10000 else ""
        print(f"  {i:>2}. [{tag}] ₹{amount:>10,.2f}  {bar}{flag}")


def print_spending_breakdown(transactions):
    """
    Show spending breakdown by category using a dictionary.

    Args:
        transactions (list): List of (amount, type, category) tuples.
    """
    category_totals = {}

    # for loop to build category dictionary
    for amount, txn_type, category in transactions:
        if txn_type == "debit":
            if category not in category_totals:
                category_totals[category] = 0
            category_totals[category] += amount

    if not category_totals:
        print("\n  No debit transactions to show breakdown.")
        return

    print("\n" + "=" * 40)
    print("  SPENDING BREAKDOWN (Debits Only)")
    print("=" * 40)

    total_spent = sum(category_totals.values())

    for category, total in category_totals.items():
        percentage = (total / total_spent) * 100 if total_spent > 0 else 0
        bar_len = int(percentage / 5)
        bar = "█" * bar_len
        print(f"  {category.capitalize():<10} ₹{total:>10,.2f}  {bar} {percentage:.1f}%")


def print_summary(transactions):
    """
    Print overall transaction summary statistics.

    Args:
        transactions (list): List of (amount, type, category) tuples.
    """
    if not transactions:
        print("\n  No transactions to summarise.")
        return

    total_credits = 0
    total_debits = 0
    high_value_count = 0
    amounts = []

    # for loop to calculate all stats
    for amount, txn_type, _ in transactions:
        amounts.append(amount)
        if txn_type == "credit":
            total_credits += amount
        else:
            total_debits += amount
        if amount > 10000:
            high_value_count += 1

    net_balance = total_credits - total_debits
    highest = max(amounts)
    average = sum(amounts) / len(amounts)

    print("\n" + "=" * 45)
    print("  TRANSACTION SUMMARY")
    print("=" * 45)
    print(f"  Total Transactions  : {len(transactions)}")
    print(f"  Total Credits       : ₹{total_credits:>12,.2f}")
    print(f"  Total Debits        : ₹{total_debits:>12,.2f}")
    print(f"  Net Balance         : ₹{net_balance:>12,.2f}  {'OK' if net_balance >= 0 else 'NO'}")
    print(f"  Highest Transaction : ₹{highest:>12,.2f}")
    print(f"  Average Amount      : ₹{average:>12,.2f}")
    print(f"  High Value (>₹10K)  : {high_value_count} transaction(s)")
    print("=" * 45)


def main():
    """Entry point — collect transactions and print analytics."""
    transactions = []

    print("\n" + "=" * 55)
    print("     PAYTM TRANSACTION ANALYZER")
    print("=" * 55)
    print("  Enter transactions one by one. Type 'done' to finish.\n")

    # while loop — keeps accepting transactions until user types 'done'
    while True:
        result = get_transaction()

        if result is None:
            # User typed 'done' — exit the loop
            break

        if result == "skip":
            # Invalid input — continue to next iteration
            continue

        amount, txn_type, category = result
        transactions.append((amount, txn_type, category))

        # Flag high value immediately
        if amount > 10000:
            print(f" HIGH VALUE transaction flagged: ₹{amount:,.2f}")

        print(f"  Recorded: {txn_type.upper()} ₹{amount:,.2f} [{category}]")

    if not transactions:
        print("\n  No transactions entered. Exiting.")
        return

    # Print all analytics
    print_bar_chart(transactions)
    print_spending_breakdown(transactions)
    print_summary(transactions)


if __name__ == "__main__":
    main()
