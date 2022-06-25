"""Export an equation as an image file."""
import matplotlib.pyplot as plt
import seaborn as sns
import os


# %% Plotting parameters

DPI = 1200
FONTSIZE = "medium"
GRAPHICS_DIR = "graphics"

sns.set_theme(style="whitegrid", font="monospace",
              context="paper")


# %% Input equation
eq_name = "sizing_eq"
latex_eq = r"\frac{W_{bat}}{W_{0}} = \frac{1}{W_{0}\cdot e_{bat}\cdot\%C_{bat}}\sum E_{i} =  \frac{1}{e_{bat}\cdot \%C_{bat}}\sum\left(\frac{P}{W}\frac{\Delta r}{V}\right)_{i}"


# %% Process string and save figure

eq_string = r'$\mathdefault{' + latex_eq + r'}$'
fig, ax = plt.subplots(dpi=DPI, figsize=(0.000001, 0.000001))
ax.axis("off")
ax.text(0.5, 0.5, eq_string, ha="center", va="center", fontsize=FONTSIZE)
fig.savefig(os.path.join(GRAPHICS_DIR, eq_name + ".png"), format="png",
            transparent=True, bbox_inches="tight", pad_inches=0)
