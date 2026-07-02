#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot the hydrogen-carbon isotope coordinate system for solar system bodies
and the interstellar object 3I/ATLAS.

Data points include:
- Sun, Venus, Earth, Moon, Mars, Jupiter, comet 67P, and 3I/ATLAS.
- X-axis: f_lock = ln(D/H / 1.5e-5)
- Y-axis: Y_C = ln((12C/13C) / 89)
- Error bars are shown for both axes where available.
"""

import numpy as np
import matplotlib.pyplot as plt

# ========================================================
# Data: (name, f_lock, f_lock_err, Y_C, Y_C_err)
# Errors are approximate; if not available, set to zero.
# ========================================================
data = [
    ("Sun",      0.336,  0.00,  0.049,  0.033),   # error from 3.0/89 ~0.034
    ("Venus",    2.523,  0.00, -0.008,  0.055),
    ("Earth",    2.342,  0.00,  0.009,  0.016),
    ("Moon",     2.303,  0.00,  0.019,  0.007),
    ("Mars",     1.649,  0.00,  0.012,  0.034),   # average error
    ("Jupiter",  0.405,  0.00,  0.010,  0.078),
    ("67P",      1.262,  0.00, -0.057,  0.048),   # 84/89 -> ln(0.944) = -0.057
    ("3I/ATLAS", 6.482,  0.00,  0.502,  0.158),   # 147/89, error ~ (191-123)/(2*89)=0.38? approximate
]

# Convert to arrays
names = [d[0] for d in data]
f_lock = np.array([d[1] for d in data])
f_err = np.array([d[2] for d in data])
Y_C = np.array([d[3] for d in data])
Y_err = np.array([d[4] for d in data])

# ========================================================
# Plot
# ========================================================
fig, ax = plt.subplots(figsize=(9, 6))

# Colors: solar system bodies (blue), 3I/ATLAS (red)
colors = ['blue' if n != '3I/ATLAS' else 'red' for n in names]
sizes = [80 if n != '3I/ATLAS' else 150 for n in names]
markers = ['o' if n != '3I/ATLAS' else '*' for n in names]

# Scatter with error bars
for i, name in enumerate(names):
    ax.errorbar(f_lock[i], Y_C[i],
                xerr=f_err[i], yerr=Y_err[i],
                fmt=markers[i], color=colors[i],
                markersize=10 if markers[i]=='*' else 8,
                capsize=4, elinewidth=1.5,
                label=name if name != '3I/ATLAS' else None)

# Special label for 3I/ATLAS
ax.scatter(f_lock[-1], Y_C[-1], color='red', s=150, marker='*', label='3I/ATLAS', zorder=5)

# Annotate points with names
for i, name in enumerate(names):
    ax.annotate(name, (f_lock[i], Y_C[i]),
                xytext=(5, 5), textcoords='offset points',
                fontsize=9, fontweight='bold')

# Draw the carbon benchmark line at Y_C = 0
ax.axhline(y=0, color='gray', linestyle='--', linewidth=1.5, alpha=0.7, label='Carbon benchmark (Y$_C \\approx$ 0)')

# Shade the solar system region (Y_C around 0)
ax.axhspan(-0.10, 0.10, color='gray', alpha=0.15)

# Labels and title
ax.set_xlabel('$f_{\\mathrm{lock}} = \\ln(\\mathrm{D/H} / 1.5\\times10^{-5})$', fontsize=14)
ax.set_ylabel('$Y_{\\mathrm{C}} = \\ln((^{12}\\mathrm{C}/^{13}\\mathrm{C}) / 89)$', fontsize=14)
ax.set_title('Hydrogen–Carbon Isotope Coordinate System', fontsize=16)

# Set limits
ax.set_xlim(-0.5, 7.5)
ax.set_ylim(-0.3, 0.8)

# Grid and legend
ax.grid(True, linestyle=':', alpha=0.4)
ax.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.savefig('carbon_manifold.png', dpi=300)
plt.show()

print("Figure saved as 'carbon_manifold.png'")