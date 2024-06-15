import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle

def draw_number_circle_and_line(ax):
    multiples = [0, 1/6, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6, 1, 7/6, 5/4, 4/3, 3/2, 5/3, 7/4, 11/6, 2]
    circle_labels = ['0', '$\\frac{\\pi}{6}$', '$\\frac{\\pi}{4}$', '$\\frac{\\pi}{3}$', '$\\frac{\\pi}{2}$', '$\\frac{2\\pi}{3}$', '$\\frac{3\\pi}{4}$', '$\\frac{5\\pi}{6}$', '$\\pi$', '$\\frac{7\\pi}{6}$', '$\\frac{5\\pi}{4}$', '$\\frac{4\\pi}{3}$', '$\\frac{3\\pi}{2}$', '$\\frac{5\\pi}{3}$', '$\\frac{7\\pi}{4}$', '$\\frac{11\\pi}{6}$', '$2\\pi$']
    line_labels = [f'$\\frac{{{Fraction(multiple/2).limit_denominator().numerator}}}{{{Fraction(multiple/2).limit_denominator().denominator}}}$' if Fraction(multiple/2).limit_denominator().denominator != 1 and multiple != 0 else f'${Fraction(multiple/2).limit_denominator().numerator}$' for multiple in multiples]

    theta = np.array(multiples) * np.pi
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)

    ax.plot(np.cos(np.linspace(0, 2*np.pi, 100)), np.sin(np.linspace(0, 2*np.pi, 100)), 'b-', linewidth=2)
    ax.scatter(x_circle, y_circle, color='blue')
    for i, (x, y, label) in enumerate(zip(x_circle, y_circle, circle_labels)):
        angle = theta[i]
        x_offset = -0.06 * np.cos(angle)
        y_offset = -0.06 * np.sin(angle)
        if label != '0': 
            ax.text(x + x_offset, y + y_offset, label, ha='center', va='center', color='blue', fontsize=10, rotation=0, rotation_mode='anchor')
        else:
            ax.text(x + 0.04, y + y_offset, label, ha='center', va='center', color='blue', fontsize=10, rotation=0, rotation_mode='anchor')
    
    x_line = np.linspace(-0.7, 0.7, len(multiples))
    y_line1 = np.zeros_like(x_line) + 0.2
    y_line2 = np.zeros_like(x_line) - 0.2
    ax.plot(x_line, y_line1, 'k-', linewidth=2)
    ax.scatter(x_line, y_line1, color='black')
    for i, (x, y, label) in enumerate(zip(x_line, y_line1, line_labels)):
        ax.text(x, y+0.12, label, ha='center', va='top', color='black')

    ax.plot(x_line, y_line2, 'b-', linewidth=2)
    ax.scatter(x_line, y_line2, color='blue')
    for i, (x, y, label) in enumerate(zip(x_line, y_line2, circle_labels)):
        ax.text(x, y-0.13, label, ha='center', va='bottom', color='blue')

    for x1, y1, x2, y2 in zip(x_line, y_line1, x_line, y_line2):
        ax.arrow(x1, y1, 0, y2-y1+0.05, head_width=0.02, head_length=0.05, fc='k', ec='k')
    
    ax.text(0, 0.6, r'Number Line $\rightarrow$', ha='right', fontsize=12)
    ax.text(0, 0.6, ' Number Circle', color='blue', ha='left', fontsize=12)
    ax.text(0, 0.5, r'$f(x) =$', ha='right', fontsize=12)
    ax.text(0, 0.5, r'$ 2\pi x$', color='blue',ha='left', fontsize=12)
    ax.text(0, 0.4, r'$[0,1] \rightarrow$', ha='right', fontsize=12)
    ax.text(0, 0.4, r'$ [0,2\pi]$', color='blue', ha='left', fontsize=12)
    ax.text(0, -0.5, r'Removing 0,1 logical edges from models.', ha='center')
    ax.axis('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(True)

def draw_3r_relativistic_sphere(ax):
    radius = 1
    theta = np.linspace(0, 2 * np.pi, 100)

    x_force = radius * np.cos(theta)
    y_force = radius * np.sin(theta)
    z_force = np.zeros_like(theta)

    x_time = radius * np.sin(theta)
    y_time = np.zeros_like(theta)
    z_time = radius * np.cos(theta)

    x_distance = np.zeros_like(theta)
    y_distance = radius * np.sin(theta)
    z_distance = radius * np.cos(theta)

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='b', alpha=0.1)

    ax.plot(x_time, y_time, z_time, color='red', label='x (time)')
    ax.plot(x_distance, y_distance, z_distance, color='green', label='y (distance)')
    ax.plot(x_force, y_force, z_force, color='blue', label='z (force) i')

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    ax.legend()

fig = plt.figure(figsize=(14, 7))
fig.suptitle('3R Relativistic Sphere', fontsize=16)

ax1 = fig.add_subplot(121)
draw_number_circle_and_line(ax1)
for spine in ax1.spines.values():
    spine.set_visible(False)

ax2 = fig.add_subplot(122, projection='3d')
draw_3r_relativistic_sphere(ax2)

# Add annotation between the diagrams
fig.text(0.5, 0.5, r'$x, y, z \Rightarrow$', ha='center', va='center', fontsize=16, color='black')

plt.tight_layout(rect=[0, 0, 1, 0.95])

# Add a border around the entire figure below the title
rect = Rectangle((0.02, 0.02), 0.96, 0.92, fill=False, color="black", lw=2, zorder=10,
                 transform=fig.transFigure, figure=fig)
fig.patches.append(rect)

plt.savefig('3Rsphere.png')
plt.show()





