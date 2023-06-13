import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
df_id_gs1=pd.read_csv("data/id-vs-vds-parametric-gs1.csv")
df_id_gs1=df_id_gs1.iloc[:, [0, 1, 3, 5]]
df_id=df_id_gs1.rename(columns={'/V0/PLUS (Vgs1=0.9) X': "vds", 
                                '/V0/PLUS (Vgs1=0.9) Y': "vgs0.9", 
                               '/V0/PLUS (Vgs1=2.7) Y': "vgs2.7", 
                               '/V0/PLUS (Vgs1=1.8) Y': "vgs1.8"})
fig, ax=plt.subplots(figsize=(8,6))
ax.plot(df_id["vds"], df_id["vgs0.9"]*-1, label="$V_{G1-CS}=0.9 V$")
ax.plot(df_id["vds"], df_id["vgs1.8"]*-1, label="$V_{G1-CS}=1.8 V$")
#ax.plot(df_id["vds"], df_id["vgs2.7"]*-1, label="$V_{G1-CS}=2.7 V$")
ax.plot(3.6, 56.7575E-3, marker='o', markersize=5)

ax.annotate('(3.6V, 56.76mA)', xy=(3.6, 56.7575e-3), xytext=(3.2, 45E-3), arrowprops=dict(arrowstyle='->'))
ax.grid(True)
ax.set_xlabel(r"$V_{DD}$ (V)", fontsize=15)
ax.set_ylabel(r"$I_D$ (mA)", fontsize=15)
# Set the y-axis tick formatter
# Define the custom formatter function
def y_formatter(value, _):
    value *= 1000  # Multiply the value by 1000
    return f'{value:.1f}'  # Use decimal notation for larger values


# Set the custom formatter function for the y-axis ticks
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(y_formatter))
ax.tick_params(axis='both', labelsize=12)
plt.legend()
plt.savefig('id-vs-vds-parametric-gs1.png', dpi=300)
plt.show()
#above=undefined, below=0