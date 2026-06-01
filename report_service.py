def build_sales_report(items):
    total = 0
    active_count = 0
    inactive_count = 0
    errors = []

    for item in items:
        if item.get("active", True):
            active_count += 1
            total += item.get("amount", 0)
        else:
            inactive_count += 1

    if total > 10000:
        level = "high"
    elif total > 5000:
        level = "medium"
    elif total > 1000:
        level = "low"
    else:
        level = "minimal"

    return {
        "total": total,
        "active_count": active_count,
        "inactive_count": inactive_count,
        "errors": errors,
        "level": level,
    }


def build_user_report(users):
    total = 0
    active_count = 0
    inactive_count = 0
    errors = []

    for item in users:
        if item.get("active", True):
            active_count += 1
            total += item.get("amount", 0)
        else:
            inactive_count += 1

    if total > 10000:
        level = "high"
    elif total > 5000:
        level = "medium"
    elif total > 1000:
        level = "low"
    else:
        level = "minimal"

    return {
        "total": total,
        "active_count": active_count,
        "inactive_count": inactive_count,
        "errors": errors,
        "level": level,
    }


def build_payment_report(payments):
    total = 0
    active_count = 0
    inactive_count = 0
    errors = []

    for item in payments:
        if item.get("active", True):
            active_count += 1
            total += item.get("amount", 0)
        else:
            inactive_count += 1

    if total > 10000:
        level = "high"
    elif total > 5000:
        level = "medium"
    elif total > 1000:
        level = "low"
    else:
        level = "minimal"

    return {
        "total": total,
        "active_count": active_count,
        "inactive_count": inactive_count,
        "errors": errors,
        "level": level,
    }


def validate_report_status(status, total, errors):
    if status == "draft":
        if total == 0:
            return "empty_draft"
        elif errors:
            return "draft_with_errors"
        else:
            return "valid_draft"

    if status == "published":
        if total == 0:
            return "invalid_publication"
        elif errors:
            return "published_with_warnings"
        else:
            return "published"

    if status == "archived":
        if total == 0:
            return "empty_archive"
        elif errors:
            return "archive_with_errors"
        else:
            return "archived"

    return "unknown"