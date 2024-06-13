import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from brokenaxes import brokenaxes
import math

# Parameters
n = 100
p = 0.5
l = 30  # lower bound
u = n - l  # upper bound

# Binomial distribution
x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)

# Calculate the cumulative probability for the range l to u heads
p_lu = binom.cdf(u, n, p) - binom.cdf(l-1, n, p)
t_lu = f'P({l} < X < {u}) = {p_lu:.10f}'

# Calculate the probabilities for X = 0,50,100
p_0 = binom.pmf(0, n, p)
m0 = np.floor(np.log10(np.abs(p_0)))
m = p_0 / 10**m0
t_0 = f'$P(X=0)={m:.2f}\\times10^{{{int(m0)}}}$'
p_50 = binom.pmf(50, n, p)
t_50 = f'P(X = 50) = {p_50:.10f}'
p_100 = binom.pmf(100, n, p)
m10 = np.floor(np.log10(np.abs(p_100)))
m = p_100 / 10**m10
t_100 = f'$P(X=100)={m:.2f}\\times10^{{{int(m10)}}}$'

# Calculate the probabilities for x=30 and x=70
p_30 = pmf[30]
p_70 = pmf[70]

# Calculate the mantissas and exponents
m30 = p_30 / 10**np.floor(np.log10(np.abs(p_30)))
m30_10 = np.floor(np.log10(np.abs(p_30)))

m70 = p_70 / 10**np.floor(np.log10(np.abs(p_70)))
m70_10 = np.floor(np.log10(np.abs(p_70)))

# Create the text strings
t_30 = f'$P(X=30)={m30:.2f}\\times10^{{{int(m30_10)}}}$'
t_70 = f'$P(X=70)={m70:.2f}\\times10^{{{int(m70_10)}}}$'

# Create the plot with a broken y-axis
fig = plt.figure(figsize=(10, 6))
bax = brokenaxes(xlims=((0, 100),), ylims=((0, 0.1), (0.99, 1)), hspace=0.1)
# Plot the binomial distribution
bax.bar(x, pmf, color='blue', edgecolor='blue', linewidth=0)
bax.bar(50, pmf[50], color='green', edgecolor='green', linewidth=0)
# Add 30, 50, 70, 100 to the plot# Add legend
bax.plot([0, 0], [0, 0.002], color='red', linestyle='--', label='0 Heads')
bax.text(1, 0.001, t_0, ha='left', va='bottom', color='red')
bax.plot([l, l], [0, 0.002], color='orange', linestyle='--', label=f'{l} Heads')
bax.text(35, 0.007, t_30, ha='right', va='bottom', color='orange')
bax.plot([50, 50], [0, pmf[50]], color='green', linestyle='--', label='50 Heads')
bax.text(50, 0.08, t_50, ha='center', va='bottom', color='green')
bax.plot([u, u], [0, 0.002], color='orange', linestyle='--', label=f'{u} Heads')
bax.text(65, 0.007, t_70, ha='left', va='bottom', color='orange')
bax.plot([100, 100], [0, 0.002], color='red', linestyle='--', label='100 Heads')
bax.text(99, 0.001, t_100, ha='right', va='bottom', color='red')

bax.legend()
# Add cumulative probability text to the plot
bax.text(50, 0.09, t_lu, fontsize=12, ha='center', color='grey', bbox=dict(facecolor='white', alpha=0.5))

# Set x-ticks to go in steps of 10
bax.set_xticks(np.arange(0, n+1, 10))

# Title and labels
fig.suptitle(r'Binomial Distribution: $X \sim B(100, 0.5)$')
bax.set_xlabel('Number of Heads')
bax.set_ylabel('Probability')

# Save the plot
plt.savefig('binomial.png')
plt.show()
