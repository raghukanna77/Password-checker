import re

def check_password_strength(password):
    # Strength rules
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count number of failed rules
    errors = sum([length_error, lowercase_error, uppercase_error, digit_error, special_error])

    if len(password) == 0:
        return "❗ Please enter a password"
    elif errors == 0:
        return "✅ Strong Password 💪"
    elif errors <= 2:
        return "⚠️ Medium Password 😐"
    else:
        return "❌ Weak Password"

if __name__ == "__main__":
    print("=== Password Strength Checker (Console) ===")
    pwd = input("Enter your password: ")
    print(check_password_strength(pwd))
