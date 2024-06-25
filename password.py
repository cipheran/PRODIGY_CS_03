import re

def assess_password_strength(password):
    length_score = len(password) * 4
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    numbers = bool(re.search(r'[0-9]', password))
    symbols = bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>/?\[\]\'\"\\|`~]', password))

    character_types = sum([uppercase, lowercase, numbers, symbols])
    character_types_score = character_types * 4

    if character_types >= 3:
        character_types_score += (character_types - 2) * 2

    consecutive_score = 0
    for i in range(len(password) - 1):
        if ord(password[i]) == ord(password[i+1]) - 1 or ord(password[i]) == ord(password[i+1]) + 1:
            consecutive_score -= 1

    sequential_score = 0
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2:
            sequential_score -= 1
        if ord(password[i]) == ord(password[i+1]) + 1 == ord(password[i+2]) + 2:
            sequential_score -= 1

    total_score = length_score + character_types_score + consecutive_score + sequential_score

    if total_score >= 60:
        feedback = "Strong"
    elif total_score >= 40:
        feedback = "Medium"
    else:
        feedback = "Weak"

    return total_score, feedback

password = input("Enter your password: ")
score, strength = assess_password_strength(password)
print("Password Strength:", strength)