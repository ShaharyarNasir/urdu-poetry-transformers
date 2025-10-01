# src/annotation_ui.py
import streamlit as st
import pandas as pd
from pathlib import Path
import random

DATA_CSV = "./data/normalized/corpus_normalized.csv"
ANNOT_OUT = "./data/annotated/pilot_annotations.csv"
Path("./data/annotated").mkdir(parents=True, exist_ok=True)


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_CSV)
    # build couplets: group by poem_id and couplet_id
    df2 = df[['poem_id', 'couplet_id', 'line_text', 'line_norm']].copy()
    return df2


df = load_data()
# sample random couplets for annotation
couplets = df.groupby(['poem_id', 'couplet_id']).agg({
    'line_text': lambda s: list(s),
    'line_norm': lambda s: list(s)
}).reset_index()

idx = st.sidebar.number_input("start index", 0, len(couplets)-1, 0)
sample = couplets.iloc[idx]
st.header(f"Poem: {sample['poem_id']}  |  couplet: {sample['couplet_id']}")
lines = sample['line_norm']
for i, l in enumerate(lines):
    st.write(f"Misra {i+1}: {l}")

# annotation fields
meter = st.selectbox("Meter (coarse)", ["unknown", "short", "long", "other"])
syllpattern = st.text_input("Syllable pattern (H/L..)", "")
radif = st.text_input("Radif (if any)", "")
qaafiya = st.text_input("Qaafiya (if any)", "")
metaphor = st.radio("Metaphor?", ["no", "yes"])
met_domain = st.selectbox("Metaphor domain", [
                          "", "wine", "night", "rose", "separation", "divine", "beloved", "journey", "sleep", "intoxication"])
affect = st.selectbox("Affect", [
                      "longing", "ecstasy", "resignation", "irony", "devotion", "anger", "other"])
comment = st.text_area("Comment (edge cases)")

if st.button("Save annotation"):
    row = {
        "poem_id": sample['poem_id'],
        "couplet_id": sample['couplet_id'],
        "line1": lines[0] if len(lines) > 0 else "",
        "line2": lines[1] if len(lines) > 1 else "",
        "meter": meter,
        "syllpattern": syllpattern,
        "radif": radif,
        "qaafiya": qaafiya,
        "metaphor": metaphor,
        "met_domain": met_domain,
        "affect": affect,
        "comment": comment
    }
    outdf = pd.DataFrame([row])
    if Path(ANNOT_OUT).exists():
        outdf.to_csv(ANNOT_OUT, index=False, mode='a', header=False)
    else:
        outdf.to_csv(ANNOT_OUT, index=False)
    st.success("Saved.")
