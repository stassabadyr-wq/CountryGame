from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "countries.txt"


def parse_countries(text: str) -> list[dict]:
    """Строки вида КОД|Страна|Столица|Регион. Пустые строки пропускаем."""
    result = []
    for number, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 4 or not all(parts):
            raise ValueError(f"Строка {number} в countries.txt заполнена неверно: {line!r}")
        code, name, capital, region = parts
        result.append(
            {"code": code, "name_ru": name, "capital_ru": capital, "region": region}
        )
    return result


def load_countries(path: Path = DATA_PATH) -> list[dict]:
    return parse_countries(path.read_text(encoding="utf-8-sig"))
