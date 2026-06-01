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

    keyword_rules = {
        "error": {
            "critical": "critical_error",
            "warning": "warning_error",
            "default": "common_error",
        },
        "payment": {
            "failed": "payment_failed",
            "success": "payment_success",
            "default": "payment_unknown",
        },
        "user": {
            "created": "user_created",
            "deleted": "user_deleted",
            "blocked": "user_blocked",
            "default": "user_event",
        },
    }

    for keyword, rules in keyword_rules.items():
        if keyword in normalized:
            return classify_by_rules(normalized, rules)

    return "general"


def classify_by_rules(text, rules):
    for keyword, result in rules.items():
        if keyword != "default" and keyword in text:
            return result

    return rules["default"]


def format_user_notification(username, action, status):
    prefixes = {
        "success": "Success",
        "warning": "Warning",
        "error": "Error",
    }

    actions = {
        "created": "was created",
        "updated": "was updated",
        "deleted": "was deleted",
        "blocked": "was blocked",
    }

    prefix = prefixes.get(status, "Info")
    action_text = actions.get(action)

    if not action_text:
        return f"{prefix}: unknown action for user {username}"

    return f"{prefix}: user {username} {action_text}"
