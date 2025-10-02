import matplotlib.pyplot as plt
import numpy as np

# Data from paper
models = ['Rule-Based', 'BiLSTM', 'MiniLM+LoRA']
tasks = ['Meter', 'Rhyme', 'Sentiment']
f1_scores = np.array(
    [[0.66, 0.70, 0.68], [0.71, 0.82, 0.77], [0.80, 0.82, 0.77]])
errors = np.array([[0.02, 0.03, 0.02], [0.02, 0.02, 0.02],
                  [0.01, 0.01, 0.01]])  # Example std devs

# Plot
x = np.arange(len(tasks))
width = 0.25
fig, ax = plt.subplots(figsize=(8, 6))
for i, model in enumerate(models):
    ax.bar(x + i*width, f1_scores[i], width,
           label=model, capsize=5, yerr=errors[i])
ax.set_xticks(x + width, tasks)
ax.set_ylabel('Macro F1 Score')
ax.set_title('Model Performance Across Tasks')
ax.legend()
plt.savefig('figures/performance_comparison.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
