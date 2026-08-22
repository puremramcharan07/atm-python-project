import tkinter as tk
from tkinter import messagebox
import atm_logic


root = tk.Tk()
root.title("ATM")
root.geometry("450x500")
root.resizable(False, False)


def clear():
    for widget in root.winfo_children():
        widget.destroy()


# ---------------- LOGIN ----------------

def login_screen():

    clear()

    tk.Label(
        root,
        text="ATM",
        font=("Arial", 25, "bold")
    ).pack(pady=40)

    tk.Label(
        root,
        text="Enter Your PIN:",
        font=("Arial", 14)
    ).pack()

    pin_entry = tk.Entry(
        root,
        show="*",
        font=("Arial", 16),
        justify="center"
    )
    pin_entry.pack(pady=10)

    def enter():

        entered_pin = pin_entry.get()

        if entered_pin == atm_logic.pin:
            account_screen()
        else:
            messagebox.showerror(
                "Error",
                "Incorrect PIN"
            )

    tk.Button(
        root,
        text="ENTER",
        width=15,
        command=enter
    ).pack(pady=15)

    tk.Button(
        root,
        text="EXIT",
        width=15,
        command=root.destroy
    ).pack()


# ---------------- ACCOUNT ----------------

def account_screen():

    clear()

    tk.Label(
        root,
        text="Select Account",
        font=("Arial", 20, "bold")
    ).pack(pady=40)

    tk.Button(
        root,
        text="1. Saving Account",
        width=22,
        command=menu_screen
    ).pack(pady=10)

    tk.Button(
        root,
        text="2. Current Account",
        width=22,
        command=menu_screen
    ).pack(pady=10)

    tk.Button(
        root,
        text="3. Exit",
        width=22,
        command=root.destroy
    ).pack(pady=10)


# ---------------- MAIN MENU ----------------

def menu_screen():

    clear()

    tk.Label(
        root,
        text="ATM SERVICES",
        font=("Arial", 20, "bold")
    ).pack(pady=30)

    tk.Button(
        root,
        text="1. Balance Enquiry",
        width=25,
        command=balance_screen
    ).pack(pady=6)

    tk.Button(
        root,
        text="2. Deposit",
        width=25,
        command=deposit_screen
    ).pack(pady=6)

    tk.Button(
        root,
        text="3. Cash Withdrawal",
        width=25,
        command=withdrawal_screen
    ).pack(pady=6)

    tk.Button(
        root,
        text="4. Pin Change",
        width=25,
        command=pin_change_screen
    ).pack(pady=6)

    tk.Button(
        root,
        text="5. Mini Statement",
        width=25,
        command=statement_screen
    ).pack(pady=6)

    tk.Button(
        root,
        text="6. Exit",
        width=25,
        command=root.destroy
    ).pack(pady=6)


# ---------------- BALANCE ----------------

def balance_screen():

    clear()

    tk.Label(
        root,
        text="Balance Enquiry",
        font=("Arial", 20, "bold")
    ).pack(pady=30)

    tk.Label(
        root,
        text="Enter PIN:"
    ).pack()

    pin_entry = tk.Entry(
        root,
        show="*",
        font=("Arial", 16)
    )
    pin_entry.pack(pady=10)

    def enter():

        success, result = atm_logic.check_balance(
            pin_entry.get()
        )

        if success:
            messagebox.showinfo(
                "Balance",
                f"Balance: ₹{result}"
            )
        else:
            messagebox.showerror(
                "Error",
                result
            )

    tk.Button(
        root,
        text="ENTER",
        width=15,
        command=enter
    ).pack(pady=10)

    tk.Button(
        root,
        text="BACK",
        width=15,
        command=menu_screen
    ).pack()


# ---------------- DEPOSIT ----------------

def deposit_screen():

    clear()

    tk.Label(
        root,
        text="Deposit Amount",
        font=("Arial", 20, "bold")
    ).pack(pady=30)

    amount_entry = tk.Entry(
        root,
        font=("Arial", 16)
    )
    amount_entry.pack(pady=10)

    def deposit():

        try:
            amount = int(amount_entry.get())

            success, result = atm_logic.deposit(amount)

            if not success:
                messagebox.showerror(
                    "Error",
                    result
                )
                return

            confirm = messagebox.askyesno(
                "Confirm Amount",
                result + "\n\nCorrect Amount?"
            )

            if confirm:

                new_balance = atm_logic.confirm_deposit(
                    amount
                )

                messagebox.showinfo(
                    "Success",
                    f"Total Balance: ₹{new_balance}"
                )

                menu_screen()

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter numbers only"
            )

    tk.Button(
        root,
        text="ENTER",
        width=15,
        command=deposit
    ).pack(pady=15)

    tk.Button(
        root,
        text="BACK",
        width=15,
        command=menu_screen
    ).pack()


# ---------------- WITHDRAWAL ----------------

def withdrawal_screen():

    clear()

    tk.Label(
        root,
        text="Cash Withdrawal",
        font=("Arial", 20, "bold")
    ).pack(pady=25)

    tk.Label(
        root,
        text="Enter Withdrawal Amount:"
    ).pack()

    amount_entry = tk.Entry(
        root,
        font=("Arial", 16)
    )
    amount_entry.pack(pady=8)

    tk.Label(
        root,
        text="Enter PIN:"
    ).pack()

    pin_entry = tk.Entry(
        root,
        show="*",
        font=("Arial", 16)
    )
    pin_entry.pack(pady=8)

    def withdraw():

        try:

            amount = int(amount_entry.get())

            success, result = atm_logic.withdrawal(
                amount,
                pin_entry.get()
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    f"Withdrawal Completed\n"
                    f"Total Balance: ₹{result}"
                )

                menu_screen()

            else:

                messagebox.showerror(
                    "Error",
                    result
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter valid amount"
            )

    tk.Button(
        root,
        text="ENTER",
        width=15,
        command=withdraw
    ).pack(pady=12)

    tk.Button(
        root,
        text="BACK",
        width=15,
        command=menu_screen
    ).pack()


# ---------------- PIN CHANGE ----------------

def pin_change_screen():

    clear()

    tk.Label(
        root,
        text="Pin Change",
        font=("Arial", 20, "bold")
    ).pack(pady=25)

    tk.Label(root, text="Enter Mobile Number:").pack()

    mobile = tk.Entry(root)
    mobile.pack(pady=5)

    tk.Label(root, text="Enter OTP:").pack()

    otp = tk.Entry(root)
    otp.pack(pady=5)

    tk.Label(root, text="Enter New PIN:").pack()

    new_pin = tk.Entry(
        root,
        show="*"
    )
    new_pin.pack(pady=5)

    tk.Label(root, text="Re-enter New PIN:").pack()

    confirm_pin = tk.Entry(
        root,
        show="*"
    )
    confirm_pin.pack(pady=5)

    def change():

        success, result = atm_logic.change_pin(
            mobile.get(),
            otp.get(),
            new_pin.get(),
            confirm_pin.get()
        )

        if success:

            messagebox.showinfo(
                "Success",
                result
            )

            login_screen()

        else:

            messagebox.showerror(
                "Error",
                result
            )

    tk.Button(
        root,
        text="ENTER",
        width=15,
        command=change
    ).pack(pady=12)

    tk.Button(
        root,
        text="BACK",
        width=15,
        command=menu_screen
    ).pack()


# ---------------- MINI STATEMENT ----------------

def statement_screen():

    clear()

    tk.Label(
        root,
        text="Mini Statement",
        font=("Arial", 20, "bold")
    ).pack(pady=30)

    data = atm_logic.mini_statement()

    if data:

        for item in data:
            tk.Label(
                root,
                text=item,
                font=("Arial", 12)
            ).pack(pady=5)

    else:

        tk.Label(
            root,
            text="No Transactions"
        ).pack(pady=20)

    tk.Label(
        root,
        text=f"Current Balance: ₹{atm_logic.balance}",
        font=("Arial", 14, "bold")
    ).pack(pady=20)

    tk.Button(
        root,
        text="BACK",
        width=15,
        command=menu_screen
    ).pack()


# ---------------- START ----------------

login_screen()

root.mainloop()