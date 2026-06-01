from app.text_utils import (
    normalize_text,
    count_words,
    is_palindrome,
    shorten_text,
    classify_message,
    format_user_notification,
)


def test_normalize_text():
    assert normalize_text("  Hello    WORLD ") == "hello world"


def test_count_words():
    assert count_words("Hello world from tests") == 4
    assert count_words("   ") == 0


def test_is_palindrome():
    assert is_palindrome("level") is True
    assert is_palindrome("hello") is False


def test_shorten_text():
    assert shorten_text("hello", 10) == "hello"
    assert shorten_text("hello world", 5) == "hello..."


def test_classify_message():
    assert classify_message("") == "empty"
    assert classify_message("critical error happened") == "critical_error"
    assert classify_message("payment success") == "payment_success"
    assert classify_message("user deleted") == "user_deleted"
    assert classify_message("something else") == "general"


def test_format_user_notification():
    assert format_user_notification("anna", "created", "success") == "Success: user anna was created"
    assert format_user_notification("anna", "blocked", "warning") == "Warning: user anna was blocked"
    assert format_user_notification("anna", "unknown", "error") == "Error: unknown action for user anna"