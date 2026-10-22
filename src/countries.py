import json
from pathlib import Path

import requests

API_URL = "https://restcountries.com/v3.1/all"
FIELDS = "name,capital,translations,flags,region,cca2,unMember"
CACHE_PATH = Path(__file__).resolve().parent.parent / "data" / "countries.json"


def fetch_raw() -> list[dict]:
    response = requests.get(API_URL, params={"fields": FIELDS}, timeout=20)
    response.raise_for_status()
    return response.json()


def normalize(raw: list[dict]) -> list[dict]:
    """Оставляем страны-члены ООН со столицей, берём только нужные поля."""
    result = []
    for item in raw:
        capitals = item.get("capital") or []
        if not capitals or not item.get("unMember"):
            continue
        name_en = (item.get("name") or {}).get("common", "")
        name_ru = ((item.get("translations") or {}).get("rus") or {}).get("common") or name_en
        result.append(
            {
                "code": item.get("cca2", ""),
                "name_en": name_en,
                "name_ru": name_ru,
                "capital_en": capitals[0],
                "region": item.get("region", ""),
                "flag_png": (item.get("flags") or {}).get("png", ""),
            }
        )
    result.sort(key=lambda c: c["name_en"])
    return result


def load_countries(refresh: bool = False) -> list[dict]:
    """Читаем кэш data/countries.json; если его нет (или refresh), качаем из API."""
    if CACHE_PATH.exists() and not refresh:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    countries = normalize(fetch_raw())
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(
        json.dumps(countries, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return countries
