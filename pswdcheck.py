# Password Checker
# SoftDev, Spring 2017
# Misha Kotlik


# boolean verify_pass(password)
def verify_pass(password):
    """Password verification function
    Args: string password
    Returns: boolean, true if password contains at least one lowercase letter,
    one uppercase letter, and one number.
    """
    lower_chars = [c for c in password if c.islower()]
    upper_chars = [c for c in password if c.isupper()]
    numbers = [c for c in password if c.isdigit()]
    if lower_chars and upper_chars and numbers:
        return True
    else:
        return False
