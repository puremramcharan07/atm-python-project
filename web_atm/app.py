from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ATM details
pin = "7093"
balance = 5000
transactions = []


# ---------------- LOGIN ----------------

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        entered_pin = request.form["pin"]

        if entered_pin == pin:
            return redirect(url_for("account"))

        return render_template(
            "index.html",
            message="Incorrect PIN"
        )

    return render_template(
        "index.html",
        message=""
    )


# ---------------- ACCOUNT ----------------

@app.route("/account", methods=["GET", "POST"])
def account():

    if request.method == "POST":
        account_type = request.form["account"]
        return redirect(url_for("dashboard"))

    return render_template("account.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html",
        balance=balance
    )


# ---------------- BALANCE ----------------

@app.route("/balance", methods=["GET", "POST"])
def balance_enquiry():

    if request.method == "POST":

        entered_pin = request.form["pin"]

        if entered_pin == pin:
            return render_template(
                "balance.html",
                balance=balance,
                message=""
            )

        return render_template(
            "balance.html",
            balance=None,
            message="Incorrect PIN"
        )

    return render_template(
        "balance.html",
        balance=None,
        message=""
    )


# ---------------- DEPOSIT ----------------

@app.route("/deposit", methods=["GET", "POST"])
def deposit():

    if request.method == "POST":

        try:
            amount = int(request.form["amount"])

            if amount <= 0:
                return render_template(
                    "deposit.html",
                    message="Enter a valid amount"
                )

            if amount % 100 != 0:
                return render_template(
                    "deposit.html",
                    message="Enter amount in multiples of 100"
                )

            a = amount // 500
            rem = amount % 500

            b = rem // 200
            rem = rem % 200

            c = rem // 100

            details = (
                f"500 × {a} = ₹{500 * a}<br>"
                f"200 × {b} = ₹{200 * b}<br>"
                f"100 × {c} = ₹{100 * c}<br>"
                f"<strong>Total Amount = ₹{amount}</strong>"
            )

            return render_template(
                "deposit_confirm.html",
                amount=amount,
                details=details
            )

        except ValueError:

            return render_template(
                "deposit.html",
                message="Enter numbers only"
            )

    return render_template(
        "deposit.html",
        message=""
    )


# ---------------- CONFIRM DEPOSIT ----------------

@app.route("/confirm-deposit", methods=["POST"])
def confirm_deposit():

    global balance

    amount = int(request.form["amount"])

    balance += amount

    transactions.append(
        f"Deposit: ₹{amount}"
    )

    return render_template(
        "success.html",
        message=f"Deposit Successful! Current Balance: ₹{balance}"
    )


# ---------------- WITHDRAWAL ----------------

@app.route("/withdraw", methods=["GET", "POST"])
def withdrawal():

    if request.method == "POST":

        try:

            amount = int(request.form["amount"])
            entered_pin = request.form["pin"]

            if entered_pin != pin:
                return render_template(
                    "withdraw.html",
                    message="Incorrect PIN"
                )

            if amount <= 0:
                return render_template(
                    "withdraw.html",
                    message="Enter a valid amount"
                )

            if amount > balance:
                return render_template(
                    "withdraw.html",
                    message="Insufficient Balance"
                )

            return render_template(
                "withdraw_confirm.html",
                amount=amount
            )

        except ValueError:

            return render_template(
                "withdraw.html",
                message="Enter valid amount"
            )

    return render_template(
        "withdraw.html",
        message=""
    )


# ---------------- CONFIRM WITHDRAWAL ----------------

@app.route("/confirm-withdraw", methods=["POST"])
def confirm_withdraw():

    global balance

    amount = int(request.form["amount"])

    if amount > balance:
        return render_template(
            "withdraw.html",
            message="Insufficient Balance"
        )

    balance -= amount

    transactions.append(
        f"Withdrawal: ₹{amount}"
    )

    return render_template(
        "success.html",
        message=f"Withdrawal Successful! Current Balance: ₹{balance}"
    )


# ---------------- PIN CHANGE ----------------

@app.route("/pin-change", methods=["GET", "POST"])
def pin_change():

    global pin

    if request.method == "POST":

        mobile = request.form["mobile"]
        otp = request.form["otp"]
        new_pin = request.form["new_pin"]
        confirm_pin = request.form["confirm_pin"]

        if len(mobile) != 10 or not mobile.isdigit():
            return render_template(
                "pin_change.html",
                message="Enter valid Mobile Number"
            )

        if otp != "1234":
            return render_template(
                "pin_change.html",
                message="Incorrect OTP"
            )

        if len(new_pin) != 4 or not new_pin.isdigit():
            return render_template(
                "pin_change.html",
                message="PIN must contain 4 digits"
            )

        if new_pin != confirm_pin:
            return render_template(
                "pin_change.html",
                message="PIN Not Matched"
            )

        pin = new_pin

        return render_template(
            "success.html",
            message="PIN Successfully Changed"
        )

    return render_template(
        "pin_change.html",
        message=""
    )


# ---------------- MINI STATEMENT ----------------

@app.route("/statement")
def statement():

    recent_transactions = transactions[-5:]

    return render_template(
        "statement.html",
        transactions=recent_transactions,
        balance=balance
    )


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    return redirect(url_for("login"))


# ---------------- RUN ----------------
if __name__ == "__main__":
    import webbrowser
    from threading import Timer

    Timer(1, lambda: webbrowser.open("http://127.0.0.1:5000")).start()

    app.run(debug=True)