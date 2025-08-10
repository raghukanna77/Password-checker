import tkinter as tk
import re

def check_password_strength():
    password = entry.get()
    
    # Strength rules
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Determine strength
    errors = sum([length_error, lowercase_error, uppercase_error, digit_error, special_error])
    if len(password) == 0:
        result_label.config(text="❗ Please enter a password", fg="orange")
    elif errors == 0:
        result_label.config(text="✅ Strong Password 💪", fg="green")
    elif errors <= 2:
        result_label.config(text="⚠️ Medium Password 😐", fg="blue")
    else:
        result_label.config(text="❌ Weak Password", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=check_password_strength).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
