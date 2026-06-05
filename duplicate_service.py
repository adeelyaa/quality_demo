def build_sales_summary(records):
    total_amount = 0
    active_count = 0
    inactive_count = 0
    high_value_count = 0
    errors = []

    for record in records:
        amount = record.get("amount", 0)
        is_active = record.get("active", True)

        if is_active:
            active_count += 1
            total_amount += amount

            if amount > 1000:
                high_value_count += 1
        else:
            inactive_count += 1

        if amount < 0:
            errors.append(record)

    if total_amount > 10000:
        level = "high"
    elif total_amount > 5000:
        level = "medium"
    elif total_amount > 1000:
        level = "low"
    else:
        level = "minimal"

    return {
        "total_amount": total_amount,
        "active_count": active_count,
        "inactive_count": inactive_count,
        "high_value_count": high_value_count,
        "errors_count": len(errors),
        "level": level,
    }


def build_payment_summary(records):
    total_amount = 0
    active_count = 0
    inactive_count = 0
    high_value_count = 0
    errors = []

    for record in records:
        amount = record.get("amount", 0)
        is_active = record.get("active", True)

        if is_active:
            active_count += 1
            total_amount += amount

            if amount > 1000:
                high_value_count += 1
        else:
            inactive_count += 1

        if amount < 0:
            errors.append(record)

    if total_amount > 10000:
        level = "high"
    elif total_amount > 5000:
        level = "medium"
    elif total_amount > 1000:
        level = "low"
    else:
        level = "minimal"

    return {
        "total_amount": total_amount,
        "active_count": active_count,
        "inactive_count": inactive_count,
        "high_value_count": high_value_count,
        "errors_count": len(errors),
        "level": level,
    }
