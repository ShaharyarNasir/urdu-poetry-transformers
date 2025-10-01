# src/normalize.py
import re
import unicodedata
import pandas as pd
from pathlib import Path

IN_CSV = Path("data/raw_corpus.csv")
OUT_CSV = Path("data/normalized/corpus_normalized.csv")
OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

REPLACEMENTS = {
    '\u0640': '',
    '\u06cc': '\u064a',
    '\u06c0': '\u06c1',
    '\u06d2': '\u064a',
}

DIACRITICS = [
    '\u064b', '\u064c', '\u064d', '\u064e', '\u064f', '\u0650', '\u0651', '\u0652'
]


def normalize_line(s):
    s = unicodedata.normalize('NFC', s)
    for k, v in REPLACEMENTS.items():
        s = s.replace(k, v)
    s = re.sub(r'\s+', ' ', s).strip()
    for d in DIACRITICS:
        s = s.replace(d, '')
    s = s.replace('إ', 'ا').replace('أ', 'ا').replace('آ', 'ا')
    return s


def run():
    df = pd.read_csv(IN_CSV)
    df['line_norm'] = df['line_text'].astype(str).apply(normalize_line)
    df.to_csv(OUT_CSV, index=False)
    print("✅ Normalized data saved to", OUT_CSV)


if __name__ == "__main__":
    run()
