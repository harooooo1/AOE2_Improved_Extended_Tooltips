"""Consistency checker for the tooltip language files.

Usage (from the repo root):
    python tools/validate.py          # check everything, exit code 1 on problems
    python tools/validate.py --sync   # first copy EN -> EN-copy languages and ES -> MX, then check

Checks:
  1. Every file parses (ID "text" lines), has no duplicate IDs, uses UTF-8 BOM + CRLF.
  2. DE/ES/IT contain exactly the same IDs as EN, in the same order.
  3. Every entry uses the same formatting tags (<b>, <GREY>, <cost>, \\n, ...) in the same order as EN.
  4. Every entry contains the same numbers as EN (catches stats that were updated in EN only).
  5. EN-copy languages are identical to EN, MX is identical to ES.

Known, intentional number differences (e.g. "30k" vs "30.000") are listed in
tools/number_exceptions.txt. An exception only applies while the difference stays exactly
the same, so a later EN stat change in that entry is still reported.
"""
import collections
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "resources", "{}", "strings", "key-value", "key-value-modded-strings-utf8.txt")
EXCEPTIONS = os.path.join(ROOT, "tools", "number_exceptions.txt")

TRANSLATED = ["de", "es", "it"]
EN_COPIES = ["br", "fr", "hi", "jp", "ko", "ms", "pl", "ru", "tr", "tw", "vi", "zh"]
ES_COPIES = ["mx"]

ENTRY = re.compile(r'^(\d+)\s+"([^"]*)"\s*(//.*)?$')
TAG = re.compile(r"<[^>]+>|\\n")
NUMBER = re.compile(r"\d+(?:[.,]\d+)?")

errors = []


def error(msg):
    errors.append(msg)


def load(lang):
    raw = open(PATH.format(lang), "rb").read()
    if not raw.startswith(b"\xef\xbb\xbf"):
        error(f"{lang}: missing UTF-8 BOM")
    text = raw.decode("utf-8-sig")
    if "\n" in text.replace("\r\n", ""):
        error(f"{lang}: has LF-only line endings (expected CRLF)")
    entries = collections.OrderedDict()
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("//"):
            continue
        m = ENTRY.match(line)
        if not m:
            error(f"{lang}: line {n} cannot be parsed: {line[:80]}")
            continue
        if m[1] in entries:
            error(f"{lang}: duplicate ID {m[1]} (line {n})")
        entries[m[1]] = m[2]
    return entries


def numbers(text):
    return collections.Counter(x.replace(",", ".") for x in NUMBER.findall(text))


def number_signature(en_text, tr_text):
    a, b = numbers(en_text), numbers(tr_text)
    fmt = lambda c: ",".join(sorted(c.elements()))
    return f"EN:{fmt(a - b)} TR:{fmt(b - a)}"


def load_exceptions():
    result = set()
    if os.path.exists(EXCEPTIONS):
        for line in open(EXCEPTIONS, encoding="utf-8"):
            line = line.split("#", 1)[0].strip()
            if line:
                lang, id_, sig = line.split(None, 2)
                result.add((lang, id_, sig))
    return result


def sync():
    en, es = PATH.format("en"), PATH.format("es")
    for lang in EN_COPIES:
        shutil.copyfile(en, PATH.format(lang))
    for lang in ES_COPIES:
        shutil.copyfile(es, PATH.format(lang))
    print(f"Synced EN -> {', '.join(EN_COPIES)}; ES -> {', '.join(ES_COPIES)}")


def main():
    if "--sync" in sys.argv:
        sync()

    exceptions = load_exceptions()
    en = load("en")
    for lang in TRANSLATED:
        tr = load(lang)
        missing = [k for k in en if k not in tr]
        extra = [k for k in tr if k not in en]
        if missing:
            error(f"{lang}: missing IDs {missing}")
        if extra:
            error(f"{lang}: IDs not in EN {extra}")
        if not missing and not extra and list(tr) != list(en):
            first = next(i for i, (a, b) in enumerate(zip(en, tr)) if a != b)
            error(f"{lang}: entry order differs from EN (first difference at EN ID {list(en)[first]})")
        for k in en:
            if k not in tr:
                continue
            if TAG.findall(en[k]) != TAG.findall(tr[k]):
                error(f"{lang} {k}: tags differ from EN")
            if numbers(en[k]) != numbers(tr[k]):
                sig = number_signature(en[k], tr[k])
                if (lang, k, sig) not in exceptions:
                    error(f"{lang} {k}: numbers differ from EN   ->  {lang} {k} {sig}")

    for lang in EN_COPIES:
        if open(PATH.format(lang), "rb").read() != open(PATH.format("en"), "rb").read():
            error(f"{lang}: not identical to EN (run with --sync)")
    for lang in ES_COPIES:
        if open(PATH.format(lang), "rb").read() != open(PATH.format("es"), "rb").read():
            error(f"{lang}: not identical to ES (run with --sync)")

    for e in errors:
        print(e)
    if errors:
        print(f"\nFAILED: {len(errors)} problem(s)")
        return 1
    print(f"OK: {len(en)} entries consistent across EN/{'/'.join(x.upper() for x in TRANSLATED)}, all copies in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
