import pytest

from src.countries import load_countries, parse_countries


def test_file_is_complete_and_unique():
    countries = load_countries()
    assert len(countries) == 193
    assert len({c["code"] for c in countries}) == 193
    assert len({c["name_ru"] for c in countries}) == 193
    assert all(len(c["code"]) == 2 for c in countries)


def test_known_capitals():
    by_name = {c["name_ru"]: c["capital_ru"] for c in load_countries()}
    assert by_name["Франция"] == "Париж"
    assert by_name["Австралия"] == "Канберра"
    assert by_name["Канада"] == "Оттава"
    assert by_name["Бразилия"] == "Бразилиа"


def test_bad_line_raises():
    with pytest.raises(ValueError):
        parse_countries("FR|Франция|Париж")
