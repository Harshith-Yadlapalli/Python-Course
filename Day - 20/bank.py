balance = 100000
pin = 3424
def deposit (amount):
    global balance
    return balance + amount
def withdraw (amount):
    global balance
    if amount < balance:
        balance = amount
        return balance
    return "insufficiant balance"
def check_balance():
    return balance
def pin_num():
    return pin