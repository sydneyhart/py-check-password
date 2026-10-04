import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "A1@abcde",           # Exactly 8 characters
        "A1@" + "a" * 13,     # Exactly 16 characters
        "ABCDEFG1@",          # Lowercase is not required
        "A123456@",           # Only one uppercase letter
        "Abcdefg1$",          # Only one digit and special character
    ],
)
def test_valid_password(password):
    assert check_password(password) is True


@pytest.mark.parametrize("special", list("$@#&!-_"))
def test_each_allowed_special_character(special):
    assert check_password(f"Abcdef1{special}") is True


@pytest.mark.parametrize("digit", "0123456789")
def test_each_allowed_digit(digit):
    assert check_password(f"Abcdef@{digit}") is True


@pytest.mark.parametrize(
    "password",
    [
        "",
        "qwerty",
        "Str@ng",
        "A1@abcd",            # Exactly 7 characters
        "A1@" + "a" * 14,     # Exactly 17 characters
        "abcdef1@",           # Missing uppercase letter
        "Abcdefg@",           # Missing digit
        "Abcdefg1",           # Missing special character
        "abcdefgh",           # Missing all three required types
    ],
)
def test_invalid_password(password):
    assert check_password(password) is False


@pytest.mark.parametrize(
    "character",
    [
        " ",
        "\t",
        "\n",
        ".",
        ",",
        "?",
        "+",
        "=",
        "/",
        "\\",
        "*",
        "%",
        "^",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        ":",
        ";",
        "'",
        '"',
        "`",
        "~",
        "é",
        "É",
        "Ж",
        "中",
        "١",                 # Non-ASCII digit
        "１",                 # Fullwidth digit
        "²",                 # Superscript digit
        "🙂",
    ],
)
def test_forbidden_characters(character):
    assert check_password(f"Abcdef1@{character}") is False
