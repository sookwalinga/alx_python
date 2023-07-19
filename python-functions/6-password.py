def validate_password(password):
    # Check the length of the password
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and digits
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

        if has_upper and has_lower and has_digit:
            break

    # Check for spaces
    if ' ' in password:
        return False

    # Return True if all checks passed
    return has_upper and has_lower and has_digit
