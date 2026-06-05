from report_service import (
    build_report,
    build_sales_report,
    build_user_report,
    build_payment_report,
    classify_total_level,
    validate_report_status,
)


def test_build_report():
    records = [
        {"active": True, "amount": 100},
        {"active": True, "amount": 200},
        {"active": False, "amount": 500},
    ]

    report = build_report(records)

    assert report["total"] == 300
    assert report["active_count"] == 2
    assert report["inactive_count"] == 1
    assert report["level"] == "minimal"


def test_specific_report_builders():
    records = [{"active": True, "amount": 2000}]

    assert build_sales_report(records)["level"] == "low"
    assert build_user_report(records)["level"] == "low"
    assert build_payment_report(records)["level"] == "low"


def test_classify_total_level():
    assert classify_total_level(12000) == "high"
    assert classify_total_level(7000) == "medium"
    assert classify_total_level(2000) == "low"
    assert classify_total_level(100) == "minimal"


def test_validate_report_status():
    assert validate_report_status("draft", 0, []) == "empty_draft"
    assert validate_report_status("draft", 100, []) == "valid_draft"
    assert validate_report_status("published", 0, []) == "invalid_publication"
    assert validate_report_status("published", 100, ["minor"]) == "published_with_warnings"
    assert validate_report_status("archived", 100, []) == "archived"
    assert validate_report_status("unknown", 100, []) == "unknown"
