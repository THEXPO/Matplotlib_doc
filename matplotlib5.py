import matplotlib.pyplot as plt
import numpy as np

#Subplot in matplotlib

# Sample data
x = np.linspace(0, 10, 100)   # 100 points from 0 to 10
y1 = np.sin(x)                # sine curve
y2 = np.cos(x)                # cosine curve
y3 = np.exp(0.1 * x)          # exponential growth
y4 = np.random.randn(100)     # random values

# Create 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1: Line plot (sine)
axs[0,0].plot(x, y1, 'b-')
axs[0,0].set_title("Sine Wave")

# Plot 2: Line plot (cosine)
axs[0,1].plot(x, y2, 'r--')
axs[0,1].set_title("Cosine Wave")

# Plot 3: Exponential curve
axs[1,0].plot(x, y3, 'g-.')
axs[1,0].set_title("Exponential Growth")

# Plot 4: Histogram of random data
axs[1,1].hist(y4, bins=20, color='purple', edgecolor='black')
axs[1,1].set_title("Random Data Histogram")

# Adjust layout to avoid overlap
plt.tight_layout()
plt.show()
