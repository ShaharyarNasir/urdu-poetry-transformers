import sentencepiece as spm
from pathlib import Path
import pandas as pd

df = pd.read_csv("./data/normalized/corpus_normalized.csv")
text_file = "../data/normalized/all_lines.txt"
Path(text_file).write_text(
    "\n".join(df['line_norm'].astype(str).tolist()), encoding='utf8')

model_dir = Path("../models")
# create models folder if not exist
model_dir.mkdir(parents=True, exist_ok=True)

spm.SentencePieceTrainer.train(
    input=text_file,
    model_prefix=str(model_dir / 'spm_urdu'),
    vocab_size=100,  # or another value that fits your data
    character_coverage=0.9995,
    model_type='bpe'
)
print("Tokenizer trained:", model_dir / "spm_urdu.model")
