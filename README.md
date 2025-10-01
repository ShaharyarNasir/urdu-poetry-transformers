````markdown
# Urdu Poetry Transformers

This repository provides a complete pipeline for building compact transformer models to analyze classical Urdu poetry. The pipeline includes:

- Data ingestion from raw text files  
- Text normalization and cleaning  
- Training a SentencePiece tokenizer on normalized data  
- Annotation UI for linguistic features (meter, rhyme, metaphor, affect)  
- Training compact transformer classifiers on annotated data  
- Evaluation and error analysis  
- Starter outline and text for academic publication  

---

## Project Structure

```text
urdu-poetry-transformers/
├─ data/
│  ├─ raw/                # Raw Urdu poetry text files (.txt)
│  ├─ normalized/         # Normalized corpus CSV & text files
│  └─ annotated/          # Annotation CSV outputs
├─ models/                # Trained tokenizers and models (ignored by git)
├─ notebooks/             # Jupyter notebooks (optional)
├─ src/
│  ├─ ingest.py           # Ingest raw text files into CSV
│  ├─ normalize.py        # Normalize text (Unicode fixes, diacritics)
│  ├─ train_tokenizer.py  # Train SentencePiece tokenizer on normalized data
│  ├─ annotation_ui.py    # Streamlit UI for annotation
│  ├─ train.py            # Train compact transformer on annotated labels
│  └─ eval.py             # Evaluate model predictions
├─ docs/                  # Documentation, generated figures
├─ paper/                 # Manuscript drafts and annotation guidelines
├─ README.md              # This file
├─ requirements.txt       # Python dependencies
└─ .gitignore             # Git ignore config
````

---

## Setup Instructions

### 1) Clone the repo and create virtual environment

```bash
git clone <repo-url>
cd urdu-poetry-transformers

# Create Python virtual environment (Python 3.9+ required)
python -m venv venv

# Activate virtual environment
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 2) Prepare raw data

Place your Urdu poetry text files (`.txt`) inside `data/raw/`.

* Filenames should be like `ghalib_001.txt`, `faiz_01.txt` to help identify poet and poem.
* Each file should contain lines of poetry (one per line).

---

### 3) Ingest raw texts

Run the ingestion script to convert raw `.txt` files into a CSV:

```bash
python src/ingest.py
```

* This creates `data/raw_corpus.csv` with columns: `poet`, `poem_id`, `couplet_id`, `line_text`.

---

### 4) Normalize text

Clean and normalize the corpus with Unicode fixes and diacritics removal:

```bash
python src/normalize.py
```

* Produces `data/normalized/corpus_normalized.csv` with a new `line_norm` column.

---

### 5) Train SentencePiece tokenizer

Train a subword tokenizer on normalized lines:

```bash
mkdir -p models
python src/train_tokenizer.py
```

* Outputs `models/spm_urdu.model` and `models/spm_urdu.vocab`.

---

### 6) Annotate data with Streamlit UI

Start the annotation interface to label poetic features:

```bash
streamlit run src/annotation_ui.py
```

* Annotators can browse couplets, assign labels (meter, rhyme, metaphor, affect), and save.
* Annotations saved to `data/annotated/pilot_annotations.csv`.

---

**Note:** If you see
`Not enough labeled data to train/test split. Please add more annotations.`
→ run `Create_pilot_annotation.py` from the root folder.

---

### 7) Train a compact transformer classifier

Fine-tune a DistilBERT-based model on your annotations:

```bash
python src/train.py
```

* Trains a classifier for meter (or other features, modify labels accordingly).
* Saves model to `models/distil_urdu_meter`.

---

### 8) Evaluate model predictions

After generating predictions, run evaluation:

```bash
python src/eval.py
```

* Produces classification reports and confusion matrices saved in `docs/`.

---

## Additional Notes

* **Licensing:** Add `source_url` and `license` columns in your CSV if applicable.
* **Diacritics:** Normalization strips most diacritics to reduce sparsity.
* **Model choice:** Replace `distilbert-base-multilingual-cased` in `train.py` with Urdu-specific models if available.
* **Annotation:** Start with 100–300 couplets for a pilot annotation.
* **Improvements:** Add LoRA, distillation, or multi-task models later.

---

## Paper and Guidelines

* Annotation guidelines draft: `paper/annotation_guidelines.md`
* Manuscript starter: `paper/draft.md`

---

## Contact / Contributing

Please open issues or pull requests for bug fixes, new features, or help.

---

Happy Urdu poetry modeling! 🌹📜

```
```
