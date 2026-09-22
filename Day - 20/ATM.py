import bank
# print(bank.deposit(5000))
# print(bank.withdraw(2000))
# print(bank.check_balance())
enter_pin = int(input(" Enter your 4-Digit Pin : "))
# p = bank.pin_num()
if bank.pin_num() == enter_pin:
    print(" enter your choice:  ")
    print("1. want to check balance?")
    print("2. want to withdraw money?")
    print("3. want to deposit money?")
    choice = input()
    if choice == "1":
        print("balance in your account", bank.check_balance())
    elif choice == "2":
        amount = int(input(" Enter amount to withdraw : "))
        print(bank.withdraw(amount))
    elif choice == "3":
        amount2 = int(input(" Enter the amount to deposit : "))
        print(bank.deposit(amount2))
    else:
        print("please enter correct choice")
else:
    print("please enter your correct pin")