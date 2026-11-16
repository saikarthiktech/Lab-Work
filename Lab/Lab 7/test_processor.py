from hypothesis import given, strategies as st

from movie_tickets import average_rating, parse_seat, total_price


@given(st.one_of(st.text(), st.none()))
def test_parse_seat_no_crash(value):
    result = parse_seat(value)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and result[0].isalpha()
        and isinstance(result[1], int)
        and result[1] > 0
    )


@given(st.one_of(st.text(), st.none()))
def test_total_price_no_crash(value):
    result = total_price(value)
    assert isinstance(result, float)
    assert result >= 0.0


@given(st.one_of(st.text(), st.none()))
def test_average_rating_no_crash(value):
    result = average_rating(value)
    assert isinstance(result, float)
    assert 0.0 <= result <= 5.0


def test_parse_seat_valid_and_invalid_examples():
    assert parse_seat(" h12 ") == ("H", 12)
    assert parse_seat("") is None
    assert parse_seat("H0") is None
    assert parse_seat("H-1") is None
    assert parse_seat(None) is None


def test_total_price_valid_and_invalid_examples():
    assert total_price("150,250,400") == 944.0
    assert total_price(" 150, 250 ") == 472.0
    assert total_price("150,,400") == 0.0
    assert total_price("one,two") == 0.0
    assert total_price(None) == 0.0


def test_average_rating_valid_and_invalid_examples():
    assert average_rating("4 5 3") == 4.0
    assert average_rating("0 5") == 2.5
    assert average_rating("4 five 3") == 0.0
    assert average_rating("6 3") == 0.0
    assert average_rating(None) == 0.0
