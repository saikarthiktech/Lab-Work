"""
Branch Coverage Test Cases for movie_tickets.py
SRN: PES2UG24CS141
Subject: Software Engineering Lab 6 - Code and Branch Coverage Analysis

Achieves 100% Branch Coverage and 100% Line Coverage by testing all
decision branches, boolean combinations, and boundary edge cases.
"""

import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ============================================================================
# 1. Tests for ticket_price(seat, age, show_hour, is_weekend)
# ============================================================================

def test_ticket_price_invalid_seat():
    """Branch: seat not in SEAT_PRICE -> True."""
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("balcony", 25, 14, False)


def test_ticket_price_valid_seats():
    """Branch: seat not in SEAT_PRICE -> False across all seat categories."""
    assert ticket_price("regular", 25, 14, False) == 150
    assert ticket_price("premium", 25, 14, False) == 250
    assert ticket_price("recliner", 25, 14, False) == 400


def test_ticket_price_show_hour_negative():
    """Branch: show_hour < 0 -> True."""
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)


def test_ticket_price_show_hour_too_high():
    """Branch: show_hour > 23 -> True."""
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


def test_ticket_price_morning_show():
    """Branch: show_hour < 12 -> True (price -= 50)."""
    # 150 - 50 = 100
    assert ticket_price("regular", 25, 9, False) == 100


def test_ticket_price_evening_show():
    """Branch: show_hour >= 18 -> True (price += 30)."""
    # 150 + 30 = 180
    assert ticket_price("regular", 25, 18, False) == 180


def test_ticket_price_afternoon_show():
    """Branch: show_hour < 12 is False and show_hour >= 18 is False."""
    # 150 + 0 = 150
    assert ticket_price("regular", 25, 14, False) == 150


def test_ticket_price_weekend_surcharge():
    """Branch: is_weekend -> True (price += 40)."""
    # 150 + 40 = 190
    assert ticket_price("regular", 25, 14, True) == 190


def test_ticket_price_weekday():
    """Branch: is_weekend -> False."""
    # 150 + 0 = 150
    assert ticket_price("regular", 25, 14, False) == 150


def test_ticket_price_infant():
    """Branch: age < 3 -> True (returns 0)."""
    assert ticket_price("regular", 2, 14, False) == 0


def test_ticket_price_child_discount():
    """Branch: age <= 12 -> True (price // 2)."""
    # 150 // 2 = 75
    assert ticket_price("regular", 10, 14, False) == 75
    # Boundary: age == 12
    assert ticket_price("regular", 12, 14, False) == 75


def test_ticket_price_senior_discount():
    """Branch: age >= 60 -> True (price // 2)."""
    # 150 // 2 = 75
    assert ticket_price("regular", 65, 14, False) == 75
    # Boundary: age == 60
    assert ticket_price("regular", 60, 14, False) == 75


def test_ticket_price_adult_no_discount():
    """Branch: age <= 12 is False and age >= 60 is False (regular adult price)."""
    # 150 (age 25)
    assert ticket_price("regular", 25, 14, False) == 150


# ============================================================================
# 2. Tests for group_discount(tickets, is_student_group)
# ============================================================================

def test_group_discount_invalid_tickets():
    """Branch: tickets < 1 -> True."""
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(-5, False)


def test_group_discount_ten_or_more_non_student():
    """Branch: tickets >= 10 -> True, is_student_group -> False."""
    # discount = 15
    assert group_discount(10, False) == 15


def test_group_discount_ten_or_more_student():
    """Branch: tickets >= 10 -> True, is_student_group -> True (discount = 15 + 5 = 20)."""
    assert group_discount(15, True) == 20


def test_group_discount_five_to_nine_non_student():
    """Branch: tickets >= 5 -> True, is_student_group -> False."""
    # discount = 10
    assert group_discount(5, False) == 10


def test_group_discount_five_to_nine_student():
    """Branch: tickets >= 5 -> True, is_student_group -> True (discount = 10 + 5 = 15)."""
    assert group_discount(8, True) == 15


def test_group_discount_under_five_non_student():
    """Branch: tickets < 5 -> else branch (discount = 0), is_student_group -> False."""
    assert group_discount(3, False) == 0


def test_group_discount_under_five_student():
    """Branch: is_student_group is True BUT discount > 0 is False (short-circuit / branch)."""
    # discount remains 0 because discount is not > 0
    assert group_discount(3, True) == 0


# ============================================================================
# 3. Tests for snack_combo(size, has_coupon)
# ============================================================================

def test_snack_combo_small_with_coupon():
    """Branch: size == 'small' -> True, has_coupon -> True."""
    # 120 - 50 = 70
    assert snack_combo("small", True) == 70


def test_snack_combo_small_without_coupon():
    """Branch: size == 'small' -> True, has_coupon -> False."""
    # 120
    assert snack_combo("small", False) == 120


def test_snack_combo_medium_with_coupon():
    """Branch: size == 'medium' -> True, has_coupon -> True."""
    # 180 - 50 = 130
    assert snack_combo("medium", True) == 130


def test_snack_combo_medium_without_coupon():
    """Branch: size == 'medium' -> True, has_coupon -> False."""
    # 180
    assert snack_combo("medium", False) == 180


def test_snack_combo_large_with_coupon():
    """Branch: else (large/other) -> True, has_coupon -> True."""
    # 250 - 50 = 200
    assert snack_combo("large", True) == 200


def test_snack_combo_large_without_coupon():
    """Branch: else (large/other) -> True, has_coupon -> False."""
    # 250
    assert snack_combo("large", False) == 250
