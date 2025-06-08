# Cash Machine

A simple Python program that simulates an ATM's ability to dispense money using different combinations of banknotes (10€, 50€, and 100€).

## How it works

The program takes an amount and finds all possible ways to pay it out using the available banknotes. For example, 100€ can be paid out as:
- 1 x 100€
- 2 x 50€
- 1 x 50€ + 5 x 10€
- 10 x 10€

## Running the program

1. Make sure you have Python 3.7+ installed
2. Run the program:
```bash
python main.py
```

The program will show all possible combinations for several test amounts (30€, 50€, 60€, 80€, 140€, 230€, 370€, 610€, and 980€).

## Project Structure

- `atm_payout.py`: Core logic for finding banknote combinations
- `main.py`: Example usage with test amounts
