import sys
# Expecting exactly 2 parameters: Initial balance and Deposit amount
if len(sys.argv) != 3:
    print("ERROR: Please provide Initial Balance and Deposit Amount as parameters.")
    print("Usage: python3 bank_balance.py <INITIAL_BALANCE> <DEPOSIT_AMOUNT>")
    sys.exit(1)
# Reading values from Jenkins parameters (command-line arguments)
initial_balance = float(sys.argv[1])
deposit_amount = float(sys.argv[2])
print("\n=== INPUT RECEIVED FROM JENKINS PARAMETERS ===")
print("Initial Balance:", initial_balance)
print("Deposit Amount:", deposit_amount)
# Calculate updated balance
updated_balance = initial_balance + deposit_amount
# Output
print("\n===== RESULT =====")
print("Updated Balance after Deposit:", updated_balance)
