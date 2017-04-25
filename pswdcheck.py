# Password Checker
# SoftDev, Spring 2017
# Misha Kotlik


# Global debug setting
DEBUG = False


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
    if DEBUG:
        print "Lower: " + str(lower_chars)
        print "Upper: " + str(upper_chars)
        print "Numbers: " + str(numbers)
    if lower_chars and upper_chars and numbers:
        return True
    else:
        return False


if __name__ == "__main__":
    DEBUG = False
    print "Verifying password 'MyMilkshake3':"
    print verify_pass("MyMilkshake3")
    print "Verifying password 'bringstheboys':"
    print verify_pass("bringstheboys")
    print "Verifying password '3OH3':"
    print verify_pass("3OH3")
