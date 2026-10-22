from src.countries import normalize


def test_normalize_filters_and_maps():
    raw = [
        {"name": {"common": "France"}, "capital": ["Paris"], "unMember": True,
         "translations": {"rus": {"common": "Франция"}}, "flags": {"png": "x.png"},
         "region": "Europe", "cca2": "FR"},
        {"name": {"common": "Nowhere"}, "capital": [], "unMember": True},
        {"name": {"common": "Taiwan"}, "capital": ["Taipei"], "unMember": False},
    ]
    result = normalize(raw)
    assert len(result) == 1
    assert result[0]["name_ru"] == "Франция"
    assert result[0]["capital_en"] == "Paris"
