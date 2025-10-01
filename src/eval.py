# src/eval.py
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

df_true = pd.read_csv("./data/annotated/pilot_annotations.csv")
# Assume predictions saved in file predictions.csv with columns poem_id,couplet_id,pred_meter
df_pred = pd.read_csv("./data/annotated/predictions.csv")

df = df_true.merge(df_pred, on=['poem_id', 'couplet_id'])
print(classification_report(df['meter'], df['pred_meter']))
cm = confusion_matrix(df['meter'], df['pred_meter'],
                      labels=sorted(df['meter'].unique()))
sns.heatmap(cm, annot=True, fmt="d")
plt.savefig("./docs/confusion_matrix.png")
