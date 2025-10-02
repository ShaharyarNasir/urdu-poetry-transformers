import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Example confusion matrix (replace with actual data)
cm = np.array([[10, 2, 0, 0, 0], [1, 15, 3, 0, 0], [
              0, 2, 12, 1, 0], [0, 0, 2, 10, 1], [0, 0, 0, 2, 8]])
labels = ['Despair', 'Melancholy', 'Neutral', 'Hope', 'Joy']

# Plot
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='viridis',
            xticklabels=labels, yticklabels=labels)
plt.title('Sentiment Classification Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.savefig('figures/sentiment_heatmap.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
