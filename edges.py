import matplotlib.pyplot as plt

# Plot edges and discreteness
plt.figure(figsize=(6, 4))
plt.plot([0, 1], [0, 0], 'k-', linewidth=2)
plt.scatter([0, 0.5, 1], [0, 0, 0], color='blue')
plt.text(0, 0.05, '0', ha='center')
plt.text(1, 0.05, '1', ha='center')
plt.text(0.5, 0.05, '0.5', ha='center')
plt.title('Edges and Discreteness')
plt.xlabel('Logical Model')
plt.yticks([])
plt.savefig('edges.png')
plt.show()
