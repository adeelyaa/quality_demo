import pytest

from app.calculator import (
    add,
    subtract,
    multiply,
    divide,
    calculate_average,
    calculate_order_total,
    get_discount_rate,
    get_delivery_price,
    classify_payment,
)


def test_basic_math_operations():
    assert add(2, 3) == 5
    assert subtract(7, 2) == 5
    assert multiply(4, 3) == 12
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_calculate_average():
    assert calculate_average([2, 4, 6]) == 4
    assert calculate_average([]) == 0


def test_order_total_for_vip_customer():
    items = [
        {"price": 100, "quantity": 2, "active": True},
        {"price": 50, "quantity": 1, "active": True},
        {"price": 1000, "quantity": 1, "active": False},
    ]

    assert calculate_order_total(items, "vip", "standard") == 235


def test_discount_and_delivery_rules():
    assert get_discount_rate(1200, "vip") == 0.25
    assert get_discount_rate(600, "regular") == 0.07
    assert get_discount_rate(300, "new") == 0
    assert get_delivery_price("express") == 25
    assert get_delivery_price("pickup") == 0
    assert get_delivery_price("unknown") == 15


def test_classify_payment():
    assert classify_payment(-1, "card", "US") == "invalid"
    assert classify_payment(1200, "card", "US") == "manual_review"
    assert classify_payment(600, "card", "EU") == "additional_check"
    assert classify_payment(100, "cash", "US") == "approved"
    assert classify_payment(700, "cash", "US") == "not_allowed"