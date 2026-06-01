def build_report(records):
    total = 0
    active_count = 0
    inactive_count = 0
    errors = []

    for record in records:
        if record.get("active", True):
            active_count += 1
            total += record.get("amount", 0)
        else:
            inactive_count += 1

    return {
        "total": total,
        "active_count": active_count,
        "inactive_count": inactive_count,
        "errors": errors,
        "level": classify_total_level(total),
    }


def build_sales_report(items):
    return build_report(items)


def build_user_report(users):
    return build_report(users)


def build_payment_report(payments):
    return build_report(payments)


def classify_total_level(total):
    if total > 10000:
        return "high"

    if total > 5000:
        return "medium"

    if total > 1000:
        return "low"

    return "minimal"


def validate_report_status(status, total, errors):
    status_handlers = {
        "draft": validate_draft_report,
        "published": validate_published_report,
        "archived": validate_archived_report,
    }

    handler = status_handlers.get(status)
    if not handler:
        return "unknown"

    return handler(total, errors)


def validate_draft_report(total, errors):
    if total == 0:
        return "empty_draft"

    if errors:
        return "draft_with_errors"

    return "valid_draft"


def validate_published_report(total, errors):
    if total == 0:
        return "invalid_publication"

    if errors:
        return "published_with_warnings"

    return "published"


def validate_archived_report(total, errors):
    if total == 0:
        return "empty_archive"

    if errors:
        return "archive_with_errors"

    return "archived"
