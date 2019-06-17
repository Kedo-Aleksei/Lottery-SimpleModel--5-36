import csv
import numpy as np
import pip
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib_colorbar as pltc

A = pd.read_csv('matrix.csv').values

plt.figure(figsize=(16, 16))
sns.heatmap(A, vmin=0, vmax=1, cmap = "CMRmap", center=None, robust=False, annot=None, fmt='.2g', annot_kws=None, linewidths=0, linecolor='white', cbar=True, cbar_ax=None, square=False, xticklabels=False, yticklabels=False, mask=None, ax=None)
plt.show()
