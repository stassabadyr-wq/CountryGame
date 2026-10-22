import random

from src.countries import load_countries


def main() -> None:
    countries = load_countries()
    print(f"Загружено стран: {len(countries)}")
    for c in random.sample(countries, 5):
        print(f"- {c['name_ru']} ({c['name_en']}): {c['capital_en']} [{c['region']}]")


if __name__ == "__main__":
    main()
