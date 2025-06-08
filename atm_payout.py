from typing import TypedDict


class ATMState(TypedDict):
    ten_euro_notes: int
    fifty_euro_notes: int
    hundred_euro_notes: int


class InvalidAmountError(Exception):
    """Raised when the amount is invalid for ATM payout."""
    pass


def validate_amount(amount: int) -> None:
    """
    Validates if the amount is valid for ATM payout.
    Raises InvalidAmountError if the amount is invalid.
    """
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive")
    if amount % 10 != 0:
        raise InvalidAmountError("Amount must be a multiple of 10")


def find_payout_combinations(amount: int, state: ATMState) -> list[dict[int, int]]:
    """
    Finds all possible combinations of banknotes that sum up to the target amount.
    Returns a list of dictionaries where each dictionary represents a combination
    with keys as denominations and values as counts.
    """
    combinations = []

    # Iterate through all possible combinations of 100 and 50 EUR notes
    max_hundreds = min(amount // 100, state["hundred_euro_notes"])
    max_fifties = min(amount // 50, state["fifty_euro_notes"])

    for hundreds in range(max_hundreds + 1):
        amount_remaining_after_hundreds = amount - hundreds * 100

        for fifties in range(min(amount_remaining_after_hundreds // 50, max_fifties) + 1):
            amount_remaining_after_fifties = amount_remaining_after_hundreds - fifties * 50

            tens_needed = amount_remaining_after_fifties // 10

            if tens_needed <= state["ten_euro_notes"]:
                combination = {}
                if hundreds > 0:
                    combination[100] = hundreds
                if fifties > 0:
                    combination[50] = fifties
                if tens_needed > 0:
                    combination[10] = tens_needed

                combinations.append(combination)

    return combinations


def format_combination(combination: dict[int, int]) -> str:
    """Formats a combination into a human-readable string."""
    parts = []

    for denomination, count in sorted(combination.items(), reverse=True):
        parts.append(f"{count} x {denomination} EUR")

    return " + ".join(parts)