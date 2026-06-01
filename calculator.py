def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_order_total(items, customer_type, delivery_type):
    total = sum(
        item["price"] * item["quantity"]
        for item in items
        if item.get("active", True)
        and item.get("quantity", 0) > 0
        and item.get("price", 0) > 0
    )

    discount = get_discount_rate(total, customer_type)
    delivery_price = get_delivery_price(delivery_type)

    return total - total * discount + delivery_price


def get_discount_rate(total, customer_type):
    discount_rules = {
        "vip": [(1000, 0.25), (500, 0.15), (0, 0.10)],
        "regular": [(1000, 0.12), (500, 0.07), (0, 0.03)],
        "new": [(1000, 0.08), (500, 0.04), (0, 0.00)],
    }

    for threshold, rate in discount_rules.get(customer_type, []):
        if total > threshold:
            return rate

    return 0


def get_delivery_price(delivery_type):
    delivery_prices = {
        "express": 25,
        "standard": 10,
        "pickup": 0,
    }

    return delivery_prices.get(delivery_type, 15)


def classify_payment(amount, payment_type, country):
    if amount <= 0:
        return "invalid"

    if payment_type == "card":
        return classify_card_payment(amount, country)

    if payment_type == "bank_transfer":
        return classify_by_threshold(amount, 2000, 1000)

    if payment_type == "cash":
        return "not_allowed" if amount > 500 else "approved"

    return "unknown"


def classify_card_payment(amount, country):
    thresholds = {
        "US": (1000, 500),
        "EU": (900, 400),
    }

    manual_limit, check_limit = thresholds.get(country, (None, 300))

    if manual_limit is not None and amount > manual_limit:
        return "manual_review"

    if amount > check_limit:
        return "additional_check"

    return "approved"


def classify_by_threshold(amount, manual_limit, check_limit):
    if amount > manual_limit:
        return "manual_review"

    if amount > check_limit:
        return "additional_check"

    return "approved"
