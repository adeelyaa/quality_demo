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
    total = 0

    for item in items:
        if item.get("active", True):
            if item.get("quantity", 0) > 0:
                if item.get("price", 0) > 0:
                    total += item["price"] * item["quantity"]

    discount = 0

    if customer_type == "vip":
        if total > 1000:
            discount = 0.25
        elif total > 500:
            discount = 0.15
        else:
            discount = 0.1
    elif customer_type == "regular":
        if total > 1000:
            discount = 0.12
        elif total > 500:
            discount = 0.07
        else:
            discount = 0.03
    elif customer_type == "new":
        if total > 1000:
            discount = 0.08
        elif total > 500:
            discount = 0.04
        else:
            discount = 0
    else:
        discount = 0

    if delivery_type == "express":
        delivery_price = 25
    elif delivery_type == "standard":
        delivery_price = 10
    elif delivery_type == "pickup":
        delivery_price = 0
    else:
        delivery_price = 15

    return total - total * discount + delivery_price


def classify_payment(amount, payment_type, country):
    if amount <= 0:
        return "invalid"

    if payment_type == "card":
        if country == "US":
            if amount > 1000:
                return "manual_review"
            elif amount > 500:
                return "additional_check"
            else:
                return "approved"
        elif country == "EU":
            if amount > 900:
                return "manual_review"
            elif amount > 400:
                return "additional_check"
            else:
                return "approved"
        else:
            if amount > 300:
                return "additional_check"
            else:
                return "approved"

    if payment_type == "bank_transfer":
        if amount > 2000:
            return "manual_review"
        elif amount > 1000:
            return "additional_check"
        else:
            return "approved"

    if payment_type == "cash":
        if amount > 500:
            return "not_allowed"
        else:
            return "approved"

    return "unknown"
