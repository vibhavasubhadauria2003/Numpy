import matplotlib.pyplot as plt

# Define vector
v = [3, 2]

# Plot arrow from origin
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue')

# Mark the tip with red dot
plt.plot(v[0], v[1], 'ro')

# Add grid, labels, title
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Vector Plot')

plt.show()