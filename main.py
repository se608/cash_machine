from atm_payout import (
    ATMState,
    find_payout_combinations,
    format_combination,
    validate_amount,
    InvalidAmountError
)

def main():
    # Example initial state with plenty of notes
    initial_state: ATMState = {
        "ten_euro_notes": 20,
        "fifty_euro_notes": 50,
        "hundred_euro_notes": 30
    }

    # Test amounts
    test_amounts = [30, 50, 60, 80, 140, 230, 370, 610, 980]

    for amount in test_amounts:
        print(f"\nPossible combinations for {amount} EUR:")

        try:
            validate_amount(amount)
            combinations = find_payout_combinations(amount, initial_state)

            if combinations == []:
                print("No possible combinations found with available banknotes")
                continue

            for i, combination in enumerate(combinations, 1):
                print(f"{i}. {format_combination(combination)}")

        except InvalidAmountError as e:
            print(e)

if __name__ == "__main__":
    main()