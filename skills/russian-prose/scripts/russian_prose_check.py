#!/usr/bin/env python3
"""Flag mechanical slop patterns in Russian prose of Markdown files.

Rule ids match the numbered patterns in this skill's SKILL.md.
Usage (from the skill directory): python3 scripts/russian_prose_check.py FILE.md [FILE.md ...]
Checks Markdown files only.
Exit code 1 when anything is found.
"""

import re
import sys
from dataclasses import dataclass

CYR = "а-яёА-ЯЁ"


@dataclass(frozen=True)
class Rule:
    id: int
    name: str
    pattern: re.Pattern
    min_hits: int = 1
    show_group: int = 0


def rx(p: str) -> re.Pattern:
    return re.compile(p, re.IGNORECASE)


RULES = [
    Rule(1, "тире", rx(rf"—|–|[{CYR}»)] - [{CYR}«(]")),
    Rule(2, "телеграф: символ вместо слов", rx(rf"[{CYR}»)\d] ?(\+|→|=|≠|×|←|⇒) ?[{CYR}«(]"), show_group=1),
    Rule(3, "список через слэш", rx(rf"[{CYR}»)] / [{CYR}«(]")),
    Rule(4, "латиница в русской фразе", re.compile(r"(?<![\w.-])[a-z][a-z-]{2,}(?![\w.-])"), min_hits=2),
    Rule(5, "калька", rx(
        r"\bреальн(ая|ый|ое|ые) (причин|контент|проблем|смысл)|\bздесь фокус|\bфокус —|"
        r"\bимеет смысл|\bиметь смысл|(?-i:\b[Оо]к\b)(?!-)|\bна основе того,|\bв порядке, чтобы|"
        rf"\bделает [{CYR} ]+ (легче|проще)|\bпо сути\b|\bиграет роль|\bв конце дня\b"
    )),
    Rule(6, "канцелярит", rx(
        r"\bявля(ется|ются|ющ)|\bосуществ|\bпроизвод(ить|ится|ит|ят) (провер|обновл|настрой)|"
        r"\bданн(ый|ая|ое|ого|ой|ом|ому|ую)\b|\bвышеуказ|\bв рамках\b|\bс целью\b|"
        r"\bважно отметить|\bстоит (подчеркнуть|отметить)|\bв современном мире"
    )),
    Rule(7, "больше одного выделения жирным", re.compile(r"\*\*[^*\n]+\*\*"), min_hits=2),
    Rule(8, "больше одного пояснения в скобках", re.compile(rf"\([^()\n]*[{CYR}][^()\n]*\)"), min_hits=2),
]

STRIP = [
    (re.compile(r"`[^`\n]*`"), "Код"),
    (re.compile(r"!\[\[[^\]]*\]\]"), " "),
    (re.compile(r"\[\[[^\]|]*\|([^\]]*)\]\]"), r"\1"),
    (re.compile(r"\[\[[^\]]*\]\]"), "Ссылка"),
    (re.compile(r"\[([^\]]*)\]\([^)]*\)"), r"\1"),
    (re.compile(r"https?://\S+"), " "),
    (re.compile(r"\b[\w-]+(\.[\w-]+)+(/\S*)?"), "Адрес"),
    (re.compile(r"«[^»\n]*»"), "«Цитата»"),
    (re.compile(r'"[^"\n]*"'), "«Цитата»"),
    (re.compile(r"^\s*(>\s*)*(\[![^\]]*\]\S*)?"), ""),
    (re.compile(r"^\s*([-*+]|\d+[.)])\s+(\[[ xX]\]\s+)?"), ""),
]

HAS_CYR = re.compile(f"[{CYR}]")


def prose_lines(text: str):
    lines = text.splitlines()
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1
    fence = None
    for n in range(i, len(lines)):
        s = lines[n].strip()
        if fence:
            if s.startswith(fence):
                fence = None
            continue
        m = re.match(r"(`{3,}|~{3,})", s)
        if m:
            fence = m.group(1)
            continue
        if not s or s.startswith(("#", "|", "<!--", "%%")) or re.fullmatch(r"[-*_]{3,}", s):
            continue
        clean = lines[n]
        for pat, rep in STRIP:
            clean = pat.sub(rep, clean)
        if HAS_CYR.search(clean):
            yield n + 1, clean


def check(path: str):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for lineno, line in prose_lines(text):
        for rule in RULES:
            hits = [m.group(rule.show_group).strip() for m in rule.pattern.finditer(line)]
            if len(hits) >= rule.min_hits:
                yield lineno, rule, hits, line.strip()


def main(paths):
    total = 0
    for path in paths:
        for lineno, rule, hits, line in check(path):
            total += 1
            shown = ", ".join(dict.fromkeys(hits))
            print(f"{path}:{lineno}: [{rule.id}] {rule.name} ({shown}): {line[:160]}")
    if total:
        print(f"\n{total} строк с находками", file=sys.stderr)
    return 1 if total else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
