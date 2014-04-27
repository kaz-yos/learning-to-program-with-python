###
### C-c C-c for eval buffer
### example program: ATM
## Create variables
user_pin = 5544
user_balance = 500

## define an ATM
pin_attempt = input("enter your PIN ")
pin_attempt = int(pin_attempt)  # convert to int

if pin_attempt == user_pin:
    amount_to_withdraw = int(input("How much would youlike to withdraw? "))
    if amount_to_withdraw <= user_balance:
        print("Disbursing " + str(amount_to_withdraw))
        print("Remaining balance: " + str(user_balance - amount_to_withdraw))
    else:
        print("Insufficient funds.")
else:
    print("Invalid PIN.")

print("Transaction concluded.")
