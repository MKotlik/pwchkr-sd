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


# int get_pass_strength(password)
def get_pass_strength(password):
    """Password strength Checker
    Args: string password
    Returns: int, strength from 0 to 10 based on presence of lowercase letters,
    uppercase letters, numbers, symbols, and length of password
    """
    strength = 0
    length = len(password)

    # Creating password element lists
    lower_chars = [c for c in password if c.islower()]
    upper_chars = [c for c in password if c.isupper()]
    numbers = [c for c in password if c.isdigit()]
    symbols = [c for c in password if c in "!@#$%^&*~-?"]

    # Debug
    if DEBUG:
        print "Lower: " + str(lower_chars)
        print "Upper: " + str(upper_chars)
        print "Numbers: " + str(numbers)
        print "Symbols: " + str(symbols)

    # Point tally
    if lower_chars:
        strength += 1
        if len(lower_chars) > 1:
            strength += 1
    if upper_chars:
        strength += 1
        if len(upper_chars) > 1:
            strength += 1
    if numbers:
        strength += 1
        if len(numbers) > 1:
            strength += 1
    if symbols:
        strength += 1
        if len(symbols) > 1:
            strength += 1
    if length > 8:
        strength += 1
        if length > 12:
            strength += 1

    return strength

if __name__ == "__main__":
    DEBUG = False
    print "Verifying password 'MyMilkshake3':"
    print verify_pass("MyMilkshake3")
    print "Verifying password 'bringstheboys':"
    print verify_pass("bringstheboys")
    print "Verifying password '3OH3':"
    print verify_pass("3OH3")
    print "======================"
    print "Checking strength of password '':"
    print get_pass_strength("")
    print "Checking strength of password 'M':"
    print get_pass_strength("M")
    print "Checking strength of password 'Me@3':"
    print get_pass_strength("Me@3")
    print "Checking strength of password '2stronk#You':"
    print get_pass_strength("2stronk#You")
    print "Checking strength of password '3Bull2Str@nk!':"
    print get_pass_strength("3Bull2Str@nk!")
