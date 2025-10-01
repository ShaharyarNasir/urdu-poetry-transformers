# src/ingest.py
import os
import glob
from pathlib import Path

import pandas as pd  # Move to top (style improvement)

RAW_DIR = Path("../data/raw")
OUT_CSV = Path("../data/raw_corpus.csv")


def ingest_from_txt(raw_dir=RAW_DIR, out_csv=OUT_CSV):
    rows = []

    for txtfile in glob.glob(str(raw_dir / "*.txt")):
        # expects filenames like ghalib_001.txt
        poet = Path(txtfile).stem.split("_")[0]
        with open(txtfile, "r", encoding="utf8") as fh:
            lines = [l.rstrip("\n") for l in fh]

        couplet_id = 0
        for i, line in enumerate(lines):
            if line.strip() == "":
                continue
            rows.append({
                "poet": poet,
                "poem_id": Path(txtfile).stem,
                "couplet_id": couplet_id,
                "line_text": line
            })
            if i % 2 == 1:
                couplet_id += 1

    # ✅ Ensure output directory exists
    os.makedirs(out_csv.parent, exist_ok=True)

    # Write CSV
    df = pd.DataFrame(rows)
    df.to_csv(out_csv, index=False)
    print(f"Wrote {len(df)} lines to {out_csv}")


if __name__ == "__main__":
    ingest_from_txt()
