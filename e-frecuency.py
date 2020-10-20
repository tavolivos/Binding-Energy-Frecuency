###################################
#  By: Gustavo E. Olivos-Ramirez  #
#      gustavo.olivos@upch.pe     #
#      Lima-Peru                  #
###################################

import subprocess
import os
import matplotlib.pyplot as pl
import pandas as pd
import numpy as np

font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 22}
pl.rc('font', **font)

labels = ['0', '', '1K', '', '2K', '', '3K', '', '4K']

df = pd.read_csv('energies.csv')

bins = [-9, -8, -7, -6, -5, -4, -3,]
names = ['[-8,-9]', '[-7,-8]', '[-6,-7]', '[-5,-6]', '[-4,-5]', '[-3,-4]']

df['Frecuency'] = pd.cut(df['BindingEnergy'], bins, labels = names)

fig = pl.figure(figsize=(13,6))
ax = fig.add_subplot()
fig.subplots_adjust(bottom=0.15, left=0.15)


df.Frecuency.value_counts(sort=False, normalize=False).plot(kind='barh', color='salmon')

barplot = df.Frecuency.value_counts(sort=False, normalize=False)

for i, v in enumerate(barplot):
    ax.text(v, i, str(v), color='black', fontweight='bold', size='14', va='center')

ax.set_xlabel("Number of ligands (per thousand)")
ax.set_ylabel("Binding Energy\n(kcal/mol)")
ax.set_xlim(0, 4000) 
ax.set_xticklabels(labels)
h, l = ax.get_legend_handles_labels()
ax.legend(l)
#ax.tick_params(direction='out', length=6, width=2, colors='r', grid_color='r', grid_alpha=0.5)

subprocess.call ('mkdir IMG-FREC', shell = True)

fig.savefig("IMG-FREC/e-frec.png", format='png', dpi=800, transparent=True)
fig.savefig("IMG-FREC/e-frec.svg", format='svg', dpi=800, transparent=True)
fig.savefig("IMG-FREC/e-frec.pdf", format='pdf', dpi=800, transparent=True)
fig.savefig("IMG-FREC/e-frec.tif", format='tif', dpi=800, transparent=True)

print("Enjoy your plots")
print("Great power brings great responsibility")
