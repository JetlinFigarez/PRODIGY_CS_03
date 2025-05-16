import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    print("\n--- Password Analysis ---")
    print(f"Password: {password}")
    if length_error:
        print("❌ Password should be at least 8 characters long.")
    if digit_error:
        print("❌ Add at least one number.")
    if uppercase_error:
        print("❌ Add at least one uppercase letter.")
    if lowercase_error:
        print("❌ Add at least one lowercase letter.")
    if symbol_error:
        print("❌ Add at least one special character.")

    if score == 5:
        print("✅ Strong Password 💪")
    elif 3 <= score < 5:
        print("⚠️ Medium Strength Password – Could Be Better.")
    else:
        print("🚫 Weak Password – Needs Improvement.")

if __name__ == "__main__":
    user_input = input("Enter your password to test: ")
    check_password_strength(user_input)
