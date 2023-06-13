import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import tikzplotlib
noiseFactor=pd.read_csv("data/noise-factor-db.csv")
fig, ax=plt.subplots(figsize=(8,6))
ax.plot(noiseFactor['NF dB10 X'], noiseFactor['NF dB10 Y'], linewidth=2, color="red")
ax.set_xlim(1.5e10, 4.5e10)
ax.set_ylim(0, 70)
ax.grid()
ax.set_xlabel("Frequency (GHz)", fontsize=15)
ax.set_ylabel("Noise Factor (db)", fontsize=15)
ax.tick_params(axis='both', labelsize=12)
new_xtick_labels = ['15', '20', '25', '30', '35', '40', '45']
ax.set_xticklabels(new_xtick_labels)
#tikzplotlib.clean_figure()
#tikzplotlib.save("noise-figure.tex")
#plt.savefig('noise-factor.png', dpi=300)
plt.show()