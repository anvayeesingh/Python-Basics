import random
import string


def generate_random_password(length=12):
    if length < 3:
        raise ValueError("Password length must be at least 3 characters.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
    ]
    all_chars = lower + upper + digits
    password_chars += [
        random.choice(all_chars) for _ in range(length - len(password_chars))
    ]
    random.shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    generated_password = generate_random_password(12)
    print(f"Generated Password: {generated_password}")
