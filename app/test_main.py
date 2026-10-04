import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "A1@abcde",
        "A1@" + "a" * 13,
        "ABCDEFG1@",
        "A123456@",
        "Abcdefg1$",
    ],
)
def test_valid_password(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize("special", list("$@#&!-_"))
def test_each_allowed_special_character(special: str) -> None:
    assert check_password(f"Abcdef1{special}") is True


@pytest.mark.parametrize("digit", "0123456789")
def test_each_allowed_digit(digit: str) -> None:
    assert check_password(f"Abcdef@{digit}") is True


@pytest.mark.parametrize(
    "password",
    [
        "",
        "qwerty",
        "Str@ng",
        "A1@abcd",
        "A1@" + "a" * 14,
        "abcdef1@",
        "Abcdefg@",
        "Abcdefg1",
        "abcdefgh",
    ],
)
def test_invalid_password(password: str) -> None:
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
        "١",
        "１",
        "²",
        "🙂",
    ],
)
def test_forbidden_characters(character: str) -> None:
    assert check_password(f"Abcdef1@{character}") is False
