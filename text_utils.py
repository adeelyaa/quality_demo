def normalize_text(text):
    return " ".join(text.strip().lower().split())


def count_words(text):
    normalized = normalize_text(text)
    if not normalized:
        return 0
    return len(normalized.split())


def is_palindrome(text):
    normalized = normalize_text(text).replace(" ", "")
    return normalized == normalized[::-1]


def shorten_text(text, max_length):
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."