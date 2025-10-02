import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np

import os

# Ensure figures directory exists
os.makedirs("figures", exist_ok=True)

# Simulated embeddings (replace with actual MiniLM embeddings, shape: 250x384)
np.random.seed(42)
embeddings = np.random.rand(250, 384)
labels = np.array(['Ghalib']*100 + ['Mir']*60 + ['Iqbal']*50 + ['Faiz']*40)

# Compute t-SNE
tsne = TSNE(n_components=2, random_state=42)
tsne_results = tsne.fit_transform(embeddings)

# Plot
plt.figure(figsize=(8, 6))
colors = {'Ghalib': 'red', 'Mir': 'blue', 'Iqbal': 'green', 'Faiz': 'yellow'}
for poet in colors:
    mask = labels == poet
    plt.scatter(tsne_results[mask, 0], tsne_results[mask,
                1], c=colors[poet], label=poet, alpha=0.6)
plt.legend()
plt.title('t-SNE Visualization of Verse Embeddings')
plt.xlabel('t-SNE Dimension 1')
plt.ylabel('t-SNE Dimension 2')

plt.savefig("figures/tsne_clusters.pdf", format="pdf", dpi=300, bbox_inches="tight")
plt.close()
