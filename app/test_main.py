from string import ascii_letters, ascii_uppercase, digits


def check_password(password: str) -> bool:
    if not 8 <= len(password) <= 16:
        return False

    special_characters = "$@#&!-_"
    allowed_characters = ascii_letters + digits + special_characters

    has_upper = False
    has_digit = False
    has_special = False

    for character in password:
        if character not in allowed_characters:
            return False

        if character in ascii_uppercase:
            has_upper = True
        elif character in digits:
            has_digit = True
        elif character in special_characters:
            has_special = True

    return all((has_upper, has_digit, has_special))
