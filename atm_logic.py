# atm_app.py

pin = "7093"
balance = 5000
transactions = []


# Balance Enquiry
def check_balance(entered_pin):

    if entered_pin == pin:
        return True, balance
    else:
        return False, "Incorrect Pin"


# Deposit
def deposit(amount):

    global balance

    if amount % 100 != 0:
        return False, "Enter Amount in multiples of 500, 200, 100 only"

    a = amount // 500
    rem = amount % 500

    b = rem // 200
    rem1 = rem % 200

    c = rem1 // 100

    details = (
        f"500*{a}={500*a}\n"
        f"200*{b}={200*b}\n"
        f"100*{c}={100*c}\n"
        f"Total Amount={amount}"
    )

    return True, details


# Confirm Deposit
def confirm_deposit(amount):

    global balance

    balance = balance + amount

    transactions.append(
        f"Deposit: ₹{amount}"
    )

    return balance


# Cash Withdrawal
def withdrawal(amount, entered_pin):

    global balance

    if entered_pin != pin:
        return False, "Incorrect Pin"

    if amount > balance:
        return False, "Insufficient Balance"

    balance = balance - amount

    transactions.append(
        f"Withdrawal: ₹{amount}"
    )

    return True, balance


# PIN Change
def change_pin(mobile, otp, new_pin, confirm_pin):

    global pin

    if len(mobile) != 10 or not mobile.isdigit():
        return False, "Enter valid Mobile Number"

    # Demo OTP
    if otp != "1234":
        return False, "Incorrect OTP"

    if len(new_pin) != 4 or not new_pin.isdigit():
        return False, "PIN must contain 4 digits"

    if new_pin != confirm_pin:
        return False, "PIN Not Matched"

    pin = new_pin

    return True, "PIN Successfully Changed"


# Mini Statement
def mini_statement():

    return transactions[-5:]