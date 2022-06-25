"""Export an equation as an image file."""
import matplotlib.pyplot as plt
import seaborn as sns
import os


# %% Plotting parameters

DPI = 200
FONTSIZE = "medium"
FORMAT = "png"
GRAPHICS_DIR = "graphics"

sns.set_theme(style="whitegrid", font="monospace",
              context="paper")


# %% Input equation
eq_name = "J"
latex_eq = r"J = \frac{V_{\infty}}{n\cdot D}"

eq_string = r'$\mathdefault{' + latex_eq + r'}$'


# %% Generate and save figure

fig = plt.figure(dpi=DPI)
fig.tight_layout()
fig.text(0, 0, eq_string)
fig.savefig(os.path.join(GRAPHICS_DIR, eq_name + '.' + FORMAT), format=FORMAT,
            transparent=True, bbox_inches="tight", pad_inches=0)


# %% Display equation

disp_fig, ax = plt.subplots(dpi=DPI, figsize=(1e-6, 1e-6))
ax.axis("off")
ax.text(0.5, 0.5, eq_string, ha="center", va="center", fontsize=FONTSIZE)
