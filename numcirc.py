import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

# Define the π multiples and their labels
multiples = [0, 1/6, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6, 1, 7/6, 5/4, 4/3, 3/2, 5/3, 7/4, 11/6, 2]
circle_labels = ['0', '$\\frac{\\pi}{6}$', '$\\frac{\\pi}{4}$', '$\\frac{\\pi}{3}$', '$\\frac{\\pi}{2}$', '$\\frac{2\\pi}{3}$', '$\\frac{3\\pi}{4}$', '$\\frac{5\\pi}{6}$', '$\\pi$', '$\\frac{7\\pi}{6}$', '$\\frac{5\\pi}{4}$', '$\\frac{4\\pi}{3}$', '$\\frac{3\\pi}{2}$', '$\\frac{5\\pi}{3}$', '$\\frac{7\\pi}{4}$', '$\\frac{11\\pi}{6}$', '$2\\pi$']
line_labels = [f'$\\frac{{{Fraction(multiple/2).limit_denominator().numerator}}}{{{Fraction(multiple/2).limit_denominator().denominator}}}$' if Fraction(multiple/2).limit_denominator().denominator != 1 and multiple != 0 else f'${Fraction(multiple/2).limit_denominator().numerator}$' for multiple in multiples]

# Create the number circle
theta = np.array(multiples) * np.pi
x_circle = np.cos(theta)
y_circle = np.sin(theta)

# Define colors for gradient
colors = plt.cm.viridis(np.linspace(0, 1, len(multiples)))

# Plotting
plt.figure(figsize=(8, 8))

# Plot the number circle
plt.plot(np.cos(np.linspace(0, 2*np.pi, 100)), np.sin(np.linspace(0, 2*np.pi, 100)), 'b-', linewidth=2)
plt.scatter(x_circle, y_circle, color='green')
for i, (x, y, label, color) in enumerate(zip(x_circle, y_circle, circle_labels, colors)):
    angle = theta[i]
    x_offset = -0.06 * np.cos(angle)
    y_offset = -0.06 * np.sin(angle)
    if label != '0': 
        plt.text(x + x_offset, y + y_offset, label, ha='center', va='center', color='green', fontsize=10, rotation=0, rotation_mode='anchor')
    else :
        plt.text(x + 0.04, y + y_offset, label, ha='center', va='center', color='green', fontsize=10, rotation=0, rotation_mode='anchor')
# Plot the number line
x_line = np.linspace(-0.7, 0.7, len(multiples))
y_line1 = np.zeros_like(x_line) + 0.2
y_line2 = np.zeros_like(x_line) - 0.2  # Second line
plt.plot(x_line, y_line1, 'b-', linewidth=2)
plt.scatter(x_line, y_line1, color='red')
for i, (x, y, label, color) in enumerate(zip(x_line, y_line1, line_labels, colors)):
    plt.text(x, y+0.08, label, ha='center', va='top', color='red')

# Plot the second line
plt.plot(x_line, y_line2, 'b-', linewidth=2)
plt.scatter(x_line, y_line2, color='green')
for i, (x, y, label, color) in enumerate(zip(x_line, y_line2, circle_labels, colors)):
    plt.text(x, y-0.09, label, ha='center', va='bottom', color='green')

# Add mapping arrows and f(x)=2πx
for x1, y1, x2, y2 in zip(x_line, y_line1, x_line, y_line2):
    plt.arrow(x1, y1, 0, y2-y1+0.05, head_width=0.02, head_length=0.05, fc='k', ec='k')

plt.text(0, 0.5, r'$f(x) = 2\pi x$', ha='center', fontsize=16)
plt.text(0, 0.4, r'$[0,1] \rightarrow [0,2\pi]$', ha='center', fontsize=16)
plt.text(0, -0.5, r'Removing 0,1 logical edges from model.', ha='center')
plt.title(r'Number line $\rightarrow$ Number Circle', fontsize=16)
plt.axis('equal')
plt.xticks([])
plt.yticks([])
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.savefig('line_to_circle.png')
plt.show()





