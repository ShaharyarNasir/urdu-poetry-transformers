# src/train.py
from sklearn.metrics import f1_score, accuracy_score
from datasets import load_dataset, Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import pandas as pd
import numpy as np

MODEL_NAME = "distilbert-base-multilingual-cased"
TOKENIZER = MODEL_NAME
OUT_DIR = "./models/distil_urdu_meter"

# Load annotated pilot
df = pd.read_csv("./data/annotated/pilot_annotations.csv")
df = df.dropna(subset=['meter'])  # keep labeled rows

print("Number of labeled rows:", len(df))
if len(df) < 2:
    raise ValueError(
        "Not enough labeled data to train/test split. Please add more annotations.")

# Map labels to ints
labels = {lab: i for i, lab in enumerate(sorted(df['meter'].unique()))}
df['label'] = df['meter'].map(labels)

# Prepare dataset with one line (line1 + line2)
df['text'] = df['line1'].fillna('') + " [SEP] " + df['line2'].fillna('')
ds = Dataset.from_pandas(df[['text', 'label']])

# Tokenization
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER)


def tokenize(batch):
    return tokenizer(batch['text'], truncation=True, padding='max_length', max_length=128)


ds = ds.map(tokenize, batched=True)
ds.set_format(type='torch', columns=['input_ids', 'attention_mask', 'label'])

# Train-test split
if len(ds) >= 10:
    ds = ds.train_test_split(test_size=0.2)
    train_ds = ds['train']
    eval_ds = ds['test']
else:
    print("Dataset too small to split, using entire data as training, no evaluation.")
    train_ds = ds
    eval_ds = None

# Load model
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME, num_labels=len(labels))

# Training arguments
training_args = TrainingArguments(
    output_dir=OUT_DIR,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
    fp16=False,
    push_to_hub=False
)

# Metrics


def compute_metrics(pred):
    labels = pred.label_ids
    preds = np.argmax(pred.predictions, axis=1)
    return {
        "accuracy": accuracy_score(labels, preds),
        "f1": f1_score(labels, preds, average='macro')
    }


# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=eval_ds if eval_ds else None,
    compute_metrics=compute_metrics if eval_ds else None
)

trainer.train()
trainer.save_model(OUT_DIR)
