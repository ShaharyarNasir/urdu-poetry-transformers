import matplotlib.pyplot as plt

# Example F1 scores (replace with actual data)
epochs = range(1, 11)
phonetic = [0.68, 0.70, 0.72, 0.72, 0.72, 0.72, 0.72, 0.72, 0.72, 0.72]
mixed = [0.68, 0.70, 0.73, 0.75, 0.76, 0.77, 0.77, 0.77, 0.77, 0.77]
raw = [0.68, 0.70, 0.73, 0.75, 0.77, 0.78, 0.79, 0.80, 0.80, 0.80]

# Plot
plt.figure(figsize=(8, 6))
plt.plot(epochs, phonetic, label='Phonetic Only', linestyle='--')
plt.plot(epochs, mixed, label='Mixed', linestyle='-.')
plt.plot(epochs, raw, label='Raw Orthography', linestyle='-')
plt.xlabel('Epoch')
plt.ylabel('Macro F1 Score')
plt.title('Curriculum Learning Impact on Meter Detection')
plt.legend()
plt.grid(True)
plt.savefig('figures/curriculum_progression.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
