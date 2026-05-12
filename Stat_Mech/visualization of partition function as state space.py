import numpy as np
import matplotlib.pyplot as plt

# Font Preferences
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
plt.rcParams['mathtext.fontset'] = 'stix'

# Create a 10x10 grid of states
grid_size = 10
energies = np.arange(1, grid_size ** 2 + 1).reshape(grid_size, grid_size)

# Temperatures representing different "Degrees of Freedom"
temps = [2, 10, 50]
titles = ['Cold', 'Moderate', 'Hot']
cmaps = ['Reds', 'YlOrBr', 'Blues']

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

for i, T in enumerate(temps):
    beta = 1.0 / T
    # Calculate weights: e^(-beta * E)
    weights = np.exp(-beta * energies)
    Z = np.sum(weights)

    # Plot heatmap
    im = axes[i].imshow(weights, cmap=cmaps[i], origin='upper')
    axes[i].set_title(f'{titles[i]}\n$Z \\approx {Z:.2f}$', fontsize=16)
    axes[i].axis('off')  # Hide grid lines for the "pure math" look
    fig.colorbar(im, ax=axes[i], fraction=0.046, pad=0.04)

plt.suptitle('Visualizing the Partition Function',
             fontsize=20, fontweight='bold', y=1.05)
plt.tight_layout()
plt.savefig('partition_function_grid.png')

#PL
