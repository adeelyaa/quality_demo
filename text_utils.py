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


def classify_message(text):
    normalized = normalize_text(text)

    if not normalized:
        return "empty"

    if "error" in normalized:
        if "critical" in normalized:
            return "critical_error"
        elif "warning" in normalized:
            return "warning_error"
        else:
            return "common_error"

    if "payment" in normalized:
        if "failed" in normalized:
            return "payment_failed"
        elif "success" in normalized:
            return "payment_success"
        else:
            return "payment_unknown"

    if "user" in normalized:
        if "created" in normalized:
            return "user_created"
        elif "deleted" in normalized:
            return "user_deleted"
        elif "blocked" in normalized:
            return "user_blocked"
        else:
            return "user_event"

    return "general"


def format_user_notification(username, action, status):
    if status == "success":
        prefix = "Success"
    elif status == "warning":
        prefix = "Warning"
    elif status == "error":
        prefix = "Error"
    else:
        prefix = "Info"

    if action == "created":
        return f"{prefix}: user {username} was created"
    elif action == "updated":
        return f"{prefix}: user {username} was updated"
    elif action == "deleted":
        return f"{prefix}: user {username} was deleted"
    elif action == "blocked":
        return f"{prefix}: user {username} was blocked"
    else:
        return f"{prefix}: unknown action for user {username}"
