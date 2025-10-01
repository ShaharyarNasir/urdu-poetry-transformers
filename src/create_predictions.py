import pandas as pd
import os

# Load annotation CSV
df = pd.read_csv("data/annotated/pilot_annotations.csv", encoding="utf-8")

# Check for required columns
required_cols = {"poem_id", "couplet_id", "meter"}
if not required_cols.issubset(df.columns):
    raise ValueError(f"Missing columns. Found: {df.columns.tolist()}")

# Generate predictions (same as ground truth for now)
df_pred = df[["poem_id", "couplet_id"]].copy()
df_pred["pred_meter"] = df["meter"]

# Save clean CSV (comma-separated, UTF-8)
os.makedirs("data/annotated", exist_ok=True)
df_pred.to_csv("data/annotated/predictions.csv", index=False, encoding="utf-8")

print("✅ Clean predictions.csv created.")
