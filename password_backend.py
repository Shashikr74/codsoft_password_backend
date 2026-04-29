# file: password_backend.py

import string
import secrets

def generate_password(length=8, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    if length < 4:
        return "Error: Length should be at least 4"

    char_pool = ""

    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        return "Error: No character set selected"

    # Ensure at least one from each selected category
    password = []
    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    # Fill remaining length
    for _ in range(length - len(password)):
        password.append(secrets.choice(char_pool))

    # Shuffle securely
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)
