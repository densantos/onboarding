import secrets
import string

def generate_password(length=12):
    """Generate a secure random password."""
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")

    # Characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generating a random password
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password
