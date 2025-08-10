import tkinter as tk
from tkinter import ttk
import re

def get_strength_score(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    return score

def update_strength_meter(event=None):
    password = entry.get()
    score = get_strength_score(password)
    
    progress_bar["value"] = score
    if score == 0:
        result_label.config(text="❗ Please enter a password", fg="orange")
    elif score <= 2:
        result_label.config(text="❌ Weak Password", fg="red")
    elif score <= 4:
        result_label.config(text="⚠️ Medium Password", fg="blue")
    else:
        result_label.config(text="✅ Strong Password", fg="green")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker - Live Meter")
root.geometry("400x220")

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack()

# Progress Bar
progress_bar = ttk.Progressbar(root, length=250, maximum=5)
progress_bar.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Bind key release to update strength
entry.bind("<KeyRelease>", update_strength_meter)

root.mainloop()
