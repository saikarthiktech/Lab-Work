"""
Code Coverage Test Cases for movie_tickets.py
SRN: PES2UG24CS141
Subject: Software Engineering Lab 6 - Code and Branch Coverage Analysis
"""

import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ---------------------------------------------------------
# Test Cases for ticket_price (Line Coverage)
# ---------------------------------------------------------

def test_ticket_price_unknown_seat():
    """Verify that an unknown seat type raises ValueError."""
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("vip_box", 25, 14, False)


def test_ticket_price_invalid_show_hour():
    """Verify that a negative show hour raises ValueError."""
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)


def test_ticket_price_infant_morning_discount():
    """Verify infant (< 3) ticket price is 0, covering show_hour < 12 and age < 3."""
    # Base: premium (250) - morning (50) = 200, age < 3 returns 0
    assert ticket_price("premium", 2, 10, False) == 0


def test_ticket_price_evening_weekend_child():
    """Verify evening, weekend, and child (age <= 12) discounts."""
    # Base: recliner (400) + evening (30) + weekend (40) = 470; child (age 10) = 470 // 2 = 235
    assert ticket_price("recliner", 10, 19, True) == 235


# ---------------------------------------------------------
# Test Cases for group_discount (Line Coverage)
# ---------------------------------------------------------

def test_group_discount_zero_tickets():
    """Verify zero or negative tickets raise ValueError."""
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_group_discount_ten_plus_with_student():
    """Verify group discount for >= 10 tickets with student group bonus."""
    # tickets >= 10 (15) + student bonus (5) = 20
    assert group_discount(12, True) == 20


def test_group_discount_five_to_nine_tickets():
    """Verify group discount for 5 to 9 tickets."""
    # tickets >= 5 (10) + student bonus (5) = 15
    assert group_discount(6, True) == 15


def test_group_discount_small_group():
    """Verify small group (< 5 tickets) gets no discount."""
    assert group_discount(2, False) == 0


# ---------------------------------------------------------
# Test Cases for snack_combo (Line Coverage)
# ---------------------------------------------------------

def test_snack_combo_small():
    """Verify small combo price with coupon."""
    # small (120) - coupon (50) = 70
    assert snack_combo("small", True) == 70


def test_snack_combo_medium():
    """Verify medium combo price with coupon."""
    # medium (180) - coupon (50) = 130
    assert snack_combo("medium", True) == 130


def test_snack_combo_large():
    """Verify large/other combo price with coupon."""
    # large (250) - coupon (50) = 200
    assert snack_combo("large", True) == 200
